# Methods I choose from

The method follows the problem. I combine these practices rather than impose one fixed sequence or a universal automation ratio. The shared operating cycle is Discover → Diagnose → Define → Prevent → Design → Verify → Decide → Improve.

| Practice | When I use it | What I do | Evidence / decision |
|---|---|---|---|
| Product and delivery discovery | Entering a team, a new workflow or a changed architecture | Walk through real work, shadow testing, trace a change to production, map owners and waits | Confirmed process/dependency view and questions |
| Risk-based testing | Choosing scope, depth and order under real capacity | Connect failure scenarios, consequences, change, uncertainty and required controls | Prioritized coverage and explicit residual risk |
| Shift-left and static review | Decisions are still changeable | Review criteria, designs, contracts and data rules; resolve consequential ambiguity with Product/Engineering | Source-linked decisions and preventive findings with chronology |
| Collaborative refinement | Multiple perspectives must agree on expected behavior | Work through examples and exceptions with the relevant contributors; a three-perspective discussion where useful | Shared rules and independent test oracles |
| Equivalence partitioning and boundaries | Inputs have categories or confirmed limits | Select representative valid/invalid partitions and edge values | Compact coverage with a clear rule basis |
| Decision tables | Outcomes depend on combinations of conditions | Model relevant condition/action combinations and prioritize consequential interactions | Auditable rule-combination coverage |
| State-transition testing | Lifecycle, approvals, cancellation or recovery matters | Check allowed/forbidden transitions and resulting persisted effects | State model and transition assertions |
| Exploratory testing | Learning, unexpected interaction and usability need investigation | Use a time-bounded charter, notes, hypotheses and evidence | Findings and new coverage/questions, separate from acceptance claims |
| Layered verification | A behavior spans code, service, contract, UI or data | Choose the lowest effective assertion level and retain meaningful cross-layer journeys | Fast useful feedback plus end-to-end confidence |
| Contract and failure-mode testing | A service or third party can change or fail | Verify schemas/semantics, limits, retries, partial outcomes, ordering and recovery when relevant | Provider-specific protection evidence |
| Data reconciliation | Transformations, migrations or derived information drive behavior | Use independent expected values, schema-aware queries, aggregates and row-level investigation | Source-to-outcome consistency and explained differences |
| Impact-based regression | A change/fix affects dependencies | Select from changed behavior, shared components, history and risk | Justified regression scope, not a blind full-suite habit |
| Quality-attribute verification | Performance, recovery, accessibility or security is material | Agree targets/method/scope and collect actual measurements with suitable expertise | Requirement-level evidence and remaining limits |
| Root-cause and escape analysis | A failure recurs or reaches production | Separate introduction from escape, reconstruct evidence and test causal hypotheses | Specific corrective action and recurrence review |
| Continuous testing and delivery feedback | Checks must support frequent change | Use appropriate pipeline stages, isolation, current artifacts and verified enforcement | Actual required-check/gate behavior |
| Mentoring and shared quality ownership | Capability or standards must grow | Review reasoning, pair on difficult work and transfer independent ownership | Improved work samples and actionable responsibility |
| Inspect/adapt | A pilot or delivery cycle ends | Compare evidence with its intended protection and decide retain/modify/stop | Reviewed improvement backlog and next experiment |

## Delivery frameworks

In Scrum, integrate quality into existing refinement, planning, daily coordination, delivery and retrospection; improve the team's actual Definition of Done with the team. In continuous flow/Kanban, inspect WIP, queues, blocked work and change readiness. In milestone delivery, plan progressive verification and dependencies. In migration work, establish mappings, reconciliation and recovery. Do not create extra ceremonies by default or compare teams by story points.

## Prioritization and uncertainty

Use the actual project taxonomy where available. Explain priorities through consequences and evidence. Unknown probability remains unknown; an ordinal priority score does not become a percentage of incidents prevented. Preserve the highest-impact gaps visibly when capacity requires deferral.

## The verification chain

**Source/revision → requirement/risk → control → case/verification → run/build → evidence → defect/fix → retest/regression → assessment → learning.**

This chain makes judgments reviewable across manual work, automation and AI assistance.
