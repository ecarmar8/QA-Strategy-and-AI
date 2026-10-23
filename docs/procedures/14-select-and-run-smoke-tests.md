---
name: select-and-run-smoke-tests
description: "Quickly assess build testability before deeper regression or specialized testing."
---

# 14 · Select and run smoke tests

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Quickly assess build testability before deeper regression or specialized testing.

## Shared contract

Read [docs/operating-contract.md](../operating-contract.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Ready environment, approved execution scope, build identifier, essential journey list and stable smoke cases/data.

## Procedure

1. Select a small risk-based set proving access, core journey availability, a key integration and a basic persisted effect. Keep it quick and diagnostic; do not call a full regression smoke.
2. Confirm current target/build, data and cleanup. Execute through actual available tools or supervised manual steps; record who performed each action and its evidence.
3. Validate the business effect, not just page load or a 200 response. Record run-level Passed, Failed, Blocked, Not Run or Not Applicable according to 90.
4. If smoke fails, diagnose product versus environment/setup failure. Raise a defect only with supporting evidence and route environment blockers to their owner.
5. Recommend whether each track can proceed. A failed essential smoke blocks dependent testing; independent design/review can continue. Do not rerun repeatedly until green without retaining the first result and explanation.
6. Summarize duration, results, blocking evidence and next checkpoint for the team.

## Required output

Smoke run: Run ID | Case/version | Build/environment | Started/ended UTC | Result | Evidence | Blocker/defect | Cleanup. Finish with Proceed / Proceed on independent tracks / Stop dependent execution.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [docs/templates.md](../templates.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass.

## Quality checks and boundaries

A smoke pass establishes basic readiness, not release approval. Missing test tools yields Not Run or Blocked, never a simulated pass in connected mode.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Application boundary

Apply this procedure to the actual product sources and current scope. Missing rules remain Pending definition; proposed work is not executed evidence.

## Handoff

17–21 when ready; 22 for failures, 13 for environment blockers.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
