# Engagement and improvement plan

Use this as a proposed sequence, adapted to the team's current delivery cycle and available access. Timeboxes guide review points; they do not promise complete discovery or a guaranteed decrease in bugs. Continue the team's existing critical validation while learning. Escalate urgent evidenced risks immediately.

| Period / checkpoint | Actions | Concrete deliverable | Review / exit evidence |
|---|---|---|---|
| Initial alignment | Confirm problem, business goals, scope, authority, sources, confidentiality and immediate release commitments | Engagement brief and stakeholder map | Sponsor and contributors review the initial understanding |
| First working days | Product walkthrough, team conversations, shadow current testing, trace a change and a production escape if available | Product/process map, actual delivery map, questions | Sources and unknowns explicit; workflow checked by participants |
| First diagnostic review | Review a bounded escape sample and work-flow evidence; identify detection gaps and waiting | Baseline, causal hypotheses and priority gaps | Evidence distinguishes confirmed patterns from assumptions |
| First improvement cycle | Agree one critical workflow and intervention; pair with the current tester; apply relevant controls | Pilot charter, refined criteria, risk-control coverage, actual evidence | Control effectiveness checked; original gap and remaining limits visible |
| End of first cycle | Present findings, pilot evidence, unresolved risks and next decisions | One-page executive report and updated backlog | Stakeholders decide retain/modify/stop or extend the pilot |
| Following cycles | Extend useful practices, add justified regression/automation, strengthen data and mentoring | Updated strategy and maintained controls | Evidence supports each expansion; maintenance owners identified |
| Ongoing observation | Review incidents, recurrence, control freshness and delivery waits | Trend review and improvement decisions | Comparable periods and baseline changes documented |

## A practical first ten-day outline

Days 1–2: align and observe a representative workflow. Days 3–4: reconstruct a small evidence-backed sample of escapes and waits. Day 5: agree the first pilot and success evidence. Days 6–10: apply it within normal delivery, mentor through the work and report results and limitations. Adjust to access, product complexity and the sprint/flow; do not wait for day 5 to report an urgent exposure.

## Minimum weekly communication

State what was learned, which important risks have verified controls, what remains unverified, what blocks progress and which decision is needed from whom. Include a source/build and an owner for every consequential action. Record the next review point. Use the team's existing meetings rather than adding meetings by default.

## Selecting the first pilot

Select a confirmed or credible high-impact gap with available evidence, a bounded change/process, an owner and a feasible verification method. If requirements are unclear, pilot early clarification. If integration behavior escapes, pilot contract/side-effect checks. If build differences invalidate results, pilot environment/build readiness. If queues consume validation time, pilot visibility and smaller verifiable slices. Do not choose automation simply because a tool is available.

## Capacity and contingency

List concurrent commitments, available contributors, dependencies and protected essential checks. If capacity is insufficient, show explicitly which scope will be deferred, what assurance is missing and who decides. When access is blocked, continue source analysis, questions and test design where valid; keep dependent execution Not Run/Blocked.
