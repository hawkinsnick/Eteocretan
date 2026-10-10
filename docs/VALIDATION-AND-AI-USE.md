# Validation and AI research use

This guide states reproducible checks and scientific boundaries. It is not an independent scholarly review or a new corpus reading.

## Local verification

From the repository root, run:

```sh
python -m corpuskit validate
python -m corpuskit audit
python scripts/release_check.py
```

Record the exact repository commit, Python version, command output, and any failure. Do not infer that these checks passed merely from this document; run them on the checked-out version. Software validation is not epigraphic acceptance.

## Corpus-specific evidence boundaries

The archive contains alternative readings of the same inscriptions; do not count them as independent witnesses. The current analytical admission remains zero rows/tokens. Keep Praisos and Dreros source claims distinct; do not admit disputed Arkalochori or Azoria material as certified Eteocretan text.

## AI research contract

Read [the individual AI skill](../ai-skill/SKILL.md), [rights-only readiness](RIGHTS-ONLY-READINESS.md), and [residual blocker ledger](../research/residual-blocker-ledger.json). Check `ai-skill/generated/source-state.json` for the commit represented by any generated AI bundle. Canonical records take precedence over generated summaries. Preserve source attribution, disagreements, uncertainty, negative evidence, exclusions, and record-specific rights. Cross-corpus comparisons require explicit comparability and witness-independence checks; shared fleet membership is not linguistic evidence.

## Human-review boundary

Treat source collation, physical object identification, language classification, and independent specialist adjudication as separate gates. Never mark an unreviewed transcription as expert-accepted or manufacture an attestation. Maintain a traceable link from any proposed correction to its source and reviewer.
