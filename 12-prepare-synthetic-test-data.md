---
name: prepare-synthetic-test-data
description: "Define safe, reproducible data for functional, automation, financial or nonfunctional testing."
---

# 12 · Prepare and control test data

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Define safe, reproducible data for functional, automation, financial or nonfunctional testing.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Case requirements, approved environment, data constraints, currency/precision rules and cleanup/retention policy.

## Procedure

1. Map each case to accounts, roles, balances, lifecycle states, provider fixtures and negative/boundary values. Use synthetic identities and nonproduction provider modes.
2. Separate data values chosen for illustration from confirmed product limits. Generate values with decimal/minor-unit precision matching the approved currency; record time zones and controllable clocks where relevant.
3. Define setup, reservation/isolation, reset and cleanup steps. Give concurrent or parallel runs unique operation IDs and isolated balances so one test cannot corrupt another test oracle.
4. For migrated or reconciled data, specify baseline snapshots and independent totals. Use approved masking if existing data must be sampled; never assume production data is allowed.
5. Identify personal data, secrets and sensitive financial fields; redact logs and reports without destroying necessary correlation. Define access and evidence retention from supplied policy, otherwise ask the owner.
6. Execute setup/cleanup only within authorized test scope. Record generated records and cleanup outcome; leave blocked rather than fabricate a seeded environment.

## Required output

Data catalog: Dataset ID | Cases | Synthetic values/state | Source rule | Setup | Isolation | Owner | Cleanup | Retention | Status. Include secret references by name only, never secret values.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

No real funds/customer identities by default; no destructive SQL against shared data. If cleanup fails, report residual records and affected reruns.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Small example

Input: concurrent USD70 refunds against USD100. Output: isolated synthetic payment and two distinct operation identities; clean/reset after run; no reuse of another test’s balance.

## Handoff

13 then relevant execution skills; 18 for controlled data checks.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
