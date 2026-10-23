---
name: orchestrate-testing-lifecycle
description: Coordinate a QA engagement from product and team discovery through diagnosis, prevention, verification, leadership, release assessment and improvement, or resume an existing stage.
---

# 00 · Orchestrate an adaptive QA engagement

Read [QA_STRATEGY.md](QA_STRATEGY.md), [ENGAGEMENT_PLAN.md](ENGAGEMENT_PLAN.md) and [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md). Keep artifacts in English. Apply 31 and 32 throughout. Use current authorization and actual source/tool capabilities.

## Inputs

User objective, available project sources, current checkpoint if any, scope and authority. A missing environment does not prevent discovery or source analysis. No specific sector, delivery model, work-management platform or execution tool is required.

## Procedure

1. Resume a valid checkpoint; otherwise establish the engagement objective and available context. Identify products, users, stakeholders, decisions, current commitments and boundaries. Ask for essential missing sources while progressing on valid independent work.
2. Learn a real critical workflow with Product and current QA. Map actors, rules, states, data and dependencies using 03–06 where applicable. Meet contributors and shadow actual work. Trace a change from definition to release; record current practices and waits. Use supplied exports when connectors are unavailable. Use 01 only if actual Azure access is needed, not as the first mandatory step.
3. Diagnose using a bounded sample of escaped defects and successful/recent work when available. Record selection limits, introduction causes versus escape causes, evidence, hypotheses and decision ownership. For a new product use design/requirements risk instead; production data remains absent. Do not assume the tester caused the escapes.
4. Establish a baseline; apply 07–09 to propose a contextual strategy and one focused pilot. Specify the gap, critical process, controls, owner, verification and success criteria. Record actual reviews/decisions without fabricating agreement.
5. Apply 04 for early clarification and 10–13 for source-backed design, coverage, data and environment readiness. Use PROJECT_TEMPLATES.md where equivalent artifacts are absent. Begin prevention before affected implementation where feasible and retain chronology.
6. When prerequisites and authority exist, apply 14 and relevant 17–21 tracks. Decide automation through 15–16. Use 34 before actual Playwright MCP work; tooling setup is not the purpose of this engagement. Use 25 only for an applicable pipeline. Keep design and actual execution distinct.
7. Apply 22–24 for failures, corrections and impact regression. Recheck scope/evidence after changes. Mentor through the work using 31; preserve contributor ownership and observable learning.
8. Apply 26–28 and PROCESS_RISK_KPIS.md for the executive report and scoped recommendation. No financial KPIs or unsupported prevention claims. Retain residual risks and unknowns. Business acceptance and the human release decision remain separate.
9. Use 29 within the authorized release/incident scope and 30 for outcome review, recurrence and the improvement backlog. Evaluate the pilot and decide with owners whether to retain, adapt or stop. Publish through 33 only for actual authorized Azure writes; other systems require their real capabilities and authority.

## Role-specific context

When the user supplies a vacancy or target engagement, map its requirements to the strategy, relevant procedures and proof without converting the general method into a mandatory industry profile. For the selected CapRelease context, use [profiles/caprelease/ROLE_TRACEABILITY.md](profiles/caprelease/ROLE_TRACEABILITY.md) and its linked strategy, KPI and AI evidence documents.

## Output and handoff

Return only stage-appropriate artifacts: context brief, process/delivery map, diagnostic findings, baseline, project strategy/pilot, risk-control coverage, actual evidence, executive report or improvement review. Each carries scope, source/revision, status, owner or Unassigned, unknowns and next action. Use [PROJECT_TEMPLATES.md](PROJECT_TEMPLATES.md) and [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md).

Save a checkpoint with completed stages, artifact references, verified facts, open decisions, freshness invalidators and the next relevant procedure. Do not run every numbered procedure merely to complete a sequence. Unconfirmed rules remain Pending definition; unexecuted cases remain Not Run. Missing prerequisite blocks only dependent work. No outcomes, approvals, chronology or tools may be invented.
