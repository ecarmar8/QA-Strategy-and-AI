---
name: execute-api-and-integration-tests
description: "Validate APIs, service contracts, asynchronous integrations or provider sandboxes."
---

# 17 · Execute API and integration tests

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Validate APIs, service contracts, asynchronous integrations or provider sandboxes.

## Shared contract

Read [docs/operating-contract.md](../operating-contract.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

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

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [docs/templates.md](../templates.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass.

## Quality checks and boundaries

Use the actual safe target and workload scope. A successful HTTP response without the required business/data effect cannot satisfy an integrity assertion.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Application boundary

Apply this procedure to the actual product sources and current scope. Missing rules remain Pending definition; proposed work is not executed evidence.

## Data-heavy integration and cross-service contract depth

For each actual provider/operation, confirm pagination/completeness, mappings, schema/version changes, required versus missing/null fields, timestamp/precision semantics, authentication expiry, limits and documented throttling/error behavior. Verify bounded retry/backoff, duplicate/reordered inputs, partial processing, recovery/replay and downstream consistency where applicable. Do not assume a particular status code, retry count or freshness window.

Trace the input through transformation/storage to the actual consuming process; inspect actual records and independent expected values. Separate controlled fault stubs, provider sandbox and actual integration evidence. Across .NET/Python or other heterogeneous services, assess actual serialization/null/date/numeric contracts and version compatibility rather than assuming language defaults agree.

## Handoff

18 for persisted-data validation, 22 for failures, 24 for regression.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
