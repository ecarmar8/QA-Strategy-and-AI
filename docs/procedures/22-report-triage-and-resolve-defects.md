---
name: report-triage-and-resolve-defects
description: "Document a reproducible failure, prioritize it and handle a developer who disputes the finding."
---

# 22 · Report, triage and resolve defect disagreements

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Document a reproducible failure, prioritize it and handle a developer who disputes the finding.

## Shared contract

Read [docs/operating-contract.md](../operating-contract.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Expected behavior source, case/run/build, actual observation, sanitized evidence, impact and current defect lifecycle.

## Procedure

1. Validate reproducibility and rule out known environment/data/test issues without hiding uncertainty. State expected behavior with its source, actual behavior and minimal reproduction steps.
2. Create a clear defect proposal with summary, scope/build, data, evidence/correlation IDs, financial/user impact, frequency and workaround. Separate severity (impact) from priority (scheduling); propose both with reasons and local taxonomy.
3. Link story/AC/case/run/evidence. Check existing defects to prevent duplicates while preserving all affected scenarios.
4. When a developer disagrees, compare evidence and reproduce together. Distinguish a requirement ambiguity, implementation failure, environment problem and enhancement request. Ask the product/domain owner to resolve ambiguous intent; do not argue from job title.
5. Record the decision, rationale, owner and affected test expectations. Escalate unresolved essential money/access risk through the agreed triage path with facts and proposed options.
6. Create/update the remote defect only via 33 if authorized; otherwise return a reviewable Markdown draft. Track New/Triaged/Assigned/Fixed/Retest/Reopened/Closed through the actual configured workflow, not assumed state names.

## Required output

Defect draft: ID/reference | Title | Expected/source | Actual | Reproduction | Build/environment | Data | Evidence | Impact/severity | Priority/reason | Workaround | Links | Owner | Triage decision/history.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [docs/templates.md](../templates.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass.

## Quality checks and boundaries

Do not call every unexpected observation a confirmed bug. Do not close a disputed issue merely because the developer rejects it. No secret-bearing screenshots or blame language.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Application boundary

Apply this procedure to the actual product sources and current scope. Missing rules remain Pending definition; proposed work is not executed evidence.

## Handoff

23 after fix; 04 for ambiguity; 33 for authorized writeback.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
