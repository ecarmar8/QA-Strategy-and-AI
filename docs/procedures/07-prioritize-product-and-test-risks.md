---
name: prioritize-product-and-test-risks
description: "Choose testing effort based on business exposure, technical change and evidence gaps."
---

# 07 · Prioritize product and test risks

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Choose testing effort based on business exposure, technical change and evidence gaps.

## Shared contract

Read [docs/operating-contract.md](../operating-contract.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Story/dependency/state/financial models, change scope, incidents and architecture information if supplied. No unsupported probability estimates.

## Procedure

1. Identify concrete failure events and affected users, money, data, access, business continuity and recovery. Link each to a source and changed component.
2. Assess impact and likelihood using a documented qualitative scale and available evidence. If likelihood is unknown, say Unknown and prioritize the uncertainty; do not generate precise probabilities.
3. Use P1 for money loss, integrity/access violations or critical journeys; P2 for significant functions with a viable workaround; P3 for secondary effects. Explain the local priority, rather than treating it as a universal severity mapping.
4. Record inherent risk, proposed test/monitoring/mitigation and residual uncertainty. Consider dependency centrality, integration volatility, historical failures and blast radius without double-counting the same risk.
5. Select essential release evidence and areas suitable for exploratory testing, automation, data checks or nonfunctional assessment. Prioritize by risk reduction per feasible effort.
6. Review the register with business/engineering owners. Track accepted residual risks with named owner, rationale, mitigation, expiry/review trigger and applicable release/build.

## Required output

Risk register: Risk ID | Failure event | Source | Impact | Likelihood/evidence | Test priority/reason | Mitigation | Required evidence | Owner | Residual risk | Acceptance status.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [docs/templates.md](../templates.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass.

## Quality checks and boundaries

No numerical risk score without a defined scale and evidence. A missing essential financial-integrity check remains a release blocker; an arbitrary pass rate cannot cancel it.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Application boundary

Apply this procedure to the actual product sources and current scope. Missing rules remain Pending definition; proposed work is not executed evidence.

## Handoff

08–10, 21 for nonfunctional risks, 28 for release assessment.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
