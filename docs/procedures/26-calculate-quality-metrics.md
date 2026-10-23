---
name: calculate-quality-metrics
description: "Calculate evidence-based process-risk, shift-left and functional/non-functional assurance KPIs for a quality review, with activity metrics as supporting detail and no financial estimates."
---

# 26 · Calculate meaningful quality metrics

Version: 1.3 · Language: English · Role: Senior QA / QA Lead

## When to use

Calculate transparent QA metrics for a defined scope, build and reporting period.

## Shared contract

Read [docs/operating-contract.md](../operating-contract.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Read [docs/metrics.md](../metrics.md), the authoritative KPI dictionary. Require the confirmed risk/process/control baseline, current implementation/verification evidence, early-review chronology, preventive findings and agreed non-functional requirements as applicable. Missing inputs remain unknown; no financial data is required.

Versioned case/AC baseline; selected latest applicable run per case/build; preserved attempts; defect history; timestamps; automated-suite inventory if available.

## Procedure

1. Use reporting profile PROCESS_RISK and write in English. Exclude costs, savings, ROI, monetary exposure, expected-loss estimates and financial-benefit claims. Do not ask the QA lead for financial data. Business amounts used as functional inputs remain legitimate test data.
2. Lead with Verified risk mitigation, Unresolved critical risks, Critical process assurance, Shift-left readiness, Preventive findings resolved and Non-functional assurance. Apply the exact formulas and eligibility rules in docs/metrics.md. Mitigation requires every required control to be implemented, currently verified and source-linked. Acceptance/deferral is not mitigation.
3. Freeze scope, cohort, current build/context, status taxonomy and denominators before calculating. Missing baseline/chronology gives Not measured; a known zero denominator gives No data. Expose unknown/unclassified populations. Do not infer early prevention from a final story or convert ordinal risk scores into incident-reduction percentages.
4. Put execution metrics in supporting detail: execution coverage = (Passed + Failed) / applicable planned cases; pass rate = Passed / (Passed + Failed). Blocked and Not Run stay separate. Preserve all attempts, count each risk once and deduplicate defects by ID.
5. For preventive metrics, require actual review/decision chronology and confirmed findings. A question or proposal alone is not a prevented defect. For non-functional assurance, require agreed scope/targets, real measurements, method/context and current evidence. Missing scope is Not assessed, not 100% or Not applicable.
6. Reconcile the risk-control ledger with skill 28's essential gates. Show failed/missing controls and residual concerns even when aggregate coverage is high. Keep designed coverage, current passing evidence and future incident outcomes distinct. Do not compare people by raw defect/case counts.
7. Label fictitious metrics SIMULATED, supplied history with provenance/limits and unknown samples as unverified. Return the metric dictionary, missing evidence and next actions. No universal quality score or unsupported causal prevention claim.

## Required output

Primary output: the six PROCESS_RISK KPIs using docs/metrics.md. Supporting output: execution, defect and automation detail. Omit financial KPI sections entirely, including placeholder cost/ROI cards.

Metric dictionary/table: Metric | Formula | Numerator | Denominator | Scope/build/window | Value | Evidence/source | Limitation. Add status distribution and essential unresolved risks.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [docs/templates.md](../templates.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass.

## Quality checks and boundaries

Reconcile totals; no division by zero, cherry-picked denominator or mixed-build aggregate. Metrics inform decisions, they do not automatically approve a release.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Small example

Five confirmed critical risks: two have all required controls verified, one control fails and two remain unverified. Report verified mitigation 2/5 = 40% and three unresolved critical risks. Missing early-review chronology gives Not measured. This is mitigation coverage, not a 40% decrease in incident probability or a claim that future incidents were prevented. Case pass rate remains supporting detail.

## Handoff

27 for visualization, 28 for decisions; 11 for missing baseline.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
