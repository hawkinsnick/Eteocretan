"""Compare literal recorded versions without deciding physical line alignment."""
import hashlib,itertools,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def compare(readings):
    if len({r['record_id'] for r in readings})!=len(readings):
        raise ValueError('duplicate reading version')
    pairs=[]
    for a,b in itertools.combinations(readings,2):
        if a['object_id']!=b['object_id'] or a['source_level']==b['source_level']:continue
        def summary(r):
            return {'record_id':r['record_id'],'representation':r['representation'],
                    'source_level':r['source_level'],'source':r['source'],
                    'line_count':len(r['lines']),
                    'literal_text_sha256':hashlib.sha256('\n'.join(l['text'] for l in r['lines']).encode()).hexdigest()}
        pairs.append({'object_id':a['object_id'],'versions':[summary(a),summary(b)],
                      'literal_source_strings_equal':[l['text'] for l in a['lines']]==[l['text'] for l in b['lines']],
                      'physical_line_alignment_established':False,'preferred_version':None,
                      'analysis_admission_granted':False})
    return {'format':'eteocretan-reading-version-comparison-v1','pairs':pairs,
            'normalization_applied':False,'independent_review':False,
            'boundary':'Literal version comparison only. Line counts are representation units; grouped historical lines and modern line division need not agree. Script conversion, lacuna repair, segmentation and source preference are not inferred.'}
if __name__=='__main__':
    print(json.dumps(compare(json.loads((R/'data/readings.json').read_text())),ensure_ascii=False,indent=2))
