# Diagnose before prescribing

Use these problem patterns to choose an investigation, not to assume a cause. More than one can coexist; map their dependencies and prioritize consequential gaps with the team.

## Defects escape to production

**Signal:** Recurring user reports or late discoveries.

**Investigate:** Trace a bounded sample: expected behavior, introduction mechanism, detection opportunity, tested build and release decision.

**First intervention:** Agree one specific protection around a confirmed escape mechanism; verify it with the current tester and developers.

**Proof of effect:** Implemented control, current verification and later recurrence review across comparable release cohorts.

**Skills:** 00, 04, 07, 11, 22, 24, 30, 31. **Measures:** K01, K02, K05, K12.

## Requirements change or remain ambiguous

**Signal:** Different interpretations, rework or late acceptance disputes.

**Investigate:** Compare source revisions, rules, exceptions, decisions and the timing of changes.

**First intervention:** Resolve the essential uncertainty before affected implementation and review representative examples with the decision owner.

**Proof of effect:** Confirmed rule/change, real chronology and cases with independent expected results.

**Skills:** 03, 04, 05, 06, 10, 11. **Measures:** K04, K05.

## Useful feedback arrives too late

**Signal:** Large queues, last-minute testing or repeated waiting.

**Investigate:** Observe real work arrival, WIP, build/data readiness, blocked periods and available validation time.

**First intervention:** Pilot a smaller verifiable slice, earlier collaboration or a specific readiness correction according to the observed bottleneck.

**Proof of effect:** Actual timestamps, explicit waiting work and control evidence from the changed delivery slice.

**Skills:** 00, 09, 13, 14, 25, 31. **Measures:** K04, K13.

## Integrations fail unpredictably

**Signal:** Retries, partial results, duplicates or provider-specific failures.

**Investigate:** Inspect contracts, identity, pagination, limits, mappings, ordering and actual persisted effects.

**First intervention:** Define provider-specific required failure/recovery protections and verify them in an authorized controlled environment.

**Proof of effect:** Contract/revision, request/response, recovery result and consistent downstream state.

**Skills:** 03, 06, 12, 17, 18, 21. **Measures:** K07, K08, K10.

## Data cannot be trusted

**Signal:** Conflicting reports, wrong derived values or migration discrepancies.

**Investigate:** Confirm grain, schema, mappings, precision, time, null semantics and independent expected values.

**First intervention:** Trace a representative source change through transformation/persistence to the actual consumer; reconcile aggregate and row-level results.

**Proof of effect:** Reviewed query, snapshot, expected/actual differences and source-to-outcome lineage.

**Skills:** 05, 06, 12, 17, 18. **Measures:** K08, K09.

## Automation gives noisy or false confidence

**Signal:** Flaky results, skipped checks, brittle suites or green builds with missing evidence.

**Investigate:** Inspect assertion value, isolation, fixtures, retries, quarantine, runner exits and actual gate enforcement.

**First intervention:** Stabilize a small set of important protections at the lowest effective layer and prove required failures block progression.

**Proof of effect:** Reviewed assertions, first-attempt/retry records, safe negative gate test and named maintenance owner.

**Skills:** 11, 13, 15, 16, 20, 25. **Measures:** K01, K11.

## QA capability needs to grow

**Signal:** Unclear standards, overloaded ownership or dependence on one experienced person.

**Investigate:** Review current work samples, reasoning, capacity, knowledge concentration and decision ownership.

**First intervention:** Agree proportionate standards; pair on one important scenario, then have the tester lead and explain subsequent evidence.

**Proof of effect:** Revised work samples, explicit responsibilities and observable independent judgment.

**Skills:** 09, 10, 11, 22, 31, 32. **Measures:** K03, K13.

## Release decisions lack a clear basis

**Signal:** Conflicting opinions, activity counts or unrecorded acceptance of risk.

**Investigate:** Reconcile actual build/scope, agreed gates, stale results, required acceptance and operational prerequisites.

**First intervention:** Make essential failed/missing protection explicit; present a supported recommendation, next action and actual decision owner.

**Proof of effect:** Gate-level evidence, residual risks and a human decision record separate from QA recommendation.

**Skills:** 07, 11, 21, 26, 27, 28, 29. **Measures:** K01, K02, K03, K06.

Use [the skill catalog](skills.md), [primary KPIs](metrics.md) and [supporting diagnostics](quality-diagnostics.md). Record findings, hypotheses, owners and the next decision using [the working templates](project-templates.md).
