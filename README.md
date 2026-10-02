# Eteocretan source and reading archive

**1.0.0 — an attributed reference archive with explicit coverage limits.**

This project preserves Eteocretan source readings and disagreements for
inspection, comparison and future collation. It does not offer a decipherment,
a settled modern critical edition, or an exhaustive corpus.

| Measure | Snapshot |
|---|---:|
| Named inscriptions with reading versions | 8 |
| Attributed reading versions | 12 |
| Historical primary-edition versions | 4, concerning Praisos 1–3 |
| Separately excluded secondary versions | 8 |
| Source text rows across all versions | 101 |
| Coverage-register entries | 11, including one collection-level lead |
| Analytically admitted rows / tokens | 0 / 0 |

The historical layer encodes Conway's printed Praisos readings, including
both conservative and probable readings of Praisos 2. The secondary layer
preserves a licensed Wikipedia transcription reference for Dreros 1–2 and
Praisos 1–6. These are versions of existing inscriptions, not independent
witnesses. Their disagreements remain visible. Uncertainty, injury and
unreviewed transcription prevent frequency admission in this first release.
The zero count is an explicit scientific gate, not an empty source archive.

Dreros primary editions and later Praisos critical editions remain source
leads. The [coverage register](research/coverage-register.json) also retains
Psychro's disputed authenticity, Arkalochori's disputed script assignment,
and the Azoria collection lead. Arkalochori is not assigned to Eteocretan.

Download [the 1.0.0 ZIP](https://github.com/hawkinsnick/Eteocretan/releases/tag/v1.0.0)
and unzip it. Python 3.10+ runs the tools without extra packages or a network
connection. Open a terminal in the extracted folder:

```bash
python -m corpuskit validate
python -m corpuskit audit
python -m corpuskit search 'isaluria'
python -m corpuskit search 'barxe'
python -m corpuskit frequency --language ecr
python -m corpuskit verify-export exports
python scripts/release_check.py
```

Use [the reading JSON](exports/corpus.json), [JSONL](exports/corpus.jsonl),
[line CSV](exports/lines.csv) and [audit](exports/audit.json). Original source
page evidence and the secondary HTML snapshot are included in `data`.
Object IDs group alternatives while record IDs distinguish reading versions.
Search includes excluded material and clearly reports its eligibility.

Read [the method](docs/METHOD.md), [researcher workflow](docs/RESEARCHER_WORKFLOW.md),
[coverage policy](docs/COVERAGE.md), [source credits](NOTICE), and
[family links](research/family/README.md). Data and documentation are
CC BY-SA 4.0; code is MIT. Public-domain originals retain that status.

Here 1.0 means a tested and reproducible attributed archive. Independent
collation, critical source reconciliation and full discovery coverage remain
separate gates. The next work should strengthen those gates rather than
inflate the number of admitted readings.
