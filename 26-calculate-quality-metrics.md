---
name: calculate-quality-metrics
description: "Calculate transparent QA metrics for a defined scope, build and reporting period."
---

# 26 · Calculate meaningful quality metrics

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Calculate transparent QA metrics for a defined scope, build and reporting period.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Versioned case/AC baseline; selected latest applicable run per case/build; preserved attempts; defect history; timestamps; automated-suite inventory if available.

## Procedure

1. Define scope, time window, build, status taxonomy, deduplication and denominator before calculating. Include Passed, Failed, Blocked and Not Run separately; remove Not Applicable only with a documented scope decision.
2. For planned applicable cases N, use execution coverage = (Passed + Failed) / N; completion without blockers must not treat Blocked as executed. Use pass rate = Passed / (Passed + Failed). Show counts and no-data when denominator is zero.
3. For requirement coverage, report confirmed testable AC with reviewed designed cases / confirmed testable AC; separately report essential AC with current passing evidence / essential AC. Pending/unknown criteria remain visible.
4. Count distinct defects by severity, state and affected essential risk; avoid equating failed tests to defect count. Calculate reopen rate or defect age/repair lead time only with complete lifecycle timestamps and a defined cohort.
5. For automation, distinguish candidates, implemented tests, current executed coverage and reliability. Report first-attempt versus after-retry results, flaky tests and maintenance burden where recorded; no invented productivity percentages.
6. For leakage, define release cohort and postrelease observation window; for performance, include workload, sample count and percentile source. Do not compare teams or people using raw defect/case counts.
7. Show missing/stale data, limitations and essential gate status alongside aggregates. Label fictitious demo metrics SIMULATED. Label real user-supplied historical metrics with their source and verification limits, not SIMULATED; if provenance is unclear, use Sample / provenance unverified and avoid treating them as current-release evidence.

## Required output

Metric dictionary/table: Metric | Formula | Numerator | Denominator | Scope/build/window | Value | Evidence/source | Limitation. Add status distribution and essential unresolved risks.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

Reconcile totals; no division by zero, cherry-picked denominator or mixed-build aggregate. Metrics inform decisions, they do not automatically approve a release.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Small example

Input: six cases, 3 Passed, 1 Failed, 1 Blocked, 1 Not Run. Output: executed 4/6 = 66.7%; pass 3/4 = 75%; one blocker and one unrun visible; defects counted separately.

## Handoff

27 for visualization, 28 for decisions; 11 for missing baseline.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
