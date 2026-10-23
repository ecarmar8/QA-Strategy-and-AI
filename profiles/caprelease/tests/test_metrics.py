"""Calculator tests using synthetic inputs, never company results.

Run: python -m unittest discover -s profiles/caprelease/tests -v
"""
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import unittest

PROFILE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('caprelease_report',PROFILE/'build_report.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def blank():
    return json.loads((PROFILE/'kpi-ledger.json').read_text())


def control(identifier, status='Verified'):
    return dict(id=identifier,source='Synthetic unit-test source',required=True,status=status,
                implementation_ref='Synthetic implementation',verification_ref='Synthetic verification',
                evidence_current=True,evidence_ids=['TEST-EVIDENCE'])


def established(key, rows):
    ledger=blank()
    ledger.update(scope='Synthetic calculator test only',period='Synthetic cohort')
    ledger['baselines'][key]='Established'
    ledger[key]=rows
    return ledger


def metric(ledger, code):
    return next(x for x in module.calculate(ledger) if x['id']==code)


class MeasurementContractTests(unittest.TestCase):
    def test_unknown_and_known_empty_are_distinct(self):
        self.assertTrue(all(x['value']=='Not measured' for x in module.calculate(blank())))
        ledger=established('integration_controls',[])
        self.assertEqual(metric(ledger,'K07')['value'],'No data')
        self.assertIsNone(metric(ledger,'K08')['denominator'])

    def test_failures_and_reviewed_exclusions_do_not_inflate_assurance(self):
        rows=[control('C1'),control('C2','Failed'),control('C3','Not verified')]
        rows.append(dict(id='C4',source='Reviewed exclusion',required=False,exclusion_reason='Outside confirmed scope'))
        value=metric(established('integration_controls',rows),'K07')
        self.assertEqual(value['value'],'33.3%')
        self.assertEqual(value['denominator'],3)

    def test_stale_evidence_and_missing_signal_cannot_be_verified(self):
        stale=control('C1');stale['evidence_current']=False
        with self.assertRaises(ValueError):
            module.calculate(established('data_rules',[stale]))
        decision=control('D1')
        decision.update(required_signal_ids=['SALES','INVENTORY'],linked_signal_ids=['SALES'],
                        signals_current_under_policy=True,policy_ref='Synthetic policy',rule_version='Synthetic version')
        with self.assertRaises(ValueError):
            module.calculate(established('decisions',[decision]))
        decision['linked_signal_ids'].append('INVENTORY')
        self.assertEqual(metric(established('decisions',[decision]),'K08')['value'],'100.0%')

    def test_automated_file_or_passing_manual_control_is_not_enforced_coverage(self):
        automated=control('A1')
        automated.update(required_assertions=2,automated_assertions=2,gate_enforced=True,
                         pipeline_run_ref='Synthetic run',gate_verification_ref='Synthetic enforcement proof')
        manual=deepcopy(automated);manual.update(id='A2',automated_assertions=0,gate_enforced=False)
        self.assertEqual(metric(established('automation_controls',[automated,manual]),'K11')['value'],'50.0%')
        automated['gate_enforced']=False
        self.assertEqual(metric(established('automation_controls',[automated]),'K11')['value'],'0.0%')

    def test_critical_escapes_count_releases_once_and_keep_window_explicit(self):
        releases=[dict(id='R1',source='Synthetic deployment',observation_complete=True),
                  dict(id='R2',source='Synthetic deployment',observation_complete=True),
                  dict(id='R3',source='Synthetic deployment',observation_complete=False)]
        ledger=established('releases',releases)
        ledger.update(production_attribution_complete=True,observation_window='Synthetic complete window')
        ledger['critical_defects']=[dict(id=x,source='Synthetic defect',introduced_release_id='R1',
                                        classification_ref='Synthetic criticality',critical=True,confirmed=True) for x in ['D1','D2']]
        result=metric(ledger,'K12')
        self.assertEqual((result['numerator'],result['denominator'],result['value']),(1,2,'50.0%'))
        ledger['production_attribution_complete']=False
        self.assertEqual(metric(ledger,'K12')['value'],'Not measured')

    def test_feedback_quantiles_include_visible_waiting_population(self):
        items=[dict(id=str(h),source='Synthetic history',readiness_rule_ref='Synthetic readiness',
                    ready_at='2026-01-01T00:00:00Z',feedback_at=f'2026-01-01T0{h}:00:00Z',feedback_ref='Synthetic feedback') for h in [1,3,5]]
        items.append(dict(id='waiting',source='Synthetic history',readiness_rule_ref='Synthetic readiness',ready_at='2026-01-01T00:00:00Z'))
        result=metric(established('feedback_items',items),'K13')
        self.assertEqual(result['value'],'3.00h / 4.60h')
        self.assertIn('1 awaiting feedback',result['note'])
        items[0]['feedback_at']='2025-12-31T00:00:00Z'
        with self.assertRaises(ValueError):
            module.calculate(established('feedback_items',items))

    def test_ai_reviews_and_effort_do_not_imply_saved_money(self):
        artifacts=[dict(id=str(i),source='Synthetic draft',first_review_completed=True,
                        review_ref='Synthetic review',reviewer='Synthetic reviewer',material_correction_policy_ref='Synthetic criteria',
                        accepted_without_material_correction=(i==0)) for i in range(2)]
        artifacts.append(dict(id='pending',source='Synthetic draft',first_review_completed=False))
        result=metric(established('ai_artifacts',artifacts),'K14')
        self.assertEqual(result['value'],'50.0%')
        self.assertIn('1 artifacts not yet reviewed',result['note'])
        pairs=[dict(id='P1',source='Synthetic observed effort',baseline_ref='Synthetic baseline',assisted_ref='Synthetic assisted',
                    comparability_ref='Synthetic matched scope',same_output_standard_verified=True,baseline_minutes=100,assisted_minutes=125)]
        self.assertEqual(metric(established('effort_pairs',pairs),'K15')['value'],'-25.0%')
        pairs[0].pop('comparability_ref')
        self.assertEqual(metric(established('effort_pairs',pairs),'K15')['value'],'Not measured')


if __name__=='__main__':
    unittest.main()
