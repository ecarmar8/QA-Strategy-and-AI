---
name: plan-and-estimate-testing
description: "Estimate QA work, coordinate people and dependencies, and create a realistic execution plan."
---

# 09 · Plan and estimate testing

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Estimate QA work, coordinate people and dependencies, and create a realistic execution plan.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Approved scope/strategy, dependency graph, team capacity, known absences, environments, data and delivery window. Existing throughput only if comparable.

## Procedure

1. Break work into refinement, design/review, setup/data, manual execution, automation, nonfunctional tracks, defect investigation, retest/regression and reporting. Include business UAT preparation/support and actual business-owner acceptance when required; distinguish QA support from the business decision. Do not estimate only initial execution.
2. Estimate ranges and assumptions for each work package using complexity, unknowns, integrations and historical data where reliable. Separate elapsed waiting time from active effort and avoid fictitious precision.
3. Use dependency order and specialist availability to place work in feasible waves. Identify environment, provider and approval constraints on the critical path. Reserve a reasoned contingency for uncertainty and rework.
4. Assign a responsible owner and reviewer, balancing skill development and business risk. Pair junior staff on critical financial paths; avoid measuring performance by case counts.
5. Define checkpoints, update frequency and change triggers. Show what changes if a requirement, build, environment or team capacity changes.
6. Publish a plan with confidence, blockers, entry/exit conditions and escalation path. Re-estimate material scope changes with a versioned rationale.

## Required output

Plan: Work package | Scope/risk | Dependencies | Owner/reviewer | Effort range | Waiting constraint | Planned wave | Deliverable | Confidence. Include capacity calculation and assumptions.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

Do not add overlapping person-days as elapsed days. No hidden overtime assumption. Protect critical review and retest capacity.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Application boundary

Apply this procedure to the actual product sources and current scope. Missing rules remain Pending definition; proposed work is not executed evidence.

## Handoff

10–14, 31 for people constraints, 00 checkpoint.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
