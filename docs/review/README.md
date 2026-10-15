# Agent Promise Protocol: review package for Dr. Mark Burgess

**Prepared October 15, 2026. Conceptual review of APP 0.4 and its reference implementation.**

APP proposes a way for agents to publish permitted intent, issue their own qualified conditional offers, and adopt exact terms. Its central question is how an agent can express what it seeks without promising that outcome, issuing another agent's promise, or treating a response as assent. Either participant can initiate the interaction.

We are asking for criticism of that interpretation of Promise Theory, especially where APP's governance and admission requirements add something the theory does not require. The protocol and reference implementation are concrete enough to inspect. Their correctness as an interpretation of the theory remains a question for review.

## Suggested reading order

1. Read the [theory correspondence](promise-theory-correspondence.md): foundations, mappings, deliberate additions and points of tension.
2. Follow the [worked research example](worked-example.md), or run `agent-promise-protocol review-demo`. One requester and one provider form an agreement; a later provider inability report and a separate requester assessment leave the original promise attributable.
3. Use the [critique disposition](critique-disposition.md) to see what was clarified, retained or deferred. The [promise model](../../promise-model.md) and [C2](../../contracts/02-qualified-actions.md) contain the operative wording.

The example uses two controlled signing identities in the same implementation and delegated authority realm. It does not demonstrate independently implemented agents, autonomous model reasoning, real research delivery or emergent coordination. A valid signature establishes authorship of the claim; it does not establish the claim's truth.

## The distinctions we intend to preserve

| Question | APP's interpretation |
|---|---|
| Who made this declaration? | An authenticated record attributes exact content to its issuer. Describing somebody else's desired behavior is a request, not their issuance. |
| May this participant issue or rely on it in APP? | Capability, current delegation, understood conditions and the applicable admission policy must pass their separate checks. Failed qualification does not erase an attributable declaration. |
| What did the parties adopt? | Both adopt the same exact candidate; each issues or confirms only its own identified promises. A coordinator records the authorized result. |
| May a later action proceed? | The relevant conditions, protected principal-refusal periods and current action authority are checked separately. Agreement is not a command that causes fulfillment. |
| What happened, and who judges it? | Attributable observations and assessments retain their own reporters, evidence and meanings. APP supplies no universal fulfilled/broken verdict. |

APP's positive protected principal-refusal period is an intentional governance rule for this protocol. Prior delegation can authorize an agent to make a conditional commitment, but it does not waive that adopted right. We invite criticism of this scope choice without presenting it as a consequence of Promise Theory or silently moving it out of the core.

## Questions for Dr. Burgess

1. **Intent emission.** Does a promise scoped to declaring or seeking an outcome usefully distinguish emitted intent from an offer to supply or acquire that outcome? Is the explicit `emission_promise` redundant or self-referential, and what would a more faithful representation preserve?
2. **Qualification and assessment.** Does distinguishing an attributable declaration from an APP-qualified promise preserve the book's treatment of capability, intention and assessment? Which conclusions about ability can a local admission decision legitimately support?
3. **Autonomy and adoption.** Can exact bilateral adoption and a mutually selected allocation/coordinator authority be understood as voluntarily adopted constraints without becoming an authority over another agent's behavior? Where does our reference harness obscure that distinction?
4. **Represented principals.** Is an agent's own commitment under principal-approved policy a sound application of autonomy, or should the principal, harness and software actor be represented as separate promising agents for some claims?
5. **Conditions and later evidence.** Have we separated conditions on the promised behavior, conditions for current reliance, withdrawal, supersession, principal refusal and an observer's assessment correctly? Does our representation retain enough information to assess an unmet conditional promise without inventing a universal lifecycle?
6. **Protected recovery.** Is a mandatory positive refusal period a coherent boundary for this particular delegated-agent protocol? What does it exclude, and would a different layering preserve the same protection more clearly?
7. **Trust over repeated interactions.** Which observations should inform an agent's future confidence in another agent's promises, while leaving prior declarations and each observer's assessments intact? What minimal experiment would test that claim?

## Evidence and review boundary

The published [APP 0.4 Reference Draft](https://github.com/JohnnyFiv3r/agent-promise-protocol/releases/tag/app-v0.4-draft.1) is fixed at commit `85c3fa637b8f1ed7c0a55568b8a33a072918fd43`. Its release report records 193 runtime tests, 7 release checks, actual local OPA/mutual-TLS integration, and package verification. Those results qualify that recorded implementation under controlled assumptions; they do not validate the theoretical mapping.

This review package adds explanatory material and a narrower demonstration on top of that release. It does not relabel the release's test evidence as a result for the new changes. Commands and evidence boundaries are in the [validation guide](../../validation.md); the accompanying change review records the new revision's results.

The reference runtime uses one explicitly delegated shared authority ledger. Separate stores can verify transported evidence, but complete independent-store formation and independently authored interoperability remain [unimplemented or unassessed work](../../design/independent-participant-slice.md). No adoption, performance or conceptual-readiness percentage is asserted.

Review of APP does not require a marketplace, sourcesQL, a shopping interface, payment processing or settlement. Those application and native-system responsibilities remain outside the protocol's defined boundary. The next useful outcome is correction of the conceptual model, not a claim of production commerce readiness.
