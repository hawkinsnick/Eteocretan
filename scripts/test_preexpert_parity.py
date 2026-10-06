#!/usr/bin/env python3
import json,pathlib,sys
R=pathlib.Path(__file__).resolve().parents[1]
req=["data/records.json","research/coverage-register.json","research/source-lineage-register.json","research/disagreement-register.json","research/rights-source-matrix.json","research/residual-blocker-ledger.json","research/browser-sources.json"]
missing=[p for p in req if not (R/p).exists()]
records=json.loads((R/"data/records.json").read_text());coverage=json.loads((R/"research/coverage-register.json").read_text())
assert not missing,missing
assert len(records)==12,len(records)
assert len(coverage)==11,len(coverage)
assert sum(1 for r in records for l in r.get("lines",[]) if l.get("analysis_eligible"))==0
assert all(not x.get("analysis_eligible") for x in coverage)
print(json.dumps({"status":"PASS","records":len(records),"coverage_entries":len(coverage),"analysis_eligible_lines":0,"required_controls":len(req)}))
