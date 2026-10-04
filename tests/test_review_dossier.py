import importlib.util,json,shutil,tempfile,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('dossier',R/'scripts/build_review_dossier.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class DossierTests(unittest.TestCase):
 def test_all_objects_and_versions_replay_without_admission(self):
  x=m.build();self.assertEqual(x,json.loads((R/'analysis/source-critical-dossier.json').read_text()))
  self.assertEqual(x['reading_versions'],12);self.assertEqual(x['coverage_entries'],11)
  self.assertEqual(x['azoria_item_candidates'],2)
  self.assertTrue(all(not d['analysis_eligible'] and not d['independent_review'] for d in x['dossiers']))
 def test_numbering_and_language_conflicts_retained(self):
  x=m.build();items={d['object_id']:d for d in x['dossiers']}
  self.assertEqual(items['ECR-DREROS-2']['primary_metadata_candidates'][0]['edition_item'],'no. 5')
  self.assertTrue(items['ECR-DREROS-1']['near_primary_witness'])
  for key in ['ECR-PRAISOS-4','ECR-PRAISOS-5']:
   self.assertIn('ATTRIBUTION_LEVELS_DIFFER',[f['kind'] for f in items[key]['review_findings']])
  archive=items['ECR-PRAISOS-2']['institutional_archive_witness']
  self.assertEqual(archive['reference_number'],'BSA SPHS/1/2816.7202')
  self.assertFalse(archive['independent_ancient_witness']);self.assertFalse(archive['image_collated'])
  self.assertNotIn('institutional_archive_witness',items['ECR-PRAISOS-1'])
 def test_candidate_promotions_and_orphan_versions_rejected(self):
  for action in ['promotion','orphan','duplicate','archive_misjoin']:
   with tempfile.TemporaryDirectory() as tmp:
    root=Path(tmp)/'repo';shutil.copytree(R,root,ignore=shutil.ignore_patterns('.git','__pycache__'))
    p=root/('research/azoria-item-candidates.json' if action=='promotion' else 'research/open-image-register.json' if action=='archive_misjoin' else 'data/readings.json');x=json.loads(p.read_text())
    if action=='promotion':x['candidates'][0]['language']='ecr'
    elif action=='orphan':x[0]['object_id']='UNKNOWN'
    elif action=='duplicate':x.append(x[0])
    else:x['items'][-1]['object_id']='ECR-PRAISOS-1'
    p.write_text(json.dumps(x),encoding='utf-8')
    with self.assertRaises(ValueError):m.build(root)

 def test_unverified_azoria_count_and_join_promotions_rejected(self):
  for field in ['physical_join','text_count','image_inspection']:
   with tempfile.TemporaryDirectory() as tmp:
    root=Path(tmp)/'repo';shutil.copytree(R,root,ignore=shutil.ignore_patterns('.git','__pycache__'))
    p=root/'research/azoria-item-candidates.json';x=json.loads(p.read_text())
    if field=='physical_join':x['reported_handle_relationship']['physical_join_certified']=True
    elif field=='text_count':x['publication_count_units'][0]['eteocretan_text_count']=3
    else:x['later_publication_identity_lead']['figure_directly_inspected']=True
    p.write_text(json.dumps(x))
    with self.assertRaises(ValueError):m.build(root)
