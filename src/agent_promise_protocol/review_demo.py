"""One signed, controlled example for semantic review; no native execution.

The two participants use distinct keys but one implementation and authority.
The domain predicates below are explicitly selected TEST rules, not APP rules.
"""

import json
from pathlib import Path

from .crypto import Registry, canonical, check_ref, content_ref
from .domain import ActionMeaning
from .errors import ProtocolError
from .fixtures import Environment, U
from .guards import timestamp
from .records import ref_key


REVIEW = U + "review-v1:"
CONDITION = REVIEW + "clearance-and-source-access"
INABILITY = REVIEW + "provider-inability"
ASSESSMENT = REVIEW + "delivery-not-established"
EVIDENCE = REVIEW + "evidence"
REPORT = "source-backed-research-review"


class ReviewEnvironment(Environment):
    """Narrow local domain: a report, source access, and a bounded assessment."""

    def __init__(self, directory):
        super().__init__(directory)
        self.sources_available = True
        self.principals_cleared = False
        self.semantics_ref = self.document(
            "review-semantics-v1",
            {
                "actions": {
                    "declare_interest": "Disclose interest only; no purchase or report commitment.",
                    "produce_report": "Produce one report comparing two fictional sources, with claim-to-source citations.",
                },
                "condition_type": CONDITION,
                "conditions": {
                    "issuance_adoption_finalization": "The condition is understood; current source access is available in the fixture. Future principal clearance is not claimed.",
                    "performance": "Principal clearance and source access must both be current.",
                },
                "evidence_profile_uri": EVIDENCE,
                "evidence_rules": {
                    "freshness": "At admission, observed_at must equal the controlled clock; the required source object must resolve exactly.",
                    "finality": "Admission records attribution and rule acceptance only. Neither claim establishes a final agreement outcome.",
                    "correction": "Later observations require new authenticated records. Earlier records are retained; no supersession or contradiction resolution is demonstrated.",
                },
                "provider_report": {
                    "issuer": "agent:researcher",
                    "claim_type": INABILITY,
                    "meaning": "The performer reports lost source access and inability to deliver at the observation time. This is attributable self-report, not external verification.",
                },
                "requester_assessment": {
                    "issuer": "agent:requester",
                    "claim_type": ASSESSMENT,
                    "rule": "On an admitted provider-inability record for this exact action and occurrence, the requester records delivery_not_established on that report alone.",
                    "limits": "No deadline, universal breach, cancellation, capacity release, independent verification, or terminal agreement state is inferred.",
                },
            },
        )
        for action_name in ("declare_interest", "produce_report"):
            self.domain.actions[U + action_name] = ActionMeaning(
                self.semantics_ref, self._valid_action, self._valid_occurrence
            )
        self.domain.understood_uris.update({CONDITION, INABILITY, ASSESSMENT})
        self.domain.qualification_checks[CONDITION] = self._qualified
        self.domain.evidence_checks[EVIDENCE] = self._evidence

    def _qualified(self, promise, stage):
        return (
            promise["qualifications"] == [self.condition()]
            and self.sources_available
            and (stage != "performance" or self.principals_cleared)
        )

    def condition(self):
        return {
            "type_uri": CONDITION,
            "parameters": {"definition_ref": self.semantics_ref},
        }

    def promise(self, actor, other, name, action_name):
        result = super().promise(actor, other, name, action_name)
        if action_name == "produce_report":
            result["qualifications"] = [self.condition()]
            result["action"]["parameters"]["scope"] = (
                "Compare two fictional sources and cite each material claim."
            )
        return result

    def intent(self, name):
        result = self.emit(
            "requester",
            "intent",
            {
                "intent_id": "intent:" + name,
                "revision": 1,
                "previous_digest": None,
                "market_posture": "seek_result",
                "topic": "source-backed research",
                "desired_outcome": "One report comparing two fictional sources, with citations for material claims; simulation only.",
                "preferences": ["Attributable evidence", "Explicit uncertainty"],
                "disclosure_audience": ["fixture:research"],
                "publication_contract_ref": content_ref(self.publications["requester"]),
                "validity": self.validity("requester"),
                "emission_promise": self.promise(
                    "requester", "researcher", name + ":interest", "declare_interest"
                ),
            },
            identifier="intent:" + name,
        )
        self.require_applied(
            self.invoke("requester", "requester", "submit_record", result)
        )
        return result

    def _evidence(self, record, accepted):
        if accepted.get("kind") != "accepted_offer":
            return False
        body = record["body"]
        candidate = self.store.resolve(accepted["body"]["candidate_ref"])
        promise = candidate["body"]["own_promises"][0]
        actor = record["issuer_agent_id"]
        claim = body["claim"]
        if (
            body["agreement_ref"] != content_ref(accepted)
            or body["action_ref"]
            != {
                "promiser_agent_id": promise["promiser_agent_id"],
                "promise_id": promise["promise_id"],
            }
            or body["action_instance"]
            != {
                "type_uri": U + "one-report",
                "parameters": {"report_id": REPORT, "ordinal": 1},
            }
            or promise["action"]["semantics_ref"] != self.semantics_ref
            or body["observed_at"] != timestamp(self.clock.now_ms)
            or len(body["native_evidence_refs"]) != 1
        ):
            return False
        evidence = self.store.resolve(body["native_evidence_refs"][0])
        if claim["type_uri"] == INABILITY:
            return (
                actor == "agent:researcher"
                and body["category"] == "fulfillment"
                and body["reporter_role"] == "performer"
                and body["authority_refs"] == [self.principal_policies["researcher"]]
                and claim["parameters"]
                == {
                    "reason": "source_access_lost",
                    "definition_ref": self.semantics_ref,
                }
                and evidence
                == {
                    "id": "fixture:source-access-lost",
                    "test_only": True,
                    "agreement_ref": content_ref(accepted),
                    "observed_at": body["observed_at"],
                    "source_access_available": False,
                    "real_world_observation": False,
                }
                and not self.sources_available
            )
        return (
            claim["type_uri"] == ASSESSMENT
            and actor == "agent:requester"
            and body["category"] == "assessment"
            and body["reporter_role"] == "assessor"
            and body["authority_refs"] == [self.principal_policies["requester"]]
            and claim["parameters"]
            == {
                "result": "delivery_not_established",
                "definition_ref": self.semantics_ref,
            }
            and self.store.is_admitted(content_ref(evidence))
            and evidence.get("kind") == "lifecycle_evidence"
            and evidence["issuer_agent_id"] == "agent:researcher"
            and evidence["body"]["claim"]["type_uri"] == INABILITY
            and all(
                evidence["body"][field] == body[field]
                for field in ("agreement_ref", "action_ref", "action_instance")
            )
        )


