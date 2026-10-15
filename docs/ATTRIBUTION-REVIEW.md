# Attribution review

All five controls; Duhoux-derived classification remains indirect, Conway versions remain a lineage, and Lejeune’s Dreros discussion depends on the earlier editor.

Existing source consultation receipts and limits are inherited exactly from the referenced native packets. This pass inspects those packets, not the underlying publications afresh. No exhaustive literature search, new autopsy or independent review is claimed.

The complete selections below name the finite native collections reviewed. Other repository records and the broader literature are outside this checkpoint. Case counts are review tasks, not inscriptions, independent witnesses or fully attributed alternative pairs.

| Complete native selection | Rows |
|---|---:|
| `research/disagreement-register.json/items` | 5 |

Use the case query to read the finding together with the complete native evidence, including any named author/publication, source locator, inspection state, qualification and source dependence. Missing metadata stays missing; a source ID alone is not proof of direct consultation.

```sh
python scripts/attribution_review.py --check
python scripts/attribution_review.py --case 'ECR-DIS-001'
python scripts/evidence_query.py --list attribution-review
```

| Review ID | Type | Finding | Remaining work |
|---|---|---|---|
| ECR-DIS-001 | CLASSIFICATION | Project uncertainty and the Duhoux-derived language claim are different assertion voices; the latter is not a directly collated Duhoux page. | Lawful direct critical-source inspection or qualified expert assessment is still needed. |
| ECR-DIS-002 | COVERAGE_GAP | Historical Conway versions exist; the later critical-edition side is not directly collated. Version count is not witness independence. | Collate exact loci in the critical edition; retain alternative presentations within the Conway lineage. |
| ECR-DIS-003 | READING_COMPARISON | The Lejeune packet identifies near-primary Dreros1 ambiguities and its van Effenterre1946 dependence. It does not complete Dreros2 or certify original facsimile readings. | Compare the original edition/facsimile and exact secondary loci; keep nu/mu/u and punctuation ambiguities attributed. |
| ECR-DIS-004 | CLASSIFICATION | Psychro authenticity remains a quarantined competing-claim question; no source-specific paired argument is encoded here. | Identify the actual publications, loci and object evidence for each authenticity claim. |
| ECR-DIS-005 | CLASSIFICATION | HM X2416 is a disputed-script candidate, not an admitted Eteocretan inscription. | Establish source-specific script arguments and admissible object evidence before admission. |

`research/attribution-review.json` pins every referenced native artifact by SHA-256 and records exact JSON pointers. `analysis/attribution-review-audit.json` is replayed by the checker. Queries reject changed input bytes before returning any case. The earlier native records remain unchanged.

Pair-attribution states describe documentary limitations, not scientific acceptance. A partial located comparison can be a real scholarly alternative without full typographic, physical-position or independent collation. `NOT_APPLICABLE` marks controls and interpretations for which a two-reading pair is not the appropriate unit. No unknown pair/witness total is replaced with zero.
