---
name: design-functional-test-cases
description: "Turn confirmed requirements and risks into clear manual or automation-ready test cases."
---

# 10 · Design functional test cases

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Turn confirmed requirements and risks into clear manual or automation-ready test cases.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Versioned stories/AC, business and state models, risk register, interfaces, permitted data and environment assumptions.

## Procedure

1. Create stable case IDs linked to story/AC/risk and source revision. Choose positive, negative, boundary, equivalence, decision-table and transition techniques where meaningful.
2. Apply the functional applicability scan: CRUD, mandatory/optional fields, permissions, search, filters, grids, sorting, pagination, export, reports, APIs, audit and integrations. Explain Not applicable entries.
3. Define objective, business priority and reason, preconditions, synthetic data, ordered actions, observable expected outcomes and cleanup. Expected results must verify state/data/financial effects where relevant, not just messages or HTTP status.
4. Keep steps reproducible without invented selectors, endpoints or credentials. Reference an observed interface or actual contract; otherwise mark the interface binding Pending.
5. Separate a case definition from each run result. Unknown requirements yield Pending definition and execution Not Run, with the exact blocking question. Do not manufacture an expected outcome to complete a table.
6. Review redundancy, independence and necessary end-to-end combinations. Mark automation suitability as a proposal for 15 rather than automatically converting every case into code.

## Required output

Case fields: ID; story/AC/source revision; goal; risk; priority/reason; definition status; preconditions; data; numbered steps; observable expected results; postconditions/cleanup; proposed execution method. Initial execution status is Not Run.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

One clear objective per case; clear oracle for every assertion; traceable assumptions. Keep synthetic values distinct from confirmed business limits.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Application boundary

Apply this procedure to the actual product sources and current scope. Missing rules remain Pending definition; proposed work is not executed evidence.

## Handoff

11 for review, 12–13 for readiness, 15 for automation selection.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
