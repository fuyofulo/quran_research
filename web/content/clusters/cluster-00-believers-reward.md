# Cluster 0 — The Believers' Reward (الإيمان والجنّات)

> **Size:** 62 roots | **Source:** Parallel-agent analysis, 2026-04-26
> **Top members:** امن · عمل · عند · جنن · حسن · نور · صلح · سوا
> **Full data:** `data/full-quran-graph/clusters.json` key "0"

## Cluster name
**The Believers' Reward (الإيمان والجنّات)**

## Semantic territory

This cluster is the densest formulaic core of Quranic eschatology — the recurring promise to those who believe and act righteously. The data is unambiguous: ايمن (Amn, "believe") co-occurs with عمل (Eml, "do/work") in 101 ayahs, and SlH ("righteous deeds") co-occurs with عمل in 93 ayahs. The phrase **الذين آمنوا وعملوا الصالحات** ("those who believe and do righteous deeds") is a genuine Quranic n-gram, and that n-gram pulls into its orbit the entire vocabulary of paradise: جنّة (gardens), نهر (rivers), جري (flow), تحت (beneath), خلد (abide eternally), أبد (forever), ادخل (enter), أجر (reward), جزي (recompense), حسن (goodness/beauty), سواء (likewise/peer), فوز (great attainment), رضو (mutual pleasure of God and servant), طهر (purification), and نور (light). Negative-pole roots that appear here belong to the same formula's *contrast* clause: حبط (deeds rendered worthless), خزي (disgrace), سخط (divine wrath), خدع (the hypocrites' self-deception). It is, in graph terms, a single sentence template that learned to be a community.

## Sub-themes

1. **The two-verb covenant** — آمن + عمل + صلح: faith inseparable from righteous action. SlH's strongest two partners are Eml (.55) and Amn (.48); this is the densest dyad in the corpus.
2. **Garden topography** — جنّة, نهر, جري, تحت, غرف ("chambers"), روض ("meadows"), ظما ("thirst" – its absence), بول (entering, dwelling), ثوي ("dwelling"), زلف ("brought near"). nhr's signature partners are jry (.44) and tHt (.39): rivers that flow beneath.
3. **Eternity and recompense** — خلد, أبد, دوم ("perpetual"), أجر, جزي, ثوب ("reward/return"), نفل ("bonus"), وهب ("grant"), لدن ("from Himself"), عطو ("bestowal"), قرض ("the goodly loan to God"). The reward economy.
4. **Honour vs. abasement (the contrast clause)** — رضو, فوز, نور, حسن, عظم ("magnificent reward"), طهر vs. خزي, حبط ("deeds nullified"), ضيع ("lost"), سخط, خدع, تبر ("ruined"), زلق ("slipped"), زلزل ("shaken"), صغو ("hearts inclining wrongly").
5. **Trial and purification as entry-conditions** — محص, محن, خبت ("humbled before the Lord" — a verbatim paradise-dweller predicate in 11:23), ضعف ("the weak/oppressed"), دفع ("warding off"), حمي ("zeal/protection"), أوب ("returning to God"). The roots that explain *who* the formula admits.

## Top 7 structurally important roots (by in-cluster co-occurrence sum)

1. **امن / Amn** — 879 occ, in-cluster sum 636. The keystone; binds the whole cluster.
2. **عمل / Eml** — 360 occ, sum 554. The verb that turns belief into the formula.
3. **جنن / jnn** — 201 occ, sum 445. The destination noun.
4. **صلح / SlH** — 180 occ, sum 407. The qualifier on Eml; "righteous" deeds.
5. **نهر / nhr** — 113 occ, sum 318. The hydraulic signature of paradise.
6. **جري / jry** — 64 occ, sum 288. Co-binds with nhr, tHt to form the "flow beneath" image.
7. **تحت / tHt** — 51 occ, sum 292. Punches far above its raw frequency — almost every تحت in the cluster is part of تجري من تحتها الأنهار.

(Hsn, dxl, swA, xld, Ajr, End all sit just below this tier and form the second ring.)

## Surprises

- **بعل (bEl, "husband/Baal")** clusters here, not in the family/marriage cluster. Reason: it appears in legal contexts adjacent to the believer-formula (2:228, 4:128, 11:72), so co-occurrence drags it in via Amn rather than via family vocabulary.
- **رسّ (rss, "people of Ar-Rass")** — an obscure destroyed people, appears only twice (25:38, 50:12) but in each case alongside صحب ("companions of"), which is itself a paradise-formula word (أصحاب الجنّة). The graph correctly notices that rss's partner is the formula word, not the destruction word.
- **قرض (qrD, "loan")** — "Who will lend Allah a goodly loan?" is a *reward-economy* verse, not a finance verse; the clustering catches the theological metaphor.
- **ضعف (DEf, "weakness")** — sits in the *reward* cluster, not the affliction cluster, because its dominant Quranic context is "the oppressed/weak who will be heirs of paradise."
- **خدع (xdE, "deceive")** — only 5 occurrences; lands here because every instance is about hypocrites trying to deceive the believers (Amn).
- **زلزلة (zlzl, "earthquake/convulsion")** clusters with paradise rather than with eschatological terror, because in 2:214 and 33:11 it describes the *testing* of believers en route to the garden.
- **The cluster contains almost no ritual-worship roots** (no صلو, زكو, صوم, حجّ) — those live elsewhere. This is purely the *outcome* vocabulary of faith, not its practice.

## Suggested research directions

1. **Phrase-template extraction.** Quantify how much of the cluster's modularity is driven by a single n-gram (تجري من تحتها الأنهار خالدين فيها). Slide a window across ayahs and measure: what fraction of cluster-internal edges collapse to ≤3 fixed templates? This would distinguish *thematic* clustering from *formulaic* clustering.
2. **Polarity-balanced sub-graph.** Within the cluster, separate reward-pole roots (رضو, فوز, نور, جنن, نهر) from punishment/contrast-pole roots (خزي, حبط, سخط, خدع, تبر, ضيع). Are these two halves connected only via Amn/Eml as bridges, or do they share their own internal edges? This would reveal whether the Quran treats reward and disgrace as a single rhetorical unit or as parallel sub-systems.
3. **Diachronic / surah-order layering.** Do Meccan surahs lean on the شرعة/جنّة imagery (jnn, nhr, xld) while Medinan surahs add the legal-economic layer (qrD, jzy, Ajr, dxl)? Plot per-root surah distributions weighted by Nöldeke chronology to see if the cluster grew a juridical shell over a poetic core.
4. **The "humbled-heart" entry condition.** Roots like خبت, محص, محن, أوب, ضعف appear small but topologically connect Amn to the trial vocabulary. Extract every ayah containing two of these plus Amn — this should yield a tight characterization of the Quran's psychological prerequisites for the reward formula, distinct from the legal prerequisites.

## One-sentence summary

Cluster #0 is the Quran's reward formula made graph — the gravitational well around الذين آمنوا وعملوا الصالحات that pulls in the gardens, the rivers beneath, eternal abiding, divine pleasure, and (as inverse shadows) the disgrace and nullified deeds of those who fail it.
