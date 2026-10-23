---
name: assess-and-execute-nonfunctional-tests
description: "Plan or execute proportionate performance, resilience, security, accessibility and compatibility checks."
---

# 21 · Assess and execute nonfunctional tests

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Plan or execute proportionate performance, resilience, security, accessibility and compatibility checks.

## Shared contract

Read [docs/operating-contract.md](../operating-contract.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Risk-based scope, service objectives/requirements, architecture, specialist ownership, authorized environment/workload and observability. Explicit approval for load, fault injection or security probing.

## Procedure

1. Choose relevant dimensions from performance/capacity, resilience/recovery, security/access, accessibility, compatibility and usability. Separate QA baseline checks from specialist assessment and formal certification.
2. Define a measurable requirement, workload/profile, environment, data, measurement point and acceptance source for each check. If no objective exists, propose one for owner review; do not invent a contractual threshold.
3. For performance, specify concurrency/arrival rate, mix, duration, warmup, p50/p95/p99 as appropriate, error categories and resource context. Avoid comparing production and small sandboxes as equivalent.
4. For resilience, specify permitted fault, expected recovery/data integrity, stop conditions and rollback contact. For security, stay within explicit scope and approved techniques; for accessibility, state reviewed criteria/method and remaining manual/specialist work.
5. Execute only with compatible tooling and authorized bounds. Monitor limits and stop on unexpected customer impact or scope breach. No stress tests against production by implication.
6. Report method, sample size, limitations and evidence. Compare to confirmed targets; distinguish observation from pass/fail when requirements are pending.

## Required output

Nonfunctional plan/report: Dimension | Risk | Requirement/source | Method/tool | Profile | Environment | Bounds/stop rule | Measurement | Target | Actual | Verdict/limitation | Owner.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [docs/templates.md](../templates.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass.

## Quality checks and boundaries

No “secure/compliant/accessibility certified” claim from a few checks. No pass where target or measurement is absent. Functional login access does not authorize load/security testing.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Application boundary

Apply this procedure to the actual product sources and current scope. Missing rules remain Pending definition; proposed work is not executed evidence.

## Scope-specific assurance boundaries

Separate business turnaround from technical processing/response targets. Confirm load models and actual service objectives before evaluating k6/JMeter or existing performance tooling. For accessibility, agree the standard/version/level and combine automated findings with manual assessment; no tool alone establishes conformance (https://www.w3.org/WAI/test-evaluate/). For regulated work, confirm actual firm/activity scope and obligations with responsible owners; a registration label alone does not establish every applicable rule.

## Handoff

04 for missing objectives, 22 for findings, 28 for essential gate impact.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.

## Test-type and implementation map

Use [the full test-type matrix](../test-types.md) to select performance, scalability, resilience, recovery, security, privacy, accessibility, compatibility and operational checks. The local automated subset and remaining product/specialist work are explicit. Do not treat the catalog as evidence of execution.