def build_review_scenario(env):
    """Exercise protocol transitions; leave evidence inspectable to tests/callers."""
    named = {}
    unqualified = env.promise(
        "researcher", "requester", "unqualified", "produce_report"
    )
    unqualified["capability_refs"] = [
        env.document("unapproved-capability", {"claim": "I can produce a report"})
    ]
    named["unqualified_assertion"] = env.emit(
        "researcher",
        "promise",
        {
            "publication_contract_ref": content_ref(env.publications["researcher"]),
            "own_promise": unqualified,
        },
    )
    env.registry.verify(
        named["unqualified_assertion"], env.store.resolve, env.clock.now_ms
    )
    named["qualification_denial"] = env.invoke(
        "researcher", "requester", "submit_record", named["unqualified_assertion"]
    )
    agreement = env.bilateral(REPORT)
    named.update({key: agreement[key] for key in ("intent", "candidate", "accepted")})
    named["provider_offer"] = agreement["offers"][0]
    named["requester_adoption"], named["provider_adoption"] = agreement["adoptions"]
    originals = {
        key: canonical(named[key])
        for key in ("provider_offer", "candidate", "accepted")
    }
    named["status_after_formation"] = env.status(named["accepted"])
    env.notify(named["accepted"])
    env.advance_healthy(named["accepted"])
    named["status_after_recovery_window"] = env.status(named["accepted"])
    env.principals_cleared = (
        named["status_after_recovery_window"]["body"]["status"]
        == "refusal_windows_closed"
    )

    # This is a controlled change in the fixture, never a service call or withdrawal.
    env.sources_available = False
    observation_ref = env.document(
        "source-access-lost",
        {
            "agreement_ref": content_ref(named["accepted"]),
            "observed_at": timestamp(env.clock.now_ms),
            "source_access_available": False,
            "real_world_observation": False,
        },
    )
    promise = named["candidate"]["body"]["own_promises"][0]
    base = {
        "agreement_ref": content_ref(named["accepted"]),
        "action_ref": {
            "promiser_agent_id": promise["promiser_agent_id"],
            "promise_id": promise["promise_id"],
        },
        "action_instance": {
            "type_uri": U + "one-report",
            "parameters": {"report_id": REPORT, "ordinal": 1},
        },
        "evidence_profile_uri": EVIDENCE,
        "observed_at": timestamp(env.clock.now_ms),
    }
    named["provider_inability"] = env.emit(
        "researcher",
        "lifecycle_evidence",
        {
            **base,
            "category": "fulfillment",
            "reporter_role": "performer",
            "claim": {
                "type_uri": INABILITY,
                "parameters": {
                    "reason": "source_access_lost",
                    "definition_ref": env.semantics_ref,
                },
            },
            "native_evidence_refs": [observation_ref],
            "authority_refs": [env.principal_policies["researcher"]],
        },
    )
    env.require_applied(
        env.invoke(
            "researcher", "requester", "submit_record", named["provider_inability"]
        )
    )
    named["requester_assessment"] = env.emit(
        "requester",
        "lifecycle_evidence",
        {
            **base,
            "category": "assessment",
            "reporter_role": "assessor",
            "claim": {
                "type_uri": ASSESSMENT,
                "parameters": {
                    "result": "delivery_not_established",
                    "definition_ref": env.semantics_ref,
                },
            },
            "native_evidence_refs": [content_ref(named["provider_inability"])],
            "authority_refs": [env.principal_policies["requester"]],
        },
    )
    named["assessment_receipt"] = env.invoke(
        "requester", "requester", "submit_record", named["requester_assessment"]
    )
    env.require_applied(named["assessment_receipt"])
    replay = env.deliver(env.last_request)
    named["status_after_observations"] = env.status(named["accepted"])
    unchanged = all(
        canonical(env.store.resolve(content_ref(named[key]))) == value
        for key, value in originals.items()
    )
    return named, {
        "mode": "controlled simulation; one implementation and one shared authority ledger",
        "participants": ["agent:requester", "agent:researcher"],
        "qualification_denial": named["qualification_denial"]["body"]["reason_code"],
        "formation_status": named["status_after_formation"]["body"]["status"],
        "principal_recovery_status": named["status_after_recovery_window"]["body"][
            "status"
        ],
        "provider_report": "source_access_lost",
        "requester_assessment": "delivery_not_established",
        "status_after_observations": named["status_after_observations"]["body"][
            "status"
        ],
        "original_commitment_records_unchanged": unchanged,
        "assessment_replay_same_receipt": content_ref(replay)
        == content_ref(named["assessment_receipt"]),
        "native_adapter_calls": {
            "prepare": env.adapter.prepare_calls,
            "dispatch": env.adapter.dispatch_calls,
            "reconcile": env.adapter.reconcile_calls,
        },
        "real_research_execution_or_payment": False,
        "limits": [
            "Fixture capability evidence is not real researcher qualification.",
            "The requester assessment relies on provider self-report, not independent validation.",
            "Recovery status is not fulfillment, breach, cancellation, or payment status.",
            "Exported keys establish only this fixture's self-consistency; they are not an external trust root.",
        ],
        "records": {name: content_ref(record) for name, record in named.items()},
    }


