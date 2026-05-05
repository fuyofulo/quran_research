# Notes index

All research notes from the Quran first-principles study. Each major investigation lives in its own folder. Notes are written by Claude (the LLM), informed by deterministic concept profiles in `data/concepts/`. Always treat notes as one reading; the JSON data is the audit trail.

## Investigations

Each folder collects everything from one research thread — per-root deep-reads, cross-cutting investigations, the synthesis, and a folder README that explains the topic and indexes the files.

### [`mercy/`](mercy/) — Mercy / Wombs (ر-ح-م)
The first concept analyzed. Proof-of-workflow for the root-anchored knowledge graph approach. Headline finding: divine mercy in the Quran is etymologically the same root as the maternal womb.
- Main file: [`mercy/concept-rhm.md`](mercy/concept-rhm.md)
- 1 file · 339 occurrences analyzed

### [`cognition/`](cognition/) — Research / Inquiry / Cognition
Multi-phase, multi-agent investigation. Started from "how does the Quran represent research?" — discovered the Quran has no single word for it, instead a constellation of 14 cognitive roots. Mapped the constellation, then traced four cross-cutting structural patterns (heart-locus epistemology, institutional vocabulary gap, God-human cognitive mirror, negative space).
- **Start here:** [`cognition/README.md`](cognition/README.md) (folder index)
- **Synthesis:** [`cognition/concept-research-deep.md`](cognition/concept-research-deep.md)
- 22 files · 15 roots + 5 cross-cutting investigations + 2 synthesis files

