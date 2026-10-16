<p align="center">
  <img src="assets/brand/app-icon.png" width="112" alt="Agent Promise Protocol heart-shaped handshake logo">
</p>

<h1 align="center">Agent Promise Protocol (APP)</h1>

<p align="center">
  <strong>Emit intent. Make qualified promises. Agree on exact terms.</strong>
</p>

<p align="center">
  An open protocol for agreements between autonomous agents acting on behalf of people and organizations.
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-FFD88A?style=flat-square&amp;labelColor=C94B00"></a>
  <a href="pyproject.toml"><img alt="Python: 3.11+" src="https://img.shields.io/badge/Python-3.11%2B-FFD88A?style=flat-square&amp;labelColor=C94B00"></a>
  <a href="contract.md"><img alt="APP: 0.4" src="https://img.shields.io/badge/APP-0.4-FFD88A?style=flat-square&amp;labelColor=C94B00"></a>
  <a href="#status-and-validation"><img alt="Status: Early Release" src="https://img.shields.io/badge/Status-Early%20Release-FFD88A?style=flat-square&amp;labelColor=C94B00"></a>
</p>

<p align="center">
  <a href="#overview">Overview</a> ·
  <a href="contract.md">Specification</a> ·
  <a href="#getting-started">Get started</a> ·
  <a href="contracts/README.md">Review guide</a> ·
  <a href="https://github.com/JohnnyFiv3r/agent-promise-protocol/issues">Feedback</a>
</p>

## Overview

Agent Promise Protocol lets an agent express what it seeks without turning that intent into an offer. Other agents respond with actions they are capable and authorized to promise. The parties negotiate, adopt the same exact terms, and preserve a protected opportunity for every represented principal to refuse.

APP is an A2A extension for commitments involving products, services, information, access or outcomes. Either participant can initiate an exchange. Applications define what an action means; APP governs who can promise it and how the parties agree to its terms.

## Why APP?

An agent seeking a source-backed report needs to distinguish a request for research from a promise to buy it. A provider needs to offer its work under clear conditions, revise its terms, and know which agreement was adopted. The people or organizations represented by those agents need to retain their right to refuse.

APP gives participants shared rules for those decisions:

- **Intent without an implied offer.** Emission promises the scoped act of declaring or seeking. It does not commit the agent to supply, purchase or obtain the requested outcome.
- **Promises with an accountable author.** An offer already issues its author's conditional promises. Requested counterpart actions remain requests until that actor issues its own promise. Capability and authority are checked separately.
- **Negotiation within declared limits.** Policies control publication, permitted contact and finite interaction budgets. Revising an offer does not renew its allowance or silently change adopted terms.
- **Exact agreement with principal protection.** Each party adopts the same immutable candidate. Agent agreement, principal clearance and downstream authorization remain separate decisions.

## Protocol at a glance

The baseline is one bilateral agreement. Optional features reuse that agreement model for composition and downstream evidence.

| Area | What APP defines | Contracts |
|---|---|---|
| Publication and negotiation | Consent, audience, admission, bounded offers and revisions | [C1](contracts/01-publication-policy.md), [C3](contracts/03-admission-negotiation.md) |
| Qualified actions | Intent, self-authored promises, counterpart requests, capability and authority | [C2](contracts/02-qualified-actions.md) |
| Agreement and principal rights | Exact adoption, durable finalization, notice and protected refusal | [C4](contracts/04-formation.md), [C5](contracts/05-principal-refusal.md) |
| Communication and proof | A2A operations, exact record identity, attribution and recovery | [C6](contracts/06-a2a-evidence.md) |
| Optional composition and handoff | Dependencies between agreements, guarded handoff and interpretation of returned evidence | [C7](contracts/07-composition.md), [C8](contracts/08-adapter-boundary.md) |

A research agreement follows a straightforward path:

1. A requester emits an intent within its publication and contact policies.
2. A provider offers its own qualified, conditional promise to produce the report.
3. Both agents adopt one exact candidate, and the originator records finalization.
4. The accepted object starts with principal-refusal windows pending; qualifying notice and the adopted rules govern clearance.
5. Any downstream action requires its own authority. Later delivery reports and assessments remain separate from the original promise.

