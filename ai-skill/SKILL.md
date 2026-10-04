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
