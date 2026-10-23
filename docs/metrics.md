# Process-risk reporting contract — English

Reporting profile: **PROCESS_RISK**. Audience: quality review. Scope: QA-observable processes, confirmed requirements, preventive analysis, functional and non-functional controls, evidence and release readiness.

Do not generate cost savings, ROI, monetary exposure, expected-loss estimates or financial-benefit metrics. Do not ask the QA lead to obtain financial data for this profile. Monetary amounts used as functional test inputs are valid business data; they are not cost/savings indicators.

## The question the report answers

**Which process failures have verified controls, what did early analysis resolve, and which important risks remain unresolved?**

Use “Verified risk mitigation” for implemented controls supported by current evidence. Reserve “Risk avoided” for a documented decision that removes the specific exposure from scope and has been reviewed by its owner. A test pass, defect discovery or no-incident observation alone does not establish that future incidents were prevented. Testing can reveal weaknesses and verify controls; fixes, design decisions and operational controls are what change the behavior or exposure.

These are proposed operational KPI definitions for this QA strategy, not universal industry benchmarks. Agree the scope, essential controls and thresholds with the appropriate owners before interpreting a percentage as sufficient assurance.

## quality indicators and exact formulas

Let R be the deduplicated, confirmed, applicable risk baseline for the report scope. Each risk has a scenario, process, source, critical flag and required control IDs. A risk is verified mitigated only when it has at least one required control and **every required control** is implemented, currently verified and supported by source-linked evidence. Failed, missing, stale, accepted or deferred controls do not qualify.

| KPI / dashboard label | Numerator | Denominator / unit | Interpretation |
|---|---|---|---|
| **Verified risk mitigation** | Risks in R whose required controls all meet the verification rule | All risks in R; multiply by 100 | Mitigation coverage of the identified baseline, not percentage reduction of real-world probability |
| **Unresolved critical risks** | Critical risks in R with at least one failed/unverified control, or no required control defined | Count; also show count / all critical risks | Exposes essential remaining failures and assurance gaps; accepted risk remains visible |
| **Critical process assurance** | In-scope critical processes whose required controls all meet the verification rule | All in-scope critical processes; multiply by 100 | A process requires complete relevant control evidence, not one passing happy path |
| **Shift-left readiness** | Critical stories that started development with risk/dependency review completed and essential decisions resolved before development | Critical stories that started development in the defined cohort; multiply by 100 | Requires source-backed chronology; it does not prove implementation controls already work |
| **Preventive findings resolved** | Confirmed pre-development findings requiring early resolution that were resolved before implementation, with a decision/change reference | All confirmed pre-development findings requiring early resolution in the same cohort; multiply by 100 | Includes pending/late resolutions in the denominator; recommendations/questions alone are not confirmed prevented defects |
| **Non-functional assurance** | Applicable agreed non-functional requirements met with current evidence | All applicable agreed non-functional requirements; multiply by 100 | Requires agreed targets and actual measurements; absent scope is Not assessed, not Not applicable or 100% |

**All percentages = numerator / denominator × 100.** A known zero denominator gives **No data**. Missing baseline, chronology, scope or required metadata gives **Not measured**, with the missing input and affected population. Never replace unknowns with zero. Do not infer dates or early prevention from a polished final story. Display unclassified risks/processes and unresolved scope questions as limitations; the identified baseline is not proof that every possible risk has been found.

Report risk statuses as **Verified mitigated**, **Control failed** and **Not verified**. Control failed takes precedence when both failed and missing controls exist; list both issues in the detail. This is a reporting classification, not an assertion that a future incident is certain.

## Primary page versus supporting detail

Primary page:

1. QA recommendation and essential unresolved process risks.
2. The six indicators above, with counts, denominators, scope/build, source and uncertainty.
3. Risk status chart and a risk → process → control → case → evidence matrix.
4. Functional process assurance, non-functional scope/results and preventive decisions.
5. Next actions and accountable owners; human release decision separate.

Supporting detail: cases designed/executed, Passed/Failed/Blocked/Not Run, pass rate, defects and automation. Preserve these for diagnosis and traceability; they do not lead the quality page or substitute for risk-control evidence. Count a risk once even if many cases cover it. Multiple risks may share a control, with explicit links.

Never treat an essential failed/missing control as acceptable because mitigation coverage is high. A critical risk accepted by an owner remains residual risk; it does not become Verified mitigated. Apply skill 28's mandatory gates and policy rather than approving from an aggregate percentage.

## Minimum evidence ledger

| Record | Required fields |
|---|---|
| Risk | Stable ID, failure scenario, process, confirmed source/revision, criticality/reason, required controls, residual concern/next action |
| Control | ID, purpose, implementation evidence, required cases or other verification method, actual current evidence refs, verification state, scope/build, owner |
| Process | ID/name, critical flag, complete required control baseline, source and scope; unassessed parts explicit |
| Early review | Story ID, whether/when development started, review/decision timestamps or explicit sourced relative chronology, essential decisions resolved, references |
| Preventive finding | Unique ID, confirmed issue, affected rule/process, identified stage, need for pre-development resolution, resolution stage and approved change/decision reference |
| Non-functional requirement | ID, agreed target/source, applicable scope, actual measurement/evidence, method/environment, result/current applicability |

