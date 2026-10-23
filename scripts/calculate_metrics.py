"""Compute quality diagnostics from source ledgers and write a reviewable result ledger.

No network, database access, client execution or invented measurement is involved.
Run: python scripts/calculate_metrics.py
"""
from __future__ import annotations
import argparse
from datetime import datetime
import json
from pathlib import Path
from math import isfinite

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
BASELINES = ('integration_controls', 'outcomes', 'data_rules', 'contracts',
             'automation_controls', 'releases', 'feedback_items', 'ai_artifacts', 'effort_pairs')
LABELS = ('Integration failure-mode assurance', 'Source-to-outcome traceability',
          'Critical data-rule assurance', 'Critical contract assurance',
          'Enforced automation of critical controls', 'Critical escape incidence',
          'Actionable QA feedback lead time', 'AI first-review acceptance',
          'Observed AI effort change')
FORMULAS = (
    '100 × verified required protections / required applicable protections',
    '100 × traceable outcomes / outcomes in the confirmed cohort',
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
        elif key == 'outcomes':
            n = 0
            for r in records:
                good = verified(r)
                if good:
                    required = string_list(r, 'required_source_ids')
                    linked = string_list(r, 'linked_source_ids')
                    require(r.get('policy_ref') and r.get('rule_version') and
                            bool_field(r, 'sources_current_under_policy') and set(required) <= set(linked) and
                            (required or r.get('exception_ref')),
                            f'{r["id"]}: traceable outcome needs required source links, applicable policy and rule version.')
                n += int(good)
            metric.update(value=pct(n, len(records)), numerator=n, denominator=len(records),
                          note='Evidence/lineage coverage under the confirmed source policy; not proof of business-policy correctness.')
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


def main():
    parser=argparse.ArgumentParser(description='Calculate source-backed quality diagnostics.')
    parser.add_argument('--ledger',type=Path,default=ROOT/'data/quality-ledger.json')
    parser.add_argument('--output',type=Path,default=ROOT/'reports/quality-diagnostics.json')
    args=parser.parse_args()
    result=calculate(json.loads(args.ledger.read_text()))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(f'Calculated {len(result)} diagnostics from the supplied ledger. No product execution performed.')


if __name__=='__main__':
    main()
