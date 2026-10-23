---
name: verify-fixes-and-reopen-defects
description: "Retest a claimed fix, validate related behavior and decide whether a defect can close."
---

# 23 · Verify fixes and reopen defects

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Retest a claimed fix, validate related behavior and decide whether a defect can close.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Defect/source evidence, fix build/commit, changed components, expected behavior, authorized environment/data and linked cases.

## Procedure

1. Check that the actual target contains the claimed fix and that prerequisites/data reproduce the original condition. A status of Fixed is not proof.
2. Execute the original minimal reproduction and linked case under the same relevant conditions. Compare actual business and persisted effects against the confirmed rule.
3. Add targeted negative/boundary variants around the changed behavior. Use 24 to select related regression based on components, dependencies and financial invariants.
4. Preserve the initial failure, fix reference, retest result and evidence as separate records. If the original issue persists, reopen with exact build and reproduction; if a distinct issue appears, link a separate defect.
5. Recommend closure only when the agreed verification evidence exists and impacted essential regression is satisfied. If a prerequisite is missing, record Retest Blocked rather than closing.
6. Update remote workflow only through authorized writeback and actual configured states.

## Required output

Fix verification: Defect | Fix reference/build | Original case/run | Retest run/evidence | Targeted regression | Result | Reopen/close recommendation | Remaining risk | Reviewer.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

No closure from a developer statement alone. Do not overwrite the original failure with a passing retest. Changed build invalidates affected earlier evidence.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Small example

Input: excess-refund defect marked Fixed, target still old build. Output: Retest Blocked; request correct build; no closed status.

## Handoff

24 for related regression; 26–28 after evidence; 33 for authorized updates.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
