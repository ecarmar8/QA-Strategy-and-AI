---
name: analyze-acceptance-criteria-and-refine
description: "Review incomplete, complex or ambiguous user stories and prepare actionable refinement questions."
---

# 04 · Analyze acceptance criteria and refine stories

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Review incomplete, complex or ambiguous user stories and prepare actionable refinement questions.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Versioned story text, current AC, business glossary, design/contracts and confirmed stakeholder answers. Scope boundaries and product owner if known.

## Procedure

1. Separate the business objective, user role, trigger, preconditions, rules, observable outcomes and exclusions. Label each statement Confirmed, Observed, Proposed or Pending question.
2. Build an applicability scan for create/read/update/delete, required/optional fields, permissions, search, filters, grids/sort/pagination/export, reports, APIs, states, approvals, audit and integrations. Mark Not applicable with a reason; do not force CRUD onto every workflow.
3. Test criteria for ambiguity, inconsistency, missing negative paths, data boundaries, concurrency, recoverability and observable evidence. Identify where an implementation detail has been mistaken for a business rule.
4. For a complex story, propose vertical slices with independently valuable outcomes and traceable boundaries. For an incomplete story, identify the smallest missing decision that blocks expected results. Do not invent minimum lengths, roles, statuses, HTTP codes or limits.
5. Prioritize questions by effect on money, access, data integrity, dependencies and testability. For each question, identify decision owner, affected cases and consequence of leaving it unresolved.
6. Propose revised Given/When/Then criteria as recommendations. Record product-owner acceptance separately; an LLM suggestion does not become a requirement until confirmed. Keep dependent cases Pending definition / Not Run until clarified.

## Required output

Refinement matrix: AC/Gap ID | Source | Confirmed rule | Gap/question | Business impact | Proposed wording | Decision owner | Status | Affected cases. Finish with Ready for design / Partially ready / Blocked and reasons.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

All suggested criteria are labeled Proposed. Contradictory sources require resolution, not a silent choice. Continue independent coverage work while blocking only affected scenarios.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Application boundary

Apply this procedure to the actual product sources and current scope. Missing rules remain Pending definition; proposed work is not executed evidence.

## Handoff

05–07; after answers, version the story and revisit 10–11.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
