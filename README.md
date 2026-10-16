<p align="center">
  <img src="assets/brand/app-icon.png" width="112" alt="Agent Promise Protocol heart-shaped handshake logo">
</p>

# Agent Promise Protocol (APP)

**Emit intent. Make qualified promises. Agree on exact terms.**

Agent Promise Protocol lets agents express what they seek without turning that intent into an offer. Other agents can respond with actions they are capable and authorized to promise. The parties negotiate, adopt the same exact terms, and preserve a protected opportunity for every represented principal to refuse.

Use APP when agents need to negotiate a commitment involving a product, service, information, access or an outcome. Either participant can initiate the exchange. Applications define what the actions mean; APP defines how participants qualify, negotiate and adopt their commitments.

<p>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-FFD88A?style=flat-square&amp;labelColor=C94B00"></a>
  <a href="pyproject.toml"><img alt="Python: 3.11+" src="https://img.shields.io/badge/Python-3.11%2B-FFD88A?style=flat-square&amp;labelColor=C94B00"></a>
  <a href="https://github.com/JohnnyFiv3r/agent-promise-protocol/releases/tag/app-v0.4-draft.1"><img alt="APP: 0.4 reference draft" src="https://img.shields.io/badge/APP-0.4%20reference%20draft-FFD88A?style=flat-square&amp;labelColor=C94B00"></a>
</p>

## From intent to agreement

- **Express intent.** Publish an outcome within the applicable consent and admission rules. Seeking an outcome does not promise to supply or acquire it, or issue another agent's promise.
- **Make qualified offers.** Each agent issues only its own promises, subject to capability, current authority and understood conditions. An attributable declaration and an APP-qualified promise remain distinct; a signature alone does not prove a claim true.
- **Negotiate exact terms.** Exchange and revise offers within the participants' declared policies and interaction budgets. Both agents adopt the same exact candidate for each bilateral agreement.
- **Protect principal refusal.** Preserve the positive refusal period for every represented principal. Agent agreement, principal clearance and downstream authorization are separate decisions.
- **Retain attributable evidence.** Keep declarations, later observations and assessments tied to their issuers. Agreement does not establish fulfillment or payment, and APP supplies no universal verdict on whether a promise was kept.

For conceptual review, start with the **[Promise Theory review note](docs/review/promise-theory-correspondence.md)**. The [review package for Dr. Mark Burgess](docs/review/README.md) brings together the theoretical correspondence, APP's deliberate governance additions, seven questions and a worked research example.

## Try one agreement

