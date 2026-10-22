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

### [`finance/`](finance/) — Money, wealth, and economic ethics (maximum scope, Phase 3 executed)
The Quran's full financial doctrine: riba, zakat, sadaqah, infaq, inheritance, debt contracts, fair-measure, ownership, hoarding, spoils, theft. 8 root-clusters covering ~37 finance roots, 7 narrative passages (riba arc, Baqarah 282, inheritance verses, Qarun, Madyan/Shu'ayb, Solomon, Anfal/Hashr), 4 cross-cutting essays, 4 rabbit holes, 1 structural pre-cut, integrated synthesis. Used the optimized 4-phase pipeline at MAX scope with Phase 3 executed (25 files, ~1.5M tokens — ~50% off pre-optimization baseline despite covering the most extensive financial vocabulary).

Headline findings: the Quran does NOT legislate an economy — it legislates the human relationship to wealth that passes through their hands; the double-grammar of ownership (mwl=human handling / rzq=divine provision) resolves as STEWARDSHIP under fiduciary tenancy [57:7]; the give-vocabulary is nested (qarḍ ḥasan ⊂ zakāt ⊂ ṣadaqa ⊂ infāq) with NO specified rate anywhere; riba is uniquely escalated to "war from Allah" [2:279] because it forges the divine shape of increase to extract from the distressed (the rbw root carries BOTH "natural growth" and "interest" senses — 30:39 deploys both in one verse); the justice machinery is built from ONE principle (qisṭ), ONE symbol (mīzān), ONE mechanism (witnessing), ONE document (writing), ONE diagnostic case (the orphan) and ONE enforcement (the Day of Reckoning) — NO state, NO court, NO inspector; the dūla principle [59:7] states the supreme distributive intent — wealth must not become a closed rotation among the wealthy; Qarun and Solomon are the paradigm pair — same wealth, opposite orientations (active self-attribution "ʿilm ʿindī" vs passive divine bestowal "hādhā min faḍli rabbī"), opposite ends; the architecture is conscience-not-enforcement and REQUIRES belief in divine accounting to function — the negative space (no rate, no ceiling, no enforcement) IS the design.
- **Start here:** [`finance/README.md`](finance/README.md)
- **Synthesis:** [`finance/concept-finance-deep.md`](finance/concept-finance-deep.md)
- 25 files · 8 root + 7 narrative + 4 cross-cutting + 4 rabbit-holes + 2 structural + 1 synthesis + 1 README

### [`teleportation/`](teleportation/) — Teleportation in the Quran
First THEMATIC (non-root-anchored) investigation. The Quran has no single word for teleportation; instead a constellation of 16 roots + 13+ narratives spanning Solomon's throne (27:38-40), the Night Journey (17:1), Idrīs and Jesus's vertical raisings, Abraham's four birds (2:260), the Cave Sleepers (Surah 18), the man revived after 100 years (2:259), Maryam's mobility set, the Hour, the Trumpet, angelic descent, jinn flight, and soul-extraction. Used the 4-phase pipeline extended with NARRATIVE agents (a new agent-class for thematic investigations). 30 files, ~150,000 words. Headline findings: the vertical-horizontal lexical apartheid (rfE/Erj never co-occur with sry); the Isrāʾ-Miʿrāj fusion is hadith elaboration not Quranic text; the Quran reports JUXTAPOSITION not TRAJECTORY (mechanism-silence as apophatic causation); the 5-phase withdrawal-miracle template recurs across Cave Sleepers, Maryam, Noah, Lot, Moses; the graduated speed-ladder from hoopoe (animal) to *kun fa-yakūn* (creation-fast) calibrates speed by epistemic access to divine inscription; the 27:40 "before your gaze returns" outpaces the ʿifrīt's "before you rise" by an order of magnitude — knowledge-of-the-Book outpaces strength.
- **Start here:** [`teleportation/README.md`](teleportation/README.md) (folder index)
- **Synthesis:** [`teleportation/concept-teleportation-deep.md`](teleportation/concept-teleportation-deep.md)
- 30 files · 16 roots + 7 narratives + 4 cross-cutting + 2 structural + 1 synthesis

