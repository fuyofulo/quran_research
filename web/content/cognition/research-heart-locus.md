# Cross-cutting investigation: The Heart-Centered Epistemology

> **Source:** Phase 2 rabbit-hole agent, deep "research" investigation, 2026-04-26.
> **Hypothesis tested:** The Quran systematically locates real cognition IN THE HEART (qalb), not in the brain. This is structurally distinct from Greek nous-centered, Cartesian cogito-centered, and modern brain-centered epistemologies.
> **Triggered by:** Convergent findings across multiple individual root analyses (lbb, bSr 22:46, fqh+akinna, dbr 47:24, *kr+qulūb).
> **New concept JSONs built:** qlb, Sdr, fAd, nfs.

## The Hypothesis

The Quran systematically locates real cognition — comprehension, belief, blindness/insight, remembrance, deviation, certainty — in the **qalb** (heart), not in the brain or an abstract intellect. Cognitive faculties (sight, hearing, reflection, deep comprehension) succeed or fail depending on the heart's *state*. This is structurally distinct from Greek nous-centered, Cartesian cogito-centered, and modern brain-centered epistemologies.

## 1. The qlb data

Built `data/concepts/qlb.json` (`python3 scripts/build_concept.py qlb`):

- **168 occurrences** across **155 ayahs** in **48 surahs** (110 Medinan / 58 Meccan).
- **9 lemmas**, falling into two semantic families:
  - **Heart-as-organ (the noun قَلْب `qalb`)** — 132 occurrences, the dominant sense.
  - **Turning/overturning verbs** (`{nqalaba` 17, `qal~aba` 6, `taqal~ub` 5, `munqalibūn` 3, `munqalab` 2, `tataqal~abu` 1, `tuqolabu` 1, `mutaqal~ab` 1) — same root, semantically about flipping, returning, being turned over (the heart is literally "the turner").
- Of the 132 noun forms: **112 plural** (qulūb, قُلُوب — collective hearts), **20 singular** (qalb / qalbī / qalbihi). The collective plural dominates because the Quran usually addresses *communities* of hearers/disbelievers/believers.
- Co-occurrence with صدر (chest/breast) at the ayah level: **5 ayahs** explicitly join the two — including the key 22:46 ("hearts within the breasts"), 39:22, 16:106, 42:24, 3:154. This embodied locator (heart-inside-chest) is rare but doctrinally pivotal: the Quran insists the cognitive heart is a *physical, located thing*, not a metaphor.

## 2. What is done to hearts (precise root co-occurrence)

Using ayah-level root co-occurrence from `data/morphology/words.jsonl` against the 124 unique qalb-noun ayahs:

