---
name: model-business-processes-and-states
description: "Translate complex journeys into testable state, decision and integration models."
---

# 05 · Model business processes and state transitions

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Translate complex journeys into testable state, decision and integration models.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Refined stories, approved lifecycle states, actor/permission matrix, interface contracts, dependency ledger and unresolved questions.

## Procedure

1. Map actors and system boundaries for UI/web/desktop, API, ledger, provider and back-office operations. Distinguish a user action from an asynchronous provider response.
2. Extract only confirmed states, allowed transitions, guards, irreversible actions and terminal conditions. For every transition identify the command/event, prior state, resulting state, persisted effect and audit evidence.
3. Build decision tables for interacting rules, equivalence classes and boundary partitions where justified. Include invalid transitions, duplicate/out-of-order events, retries, partial failures and cancellation only when relevant.
4. Map end-to-end journeys across components and reconciliation checkpoints. Identify eventual consistency windows only when specified; otherwise ask how completion is observed and when a timeout becomes a failure.
5. Review models with business and technical owners. Separate a desired business state from an observed implementation state; neither silently overwrites the other.
6. Use a compact Mermaid state diagram or flowchart and an accompanying transition table. Model uncertain states as questions outside the confirmed graph.

## Required output

Transition model: Transition ID | Prior state | Trigger | Guard | Next state | Financial/data effect | Observable evidence | Source | Negative transition. Include decision table and journey checkpoints.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

Every modeled transition has a source. Unknown provider timing is not an invented SLA. Do not equate HTTP success with a completed financial transaction.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Small example

Input: confirmed Submitted → ProviderPending → Settled, with retry behavior unspecified. Output: model these states; add a retry/idempotency question; create a pending duplicate-event scenario.

## Handoff

06 for money invariants, 10 for cases, 17 for integration execution.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
