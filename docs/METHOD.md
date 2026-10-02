# Method and admission boundaries

Every reading is attributed to a source, and every source has a reproducible
locator and checksum. Original source snapshots are preserved. Derived records
replay offline; a checksum demonstrates byte integrity, not correctness of an
ancient reading. Unknown physical-object counts remain null.

The JSON line order preserves the source response or printed reading order;
line labels are retained without renumbering physical lines. A source row may
be a comment, header, joined line group, or alphabetic parallel. JSON, JSONL
and CSV exports preserve the same text and source locators. Raw source files
in `data/raw` and page evidence in `data/source-evidence` remain available
in the repository and release archive.

Frequency is explicitly the count of *whole unmarked source strings*, not
phonemes, native glyphs, reconstructed words, or independently verified
readings. Spelling, case and Unicode composition remain unchanged. Source
clitic strings containing `=` count once. Whitespace, `:` and `|` delimit
source strings; this does not assert an ancient word boundary. Damage,
restoration brackets, uncertainty marks, underdots, unexplained glyphs and
editorial numerals block the whole affected string; missing letters are never
silently stripped and fragments are never joined across gaps.

Native family reports retain their own units and acceptance gates. Their
snapshots are pinned by commit and hash. Research and geographic links create
zero independent witnesses and imply neither language identity nor a mapping
between signs. No training/evaluation split or decipherment benchmark is
claimed. A language partition must be selected for frequency; there is no
pooled cross-language frequency command.

## Historical and secondary reading versions

Four versions derive from public-domain historical pages: Praisos 1,
Praisos 2 reading (i), Praisos 2 reading (ii), and Praisos 3. They are project
encodings of those printed versions, not new observations of the inscriptions.
The attached scan is authoritative for typography, underlining, supra-linear
alternatives and sign shapes. The project text uses normal Unicode Greek
phi and capital Greek letterforms and [trace] for partial strokes. Spacing
and dot runs are normalized; the text is therefore not called lossless
facsimile transcription. The full original PDF URL, page and SHA-256 are
retained. CSV/JSON roundtrip is lossless with respect to the *project's saved
text*, not the typography of the original stone or publication.

Praisos 1's historical source presents lines 1–2 and 3–4 as joined line
pairs, then line 5. These are retained as line groups. They are not silently
renumbered into three physical lines. Praisos 3's printed p. 117 form has
editorial corrections and disagreements discussed later in the same article;
no later consensus is inferred here. The article's session date 1903–1904
and its 1905 written/addendum dates remain distinct.

All historical lines carry conservative uncertainty flags. No line or
string from this unreviewed encoding is admitted to frequency in 1.0.
Conway's hypothetical linguistic interpretation and reconstructed sound
values are not imported as established facts. The reading (ii) version is
an alternative for the same Praisos 2 object, not additional evidence.

Eight secondary versions are extracted from exact HTML element IDs in a
pinned Spanish Wikipedia revision. Their strings replay from the saved
HTML, but that proves copying integrity only. The Dreros Greek portions
are explicitly separated as source-attributed parallel components; no Greek
text contributes Eteocretan counts. Damaged fragments, vacat labels, and
secondary transliteration discrepancies are retained without correction.
The secondary reference layer is useful for source discovery and comparisons,
not a substitute for the primary editions.

The coverage register is explicitly incomplete. It contains eight named
inscriptions, two disputed objects and one collection-level lead. Eleven
register entries do not mean eleven Eteocretan inscriptions. New Azoria
material must be reconciled item by item before counting physical objects.
