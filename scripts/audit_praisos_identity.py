"""Replay the primary-page Praisos I/II/III identity crosswalk."""
import argparse,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def audit(root=ROOT):
 root=Path(root)
 def read(p):return json.loads((root/p).read_text(encoding='utf-8'))
 cross=read('research/praisos-historical-identity-crosswalk.json');readings=read('data/readings.json');archive=read('research/institutional-archive-leads.json');versions={r['record_id']:r for r in readings};objects=[]
 for entry in cross['entries']:
  if hashlib.sha256((root/entry['evidence_path']).read_bytes()).hexdigest()!=entry['evidence_sha256']:raise ValueError('primary page hash mismatch')
  version=versions.get(entry['project_reading_record'])
  if not version or version['object_id']!=entry['project_object_id']:raise ValueError('historical reading/object join mismatch')
  if entry['project_object_id']!='ECR-PRAISOS-3' and entry['literal_identity_marker'] not in ''.join(line['text'] for line in version['lines']):raise ValueError('literal identity marker absent from reading')
  objects.append(entry['project_object_id'])
 if objects!=['ECR-PRAISOS-1','ECR-PRAISOS-2','ECR-PRAISOS-3']:raise ValueError('Praisos historical order changed')
 a=cross['archive_join'];lead=next(e for e in archive['entries'] if e['reference_number']==a['reference_number'])
 if lead['project_object_join']['object_id']!=a['project_object_id'] or a['archive_title_marker'] not in lead['title']:raise ValueError('archive/crosswalk mismatch')
 return {'format':'eteocretan-praisos-identity-audit-v1','crosswalk_sha256':hashlib.sha256((root/'research/praisos-historical-identity-crosswalk.json').read_bytes()).hexdigest(),'objects_reconciled':objects,'archive_reference':a['reference_number'],'archive_join':a['project_object_id'],'preferred_readings_selected':0,'museum_accessions_established':0,'independent_reviews_added':0,'boundary':cross['boundary']}
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();output=json.dumps(audit(),ensure_ascii=False,indent=2)+'\n';target=ROOT/'analysis/praisos-identity-audit.json'
 if a.check:
  if target.read_text(encoding='utf-8')!=output:raise SystemExit('Praisos identity audit stale')
  print('Praisos I/II/III source identities and BSA archive join replay exactly.')
 else:print(output,end='')
