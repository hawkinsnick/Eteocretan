import copy,importlib.util,json,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('comparison',R/'scripts/compare_reading_versions.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class ComparisonTests(unittest.TestCase):
 def setUp(self):self.readings=json.loads((R/'data/readings.json').read_text())
 def test_replay_retains_representation_limits(self):
  actual=m.compare(self.readings)
  self.assertEqual(actual,json.loads((R/'analysis/reading-version-comparison-v1.json').read_text()))
  self.assertEqual(len(actual['pairs']),4)
  self.assertFalse(actual['normalization_applied'])
  for p in actual['pairs']:
   self.assertIsNone(p['preferred_version']);self.assertFalse(p['physical_line_alignment_established']);self.assertFalse(p['analysis_admission_granted'])
 def test_literal_spaces_and_uncertainty_remain_significant(self):
  a=copy.deepcopy(self.readings[2]);b=copy.deepcopy(a);b['record_id']='TEST-ONLY';b['source_level']='historical_edition'
  self.assertTrue(m.compare([a,b])['pairs'][0]['literal_source_strings_equal'])
  b['lines'][0]['text']+=' '
  self.assertFalse(m.compare([a,b])['pairs'][0]['literal_source_strings_equal'])
  b['lines'][0]['text']=a['lines'][0]['text']+'?'
  self.assertFalse(m.compare([a,b])['pairs'][0]['literal_source_strings_equal'])
 def test_identity_join_is_required(self):
  a=copy.deepcopy(self.readings[2]);b=copy.deepcopy(a);b['record_id']='TEST-ONLY';b['source_level']='historical_edition';b['object_id']='OTHER-OBJECT'
  self.assertEqual(m.compare([a,b])['pairs'],[])
 def test_duplicate_version_rejected(self):
  with self.assertRaises(ValueError):m.compare(self.readings+[self.readings[0]])