The repository includes an independently implemented Python reference runtime, schemas and executable checks. With Python 3.11 or newer and [uv](https://docs.astral.sh/uv/) installed, run the current checkout:

```sh
git clone https://github.com/JohnnyFiv3r/agent-promise-protocol.git
cd agent-promise-protocol
uv sync --locked --extra dev
uv run --locked agent-promise-protocol review-demo
```

The review demo follows one requester and one provider through a bilateral research agreement. It then records a provider inability report and a separate requester assessment while preserving the original promise. It writes a portable signed trace and a readable summary into a fresh temporary directory. Add `--directory PATH` to choose a fresh, empty output directory.

For the broader demonstration, including principal refusal, restart recovery, three-agent composition and guarded fake-adapter handoff:

```sh
uv run --locked agent-promise-protocol demo
```

The broader demo prints structured observations and writes durable SQLite ledgers into a fresh temporary directory. It also accepts `--directory PATH` to choose a fresh output directory.

**Both demos are controlled simulations.** Ed25519 signatures, RFC 8785 digests, schema checks and SQLite transactions are real. Capability evidence, principal policies, clock, inbox/health observations and peer transport identities are controlled fixtures using `TestPolicy`. The broader demo's native adapter is a deterministic fake. Neither demo makes network calls, real service requests, orders or payments; neither demonstrates independently implemented agents or autonomous model reasoning.

Start with the **[implementer guide](docs/implementer-guide.md)**, then the [runtime and integration guide](docs/runtime.md). [Validation](validation.md) records evidence categories and reproduction commands; [conformance](conformance.md) explains the remaining assessment scope. Passing this implementation's tests does not establish full RP1 deployment conformance, independent interoperability or ease of adoption by another builder.

## One agreement first

The bilateral primitive does not require a transaction plan or native adapter. Composition, adapter handoff and lifecycle evidence are additional declared features. Unknown required features or meanings block the dependent act.

Applications supply understood action semantics, truthful capability and constraints, principal-approved permissions, and a usable principal notice/refusal channel. The package supplies protocol checks and integration boundaries; it cannot manufacture those application facts. The current authority arrangement is one explicitly delegated realm sharing one SQLite ledger. It does not provide federated consensus or fencing against a separate database copy.

Keep **agent agreement**, **principal clearance**, and **downstream authorization** separate. A positive refusal-window status never fabricates native action authority or a human signature.

## Hosting and ownership

A buyer can use one connector to its delegated APP participant, or an embedded participant. Sellers expose independently hosted A2A APP endpoints. Discovery, intent routing and offer aggregation are optional application services. Each participant may retain its own permitted signed evidence; the core requires no APP-operated ledger or mandatory discovery provider.

The [deployment model](deployment-model.md) distinguishes journal custody from scoped coordinator, resource and refusal/status authority. RP1 currently selects a common conflict authority, and runtime 0.1 uses a shared SQLite store. The [independent-participant slice](design/independent-participant-slice.md) is the remaining distributed-runtime work; separate-store portability tests do not claim it has already been implemented.

## Choose a starting point

| You want to… | Start here |
|---|---|
| Understand and critique the Promise Theory interpretation | [Review note](docs/review/promise-theory-correspondence.md) and [worked research example](docs/review/worked-example.md) |
| Build an APP participant | [Implementer guide](docs/implementer-guide.md), [conceptual quick-start](docs/quickstart.md) and [runtime guide](docs/runtime.md) |
| Read the governing contracts | [Eight contracts](contracts/README.md): C1–C6 cover bilateral formation and recovery, C7 composition, C8 the adapter boundary and evidence |
| Inspect the model and decisions | [Core model](contract.md), [current decisions](decisions-v0.4.md), [architecture](protocol-architecture.md) and [trust/failure model](design/trust-and-failure-model.md) |
| Implement the reference profile and harness boundary | [RP1 profile](profiles/reference-profile.md) and [application/harness design](profiles/harness-interface.md) |
| Work with wire structures | [Semantic schemas](schemas/contract.schema.json), [interaction envelopes](schemas/interaction.schema.json) and [admission declaration](schemas/admission-policy.schema.json) |
| Inspect examples and implementation | [Fictional examples](examples/README.md), [worked scenarios](examples/lifecycle-walkthroughs.md), [runtime source](src/agent_promise_protocol/) and [tests](tests/runtime/) |

## Status and development

APP is a **0.4 reference draft** with a **0.1 Python reference runtime**. Run the runtime and document checks from the checkout:

```sh
uv run --locked --extra dev python -m pytest tests/runtime -q -ra
uv run --locked --extra dev python checks/validate.py
```

Separate integration tests exercise actual TLS 1.3 mutual authentication and a local OPA 1.21.1 service. Installing the Python package does not install OPA; use the [validation guide](validation.md) for the required setup and evidence boundaries. See the [changelog](CHANGELOG.md) for changes.

The original ABP contract/profile baseline is preserved at `f4a01e2`. The current draft adds [deployment and ownership clarifications](deployment-model.md) and uses APP's distinct wire namespace. The underlying commitment and RP1 authority guarantees are preserved; old identifiers and signed records are not silently accepted as APP. Historical archives retain their original names and status. [P01–P27](tests/PROPOSED.md) remain proposed assessment scenarios, with partial coverage by executable tests. They are not a checklist in which every proposal has passed.

## Reference release and compatibility

The [APP 0.4 Reference Draft release](https://github.com/JohnnyFiv3r/agent-promise-protocol/releases/tag/app-v0.4-draft.1) fixes the reference draft, RP1 profile, schemas, examples and runtime source as one identifiable release. The current checkout also includes the subsequent conceptual review package and `review-demo`. [Release metadata](release.json) lists their distinct versions and normative sources. The release assets include the source bundle, wheel, source distribution, verification report, release manifest and SHA-256 checksums. The report names the exact tested source commit and package hashes.

The extension and profile URIs are exact identifiers. Their `main` URLs do not make mutable page content authoritative: implementations pin the understood contract/schema revision. The [APP namespace transition](docs/namespace-transition.md) explicitly replaces the earlier ABP names without translating existing acts. Breaking semantic changes require new protocol/profile identifiers and explicit understanding by participants. A documentation correction or implementation repair must not reinterpret an already adopted agreement. Maintainers review changes through pull requests; [contribution](CONTRIBUTING.md) and [release](RELEASING.md) guidance explain that process.

## Native boundary and current limits

The runtime freezes a preparation, journals a stable dispatch attempt before invoking an enrolled adapter, and reconciles uncertain outcomes without automatically dispatching again. The provided adapter is a deterministic fake. No AP2, UCP, ACP, payment rail or live service integration has been qualified.

Production authenticated time/NTS, qualifying HTTPS principal inbox operation, signed registry distribution and failover fencing remain integration work. `policy_defined` validity is unsupported. Some unusual object-key orderings cannot produce a matching OPA/JCS decision digest and fail closed. See the [runtime limits](docs/runtime.md#current-limits) and [policy implementation notes](policies/README.md).

Original specification, schemas, runtime and examples are MIT licensed. Ordinary general-purpose dependencies are declared in [pyproject.toml](pyproject.toml) and pinned in [uv.lock](uv.lock). Related projects provide [research and inspiration](research/README.md); comparator implementation code and imported test suites are not used. See [contribution guidance](CONTRIBUTING.md). Historical snapshots preserve [0.3](archive/0.3/README.md), [0.1](archive/0.1/README.md), and [0.2 in Git history](https://github.com/JohnnyFiv3r/agent-promise-protocol/tree/0011b504b706970c54a780d700be3efe444d4898).
