"""Bind the Guarducci institutional access route to existing coverage leads."""
import argparse,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];ROUTE='research/guarducci-1942-access-route.json';COVERAGE='research/coverage-register.json'
def build(root=ROOT):
 root=Path(root);raw=(root/ROUTE).read_bytes();route=json.loads(raw);coverage=json.loads((root/COVERAGE).read_text());matched=[]
 concordance=json.loads((root/'research/praisos-guarducci-number-concordance.json').read_text())
 supported={r['project_id'] for r in concordance['records']}
 unsupported=[]
 for obj in coverage:
  if any('Guarducci' in lead.get('citation','') and 'pp. 134–142' in lead.get('citation','') for lead in obj.get('source_leads',[])):
   if obj['object_id'] in supported:matched.append(obj['object_id'])
   else:
    leads=[l for l in obj['source_leads'] if 'Guarducci' in l.get('citation','')]
    if any(l.get('routing_status')!='UNVERIFIED_FOR_THIS_OBJECT' for l in leads):raise ValueError('unsupported edition coverage promoted')
    unsupported.append(obj['object_id'])
 if matched!=['ECR-PRAISOS-1','ECR-PRAISOS-2','ECR-PRAISOS-3','ECR-PRAISOS-4','ECR-PRAISOS-5','ECR-PRAISOS-6']:raise ValueError('Guarducci coverage join changed')
 if unsupported!=route['routing_correction']['unsupported_inherited_project_ids'] or matched!=route['routing_correction']['supported_reported_project_ids']:raise ValueError('route correction drift')
 e=route['edition']
 if e['volume_content_directly_inspected'] or not e['catalogue_metadata_directly_inspected']:raise ValueError('access/inspection state invalid')
 return {'format':'eteocretan-guarducci-route-audit-v1','route_sha256':hashlib.sha256(raw).hexdigest(),'coverage_sha256':hashlib.sha256((root/COVERAGE).read_bytes()).hexdigest(),'coverage_object_count':len(matched),'coverage_object_ids':matched,'unsupported_inherited_object_ids':unsupported,'concordance_sha256':hashlib.sha256((root/'research/praisos-guarducci-number-concordance.json').read_bytes()).hexdigest(),'institutional_resource_identifier':e['resource_identifier'],'volume_filename':e['volume_filename'],'project_print_locator':e['project_locator'],'primary_pages_collated':0,'reading_versions_added':0,'analytical_admissions_added':0,'boundary':route['boundary']}
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();output=json.dumps(build(),ensure_ascii=False,indent=2)+'\n';target=ROOT/'analysis/guarducci-route-audit.json'
 if a.check:
  if target.read_text()!=output:raise SystemExit('Guarducci route audit stale')
  print('Guarducci institutional route supports six reported Praisos joins; two Dreros citations remain unverified.')
 else:print(output,end='')
