"""The review example distinguishes attribution, qualification and assessment."""

from copy import deepcopy
import json

import pytest

from agent_promise_protocol.crypto import content_ref
from agent_promise_protocol.demo import main
from agent_promise_protocol.errors import ProtocolError
from agent_promise_protocol.fixtures import U
from agent_promise_protocol.review_demo import (
    ASSESSMENT,
    INABILITY,
    ReviewEnvironment,
    build_review_scenario,
    run_review_demo,
    verify_trace,
)


@pytest.fixture
def scenario(tmp_path):
    env = ReviewEnvironment(tmp_path / "authority")
    try:
        named, summary = build_review_scenario(env)
        yield env, named, summary
    finally:
        env.close()


def test_authenticated_assertion_is_not_qualification_and_adoption_is_exact(scenario):
    env, records, _ = scenario
    unqualified = records["unqualified_assertion"]
    env.registry.verify(unqualified, env.store.resolve, env.clock.now_ms)
    assert not env.store.is_admitted(content_ref(unqualified))
    assert records["qualification_denial"]["body"]["reason_code"] == "authority_absent"
    intent_action = records["intent"]["body"]["emission_promise"]["action"][
        "action_type"
    ]
    assert intent_action == U + "declare_interest"
    requester, provider = records["requester_adoption"], records["provider_adoption"]
    assert requester["issuer_agent_id"] == "agent:requester"
    assert provider["issuer_agent_id"] == "agent:researcher"
    assert (
        requester["proofs"][0]["verification_method"]
        != provider["proofs"][0]["verification_method"]
    )
    assert requester["body"]["adopted_own_promise_ids"] == []
    promise = records["provider_offer"]["body"]["own_promises"][0]
    assert promise["promiser_agent_id"] == "agent:researcher"
    assert promise["qualifications"]
    assert provider["body"]["adopted_own_promise_ids"] == [promise["promise_id"]]
    candidate_ref = content_ref(records["candidate"])
    assert (
        requester["body"]["candidate_ref"]
        == provider["body"]["candidate_ref"]
        == candidate_ref
    )
    assert records["accepted"]["body"]["candidate_ref"] == candidate_ref


def test_assessment_preserves_originals_and_does_not_become_clearance_or_execution(
    scenario,
):
    env, records, summary = scenario
    assert summary["formation_status"] == "pending_refusal_windows"
    assert (
        summary["principal_recovery_status"]
        == summary["status_after_observations"]
        == "refusal_windows_closed"
    )
    assert summary["native_adapter_calls"] == {
        "prepare": 0,
        "dispatch": 0,
        "reconcile": 0,
    }
    assert env.ledger.items("handoff_slots") == []
    assert summary["original_commitment_records_unchanged"]
    assert summary["assessment_replay_same_receipt"]
    for name in ("provider_offer", "candidate", "accepted"):
        original = records[name]
        assert env.store.resolve(content_ref(original)) == original
        env.registry.verify(original, env.store.resolve, env.clock.now_ms)
    observation, assessment = (
        records["provider_inability"],
        records["requester_assessment"],
    )
    assert observation["body"]["claim"]["type_uri"] == INABILITY
    assert assessment["body"]["claim"]["type_uri"] == ASSESSMENT
    assert assessment["body"]["native_evidence_refs"] == [content_ref(observation)]
    assert assessment["issuer_agent_id"] != observation["issuer_agent_id"]
    assert records["assessment_receipt"]["body"]["outcome"] == "applied"


def test_provider_cannot_promote_self_report_into_requester_assessment(scenario):
    env, records, _ = scenario
    body = deepcopy(records["requester_assessment"]["body"])
    body["authority_refs"] = [env.principal_policies["researcher"]]
    claimed = env.emit("researcher", "lifecycle_evidence", body)
    env.registry.verify(claimed, env.store.resolve, env.clock.now_ms)
    receipt = env.invoke("researcher", "requester", "submit_record", claimed)
    assert receipt["body"]["outcome"] == "blocked"
    assert receipt["body"]["reason_code"] == "unsupported_semantics"
    assert not env.store.is_admitted(content_ref(claimed))


