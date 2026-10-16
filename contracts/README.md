# Agent-governing contracts

**APP 0.4 · normative · MIT**

The default is **one bilateral agreement**. An agent emits intent or initiates with an offer. Each party promises only its own qualified actions. Both adopt the same exact candidate, the originator records finalization, and every represented principal retains a protected opportunity to refuse.

These eight contracts define one agreement model. C1–C6 govern the baseline. C7 and C8 add explicitly negotiated features over that same model. A conforming harness verifies applicable requirements and preserves recoverable outcomes; it cannot grant itself authority, manufacture capability, or compel an autonomous agent to perform.

## Reading path

Start with the [core model and glossary](../contract.md#reading-the-core-model). Read C1–C5 in order to follow publication through agreement and principal refusal, then C6 for A2A carriage and evidence verification. C7 and C8 apply when their features are selected. The introductory “Reading this contract” sections are informative; numbered requirements govern conformance.

Each contract answers a different question about the same interaction:

| Contract | Applies to | Question it answers |
|---|---|---|
| [C1: Publication and policy](01-publication-policy.md) | Baseline | Who may publish what, to whom, and who may respond? |
| [C2: Qualified actions](02-qualified-actions.md) | Baseline | What is being promised, who can promise it, and what evidence qualifies that act? |
| [C3: Admission and negotiation](03-admission-negotiation.md) | Baseline | How do offers, revisions and retries stay within consent and interaction budgets? |
| [C4: Exact formation](04-formation.md) | Baseline | How do two adoptions become one recoverable, immutable agreement? |
| [C5: Principal refusal](05-principal-refusal.md) | Baseline | How are principals notified, allowed to refuse, and protected when status is uncertain? |
| [C6: A2A and portable proof](06-a2a-evidence.md) | Baseline and selected features | How are operations carried and exact records verified or recovered? |
| [C7: Composition](07-composition.md) | Optional `composition` | How do separate bilateral agreements participate in a plan with explicit dependencies? |
| [C8: Adapter boundary and lifecycle evidence](08-adapter-boundary.md) | Optional `adapter-handoff` and `lifecycle-evidence` | When may an action be handed off, and what does returned evidence establish? |

The [deployment model](../deployment-model.md) separates participant-owned journals from scoped coordination, resource and status authority. The core requires no network operator or shared database. RP1's common conflict authority is an explicit profile constraint.

## One complete default path

[RP1](../profiles/reference-profile.md) selects the concrete verification, policy, ordering, retrieval, and notice mechanisms. Its default `supported_features` is `["bilateral"]`. Applications supply the capability's meaning, principal-approved permissions, truthful constraints/capacity, and relevant application and notice hooks. The [harness interface](../profiles/harness-interface.md) assigns protocol mechanics to the reusable harness.

The [Python reference runtime](../docs/runtime.md) exercises these contracts in controlled scenarios using a shared SQLite ledger. Its [validation results](../validation.md) identify what has been executed; the profile and interface documents alone are not implementation or deployment evidence.

`composition`, `adapter-handoff`, and `lifecycle-evidence` are separate advertised features. `adapter-handoff` requires `lifecycle-evidence`; neither requires composition. Required features and semantics must be understood and accepted by every affected participant. Unsupported required meaning blocks the affected act instead of being approximated. Schema availability does not activate a feature.

Baseline portable proofs and current authority/status evidence remain mandatory. The optional `lifecycle-evidence` feature concerns downstream typed observations; it does not make core signature, delegation, or principal-recovery verification optional.

## Reading and authority

The [core contract](../contract.md) supplies shared semantics. [Current decisions](../decisions-v0.4.md) explicitly reconcile lifecycle scope and proposed testing with the [earlier decisions](../decisions-v0.2.md). C1–C8 provide the applicable normative requirements; advanced features do not create additional categories of agreement.

`MUST` and `MUST NOT` are requirements. `SHOULD` permits a documented exception preserving every `MUST`. `MAY` identifies an allowed choice. Conformance is to the selected version, negotiated features, and understood profiles. Schema validity alone does not establish cross-record correctness, authority, current status, or ordering.

## Machine-readable surfaces

- [Semantic records](../schemas/contract.schema.json): baseline publication through accepted-object recovery, plus feature-scoped composition, handoff, and lifecycle evidence.
- [Interaction requests and receipts](../schemas/interaction.schema.json): explicit recipient, admission basis, stable operation identity, and attributable processing outcome. The bilateral path uses `submit_record`, `finalize_candidate`, and `query_status`.
- [Admission declaration](../schemas/admission-policy.schema.json): shared accounting scope, eligibility, finite policy-selected allowances, replenishment, and protected control traffic.

These are interoperability surfaces, not a requirement to create a separate service for every contract. Existing identity, delegation, proof, policy, storage, and clock mechanisms retain their native responsibilities. Continuing permission is not a standing promise.

## Boundary and status

**Agent agreement, principal clearance, and downstream authorization remain separate.** Positive principal-recovery periods and usable refusal paths are universal. Optional handoff does not waive them; RP1 holds externally effective dispatch until relevant periods clear and current native authority is established.

APP governs exact commitments, optional composition, the selected adapter boundary, and interpretation of attributed evidence. Native systems perform execution, commerce validation, payments, fulfillment, assessment, and settlement. The reference runtime supplies a deterministic fake adapter; no live native integration has been qualified.

[Worked examples](../examples/lifecycle-walkthroughs.md) are schematic. [Proposed tests](../tests/PROPOSED.md) stop at controlled adapter substitutes and injected evidence. The specification, profile, and proposed checks are not executed runtime-conformance or native-transaction evidence.
