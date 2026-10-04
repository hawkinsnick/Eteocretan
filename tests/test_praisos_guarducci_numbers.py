import importlib.util,json,shutil,tempfile,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1];s=importlib.util.spec_from_file_location('numbers',R/'scripts/audit_praisos_guarducci_numbers.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class GuarducciNumberTests(unittest.TestCase):
 def test_number_and_uncertainty_classes_replay(self):
  x=m.build();self.assertEqual(x,json.loads((R/'analysis/praisos-guarducci-number-audit.json').read_text()));self.assertEqual(x['reported_number_count'],6);self.assertEqual(x['historically_named_crosswalk_count'],3);self.assertEqual(x['perhaps_eteocretan_fragment_count'],3);self.assertEqual(x['primary_guarducci_pages_collated'],0)
 def test_fragment_promotion_is_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d)/'repo';shutil.copytree(R,root,ignore=shutil.ignore_patterns('.git','__pycache__'));p=root/'research/praisos-guarducci-number-concordance.json';x=json.loads(p.read_text());x['records'][3]['language_status_reported']='Eteocretan';p.write_text(json.dumps(x));
   with self.assertRaises(ValueError):m.build(root)
if __name__=='__main__':unittest.main()
