---
name: connect-azure-devops-securely
description: "Access Azure DevOps as the user, verify the authenticated account, or diagnose a failed connection."
---

# 01 · Connect to Azure DevOps securely

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Access Azure DevOps as the user, verify the authenticated account, or diagnose a failed connection.

## Shared contract

Read [docs/operating-contract.md](../operating-contract.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Organization URL, Services versus Server deployment, project/team scope and requested read/write capabilities. Existing authorized connector/session is preferred. Never request a password in chat.

## Procedure

1. Inspect available service tools and their authentication guidance. Reuse an authorized signed-in session when possible; verify account and tenant/project scope with a minimal read.
2. For Azure DevOps Services, prefer Microsoft Entra interactive sign-in or a supported delegated connector. If username/password is required by the identity provider, the user enters it only in its legitimate sign-in surface, completes MFA, and returns control. Do not bypass MFA, capture credentials or replay a password against REST.
3. For Azure DevOps Server, determine supported organization authentication separately; do not assume Entra Services instructions apply. Follow its documented Windows or token integration.
4. For unattended execution, use an approved managed identity or service principal where supported. If a PAT is genuinely needed, limit scope and lifetime, source it from an approved secret store and redact it everywhere. Never write it into these Markdown files, reports, screenshots or repository history.
5. Verify access using the smallest read for the requested project. Record deployment, sanitized account identifier, granted capabilities and timestamp. Do not enumerate unrelated projects.
6. Handle 401 by checking session/expiry, 403 by checking project permission, and network errors separately. Avoid blind retries or expanding permissions. If no connector or permitted sign-in exists, return Blocked with the exact missing capability; accept a sanitized export for analysis.

## Required output

Connection record: Deployment | Organization | Project | Auth method | Account alias | Verified read capability | Authorized write scope | Checked UTC | Limitation. Do not include tokens, cookies or session storage.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [docs/templates.md](../templates.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass.

## Quality checks and boundaries

A working login is not authorization to mutate work items, execute business operations or deploy. Do not claim that a password is a supported REST authentication method for every deployment.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Application boundary

Apply this procedure to the actual product sources and current scope. Missing rules remain Pending definition; proposed work is not executed evidence.

## Handoff

02. Reference 98-SOURCES.md for Microsoft authentication guidance.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
