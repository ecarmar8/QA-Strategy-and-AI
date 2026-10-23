---
name: coordinate-ci-and-continuous-validation
description: "Design or run automated feedback in an existing authorized delivery pipeline."
---

# 25 · Coordinate CI and continuous validation

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Design or run automated feedback in an existing authorized delivery pipeline.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Actual repository/pipeline, test suite/tags, runtime, safe target/environment, secret handling, ownership and approved mutation scope.

## Procedure

1. Inspect pipeline conventions and available runners. Plan fast deterministic checks near changes and slower integration/end-to-end/nonfunctional checks at suitable checkpoints based on risk and environment constraints.
2. Define triggers, test selection, target build binding, isolated data, concurrency and dependency availability. Do not silently run transaction tests on a default production endpoint.
3. Configure secret references and sanitized result/artifact publication only if repository/pipeline edits are authorized. Otherwise provide a reviewable configuration proposal rather than claiming deployment.
4. Define gating behavior for assertion failures, infrastructure errors, blocked essential tests and flaky/quarantined checks. A pipeline green badge with skipped essential tests is not release evidence.
5. Preserve attempt-level outcomes, logs, build/commit references and retention rules. Retries must remain visible; quarantine requires owner, impact and expiry.
6. For an authorized run, collect actual results and compare with the intended scope. Triggering a pipeline that can deploy needs release-specific authority; test authorization alone does not grant it.

## Required output

Pipeline validation plan/run: Stage/trigger | Suite | Build target | Runtime | Data/isolation | Secret reference | Gate | Artifact | Owner | Actual run/reference | Limitation.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

Do not invent pipeline IDs or supported tasks. No pipeline changes or deployment by implication. Headless execution is appropriate when its CI context is configured and authorized.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Small example

Input: tests exist but no pipeline write scope. Output: proposed stages and gates in Markdown; existing run read only; no YAML mutation or pipeline trigger.

## Handoff

26–28; 16 for flake/design issues; 33 for approved Azure result publication.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
