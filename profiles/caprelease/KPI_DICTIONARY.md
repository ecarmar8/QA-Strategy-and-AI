# CapRelease — exact QA KPI dictionary

Use the six primary indicators in [PROCESS_RISK_KPIS.md](../../PROCESS_RISK_KPIS.md). Keep the executive page focused; use the additional indicators below to explain the observed gap, integration/data assurance or delivery constraint. These are locally proposed operational definitions, not external benchmarks. Agree scope, criticality and required protections with the actual owners.

## Common measurement contract

- Freeze/report the product, scope, build/configuration, rule/contract revision, period and baseline revision. Show additions/removals and unknown classification.
- Deduplicate by stable risk/control/decision/release ID. Link evidence to actual applicable runs or verified non-test controls. A failed test is not automatically a unique defect.
- A verified protection needs confirmed expected behavior, implementation evidence and current verification of every required assertion. Accepted/deferred/missing/stale protection never counts as verified.
- A percentage is **100 × numerator / denominator**. A confirmed denominator of zero gives **No data**. Missing population, evidence classification or required chronology gives **Not measured** and names the affected records. Known failures are measured failures; do not hide them as missing data.
- Show counts with every percentage. Do not silently remove blocked, unverified or failed required records. Justified non-applicability needs a reviewed source/decision.
- A target is a decision aid agreed after baseline review; formulas are exact, initial project values are unknown. Never invent a 30%/50% improvement target to sound convincing.

## Primary executive indicators

| ID / label | Exact formula | Evidence / interpretation |
|---|---|---|
| K01 Verified risk mitigation | 100 × identified applicable risks whose complete required control set is implemented and currently verified / all identified applicable risks | Mitigation coverage of the confirmed risk baseline; not incident probability reduction |
| K02 Unresolved critical risks | Count of identified critical risks with any failed/unverified required control, or no defined required control | Also show count/all critical risks, consequence, owner and next action; accepted risk remains residual |
| K03 Critical process assurance | 100 × critical processes with their complete required control set implemented and currently verified / all confirmed in-scope critical processes | One passing happy path does not establish process assurance |
| K04 Shift-left readiness | 100 × critical stories started in the cohort with risk/dependency review and essential decisions completed before development / all critical stories started in that cohort | Source-backed start/review/decision chronology; unknown timing makes cohort Not measured |
| K05 Preventive findings resolved | 100 × confirmed pre-development findings requiring early resolution that were resolved before affected implementation with decision/change evidence / all confirmed pre-development findings requiring early resolution in the cohort | Late/unresolved findings remain in the denominator; proposals alone do not count |
| K06 Non-functional assurance | 100 × agreed applicable NFRs met with current evidence / all agreed applicable NFRs | Defined targets and actual measurement required; absent NFR evaluation is Not assessed, not 100% |

For K01–K06 the shared dictionary remains authoritative. K01/K03 require at least one defined required control per counted risk/process.

## Role-specific diagnostic indicators

| ID / label | Exact formula | Required baseline and safeguards | What decision it helps |
|---|---|---|---|
| K07 Integration failure-mode assurance | 100 × required provider failure-mode protections verified / all required applicable provider failure-mode protections | Deduplicated provider + operation + condition control IDs; verify complete expected response/recovery/persisted effect; retain errors, throttling/retry and partial outcomes in scope where agreed | Which integration protections still lack evidence? |
| K08 Decision-data traceability | 100 × in-scope decisions with every policy-required signal linked/current under that policy, a rule version and traceability evidence / all in-scope decisions selected in the confirmed cohort | Confirm each decision's required signal set and freshness rules; do not assume all four signals block every decision. Scope/sample and incomplete decisions remain explicit | Can the team explain which inputs/rules support the outcome? |
| K09 Critical data-rule assurance | 100 × critical source/derived/persisted-data rules verified / all agreed applicable critical data rules | Independent oracle, actual schema/snapshot, mapping/precision/time rules and row-level plus aggregate evidence as appropriate | Can the technical team trust the information delivered to its consumer? |
| K10 Critical contract assurance | 100 × required critical consumer/provider contract obligations verified / all required applicable critical contract obligations | Contract revision and actual boundary; include agreed breaking-change/error behavior, not only schema success | Are important interface assumptions verified? |
| K11 Enforced automation of critical controls | 100 × critical controls with all required assertions automated, current successful execution and verified pipeline enforcement / all agreed applicable critical controls | Total population includes manual/unautomated critical controls. Show automated assertion counts, pipeline-run reference and gate proof; do not equate test-file count with protection | Which critical protections provide repeatable, enforced feedback? |
| K12 Critical escape incidence | 100 × mature deployed-release cohort members linked to at least one confirmed critical escaped defect / all deployed releases in that cohort with the agreed observation window complete | Define window, critical taxonomy and introduced-release attribution; unknown mapping/classification makes the measure unavailable. Exclude immature releases explicitly and report their count | Are critical escapes changing across comparable mature cohorts? |
| K13 Actionable QA feedback lead time | For each eligible work item, elapsed hours = first actionable QA feedback timestamp − timestamp the agreed test-ready criteria were first met. Report p50/p90 across the cohort | Fix calendar vs working hours, readiness rule, time zone and definition of actionable feedback. Show still-waiting items/age separately; no imputed timestamps | Is the delivery process receiving useful feedback promptly? |
| K14 AI first-review acceptance | 100 × AI-assisted artifacts accepted at first completed accountable review without material correction / all AI-assisted artifacts with a completed first review in the cohort | Record criteria for material correction, input sources, AI draft, review and decision; show unreviewed artifacts separately | Is AI producing useful, reviewable work, rather than adding hidden rework? |
| K15 Observed AI effort change | 100 × (sum comparable baseline active minutes − sum assisted active minutes) / sum comparable baseline active minutes | Use matched comparable tasks and the same accepted output standard; assisted effort includes prompting, review, correction and verification. Missing matching/effort makes Not measured; negative values are valid | Does this particular AI-assisted workflow release measurable working capacity? |

K15 is a time/capacity comparison, not financial savings and not proof of AI causality under uncontrolled conditions. Do not sum K01–K11 or count the same protection repeatedly as independent prevented incidents. K08 measures evidence/lineage coverage, not correctness of lending policy. K12 is a team outcome and observed association, not individual QA attribution.

## Target setting and executive interpretation

For a release, every agreed essential gate must be met. An overall KPI above an arbitrary threshold cannot waive an essential failed/missing control. K02 should enumerate every essential unresolved exposure; zero is meaningful only after the critical-risk baseline is confirmed, not merely because the ledger is empty.

For trends, agree improvement directions and review points after the baseline. Preserve cohort size, workload/change mix, severity and observation windows. More identified risks or early findings can indicate improved discovery. Fewer escaped defects in a short or smaller release period do not establish sustained prevention.

## Collection and ownership

Collect requirement/review/decision chronology from real work-item history, not inferred final text. Collect verification/build/contract evidence from actual runs and reviewed data queries. Collect deployed-release and production-defect records with Engineering/operations. Collect AI draft/review/effort records from actual sessions and human review. Record actual owners or Unassigned; do not fabricate named responsibilities.

The supplemental report calculator in build_report.py derives K07–K15 from kpi-ledger.json; all baselines start Not established. It refuses inconsistent verified claims. The six primary metrics continue to derive from the shared HTML report data. Do not manually type achievement percentages into either report.
