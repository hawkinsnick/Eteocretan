import importlib.util,json,shutil,tempfile,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1];s=importlib.util.spec_from_file_location('context',R/'scripts/audit_dreros_context.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class DrerosContextTests(unittest.TestCase):
 def test_metadata_replays_with_group_scope_and_no_admission(self):
  x=m.build();self.assertEqual(x,json.loads((R/'analysis/dreros-context-audit.json').read_text()))
  self.assertEqual(x['source_page_renderings_inspected'],2);self.assertEqual(x['source_figures_inspected'],1)
  self.assertEqual(x['named_inscription_assertions'],3);self.assertEqual(x['group_history_assertions'],3)
  self.assertEqual(x['reading_versions_added'],0);self.assertFalse(x['named_object_loss_certified'])
 def test_hostile_metadata_promotions_rejected(self):
  for attack in ['misjoin','group_loss','original_facsimile','semantic_alignment','duplicate','orphan','source_witness','redistribution','language','hypothesis','reading']:
   with self.subTest(attack=attack),tempfile.TemporaryDirectory() as tmp:
    root=Path(tmp)/'repo';shutil.copytree(R,root,ignore=shutil.ignore_patterns('.git','__pycache__'));p=root/m.SOURCE;x=json.loads(p.read_text())
    if attack=='misjoin':x['assertions'][0]['object_id']='ECR-DREROS-2'
    elif attack=='group_loss':x['assertions'][-1]['object_id']='ECR-DREROS-1'
    elif attack=='original_facsimile':x['source']['original_1946_facsimile_inspected']=True
    elif attack=='semantic_alignment':x['limits']['semantic_alignment_established']=True
    elif attack=='duplicate':x['assets'].append(x['assets'][0])
    elif attack=='orphan':x['assertions'][0]['evidence_assets']=['UNREGISTERED']
    elif attack=='source_witness':x['source_edges'][0]['independent_ancient_witness']=True
    elif attack=='redistribution':x['assets'][0]['redistributed']=True
    elif attack=='language':x['assertions'][2]['status']='PROJECT_CERTIFIED'
    elif attack=='hypothesis':x['assertions'][3]['status']='OBJECT_DATE'
    else:x['assertions'][0]['reading_admission']=True
    p.write_text(json.dumps(x))
    with self.assertRaises(ValueError):m.build(root)
