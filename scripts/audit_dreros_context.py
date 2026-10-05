"""Validate attributed physical context; no source pixels are distributed.
--verify-remote re-fetches the five public assets and checks captured hashes in memory.
Offline checks replay metadata and scientific boundaries, not pixel interpretation.
"""
import argparse, hashlib, json, re, urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];SOURCE='research/dreros-context-evidence.json'
def build(root=ROOT):
 root=Path(root);raw=(root/SOURCE).read_bytes();x=json.loads(raw)
 known={c['object_id'] for c in json.loads((root/'research/coverage-register.json').read_text())}
 assets={a['id']:a for a in x['assets']}
 if len(assets)!=len(x['assets']) or len(assets)!=5:raise ValueError('duplicate/missing source assets')
 for a in assets.values():
  if a['redistributed'] or not a['directly_inspected'] or a['source_id']!=x['source']['id']:raise ValueError('source inspection/rights mismatch')
  if not re.fullmatch('[0-9a-f]{64}',a['sha256']) or a['bytes']<=0 or not a['url'].startswith('https://www.persee.fr/'):raise ValueError('invalid source evidence')
 claims=x['assertions']
 if len({c['id'] for c in claims})!=len(claims):raise ValueError('duplicate context claims')
 for c in claims:
  if c['reading_admission'] or c['independent_review']:raise ValueError('metadata promoted to admission/review')
  if c['source_id']!=x['source']['id'] or not c['evidence_assets'] or any(a not in assets for a in c['evidence_assets']):raise ValueError('context orphan source')
  if c['scope']=='NAMED_INSCRIPTION':
   if c['object_id']!='ECR-DREROS-1' or c['object_id'] not in known:raise ValueError('photograph misjoined')
  elif c['object_id'] is not None:raise ValueError('group history assigned to a named object')
  if c['kind']=='LANGUAGE_ATTRIBUTION' and c['status']!='AUTHOR_ATTRIBUTION_NOT_PROJECT_ADJUDICATION':raise ValueError('language attribution promoted')
  if c['kind']=='DISPLAY_HISTORY_HYPOTHESIS' and c['status']!='AUTHOR_HYPOTHESIS_NOT_OBJECT_DATING':raise ValueError('history hypothesis promoted to date')
 limits=x['limits']
 if limits!={'named_object_loss_certified':False,'present_museum_accession':None,'physical_object_count':None,'new_reading_versions':0,'analytical_admissions':0,'semantic_alignment_established':False,'photograph_capture_date':None}:raise ValueError('unestablished context fact promoted')
 if x['source']['original_1946_facsimile_inspected'] or x['source']['pages_directly_inspected']!=[544,545]:raise ValueError('original edition/inspection promotion')
 if any(e['independent_ancient_witness'] for e in x['source_edges']):raise ValueError('same stone counted as independent witness')
 return {'format':'eteocretan-dreros-context-audit-v1','input_hashes':{SOURCE:hashlib.sha256(raw).hexdigest(),'research/coverage-register.json':hashlib.sha256((root/'research/coverage-register.json').read_bytes()).hexdigest()},'source_assets_inspected':len(assets),'source_page_renderings_inspected':sum(a['kind']=='page_rendering' for a in assets.values()),'source_figures_inspected':sum(a['kind']=='figure_rendering' for a in assets.values()),'context_assertions':len(claims),'named_inscription_assertions':sum(c['scope']=='NAMED_INSCRIPTION' for c in claims),'group_history_assertions':sum(c['scope']!='NAMED_INSCRIPTION' for c in claims),'reading_versions_added':0,'analytical_admissions_added':0,'source_images_redistributed':0,'named_object_loss_certified':False,'assertions':claims,'limits':limits,'boundary':'Offline audit validates metadata linkage and non-promotion, not source-pixel interpretation or independent epigraphic review.'}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');p.add_argument('--verify-remote',action='store_true');a=p.parse_args()
 out=json.dumps(build(),ensure_ascii=False,indent=2)+'\n'
 if a.verify_remote:
  for asset in json.loads((ROOT/SOURCE).read_text())['assets']:
   data=urllib.request.urlopen(asset['url'],timeout=30).read()
   if hashlib.sha256(data).hexdigest()!=asset['sha256']:raise ValueError('Remote asset drift: '+asset['id'])
  print('All captured remote source assets match; no files saved.')
 if a.check:
  if (ROOT/'analysis/dreros-context-audit.json').read_text()!=out:raise SystemExit('Dreros context audit stale')
  print('Dreros physical-context metadata replays without reading/identity promotion.')
 elif not a.verify_remote:print(out,end='')
if __name__=='__main__':main()
