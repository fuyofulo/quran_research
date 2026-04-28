# Cluster 90 — The Sin–Mercy Economy

> **Size:** 24 roots | **Source:** Parallel-agent analysis, 2026-04-26
> **Top members:** رحم · غفر · موت · غير · عدو · توب · ضرر · فسق
> **Full data:** `data/full-quran-graph/clusters.json` key "90"
> **Cross-reference:** This cluster contains رحم (mercy/wombs); see also `notes/mercy/concept-rhm.md` for prior deep analysis.

## Cluster name
**The Sin–Mercy Economy: Forgiveness, Transgression, and Forbidden Things**

## Semantic territory

This cluster maps the Quran's complete moral-transactional economy — the full circuit by which human wrongdoing meets divine response. Where cluster #90 collects 24 roots that systematically co-appear at the *ayah level*, the structural logic is striking: every offense-root (إثم، فسق، عصي، عدو، ضرر، سفك، بهت) sits in the gravitational field of every relief-root (رحم، غفر، توب، نفع), bound together by the formulaic closing "إِنَّ اللَّهَ غَفُورٌ رَحِيمٌ." Mercy, here, is not abstract — it is the back-half of a sin/forgiveness ledger. The cluster also pulls in the *concrete substrates* over which that ledger transacts: meat (لحم), blood (دمو), pig (خنزر), what is consecrated (هلل), death (موت), oath/division of estate (قسم), inclination-toward-sin in bequests (جنف), bloodshed (سفك), clothing-as-recompense (كسو), traveling/fasting (سيح). Mercy in cluster #90 is the language of dietary, contractual, and bodily-ethical law — not the cosmological mercy of سورة الرحمن.

## Sub-themes

1. **The formulaic closing pair (رحم ↔ غفر ↔ توب).** This is the cluster's core engine. غفر co-occurs with رحم in 91 ayahs (the highest in-cluster pairing); توب co-occurs with both. These three roots constitute the standard Qur'anic verse-coda: "تُوبُوا… غَفُورٌ رَحِيمٌ." Mercy here is *triggered* by repentance and *expressed* as forgiveness.

2. **The dietary-law sub-graph (خنزر، لحم، دمو، هلل، موت، جنف).** A tight, almost mechanical cluster: every one of these roots co-occurs with every other in exactly the same 4 ayahs (2:173, 5:3, 6:145, 16:115). The cluster is so symmetric it nearly forms a clique. The closing of these verses ("فَإِنَّ اللَّهَ غَفُورٌ رَحِيمٌ") is what binds them upward into the mercy field.

3. **Wrongdoing and its modalities (إثم، فسق، عدو، عصي، ضرر، سفك، بهت).** Seven distinct categories of moral failure: sin-as-burden (إثم), corruption-from-the-path (فسق), enmity/aggression (عدو), disobedience (عصي), inflicting-harm (ضرر), bloodshed (سفك), and slander/calumny (بهت). The cluster doesn't conflate these; it lists the offense-types that *qualify* for the mercy formula.

4. **Hope vs. despair (قنط، عسى، حرص).** قنط appears 4 of its 6 times paired directly with رحم — "do not despair of God's mercy" (15:56, 39:53, 30:36, 41:49). عسى ("perhaps/it may be") functions as the modal of conditional hope. حرص is the human counter-weight of greedy clinging to life. Together they encode the *affective* posture the human takes inside the sin/mercy economy.

5. **Benefit/harm symmetry and contractual ethics (نفع ↔ ضرر، قسم، كسو، سيح).** نفع and ضرر co-occur 17 times — they are nearly Quranic antonyms ("they neither benefit nor harm"). قسم spans both oath-swearing and the *division* of an estate; كسو (clothing) and سيح (traveling/fasting) appear as expiations and as marks of the repentant. This is the contractual-law underbelly of the cluster.

## Top 7 structurally important roots

1. **رحم (rHm, 339)** — the field's gravitational center; co-occurs with every sub-graph.
2. **غفر (gfr, 234)** — the operational verb of mercy in this cluster (91-ayah overlap with rHm).
3. **توب (twb, 87)** — the human-side verb that activates the rHm/gfr response.
4. **عدو (Edw, 105)** — the prototypical offense-type; binds to إثم (9), غفر (7), and the war-ethics ayahs.
5. **موت (mwt, 165)** — bridges the dietary-law sub-graph with the resurrection/judgment frame; the moment at which the ledger settles.
6. **ضرر (Drr, 60)** — the harm-pole of the moral economy; the strongest نفع↔ضرر axis (17 ayahs).
7. **إثم (Avm, 48)** — the densest connector among offense-types: links to عدو, غفر, غير, رحم, موت, جنف.

## Surprises

- **The cluster is bimodal.** It's not one concept but two interlocking circuits: an *abstract* one (sin → repentance → forgiveness → mercy) and a *concrete* one (forbidden food, bequest law, oath, bloodshed). Louvain detected them as one cluster because the formulaic verse-coda *physically welds* the two.
- **خنزر/لحم/دمو/هلل form a near-clique.** Eight roots co-appearing in exactly the same handful of dietary verses — a structural footprint so clean it's almost a fingerprint of one verse-template repeated across surahs.
- **ESy and Esy are duplicates.** Both are عصي (disobedience) with identical lemmas (عَصَا) and identical co-occurrence profiles. This is a data-quality artifact in the underlying QAC morphology, not a real distinction. **Worth flagging upstream.**
- **قنط (despair) is almost entirely a *negation*-context word.** 5 of 6 occurrences are "do not despair." The cluster treats despair-of-mercy as itself an offense.
- **رحم is here in a different mode than in concept-rhm.md.** The earlier analysis surfaced rHm's pairing with Allah/Lord/Knowing (the *attribute* mode). Cluster #90 surfaces the *transactional* mode — mercy paired with sin-vocabulary. **These are the same root operating in two registers.**

## Suggested research directions

1. **Verse-template extraction.** Build a structural matcher for the "[offense-clause] + إِنَّ اللَّهَ غَفُورٌ رَحِيمٌ" template. Quantify how many of the 313 rHm ayahs are this template vs. attribute statements vs. narrative.
2. **The dietary-law clique as a validation case.** The خنزر/لحم/دمو/هلل clique should appear as a sub-cluster under almost any community-detection algorithm; use it as a benchmark for comparing Louvain vs. spectral vs. label-propagation.
3. **Cross-reference with cluster containing ذنب، خطء، سيء.** This cluster names *some* offense-roots but not all. Where does sin-vocabulary split across clusters, and why? (Hypothesis: the offense-roots that don't appear here pair more with judgment/punishment than with mercy/forgiveness — a different transactional circuit.)
4. **Resolve the ESy/Esy duplication in `data/morphology/roots.json`.** This duplication is propagating through every concept file and inflating cluster sizes. Worth a one-line fix and a re-run of `build_concept.py`.

## One-sentence summary

Cluster #90 is the Quran's moral-transactional economy — the syntactically-bound circuit where every named human offense (sin, transgression, harm, disobedience, forbidden food) terminates in the formulaic divine response of forgiveness and mercy.
