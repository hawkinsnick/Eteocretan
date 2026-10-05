import importlib.util,json,shutil,tempfile,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1];s=importlib.util.spec_from_file_location('guarducci',R/'scripts/audit_guarducci_route.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class GuarducciRouteTests(unittest.TestCase):
 def test_route_is_actionable_but_uncollated(self):
  x=m.build();self.assertEqual(x,json.loads((R/'analysis/guarducci-route-audit.json').read_text()));self.assertEqual(x['coverage_object_count'],6);self.assertEqual(x['institutional_resource_identifier'],'000070579');self.assertEqual(x['volume_filename'],'000070579_3.pdf');self.assertEqual(x['primary_pages_collated'],0);self.assertEqual(x['reading_versions_added'],0)
 def test_false_inspection_promotion_rejected(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp)/'repo';shutil.copytree(R,root,ignore=shutil.ignore_patterns('.git','__pycache__'));p=root/'research/guarducci-1942-access-route.json';x=json.loads(p.read_text());x['edition']['volume_content_directly_inspected']=True;p.write_text(json.dumps(x));
   with self.assertRaises(ValueError):m.build(root)

 def test_repeated_citation_cannot_establish_dreros_coverage(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp)/"repo";shutil.copytree(R,root,ignore=shutil.ignore_patterns(".git","__pycache__"));p=root/"research/coverage-register.json";x=json.loads(p.read_text())
   for o in x:
    if o["object_id"]=="ECR-DREROS-1":
     for l in o["source_leads"]:
      if "Guarducci" in l.get("citation",""):l["routing_status"]="CONFIRMED"
   p.write_text(json.dumps(x))
   with self.assertRaises(ValueError):m.build(root)