### [`fasting/`](fasting/) — Fasting (ṣawm) — the first APPLIED investigation
Commissioned with a practical question rather than a scholarly one: *I fasted seven days to get closer to Allah and it didn't work — what does the Quran actually say fasting is for, what does science say it does, and what have people actually experienced?* This is the first investigation to combine the Quranic pipeline with an **external-evidence track** (peer-reviewed physiology and psychology; several hundred sourced first-person accounts) and to end in a **practice guide** rather than a synthesis alone. Three evidence streams were researched by agents that never read each other's work, then compared for convergence.

The corpus is astonishingly small: **`Swm` occurs 14 times in the entire Quran**, in 11 ayahs. Only 5 concern Ramadan; 6 sit in expiation/substitution ladders where fasting is the fallback for someone who cannot free a person or feed the poor. 13 of 14 are Medinan — the single Meccan occurrence, 19:26, is Maryam's fast **of speech**, in a verse that commands her to eat and drink.

Headline findings: the Quran legislates the **emptying** with precision and specifies almost nothing to put in it (four of the five imperatives in 2:183–187 are permissions to eat, drink and be with your spouse); **hunger never appears in a fasting verse** and is uniformly negative across all 5 of its Quranic occurrences; **no reward is promised for fasting anywhere**, and the intention-root `nwy` does not occur in the Quran at all; **`Swm` and `Slw` share zero ayahs in the whole corpus** — fasting and prayer are never put in the same verse; 2:177's definition of the *muttaqūn* omits fasting entirely, and surahs 97 and 44 describe the night the month exists for without mentioning fasting; the purpose-clause `laʿalla…tattaqūn` occurs 12 times and **9 of the 12 attach taqwā to received-and-retained divine speech**, not to any physical act; the formula *li-tukabbirū Allāha ʿalā mā hadākum* occurs in exactly **two** places — 2:185 (the fasting verse) and 22:37 (*"their flesh does not reach Allah, nor their blood, but the taqwā from you reaches Him"*), licensing the transfer: **the hunger is the fast's flesh and blood, the part that does not travel**; 57:27 disowns monasticism with `mā katabnāhā` — the *same lemma* 2:183 uses to prescribe the fast; and of the 16 verses putting a question to the Prophet, 13 are answered with `qul` — the exceptions include **2:186**, the one verse that says *I am near*, where God answers in the first person with no intermediary, stating His side in the indicative (already happening) and ours in the jussive (**outstanding**).
- **Start here:** [`fasting/README.md`](fasting/README.md) (folder index)
- **The deliverable:** [`fasting/practice-guide.md`](fasting/practice-guide.md) — the applied output
- **Synthesis:** [`fasting/concept-fasting-deep.md`](fasting/concept-fasting-deep.md)
- 15 files · 5 roots + 2 narratives + 2 cross-cutting + 1 structural + 4 external + 1 synthesis + 1 practice guide

### [`tahajjud/`](tahajjud/) — Tahajjud and the Quranic night (the first PAIRED investigation)
Run immediately after `fasting/` and designed from the outset to be compared against it — the fasting corpus was the control, and the comparison was a named deliverable rather than an incidental cross-reference. Commissioned with: *"when it comes to fasting and tahajjud I think tahajjud is extremely hard. I just want to learn more about tahajjud and how it is different from fasting according to the Quran."* MAX scope with Phase 3 executed: 6 root files, 4 narratives, 4 cross-cutting essays, 3 rabbit holes, structural pre-cut, synthesis. 19 files, ~39,300 words, ~19 agents.

**The corpus is the exact inverse of fasting's.** `hjd` — the word "tahajjud" — occurs **exactly once in the entire Quran** (17:79), against a night vocabulary in the hundreds (`*kr` 292, `dEw` 212, `Slw` 99, `lyl` 92, `sbH` 92, `sjd` 92). Fasting is a *named institution with thin content*; night-worship is an *unnamed practice with thick content*.

