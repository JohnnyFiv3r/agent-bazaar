# APP and Promise Theory: correspondence for review

**Research note for Dr. Mark Burgess · 15 October 2026 · informative**

Agent Promise Protocol (APP) proposes a common way to publish intent, issue qualified conditional offers, adopt exact terms, and preserve a represented principal's opportunity to refuse. The central design is symmetric: an agent seeking an outcome and an agent seeking opportunities to supply an outcome can each publish intent without offering that outcome. This note separates the theoretical correspondence from APP's engineering and governance choices. It adds no wire fields, changes no contract, and claims no endorsement. The [review cover](README.md) contains the questions and reading order.

The [promise model](../../promise-model.md) and [C2](../../contracts/02-qualified-actions.md) define a narrower admissible protocol act than a general account of declared intention. A conforming APP issuer needs policy-acceptable capability and current commitment authority. That restriction must not collapse five questions: who issued a statement, whether APP may admit it, whether a counterparty trusts it, what actually happens, and how an observer assesses what happened.

## Correspondence, with the differences exposed

The source anchors below refer to Bergstra and Burgess, *Promise Theory: Principles and Applications*, second edition (2019). Their relevant distinctions include autonomous authorship, proposed versus issued promises, scope, polarity, conditionality, and observer assessment. APP uses these distinctions; it does not derive its entire state machine from them.

| Source concept and anchor | APP correspondence | Additional APP choice or limit |
|---|---|---|
| Own behavior; autonomous declaration [S1, S2] | Authenticated issuer must be the promiser of an `own_promise` | Cryptography establishes attributable content. C2 separately requires qualification for protocol admission. |
| Proposal versus made promise [S2] | A requested counterpromise and `issue_on_adoption` candidate description await that actor's issuance | An APP offer already issues its author's conditional promises. A second party's assent does not create the offer retrospectively. |
| Scope concerns information sharing [S3] | Promisees, permitted disclosure audience, and known recipients are distinguished | A disclosure rule specifies permission; it cannot prove that no unauthorized observer learned the content. |
| Give/receive polarity [S4] | `provide` and `receive` identify the named action's direction | Neither denotes buyer/seller role, acceptance of commercial terms, or satisfaction with delivery. |
| Conditional promising [S6] | Qualifications distinguish present checks and later prerequisites | C2 requires named semantics, check stage, decision authority, evidence, and unknown-state behavior. |
| Contextual assessment [S5] | Attributable evidence can name observer, subject, criteria, time, and result | A signature, accepted object, or transport receipt does not establish successful performance. |
| Invitation versus intrusive delivery [S7] | Publication consent and bounded admitted replies precede negotiation | Budgets, option lineages, replay accounting, and protected control paths are APP engineering mechanisms rather than deductions from the theory. |
| Permission and capability [S8] | Principal policy identifies whose resources and acts a delegation covers | Policy authority is scoped. Neither a principal nor a coordinator authors an autonomous counterparty's promise. |

## 1. Intent emission is the first act, not a miniature purchase

An APP `intent` contains an `emission_promise` whose subject is declaring or seeking the described outcome. Its qualification concerns that act: the emitter may publish this information, to this audience, for these uses. Its requested outcome remains a description of what it seeks. These are different scopes within one record.

For example, A declares that it seeks a source-backed research report. A does not thereby promise to purchase one, provide research, reserve funds, or obtain a successful report. B can symmetrically declare that it seeks research engagements without promising to deliver an unspecified future report. B's later offer can promise its own specified research action under explicit agreement and recovery conditions. Conduct B requests of A becomes A's promise only through A's own authorized issuance or adoption.

This separation also prevents a discovery intermediary from changing the transaction. Routing A's intent does not turn it into A's purchase offer; listing B's advertised capability does not produce B's delivery promise. Publication and reply permission remain separate. An agent may be permitted to discover an intent while lacking permission to send unlimited revisions to its author.

