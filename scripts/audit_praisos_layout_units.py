"""Reconcile primary-page line counts with project representation rows."""
import argparse, hashlib, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = "research/praisos-primary-layout-evidence.json"

def build(root=ROOT):
    root = Path(root); raw = (root / EVIDENCE).read_bytes(); evidence = json.loads(raw); readings = json.loads((root / "data/readings.json").read_text())
    records = {r["record_id"]: r for r in readings}; rows = []
    for entry in evidence["entries"]:
        if hashlib.sha256((root / entry["evidence_path"]).read_bytes()).hexdigest() != entry["evidence_sha256"]: raise ValueError("primary page hash mismatch")
        versions = [records[rid] for rid in entry["source_record_ids"]]
        if any(v["object_id"] != entry["project_object_id"] for v in versions): raise ValueError("layout/object join mismatch")
        expected = entry["project_representation_row_labels"]
        if any([line["label"] for line in v["lines"]] != expected for v in versions): raise ValueError("project row labels diverge from registered layout")
        if entry["project_object_id"] == "ECR-PRAISOS-2" and entry["printed_alternative_count"] != len(versions): raise ValueError("alternative count mismatch")
        rows.append({"project_object_id": entry["project_object_id"], "source_line_count": entry["source_line_count"],
                     "reading_version_count": len(versions), "rows_per_version": [len(v["lines"]) for v in versions],
                     "printed_group_count": len(entry.get("printed_transliteration_group_labels", [])) or None})
    return {"format": "eteocretan-praisos-layout-unit-audit-v1", "evidence_sha256": hashlib.sha256(raw).hexdigest(),
            "objects": rows, "source_line_total_across_three_objects": sum(r["source_line_count"] for r in rows),
            "reading_version_count": sum(r["reading_version_count"] for r in rows), "preferred_readings_selected": 0,
            "boundary": evidence["boundary"]}

if __name__ == "__main__":
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--check",action="store_true");a=p.parse_args();output=json.dumps(build(),ensure_ascii=False,indent=2)+"\n";target=ROOT/"analysis/praisos-layout-unit-audit.json"
    if a.check:
        if target.read_text(encoding="utf-8")!=output: raise SystemExit("Praisos layout-unit audit stale")
        print("Praisos source lines, alternatives and representation rows replay exactly.")
    else: print(output,end="")