Headline findings: **every night-worship imperative in the Quran is second-person masculine SINGULAR and addressed to the Prophet** (73:2, 17:79, 20:130, 50:40, 52:49, 76:26) while every fasting imperative is PLURAL — there is no plural night-standing command anywhere, and the three portraits (25:64, 51:17, 32:16) are third-person reports, not instructions; when the Quran addresses a plural "you" about the night it says the night was made for you to **rest** in, never to stand in it; the night's characteristic verb is **`sabbiḥ` (glorify), not `ṣalli`** — 10.3% night-attached against ṣalāh's 3.3%, and the `wa-mina al-layli fa-` + imperative template occurs 4× with three saying *glorify* and one *tahajjad* (the same partitive construction commands Lot to flee); **only 18.5% of the 81 `layl` verses are devotional** (43.2% are cosmological); **sleep is never condemned** — it is a sign (30:23), a repose God made (25:47), a battlefield mercy (8:11), and `tawaffā`, the verb for taking a soul in death, is used unmodified for it (39:42, 6:60), so the two practices suspend things with **opposite standing in the text**; the Quran's three stated reasons for the night are practical, not mystical (a heavy word is coming 73:5, speech lands straighter 73:6, the day is full 73:7) and 73:6's comparative is **elliptical** — it never says what the night-rising is stronger *than*; the night is never called blessed as a time of day, God is never said to be nearer at night, and **no verse ranks night prayer above prayer at another hour**; **73:20 is the only devotional walk-back in the Quran** and its stated ground is `lan tuḥṣūhu` — *you cannot keep count* — a clause-shape occurring only twice elsewhere, both of God's uncountable favours, while the Quran's actual lightening verb `khaffafa` (which names weakness in both its community uses) is pointedly never used in Sūrah 73; and **no felt state attaches to the vigil anywhere** — whenever the text moves from night-worship to reward the grammatical subject changes underneath it (25:64 → paid `bimā ṣabarū`; 32:16 → paid to "those who believed and did righteous deeds"; 51:17 → grounded in `kānū muḥsinīn`), so the vigil is evidence of the category, never the stated ground of payment.
- **Start here:** [`tahajjud/README.md`](tahajjud/README.md) (folder index)
- **The comparison:** [`tahajjud/2-cross-cutting/research-tahajjud-vs-fasting.md`](tahajjud/2-cross-cutting/research-tahajjud-vs-fasting.md)
- **Synthesis:** [`tahajjud/concept-tahajjud-deep.md`](tahajjud/concept-tahajjud-deep.md)
- 19 files · 6 root + 4 narrative + 4 cross-cutting + 3 rabbit-holes + 1 structural + 1 synthesis + 1 README

### [`cosmos/`](cosmos/) — Life beyond earth: does the Quran say humans exist elsewhere?
Commissioned by a direct question: *"Do humans exist outside of Earth? Does the Quran even talk about it?"* — prompted by having heard a scholar claim there are **seven or eight earth-like planets where humans reside**. The investigation answers the question and traces the claim. 12 files, ~24,500 words, 8 agents.

**The question splits in two and the halves get opposite answers.** Life beyond earth is **affirmed**; humans beyond earth appear **nowhere**.

Headline findings: **thirteen verses use `man`** — Arabic's rational-being relative pronoun — for "whoever is in the heavens" (3:83, 10:66, 13:15, 17:55, 19:93, 21:19, 22:18, 24:41, 27:65, 27:87, 30:26, 39:68, 55:29; 67:16-17 excluded, they refer to God), against 39 ayahs using `mā` for things — and those beings prostrate, glorify, ask Him, do not know the unseen, are terrified at the Trumpet, and fall dead at the blast; **42:29 is the only verse placing `dābba` (moving creatures) in the heavens**, on a dual pronoun `fīhimā` verified in the morphology, where the three parallel dispersal verses (2:164, 31:10, 45:4) all use the singular for the earth alone; at lemma level **`dābba` is the most heaven-attached being-word** (27.8%) — 3.4× the angel-word and twelve times the human-word. The angels-only reading of the thirteen was **stress-tested rather than assumed** and absorbs twelve of them, each with a closing verse (2:32 for ignorance of the unseen, 21:28/13:13/16:50 for fear, 40:7/42:5 for petition) — but **it does not absorb 39:68**, because across all six angel+death ayahs the angel is death's agent and never its patient: **no verse in the Quran says an angel dies.** Verdict: underdetermination, not contradiction.

