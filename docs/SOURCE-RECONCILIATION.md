# Source reconciliation checkpoint — 4 October 2026

The source-critical dossier organizes all eleven coverage entries and twelve attributed reading versions for review. It preserves evidence, source hashes, language-partition counts, representation units and unresolved decisions without selecting a preferred reading.

```sh
python scripts/build_review_dossier.py --check
python scripts/audit_praisos_identity.py --check
python scripts/audit_praisos_layout_units.py --check
python scripts/audit_guarducci_route.py --check
python scripts/audit_praisos_guarducci_numbers.py --check
python scripts/release_check.py
```

Read `analysis/source-critical-dossier.json` for per-object evidence and `research/azoria-item-candidates.json` for the two new source-located candidate descriptions.

## New source distinctions

| Candidate | Excavators' reported context | Identity and attribution |
|---|---|---|
| D300 upper handle | Attached to the pithos fragment used in a basin/bin lining | Description-level Figure 42 link to excavation 06-0334 (D346.1); museum accession unresolved; language uncertain. |
| D300 lower handle | Room destruction deposit | Inventory number unresolved; Eteocretan (?) remains attributed. |

Source: University of North Carolina Azoria Project, 2006 summary, §4 D300 and the pithos-handle caption: https://azoria.unc.edu/summary-field-reports/2006-summary/ . Source images and full readings are not redistributed. These candidates are separate from the native reading archive. They may relate to the reported seventeen-sherd collection, but that relationship and whether they represent distinct vessels remain unestablished.

The dossier also connects Dreros 1 to Lejeune's 1947 near-primary critical witness and its original 1946 publication target. Dreros 2 remains a candidate association with BCH edition **no. 5**, not a mechanically inferred association with source no. 2 or no. 6. Praisos 4–5 retain both the project's uncertain-language status and the differently attributed secondary baseline classification; the dossier flags that difference for review rather than resolving it automatically.

## Remaining frontier

Acquire and collate later Praisos critical editions and the original Dreros 1 facsimile. Resolve Azoria excavation and museum identifiers before any object-count claim. Compare original layouts, damaged signs, Greek/Eteocretan partitions and proposed restorations with qualified scrutiny. Twelve reading versions are not twelve independent witnesses, and all analytically admitted rows remain zero.

## Exact institutional and excavation source leads

The BSA institutional catalogue supplies archive reference **BSA SPHS/1/2816.7202**, item 157706, for the Praesos nomos-fragment copy negative, with a BSA 8:125 publication reference. Primary-page markers now support a three-way historical identity crosswalk: **Pr. I / barxe-inscription = ECR-PRAISOS-1**, **Pr. II / nomos-inscription = ECR-PRAISOS-2**, and **third Eteocretan fragment = ECR-PRAISOS-3**. `research/praisos-historical-identity-crosswalk.json` records the exact pages and hashes; `analysis/praisos-identity-audit.json` replays them. The BSA negative is therefore attached to Praisos 2, but remains a reproduction rather than a second ancient witness. Museum accessions, present physical-object identities, image rights and direct image collation remain pending.

The publicly author-uploaded Haggis et al. article indexed text (Hesperia 80, 2011, printed pp. 57–58, Figure 42; footnotes 130, 134) supports a description-level link between the bin-lining upper handle and excavation **06-0334 (D346.1)**. The second handle has no resolved individual identifier. The authors qualify the same-pithos hypothesis with “presumably”; no physical join is certified. Three D300 inscribed sherds and seventeen site-wide inscribed sherds are separate denominators, neither an Eteocretan text count. The language suggestion remains explicitly non-probative. See https://www.researchgate.net/publication/273676601_Excavations_in_the_Archaic_Civic_Buildings_at_Azoria_in_2005-2006 . Publisher/UNC delivery failed (502), and direct ResearchGate retrieval returned 403. Indexed text was inspected; PDF pages and figure pixels were not. Only original metadata and attributed summaries are redistributed.

## Praisos layout and counting units

