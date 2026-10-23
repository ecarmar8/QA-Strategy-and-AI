# Produce the CapRelease executive report

Read QA_ENGAGEMENT_STRATEGY.md, KPI_DICTIONARY.md and the shared PROCESS_RISK_KPIS.md. The initial CTO_REPORT.html presents a proposed strategy and empty evidence baselines, not a simulated execution or actual company assessment. It includes the day-one approach, six primary metrics, nine supporting diagnostics and all vacancy mappings. Keep the executive discussion focused on the relevant measures.

## Reproducible generation

From the repository root run:

```bash
python profiles/caprelease/build_report.py
```

The standard-library script reads primary-report-data.json and kpi-ledger.json, preserves the shared report layout and writes CTO_REPORT.html and CTO_REPORT.metrics.json. It performs no network requests, SQL operations, tool connection or product execution. Open CTO_REPORT.html locally. The HTML is self-contained; sanitized source ledgers and the underlying evidence remain separate reviewable artifacts.

Update both ledgers from actual reviewed sources, then regenerate. The primary report import button is hidden in this combined report because it would update only the six primary KPIs and leave supporting metrics stale. Do not manually edit a displayed percentage.

## Primary ledger

primary-report-data.json uses the shared schema_version 2.0, report_profile PROCESS_RISK contract. Use Established baseline metadata only after scope/cohort confirmation. For an actual sourced engagement report set is_template to false and populate product/build/source/period and the real evidence ledgers. A strategy-only report keeps is_template true and actual execution Not Run. See ../../HTML_REPORT_GUIDE.md and ../../PROCESS_RISK_KPIS.md.

## Supplemental ledger schema 1.0

Top-level metadata: scope, build, period and source. baselines maps each population name below to Established or Not established. Every population is an array. An unestablished population stays empty; an established scope needs an actual scope and period/cohort description. Every record has a unique id and a source reference. Missing baseline means Not measured, not a known empty population.

| Population | Required record fields / meaning |
|---|---|
| integration_controls, data_rules, contracts | id, source, required (boolean), status (Verified/Failed/Not verified). Verified also needs implementation_ref, verification_ref, evidence_current=true and nonempty evidence_ids. A required=false exclusion needs exclusion_reason and a reviewed source. |
| automation_controls | The control fields above plus required_assertions (positive integer), automated_assertions (integer from 0 to required_assertions), gate_enforced (boolean), pipeline_run_ref and gate_verification_ref. Numerator membership needs Verified, all required assertions automated and actual enforced current execution. |
| decisions | id, source, status and the same verification evidence fields. Verified additionally needs required_signal_ids, linked_signal_ids, signals_current_under_policy=true, policy_ref and rule_version. Required signal links must all be present. A confirmed zero-signal exception requires exception_ref. The underlying evidence must verify the actual source/currentness/decision linkage. |
| releases | id, source, observation_complete (boolean; unknown classification leaves the metric Not measured). This is the confirmed deployed-release cohort, not every build. Define observation_window at top level, and production_attribution_complete=true only with reviewed classification and attribution. |
| critical_defects | id, source, introduced_release_id, classification_ref, critical=true, confirmed=true. Deduplicate defects; multiple defects in one mature release count as one affected release for K12. Unknown attribution makes completeness false, not a missing row silently omitted. |
| feedback_items | id, source, ready_at, readiness_rule_ref and, when complete, feedback_at and feedback_ref. Timestamps need explicit zones. Missing readiness makes Not measured; absent feedback is still waiting and is reported separately. Eligible readiness cohort includes waiting work. |
| ai_artifacts | id, source, first_review_completed (boolean). Completed reviews need review_ref, reviewer, material_correction_policy_ref and accepted_without_material_correction (boolean). Unreviewed records stay visible outside the reviewed denominator. |
| effort_pairs | id, source, baseline_ref, assisted_ref, comparability_ref, same_output_standard_verified=true, baseline_minutes and assisted_minutes (finite, nonnegative numbers). Assisted active effort includes prompt preparation, review, correction and verification. Incomplete matching/effort means Not measured. |

Implementation/verification references and nonempty evidence fields enforce structural consistency. They do not independently establish truth, freshness or sufficiency; procedure 32 and accountable source review still apply. A boolean supplied by AI is not proof of a working control.

K13 uses calendar elapsed hours and linearly interpolated quantiles at index (n−1)×q, matching the specified calculator. If the team wants working-hour latency, agree a business calendar/time-zone policy and implement that method explicitly; do not mix it with these values. Show completed sample size and waiting items/age in the underlying review; do not infer overall improvement from completed work alone.

## Instruction for Copilot / Claude Code / another capable LLM

```text
Apply procedure 00 and the selected CapRelease role profile.
Read profiles/caprelease/QA_ENGAGEMENT_STRATEGY.md,
ROLE_TRACEABILITY.md, KPI_DICTIONARY.md, REPORTING.md and
AI_EVIDENCE_AND_ACHIEVEMENTS.md. Apply procedures 26, 27 and 32.

Use only available actual sources and current authorization.
First establish product/team/process context, confirmed rules,
scope and evidence baselines. Identify missing sources and continue
independent useful work. Do not infer findings from the vacancy.

Update primary-report-data.json and kpi-ledger.json from reviewed
records, preserving provenance, currentness and missing data.
Never type claimed achievements or percentages into the report.
Do not invent SQL tables, routes, pipeline runs, timing or approvals.
Keep six primary process-risk KPIs and relevant role diagnostics.
Exclude financial benefit metrics.

Run python profiles/caprelease/build_report.py when local execution
is available, inspect its output and review the HTML in a browser.
Preserve the distinction between proposed strategy, portfolio
deliverables and actual CapRelease results. Return the report,
source limitations and the next concrete decision/action in English.
If execution is unavailable, provide the exact blocker and keep
dependent checks Not Run; do not manufacture report values.
```

## Verification before sharing

Reconcile the role mapping, evidence/build references, all required controls and exclusions, independent oracles, cohort completeness and timestamps. Run the report calculator, inspect renderer errors and verify desktop/mobile presentation. Use only sanitized authorized material. The report is a local deliverable; this instruction does not authorize GitHub publication or sharing company data.