On the other side the ledger is flat: **`arḍ` occurs 461 times and is never pluralised** — the grammatical machinery for "multiple earths" does not exist in the text; **zero of the 19 genuine human+heaven ayahs place a human in the heavens**; and the anthropology closes on itself at 20:55 — made from the earth, returned to it, raised from it. **"Seven earths with people on them" is a three-layer stack** — an ambiguous pronoun in 65:12 (`mithlahunna`, which never repeats "seven" and mentions no inhabitant), a weak report, and the 2017 TRAPPIST-1 discovery retrofitted — none of whose layers is the Quranic text. That makes the claim **unsupported, not false**, and the file keeps those apart.

Also established: the Quran affirms **exactly two** non-human rational species (jinn and angels; no third survives checking), and the **jinn are barred from the heavens rather than resident** (72:8-9, 15:16-18, 37:6-10); **55:33 is a taunt inside a judgment scene**, not a space-travel prophecy — `sulṭān` means *warrant* in the clear majority of its 39 occurrences and no translator renders it "power" there, and `tanfudhū` occurs only in that verse; **there is no astronomy** — `falak` occurs twice against 23 occurrences of the same root meaning *ship*, no word for planet/universe/galaxy, all five `kawkab` denoting a light rather than a world; and the Quran is **geocentric in vantage but not in doctrine** — a sky that is a roof and an earth that is a bed, with no word for centre, axis, or revolution-about-something, which is why it has no geocentrism to defend and no heliocentrism to be credited with.
- **Start here:** [`cosmos/README.md`](cosmos/README.md) (folder index)
- **The answer:** [`cosmos/2-cross-cutting/research-is-there-life-beyond-earth.md`](cosmos/2-cross-cutting/research-is-there-life-beyond-earth.md)
- **The claim traced:** [`cosmos/1-narratives/narrative-65-12-seven-earths-claim.md`](cosmos/1-narratives/narrative-65-12-seven-earths-claim.md)
- **Synthesis:** [`cosmos/concept-cosmos-deep.md`](cosmos/concept-cosmos-deep.md)
- 12 files · 4 root + 2 narrative + 2 cross-cutting + 1 structural + 1 synthesis + 1 README + brief

### [`regret/`](regret/) — What the Quran says people will regret, and what leads there
Commissioned as an open, collaborative question: *"What are the things the Quran mentions humans will regret, in this life and the hereafter? If we list them, we can reverse-engineer what actions and what feelings lead to them, so I can introspect."* The first investigation whose main deliverable is a **self-examination instrument**, and the first explicitly framed as a first pass to be continued with the commissioner. 13 files, ~28,900 words, 9 agents.

**56 ayahs show people regretting their own conduct — 34 in the hereafter, 10 at death or as punishment arrives, 12 in this life** — in 49 scenes, sorted by *what* is regretted: the warning not heard (12), the whole conduct unnamed (10), whom one followed (6), wishing not to exist (6), what one neglected toward God (5), wealth trusted or withheld from the poor (5), associating others with God (4), crimes against kin (4), one rash act against others (2), bare recognition at the record (2) — plus 3 regrets the Quran depicts as **aimed at the wrong thing** (a missed gain 4:73, another's fortune 28:79, the "if only" of fate 3:156).

Headline findings: **the Quran never commands regret** — `ndm` has 7 nouns and no verb, regret-`ḥasra` 9 nouns and no verb, no prophet is ever called `nādim` — **but commands return**: `tūbū` 7×, the `istaghfir-` imperative for one's own sins 13×; none of the 12 converting cases (Adam, Moses, Yūnus, David, Noah, the calf, Joseph's brothers, the three left behind 9:118, the garden-people 68:29-32 …) uses a regret word at all. **Two words, two worlds**: `nādim` (5×) is this-life only and always `aṣbaḥa` (*became*); `nadāma` (2×) is hereafter only, both times *they concealed regret when they saw the punishment*. **Regret is triggered by seeing** what was already true (50:22; 2:167 *God shows them their deeds as regrets*). Both human `yā ḥasratā` cries name the same object — **`ʿalā mā farraṭ-`, what I neglected** (6:31, 39:56). The **blamed parties in every hereafter dispute deny coercion** — *we had no authority over you* (37:30) is word-for-word Satan's defence (14:22) — and the companion loop runs through **lost remembrance** (43:36, 25:29; 41:25 the companions *make things look good*). **The regretful never name wanting in themselves** (no `ḥubb`, `hawā`, `ghurūr`, `amānī` self-applied); those words come only in God's voice. **Negative space**: no regret anywhere over fornication, wine, usury, theft, poverty, illness or a missed opportunity. **The window**: the same confession *we were wrongdoers* is followed by hope at 68:29-32 and is all that is left at 7:5; six this-life passages show crisis-contrition that evaporates on rescue (10:12, 10:22-23, 29:65, 30:33, 31:32, 7:134-135), and **9:75 makes, in life and conditioned on being given, the same promise the dying man wishes for at 63:10** — *give charity and be among the righteous* — and breaks it. **Grief is forbidden 16 times and never over one's own sin**; 39:53 (*do not despair of God's mercy*) stands before the regret speeches of 39:56-58.
- **Start here:** [`regret/README.md`](regret/README.md) (folder index)
- **To examine your own life:** [`regret/self-examination.md`](regret/self-examination.md) (plain language, first draft)
- **The complete list:** [`regret/2-cross-cutting/research-the-regret-catalog.md`](regret/2-cross-cutting/research-the-regret-catalog.md)
- **Synthesis:** [`regret/concept-regret-deep.md`](regret/concept-regret-deep.md)
- 13 files · 2 root + 4 narrative + 2 cross-cutting + 1 structural + 1 synthesis + 1 self-examination + 1 README + brief