| State | Root | Ayahs | Example |
|---|---|---|---|
| **Sealed (set seal upon)** | TbE طبع | 11 | 16:108 — "those over whose hearts and hearing and vision Allah has sealed" |
| **Sealed (xtm)** | xtm ختم | 4 | 2:7 — `khatama llāhu ʿalā qulūbihim` |
| **Veiled with akinna (coverings)** | knn كنن | 4 | 6:25, 17:46, 18:57, 41:5 — "We placed over their hearts coverings (akinna), lest they comprehend (yafqahūhu)" |
| **Overlaid (ghishāwa)** | g$w غشو | 5 | 2:7, 45:23 — covering on hearing/sight |
| **Hardened** | qsw قسو | 6 | 2:74 ("hearts became hard like stone, even harder"), 5:13, 6:43, 22:53, 39:22, 57:16 |
| **Softened** | lyn لين | 2 | 39:23 — "their skins and hearts soften (talīnu) at the remembrance of Allah" |
| **Made firm / strengthened** | vbt ثبت | 2 | 8:11, 11:120, 25:32, 28:10 — God "binds fast" / "strengthens" the heart |
| **Sick / diseased** | mrD مرض | 12 | recurring "those in whose hearts is disease" (2:10, 5:52, 8:49, 22:53, 33:12, 47:20, 47:29...) |
| **Locked** | qfl قفل | 1 | 47:24 — `am ʿalā qulūbin aqfāluhā` ("locks upon hearts") |
| **Rusted / stained** | ryn رين | 1 | 83:14 — "rather, what they were earning has rusted (rāna) on their hearts" |
| **Opened / expanded** | $rH شرح | 2 | 39:22, 94:1, 6:125, 20:25 (always with chest, ṣadr) |
| **Made tranquil (sakīna)** | skn سكن | 4 | 48:4, 48:18, 48:26 — "He sent down sakīna into the hearts" |
| **Drawn to find rest** | (cf. *kr) | 18 | 13:28 — "hearts find rest in remembrance of Allah" |
| **United / brought together** | Alf ألف | 3 | 8:63, 3:103 — Allah joins hearts |
| **Terrorized** | rEb رعب | 4 | 3:151, 8:12, 33:26, 59:2 — "We will cast terror into the hearts of those who disbelieved" |
| **Made to deviate (zaygh)** | zyg زيغ | 5 | 3:7, 3:8 ("let not our hearts deviate"), 9:117, 33:10, 61:5 |
| **Made anxious (wajifa)** | wjf وجف | 1 | 79:8 — "Hearts that day will tremble" |
| **Dead** | mwt موت | 4 | implicit — "their hearts have died / died as disbelievers" |

Plus heart + cognitive roots: **fqh** (deep comprehension) **7 ayahs**, **dbr** (ponder) **2** (incl. the famous 47:24), **Eql** (reason) **2** (incl. 22:46), **bSr** (sight) **11**, **smE** (hear) **12**, ***kr** (remember) **18**.

The heart is treated as a **morally and cognitively conditioned organ** with a vocabulary of inner medicine: it can be sealed, locked, rusted, hardened, sick, dead — or expanded, softened, made firm, made tranquil, united, alive.

## 3. The accountability triad — 17:36

The Arabic: إِنَّ السَّمْعَ وَالْبَصَرَ وَالْفُؤَادَ كُلُّ أُولَٰئِكَ كَانَ عَنْهُ مَسْئُولًا

| | |
|---|---|
| **Saheeh** | "the hearing, the sight and the **heart** — about all those one will be questioned" |
| **Pickthall** | "the hearing and the sight and the **heart** — of each of these it will be asked" |
| **Khattab** | "all will be called to account for their hearing, sight, and **intellect**" |
| **Arberry** | "the hearing, the sight, the **heart** — all of those shall be questioned of" |

Three of four translators render `fuʾād` as "heart"; **Khattab uniquely translates it "intellect"** — exposing the conceptual collision: a Western-framed translator reaches for *intellect* because the function described (epistemic accountability for what one believes/knows) is what Western thought lodges in the mind. The Arabic itself does not.

**fuʾād (فؤاد)** is the deeper register of *heart*: 16 occurrences, all Meccan, never plural in the Madinan polemical sense. It pairs almost exclusively with hearing+sight (7 of 15 ayahs co-occur with bSr, 6 with smE). It is the heart that is "made firm" for the Prophet (11:120, 25:32), "bound fast" for Moses' mother (28:10), the heart that "did not lie about what it saw" in the vision of the Prophet (53:11), and the heart that accountability attaches to (17:36). Where `qalb` is the conditional, plural, communal organ (it can rust, lock, deviate), `fuʾād` is the **innermost witness** — the heart as ultimate seat of receptive truth. Both are anatomically heart, not head.

## 4. The chest, the self, the heart

