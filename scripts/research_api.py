#!/usr/bin/env python3
import argparse,json,pathlib
R=pathlib.Path(__file__).resolve().parents[1]
FILES={"records":"data/records.json","coverage":"research/coverage-register.json","disagreements":"research/disagreement-register.json"}
def load(k):
 v=json.loads((R/FILES[k]).read_text(encoding="utf-8"))
 return v if isinstance(v,list) else v.get("items",[])
p=argparse.ArgumentParser();p.add_argument("resource",choices=FILES);p.add_argument("--text",default="");p.add_argument("--limit",type=int,default=50);a=p.parse_args();q=a.text.lower();rows=[x for x in load(a.resource) if not q or q in json.dumps(x,ensure_ascii=False).lower()][:a.limit];print(json.dumps({"resource":a.resource,"records":rows,"warning":"Attributed evidence only; not decipherment, independent confirmation or expert adjudication."},ensure_ascii=False,indent=2))
