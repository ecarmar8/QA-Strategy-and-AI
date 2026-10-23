---
name: orchestrate-testing-lifecycle
description: "Coordinate a complete or partial QA engagement, resume a checkpoint, or explain the lifecycle to leadership."
---

# 00 · Orchestrate the testing lifecycle

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Coordinate a complete or partial QA engagement, resume a checkpoint, or explain the lifecycle to leadership.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Business objective; requested mode; available sources and tools; product surfaces; release or iteration scope; existing authorization and artifacts. Missing tools do not prevent offline analysis.

## Procedure

1. Read README.md, 90-OPERATING-CONTRACT.md and the user request. Establish the mode and reuse authorization already present in the session. Discover actual capabilities; never assume an Azure connector or Playwright runtime exists.
2. Create a stage plan with artifact owners and entry/exit conditions. Start with 01–03 for connected discovery, or supplied fixtures for offline work. Apply 31 and 32 throughout.
3. Run 04–08 to establish testable requirements, domain models, risk and strategy. Return unresolved business decisions to the product owner; continue independent analysis while dependent cases stay Pending definition.
4. Run 09–13 for planning, case design, coverage, data and environment readiness. Build the requirement-to-evidence chain before execution.
5. When authorized and ready, run smoke (14), manual/API/data/nonfunctional tracks (17–21), with automation decisions and design (15–16). For Playwright MCP, first use skill 34 to verify the actual connection and tool capabilities, then skill 20 to execute. Treat the optional CLI route separately. Desktop execution must use compatible tooling. Use 25 only when an actual CI context exists.
6. Route any failure through 22, then 23 and 24 after a fix. Preserve initial failures and subsequent runs. Do not interpret a retry as deletion of a defect.
7. Use 26–28 for metrics, visual reporting and the QA release recommendation. The authorized release owner makes the release decision. Use 29 only for an authorized release context, then 30 for closure and learning.
8. Publish through 33 only within explicit Azure write authorization. Save a checkpoint after each stage, on a blocker and before context handoff; load only the next relevant skills.

## Required output

Stage plan: Stage | Skills | Owner | Input artifacts | Output artifacts | Entry gate | Exit evidence | Status. Finish with checkpoint, immediate next action, blockers and decisions needed.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

No execution without a valid environment/authorization; no Go with missing essential evidence; no invented live results. Numbering is guidance: skip inapplicable tracks with reasons and return to prior stages when requirements change.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Small example

Input: “Assess these three remittance stories; no environment yet.” Output: CONNECTED_READ or supplied-text analysis; design may proceed; execution Not Run; environment and authorization pending; no release approval.

## Handoff

01 for access, 02 for supplied backlog, or the stage indicated by the checkpoint.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
