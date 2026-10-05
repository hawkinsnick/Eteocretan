"""Build source-located object dossiers; never adjudicate readings or admit rows."""
import argparse,hashlib,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def build(root=ROOT):
 root=Path(root)
 def read(path):return json.loads((root/path).read_text())
 coverage=read('research/coverage-register.json');readings=read('data/readings.json')
 archive=read('research/institutional-archive-leads.json');images=read('research/open-image-register.json')
 azoria=read('research/azoria-item-candidates.json');dreros=read('research/source-inspection-2026-10-02.json');lejeune=read('research/dreros1-lejeune-critical-witness.json')
 context=read('research/dreros-context-evidence.json')
 known={c['object_id']:c for c in coverage}
 if len(known)!=len(coverage):raise ValueError('duplicate coverage object')
 if len({r['record_id'] for r in readings})!=len(readings):raise ValueError('duplicate reading version')
 if any(r['object_id'] not in known for r in readings):raise ValueError('reading has no coverage identity')
 if azoria['collection_parent'] not in known:raise ValueError('Azoria parent missing')
 archive_entry=archive['entries'][0];join=archive_entry['project_object_join']
 if join['object_id']!='ECR-PRAISOS-2' or join['object_id'] not in known:raise ValueError('nomos-fragment source identity misjoined')
 image_matches=[i for i in images['items'] if i.get('asset_id')==archive_entry['reference_number']]
 if len(image_matches)!=1 or image_matches[0]['object_id']!=join['object_id']:raise ValueError('archive/image register identity mismatch')
 ids=[c['candidate_id'] for c in azoria['candidates']]
 if len(ids)!=len(set(ids)):raise ValueError('duplicate Azoria candidate')
 for c in azoria['candidates']:
  if c['analysis_eligible'] or c['language'] is not None or c['physical_object_identity_certified']:raise ValueError('unreconciled Azoria candidate promoted')
 relationship=azoria['reported_handle_relationship']
 if relationship['physical_join_certified'] or relationship['unique_vessel_count'] is not None:raise ValueError('hypothetical pithos join promoted')
 lead=azoria['later_publication_identity_lead']
 if lead['figure_directly_inspected'] or lead['museum_accession_established']:raise ValueError('indexed text promoted to figure or museum verification')
 if any(u['eteocretan_text_count'] is not None for u in azoria['publication_count_units']):raise ValueError('sherd counts promoted to Eteocretan text counts')
 dossiers=[]
 for obj in coverage:
  if obj['analysis_eligible']:raise ValueError('coverage cannot grant admission through dossier generation')
  versions=[r for r in readings if r['object_id']==obj['object_id']]
  if set(obj['reading_versions'])!={r['record_id'] for r in versions}:raise ValueError('coverage/version association mismatch')
  rows=[]
  for v in versions:
   source=v['source'];evidence=root/source['evidence_path']
   if hashlib.sha256(evidence.read_bytes()).hexdigest()!=source['sha256']:raise ValueError('reading evidence changed')
   rows.append({'record_id':v['record_id'],'source_level':v['source_level'],'representation':v['representation'],
    'source':source,'representation_row_count':len(v['lines']),
    'partition_counts':dict(Counter(l.get('partition','not_recorded') for l in v['lines'])),
    'literal_text_sha256':hashlib.sha256('\n'.join(l['text'] for l in v['lines']).encode()).hexdigest(),
    'preferred_version':False,'analysis_admission_granted':False})
  item={'object_id':obj['object_id'],'coverage_status':obj['status'],'versions':rows,
   'primary_historical_version_count':sum(v['source_level']=='primary_historical_edition' for v in versions),
   'source_leads':obj['source_leads'],'analysis_eligible':False,'independent_review':False,'review_findings':[]}
  baseline=obj.get('scholarly_baseline',{})
  if obj['status']=='uncertain_language' and 'undoubtedly' in baseline.get('classification',''):
   item['review_findings'].append({'kind':'ATTRIBUTION_LEVELS_DIFFER','project_status':obj['status'],'reported_secondary_baseline':baseline,'decision':None,'note':'Secondary classification is attributed, not project-established language identity.'})
  if obj['object_id']=='ECR-DREROS-1':
   item['near_primary_witness']=lejeune
   item['later_photograph_context']={'source':context['source'],'assets':context['assets'],'assertions':[c for c in context['assertions'] if c['object_id']==obj['object_id']],'limits':context['limits']}
   item['review_findings'].append({'kind':'ORIGINAL_EDITION_ACQUISITION_OPEN','citation':lejeune['primary_locator'],'decision':None})
  if obj['object_id']=='ECR-DREROS-2':
   item['primary_metadata_candidates']=[a for a in dreros['assertions'] if a.get('project_object_id')==obj['object_id']]
   item['review_findings'].append({'kind':'SOURCE_ITEM_NUMBER_IS_NOT_PROJECT_NUMBER','excluded_other_edition_item':'no. 6','decision':None})
  if obj['object_id']==join['object_id']:
   item['institutional_archive_witness']={'reference_number':archive_entry['reference_number'],'archive_unit':archive_entry['archive_unit'],'identity_status':archive_entry['identity_status'],'project_object_join':join,'independent_ancient_witness':False,'image_collated':False}
  if obj['object_id']==azoria['collection_parent']:
   item['item_candidates']=azoria['candidates']
   item['publication_identity_lead']=azoria['later_publication_identity_lead']
   item['reported_handle_relationship']=azoria['reported_handle_relationship']
   item['publication_count_units']=azoria['publication_count_units']
   item['publication_language_assessment']=azoria['publication_language_assessment']
  if len(versions)>1:item['review_findings'].append({'kind':'MULTIPLE_READING_VERSIONS','physical_line_alignment_established':False,'decision':None})
  dossiers.append(item)
 paths=['research/dreros-context-evidence.json','data/readings.json','research/coverage-register.json','research/azoria-item-candidates.json','research/source-inspection-2026-10-02.json','research/dreros1-lejeune-critical-witness.json','research/institutional-archive-leads.json','research/open-image-register.json']
 return {'format':'eteocretan-source-critical-dossier-v1','input_hashes':{p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in paths},
  'coverage_entries':len(coverage),'reading_versions':len(readings),'azoria_item_candidates':len(ids),
  'canonical_admissions_added':0,'dossiers':dossiers,
  'boundary':'Dossiers group attributed evidence and pending decisions. Candidate labels, reading versions, source rows and physical monuments are distinct units; no line alignment or language decision is inferred.'}
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();output=json.dumps(build(),ensure_ascii=False,indent=2)+'\n'
 if a.check:
  if (ROOT/'analysis/source-critical-dossier.json').read_text()!=output:raise SystemExit('Source critical dossier stale')
  print('All eleven coverage identities, twelve reading versions and two Azoria candidates replay.')
 else:print(output,end='')