### [`istighfar/`](istighfar/) — How the Quran teaches seeking forgiveness
Commissioned in one line: *"I want to research how the Quran teaches us to do istighfār."* Applied, like fasting and tahajjud: the deliverable is a **plain-language practice guide** with the Quran's own forgiveness prayers, verified letter-for-letter against the Arabic. 12 files, ~25,500 words, 8 agents.

**The answer:** istighfār in the Quran is **a request spoken directly to God** — *my Lord, forgive me / our Lord, forgive us* — made at once after a wrong and also without waiting for one, by a person who is **not knowingly persisting** (3:135), and followed by turning back (tawba) and setting right. It fixes **no number, no commanded hour, and no required feeling**.

Headline findings: **`astaghfiru` (*I seek forgiveness*) occurs exactly 3× and every time is a promise to seek it *for someone else*** (12:98, 19:47, 60:4) — two of them repudiated; the string *istaghfiri llāh* occurs once, as a command to the Prophet (4:106). Self-directed istighfār is always **addressed**: 17 `ighfir` imperatives among 22 quoted petitions, with a stable skeleton — address (`rabbi` for one, `rabbanā` for a group) → a reason joined with *so* (*we have believed, so forgive us*) → the request → mercy and other needs → a closing name (*best of the merciful*). **Every singular *forgive me* is a prophet's; every ordinary believer's petition is *forgive us*;** no one prays for others without including himself (except the angels). Confession is rare (2 of 22). **Istighfār and tawba are two acts in sequence** (`istaghfirū rabbakum thumma tūbū ilayhi`, 4/4 in Sūrat Hūd); setting-right (`aṣlaḥa`, `ʿamila ṣāliḥan`) attaches to tawba in 13 verses and to istighfār in none. **It does not wait for a known sin**: 7 of 15 prophetic istighfārs follow no stated wrong. The worldly promises (rain, wealth, sons) are made in only 3 commands, all to peoples rejecting a messenger; believers are told *God is Forgiving, Merciful*. **No count anywhere** (*much* attaches to dhikr ~10×, to istighfār 0×; the only number, 9:80's *seventy*, measures futility); **pre-dawn istighfār is praised, never commanded** (3:17, 51:18); **regret is not a stated condition, and the size of a sin is not the limit — time is** (4:17-18; 39:53; 25:68-70; 4:48/4:116 reported side by side, unreconciled). **The only fixed forgiveness word ever given to a people is `ḥiṭṭatun`** (2:58, 7:161) — and *those who wronged changed the word*. Forgiving people is tied to being forgiven by a question, not a deal: *do you not love that God should forgive you?* (24:22).

The investigation also found a **project-wide data trap**: `quran.json` writes open-fathatan tanwīn with a space before its alif (2,054 tokens, 1,533 ayahs), so accusative formula searches silently missed — `ghafūr raḥīm` was undercounted 56 vs 71. Documented in `agent-context.md`.
- **Start here:** [`istighfar/README.md`](istighfar/README.md) (folder index)
- **To practise:** [`istighfar/practice-guide.md`](istighfar/practice-guide.md) (12 Quranic prayers, plain language)
- **The method:** [`istighfar/2-cross-cutting/research-how-the-quran-teaches-istighfar.md`](istighfar/2-cross-cutting/research-how-the-quran-teaches-istighfar.md)
- **Synthesis:** [`istighfar/concept-istighfar-deep.md`](istighfar/concept-istighfar-deep.md)
- 12 files · 2 root + 3 narrative + 2 cross-cutting + 1 structural + 1 synthesis + 1 practice guide + 1 README + brief

### [`hope/`](hope/) — Hope and despair: what the Quran says to someone losing hope
Commissioned after the istighfār investigation, out of a conversation about long trials and a wish not yet granted: *"let's do a proper investigation on hope and despair."* Applied: the deliverable is a **plain-language guide for when hope runs low**, with 13 of the Quran's own sentences for each moment, verified letter for letter. 13 files, ~28,400 words, 9 agents.

**The answer:** in the Quran, hope is **a turning toward God that may name what it wants**, said aloud as *ʿasā rabbī*, "perhaps my Lord will…". Grief, fear, "when is God's help?", "I wish I had died" and asking for years are **never blamed**. Despair is faulted only as **a closed sentence about God**: *He will never*, *He does not know*, *He has humiliated me*. Help is called *near* and ease comes *with* hardship, but **never with a date, and never with a promise of the specific thing**.

**Headline findings:**
- **The hope verb `rajā` has no first-person form in the Quran.** Its object is God's side in 19 of 23 uses, and it is always tied to action (18:110). People voice hope as **`ʿasā` + my Lord** (Jacob 12:83, Moses 28:22, 68:32). The two `ʿasā` hopes that name a specific outcome are both shown fulfilled (12:99-100, 7:136-137).
- **Despair (`yaʾs`/`qunūṭ`, 16 ayahs) is faulted in 10.** Six are a verdict about God's side and four are the reflex *"when harm touches him"*; despair of an outcome is unblamed. **Grief and despair never share a verse.** Jacob alone speaks both: he grieves *to* God (12:86) and forbids despair *of* God (12:87).
- **"Help at the edge" is a pattern of the text under a selection the text declares** (11:120, 40:78), not a law. Where the edge ends in seizure instead of help, the text first names a refusal to humble oneself (6:43, 23:76).
- **`faraj` (relief) never occurs in the Quran.** Its relief words are `yusr` *with* (94:5-6) and *after* (65:7) hardship, `kashf`, `najāt`, `makhraj` and `rawḥ`. Relief is never dated.
- **Wishing (`tamannī`) is never addressed to God, and is faulted where it replaces deed or proof.** Desire is redirected rather than abolished: *ask God of His bounty* (4:32).
- **No one is rebuked for asking long, and no one is told to stop wanting.** Of 13 named asks, 9 are granted and 3 refused, each with a reason. "Perhaps you love a thing and it is bad for you" (2:216) concerns a command, not a withheld wish. Hearts are God's to join (8:63, 30:21, 60:7). **No prayer in the Quran asks God to remove a love.**
- **Trial is never called a sign of God's displeasure, or of His love.** Love attaches to the response (3:146, 3:159), and *"my Lord has humiliated me"* is answered with *kallā* (89:16-17).
- **Self-corrections:** 28 items. **57:23 is grief, not despair**, which also corrected the regret investigation.

Links:
- **Start here:** [`hope/README.md`](hope/README.md)
- **For the low days:** [`hope/practice-guide.md`](hope/practice-guide.md)
- **The model:** [`hope/2-cross-cutting/research-hope-and-despair.md`](hope/2-cross-cutting/research-hope-and-despair.md)
- **When the wish is not given:** [`hope/2-cross-cutting/research-when-the-wish-is-not-given.md`](hope/2-cross-cutting/research-when-the-wish-is-not-given.md)
- **Synthesis:** [`hope/concept-hope-deep.md`](hope/concept-hope-deep.md)
- 12 files: 3 root + 3 narrative + 2 cross-cutting + 1 structural + 1 synthesis + 1 guide + 1 README + brief

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
