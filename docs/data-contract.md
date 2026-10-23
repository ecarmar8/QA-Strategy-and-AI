# Evidence ledgers

Primary data uses schema_version 2.0 and PROCESS_RISK, defined in [metrics](metrics.md) and [reporting](reporting.md). Supplemental diagnostics use the contract below and [scripts/calculate_metrics.py](../scripts/calculate_metrics.py).

## Supplemental ledger schema 1.0

Top-level metadata: scope, build, period and source. baselines maps each population name below to Established or Not established. Every population is an array. An unestablished population stays empty; an established scope needs an actual scope and period/cohort description. Every record has a unique id and a source reference. Missing baseline means Not measured, not a known empty population.

| Population | Required record fields / meaning |
|---|---|
| integration_controls, data_rules, contracts | id, source, required (boolean), status (Verified/Failed/Not verified). Verified also needs implementation_ref, verification_ref, evidence_current=true and nonempty evidence_ids. A required=false exclusion needs exclusion_reason and a reviewed source. |
| automation_controls | The control fields above plus required_assertions (positive integer), automated_assertions (integer from 0 to required_assertions), gate_enforced (boolean), pipeline_run_ref and gate_verification_ref. Numerator membership needs Verified, all required assertions automated and actual enforced current execution. |
| outcomes | id, source, status and the same verification evidence fields. Verified additionally needs required_source_ids, linked_source_ids, sources_current_under_policy=true, policy_ref and rule_version. Required source links must all be present. A confirmed zero-source exception requires exception_ref. The underlying evidence must verify the actual source/currentness/outcome linkage. |
| releases | id, source, observation_complete (boolean; unknown classification leaves the metric Not measured). This is the confirmed deployed-release cohort, not every build. Define observation_window at top level, and production_attribution_complete=true only with reviewed classification and attribution. |
| critical_defects | id, source, introduced_release_id, classification_ref, critical=true, confirmed=true. Deduplicate defects; multiple defects in one mature release count as one affected release for K12. Unknown attribution makes completeness false, not a missing row silently omitted. |
| feedback_items | id, source, ready_at, readiness_rule_ref and, when complete, feedback_at and feedback_ref. Timestamps need explicit zones. Missing readiness makes Not measured; absent feedback is still waiting and is reported separately. Eligible readiness cohort includes waiting work. |
| ai_artifacts | id, source, first_review_completed (boolean). Completed reviews need review_ref, reviewer, material_correction_policy_ref and accepted_without_material_correction (boolean). Unreviewed records stay visible outside the reviewed denominator. |
| effort_pairs | id, source, baseline_ref, assisted_ref, comparability_ref, same_output_standard_verified=true, baseline_minutes and assisted_minutes (finite, nonnegative numbers). Assisted active effort includes prompt preparation, review, correction and verification. Incomplete matching/effort means Not measured. |

Implementation/verification references and nonempty evidence fields enforce structural consistency. They do not independently establish truth, freshness or sufficiency; procedure 32 and accountable source review still apply. A boolean supplied by AI is not proof of a working control.

K13 uses calendar elapsed hours and linearly interpolated quantiles at index (n−1)×q, matching the specified calculator. If the team wants working-hour latency, agree a business calendar/time-zone policy and implement that method explicitly; do not mix it with these values. Show completed sample size and waiting items/age in the underlying review; do not infer overall improvement from completed work alone.
