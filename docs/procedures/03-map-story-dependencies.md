---
name: map-story-dependencies
description: "Determine which stories depend on others, identify blocking chains and sequence testing."
---

# 03 · Map story dependencies and execution order

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Determine which stories depend on others, identify blocking chains and sequence testing.

## Shared contract

Read [docs/operating-contract.md](../operating-contract.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Backlog snapshot with relation metadata; verified business/interface dependencies; allowed project scope; links to external systems where supplied.

## Procedure

1. Read the relation type and its documented forward/inverse semantics from the deployment. Normalize every confirmed dependency as prerequisite → dependent. Preserve the raw relation and endpoints as evidence.
2. Classify edges as Confirmed explicit, Confirmed by owner, or Candidate inferred. Parent/Child and Related links alone do not prove a blocking dependency. A shared component may indicate impact rather than execution order.
3. Inspect supplied criteria and contracts for prerequisite data, APIs, state transitions, shared environments, deployment sequencing and external providers. Describe the failure mode that makes each candidate relevant, and ask the appropriate owner to confirm it.
4. Detect self-links, contradictory directions and cycles. Do not produce a topological ordering for a cyclic graph; isolate the cycle for refinement. Treat unreadable linked items as Unknown external dependency, not completed prerequisites.
5. For a validated acyclic graph, produce a staged execution order and parallelizable branches. Mark the prerequisite evidence each dependent requires, including environment or provider readiness.
6. Render a compact Mermaid graph of confirmed edges and a separate candidate table. Keep unknown or inferred dependencies out of the confirmed graph unless explicitly labeled.

## Required output

Edge ledger: Edge ID | Prerequisite | Dependent | Raw relation | Source/revision | Confidence | Blocking condition | Owner | Status. Also output cycle findings, staged order and candidate questions.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [docs/templates.md](../templates.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass.

## Quality checks and boundaries

Every arrow has evidence and an unambiguous direction. Item state Done does not by itself prove its deployed behavior is ready. Do not read another project outside authorized scope merely because it is linked.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Application boundary

Apply this procedure to the actual product sources and current scope. Missing rules remain Pending definition; proposed work is not executed evidence.

## Handoff

04 for clarification, 07 for risk, 09 for sequencing, 24 for impact.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
