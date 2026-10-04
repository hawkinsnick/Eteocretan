"""Bind Lejeune's reported Guarducci numbers without promoting fragments."""
import argparse,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];SOURCE='research/praisos-guarducci-number-concordance.json';COVERAGE='research/coverage-register.json'
def build(root=ROOT):
 root=Path(root);raw=(root/SOURCE).read_bytes();x=json.loads(raw);coverage=json.loads((root/COVERAGE).read_text());records=x['records'];ids={o['object_id'] for o in coverage}
 if [r['guarducci_number'] for r in records]!=list(range(1,7)) or any(r['project_id'] not in ids for r in records):raise ValueError('Guarducci number coverage changed')
 named=[r for r in records if r['join_status']=='HISTORICAL_NAME_AND_NUMBER_CROSSWALK'];fragments=[r for r in records if r['join_status']=='PROJECT_NUMBER_LABEL_CORRESPONDENCE_ONLY']
 if len(named)!=3 or len(fragments)!=3 or any(r['language_status_reported']!='short fragment, perhaps Eteocretan' for r in fragments):raise ValueError('fragment uncertainty changed')
 return {'format':'eteocretan-praisos-guarducci-number-audit-v1','input_hashes':{SOURCE:hashlib.sha256(raw).hexdigest(),COVERAGE:hashlib.sha256((root/COVERAGE).read_bytes()).hexdigest()},'reported_number_count':6,'historically_named_crosswalk_count':3,'number_only_fragment_correspondence_count':3,'perhaps_eteocretan_fragment_count':3,'primary_guarducci_pages_collated':0,'physical_identities_certified':0,'records':[{'guarducci_number':r['guarducci_number'],'project_id':r['project_id'],'join_status':r['join_status'],'script_class_reported':r['script_class_reported'],'language_status_reported':r['language_status_reported']} for r in records],'boundary':x['boundary']}
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();out=json.dumps(build(),ensure_ascii=False,indent=2)+'\n';target=ROOT/'analysis/praisos-guarducci-number-audit.json'
 if a.check:
  if json.loads(target.read_text())!=build():raise SystemExit('Praisos Guarducci-number audit stale')
  print('Six reported Guarducci numbers replay without promoting three uncertain fragments.')
 else:print(out,end='')
