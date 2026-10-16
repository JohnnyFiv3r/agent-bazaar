<p align="center">
  <img src="assets/brand/app-icon.png" width="112" alt="Agent Promise Protocol heart-shaped handshake logo">
</p>

# Agent Promise Protocol (APP)

**Emit intent. Make qualified promises. Agree on exact terms.**

Agent Promise Protocol lets agents express what they seek without turning that intent into an offer. Other agents respond with actions they are capable and authorized to promise. The parties negotiate, adopt the same exact terms, and preserve a protected opportunity for every represented principal to refuse.

APP is an A2A extension for commitments involving products, services, information, access or outcomes. Either participant can initiate an exchange. Applications define what an action means; APP governs who can promise it and how the parties agree to its terms.

<p>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-FFD88A?style=flat-square&amp;labelColor=C94B00"></a>
  <a href="pyproject.toml"><img alt="Python: 3.11+" src="https://img.shields.io/badge/Python-3.11%2B-FFD88A?style=flat-square&amp;labelColor=C94B00"></a>
  <a href="https://github.com/JohnnyFiv3r/agent-promise-protocol/releases/tag/app-v0.4-draft.1"><img alt="APP: 0.4 reference draft" src="https://img.shields.io/badge/APP-0.4%20reference%20draft-FFD88A?style=flat-square&amp;labelColor=C94B00"></a>
</p>

## How one agreement works

Consider an agent seeking a source-backed research report:

1. **Emit intent.** “I am seeking a report on this question.” Publication follows the principal's consent and contact policies. The emission promises the act of declaring or seeking, without committing to buy the report.
2. **Offer qualified actions.** A provider promises to produce the report under explicit conditions. That offer already issues the provider's conditional promise. Any requested action from the requester remains a request until that agent issues its own promise.
3. **Negotiate and adopt exact terms.** Agents can revise offers within declared interaction budgets. Both adopt the same immutable candidate, including their own actions, conditions and principal-refusal rules. The originator coordinates finalization.
4. **Protect principal refusal.** The accepted object begins with refusal windows pending. Every represented principal receives qualifying notice and a positive period in which to refuse.
5. **Check authority before action.** Agent agreement, principal clearance and downstream authorization are separate decisions. When the optional handoff feature is used, APP checks eligibility at the adapter boundary. Native systems perform the authorized action.

This example illustrates the flow; the [governing contracts](contracts/README.md) define the requirements. A signature establishes attribution, not capability or successful performance. Later observations and assessments remain separate from the original promise.

## Review the protocol

Start with the **[core model](contract.md)** for shared terms and the agreement flow, then use the **[contract index](contracts/README.md)** to inspect the rules. C1–C6 govern one bilateral agreement. C7 composes those agreements across more agents; C8 defines optional handoff and lifecycle evidence.

For the Promise Theory interpretation, read the **[review note](docs/review/promise-theory-correspondence.md)** and [worked research example](docs/review/worked-example.md). The [conceptual review package](docs/review/README.md) collects the questions for critique.

| Review question | Where to look |
|---|---|
| Does intent emission stay distinct from a service offer? Who can issue a promise? | [C2: Qualified actions](contracts/02-qualified-actions.md) |
| Who may publish or respond, and how is iterative negotiation bounded? | [C1: Publication and policy](contracts/01-publication-policy.md), [C3: Admission and negotiation](contracts/03-admission-negotiation.md) |
| What establishes exact agreement, and what rights does the principal retain? | [C4: Formation](contracts/04-formation.md), [C5: Principal refusal](contracts/05-principal-refusal.md) |
| How are records carried, verified and recovered? | [C6: A2A and evidence](contracts/06-a2a-evidence.md) |
| How do multiple agreements compose, and where does APP stop? | [C7: Composition](contracts/07-composition.md), [C8: Adapter boundary](contracts/08-adapter-boundary.md) |

## Scope and ownership

APP requires no central operator, discovery provider or APP-owned ledger. Participants can retain their own permitted signed evidence or delegate custody. Discovery, routing and offer aggregation are optional application services. Coordination and other authority remain explicitly scoped; storing a record grants no authority over its issuer.

The core supports independent hosting. The **current reference runtime uses one delegated authority realm and a shared SQLite ledger**. [RP1](profiles/reference-profile.md) selects a common conflict authority; the [deployment model](deployment-model.md) explains its scope. The [independent-participant runtime slice](design/independent-participant-slice.md) remains design work.

Applications supply shared action meanings, capability evidence, principal-approved permissions and usable notice/refusal channels. APP does not maintain a product taxonomy. AP2/UCP/ACP order validation, native execution, payment and settlement stay downstream. No live integration with those systems has been qualified.

## Try the reference runtime

With Python 3.11 or newer and [uv](https://docs.astral.sh/uv/) installed:

```sh
git clone https://github.com/JohnnyFiv3r/agent-promise-protocol.git
cd agent-promise-protocol
uv sync --locked --extra dev
uv run --locked agent-promise-protocol review-demo
```

The review demo follows a bilateral research agreement, then records a provider inability report and a separate requester assessment without rewriting the promise. It writes a portable signed trace and readable summary into a fresh temporary directory. Use `--directory PATH` to select a fresh, empty directory.

For principal refusal, restart recovery, three-agent composition and a guarded fake-adapter handoff:

```sh
uv run --locked agent-promise-protocol demo
```

**Both demos are controlled simulations.** Signatures, content digests, schema checks and SQLite transactions are real. Policies, capability evidence, time and peer identities are controlled fixtures; the native adapter is a deterministic fake. The demos make no network calls, real service requests, orders or payments, and do not demonstrate independent implementations or autonomous model reasoning.

To build a participant, follow the [implementer guide](docs/implementer-guide.md), [runtime guide](docs/runtime.md) and [application/harness interface](profiles/harness-interface.md). The machine-readable surfaces are the [semantic records](schemas/contract.schema.json), [interaction envelopes](schemas/interaction.schema.json) and [admission declaration](schemas/admission-policy.schema.json).

## Status and validation

APP is a **0.4 reference draft** with a **0.1 Python reference runtime**. The [fixed reference release](https://github.com/JohnnyFiv3r/agent-promise-protocol/releases/tag/app-v0.4-draft.1) includes source, packages, a verification report and checksums. The current checkout also includes the subsequent review package and `review-demo`. [Release metadata](release.json) identifies the versions and normative sources.

Run the local checks:

```sh
uv run --locked --extra dev python -m pytest tests/runtime -q -ra
uv run --locked --extra dev python checks/validate.py
```

[Validation](validation.md) separates executed checks from [proposed assessment scenarios](tests/PROPOSED.md) and gives setup for the mTLS and OPA integration checks. Passing reference tests does not establish full deployment [conformance](conformance.md) or independent interoperability. Production time, principal inbox operation, registry distribution and failover fencing remain integration work; see the [current runtime limits](docs/runtime.md#current-limits).

Protocol/profile identifiers and adopted content are pinned. Mutable documentation URLs do not authorize reinterpretation of existing agreements. The [namespace transition](docs/namespace-transition.md) records the earlier ABP-to-APP change. See [current decisions](decisions-v0.4.md), the [changelog](CHANGELOG.md), [contribution guidance](CONTRIBUTING.md) and [release process](RELEASING.md) for changes and compatibility.

## License and provenance

The specification, schemas, reference runtime and examples are [MIT licensed](LICENSE). Dependencies are declared in [pyproject.toml](pyproject.toml) and pinned in [uv.lock](uv.lock). Related projects provide [research and inspiration](research/README.md); comparator implementation code and imported test suites are not used.
