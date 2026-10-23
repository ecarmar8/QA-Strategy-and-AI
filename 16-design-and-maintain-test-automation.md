---
name: design-and-maintain-test-automation
description: "Specify or improve an automation suite after candidates and runtime are selected."
---

# 16 · Design and maintain test automation

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Specify or improve an automation suite after candidates and runtime are selected.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Approved automation decisions, observed app/repository conventions, actual contracts/DOM, runtime/toolchain, test data and authorized target.

## Procedure

1. Inspect existing tests, shared fixtures and repository instructions before proposing a design. Reuse compatible conventions and dependencies; do not create a framework simply because none was requested.
2. Map cases to focused tests with explicit arrange/action/assert/cleanup responsibilities. Separate business assertions, environment configuration, data builders and reusable interface interactions without excessive abstraction.
3. Choose deterministic assertions and independent data. Use actual selectors/contracts and controlled waits; avoid fixed sleeps as synchronization, test ordering dependencies and hidden production URLs.
4. Design safe configuration with secret references, tagged suites, build metadata and failure evidence. Keep web, API and compatible desktop runners explicit rather than promising a single universal tool.
5. Define flake diagnosis, retry reporting and quarantine rules with owner, business impact and expiry. Quarantining a critical check leaves a visible assurance gap, not a green release.
6. If implementation is requested and authorized, produce code in the actual project and verify focused tests. Otherwise deliver a design/binding plan and mark implementation Pending. Review maintenance when app behavior changes.

## Required output

Automation design: Case IDs | Test location/proposal | Interface binding | Fixtures | Assertions/oracle | Cleanup | Evidence | Tags | Owner. Include flake/maintenance register and implementation status.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

Do not generate runnable claims from unobserved selectors or nonexistent endpoints. Retries preserve attempt results. This skill library itself is instructions, not a delivered automation application.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Small example

Input: no repository but confirmed API contract. Output: proposed test design and required runtime/bindings; no assertion that a suite was installed or executed.

## Handoff

17/20 for execution; 25 for integration; 32 for review.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
