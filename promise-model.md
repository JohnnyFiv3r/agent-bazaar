# Universal qualified-action proposal

**Draft 0.4 · proposal for refinement under user decision 4**

An **APP-qualified promise** is an agent's attributable promise of its own action, made within the capability and authority required by its stated conditions and limits. APP requires evidence supporting those qualifications before conforming issuance and rechecks it where material to adoption, finalization and reliance. An **offer is a promise** whose performance is conditional on the stated agreement and policy requirements. Neither term guarantees future success.

This engineering model draws on Promise Theory's autonomous agents, self-authored behavior, provide/receive polarity, conditions, scope and assessment. It is not a verbatim definition from the book. Capability is a substantive requirement, not merely possession of a signed capability claim. An authenticated but unqualified assertion remains attributable evidence of what its author declared; it is not admissible evidence for the automatic APP act whose guard it fails. These distinctions do not relax any [C2 qualification requirement](contracts/02-qualified-actions.md#qualification-and-authority-guards). The [Promise Theory correspondence](docs/review/promise-theory-correspondence.md) distinguishes the source concepts from APP's operational choices.

## Issuance, reliance and assessment

Keep the historical declaration, APP qualification, current eligibility to rely, observer trust and assessment of actual behavior separate. A signature establishes authorship and exact content, not the truth of capability claims. Qualification evidence supports a policy decision, not certainty about future behavior. An observer's trust may inform its decisions under the applicable policies, but cannot replace required guards, rewrite the promise or erase previously adopted terms.

A conditional promise exists when its author issues it. The condition qualifies the promised behavior; mutual agreement or satisfaction of a later prerequisite does not retroactively create that issuance. A description awaiting its named actor's `issue_on_adoption` is different: the candidate author has not issued that actor's promise.

| Observation | APP interpretation |
|---|---|
| A known future condition is false or its satisfaction is unknown | Interpret the condition under its named semantics; do not infer that the conditional behavior is due or that its absence breaks the promise. |
| Required action or condition meaning is unknown | Block the dependent automatic act; preserve any attributable declaration without inventing its meaning. |
| Authority is revoked or capability evidence no longer qualifies | Reassess current eligibility under the applicable policy; preserve the original issuance and evidence used at that time. |
| An issuer withdraws a record | Apply that withdrawal to its exact target and policy-defined scope; do not erase its history or silently cancel other commitments. |
| A principal validly refuses an accepted offer | Apply C5's protected refusal to reliance on that accepted object; do not rewrite the original offer. |
| Observed performance appears to miss the promised behavior | Assess the original action and conditions under understood claim semantics, with attributable evidence and an identified assessor. |

These observations are not synonyms for a universal `broken` state. APP preserves their different subjects and evidence; domain assessment and native performance mechanisms remain outside the core. A provider claim, a counterparty assessment and an independent observer's assessment need not establish the same fact.

Autonomy has three relevant boundaries. An agent authors only its own promises. Its principal may authorize reliance on a resource-selection or ordering authority within an explicit adopted scope. Neither that authority nor the coordinator can force the agent's actual performance. Accepting scoped allocation rules is compatible with self-authorship; it does not grant a universal authority over the promiser.

## Shared shape

| Element | Meaning |
|---|---|
| Promise identity | Stable identifier for this specific action promise and its immutable version/content |
| Promiser | The agent issuing its own action; linked to the principal whose authority applies |
| Promisees | The identified intended counterparties; distinct from the permitted disclosure audience |
| Action type | Versioned semantic identifier for what the agent will do |
| Semantics reference | Immutable definition of the action's parameters, effects, prerequisites and interpretation |
| Polarity | `provide` or `receive`; describes action direction, not buyer/seller role or agreement acceptance |
| Parameters | Domain-specific typed inputs and subjects, interpreted under the named action definition |
| Capability references | Evidence supporting the agent's ability and relevant capacity to perform the action |
| Authority references | Existing principal-policy/delegation evidence covering issuance and the action under its conditions |
| Qualifications | Explicit conditions, limits and dependencies; each check has a named meaning and evidence requirement |
| Validity | The applicable policy-defined validity rule; no mandatory universal expiry |
| Disclosure | Who may learn or redistribute this record, under the publication and negotiated privacy rules |
| Portable proof | Existing proof mechanism authenticating issuer and exact content; it does not independently establish qualification, trust or fulfillment |

