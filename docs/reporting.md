# English process-risk quality report

Use [docs/metrics.md](metrics.md) with procedures 26, 27, 28 and 32. The deliverable is an evidence-based report for the actual engagement, including discovery/pilot status when release assessment is not yet possible. No browser automation connection is required to report supplied evidence.

## Report structure

1. Product, scope, period, build/source revision, evidence provenance and current stage.
2. QA assessment and essential unresolved process risks; human release decision separately.
3. Six process-risk indicators, each with counts/denominator, sources and missing information.
4. Process → risk → control → verification → evidence traceability.
5. Early decisions and preventive findings with chronology.
6. Applicable functional/non-functional results and limitations.
7. Next actions, owners and review points.
8. Supporting execution/defect detail, without making activity counts the quality outcome.

The reusable file [reports/quality-report-template.html](../reports/quality-report-template.html) starts with an empty evidence baseline and Pending assessment. It contains no example cases or product outcomes. Unknown baseline fields are explicitly missing; they do not mean no risks exist.

## Produce a report

Copy the template to `reports/qa-report.html` for the actual engagement. Replace the non-executable JSON object in `<script id="qa-report-data" type="application/json">` with the source-backed records. Preserve the HTML/CSS/renderer. Use schema_version `2.0` and report_profile `PROCESS_RISK`.

Keep required metadata from the template: `title`, `subtitle`, `target`, `run_id`, `build`, `source`, `generated_at`, `is_simulated`, `recommendation`, `decision_title`, `decision_reason`, `human_decision`, `scope_note`, `talk_track`, `cases`, `gates`, `defects`, `dependencies`, `actions`, and all process-risk extension fields. Use genuine references or Unknown/Pending where appropriate. Never invent an owner, build, time, execution or decision.

Set `is_template` to false for a sourced engagement report. Maintain `risk_baseline_status`, `process_baseline_status` and `early_review_baseline_status` as Established or Not established. Keep empty populations as arrays; the baseline metadata distinguish missing scope from a confirmed zero denominator.

The `risks`, `controls`, `processes`, `early_reviews`, `preventive_findings` and `nonfunctional` structures are defined in docs/metrics.md. The renderer validates records and arithmetic; human/source review establishes whether claims and evidence are true, sufficient and current.

Case statuses are Passed, Failed, Blocked, Not Run and justified Not Applicable. Passed/Failed require confirmed expected results, source, actual observations and evidence. Keep attempts in the underlying ledger. Gate statuses are Met, Failed, Missing and justified Not Applicable. Positive recommendations cannot hide essential failures/missing evidence. Record human approval only from an actual authorized decision.

Serialize JSON safely: escape `<` as `\u003c` so source text cannot close the data script. Never interpolate source text into executable JavaScript or raw HTML. Link only actual sanitized evidence files; validate their existence and access before sharing. The report renderer does not create evidence or verify the truth of source records.

The Load run data button imports a complete JSON object into the current browser view; it does not save a durable report. Embed the reviewed JSON to produce a reopenable file. No data is uploaded by the report. Open the local HTML with a modern browser; normal GitHub source viewing does not host the report as a webpage.

## Verification before delivery

Reconcile risk/control links, distinct IDs, cases, gates and evidence references. Reject stale evidence marked Verified. Recalculate formulas and distinguish Not measured from a known empty population. Keep accepted risks residual and essential controls prominent. Inspect desktop/mobile rendering, evidence expansion, case filters and print output. State remaining source limitations and return the actual report path.

Do not add cost, savings, ROI, monetary exposure, invented historical trends or “incidents prevented” estimates. If the available sources support only diagnosis, report diagnosis and the next decision, with release assessment Pending.
