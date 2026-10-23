---
name: select-and-execute-impact-based-regression
description: "Choose regression scope after a fix, story change, integration update or release candidate."
---

# 24 · Select and execute impact-based regression

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Choose regression scope after a fix, story change, integration update or release candidate.

## Shared contract

Read [docs/operating-contract.md](../operating-contract.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Change/fix diff or reliable summary, dependency graph, risk/case inventory, build/environment and prior evidence.

## Procedure

1. Map changes to business rules, components, contracts, data schema, feature flags and provider behavior. If the diff is unavailable, widen uncertainty explicitly and seek an owner’s impact assessment.
2. Traverse confirmed dependencies and affected journeys; use candidate dependencies as investigation prompts. Consider shared components and financial invariants across UI/API/data, not only the changed screen.
3. Select a core essential suite plus targeted impacted tests and justified exploratory checks. Record why each case is included, excluded or stale. Do not pick solely by previous failures or code coverage.
4. Recheck readiness and data, execute authorized selected cases, and preserve results by current build and attempt. Treat blocked/not-run essential cases as open evidence gaps.
5. Compare baseline and current results without deleting history. Investigate new failures via 22 and feed changed expectations through 04/10.
6. Summarize coverage achieved and residual risk for release. Request broader execution only when evidence or unresolved impact justifies it.

## Required output

Regression selection: Change | Impacted rule/component | Dependency path | Case | Inclusion/exclusion reason | Essential? | Prior evidence applicability | Current run/result | Residual risk.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [docs/templates.md](../templates.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass.

## Quality checks and boundaries

A narrow suite needs an evidence-based rationale. A previous build’s pass is not automatically valid for a changed component. No new complete-suite claim from partial execution.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Application boundary

Apply this procedure to the actual product sources and current scope. Missing rules remain Pending definition; proposed work is not executed evidence.

## Handoff

22 on failures; 26–28 for updated report and gate assessment.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