### [`full-quran-graph/`](full-quran-graph/) — Semantic graph of all 1,642 roots
Louvain clustering of co-occurrence across the entire Quran. 666 clusters detected; the 15 largest were thematically analyzed by parallel agents. Each cluster names a real semantic territory of the Quran (revelation/disbelief, allegiance/worship, believer's reward, family law, ritual purity, jihad/sabīl Allāh, dunya/ākhirah, sin/mercy economy, eschatological punishment, divine will/dominion, creation/lifecycle, vegetative signs, sea-rescue, visible sign-witnessing, commanded self).
- **Start here:** [`full-quran-graph/README.md`](full-quran-graph/README.md) (master index)
- **Interactive graph:** open [`full-quran-graph/index.html`](full-quran-graph/index.html) in any browser
- 19 files · 15 cluster analyses + interactive viz + raw data + clusters.json

### [`structural/`](structural/) — Structural analyses across the corpus
5 computational analyses covering all 6,236 ayahs and 1,642 roots: per-surah cluster signatures, translation divergence map, cross-cluster bridge roots, ayah echoes/refrains, comprehensive per-root reference. These are research instruments — they surface sorted lists of "things worth investigating" rather than narrative findings.
- **Start here:** [`structural/README.md`](structural/README.md)
- 5 markdown analyses + JSON/CSV data files in `data/structural/`

### [`time/`](time/) — Time in the Quran (the largest investigation)
22 root deep-reads + 7 cross-cutting research files + 5 rabbit-hole investigations + 2 structural pre-cuts + integrated synthesis. The most extensive concept investigation in the project (~159,000 words across 36 files). Used an explicit 4-phase pipeline (root deep-reads → cross-cutting synthesis → rabbit holes → grand synthesis), 35+ parallel agents, and structural data anchors. Headline findings: lexical apartheid between divine and creature time; tripartite grammar of appointment (Ajl=endpoint, wqt=instant, Amd=stretch); cyclical and linear time coexist without merger; the Quran has no year-as-bridge between months and generations; the binary temporal grammar lacks "during"; ~22 hapax day-names form an affect-catalog; the 14-verse "illā mā shāʾa" exception architecture brackets even eternity.
- **Start here:** [`time/README.md`](time/README.md) (folder index)
- **Synthesis:** [`time/concept-time-deep.md`](time/concept-time-deep.md)
- 36 files · 22 roots + 7 cross-cutting + 5 rabbit-holes + 2 structural + 1 synthesis

### [`afterlife/`](afterlife/) — Death, Resurrection, and the Day of Judgement (the largest investigation)
The most extensive single investigation in the project. Maps the Quran's full vocabulary and narrative architecture of the afterlife: death + soul-taking + barzakh; the Hour-event chronology; the judgment process (reckoning, scales, records, intercession); paradise and hell as mirror-inverted sensory worlds; the classes on that Day; the resurrection-phenomenology; the wajh on that Day; the ḥūr/wildān question; the hidden-exceeds-described reward (32:17); the al-Aʿrāf borderline-case. Used the optimized 4-phase pipeline at MAXIMUM scope with Phase 3 EXECUTED (~38 roots covered, 26 files, ~2M tokens — still 50% off the pre-optimization baseline despite being the largest scope).

Headline findings: the Quran's eschatology is FORENSIC + SENSORY + MERCY-WEIGHTED + WITHHOLDING; nothing is unwitnessed (7-layer witness system culminating in skin/limbs testifying against the person at 41:19-23); paradise and hell are STRUCTURALLY MIRROR-INVERTED but the mirror BREAKS asymmetrically toward mercy at every architectural seam (multiplication-vs-intensification, fixed-vs-bracketed eternity, familial-vs-isolated, present-vs-veiled); judgment follows a 4-step procedural template (light → record → witnesses → verdict at 39:69) with multi-layered evidence; the dual-track justice + mercy operates simultaneously (gfr is the largest single root in the cluster at 234 occurrences, dominating); the 14-phase phenomenological arc from death to final abode is reconstructible from cross-verse evidence; bodies are RESURRECTED with their pleasures or pains intact (Quran rejects bodily-despising dualism); the described paradise is a LOWER BOUND — the actual reward exceeds what any soul knows (32:17); intercession exists but is triple-locked (permission + recipient-approved + covenant-bearing intercessor); the al-Aʿrāf borderline-case ends in mercy (7:49) — the Quran refuses stark binary outcomes for ambiguous cases.
- **Start here:** [`afterlife/README.md`](afterlife/README.md)
- **Synthesis:** [`afterlife/concept-afterlife-deep.md`](afterlife/concept-afterlife-deep.md)
- 26 files · 8 root + 7 narrative + 4 cross-cutting + 4 rabbit-holes + 1 structural + 1 synthesis + 1 README

### [`failure/`](failure/) — Failure in the Quran (broad scope, second optimized investigation)
Companion to the success investigation. Maps the Quran's full vocabulary and narrative archetypes of failure across 32 roots and ~13 narrative passages. Used the optimized 4-phase pipeline at BROAD scope to test how the optimization scales: 16 files vs ~30+ in pre-optimization investigations; 14 agents vs ~30; ~1.23M tokens vs ~3-5M baseline (~70% reduction maintained at broader scope, only 45% more than the medium-scope success investigation despite covering 3x the roots). Headline findings: failure is REFUSAL (not incompetence/ignorance/bad luck) — the human's persistent self-defending response to a divine reminder that has arrived; the IBLĪS-ADAM master binary classifies all failure (response, not content — same act yields opposite classification by whether the actor admits or defends); the 6-stage failure-arc (jhl/gfl → ErD → Dll → kbr/kfr/$rk → qsw/xtm → Tgy/bgy/fsd → hlk/xsr); heart-disablement is divine PROCEDURAL response to persistent refusal (qsw/xtm/qfl/mrD/glf/knn always follow human resistance); failure-mode matches destruction-means (Pharaoh→sea, Qārūn→earth, ʿĀd→wind, Lūṭ→inversion); the grammatical theology: God ACTS (active voice), humans EXPERIENCE consequences (passive) — mirror of success-as-given.
- **Start here:** [`failure/README.md`](failure/README.md)
- **Synthesis:** [`failure/concept-failure-deep.md`](failure/concept-failure-deep.md)
- 16 files · 6 root + 4 narrative + 3 cross-cutting + 1 structural + 1 synthesis + 1 README

### [`success/`](success/) — Success in the Quran (the cost-optimized investigation)
First investigation run on the optimized pipeline (`notes/research-optimization-plan.md`). Topic: who are the successful (al-muflihūn / al-muttaqūn / al-abrār), what habits and routines define them, what is the heart-condition of those who succeed, and how the success/loss binary is structured. 11 files vs ~30 in prior investigations; 9 agents vs ~30; ~845k tokens vs ~3-5M baseline (~75% cost reduction). Quality held — every Phase-1+2 agent under hard cap; cross-confirmation rate maintained. Headline findings: success in the Quran is ESCAPE FROM A DEFAULT-LOSS, not positive achievement (surahs 103, 70, 91 share the *illā*-architecture); orientation-not-capability theology (no intelligence, courage, or leadership in believer-lists); the irreducible core is prayer + purification (the believer-lists' structural skeleton); the three-vocabulary partition (naṣr=conflict, fawz=eschatological, falāḥ=dispositional); success is GIVEN by God but only to those who reached for it (24:21 + 13:11 + 7:43 cooperation paradox); the integrated class hierarchy (ṣāliḥūn ⊃ muttaqūn ⊃ abrār + 4:69's nabiyyīn → ṣiddīqīn → shuhadāʾ → ṣāliḥīn + 56:7-14's sābiqūn / yamīn / mashʾama).
- **Start here:** [`success/README.md`](success/README.md)
- **Synthesis:** [`success/concept-success-deep.md`](success/concept-success-deep.md)
- 11 files · 4 root + 2 narrative + 1 structural + 2 cross-cutting + 1 synthesis + 1 README

### [`teleportation/`](teleportation/) — Teleportation in the Quran
First THEMATIC (non-root-anchored) investigation. The Quran has no single word for teleportation; instead a constellation of 16 roots + 13+ narratives spanning Solomon's throne (27:38-40), the Night Journey (17:1), Idrīs and Jesus's vertical raisings, Abraham's four birds (2:260), the Cave Sleepers (Surah 18), the man revived after 100 years (2:259), Maryam's mobility set, the Hour, the Trumpet, angelic descent, jinn flight, and soul-extraction. Used the 4-phase pipeline extended with NARRATIVE agents (a new agent-class for thematic investigations). 30 files, ~150,000 words. Headline findings: the vertical-horizontal lexical apartheid (rfE/Erj never co-occur with sry); the Isrāʾ-Miʿrāj fusion is hadith elaboration not Quranic text; the Quran reports JUXTAPOSITION not TRAJECTORY (mechanism-silence as apophatic causation); the 5-phase withdrawal-miracle template recurs across Cave Sleepers, Maryam, Noah, Lot, Moses; the graduated speed-ladder from hoopoe (animal) to *kun fa-yakūn* (creation-fast) calibrates speed by epistemic access to divine inscription; the 27:40 "before your gaze returns" outpaces the ʿifrīt's "before you rise" by an order of magnitude — knowledge-of-the-Book outpaces strength.
- **Start here:** [`teleportation/README.md`](teleportation/README.md) (folder index)
- **Synthesis:** [`teleportation/concept-teleportation-deep.md`](teleportation/concept-teleportation-deep.md)
- 30 files · 16 roots + 7 narratives + 4 cross-cutting + 2 structural + 1 synthesis

## Cross-investigation files (top-level)

These span all investigations and live at the top of `notes/`.

- [`methodology-log.md`](methodology-log.md) — captures HOW each analysis was done. Approach order, data-grounded vs interpretive claims, decisive moves, patterns reinforced or newly observed. The eventual goal is a stable system prompt for autonomous Quran research.

## Conventions for new investigations

When starting a new research thread, create a folder `notes/<topic>/` with:
- A `README.md` that explains the topic and indexes the files inside
- One `concept-<root>.md` file per root analyzed (this is mandatory — see methodology memory)
- One `research-<subtopic>.md` file per cross-cutting investigation
- A synthesis file (often `concept-<topic>-deep.md` or similar) that links to all per-root and cross-cutting files

Add an entry to this top-level README pointing at the new folder, and append an entry to `methodology-log.md` capturing the approach.

## Key files outside notes/

- `/data/concepts/<root>.json` — deterministic structured profile per root. Always the audit trail for these analyses.
- `/data/morphology/{words.jsonl, roots.json, lemmas.json, segments.jsonl}` — the QAC morphology layer (77,429 words tagged with root, lemma, POS).
- `/data/morphology/pos_legend.json` — Arabic POS names for all 33 QAC tags + classical 3-way category (ism / fiʿl / ḥarf).
- `/data/translations/{saheeh,pickthall,khattab,arberry,word-by-word}.json` — strictly-secondary annotation layer.
- `/data/arabic/quran.json` — canonical Arabic text (Uthmani Hafs) with surah metadata.
- `/scripts/build_concept.py` — generates a concept JSON for any root.
