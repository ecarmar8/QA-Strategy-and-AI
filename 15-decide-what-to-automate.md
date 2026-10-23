---
name: decide-what-to-automate
description: "Prioritize automation investment and explain exclusions or deferrals."
---

# 15 · Decide what to automate and what to keep manual

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Prioritize automation investment and explain exclusions or deferrals.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Case inventory, risk, execution frequency, stability, data/isolation, observability, maintenance capacity and actual tool capabilities.

## Procedure

1. Assess each candidate by business risk, repeatability, frequency, deterministic oracle, environment/data control, interface stability and maintenance cost. Explain the reasoning rather than assigning invented ROI.
2. Prioritize repeatable financial invariants, API contracts, critical regressions and stable happy/negative paths where automation provides reliable feedback. Evaluate component/API level before costly end-to-end UI coverage.
3. Keep discovery, exploratory learning, nuanced usability and uncertain requirements under manual judgment. Defer unstable flows, one-off checks or poorly observable outcomes until testability improves; do not equate manual with low priority.
4. Choose a suitable interface: Playwright for supported web contexts, experimental Electron only after compatibility assessment, appropriate approved tooling for native desktop, API/data tooling for service effects.
5. Define a pilot, expected feedback, ownership and maintenance plan. Flag flaky candidates, third-party dependencies and human MFA as design constraints rather than workarounds to bypass.
6. Review automation value after use: defect/risk feedback, run reliability, maintenance effort and cycle-time change. Do not set automation percentage as an end in itself.

## Required output

Decision table: Case/risk | Automate now / Pilot / Defer / Manual | Reason | Best level/tool capability | Preconditions | Oracle | Maintenance owner | Review trigger.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

No blanket “automate everything.” No promise that Playwright controls all desktop applications or native dialogs. Do not count proposed automation as implemented coverage.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Small example

Input: stable API idempotency rule and a changing desktop layout. Output: prioritize API regression; desktop exploration/manual now; reassess automation after runtime and UI stabilize.

## Handoff

16 for approved candidates; 19 for manual work; 04 for unknown rules.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
