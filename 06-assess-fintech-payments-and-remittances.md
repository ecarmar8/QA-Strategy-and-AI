---
name: assess-fintech-payments-and-remittances
description: "Assess financial integrity and business risk in payment, refund, settlement, FX or remittance workflows."
---

# 06 · Assess fintech, payments and remittance behavior

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Assess financial integrity and business risk in payment, refund, settlement, FX or remittance workflows.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Approved monetary rules and currency precision; product/provider contracts; lifecycle/ledger model; jurisdiction and compliance requirements supplied by authorized owners. Synthetic data only unless explicitly permitted.

## Procedure

1. Identify the transaction lifecycle relevant to this product: initiation, authorization/capture, payout, cancellation/refund/reversal, settlement and reconciliation as applicable. Do not assume all stages exist.
2. Extract invariants from confirmed rules: amount/currency, fees, FX quote/rate/expiry, rounding point, available/refundable balance, ledger movement, duplicate protection, operation identity and auditable actor/time. Missing definitions become refinement questions.
3. Analyze idempotency scope and retention, provider timeouts, uncertain outcomes, duplicate callbacks, reordered events, concurrent requests and recovery. Confirm which operation is safe to retry and how an unknown outcome is reconciled before retrying.
4. For remittances, assess sender/beneficiary, payout method, destination availability, compliance decision handoffs and provider/corridor differences only within the defined scope. Ask compliance owners for applicable KYC/AML/sanctions/privacy rules; do not supply legal thresholds from memory.
5. Check permissions and sensitive-data exposure across UI, API, logs and reports. Plan safe sandbox identities and provider test modes. Never send real funds or real customer data from a generic test instruction.
6. Prioritize loss, double charge/payout, balance drift, unauthorized action and reconciliation mismatch. Specify independent financial oracles, not just a green UI message.

## Required output

Financial assurance matrix: Invariant ID | Confirmed rule/source | Money/data failure | Scenario | Oracle | Provider dependency | Priority reason | Unresolved decision. Link every invariant to cases and release gates.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

Use decimal or integer minor-unit arithmetic appropriate to the confirmed currency; do not assume two decimals universally. No fabricated regulations, fee formulas or provider guarantees.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Small example

Input: fixture confirms USD 100.00 captured and total refunds ≤ captured amount. Output: partial/refund replay/concurrency/reconciliation coverage; an FX scenario remains out of scope until its contract exists.

## Handoff

07–08 and 10; unresolved rules return to 04.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
