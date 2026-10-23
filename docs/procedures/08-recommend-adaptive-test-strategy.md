---
name: recommend-adaptive-test-strategy
description: "Explain the QA approach as a senior leader and adapt functional, manual, automation and nonfunctional coverage."
---

# 08 · Recommend an adaptive test strategy

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Explain the QA approach as a senior leader and adapt functional, manual, automation and nonfunctional coverage.

## Shared contract

Read [docs/operating-contract.md](../operating-contract.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

Apply [QA_STRATEGY.md](../../QA_STRATEGY.md) and [docs/engagement-plan.md](../engagement-plan.md). Ground decisions in product/team discovery, observed delivery and diagnostic evidence. Use [docs/project-templates.md](../project-templates.md) for strategy, escape analysis, pilot and mentoring records. Do not prescribe a sector, tool or cause of defects.

## Inputs and prerequisites

Risk register; business objective; architecture/surfaces; delivery constraints; testability; team skills; environments, contracts and quality expectations.

## Procedure

1. State what confidence the release needs and the most important failure events to prevent. Define in-scope journeys and explicit exclusions with consequences.
2. Allocate functional coverage across UI/web/desktop, API/integration and data checks based on where behavior is best observed. Combine scripted manual testing, exploratory charters and automation; do not impose a universal pyramid percentage.
3. For each risk, specify technique, level, data, environment, evidence and owner. Include negative, boundary, permission, state, integration and data reconciliation coverage as applicable.
4. Select nonfunctional checks for performance, resilience, accessibility, security and compatibility based on agreed needs and available expertise. Identify specialist work and missing service-level objectives.
5. Define entry/exit gates, defect triage, traceability, regression, evidence retention, release recommendation and stakeholder communication. Distinguish QA recommendation from release authority.
6. Present a concise quality strategy and a practical track plan with tradeoffs for time/capacity. When constrained, remove or defer explicit scope with visible residual risk rather than quietly reducing essential evidence.

## Required output

One-page strategy plus track matrix: Risk/journey | Surface/level | Manual technique | Automation candidate | Nonfunctional check | Evidence | Owner | Gate. State assumptions, exclusions and adaptation triggers.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [docs/templates.md](../templates.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass.

## Quality checks and boundaries

Every major risk has an assurance method. No claim of complete coverage or zero defects. Strategy must remain understandable without naming tools for every step.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Application boundary

Apply this procedure to the actual product sources and current scope. Missing rules remain Pending definition; proposed work is not executed evidence.

## Handoff

09–16 for execution planning; 27 for quality communication.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
