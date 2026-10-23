---
name: close-testing-and-improve-process
description: "Close an iteration/release QA effort and turn evidence into practical improvements."
---

# 30 · Close testing and improve the process

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Close an iteration/release QA effort and turn evidence into practical improvements.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Final scope, run/defect/release records, residual risks, incidents, effort and team feedback.

## Procedure

1. Reconcile planned versus actual scope, evidence, unresolved defects, cleanup and release decisions. Separate QA closure from release approval and from closing every defect.
2. Archive traceability, sanitized evidence, metric definitions, outstanding risks and ownership according to supplied retention/access policy. Confirm that secrets and unneeded personal data are excluded.
3. Review escapes, delays, flaky tests, unclear criteria, environment/data issues and dispute outcomes using a blameless causal discussion. Separate facts, hypotheses and verified contributing causes.
4. Identify a small prioritized improvement backlog tied to business effect: better refinement, deterministic data, stronger reconciliation oracle, testability hooks or ownership clarity.
5. Give each action an owner, expected outcome, baseline/measurement, due/review point and success criterion. Avoid unsupported claims of percent efficiency gain.
6. Feed lessons into strategy, skill instructions, cases and mentoring. Changes to the user’s personal skill library remain a proposal unless editing/installing it is authorized.

## Required output

Closure report: Scope/evidence summary; open risks/defects and owners; cleanup/archive status; decision record; lessons; improvement table with baseline, owner and review date.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

Do not delete failure history during cleanup. No declaration of zero residual risk. Keep improvement measures realistic and observable.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Small example

Input: repeated retest delay caused by unclear build tags. Output: action to expose build ID in the test environment, owner engineering lead, measure blocked retest time next iteration.

## Handoff

08/09/16/31 for improvements; 00 for next cycle.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
