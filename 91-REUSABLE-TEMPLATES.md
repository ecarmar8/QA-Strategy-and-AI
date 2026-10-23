# Reusable QA artifact templates

Copy the relevant template. Replace bracketed placeholders with sourced values or Unknown/Pending; never silently make them up. Examples are structures, not completed evidence.

## Artifact header

| Field | Value |
|---|---|
| Artifact ID / version / type | [ID / v1 / type] |
| Mode / classification | [mode / Confirmed, Observed, Proposed or Pending question] |
| Scope / release / build | [references; Unknown if not supplied] |
| Sources / revisions / extracted UTC | [genuine references] |
| Owner / reviewer | [actual role/person or Unassigned] |
| Status / next action | [state / action] |
| Assumptions / limitations | [explicit list] |

## Backlog snapshot

| Story ID | Type/title | Revision | Source | AC reference | State/iteration | Relations | Completeness |
|---|---|---|---|---|---|---|---|
| [ID] | [value] | [rev] | [reference] | [reference or Missing] | [value] | [raw links] | [Complete/Partial/Unknown] |

Population scope/filter: [query/widget/team/area/iteration]. Paging/limit resolution: [evidence]. Exclusions: [items and reason].

## Dependency and refinement ledgers

| Edge ID | Prerequisite → dependent | Raw relation/source | Confidence | Blocking condition | Owner/status |
|---|---|---|---|---|---|
| [E-ID] | [A → B] | [type/revision] | [Confirmed/Candidate] | [specific condition] | [value] |

| Gap ID | Story/AC/source | Question | Impact if unanswered | Proposed wording | Decision owner | Confirmed answer/reference |
|---|---|---|---|---|---|---|
| [Q-ID] | [reference] | [question] | [impact/cases blocked] | [recommendation] | [owner] | [Pending] |

## Applicability and risk

| Dimension | Applicable? | Confirmed rule/source | Missing question | Cases/coverage |
|---|---|---|---|---|
| CRUD | [Yes/No + reason] | [reference] | [question] | [IDs] |
| Required/optional fields | [value] | [reference] | [question] | [IDs] |
| Roles/permissions | [value] | [reference] | [question] | [IDs] |
| Search/filters/grids/sort/pagination/export | [value] | [reference] | [question] | [IDs] |
| Reports/API/integrations | [value] | [reference] | [question] | [IDs] |
| States/approvals/audit | [value] | [reference] | [question] | [IDs] |

| Risk ID | Failure event | Source | Impact | Likelihood/evidence | Priority/reason | Required evidence | Owner | Residual risk |
|---|---|---|---|---|---|---|---|---|
| [R-ID] | [event] | [reference] | [impact] | [Unknown or evidence] | [P1/P2/P3 + why] | [check] | [owner] | [uncertainty] |

## Strategy and plan

| Risk/journey | Surface/level | Technique | Data/environment | Manual/automation decision | Owner/reviewer | Entry/exit evidence |
|---|---|---|---|---|---|---|
| [reference] | [UI/API/data/etc.] | [technique] | [references] | [reason] | [value] | [gates] |

| Work package | Dependencies | Effort range | Waiting constraints | Capacity/owner | Wave | Assumptions/confidence |
|---|---|---|---|---|---|---|
| [work] | [references] | [range and unit] | [constraint] | [value] | [wave] | [evidence/Unknown] |

## Full functional test case

```markdown
# Case TC-[id] — [business objective]
- Case version: [v1]
- Source story/revision and AC/risk: [references]
- Definition status: [Draft / Pending definition / Ready / Retired]
- Priority and reason: [P1/P2/P3 and impact]
- Preconditions: [confirmed state, identity/role, environment]
- Data: [synthetic dataset reference and values]
- Expected-result source: [approved rule/contract]
- Steps:
  1. [action]
  2. [action]
- Observable expected results: [UI/API/state/data/financial effects]
- Postconditions and cleanup: [actions and owner]
- Proposed execution method: [manual/API/web/etc.; reason]
- Pending questions: [IDs or None]
- Initial execution status: Not Run
- Review: [reviewer/status; Pending until performed]
```

## Per-run ledger — actual execution only

| Run/attempt | Case/version | Target/build/config | Tester/tool | Started/ended UTC | Expected source | Actual/evidence | Result | Defect/blocker | Cleanup |
|---|---|---|---|---|---|---|---|---|---|
| [ID/attempt] | [reference] | [reference] | [actual] | [time] | [reference] | [observation/link] | [Not Run/Passed/Failed/Blocked/Not Applicable] | [reference] | [result] |