- **ṣadr (صدر, chest/breast)** — 46 occurrences, 41 noun. Functions as the *container* of the heart (22:46 "hearts within the breasts"; 16:106 "chest at-ease with faith"). It is what gets *expanded* (شرح) to Islam (94:1, 39:22, 6:125, 20:25) — the chest is opened so the heart inside can receive. ṣadr is also where one *conceals* (11:5, 3:154). Five ayahs explicitly stack qalb-inside-ṣadr.
- **fuʾād** — 16 occurrences, the receptive, witnessing heart (above).
- **nafs (نفس, self/soul)** — 298 occurrences, the most frequent of all. But its cognitive role is different: nafs is the *moral subject* — the agent that sins, suffers, dies, is held accountable, and is divided into types: `ammāra bi-s-sūʾ` (commanding evil, 12:53), `lawwāma` (self-reproaching, 75:2), `muṭmaʾinna` (tranquil, 89:27). Nafs is *who* you are; qalb is *where you understand*.

These three are not synonyms. They form an anatomy: **ṣadr** (the chest cavity/container), **qalb** (the conditioned cognitive heart inside it), **fuʾād** (its innermost witnessing core), and **nafs** (the moral self that owns all three).

## 5. Synthesis: Quranic vs other epistemologies

- **Greek nous / Aristotelian intellectus**: cognition is in the *intellectual soul*, abstract, located in the head (already by the time of Plato's Timaeus, Galen's brain-localization). To know is to grasp form with mind.
- **Cartesian cogito**: "I think therefore I am" — thinking is the foundational act, located in *res cogitans*, which by Descartes' own dualism is non-extended but practically interfaces at the pineal gland in the head.
- **Modern cognitive science**: cognition = neural computation in the brain.

The Quran maps the same faculties — knowing, believing, comprehending, being convinced, being deluded — to **qalb / fuʾād inside the ṣadr**. Crucially:

1. **It is not metaphor**: 22:46 explicitly relocates blindness from eyes to "the hearts which are within the breasts" (`al-qulūbu llatī fī ṣ-ṣudūr`). The Quran goes out of its way to make the location physical.
2. **Cognition is conditional, not faculty-based**: in Greek/Cartesian thought, you reason badly because of bad logic or bad data. In the Quran, you fail to comprehend because your heart is *sealed, locked, covered, hardened, rusted, sick, dead*. Epistemic failure is a *medical/spiritual condition of an organ*, not a logical error.
3. **Cognition is morally indexed**: hearts harden through breaking covenants (5:13), through accumulated earnings (83:14), through arrogance. They soften through remembrance (39:23), expand through guidance (39:22), find rest through dhikr (13:28). Knowing and being are continuous — there is no morally neutral "pure reason."
4. **Sensory faculties are downstream**: hearing and sight always appear *with* the heart (17:36, 16:78, 23:78, 32:9, 46:26, 67:23). They report inputs; the heart processes. A heart that is sealed leaves the ear deaf (6:25, 17:46) — sensory failure is *caused by* heart-failure.
5. **Accountability is for the heart, not the head**: 17:36 — you will be questioned about hearing, sight, and *fuʾād*. Not about your intellect, not about your brain. The locus of moral-epistemic accountability is the heart.

## Implications for "cognition" in the Quran

To "know" in the Quran is not to entertain a justified true belief in a brain. It is for a *receptive, located organ inside a chest cavity* to be in the right state — soft, expanded, firm, tranquil, alive — such that when revelation, signs (āyāt), and travel through the earth reach it, comprehension (fiqh) and certainty happen. Conversely, perfectly intact eyes and ears can deliver perfect data to a sealed heart and produce zero understanding (the recurring fate of disbelievers). This means the Quran's epistemology is **embodied, ethical, and pathological** in a way Western epistemology has not been since the pre-Socratics — and it has its own clinical vocabulary (seal, lock, rust, disease, hardness, expansion, softening, tranquility) for diagnosing cognitive states that Western philosophy has no equivalent for.

## One-sentence summary

In the Quran, real cognition is not a function of the brain or an abstract intellect but the receptive condition of a physical heart inside the chest — an organ that can be sealed, locked, rusted, hardened, expanded, or softened, and whose moral-spiritual state, not its information input, determines whether understanding happens.
