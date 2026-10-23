---
name: verify-release-and-coordinate-incidents
description: "Plan safe postrelease verification and support an authorized incident response."
---

# 29 · Verify release and coordinate incidents

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Plan safe postrelease verification and support an authorized incident response.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Actual release authorization/status, deployed build, permitted production checks, monitoring/runbook, escalation/rollback owners and synthetic transaction policy.

## Procedure

1. Confirm what actually deployed and its scope. Do not infer deployment from a release recommendation or pipeline green result.
2. Select low-impact approved postrelease checks and health/financial reconciliation signals. Default to read-only observation; a production synthetic transaction requires explicit scope, limits and cleanup from the release/runbook owner.
3. Compare current indicators with defined expectations/baselines and observation windows. Do not invent uptime or latency thresholds, or call absence of immediate alerts proof of success.
4. If an incident is suspected, capture timeline, blast radius, correlation/build references and customer/money impact. Route through the actual incident owner and communication runbook; do not send external messages without authorization.
5. Recommend containment, feature disable or rollback based on the runbook and evidence. Execution of rollback, data repair or customer compensation needs the authorized owner; do not improvise financial corrections.
6. Preserve evidence, update incident decisions and feed recovery verification, defect work and learning into 30.

## Required output

Postrelease/incident ledger: Release/build | Check/signal | Authorized scope | Expected source | Actual evidence/time | Impact | Owner | Decision/action | Recovery verification | Follow-up.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

No production transactions, deployment or rollback implied by generic test authorization. No secrets/customer details in public reports. Distinguish monitoring observations from confirmed incident cause.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Application boundary

Apply this procedure to the actual product sources and current scope. Missing rules remain Pending definition; proposed work is not executed evidence.

## Handoff

22 for confirmed defects, 30 for review, 31 for approved stakeholder updates.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
