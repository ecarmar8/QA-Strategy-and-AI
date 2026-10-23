# Vacancy-to-delivery traceability

Source: CR-JD-01, the complete vacancy supplied in the conversation. CR-CONTEXT-01 is the candidate's additional report of a junior tester and production escapes. This matrix accounts for business context, duties, essential/desirable experience and soft skills. Coverage here means the strategy addresses the requirement; it does not mean the capability has been independently proven or a CapRelease control verified.

| ID | Vacancy requirement / context | Strategy response | Procedures | Proof / evidence needed |
|---|---|---|---|---|
| B01 | Four source signals: sales, accounting, banking, inventory/fulfilment | Map each source through transformation, storage and actual consumers; confirm freshness/completeness policy | 03,05,06,17,18 | Signal/dependency map and source-to-target evidence |
| B02 | UK eCommerce; advertised £20k–£1m blended inventory/revenue facility and fixed fee | Confirm rules, eligibility, calculations, boundaries and exceptions with Product/underwriting; no invented formula | 04,06,10,18 | Confirmed rule oracle and calculation/state coverage |
| B03 | Decisions in 24–72 hours | Clarify timing definition, workflow waits and technical versus manual stages; do not infer endpoint SLA | 00,05,09,21 | Process timing definition and applicable technical targets |
| B04 | Azure platform and small senior team | Inspect actual architecture, delivery, access and capacity before tools or process changes | 00,03,08,09 | Context/architecture and capacity plan |
| O01 | Own platform QA strategy and define quality | Agree quality expectations, coverage levels, evidence, responsibilities and improvement priorities | 00,07,08 | Reviewed project strategy and control baseline |
| O02 | Decide automated versus manual coverage | Choose by risk, recurrence, oracle and maintenance; retain exploration | 15,16 | Candidate decisions and maintained checks |
| O03 | Own release readiness and challenge senior stakeholders | Assess required evidence, explain consequence and give a supported recommendation proactively | 27,28,31 | Gate matrix, No-Go/Pending/Go rationale and decision record |
| O04 | Hands-on front-end functional/regression testing | Review actual web journeys and execute positive/negative/state/permission/regression coverage | 10,14,19,20,24 | Source-backed cases, actual runs and evidence |
| O05 | REST API testing | Validate contract, authentication/authorization, inputs/errors, states and business effects | 17,23,24 | Sanitized request/response and persisted assertions |
| O06 | Integration and contract testing | Verify producer/consumer expectations, versions and asynchronous effects | 03,17,18 | Contract and end-to-end integration evidence |
| O07 | Write SQL to build data and verify end to end | Use actual SQL Server schema, bounded T-SQL, controlled fixtures and UI/API/data correlation | 12,18 | Reviewed queries, setup/cleanup and reconciliation |
| O08 | Strong joins, indexes and stored-procedure knowledge | Investigate join cardinality/fan-out, procedure side effects, plans/index use and isolation without unauthorized DDL | 18 | Query explanations, procedure checks and diagnostic evidence |
| O09 | Challenge requirements and acceptance criteria early | Resolve ambiguity with actual owners before affected implementation | 04,06,11 | Confirmed questions/decisions and timing |
| O10 | Partner with Product and developers as a peer | Review coverage, pair on reproduction and keep evidence-based feedback short | 09,22,23,31 | Review/pairing records and actionable feedback |
| O11 | Build and maintain automated suites | Implement requested approved scope, review assertions/data/cleanup and own maintenance | 15,16,20,24 | Reviewed source, reproducible actual executions and ownership |
| O12 | Azure DevOps pipelines and gates | Inspect runner/results, fail/missing/skip/retry behavior and actual branch/stage enforcement | 25,28 | Pipeline proposal/change, safe gate proof and run artifacts |
| O13 | Third-party failure modes | Exercise permitted timeouts, errors, partial data, auth expiry and recovery | 17,21 | Provider-specific fault and recovery matrix |
| O14 | Retries and rate limits | Confirm bounded retry/backoff and provider limit semantics; verify no duplicate effects | 06,17,18 | Contract-linked retry/throttle and persisted-effect evidence |
| O15 | Edge cases in live data / data-heavy ETL | Use approved sanitized representative shapes; assess pagination, duplicates, schema drift, missing/null/late records and transformations | 12,17,18 | Data-shape coverage and discrepancy analysis |
| O16 | Actionable reporting: trends, coverage, risk, readiness | Report six process-risk KPIs with denominators, source/build, limitations and next decisions | 26,27,28 | Executive report and traceability ledger |
| O17 | Performance | Agree realistic workload and technical targets; select existing tooling or k6/JMeter as justified | 21 | Measured performance evidence or Pending definition |
| O18 | Resilience | Verify scoped dependency recovery, replay/partial failures and consistency | 17,18,21 | Authorized recovery experiment and evidence |
| O19 | Accessibility / WCAG | Agree version/level and combine automated checks with manual evaluation | 19,21 | Criteria-level accessibility findings and limits |
| O20 | Security basics / FCA context | Confirm applicable obligations and owners; assess relevant access/data/log/secret controls | 06,17,21,28 | Scoped security evidence and compliance-owner decisions |
| O21 | Lead/manage the QA function as it grows | Set standards, direct capacity/priorities, assign reviewers/backups and adapt the function | 09,30,31 | Operating standards, responsibility/capacity and improvement plan |
| O22 | Mentor and spread testing responsibility | Coach reasoning through real work; pair and hand over independent checks | 11,31 | Reviewed work samples and independence progression |
| E01 | Demonstrated ownership and leadership history | Map actual career examples to strategy decisions and team leadership; corroborate before claiming measured outcomes | 31,32 | Candidate-reported experience; supporting examples pending review |
| E02 | Playwright/Cypress/Selenium and Postman or equivalent | Explain actual experience accurately; demonstrate with real supplied scope and available runtime | 16,17,20,32 | Actual portfolio/tool evidence; no assumed advanced mastery |
| E03 | Risk judgment and non-technical trade-offs | Tie priority to failure consequence; show explicit exclusions and residual risks | 07,08,27,28 | Risk rationale and decision-ready explanation |
| E04 | Agile collaboration | Work inside the actual planning/flow cadence; inspect waits and feedback without assuming ceremonies | 00,09,30,31 | Observed delivery map and contextual agreements |
| E05 | Excellent written/spoken English | Use English strategies, criteria, reports and concise verbal walkthroughs | 04,22,27,31 | Written portfolio; spoken ability demonstrated in interview |
| E06 | Remote and time-zone collaboration | Agree overlap/escalation, document decisions and preserve actionable handoffs | 09,31 | Operating agreement; candidate history corroborated separately |
| E07 | Small team pace, independence and limited hand-holding | Prioritize a bounded pilot, continue valid work through blockers and raise decisions without prompting | 00,07,09,31 | Day-one output, checkpoint and next actions |
| E08 | Reliable home setup and daily video calls | Candidate confirms equipment/connectivity and contingency; no invented readiness claim | Candidate logistics | Candidate confirmation required |
| E09 | Remote from Medellín | Confirm actual location/arrangement with employer; do not assume eligibility from generic remote work | Candidate logistics | Candidate/employer confirmation required |
| D01 | Financial services / regulated environment experience | Use actual banking/payments/data-migration examples; confirm applicable obligations for this company | 06,18,32 | User-reported career examples; no compliance-certification claim |
| D02 | Azure DevOps Test Plans / CI/CD | Map existing items/results and gates using actual permissions; keep integrations optional elsewhere | 01,02,25,33 | Plan/run/build links and authorized published artifacts |
| D03 | Working familiarity with C#/.NET or Python | Inspect real service boundaries/code with developers and propose checks at the appropriate level | 16,17,18,32 | Reviewed code/assertions and debugging explanation |
| D04 | Contract/performance tools | Select actual contracts and bounded workload; use compatible tools without claiming undocumented expertise | 17,21 | Contract and performance artifacts |
| D05 | ISTQB or equivalent | Explain equivalent practice; claim a certificate only if supplied and verified | Candidate credentials | Certificate/status not assumed |
| D06 | Practical AI beyond surface use | Run source-grounded analysis, review coverage, propose queries/tests, validate evidence and generate reports through reusable skills | 00,04,07,10,11,18,26,27,32 | Auditable input→AI draft→review→actual output chain |
| S01 | Problem solving | Reconstruct failures, separate causes/hypotheses and test explanations | 18,22,23,30 | Evidence-backed causal analysis |
| S02 | Ownership and accountability | Name actions/owners and give a supported recommendation; preserve unknowns | 00,28,31 | Decision and action ledger |
| S03 | Communication and collaboration | Raise written and meeting concerns proactively; pair and clarify without blame | 04,22,27,31 | Actionable updates and shared decisions |
| S04 | Continuous learning | Review pilot results, recurrence, mentoring and tool limitations, then adapt | 30,31,32 | Reviewed improvement backlog and follow-up |

## Review states

Strategy mapping: Addressed. Project implementation: Not assessed. Actual CapRelease execution: Not Run. Candidate credentials/logistics and historical achievements require their own evidence. The proposed application is in QA_ENGAGEMENT_STRATEGY.md; the reusable method remains at ../../QA_STRATEGY.md.