These elements are represented by the generic promise/action definitions in the [schema](schemas/contract.schema.json). The schema establishes structural compatibility; action-specific semantics establish what the parameters mean. An implementation that does not understand a required action definition MUST NOT automatically issue or adopt it.

## Why this is universal without becoming a product ontology

The shared structure answers who, what, in which direction, under which conditions, with what ability and authority, and for how long under policy. Domain-specific definitions supply resources, quantities, units, outputs and other terms through `action_type` and immutable `semantics_ref`. APP requires shared understanding of those definitions, not a core taxonomy, mandatory capability catalog, central registry or maintainer approval.

Capability is the actor's ability to perform the described action; the product or other subject is what the action concerns. Supplying a bicycle, checking an invoice against purchase records, providing a specified amount of compute and granting dataset access illustrate that distinction. These are examples, not protocol categories. The same agent can provide inputs and receive a result; either market side can contain either polarity.

Free-form explanation may accompany typed parameters. Text cannot silently extend the typed action or authority. Unknown or ambiguous required behavior must be clarified before issuance/adoption rather than treated as compatible because descriptions sound similar.

## Intent, offer, request and adoption

**Intent emission** is scoped to communicating or seeking what the emitter identifies. Its `emission_promise` covers that act under publication authority. “I seek research” does not promise to buy research. “I seek research work” does not promise to deliver a particular report. The action's qualifications need to cover declaration/seeking, not an outcome that has not been offered.

**Offer issuance** is the author's own qualified, conditional promise of the specified behavior. It carries issued `own_promises`, not a list labeled unadopted proposals. The offer's conditions can include exact mutual terms, principal review and native downstream prerequisites. Offer issuance therefore has meaning before mutual acceptance, without activating every conditional future action.

**Requested counterpromises** describe what the author wants another agent to promise. They are addressed requests, not signed promises attributed to that agent. Only that agent can issue and adopt its own corresponding behavior.

**Terms adoption** is each party's own authenticated adoption of the complete candidate and its own identified promises under that candidate. It binds the same exact content and principal refusal rules as the other adoption. Neither signer can issue the other party's promise.

Direct acceptance is supported: the recipient need not create an offer solely to answer one. By adopting the exact candidate, it may issue the qualified own behavior requested of it, using its own capability and authority. The requesting party's candidate never supplies that issuance. The other party's acceptance cannot broaden an already-issued offer's conditions.

Agreement does not require inventing a second service obligation. A party may assent with no separate performance promise when the terms require none; its act of adoption remains a qualified, authorized act.

## Capability and authority

Capability and authority are independent: being able to perform an action does not authorize it, and permission does not establish the ability to perform it. Advertising that ability alone neither establishes authority nor issues a promise. Qualification must be checked when an offer is issued and again where material capability, capacity or authority affects adoption/finalization. Explicitly conditional authority is acceptable when the condition and the policy authorizing that conditional commitment are clear. A hoped-for future delegation is not current authority to promise.

Evidence strength is policy-defined. A claimed skill, schema-valid reference or cryptographic signature is not proof of actual competence. The issuer is accountable for its assertion; counterpart policies determine acceptable evidence before adopting terms. Unknown qualification prevents the dependent automatic transition.

An agent can promise its own composite service or its act of requesting a subcontractor. It cannot issue another autonomous agent's delivery promise. If several alternative offers depend on the same capacity, the selection constraints must state that dependency; publishing alternatives does not multiply available capacity.

## No standing-promise mechanism

Principal policies express continuing permission, eligibility and limits. They are not converted automatically into service promises. A qualified action may be issued outside an agreement, but it must identify a specific action, author, conditions and validity. `until_withdrawn` keeps only that specific issued action valid under policy. It must not be interpreted as an ambient undertaking to accept future work or as an automatically recurring service promise.

The same qualified-action model continues through [composition](contracts/07-composition.md) and [handoff/evidence](contracts/08-adapter-boundary.md). Evidence can report fulfillment or assessment under understood semantics without changing who issued the original promise or implementing a native fulfillment/assessment system. `agreement_terms` expresses both commercial and noncommercial terms; no monetary obligation is required.
