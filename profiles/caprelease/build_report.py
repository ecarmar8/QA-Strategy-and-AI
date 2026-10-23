"""Compute role diagnostics from source ledgers and build a standalone report.

No network, database access, client execution or invented measurement is involved.
Run: python profiles/caprelease/build_report.py
"""
from __future__ import annotations
import argparse
from datetime import datetime
from html import escape
import json
from pathlib import Path
import re
from math import isfinite

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASELINES = ('integration_controls', 'decisions', 'data_rules', 'contracts',
             'automation_controls', 'releases', 'feedback_items', 'ai_artifacts', 'effort_pairs')
LABELS = ('Integration failure-mode assurance', 'Decision-data traceability',
          'Critical data-rule assurance', 'Critical contract assurance',
          'Enforced automation of critical controls', 'Critical escape incidence',
          'Actionable QA feedback lead time', 'AI first-review acceptance',
          'Observed AI effort change')
FORMULAS = (
    '100 × verified required protections / required applicable protections',
    '100 × traceable decisions / decisions in the confirmed cohort',
    '100 × verified critical data rules / applicable critical data rules',
    '100 × verified critical contract obligations / required critical contract obligations',
    '100 × critical controls with fully automated assertions and enforced current passing runs / critical controls',
    '100 × mature releases with a confirmed critical escape / mature deployed releases',
    'p50 / p90 elapsed hours from agreed test readiness to first actionable QA feedback; waiting shown separately',
    '100 × first reviews accepted without material correction / completed first reviews',
    '100 × (comparable baseline minutes − assisted minutes including review/rework) / comparable baseline minutes',
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def pct(n, d):
    return f'{100*n/d:.1f}%' if d else 'No data'


def population(records):
    require(isinstance(records, list), 'A ledger must be an array.')
    ids = set()
    for r in records:
        require(isinstance(r, dict) and isinstance(r.get('id'), str) and r['id'] and r['id'] not in ids,
                'Every record needs a unique nonempty ID.')
        ids.add(r['id'])
        require(isinstance(r.get('source'), str) and r['source'].strip(), f'{r["id"]}: source required.')
    return records


def bool_field(r, key):
    require(type(r.get(key)) is bool, f'{r["id"]}: boolean {key} required.')
    return r[key]


def string_list(r, key):
    value = r.get(key)
    require(isinstance(value, list) and all(isinstance(x, str) and x.strip() for x in value)
            and len(value) == len(set(value)), f'{r["id"]}: unique string array {key} required.')
    return value


def eligible(records):
    result = []
    for r in population(records):
        if bool_field(r, 'required'):
            result.append(r)
        else:
            require(r.get('exclusion_reason'), f'{r["id"]}: exclusion reason required.')
    return result


def verified(r):
    require(r.get('status') in ('Verified', 'Failed', 'Not verified'), f'{r["id"]}: invalid verification state.')
    if r['status'] == 'Verified':
        require(r.get('implementation_ref') and r.get('verification_ref') and
                r.get('evidence_current') is True and string_list(r, 'evidence_ids'),
                f'{r["id"]}: Verified requires implementation and current source-linked verification evidence.')
        return True
    return False


def timestamp(value):
    dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
    require(dt.utcoffset() is not None, 'Timestamps need an explicit timezone.')
    return dt


def quantile(values, q):
    """Linear interpolation at index (n-1)*q, explicitly documented below."""
    values = sorted(values)
    point = (len(values)-1)*q
    i = int(point)
    return values[i] + (values[min(i+1, len(values)-1)]-values[i])*(point-i)


def calculate(ledger):
    require(ledger.get('schema_version') == '1.0', 'Expected supplemental schema_version 1.0.')
    output = []
    for number, key in enumerate(BASELINES, 7):
        state = ledger.get('baselines', {}).get(key)
        require(state in ('Established', 'Not established'), f'Invalid baseline status for {key}.')
        records = ledger.get(key, [])
        population(records)
        metric = dict(id=f'K{number:02}', label=LABELS[number-7], formula=FORMULAS[number-7],
                      value='Not measured', numerator=None, denominator=None,
                      note='Confirmed scope/cohort and source evidence not supplied.')
        if state != 'Established':
            require(not records, f'{key}: confirm the baseline before reporting records.')
            output.append(metric)
            continue
        require(ledger.get('scope') not in (None, '', 'Not supplied', 'Unknown') and ledger.get('period') not in (None, '', 'Unknown'),
                'Established baselines need an actual scope and period/cohort definition.')
        if key in ('integration_controls', 'data_rules', 'contracts', 'automation_controls'):
            cohort = eligible(records)
            n = 0
            for r in cohort:
                good = verified(r)
                if key == 'automation_controls':
                    required = r.get('required_assertions')
                    automated = r.get('automated_assertions')
                    require(type(required) is int and required > 0 and type(automated) is int and 0 <= automated <= required,
                            f'{r["id"]}: invalid assertion counts.')
                    enforced = bool_field(r, 'gate_enforced')
                    good = good and automated == required and enforced and bool(r.get('pipeline_run_ref')) and bool(r.get('gate_verification_ref'))
                n += int(good)
            metric.update(value=pct(n, len(cohort)), numerator=n, denominator=len(cohort),
                          note=f'{len(records)-len(cohort)} reviewed exclusions; failed/unverified required records remain in denominator.')
        elif key == 'decisions':
            n = 0
            for r in records:
                good = verified(r)
                if good:
                    required = string_list(r, 'required_signal_ids')
                    linked = string_list(r, 'linked_signal_ids')
                    require(r.get('policy_ref') and r.get('rule_version') and
                            bool_field(r, 'signals_current_under_policy') and set(required) <= set(linked) and
                            (required or r.get('exception_ref')),
                            f'{r["id"]}: traceable decision needs required signal links, applicable policy and rule version.')
                n += int(good)
            metric.update(value=pct(n, len(records)), numerator=n, denominator=len(records),
                          note='Evidence/lineage coverage under the confirmed signal policy; not underwriting policy correctness.')
        elif key == 'releases':
            if ledger.get('production_attribution_complete') is not True or not ledger.get('observation_window'):
                metric['note'] = 'Complete production-defect attribution and an agreed observation window are required.'
            elif any(type(r.get('observation_complete')) is not bool for r in records):
                metric['note'] = 'Release maturity classification is incomplete.'
            else:
                defects = population(ledger.get('critical_defects', []))
                release_ids = {r['id'] for r in records}
                for defect in defects:
                    require(defect.get('introduced_release_id') in release_ids and defect.get('classification_ref') and
                            defect.get('critical') is True and defect.get('confirmed') is True,
                            'Critical escape needs confirmed severity and introduced-release attribution.')
                mature = {r['id'] for r in records if r['observation_complete']}
                affected = mature & {r['introduced_release_id'] for r in defects}
                metric.update(value=pct(len(affected), len(mature)), numerator=len(affected), denominator=len(mature),
                              note=f'{len(records)-len(mature)} immature releases excluded and still observed. Window: {ledger["observation_window"]}.')
        elif key == 'feedback_items':
            if any(not r.get('ready_at') or not r.get('readiness_rule_ref') for r in records):
                metric['note'] = 'Test-readiness timestamp/rule missing; no imputation performed.'
            else:
                values=[]
                for r in records:
                    start=timestamp(r['ready_at'])
                    if r.get('feedback_at'):
                        require(r.get('feedback_ref'), 'Completed feedback needs its actual reference.')
                        hours=(timestamp(r['feedback_at'])-start).total_seconds()/3600
                        require(hours >= 0, 'Feedback cannot precede test readiness.')
                        values.append(hours)
                waiting=len(records)-len(values)
                metric.update(value=(f'{quantile(values,.5):.2f}h / {quantile(values,.9):.2f}h' if values else 'No data'),
                              denominator=len(values), note=f'p50/p90 calendar elapsed hours; {len(values)} completed, {waiting} awaiting feedback. Quantiles interpolate at (n−1)×q. Waiting work is censored, not completed.')
        elif key == 'ai_artifacts':
            reviewed=[]
            for r in records:
                if bool_field(r, 'first_review_completed'):
                    require(r.get('review_ref') and r.get('reviewer') and r.get('material_correction_policy_ref'), 'Completed AI review needs accountable review and acceptance criteria.')
                    bool_field(r, 'accepted_without_material_correction')
                    reviewed.append(r)
            n=sum(r['accepted_without_material_correction'] for r in reviewed)
            metric.update(value=pct(n, len(reviewed)), numerator=n, denominator=len(reviewed),
                          note=f'{len(records)-len(reviewed)} artifacts not yet reviewed; no productivity claim follows from acceptance alone.')
        else:
            missing=any(not r.get('baseline_ref') or not r.get('assisted_ref') or not r.get('comparability_ref') or
                        r.get('same_output_standard_verified') is not True or
                        type(r.get('baseline_minutes')) not in (int,float) or type(r.get('assisted_minutes')) not in (int,float) for r in records)
            if missing:
                metric['note']='Comparable accepted work and complete active-effort records including review/rework are required.'
            else:
                for r in records:
                    require(isfinite(r['baseline_minutes']) and isfinite(r['assisted_minutes']) and r['baseline_minutes']>=0 and r['assisted_minutes']>=0, 'Effort minutes must be finite and nonnegative.')
                baseline=sum(r['baseline_minutes'] for r in records)
                assisted=sum(r['assisted_minutes'] for r in records)
                metric.update(value=pct(baseline-assisted, baseline), numerator=baseline-assisted, denominator=baseline,
                              note=f'{len(records)} matched tasks; {assisted:g} assisted minutes including review/rework. Observed effort association, not savings or causal proof.')
        output.append(metric)
    return output


def render(ledger, primary, template):
    metrics=calculate(ledger)
    blocks=''.join(f'<tr><td><b>{escape(m["id"])} · {escape(m["label"])}</b></td><td>{escape(m["value"])}</td><td>{escape(m["formula"])}</td><td>{escape(m["note"])}</td></tr>' for m in metrics)
    role_data=json.loads((HERE/'role-requirements.json').read_text())
    role_rows=''.join('<tr>'+''.join(f'<td>{escape(r[k])}</td>' for k in ('id','requirement','response','proof'))+'</tr>' for r in role_data)
    strategy='''<section class="panel" id="roleStrategy"><div class="panel-head"><h2>Ownership from discovery to production</h2><small>Proposed approach · actual company assessment pending</small></div>
<p>Understand the product, team and actual delivery process; diagnose how defects escape; agree one focused improvement; verify the controls and coach the tester through real work.</p>
<div class="grid"><div><h3>From day one</h3><p>Align with the team, trace one workflow, review one current change and available escape evidence. Produce a source-linked context/risk/coverage draft and an actionable English update. Escalate urgent observed risks promptly.</p></div><div><h3>Hands-on depth</h3><p>Connect the customer web journey and .NET/Python API boundaries to SQL Server/Azure SQL evidence. Examine sales, accounting, banking and inventory/fulfilment inputs, transformation and the actual downstream behavior.</p></div></div>
<p><b>AI contribution:</b> accelerate structured analysis, query/test proposals, coverage review and reporting. Senior QA and domain owners review decisions; actual tools provide execution evidence.</p>
<p><b>Portfolio evidence:</b> reusable QA method, 35 skill entry points and evidence-based reporting. No CapRelease test result, incident reduction or candidate credential is invented.</p></section>'''
    supplemental=f'''<section class="panel table-panel" id="roleMetrics"><div class="panel-head"><h2>Role diagnostics — formulas and evidence</h2><small>Supporting measures · select according to the observed gap</small></div><div class="table-wrap"><table><thead><tr><th>Indicator</th><th>Current value</th><th>Exact definition</th><th>Evidence / limitation</th></tr></thead><tbody>{blocks}</tbody></table></div><p class="chart-note">Scope: {escape(ledger['scope'])} · Period: {escape(ledger['period'])} · Source: {escape(ledger['source'])}. Missing baselines are not zeros. These measures do not estimate financial benefits.</p></section>
<details class="panel table-panel" id="roleCoverage"><summary>Vacancy traceability — {len(role_data)} mapped requirements and context items</summary><p>Strategy mapping does not establish implemented controls, candidate credentials or completed company testing.</p><div class="table-wrap"><table><thead><tr><th>ID</th><th>Requirement</th><th>Response</th><th>Proof needed</th></tr></thead><tbody>{role_rows}</tbody></table></div></details>'''
    html=template.replace('<section class="metrics executive"',strategy+'<section class="metrics executive"',1)
    html=html.replace('</head>', '<style>#roleStrategy{margin-bottom:22px}#roleCoverage>summary{white-space:normal;line-height:1.6}#roleMetrics td:nth-child(2){min-width:110px}#roleStrategy .grid>div{min-width:0}#roleStrategy p{line-height:1.65}</style></head>',1)
    html=html.replace('<div class="lower" id="risk">',supplemental+'<div class="lower" id="risk">',1)
    html=re.sub(r'(<script id="qa-report-data" type="application/json">).*?(</script>)',lambda m:m[1]+json.dumps(primary,indent=2).replace('<','\\u003c')+m[2],html,flags=re.S)
    html=html.replace('01 &nbsp; Executive view','01 &nbsp; Executive view').replace('<a href="#processRisk">','<a href="#roleStrategy">02 &nbsp; Strategy & day one</a><a href="#roleMetrics">03 &nbsp; Role diagnostics</a><a href="#processRisk">',1)
    # Supplemental values are generated, not recomputed by the primary-data import button.
    html=html.replace('<button class="btn" id="importBtn">Load run data</button>', '<button class="btn" id="importBtn" hidden>Load run data</button>')
    html=html.replace('02 &nbsp; Process-risk evidence','04 &nbsp; Process-risk evidence').replace('03 &nbsp; Risks & dependencies','05 &nbsp; Risks & dependencies').replace('04 &nbsp; Next decision','06 &nbsp; Next decision')
    return html, metrics


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ledger',type=Path,default=HERE/'kpi-ledger.json')
    parser.add_argument('--primary',type=Path,default=HERE/'primary-report-data.json')
    parser.add_argument('--output',type=Path,default=HERE/'CTO_REPORT.html')
    args=parser.parse_args()
    ledger=json.loads(args.ledger.read_text());primary=json.loads(args.primary.read_text())
    template=(ROOT/'reports/qa-report-template.html').read_text()
    html, metrics=render(ledger,primary,template)
    args.output.write_text(html)
    args.output.with_suffix('.metrics.json').write_text(json.dumps(metrics,indent=2)+'\n')
    print(f'Generated {args.output}; role values derive from {args.ledger}. No product tests executed.')


if __name__ == '__main__':
    main()
