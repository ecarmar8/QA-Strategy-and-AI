---
name: produce-clear-visual-quality-reports
description: "Explain what was tested, what was observed and what decision follows for a CTO or delivery team."
---

# 27 · Produce clear visual quality reports

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Explain what was tested, what was observed and what decision follows for a CTO or delivery team.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Verified metric dictionary, traceability, current evidence, essential risks, defects, release recommendation and audience/time limit.

## Procedure

1. Lead with the decision needed, current build and recommendation. Explain the business consequence of the most important remaining risk in plain language.
2. Show a compact dashboard: scope, status distribution, essential criteria evidence, distinct serious defects, blockers and trend only when comparable historical data exists. Always show counts and denominators.
3. Use Markdown tables for exact values, Mermaid for dependencies/processes, and a simple bar/pie chart only where it clarifies actual data. Keep labels short and charts readable on GitHub. Provide a table fallback because rendering support varies.
4. Link the chain “requirement → case → actual run/evidence → defect → retest → recommendation.” Separate planned, executed and observed outcomes, and label simulations prominently on every simulated figure.
5. Prepare a 60-second talk track: objective, approach, evidence, decision and next action. Put detailed cases/evidence below the executive view, avoiding invented ROI or unsupported success claims.
6. Redact sensitive artifacts, check links/values and explain gaps, freshness and limitations. Reports are reviewable drafts until publishing is authorized.

## Required output

Markdown report: Executive decision; Build/scope; 4–6 indicators with exact counts; status chart/table; essential risks; evidence links; next actions/owners. Include a short spoken script.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

No chart without source table. No decorative green score masking failed essential gates. Do not synthesize historical trends from one run or display a fake dashboard as live.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Small example

Input: 3/6 Passed, 1 Failed, 1 Blocked, 1 Not Run, essential refund-cap failure. Output: labeled status table/chart and No-Go recommendation with the business reason first.

## Handoff

28 for release gate review, 33 for approved publication, 99 CTO walkthrough for a fixture.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
