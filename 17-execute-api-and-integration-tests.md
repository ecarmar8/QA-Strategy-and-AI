---
name: execute-api-and-integration-tests
description: "Validate APIs, service contracts, asynchronous integrations or provider sandboxes."
---

# 17 · Execute API and integration tests

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Validate APIs, service contracts, asynchronous integrations or provider sandboxes.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Actual API schema/collection and business oracle; authorized nonproduction target; identity/scopes; data; provider behavior and allowed workload.

## Procedure

1. Bind cases to actual methods, routes, parameters, payloads and response schemas. Use available API tooling, Postman or Playwright request context where appropriate. If bindings are missing, stop execution and provide a binding checklist.
2. Check authentication, authorization, validation, state transitions and business effects. Only expect specific HTTP/error codes when the contract confirms them; a plausible code is not a requirement.
3. Test idempotency, timeout/unknown outcomes, retry behavior, duplicate/out-of-order callbacks, concurrency and partial failures within approved scope. Use provider simulation only when supported and label it distinct from real sandbox integration.
4. Validate downstream persisted state, ledger/audit effects and reconciliation with correlation IDs. For asynchronous work, use bounded polling based on a supplied contract/window; unresolved timing is a question, not an arbitrary failure threshold.
5. Capture sanitized request/response metadata, actual results, build and dependency versions. Avoid tokens, personal data and financial account exposure.
6. Classify failures with evidence and clean created records. Compare producer/consumer expectations and provider responsibility before assigning blame.

## Required output

API run record: Case/run | Contract version | Method/route reference | Sanitized input | Expected source | Actual response/business effect | Correlation ID | Result/evidence | Cleanup.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

Never send real transfers or production load by default. A successful HTTP response without verified business effect cannot satisfy a financial invariant.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Small example

Input: approved sandbox replay case with real contract binding. Output: two attempts with same operation identity and one financial effect, if observed; otherwise record the actual failure/unknown evidence.

## Handoff

18 for persisted-data validation, 22 for failures, 24 for regression.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
