---
name: verify-test-environment-readiness
description: "Determine whether a target build and its dependencies are ready for trustworthy execution."
---

# 13 · Verify test environment readiness

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Determine whether a target build and its dependencies are ready for trustworthy execution.

## Shared contract

Read [docs/operating-contract.md](../operating-contract.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Environment URL/runtime, build/version/commit, allowed actions, accounts, provider configuration, data catalog, observability and rollback/cleanup contacts.

## Procedure

1. Confirm environment identity and nonproduction scope before any transaction. Record build, configuration, feature flags and dependency versions visible through authorized tools.
2. Check access/roles, connectivity, API/contract availability, browser/desktop compatibility, test data and provider sandbox status. Verify that necessary logs/correlation IDs are available without exposing secrets.
3. Inspect isolation and shared-environment constraints, rate limits and execution windows. Separate environment failure from product failure and record unresolved dependencies.
4. Confirm authorized workload, mutation scope, budget/volume and cleanup for planned tests. Security/load/fault testing requires its own explicitly permitted scope, not just an ordinary login.
5. Create a readiness decision per track. A missing desktop tool can block desktop automation while manual review and API design proceed.
6. Record expiry/invalidators: new build, changed flag/schema, provider outage, account role change or data reset. Revalidate affected gates after changes instead of reusing stale evidence.

## Required output

Readiness checklist: Check | Target/build | Expected/source | Observed/evidence | Status | Owner | Impacted tracks | Recheck trigger. Overall Ready / Partially ready / Blocked.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [docs/templates.md](../templates.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass.

## Quality checks and boundaries

No readiness claim from reachability alone. Do not leak health payloads or credentials. Do not approve execution against an unidentified target.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Application boundary

Apply this procedure to the actual product sources and current scope. Missing rules remain Pending definition; proposed work is not executed evidence.

## Handoff

14 for smoke; 09/00 for rescheduling.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
