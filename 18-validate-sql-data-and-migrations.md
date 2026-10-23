---
name: validate-sql-data-and-migrations
description: "Check persisted effects, reconciliation, migration correctness or data quality."
---

# 18 · Validate SQL, data integrity and migrations

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Check persisted effects, reconciliation, migration correctness or data quality.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Approved read-only data access or sanitized extracts, actual schema/data dictionary, source-target mapping, financial rules and migration scope.

## Procedure

1. Inspect actual schema and authorized datasets. Prefer read-only least-privilege access and bounded queries. Never invent table names or execute a mutation based on an illustrative query.
2. Define source-target checks for counts, unique keys, nullability, referential integrity, formats, state mappings, precision and business totals. Pair aggregate checks with targeted row-level samples and exception investigation.
3. For monetary effects, compare confirmed ledger/capture/refund/payout invariants by currency and reconciliation scope. Do not add unrelated currencies without a defined conversion rule.
4. For migrations, capture baseline, transformation rules, exclusions, reconciliation tolerances and cutover/rollback requirements supplied by owners. Distinguish accepted transformation from data loss.
5. Use read consistency and timing appropriate to the system. Record snapshot/time and expected eventual consistency window if confirmed. Consider time zones, rounding, duplicates and retry side effects.
6. Save sanitized query references/results, scope limits and discrepancies. Data repair, schema changes, backfills and destructive cleanup require explicit separate authorization and a reviewable plan.

## Required output

Data assurance report: Check ID | Rule/source | Dataset/snapshot | Actual query/reference | Expected | Actual | Difference | Tolerance/source | Evidence | Result | Owner.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

No production writes or full sensitive exports implied by QA analysis. A matching row count alone does not prove migration correctness. Unknown tolerance remains pending.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Small example

Input: equal source/target row counts but two refund records lose currency precision. Output: count check passes, precision invariant fails with sampled evidence; migration not declared correct.

## Handoff

22 for discrepancies, 26–28 for metrics/release evidence.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