def verify_trace(trace):
    """Check content and signatures against the bundle's TEST-ONLY public keys.

    This is an offline integrity check, not semantic replay or external identity
    certification. No private keys or SQLite state are needed.
    """
    registry = Registry()
    for identity in trace["fixture_public_identities"]:
        registry.enroll(**identity)
    objects = {}
    for item in trace["objects"]:
        check_ref(item["ref"], item["value"])
        objects[ref_key(item["ref"])] = item["value"]

    def resolve(ref):
        try:
            return objects[ref_key(ref)]
        except KeyError as exc:
            raise ProtocolError(
                "evidence_unavailable", "trace content reference is unresolved"
            ) from exc

    def check_references(value):
        if isinstance(value, dict):
            if {"id", "digest"} <= value.keys() <= {"id", "digest", "locator"}:
                check_ref(value, resolve(value))
            for child in value.values():
                check_references(child)
        elif isinstance(value, list):
            for child in value:
                check_references(child)

    verified = set()
    for key, record in objects.items():
        # Classify signed APP content independently of a supplied proof.
        # Deleting/emptying proofs must not turn a protocol record into an
        # unsigned supporting document that escapes authentication.
        if any(
            field in record
            for field in ("kind", "profile", "issuer_agent_id", "proofs")
        ):
            registry.verify(record, resolve, trace["verification_time_ms"])
            verified.add(key)
    for reference in trace["records"].values():
        record = resolve(reference)
        check_ref(reference, record)
        key = ref_key(reference)
        if key not in verified:
            # Named walkthrough records must authenticate even if an attacker
            # also strips their protocol-identifying fields.
            registry.verify(record, resolve, trace["verification_time_ms"])
            verified.add(key)
    # Check the exact references embedded in both signed records and supporting
    # documents. A valid wrapper hash cannot replace bytes pinned by a signer.
    # This traverses JSON content only; it neither fetches nor interprets terms.
    for record in objects.values():
        check_references(record)
    return {
        "content_objects": len(objects),
        "signed_records_verified": len(verified),
        "named_records_authenticated": len(trace["records"]),
        "trust_basis": "public identities declared by this controlled fixture",
    }