**Review focus ([cover question 1](README.md#questions-for-dr-burgess)):** The potential redundancy or self-reference of `emission_promise` needs examination. Any better representation must preserve the invariant that publishing a desired outcome issues no promise to produce, acquire, or purchase it. The present field remains; this note exposes its conceptual justification for critique rather than inventing another record kind.

## 2. Issuance, admissibility, trust, performance, assessment

The following notation is **APP analytical shorthand**, not new schema vocabulary or a claim of a new Promise Theory calculus. Let `π = (a, R, b | C, σ)` identify an actor, promisees, action body and conditions, and information scope. Let `K` be one exact candidate. Define:

```text
I(π, r)          attributable declaration of π in record r by actor a
Q(v, π, t)       required qualification established by verifier v at time t
Adopt(a, K)      a's authenticated adoption of the exact candidate K
F(K)            authoritative formation of K under C4
Clear(K, t)     applicable C5 principal-refusal requirements established
Assess(o, π, E)  observer o's judgment using observations E and its criteria
```

`I` records an attributable declaration, including one that fails APP's guards. It does not denote conforming APP issuance; that requires the applicable qualification checks. Preserving a rejected assertion's attribution does not admit it as a qualified promise.

`Q` means evidence meets the applicable policy for capability, capacity, commitment authority, and required semantics at the relevant stage. It is not an omniscient statement about ability. The verifier, policy version, evidence and freshness matter. Counterparty willingness to rely is a further decision; two parties can accept the same evidence as authentic and make different commercial choices.

The important non-implications are:

```text
I does not imply Q.
Q does not imply counterparty adoption or future success.
Adopt(a, K) does not supply Adopt(b, K).
F(K) does not imply Clear(K, t), native authority, or performance.
Assess(o, π, E) does not become every observer's assessment.
```

Consider a genuine issuer signing an offer after its delegation was revoked. Its authorship may be verifiable while C2/C4 reject reliance on that offer. Rejection must not be described as proof that the statement was never issued. Conversely, a forged provider signature cannot be treated as that provider's issuance merely because the proposed action is feasible.

Consider a correctly authorized researcher with convincing credentials who later supplies inaccurate citations. The issuance and formation history can remain valid while performance is assessed negatively. Qualification failure, invalid formation and poor performance are different diagnoses. A protocol that reports all three as an invalid promise loses the causal distinction the review is meant to test.

These are interpretation distinctions, not instructions to add a universal trust score. APP has no core reputation algorithm, domain evaluator, or learning mechanism. C8's optional evidence records carry an attributed claim under understood semantics; applications determine which evidence supports reliance. Any agreed assessor role affects the contractually relevant decision without making other observers unable to disagree.

## 3. Autonomy and delegated authority describe different boundaries

In §13.7.1, promising is restricted to autonomously possessed capabilities, excluding another agent's capabilities promised on its behalf [S8]. APP retains capability as a substantive requirement. Its evidence and delegation checks answer separate operational questions: what supports the claimed ability, and whose policy permits this commitment or resource use? A signed claim cannot create capability, and permission cannot establish it. Conversely, insufficient evidence can prevent APP admission without proving that the actor lacks the capability.

APP's principal is the person or organization whose policy authorizes the represented activity. The agent identity remains the issuer of its own qualified action. This is a deployment and governance relationship, not a theoretical permission to make another autonomous agent's promises. The book's principal promiser in an assisted promise [S6] must not be automatically equated with APP's represented principal.

There are three separate powers in the design:

1. **Declare one's own intended behavior.** Attribution records who did so. APP's admissibility rules can reject a statement without controlling every message that actor could emit elsewhere.
2. **Commit or use a represented resource.** The relevant owner controls permission, limits and evidence within a declared scope. A harness can prevent its enrolled actor from spending a resource it controls.
3. **Cause another actor to perform.** Neither a signed offer, owner policy, coordinator decision nor accepted object creates this power.

A policy service's `allow` result supports a scoped decision. It does not grant its operator authority over all actors in a network. A ledger custodian similarly preserves evidence without becoming its author. The practical autonomy boundary may encompass an agent's model, deterministic code, credentials and enforcing harness; APP must state which boundary it is claiming instead of treating an LLM process as the entire actor by default.

**Counterexample:** A promises B a completed report and intends to employ researcher C. A can own the composite result, or promise only to request C's work, with different terms. A cannot make C the promiser by inserting C into a transaction plan. C must issue its own action if C is to participate as promiser. C7's bilateral components retain that authorship; the orchestrator supplies coordination, not collective assent.

This makes refusal, denial and failure expressible. It does not claim that cooperative agents cease to be autonomous once they enroll. A nonconforming actor can act outside the agreed system; enforcement claims are limited to the resources and boundaries actually controlled.

## 4. Conditions need a stage and an observer

An offer can already be issued while its performance condition remains false or unresolved. It is therefore important to ask which fact is conditional, which actor determines it, and when the fact matters.

| Condition family | Example | Required interpretation |
|---|---|---|
| Present issuance/adoption qualification | Permission to offer a conditional research engagement | Must be established now; hoped-for future permission cannot fill the gap. |
| Formation prerequisite | Matching exact adoptions and protected capacity selection | Needed for C4 finalization; the offer's existence does not establish it. |
| Principal-recovery condition | Qualifying notice and completion of each protected period without timely refusal | C5 evaluates this separately from agent agreement. |
| Action prerequisite | Dataset access granted; native action authority remains current | Check at the adopted stage; earlier clearance is insufficient. |
| Performance/assessment condition | Delivered citations satisfy an agreed verification rubric | Requires observations and criteria; sending a request does not satisfy it. |

Suppose a report depends on access to a proprietary dataset. “Access is required” has understood meaning even while access is unavailable. “Our agent may issue this conditional offer only if its owner permits it” is a present authority requirement. The latter cannot be deferred by relabeling it as the former. Nor can a digest prove that both parties interpret an unfamiliar research rubric identically: it pins content; C2 still requires understood semantics.

## 5. Principal recovery is an explicit core governance commitment

APP deliberately requires a positive, nonwaivable principal-refusal period after agent agreement, with qualifying notice and a usable refusal path. This is a core design decision retained in [C5](../../contracts/05-principal-refusal.md), not a consequence claimed from Promise Theory and not an optional feature moved into a profile.

Both parties adopt that protection before finalization. Each relevant enforcing mechanism must then preserve it within its actual control. A refusal blocks future reliance on that accepted object; it does not make the prior agreement disappear or undo information already disclosed. No human reply is not a new human signature. A principal's policy supplies the duration and channel, while the protocol disallows zero or waived protection.

This deliberately excludes transactions that cannot preserve the required recovery opportunity. RP1 chooses `no_effects` before clearance. A different understood protected-effects profile would need evidence of equivalent protection; cancellation metadata alone cannot recover a disclosed secret. That limitation should be visible to a critic, not hidden behind generic claims of universal commerce support.

**Review focus ([cover questions 4 and 6](README.md#questions-for-dr-burgess)):** The adopted governance commitment and refusal/status authorities need examination at the chosen agent boundary and scale. The issue is the soundness and limits of the mechanism; removing the core protection is not this revision's proposal.

## 6. What is core, what is a profile, what has been demonstrated

| Layer | Scope in the current proposal |
|---|---|
| Core C1-C6 | Consented publication, self-authored qualified acts, bounded negotiation, exact adoption, attributable evidence and mandatory principal recovery. |
| Optional negotiated C7/C8 features | Composition, lifecycle evidence and adapter handoff. Bilateral agreement needs no transaction plan, reputation service or payment integration. Core protections still apply when features are selected. |
| RP1 mechanism choices | Particular proof, policy, transport, ordering and recovery mechanisms; one mutually accepted conflict authority per relevant scope. This is not a mandatory global APP operator. |
| Applications and downstream systems | Discovery, ranking, trust policy, product meaning, delivery, native orders, payments and settlement. APP owns no universal product taxonomy. |

The [runtime](../runtime.md) and [validation limits](../../validation.md#explicit-limits-of-the-evidence) support controlled checks of admission, authorship, exact agreement, replay, refusal and adapter gates. Integrated formation uses an explicitly delegated shared authority store. Separate-key/store evidence verification does not establish complete independent-participant negotiation. Deterministic fixtures, simulated observations and a fake adapter do not demonstrate independent learning, reputation convergence, real research quality, real delivery or settlement.

The conceptual test is whether these distinctions prevent false attribution and unjustified reliance while leaving each participant free to choose its own behavior and counterparties. Independent implementations and observed interactions can test that claim further. Passing the present checks is neither a novelty proof nor a quantitative measure of ecosystem readiness.

## Verified source anchors

All PDF page numbers below are **one-based**; printed page numbers are the book's labels. Fresh source retrieval on 15 October 2026 matched SHA-256 `f188f673bd4a48ad9d748a2e5aa5407f1180fd7b07577ebbe6df5a588b319d3b`. Relevant passages were rechecked in extracted text; PDF pages 43 and 94 were also rendered to verify definitions and notation. The earlier [whole-book reading manifest](../../promise-theory-reading-coverage.json) remains a historical coverage record, not a claim that this revision reread every page.

- **S1:** [§§1.2-1.3](https://markburgess.org/BookOfPromises.pdf#page=18), printed pp. 2-3 / PDF pp. 18-19; [§6.3.1](https://markburgess.org/BookOfPromises.pdf#page=99), printed pp. 83-84 / PDF pp. 99-100.
- **S2:** [§3.2, Definition 1; §3.3, Definition 2](https://markburgess.org/BookOfPromises.pdf#page=43), printed pp. 27-28 / PDF pp. 43-44. Also [§2.12](https://markburgess.org/BookOfPromises.pdf#page=40), printed pp. 24-25 / PDF pp. 40-41.
- **S3:** [§3.5.2, Definition 4](https://markburgess.org/BookOfPromises.pdf#page=47), printed p. 31 / PDF p. 47.
- **S4:** [§§3.11.1-3.11.3](https://markburgess.org/BookOfPromises.pdf#page=54), printed pp. 38-39 / PDF pp. 54-55.
- **S5:** [§§5.2.1-5.2.3, Definitions 21-23](https://markburgess.org/BookOfPromises.pdf#page=82), printed pp. 66-68 / PDF pp. 82-84.
- **S6:** [§6.2.1, Definition 30 and Laws 2-4](https://markburgess.org/BookOfPromises.pdf#page=94), printed pp. 78-80 / PDF pp. 94-96.
- **S7:** [§§13.5.2-13.5.3](https://markburgess.org/BookOfPromises.pdf#page=181), printed pp. 165-172 / PDF pp. 181-188.
- **S8:** [§13.7.1, Definitions 69-70](https://markburgess.org/BookOfPromises.pdf#page=197), printed pp. 181-182 / PDF pp. 197-198.
