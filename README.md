# Eteocretan source and reading archive


## AI research skill

This corpus project includes a vendor-neutral, evidence-first AI research skill in [`ai-skill/`](ai-skill/). The corpus remains the scholarly source of truth; the skill is an interface, not a second corpus or independent authority.

Researchers can give a capable AI this repository or its AI-ready bundle together with [`ai-skill/SKILL.md`](ai-skill/SKILL.md). The skill preserves provenance, uncertainty, exclusions, source dependence, rights and this project's scientific gates. Check [`ai-skill/generated/source-state.json`](ai-skill/generated/source-state.json) and the generated research-bundle index before substantive use.

For questions spanning corpus projects, use the **Combined Corpus Research AI** in [`combined-ai-skill/`](https://github.com/hawkinsnick/Linear-A/tree/ai-skill-v0.1/combined-ai-skill). It orchestrates registered individual skills without merging their evidence. Membership does not imply linguistic relationship, sign equivalence, chronology, decipherment or independent replication.

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
[family links](research/family/README.md). Project-original software is PolyForm Noncommercial 1.0.0 and project-owned content/documentation is CC BY-NC 4.0. Third-party CC BY-SA material retains CC BY-SA; public-domain originals retain that status. See the component-specific licensing files and NOTICE.

Here 1.0 means a tested and reproducible attributed archive. Independent
collation, critical source reconciliation and full discovery coverage remain
separate gates. The next work should strengthen those gates rather than
inflate the number of admitted readings.

## Source reconciliation checkpoint

See [the 4 October 2026 evidence checkpoint](docs/SOURCE-RECONCILIATION.md) for new source-located evidence, reproducible checks, unresolved anomalies and the remaining primary-source work.
