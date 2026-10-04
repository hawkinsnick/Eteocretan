import importlib.util,json,shutil,tempfile,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('identity',R/'scripts/audit_praisos_identity.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class PraisosIdentityTests(unittest.TestCase):
 def test_crosswalk_replays_without_scholarly_promotion(self):
  x=m.audit();self.assertEqual(x,json.loads((R/'analysis/praisos-identity-audit.json').read_text(encoding='utf-8')));self.assertEqual(x['objects_reconciled'],['ECR-PRAISOS-1','ECR-PRAISOS-2','ECR-PRAISOS-3']);self.assertEqual(x['archive_join'],'ECR-PRAISOS-2');self.assertEqual(x['preferred_readings_selected'],0);self.assertEqual(x['museum_accessions_established'],0)
 def test_wrong_archive_or_reading_join_rejected(self):
  for target in ['archive','reading']:
   with tempfile.TemporaryDirectory() as tmp:
    root=Path(tmp)/'repo';shutil.copytree(R,root,ignore=shutil.ignore_patterns('.git','__pycache__'));path=root/('research/institutional-archive-leads.json' if target=='archive' else 'research/praisos-historical-identity-crosswalk.json');x=json.loads(path.read_text(encoding='utf-8'))
    if target=='archive':x['entries'][0]['project_object_join']['object_id']='ECR-PRAISOS-1'
    else:x['entries'][0]['project_reading_record']='ECR-PRAISOS-2-CONWAY-127'
    path.write_text(json.dumps(x),encoding='utf-8')
    with self.assertRaises(ValueError):m.audit(root)