@pytest.mark.parametrize(
    "substitution", ["different_occurrence", "intent_as_agreement"]
)
def test_assessment_cannot_apply_provider_evidence_to_a_different_subject(
    scenario, substitution
):
    env, records, _ = scenario
    body = deepcopy(records["requester_assessment"]["body"])
    if substitution == "different_occurrence":
        body["action_instance"]["parameters"]["ordinal"] = 2
    else:
        body["agreement_ref"] = content_ref(records["intent"])
    claimed = env.emit("requester", "lifecycle_evidence", body)
    receipt = env.invoke("requester", "requester", "submit_record", claimed)
    assert receipt["body"]["outcome"] == "blocked"
    assert not env.store.is_admitted(content_ref(claimed))


def test_known_loss_of_source_access_blocks_performance_even_after_clearance(scenario):
    env, records, _ = scenario
    promise = records["provider_offer"]["body"]["own_promises"][0]
    assert env.principals_cleared
    with pytest.raises(ProtocolError, match="qualification"):
        env.harnesses["requester"].guards.own_promise(promise, stage="performance")
    env.sources_available = True
    env.harnesses["requester"].guards.own_promise(promise, stage="performance")
    env.principals_cleared = False
    with pytest.raises(ProtocolError, match="qualification"):
        env.harnesses["requester"].guards.own_promise(promise, stage="performance")


def test_portable_trace_verifies_without_ledger_and_detects_rehashed_tampering(
    tmp_path,
):
    summary = run_review_demo(tmp_path / "review")
    trace = json.loads((tmp_path / "review" / "signed-trace.json").read_text())
    assert verify_trace(trace) == summary["offline_integrity"]
    assert all(
        "d" not in identity["public_jwk"]
        for identity in trace["fixture_public_identities"]
    )
    # Rehash the object to bypass its content check; its original signature must still fail.
    altered = deepcopy(trace)
    item = next(
        item
        for item in altered["objects"]
        if item["ref"] == trace["records"]["provider_offer"]
    )
    item["value"]["body"]["own_promises"][0]["action"]["parameters"]["scope"] = (
        "Altered terms"
    )
    item["ref"] = content_ref(item["value"])
    with pytest.raises(ProtocolError):
        verify_trace(altered)


@pytest.mark.parametrize(
    "mutation", ["remove_proofs", "empty_proofs", "strip_protocol_fields"]
)
def test_portable_trace_cannot_downgrade_named_record_to_unsigned_document(
    tmp_path, mutation
):
    run_review_demo(tmp_path / "review")
    trace = json.loads((tmp_path / "review" / "signed-trace.json").read_text())
    assert verify_trace(trace)["named_records_authenticated"] == len(trace["records"])
    item = next(
        item
        for item in trace["objects"]
        if item["ref"] == trace["records"]["provider_offer"]
    )
    if mutation == "empty_proofs":
        item["value"]["proofs"] = []
    else:
        item["value"].pop("proofs")
    if mutation == "strip_protocol_fields":
        for field in ("kind", "profile", "issuer_agent_id"):
            item["value"].pop(field)
    # Both the object wrapper and its walkthrough reference are attacker data.
    # Matching rehashed content still cannot substitute for authentication.
    item["ref"] = content_ref(item["value"])
    trace["records"]["provider_offer"] = item["ref"]
    with pytest.raises(ProtocolError):
        verify_trace(trace)


def test_review_cli_writes_readable_summary_and_refuses_to_overwrite(tmp_path, capsys):
    directory = tmp_path / "review"
    assert main(["review-demo", "--directory", str(directory)]) == 0
    summary = json.loads(capsys.readouterr().out)
    assert json.loads((directory / "summary.json").read_text()) == summary
    assert "delivery_not_established" in (directory / "summary.md").read_text()
    with pytest.raises(FileExistsError):
        run_review_demo(directory)
