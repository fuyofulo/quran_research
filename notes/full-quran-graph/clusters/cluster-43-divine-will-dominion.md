# Cluster 43 — Mashī'a wa Mulk: The Grammar of Divine Will

> **Size:** 13 roots | **Source:** Parallel-agent analysis, 2026-04-26
> **Top members:** شيا · كلل · ملك · قدر · رزق · حوط · بسط · خطف
> **Full data:** `data/full-quran-graph/clusters.json` key "43"

## Cluster name
**Mashī'a wa Mulk — The Grammar of Divine Will, Dominion & Decreed Measure**

## Semantic territory

This cluster is not a topic so much as a **theological syntax** — the recurring set of words that the Qur'an uses to formulate God's unconditioned sovereignty over being, possession, allotment, and outcome. Its center of gravity is the Qur'an's two great formulaic operators: شَيْء ($yA, 519) and كُلّ (kll, 377). Together they generate the omni-quantifier "كل شيء" — "every thing" — which is then completed by an attribute of God: قَدِير (qadiyr "competent over"), مُحِيط (muHiyT "encompassing"), مَلِك (malik "sovereign"), رَزَّاق (razzaq "provider"). Around this scaffolding sit the verbs of distribution — بَسَط (basaTa, "extend/spread") and قَدَر (qadara, "measure/restrict") — which form the matched pair "yabsuṭu… wa yaqdiru" (He extends and He restricts). The smaller members (دخر "abject submission," مزق "tearing apart," محو "erasing," فوج "throngs," خطف "snatching") are eschatological/destructive verbs of what the willing Sovereign actually does to creatures. The cluster is essentially the linguistic machinery of divine prerogative.

## Sub-themes

1. **The omni-quantifier formula** — كُلّ + شَيْء + (قَدِير / عَلِيم / مُحِيط). The single most frequent theological refrain in the Qur'an lives here. شيا and كلل are functor words whose massive co-occurrence with Alh, smw, ArD reflects this construction.
2. **Sovereignty of dominion (mulk)** — مُلْك, مَلِك, مَالِك, مَلَكُوت: the lexicon of kingship/possession of heavens-and-earth, including the "to whom does the kingdom belong today?" verses.
3. **Decree, measure, and capacity (qdr)** — both قَدَر (cosmic decree, fixed measure) and قَادِر/قَدِير (divine power-to-do). qdr stands at the hinge between will and outcome.
4. **Provision economics (rzq + bsT + qdr)** — رزق ("provision") clusters with بسط ("extend") and قدر ("restrict") in the standard "yabsuṭu r-rizqa li-man yashā'u wa yaqdir" formula (13:26, 17:30, 29:62, 30:37, 34:36, 42:12, 42:27).
5. **Eschatological enactment of will** — the small-but-thematic tail (مزق "shredding apart," محو "erasing," فوج "throngs," دخر "abjectly submitted," خطف "snatched away") shows what divine will *does* in history and on the Last Day: tearing nations to pieces (34:19), erasing/confirming verses (13:39), people entering religion in throngs (110:2), all coming abjectly (27:87). فرش ("spread out": earth as bed) is the cosmological counterpart — the spreading of provision-ground.

## Top 7 structurally important roots

1. **شيا ($yA, 519)** — the universal noun "thing" + verb شاء "to will"; both senses anchor the cluster.
2. **كلل (kll, 377)** — the universal quantifier; pairs with شيا to make the omni-formulae.
3. **ملك (mlk, 206)** — kingship/dominion; carries the propositional content of sovereignty.
4. **قدر (qdr, 132)** — power + measure; the bridge from will to actualization.
5. **رزق (rzq, 123)** — the prime example of decreed apportionment; theology of sustenance.
6. **بسط (bsT, 25)** — operator of "extending" (provision, hand, stature); makes the bsT/qdr binary that defines divine economy.
7. **حوط (HwT, 28)** — أَحَاطَ / مُحِيط: God's *encompassing* — knowledge, power, and judgment that surrounds creation.

## Surprises

- **حوت (whale) vs. حوط (encompass)** — case-collision in `build_concept.py` returns Hwt (whale) when given HwT. The cluster's true HwT is محيط/أحاط, the perfect semantic complement to *kullu shay'in* (He encompasses every thing). Worth fixing the script.
- **مزق (shredding, only 4 occ)** sits in this cluster despite seeming destructive: the link is Sabā' (34:19) — God *makes them tales* and *tears them utterly*, the negative face of sovereignty.
- **فرش "to spread"** (earth as bed, 51:48) is here, not in the cosmology cluster — because in the data it lives near rzq/nEm (provisioning), framing creation itself as extended sustenance.
- **خطف "snatching"** appears tied to lightning snatching sight (2:20) and Quraysh fearing being snatched from their land (28:57, 29:67) — both are vignettes of *contingency under sovereignty*.
- The cluster is dominated by two pure functor words (شيا, كلل) that are not "theological" in themselves but are co-opted as the Qur'an's universal-quantifier vocabulary. **This is a syntactic cluster as much as a semantic one.**

## Suggested research directions

1. **Map the "kullu shay'in qadīr/ʿalīm/muḥīṭ" formulae across the Qur'an** — count exact bigram completions of كل شيء and chart how the chosen attribute (qadīr vs. ʿalīm vs. muḥīṭ vs. ḥafīẓ) varies by sūra, period (Meccan/Medinan), and surrounding theme.
2. **The bsT/qdr binary as economic theology** — extract every "yabsuṭu… wa yaqdiru" pair and analyze its rhetorical function (consolation? warning? polemic against assuming wealth = favor?).
3. **شاء (mashī'a) clauses as theological conditioner** — every "law shā'a Allāhu / li-man yashā'u" instance: what does divine will gate (guidance, provision, kingship, taking-away)? Build a typology of conditioned predicates.
4. **Fix the root-disambiguation bug** in `scripts/build_concept.py`: case-insensitive matching collides Hwt/HwT, $yA/$yA, etc. Re-run cluster #43's concept files with proper root keys.

## One-sentence summary

Cluster #43 is the Qur'an's *grammar of unconditioned divine prerogative* — the linguistic engine where universal quantifiers (kullu, shay'), the will-verb (shā'a), the dominion-noun (mulk), and the dual measure-operators (basaṭa / qadara) combine to assert that every thing, every provision, and every outcome is encompassed (muḥīṭ) by a Sovereign who acts as He wills.
