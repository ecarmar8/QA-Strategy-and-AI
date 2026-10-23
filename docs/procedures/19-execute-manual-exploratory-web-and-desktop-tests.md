---
name: execute-manual-exploratory-web-and-desktop-tests
description: "Run supervised manual cases or exploratory sessions across UI, web and desktop surfaces."
---

# 19 · Execute manual and exploratory web/desktop tests

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Run supervised manual cases or exploratory sessions across UI, web and desktop surfaces.

## Shared contract

Read [docs/operating-contract.md](../operating-contract.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Ready cases/charters, authorized target/build, roles/data, application runtime and actual available human or UI-control capability.

## Procedure

1. Choose scripted execution for confirmed outcomes and exploratory charters for uncertainty. Define charter mission, risks, data, timebox and observable outcomes without inventing requirements.
2. Inspect the actual UI and navigate by observed controls. For web and desktop cover workflow, state, permissions, validation, navigation, error recovery and persisted effects as applicable.
3. For desktop, identify native versus Electron/web shell, OS/version, install/update behavior, focus/keyboard, local storage/offline/integration concerns only where relevant. If no compatible native control exists, provide human execution steps and mark the LLM-run status Not Run.
4. Capture session notes: actions, observations, questions, evidence and reproducibility. Record actual results separately from interpretation and expected behavior. An observation with no approved expectation may be a finding/question rather than a confirmed defect.
5. Use pair testing or a reviewer on high-risk financial/access paths. Validate underlying data/effects where permitted, not just visual appearance.
6. Debrief with coverage achieved, new risks, unresolved questions and follow-up cases. Redact screenshots and record cleanup.

## Required output

Manual run ledger plus exploratory session: Charter | Build | Tester | Timebox | Areas/actions | Evidence | Findings/questions | Coverage | Follow-up. Human-reported results must identify their provenance.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [docs/templates.md](../templates.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass.

## Quality checks and boundaries

Do not claim to have clicked, observed or tested an unavailable surface. No desktop automation promise from a web-only capability. Treat accessibility/usability judgments carefully and state scope.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Application boundary

Apply this procedure to the actual product sources and current scope. Missing rules remain Pending definition; proposed work is not executed evidence.

## Handoff

22 for defects, 04 for ambiguous expectations, 24 for regression.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