For a simulation, use a separate table headed **SIMULATED — NOT EXECUTED**, add `is_simulated: true`, and never insert it into an actual-run ledger.

## Data and environment readiness

| Dataset/check | Cases/track | Confirmed setup/expected | Actual readiness/evidence | Isolation/cleanup | Owner | Status/blocker |
|---|---|---|---|---|---|---|
| [ID] | [references] | [rule/setup] | [observed or Unverified] | [plan] | [owner] | [state] |

## Defect and fix verification

```markdown
# Defect [local ID / remote ID if actually created]
- Summary: [business failure]
- Story/AC/case/run/source: [references]
- Build/environment/data: [actual values]
- Expected: [rule and source]
- Actual: [observed result]
- Reproduction steps: [minimal ordered actions]
- Evidence/correlation: [sanitized references]
- Business impact/severity: [reason and local taxonomy]
- Proposed priority: [reason]
- Workaround/frequency: [evidence or Unknown]
- Triage: [decision, rationale, owner; Pending if absent]
- Fix reference/build: [reference or Pending]
- Retest/regression: [new run references, not overwritten originals]
- Closure recommendation: [evidence-based; Pending if blocked]
```

## Traceability and regression selection

| Story/revision | AC/risk | Case/version | Change/impact reason | Essential? | Latest applicable run/build | Evidence | Defect/retest | Gate |
|---|---|---|---|---|---|---|---|---|
| [source] | [references] | [reference] | [reason] | [Yes/No] | [reference or Not Run] | [reference] | [reference] | [state] |

## Metrics and one-page report

| Metric | Numerator | Denominator | Value | Scope/build/window | Source | Limitation |
|---|---|---|---|---|---|---|
| Execution coverage | [Passed + Failed] | [applicable planned cases] | [ratio or No data] | [value] | [run ledger] | [gaps] |
| Pass rate | [Passed] | [Passed + Failed] | [ratio or No data] | [value] | [run ledger] | [blocked/not-run separate] |
| Essential evidence coverage | [essential AC with current passing evidence] | [essential AC] | [ratio or No data] | [value] | [traceability] | [missing list] |

Report order: decision needed → scope/build → counts/chart and exact table → essential failures/gaps → evidence → next actions/owners → QA recommendation and separate human decision. Do not invent a historical trend.

## Release gate and decision

| Gate | Requirement/source | Current evidence/build | Met/Failed/Missing/Not Applicable | Risk | Owner/action |
|---|---|---|---|---|---|
| [gate] | [reference] | [reference] | [state] | [impact] | [actual owner or Unassigned] |

- QA recommendation: [Go / Conditional Go / No-Go / Pending assessment].
- Rationale: [essential gate evidence].
- Nonessential risk acceptance: [owner, impact, mitigation, monitoring, expiry/review trigger, build/release; Pending if absent].
- Authorized human release decision: [Pending / actual decision with source and time].
- Required next evidence: [specific action/owner].

## People, improvement and publication

| Work/risk | Owner/reviewer | Capacity constraint | Coaching or improvement goal | Baseline | Next practice/action | Review point |
|---|---|---|---|---|---|---|
| [reference] | [value] | [value] | [specific outcome] | [observed or Unknown] | [action] | [agreed point] |

| Local artifact/version | Destination/operation | Revision before | Field/link change preview | Authorization reference | Stable source-run key | Actual response/readback | Retry action |
|---|---|---|---|---|---|---|---|
| [reference] | [project/item/type] | [actual] | [diff] | [session instruction] | [key] | [Pending or actual ID/revision] | [needed action] |

## Optional machine-readable handoff inside Markdown

This JSON is a structure example, not an actual run. An LLM can fill it without creating a software system.

```json
{
  "artifact_id": "PLAN-001",
  "version": "1",
  "mode": "CONNECTED_READ",
  "classification": "Proposed",
  "source_refs": ["supplied-story-export"],
  "scope": "selected stories only",
  "build": "Unknown",
  "is_simulated": false,
  "definition_status": "Draft",
  "execution_status": "Not Run",
  "authorization_ref": "user request: read and analyze only",
  "pending_questions": ["Q-001"],
  "next_skill": "04-analyze-acceptance-criteria-and-refine.md"
}
```
