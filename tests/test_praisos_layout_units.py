import importlib.util,json,shutil,tempfile,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1];s=importlib.util.spec_from_file_location("layout",R/"scripts/audit_praisos_layout_units.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class PraisosLayoutUnitTests(unittest.TestCase):
 def test_distinct_units_replay(self):
  x=m.build();self.assertEqual(x,json.loads((R/"analysis/praisos-layout-unit-audit.json").read_text()));self.assertEqual(x["source_line_total_across_three_objects"],31);self.assertEqual(x["reading_version_count"],4);self.assertEqual(x["objects"][0]["rows_per_version"],[3]);self.assertEqual(x["objects"][1]["rows_per_version"],[12,12]);self.assertEqual(x["preferred_readings_selected"],0)
 def test_row_drift_is_rejected(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp)/"repo";shutil.copytree(R,root,ignore=shutil.ignore_patterns(".git","__pycache__"));p=root/"data/readings.json";x=json.loads(p.read_text());next(r for r in x if r["record_id"]=="ECR-PRAISOS-1-CONWAY-135")["lines"][0]["label"]="1";p.write_text(json.dumps(x));
   with self.assertRaises(ValueError):m.build(root)
