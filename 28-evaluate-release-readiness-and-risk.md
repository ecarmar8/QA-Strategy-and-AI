---
name: evaluate-release-readiness-and-risk
description: "Recommend Go, conditional approval or No-Go using evidence and explicit decision authority."
---

# 28 · Evaluate release readiness and risk

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Recommend Go, conditional approval or No-Go using evidence and explicit decision authority.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Agreed entry/exit gates, release/build scope, current coverage/results, open defects/risks, nonfunctional evidence, rollback/monitoring plan and release authority.

## Procedure

1. Verify that evidence belongs to the release candidate, environment and relevant configuration. Reconcile scope changes, stale results, essential unrun/blocked cases and unresolved criteria.
2. Evaluate each mandatory gate independently: critical business/financial/access invariants, required regression, serious defects, essential nonfunctional requirements, data/migration integrity and operational readiness as applicable. Where business UAT is required, plan representative journeys and synthetic data with the business owner, record who actually performed acceptance and their decision, and keep missing UAT sign-off visible. QA evidence does not impersonate business acceptance.
3. Recommend No-Go when an essential gate fails, or evidence required by an established mandatory gate is missing. If the gate definition or decision policy is itself unconfirmed, use Pending assessment and name the missing decision/evidence. Neither permits a positive recommendation. Do not waive mandatory legal/security/financial-integrity obligations by averaging a pass rate or recording a generic risk acceptance.
4. For nonessential residual risks, consider a conditional recommendation only with a named authorized owner, explicit impact, mitigation/workaround, monitoring, expiry/review trigger and build/release scope. If these are absent, decision Pending.
5. State recommendation, evidence, residual risk and next actions. QA supplies the assessment; the designated release owner decides. Do not deploy, merge or change release status unless that specific action is authorized.
6. Record the final human decision separately from the QA recommendation and invalidate it when relevant release scope/build changes.

## Required output

Release assessment: Gate | Requirement/source | Evidence/build | Met/Failed/Missing/Not applicable | Risk | Owner | Action. Decision record: QA recommendation | Rationale | Conditional risks | Authority | Human decision | Timestamp.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

No Go based only on pass rate or absence of filed defects. Essential Missing is not Passed. Never fabricate approval, risk owner or release authority.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Application boundary

Apply this procedure to the actual product sources and current scope. Missing rules remain Pending definition; proposed work is not executed evidence.

## Handoff

23/24/21 to close gaps; 29 only after an actual authorized release context.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
