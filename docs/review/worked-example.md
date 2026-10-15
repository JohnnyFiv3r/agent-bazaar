# Worked example: a conditional research promise and a later inability report

This example demonstrates one bilateral interaction through the reference runtime. A requester seeks a source-backed report; a provider issues its own conditional promise; both adopt the same exact terms. Later the provider reports that it cannot currently perform, and the requester records a separate assessment. APP preserves the original commitment and the authorship of each later statement.

Run from a checkout with the locked runtime dependencies installed:

```sh
uv run --locked --extra dev agent-promise-protocol review-demo --directory /tmp/app-review-example
```

Use a fresh, empty output directory. The command prints JSON and saves:

- `summary.md`: a short walkthrough.
- `summary.json`: outcomes and exact references to the named records.
- `signed-trace.json`: portable objects, proof wrappers and fixture public keys.
- `authority/authority.sqlite`: the local reference authority's durable state.

This is a controlled simulation using distinct participant keys within **one implementation and one shared authority ledger**. The reusable fixture also enrolls unused supporting identities; only requester and researcher negotiate this agreement. No LLM, independent participant implementation, discovery service, source retrieval, actual research, native execution or payment is involved. Keys and operation IDs are freshly generated, so different runs produce different digests.

## Read the trace

The `records` map in each JSON artifact names the relevant objects by exact content reference. Resolve those references in `signed-trace.json`'s `objects` array.

| Step | Record names | What the example establishes |
| --- | --- | --- |
| Attribution without qualification | `unqualified_assertion`, `qualification_denial` | A genuine provider signature authenticates an assertion with unapproved capability evidence. The harness refuses to admit it as a qualified promise. |
| Intent | `intent` | The requester promises only to disclose its interest. It does not promise to produce the requested report or buy anything. |
| Conditional offer | `provider_offer` | The provider promises one source-backed report, subject to current source access and principal clearance before performance. Future clearance is not presumed at issuance. |
| Exact adoption | `candidate`, `requester_adoption`, `provider_adoption`, `accepted` | Both parties sign the same candidate reference. Only the provider adopts the report promise; the requester's adopted own-promise list is empty. The original issuer records finalization. |
| Principal recovery | `status_after_formation`, `status_after_recovery_window` | Formation initially has pending refusal windows. Simulated notices, healthy review time and current authority close those windows separately. |
| Performer observation | `provider_inability` | The provider reports simulated loss of source access under its own signature. The `fulfillment` category does not imply successful delivery. |
| Requester assessment | `requester_assessment`, `assessment_receipt` | The requester assesses `delivery_not_established`, explicitly relying on that admitted provider report. The receipt confirms admission of the assessment, not the truth of a completed delivery. |
| Preserved history | `status_after_observations` | The original offer, candidate and accepted object retain their exact bytes. Recovery remains closed; that status does not answer whether the report was delivered. |

The action's immutable `semantics_ref` pins the test definition, conditional phases, reporter roles and assessment rule before adoption. The rule permits the performer to report inability for the exact accepted action and occurrence. It permits the requester to assess delivery as unestablished on that report alone. A provider cannot use its own signature to supply the requester's assessment, and evidence for a different occurrence is rejected.

There is no invented deadline or generic `broken` agreement state. Loss of source access does not by itself prove breach. No withdrawal, cancellation, resource release or replacement is performed. The observation and the assessment remain distinct statements; neither rewrites the promise. Domain definitions, evidence quality and real-world assessment remain the participants' responsibility.

## Verify the portable evidence

The JSON trace contains public verification keys, never private signing keys. From the checkout, this performs an offline content and signature check without opening the SQLite ledger:

```sh
uv run --locked python - /tmp/app-review-example/signed-trace.json <<'PY'
import json
import sys
from agent_promise_protocol.review_demo import verify_trace

with open(sys.argv[1]) as source:
    print(json.dumps(verify_trace(json.load(source)), indent=2))
PY
```

This verifies content integrity, requires every embedded content reference to resolve to exact bytes within the bundle, and authenticates every named walkthrough record relative to the keys declared by the fixture. Missing or empty proofs fail verification; deleting proof fields cannot downgrade a named record into an unsigned supporting document. It is not an external identity certification, semantic replay, independent interoperability test or proof of real-world capability. The scenario tests separately exercise qualification rejection, exact adoption, reporter separation, immutable provenance, replay and the performance condition.

The example stops before the adapter boundary: **zero prepare, dispatch or reconcile calls**. The existing boundary contracts remain responsible for handoff eligibility; downstream validation, fulfillment, payment and settlement are not implemented here.
