---
name: review-coverage-and-traceability
description: "Check whether stories, risks, cases, results and defects form an auditable evidence chain."
---

# 11 · Review coverage and traceability

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Check whether stories, risks, cases, results and defects form an auditable evidence chain.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Scope baseline, AC/risk inventory, cases, run/evidence ledger, defects and release gates as available.

## Procedure

1. Build stable links from story revision → AC/risk → case version → run/build → evidence → defect → fix/retest → release decision. Preserve many-to-many relations rather than duplicating results.
2. Find uncovered confirmed criteria, risks with no tests, orphan cases and gaps in negative/permission/data/state/integration coverage. Separate intentionally excluded requirements from accidentally missing coverage.
3. Review case quality, expected outcomes and applicability decisions. A case title alone is not coverage; a designed case is not execution evidence.
4. Flag Pending definition, blocked environment, missing evidence and stale runs separately. A changed criterion may require redesign and rerun; unchanged tests may remain informative if impact analysis explicitly justifies reuse.
5. Calculate design and execution coverage only against a defined baseline. Report the uncovered essential criteria individually even if aggregate percentages look favorable.
6. Record reviewer decisions and required corrections. Keep prior baselines so a later scope change does not silently rewrite historical coverage.

## Required output

Traceability matrix: Story/revision | AC/risk | Case/version | Definition status | Latest applicable run/build | Evidence | Defect | Retest | Gate. Include gap list with owner and due decision.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

No fabricated links to unavailable artifacts. Distinguish all criteria, confirmed testable criteria and essential criteria denominators.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Application boundary

Apply this procedure to the actual product sources and current scope. Missing rules remain Pending definition; proposed work is not executed evidence.

## Handoff

04/10 for gaps, 24 for impacted reruns, 26 for metrics, 28 for gates.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
