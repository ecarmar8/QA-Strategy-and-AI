---
name: produce-clear-visual-quality-reports
description: "Generate an English quality report centered on verified process-risk mitigation, shift-left prevention, functional/non-functional assurance and unresolved risks; exclude financial estimates."
---

# 27 · Produce clear visual quality reports

Version: 1.3 · Language: English · Role: Senior QA / QA Lead

## When to use

Explain what was tested, what was observed and what decision follows for a quality review or delivery team.

## Shared contract

Read [docs/operating-contract.md](../operating-contract.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Use reporting profile PROCESS_RISK and read [docs/metrics.md](../metrics.md). Available evidence concerns QA-observable processes, requirements, reviews and actual testing; financial access is not required.

Verified metric dictionary, traceability, current evidence, essential risks, defects, release recommendation and audience/time limit.

## Procedure

1. Write all report labels, explanations and talk tracks in English. Use PROCESS_RISK. Lead with the QA recommendation, scoped process exposure and essential unresolved controls. Omit costs, savings, ROI, monetary exposure and financial-benefit sections, including placeholder cards; do not request financial data.
2. Put six indicators on the quality page: Verified risk mitigation; Unresolved critical risks; Critical process assurance; Shift-left readiness; Preventive findings resolved; Non-functional assurance. Use skill 26 and docs/metrics.md for formulas, eligibility and missing-data rules. Show counts, denominators, sources, scope/build and limitations.
3. Graph risk states as Verified mitigated, Control failed and Not verified. Show process assurance and the next action for each unresolved critical risk. Show chronology-supported preventive work and agreed non-functional scope/results. Absent data is Not measured; a known zero denominator is No data.
4. Link risk → process → required control → case or other verification method → actual evidence → defect/retest → recommendation. A risk qualifies only when every required control has current implementation/verification evidence. Keep accepted/deferred risks visible. Passing tests and discovered defects do not prove future incidents were avoided.
5. Put cases created/executed, Passed/Failed counts, pass rate, defects and automation statistics in supporting operational detail. Preserve their diagnostic traceability without using activity volume as the quality headline. Charts require exact counts; historical trends require comparable evidence.
6. Prepare a 60-second explanation of process risks, preventive analysis, verified controls, remaining gaps and the next decision. Redact artifacts, check source/build freshness, label simulations prominently and keep QA recommendation separate from human release authority.
7. Read docs/reporting.md. Copy reports/quality-report-template.html to reports/qa-report.html and retain schema_version 2.0, report_profile PROCESS_RISK and the process-risk layout. Replace embedded qa-report-data JSON using the actual risk/control/process/review/non-functional and run ledgers. Escape every < as \u003c in JSON strings. Do not invent timestamps or change unknown chronology into true/false.
8. Validate the data, arithmetic and rendered report. Inspect the underlying evidence; renderer checks alone cannot establish truth or sufficiency. If execution is unavailable, still create the report with truthful Not Run/Not verified/Blocked states and appropriate missing inputs. Return the absolute HTML path. Open local files only when the tool policy permits, otherwise give double-click instructions. No server or external dependencies are required.

## Required output

Deliver the six PROCESS_RISK indicators, process-risk/control matrix, functional/non-functional assurance, preventive evidence and next actions. Keep activity counts in supporting detail. The final browser deliverable is reports/qa-report.html. No financial KPI section or cards.

Markdown report: quality decision; Build/scope; 4–6 indicators with exact counts; status chart/table; essential risks; evidence links; next actions/owners. Include a short spoken script.

For browser-visual requests, also deliver `reports/qa-report.html`, a self-contained English report using the bundled template. Use actual engagement evidence; the empty template is not a product result. Do not claim that an HTML report connects to MCP or executes tests itself.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [docs/templates.md](../templates.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass.

## Quality checks and boundaries

No chart without source table. No decorative green score masking failed essential gates. Do not synthesize historical trends from one run or display a fake dashboard as live.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Small example

Five confirmed critical risks: two have all required controls verified, one control fails and two remain unverified. Report verified mitigation 2/5 = 40% and three unresolved critical risks. Missing early-review chronology gives Not measured. This is mitigation coverage, not a 40% decrease in incident probability or a claim that future incidents were prevented. Case pass rate remains supporting detail.

## Handoff

28 for release gate review, 33 for approved publication, 99 for the quality briefing.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