def run_review_demo(directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    if any(directory.iterdir()):
        raise FileExistsError("Use a fresh, empty review output directory")
    env = ReviewEnvironment(directory / "authority")
    try:
        _, summary = build_review_scenario(env)
        trace = {
            "format": "app-controlled-review-trace/1",
            "verification_time_ms": env.clock.now_ms,
            "fixture_public_identities": [
                {
                    "agent_id": signer.agent_id,
                    "principal_id": signer.principal_id,
                    "public_jwk": signer.public_jwk(),
                    "features": env.registry.identities[signer.agent_id]["features"],
                }
                for signer in env.signers.values()
            ],
            "records": summary["records"],
            "objects": [
                {"ref": content_ref(record), "value": record}
                for _, record in env.ledger.items("objects")
            ],
        }
        summary["offline_integrity"] = verify_trace(trace)
        summary["output_directory"] = str(directory.resolve())
        summary["artifacts"] = {
            "trace": "signed-trace.json",
            "summary": "summary.json",
            "walkthrough": "summary.md",
            "ledger": "authority/authority.sqlite",
        }
        for filename, value in (
            ("signed-trace.json", trace),
            ("summary.json", summary),
        ):
            (directory / filename).write_text(json.dumps(value, indent=2) + "\n")
        (directory / "summary.md").write_text(
            "# APP controlled review example\n\n"
            "1. A signed provider assertion with unapproved capability evidence is rejected.\n"
            "2. The requester declares interest; the provider issues its own conditional report offer.\n"
            "3. Both sign adoption of the same exact terms; only the provider adopts a report promise.\n"
            "4. Formation starts a separate principal recovery period; simulated notice and healthy time close it.\n"
            "5. The provider reports lost source access. The requester separately assesses delivery_not_established.\n"
            "6. Original commitments remain unchanged. Recovery status stays closed, without implying delivery.\n\n"
            "No native adapter calls, research, execution, payments, or independent participant implementation occur. "
            "The two participants use different signing keys within one controlled implementation and shared ledger. "
            "The assessment depends on self-report; it declares no universal breach or cancellation.\n\n"
            "See summary.json for exact record references and signed-trace.json for public keys, proofs and content. "
            "Public keys in this trace are fixture declarations, not an external trust root.\n"
        )
        return summary
    finally:
        env.close()
