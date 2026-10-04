# Source reconciliation checkpoint — 4 October 2026

The source-critical dossier organizes all eleven coverage entries and twelve attributed reading versions for review. It preserves evidence, source hashes, language-partition counts, representation units and unresolved decisions without selecting a preferred reading.

```sh
python scripts/build_review_dossier.py --check
python scripts/audit_praisos_identity.py --check
python scripts/audit_praisos_layout_units.py --check
python scripts/release_check.py
```

Read `analysis/source-critical-dossier.json` for per-object evidence and `research/azoria-item-candidates.json` for the two new source-located candidate descriptions.

## New source distinctions

| Candidate | Excavators' reported context | Identity and attribution |
|---|---|---|
| D300 upper handle | Attached to the pithos fragment used in a basin/bin lining | Inventory number unresolved; Eteocretan (?) remains attributed. |
| D300 lower handle | Room destruction deposit | Inventory number unresolved; Eteocretan (?) remains attributed. |

Source: University of North Carolina Azoria Project, 2006 summary, §4 D300 and the pithos-handle caption: https://azoria.unc.edu/summary-field-reports/2006-summary/ . Source images and full readings are not redistributed. These candidates are separate from the native reading archive. They may relate to the reported seventeen-sherd collection, but that relationship and whether they represent distinct vessels remain unestablished.

The dossier also connects Dreros 1 to Lejeune's 1947 near-primary critical witness and its original 1946 publication target. Dreros 2 remains a candidate association with BCH edition **no. 5**, not a mechanically inferred association with source no. 2 or no. 6. Praisos 4–5 retain both the project's uncertain-language status and the differently attributed secondary baseline classification; the dossier flags that difference for review rather than resolving it automatically.

## Remaining frontier

Acquire and collate later Praisos critical editions and the original Dreros 1 facsimile. Resolve Azoria excavation and museum identifiers before any object-count claim. Compare original layouts, damaged signs, Greek/Eteocretan partitions and proposed restorations with qualified scrutiny. Twelve reading versions are not twelve independent witnesses, and all analytically admitted rows remain zero.

## Exact institutional and excavation source leads

The BSA institutional catalogue supplies archive reference **BSA SPHS/1/2816.7202**, item 157706, for the Praesos nomos-fragment copy negative, with a BSA 8:125 publication reference. Primary-page markers now support a three-way historical identity crosswalk: **Pr. I / barxe-inscription = ECR-PRAISOS-1**, **Pr. II / nomos-inscription = ECR-PRAISOS-2**, and **third Eteocretan fragment = ECR-PRAISOS-3**. `research/praisos-historical-identity-crosswalk.json` records the exact pages and hashes; `analysis/praisos-identity-audit.json` replays them. The BSA negative is therefore attached to Praisos 2, but remains a reproduction rather than a second ancient witness. Museum accessions, present physical-object identities, image rights and direct image collation remain pending.

The publisher-indexed Hesperia text supplies **06-0334 (D346.1), Figure 42** as an Azoria handle lead. Direct PDF retrieval failed, so this remains an excerpt-located source lead, not a directly inspected figure or a verified match to either caption candidate.

## Praisos layout and counting units

Direct inspection of the registered Conway pages now distinguishes source lines from project rows and reading alternatives. Praisos 1 has five numbered source lines but Conway groups them into three printed transliteration units (`1–2`, `3–4`, `5`). Praisos 2 has twelve lines printed in two alternative transcriptions of the same inscription. Praisos 3 has fourteen printed lines. `research/praisos-primary-layout-evidence.json` records exact page locators and hashes; `analysis/praisos-layout-unit-audit.json` replays the four project reading versions against those structures. The resulting 31 source lines, 41 project rows across four versions, and three physical publication identities are deliberately not interchangeable denominators.
