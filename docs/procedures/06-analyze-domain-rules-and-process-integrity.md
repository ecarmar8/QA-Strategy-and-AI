---
name: analyze-domain-rules-and-process-integrity
description: Extract confirmed business rules, invariants, state constraints and integrity expectations for the actual domain in any product or enterprise process.
---

# 06 · Analyze domain rules and process integrity

Read [docs/operating-contract.md](../operating-contract.md). Use actual product sources and owner decisions; do not import rules from a different industry. Apply 32 for source review.

## Inputs

Process/state model, actors, data entities, contracts, business rules, known incidents and domain decision owners. Record missing sources explicitly.

## Procedure

1. Identify the process goal, authorized actors, inputs, outputs, lifecycle states and affected entities. Confirm the scope with available evidence.
2. Extract invariants: what must remain true before/after each operation, which transitions are allowed, which records must agree and which actions require permission. Define the independent oracle from confirmed rules.
3. Assess missing, invalid, duplicate, repeated, concurrent or reordered inputs and dependency failures only where relevant. Confirm retry, conflict and recovery semantics rather than inventing them.
4. Review calculations, precision, units, time zones, effective dates, ownership and auditability where the process uses them. Route missing definitions to their actual owner.
5. Confirm data-scope, privacy and external obligations with the appropriate owners. Do not infer jurisdictional or regulatory rules from a domain label.
6. Link failure scenarios to risks, required controls and verification at the appropriate level. Separate current behavior, confirmed rule and proposed protection. Keep unknown expected results Pending definition.

## Required output

Rule/invariant ID | Process/state | Confirmed source/revision | Failure consequence | Control | Verification/oracle | Dependency | Priority reason | Open decision/owner.

Link to 07–08 and 10 for risk, strategy and coverage. Return unresolved rules to 04. No rule or compliance claim may be fabricated. Save source references and current scope in the checkpoint.