For real control verification, inspect actual evidence and freshness; a boolean written by the LLM is not independent proof. Use the same current release/build baseline for comparable results and retain earlier runs.

## Browser-report data extension

The updated HTML report uses `schema_version: "2.0"` and `report_profile: "PROCESS_RISK"`. Retain the existing case/gate/defect records and add these arrays:

```json
{
  "schema_version": "2.0",
  "report_profile": "PROCESS_RISK",
  "controls": [
    {
      "id": "CTRL-01",
      "title": "Reject duplicate processing effects",
      "status": "Not verified",
      "implementation_verified": false,
      "evidence_current": false,
      "case_ids": ["TC-01"],
      "evidence_ids": [],
      "source": "Confirmed acceptance criterion reference"
    }
  ],
  "risks": [
    {
      "id": "RISK-01",
      "title": "Duplicate effect on retry",
      "process_id": "PROC-01",
      "critical": true,
      "control_ids": ["CTRL-01"],
      "source": "Confirmed risk assessment reference",
      "residual_note": "Retry behavior still requires verification."
    }
  ],
  "processes": [
    {
      "id": "PROC-01",
      "title": "Submit request",
      "critical": true,
      "control_ids": ["CTRL-01"],
      "source": "Agreed process scope reference"
    }
  ],
  "early_reviews": [
    {
      "story_id": "STORY-01",
      "critical": true,
      "development_started": null,
      "review_before_development": null,
      "decisions_resolved_before_development": null,
      "source": "Chronology not supplied"
    }
  ],
  "preventive_findings": null,
  "nonfunctional": {
    "scope_status": "Not assessed",
    "requirements": []
  }
}
```

This is an extension example, not a complete importable report. Use the HTML template's complete embedded object as the starting point. Initial states remain Not Run / Not verified.

Control statuses: Verified, Failed, Not verified. Verified requires `implementation_verified: true`, `evidence_current: true`, nonempty source, evidence IDs and linked passing cases where cases are the verification method. Every required case must be present and pass. Other methods require genuine evidence; do not create a fake test case just to fill a link.

Early-review booleans may be true, false or null. Null means chronology unknown. If any relevant story's start status or required timing fields are unknown, the cohort KPI is Not measured; show known records and unknowns in the detail. No started critical stories with complete chronology gives No data.

`preventive_findings: null` means no findings ledger was supplied. An empty array means a supplied ledger contains zero findings. Each finding entry uses `id`, `confirmed`, `identified_before_development`, `requires_early_resolution`, `resolved_before_implementation` and `decision_ref`. Timing fields may be null; unknown qualifying chronology makes the metric Not measured. A counted resolution requires a real decision/change reference. Preserve late and unresolved findings in the denominator.

Non-functional `scope_status` is Defined or Not assessed. Defined requirements use `id`, `title`, `status` (Met/Failed/Missing/Not Applicable), `source`, `evidence_ids`, `evidence_current` and `essential`. Met needs current evidence and a confirmed target/source. Agreed non-applicability needs a documented scope decision. Do not create performance, accessibility or security targets from memory.

The renderer checks structure, consistency and arithmetic. Skill 32 and human/domain review still establish whether the records are true and sufficient. Unknown evidence must not be converted to Verified merely to populate the dashboard.

## Copyable Copilot instruction

```text
Use the PROCESS_RISK reporting profile.
Read docs/metrics.md and apply skills 26 and 27.
Keep the report in English.

Lead with verified risk mitigation, unresolved critical risks,
critical process assurance, shift-left readiness, preventive
findings resolved and non-functional assurance.

Use only sourced process, requirement, review and test evidence.
Keep activity counts and pass rate in supporting detail.
Do not include costs, savings, ROI, monetary exposure or
financial-benefit estimates. Do not request financial data.

Do not equate passing tests with risks eliminated or incidents
prevented. Require implemented, currently verified controls.
Show Not measured for missing baselines or chronology and
No data for a known zero denominator. Keep essential failures
and evidence gaps visible regardless of aggregate percentages.

Use reports/quality-report-template.html to generate
reports/qa-report.html with schema_version 2.0 and
report_profile PROCESS_RISK. Preserve the visual layout.
Keep actual, supplied historical and simulated evidence separate.
Return the absolute HTML path and the evidence limitations.
```


## Baseline metadata for empty populations

The HTML data uses arrays for risks, processes and early_reviews, including when empty. Set risk_baseline_status, process_baseline_status and early_review_baseline_status to Established only after the scope/cohort has actually been confirmed; otherwise use Not established. A confirmed empty population gives No data for percentages; an unknown baseline gives Not measured. An established risk baseline with zero critical risks gives an unresolved-critical count of 0. Set is_template to false for an actual sourced engagement report; the reusable template starts true. These metadata describe provenance, not evidence that a control works.
