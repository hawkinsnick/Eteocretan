---
name: eteocretan-research
description: Evidence-first AI research skill for the Eteocretan corpus.
version: 0.3.1
---

# Eteocretan Research Skill

This skill is an interface to the corpus in this repository. The corpus remains the canonical source of truth. Never maintain an independent scholarly dataset inside the skill.

## Governing rules
1. Separate physical/epigraphic observation, source transcription, normalization, computational derivation, scholarly interpretation, and AI-derived analysis.
2. Prefer canonical machine-readable corpus records over prose summaries for record-level questions.
3. Preserve identifiers, provenance, uncertainty, disagreements, corrections, negative results, and superseded analyses.
4. Never invent missing signs, readings, restorations, provenience, bibliography, source independence, or rights.
5. Label calculations performed by the AI and state enough method for reproduction.
6. Respect record/source-specific licensing and attribution. Repository-level licensing must not erase upstream restrictions.
7. For cross-corpus claims, establish comparability and source independence before interpreting similarity.
8. Report blocked or missing evidence rather than filling gaps.

## Corpus-specific caution
Poorly understood language: preserve inscriptional uncertainty and distinguish readable script/transliteration from uncertain linguistic interpretation.

## Default research response
Give the direct answer, followed as relevant by Evidence; Evidentiary status; Uncertainty/limitations; Reproducibility; Rights/attribution.

## Synchronization
Read `ai-skill/generated/source-state.json` before substantive work. It records the corpus commit from which the AI-facing package was synchronized. Generated files are rebuildable views; canonical corpus files govern if a discrepancy is found.

## Academic-scrutiny gates
- Analytically admitted rows and tokens remain zero
- Alternative reading versions of one inscription are not independent witnesses
- Historical encodings are not new observations of the stones
- Arkalochori is not admitted as Eteocretan
- Decipherment and cross-script phonetic equivalence remain blocked

## Source reconciliation checkpoint
Read `docs/SOURCE-RECONCILIATION.md` and the indexed source-reconciliation artifacts before comparing versions, counting identities, or preparing specialist review.
- Use source-critical dossiers to retain project attribution versus attributed secondary classification conflicts.
- Two Azoria D300 handles are source-caption candidates with uncertain language and unreconciled inventory numbers; never admit them or infer two unique vessels.
- BSA SPHS/1/2816.7202 is source-identity crosswalked to project Praisos 2 through the archive's nomos-fragment title and Conway's Pr. II terminology; it is a copy negative, not an independent ancient witness, and does not establish a museum accession or image collation.
- Praisos source-line counts are 5, 12 and 14. Praisos 1's five lines are represented as three printed groups, while Praisos 2's two twelve-row alternatives are one object and one historical source presentation, not two witnesses.
- The primary-page crosswalk maps Pr. I/barxe, Pr. II/nomos and the third fragment to project Praisos 1, 2 and 3 respectively; it selects no preferred reading and establishes no modern museum identity.
- The Anemi institutional record identifies Guarducci volume III as resource 000070579 and file 000070579_3.pdf, with the project's print target at pp. 134–142. Delivery failed during this checkpoint, so the route adds no collated pages, readings, admissions, scan rights, or physical-object identities.
- Lejeune 1947 p. 276 n. 4 reports Guarducci nos. 1–6: three historically named inscriptions and three short fragments only perhaps Eteocretan. Script classifications are attributed source claims; number-label correspondence for nos. 4–6 is not language or physical-identity certification.

- Azoria Figure 42 / 06-0334 (D346.1) corresponds to the upper bin-lining handle at the level of primary article textual description. No figure image or museum accession was verified. The same-pithos relationship is qualified, and 3 room sherds / 17 site sherds are not Eteocretan text denominators.

At version 1.1.0, route physical-context questions through `research/dreros-context-evidence.json` and its audit. Preserve object-specific attribution versus group history, author hypotheses versus object dates, and photographic publication identity versus readings. A bilingual caption does not certify translation equivalence. Guarducci’s six reported Praisos correspondences do not establish Dreros coverage; its two inherited Dreros citations remain explicitly unverified.


## Offline corpus browser
Run `python scripts/build_corpus_browser.py` to generate `workbench/corpus-browser.html`. It searches only files explicitly admitted by `research/browser-sources.json`. Browser admission requires rights/provenance review; never recursively ingest restricted or raw upstream material. Display does not establish decipherment, source independence, or expert validation.


## Linear A method-parity gate
The repository has reached the machine-resolvable pre-expert method-parity baseline: source lineage, disagreements, rights/source controls, rights-allowlisted browser, read-only API, loss-aware exports, parity validation and expert-review packaging are present. Read `docs/RIGHTS-ONLY-READINESS.md` and `research/residual-blocker-ledger.json` before claiming completeness. Further systematic evidence growth is currently constrained by lawful access/rights to critical editions and object-level evidence. Expert adjudication remains a downstream scientific gate, not unfinished software. Do not turn Azoria collection counts into Eteocretan text counts or resolve Praisos classification conflicts by majority vote.


## Rights-wall re-audit (2026-10-06)

Before describing Guarducci 1942 as inaccessible, read `research/rights-wall-audit-2026-10-06.md`. University of Crete Anemi resource 000070579 publicly exposes volume III as `000070579_3.pdf`; access and redistribution rights are separate questions. A Greek-government catalogue PDF encountered during the audit is a later review of Guarducci III, not the edition, and must not substitute for it.

Public museum and Azoria discovery searches do not establish safe accession joins for the Eteocretan objects. The SCS description of two probably Eteocretan pithos handles strengthens an attributed discovery/classification lead only. Never promote those handles, museum objects, or Dreros location claims to canonical identity without authoritative evidence.


## Four-front public-source exhaustion (2026-10-06)

Read `research/duhoux-concordance-targets.json`, `research/praisos-ic-crosswalk.json`, `research/azoria-item-candidates.json`, and `research/dreros-source-genealogy.json` before proposing corpus expansion.

- Duhoux's 13-text universe (six secure / seven uncertain in the public review) is a reconciliation target, not permission to reconstruct or copy his critical edition.
- Publication identifiers such as IC numbers do not establish museum accessions or preferred readings.
- Azoria's 17 inscribed sherds are a site-wide discovery denominator. Only two handle candidates are currently represented individually; never synthesize fifteen missing Eteocretan records.
- Dreros editions and later discussions belong to a witness genealogy. Dependent editions, photographs and secondary transcriptions do not multiply independent ancient witnesses.

Under the currently admitted public evidence, additional canonical readings/object identities require new lawful source or institutional evidence; downstream epigraphic adjudication remains human-only.

## Validation and AI-use guide
Consult `docs/VALIDATION-AND-AI-USE.md` before asserting reproducibility, corpus completeness, expert acceptance or cross-corpus comparability. Record the source commit and actual validation outputs. Keep scientific review gates separate from passing software checks.

## Evidence-denominator policy
When comparing Eteocretan coverage, distinguish named inscriptions, editorial reading versions, source rows, and analytically admitted rows/tokens. Do not count alternative transcriptions as independent ancient witnesses or convert zero admitted tokens into linguistic frequency estimates. Preserve classification disputes and source-access limitations until independently resolved.