Direct inspection of the registered Conway pages now distinguishes source lines from project rows and reading alternatives. Praisos 1 has five numbered source lines but Conway groups them into three printed transliteration units (`1–2`, `3–4`, `5`). Praisos 2 has twelve lines printed in two alternative transcriptions of the same inscription. Praisos 3 has fourteen printed lines. `research/praisos-primary-layout-evidence.json` records exact page locators and hashes; `analysis/praisos-layout-unit-audit.json` replays the four project reading versions against those structures. The resulting 31 source lines, 41 project rows across four versions, and three physical publication identities are deliberately not interchangeable denominators.

## Guarducci volume route

`research/guarducci-1942-access-route.json` records the University of Crete Anemi institutional route to Margherita Guarducci, *Inscriptiones Creticae*, volume III (1942): permanent metadata resource **000070579**, volume file **000070579_3.pdf**, 101 scan pages, reported 600-dpi digitization dated 10 December 2003, and project print locator pp. 134–142. The supported route comprises six reported Praisos number correspondences. Two inherited generic Dreros citations are explicitly unverified and excluded from supported coverage. `analysis/guarducci-route-audit.json` binds that route to the coverage register by hashes and identifiers.

The institutional record and delivery metadata were inspected, but direct volume delivery returned gateway/time-out failures in this environment. Therefore zero primary pages, readings, or analytical rows were collated from this route. The registered file size and page count describe the institutional digital object; they do not establish that the relevant pages were seen, that the scan is openly redistributable, or that publication labels establish unique physical objects. A future lawful inspection must verify title/volume pages and pp. 134–142 before adding evidence or readings.

## Guarducci publication-number concordance

A directly inspected Persée rendering of Michel Lejeune (1947), p. 276 n. 4, reports Guarducci's section III, pp. 137–142, nos. 1–6. It names nos. 1–3 as the *barxe*, *nomos* and *neihar* inscriptions, respectively. It describes nos. 4–6 only as short fragments that may be Eteocretan. The same note attributes Ionic script to nos. 2, 3 and 5, and archaic script to nos. 1, 4 and 6. `research/praisos-guarducci-number-concordance.json` preserves those source attributions; `analysis/praisos-guarducci-number-audit.json` binds all six publication numbers to the project labels without converting the last three into certain Eteocretan texts.

This witness improves the publication-number crosswalk but does not replace inspection of Guarducci, certify present objects or museum accessions, or select readings and dates. The first three historical name/number joins and the last three number-only fragment correspondences remain different evidence classes.

## 1.1.0 physical context and source routing checkpoint

Van Effenterre’s 1961 BCH article supplies an inspected photograph of the Dreros Isaluria stone: p. 545, Figure 1, linked by n. 2 to the original RPhil 1946 pp. 131 onward. The same note distinguishes the lightly pointed Greek text from the chisel-cut inscription. The caption’s language labels remain author attribution, not certification of a bilingual translation or a new critical reading. Two page renderings (544–545) and the Figure 1 rendering were visually inspected; URLs, hashes and original short metadata summaries are registered. No source images or full article/transcription are redistributed.

The 1961 report also discusses group-level display and conservation. The proposed long display on the east Delphinion wall is an author hypothesis, not a resolved inscription date. Reports about blocks beneath a collapsed shelter and apparent wartime losses at Neapolis cannot be assigned to either named Dreros object. See `research/dreros-context-evidence.json` and `analysis/dreros-context-audit.json`.

The Guarducci route audit now uses the reported number concordance rather than counting repeated citations as coverage. It separates six Praisos publication-number correspondences from two unverified Dreros volume references. Direct Guarducci inspection remains zero; the Anemi retry returned 502. A government portal item describes a review of the edition and has not been admitted as the full volume. The original 1946 facsimile, Duhoux/Guarducci collation, museum identities and independent review remain open.

Run `python scripts/audit_dreros_context.py --check` for metadata replay. Optional `--verify-remote` retrieves the five registered public assets into memory and checks hashes; network failures or source drift do not imply scholarly validation.
