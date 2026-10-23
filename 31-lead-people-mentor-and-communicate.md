---
name: lead-people-mentor-and-communicate
description: "Coordinate QA contributors, coach a junior tester, resolve conflicts or explain quality decisions to stakeholders."
---

# 31 · Lead people, mentor and communicate

Version: 1.0 · Language: English · Role: Senior QA / QA Lead

## When to use

Coordinate QA contributors, coach a junior tester, resolve conflicts or explain quality decisions to stakeholders.

## Shared contract

Read [90-OPERATING-CONTRACT.md](90-OPERATING-CONTRACT.md) before acting. Reuse the current source snapshot, checkpoint and already granted authorization. Do not infer tool availability or write authority from this file. Apply source/evidence review in [32-review-ai-output-and-protect-evidence.md](32-review-ai-output-and-protect-evidence.md).

## Inputs and prerequisites

Team roles/capacity/skills, current risks and commitments, communication audience, decision ownership and actual collaboration authorization.

## Procedure

1. Clarify responsibilities across QA, developer, product owner, domain/compliance, operations and release authority. Assign one accountable owner per decision/action while encouraging shared quality ownership.
2. Distribute work by risk and skills, with reviewer/pairing for financial/access-critical areas. Balance delivery commitments with learning, absences and workload; do not rank individuals by defect counts.
3. For junior mentoring, use an actual case: explain business intent, ask the tester to identify oracle/data/negative paths, review their draft, give specific feedback and have them revise it. Track growing independence, not just volume.
4. Run brief risk/blocker checkpoints and evidence-based triage. Resolve disagreement through shared reproduction and sources; escalate decision ambiguity to the right owner without blame.
5. Adapt updates: CTO gets business risk, confidence and decision; developers get reproducible evidence; product gets unanswered rule decisions; testers get exact scope/data/expected outcomes.
6. Prepare messages and meeting notes as drafts. Send or schedule them only when the user/session explicitly authorizes the recipients and action. Preserve prior communication authorization without asking repeatedly.

## Required output

Team plan: Work/risk | Owner | Reviewer | Capacity constraint | Coaching goal | Checkpoint. Coaching note: observed gap | example feedback | revised artifact | next practice. Stakeholder update draft with decision/action owner.

For each output, include artifact ID/version, source references, current scope/build where applicable, assumptions, unresolved questions, status, owner and next action. Use the relevant template in [91-REUSABLE-TEMPLATES.md](91-REUSABLE-TEMPLATES.md). Keep case definitions separate from execution records.

## Missing input and stopping behavior

State the exact missing input, capability or decision and its effect. Continue independent analysis that remains valid. Keep unknown requirements Pending definition and unexecuted cases Not Run. In connected mode, unavailable execution is Blocked/Not Run; it is never a simulated pass. In OFFLINE_DEMO, label every simulated result.

## Quality checks and boundaries

No invented employee performance, commitments or named recipients. Distinguish QA recommendation from product/release authority. Avoid public sensitive defect details.

Business-rule proposals need owner confirmation; human release authority remains separate from QA assessment. Do not repeat permission requests for actions already authorized in the current scope. Stop only the dependent action when its required evidence or authorization is missing.

## Small example

Input: junior checks only a refund success toast. Output: coach them to assert balance, duplicate protection and audit using confirmed rules; pair on first run and review evidence.

## Handoff

09 for replanning, 22 for disputes, 27 for reports. Apply throughout the cycle.

Save a checkpoint with produced artifact references, decisions, blockers and the next skill. The numbering is a navigation aid, not an instruction to execute every track.