The [core model](contract.md) defines the shared vocabulary. The [contract index](contracts/README.md) gives reviewers a reading path and the question each contract answers.

## Where APP fits

Existing discovery and subscription services connect participants under their publication policies. A2A carries their APP interactions. A provider's capability may involve an MCP endpoint, API, proprietary dataset, physical product or other service.

Accepted terms can feed downstream AP2/UCP/ACP validation, execution and payment systems through the selected adapter boundary. Those systems supply their own authority and perform their native actions. No live integration with them has been qualified.

APP requires no central operator, mandatory discovery provider or APP-owned ledger. Participants can retain permitted signed evidence or delegate custody. The [deployment model](deployment-model.md) separates that custody from coordination, resource and status authority. Applications supply shared action meanings, capability evidence, principal-approved permissions and usable notice/refusal channels.

## Getting started

- **Understand the model:** read the [specification and glossary](contract.md#reading-the-core-model), then the [governing contracts](contracts/README.md).
- **Review the theory:** use the [Promise Theory review note](docs/review/promise-theory-correspondence.md), [worked research example](docs/review/worked-example.md) and [conceptual review questions](docs/review/README.md).
- **Build a participant:** follow the [implementer guide](docs/implementer-guide.md), [RP1 reference profile](profiles/reference-profile.md) and [runtime guide](docs/runtime.md).
- **Inspect the records:** explore [semantic schemas](schemas/contract.schema.json), [interaction envelopes](schemas/interaction.schema.json), [admission declarations](schemas/admission-policy.schema.json) and [examples](examples/README.md).

With Python 3.11 or newer and [uv](https://docs.astral.sh/uv/), run the reference example:

```sh
git clone https://github.com/JohnnyFiv3r/agent-promise-protocol.git
cd agent-promise-protocol
uv sync --locked --extra dev
uv run --locked agent-promise-protocol review-demo
```

The demo writes a signed research-agreement trace and readable summary to a fresh temporary directory. It then records provider inability and a separate requester assessment without rewriting the promise. Use `--directory PATH` to select a fresh, empty output directory. Run `uv run --locked agent-promise-protocol demo` for refusal, restart recovery, three-agent composition and fake-adapter scenarios.

Both demos are controlled simulations. Signatures, content digests, schema checks and SQLite transactions are real; policies, capability evidence, time and peer identities are fixtures. The adapter is a deterministic fake. The demos make no network calls, real service requests, orders or payments.

## Status and validation

**APP 0.4 · Early Release · Python reference runtime 0.1**

The current runtime uses one delegated authority realm and a shared SQLite ledger. Independent-participant runtime support remains [design work](design/independent-participant-slice.md). [Validation](validation.md) records executed checks and separates them from proposed scenarios. Passing reference tests does not establish full deployment [conformance](conformance.md), independent interoperability or autonomous model reasoning. Production integration requirements are listed in the [runtime limits](docs/runtime.md#current-limits).

The [published reference bundle](https://github.com/JohnnyFiv3r/agent-promise-protocol/releases/tag/app-v0.4-draft.1) contains source, packages, verification evidence and checksums for its recorded commit. This checkout includes subsequent documentation and the review demo. Historical tags and [release metadata](release.json) retain their original identities; wire identifiers keep their exact spelling for [compatibility](docs/namespace-transition.md#app-04-display-name).

## Contributing

Feedback on the semantics, implementation and developer experience is welcome. Open an [issue](https://github.com/JohnnyFiv3r/agent-promise-protocol/issues) with the relevant contract clause or a reproducible example, and follow the [contribution guide](CONTRIBUTING.md) for changes.

Run the local checks:

```sh
uv run --locked --extra dev python -m pytest tests/runtime -q -ra
uv run --locked --extra dev python checks/validate.py
```

The [validation guide](validation.md) covers setup for mTLS and OPA integration checks. See the [changelog](CHANGELOG.md), [current decisions](decisions-v0.4.md) and [release process](RELEASING.md) for change history and compatibility requirements.

## License

The specification, schemas, reference runtime and examples are [MIT licensed](LICENSE). Dependencies are declared in [pyproject.toml](pyproject.toml) and pinned in [uv.lock](uv.lock). Related projects provide [research and inspiration](research/README.md); comparator implementation code and imported test suites are not used.
