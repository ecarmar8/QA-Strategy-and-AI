# Project working templates

These are empty working structures. Create only those useful to the actual engagement and reuse equivalent existing artifacts. Keep placeholders until evidence is supplied; no table is a claim that review, testing or approval occurred. Stable IDs below are local identifiers until mapped to the organization's system.

## 1. Engagement brief and project strategy

- Product/project and scope: [Confirm]
- Business objectives, users and critical workflows: [Source]
- Problem prompting QA support and current evidence: [Source / hypothesis]
- Delivery approach and current commitments: [Confirm]
- Stakeholders, domain decision owner, engineering owner, QA contributors, release authority: [Confirm]
- Useful current practices to preserve: [Observed / confirmed]
- Architecture, dependencies and source revisions: [References]
- Quality requirements and risk priorities: [Confirmed / pending]
- Included/excluded validation and consequences: [Reason / decision owner]
- Levels/techniques; manual/exploratory/automation decisions: [Risk rationale]
- Data, environments, access and specialists: [Available / blocked]
- Readiness, acceptance, release and operational criteria: [Owner / source]
- Communication, triage, escalation and evidence retention: [Agreement]
- Initial baseline, pilot and next review: [References]
- Strategy status: Draft / Reviewed / Agreed; reviewer, date and source: [Pending]

## 2. Source, decision and question ledger

| ID | Type | Source/revision | Statement / question | Confirmed / observed / proposed / pending | Impact | Owner | Decision/evidence/date |
|---|---|---|---|---|---|---|---|

## 3. Product process and delivery map

| Process/step ID | Actor | Input | Rule/source | State/output | Dependencies | Failure consequence | Owner | Unknowns |
|---|---|---|---|---|---|---|---|---|

| Work-item ID | Stage | Entered | Started | Finished | Wait/blocked reason | Build/source | Decision owner |
|---|---|---|---|---|---|---|---|

Unknown timestamps stay Unknown. Do not estimate observed waiting from memory as measured data.

## 4. Escaped-defect analysis

| Defect ID | Period/build | Expected/source | Actual/consequence | Introduction cause | Escape cause | Evidence/confidence | Detection opportunity | Control proposal/owner | Follow-up |
|---|---|---|---|---|---|---|---|---|---|

Record sample selection and limitations above the table. Keep hypotheses labeled until reviewed.

## 5. Risk, control and evidence register

| Risk ID | Process | Failure scenario/consequence | Source/priority reason | Required control IDs | Owner | Residual risk | Next action |
|---|---|---|---|---|---|---|---|

| Control ID | Purpose/source | Implementation reference | Required verification/cases | Evidence/build/config | Current? | Verified / Failed / Not verified | Owner |
|---|---|---|---|---|---|---|---|

Risk status derives from all its required controls. No required control defined means Not verified; accepted/deferred risk remains residual. Record the baseline revision and additions/removals.

## 6. Early review and preventive findings

| Story ID | Critical? / source | Development start/source | Risk/dependency review time/source | Essential decisions resolved time/source | Unresolved questions |
|---|---|---|---|---|---|

| Finding ID | Confirmed issue/source | Identified stage/time | Requires early resolution? | Decision/change reference | Affected implementation start | Resolution time/stage | Owner |
|---|---|---|---|---|---|---|---|

Missing chronology is Unknown; do not infer prevention from the final version of a requirement.

## 7. Coverage and verification

| Requirement/risk | Control | Technique/level | Case/charter/version | Expected oracle/source | Data/environment | Priority | Definition state | Owner |
|---|---|---|---|---|---|---|---|---|

| Run/case/attempt | Build/config/source revision | Actual observation | Status | Evidence reference | Defect | Time | Cleanup / limitation |
|---|---|---|---|---|---|---|---|

Definition states: Draft, Pending definition, Ready, Retired. Execution: Not Run, Passed, Failed, Blocked, Not Applicable with a reason. Preserve attempts.

## 8. Non-functional requirement and readiness

| NFR ID | Attribute | Target/source/owner | Workload/client/scope | Method/environment | Actual measurement/evidence | Met / Failed / Missing / Not Applicable | Limitation |
|---|---|---|---|---|---|---|---|

| Track | Build/config | Data/accounts | Dependencies/tools | Oracle | Evidence/cleanup | Ready / Partially ready / Blocked | Owner/action |
|---|---|---|---|---|---|---|---|

## 9. Automation decision

| Candidate/risk | Repetition and value | Oracle stability | Proposed level/tool rationale | Data/dependency constraints | Automate / Manual / Defer | Owner/maintenance | Review trigger |
|---|---|---|---|---|---|---|---|

## 10. Pilot and improvement charter

- Observed gap and supporting evidence: [Reference]
- Confirmed finding versus hypothesis: [Classification]
- Bounded process/change and baseline period: [Scope]
- Proposed intervention and alternatives: [Rationale]
- Owner, contributors and capacity: [Confirm]
- Required implementation and verification: [Control/evidence]
- Success criteria and observation window: [Agree]
- Confounders, risks and rollback/stop condition for the intervention: [Describe]
- Review result and retain/modify/stop decision: [Pending]

## 11. Mentoring record

| Capability | Work sample | Tester reasoning | Feedback / paired activity | Independent follow-up | Observable progress | Next review |
|---|---|---|---|---|---|---|

## 12. Release and executive review

- Scope/build/config/period and evidence freshness: [References]
- QA recommendation and rationale: [Pending assessment until supported]
- Required gates: [ID / source / owner / Met, Failed, Missing or justified Not Applicable]
- Critical unresolved risks and consequences: [References]
- Business acceptance and operational prerequisites: [Actual status / owner]
- Accepted/deferred risks, conditions and expiry: [Actual decision or Pending]
- Authorized release owner's decision: [Pending / supplied decision reference]
- Post-release checks, observation window and incident contact: [Confirmed scope]
- Six executive KPIs with numerator/denominator, unknowns and source: [PROCESS_RISK_KPIS.md]
- Next actions: [Action / owner / date or Unknown / verification]
