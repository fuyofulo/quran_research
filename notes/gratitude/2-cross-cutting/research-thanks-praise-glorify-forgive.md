# Thanks, praise, glorification, forgiveness: how the text makes them travel

## Headline finding

The commissioner's pair is real. *Sabbiḥ bi-ḥamdi* and the istighfār verb share an ayah 4× (40:7, 40:55, 42:5, 110:3), and 110:3 commands both on receiving a gift.

**Thanks stands outside that pair.** `shkr` shares no ayah with `sbḥ` or istighfār, and never comes within five ayahs of istighfār. It reaches forgiveness by two other roads:
- ***tawba***: in one ayah (46:15), and within two ayahs in 6 more passages;
- **God's names *ghafūr shakūr*** (3×).

Remembrance comes first in 8 of 9 shared ayahs. Acknowledgement usually comes before asking. Paradise keeps only glorification, peace and praise.

---

## 1. The co-occurrence map (data-grounded, `words.jsonl`)

**Sets.**
- **`shkr`**: all 75 tokens.
- **`ḥmd`**: *ḥamd/ḥamīd/ḥāmidūn*, 61 tokens.
- **`sbḥ`**: glorify lemmas only, 87 tokens.
- **istighfār**: lemma `{sotagofara`, 40 tokens.
- **`ḏkr`**: *dhakara/dhikr/dhākir-*, 163 tokens (no *dhakar*, "male"). This is an upper bound, because *dhikr* includes "the Reminder".
- **`kbr`**: *kabbara/takbīr*, 5 tokens.
- **`twb`**: all 87 tokens.

| | shkr | ḥmd | sbḥ | istighfār | ḏkr | kbr | twb |
|---|---|---|---|---|---|---|---|
| **shkr** | 69 | 2 | **0** | **0** | 3 | 1 | 1 |
| **ḥmd** | | 59 | **16** | 4 | **0** | 1 | 3 |
| **sbḥ** | | | 83 | 4 | 5 | 0 | 3 |
| **istighfār** | | | | 36 | 1 | 0 | **9** |
| **ḏkr** | | | | | 147 | 0 | **0** |
| **kbr** | | | | | | 4 | 0 |

**Frequent pairs.**
- **sbḥ × ḥmd 16**: the *bi-ḥamdi* ayahs, plus 10:10 and 39:75.
- **istighfār × twb 9**.
- **sbḥ × ḏkr 5**.
- **ḥmd/sbḥ × istighfār 4**, the same four ayahs. **40:7 and 110:3 hold sbḥ, ḥmd, istighfār and twb together.**
- **The shkr row**: ḥmd 2 (31:12, 35:34, crossed), ḏkr 3 (2:152, 8:26, 22:36), kbr 1 (2:185), twb 1 (46:15). No ayah holds shkr with two others.

**Absences.**
- **shkr × sbḥ 0.**
- **shkr × istighfār 0, even within ±5 ayahs.** The nearest is 6 away (27:40/27:46; 40:61/40:55). Adding *mustaghfirīn* (3:17) and *istighfār* (9:114) changes nothing.
- ḥmd × ḏkr 0. ḏkr × twb 0.

**What surrounds thanks instead.**
- **shkr × the whole `gfr` root: 5 ayahs (34:15, 35:30, 35:34, 42:23, 64:17). The forgiveness is God's in all five.**
- **shkr within ±2 of twb: 9 passages** (2:52-56, 2:158-160, 2:185-187, 4:146-147, 6:53-54, 7:143-144, 16:119-121, 42:23-25, 46:15).
  Human turning appears in 7, and turning comes first in only 3 of those 7.
- **shkr within ±2 of sbḥ: 5** (§4).

**Takbīr is rare: commanded in 4 ayahs (2:185, 17:111, 22:37, 74:3).**
- The formula *Allāhu akbar* is absent; *llāhi akbar* is only a comparative (9:72, 29:45, 40:10).
- ***Li-tukabbirū llāha ʿalā mā hadākum* occurs exactly twice (2:185, 22:37), both beside thanks.** At 22:36 the thanks is one ayah earlier, under the same lead-in, *kadhālika sakhkharnāhā lakum*.

---

## 2. The sequences

| Ref | Order in the text |
|---|---|
| 110:1-3 | victory → **glorify with praise → seek forgiveness** → *tawwāb* |
| 40:55 | be patient → **seek forgiveness for your sin → glorify with praise**, evening and morning |
| 40:7-9 | angels **glorify with praise → believe → seek forgiveness** → *forgive those who turned* |
| 42:5 | angels **glorify with praise → seek forgiveness** → *ghafūr raḥīm* |
| 2:152 | **remember** → I remember you → **thank** → do not be ungrateful |
| 2:185-187 | complete the count → **magnify** → **thank** · 2:187 *He relented and pardoned* |
| 22:36-37 | **mention His name** → eat, feed → **thank** → **magnify** |
| 43:13-14 | **remember the blessing → *subḥāna…*** → *to our Lord we return* (`qlb`) |
| 23:28-29 | **praise** (*who saved us*) → **ask** (a blessed landing) |
| 46:15 | **ask to thank** → to do right → for offspring → ***I have turned to You*** → I am a *muslim* |
| 7:143-144 | ***subḥānaka* → *tubtu ilayka*** → God: ***be among the grateful*** |
| 3:190-194 | **remember** → reflect → ***subḥānaka*** → protect → *we believed* → **forgive us** → grant |
| 3:16-17; 51:16-19 | *we believed* → forgive us → … **pre-dawn seekers of forgiveness** (last); *muḥsinīn* → little sleep → **pre-dawn istighfār** → the beggar's right |
| 3:135 | a wrong → **remember God → seek forgiveness** → do not persist |
| 2:198-200 | **remember Him as He guided you** → depart → **seek forgiveness** → remember more |

**Counts (data-grounded).**
- **Remembrance comes first in 8 of the 9 ayahs `ḏkr` shares with the others** (and across 2:198-199).
  - The exception, 25:18, is the reminder **forgotten because they were given enjoyment** (*mattaʿtahum … ḥattā nasū dh-dhikr*).
- **Glorify-with-praise comes before istighfār in 3 of 4. 40:55 reverses it:** *wa-staghfir li-dhanbika wa-sabbiḥ bi-ḥamdi rabbika*.
- **Acknowledgement comes before asking** in 110:3, 40:7, 42:5, 23:28-29, 3:191-193, 7:143 and the Fātiḥa (1:2 before 1:6). **The only reversal is 40:55.**
- **Thanks is last when it is a purpose** (2:52, 2:152, 2:185, 8:26, 22:36). **Turning or returning closes** 43:14, 46:15, 7:143, 110:3 and 40:7.
- **Rites end differently**:
  - the fast in *magnify + thank* (2:185);
  - the sacrifice in *thank + magnify* (22:36-37);
  - the night prayer (73:20) and the ḥajj departure (2:199) in *seek forgiveness*;
  - the victory in *glorify with praise + seek forgiveness* (110:3).

**[interpretive] Recurring order.** *Remember → acknowledge (glorify / praise / magnify / thank) → ask → turn or return.*

The occasion seems to pick which act leads:
- **Where the verse names a gift, acknowledgement leads**: *God wants ease* (2:185), *We subjected them* (22:36), *the victory has come* (110:1).
- **Where it names a shortfall, istighfār leads or stands alone**: *you were astray* (2:198), *He knew you could not keep it* (73:20), a wrong (3:135), *your sin* under insult (40:55).
Thanks acknowledges a gift, istighfār asks after a lack, and *tawba* closes either.

> فَسَبِّحۡ بِحَمۡدِ رَبِّكَ وَٱسۡتَغۡفِرۡهُۚ إِنَّهُۥ كَانَ تَوَّابَۢا (110:3)
> Saheeh: *Then exalt [Him] with praise of your Lord and ask forgiveness of Him. Indeed, He is ever Accepting of repentance.*

The commanded response to the Quran's largest named gift has no `shkr` word. It is the commissioner's two acts.

---

## 3. Why thanks and seeking forgiveness belong together, in the text's terms

**(a) One fact, two endings.**

> وَإِن تَعُدُّواْ نِعۡمَتَ ٱللَّهِ لَا تُحۡصُوهَآۗ إِنَّ ٱلۡإِنسَٰنَ لَظَلُومࣱ كَفَّارࣱ (14:34, part)
> وَإِن تَعُدُّواْ نِعۡمَةَ ٱللَّهِ لَا تُحۡصُوهَآۗ إِنَّ ٱللَّهَ لَغَفُورࣱ رَّحِيمࣱ (16:18)
> Saheeh: *…you could not enumerate them. Indeed, mankind is most unjust and ungrateful.* / *…Indeed, Allah is Forgiving and Merciful.*

- **Data.** A negated *aḥṣā* ("you cannot count") with a human subject occurs 3× (14:34, 16:18, 73:20). **Two close *ghafūr raḥīm*.**
- **Caution on 73:20.** It counts the night vigil (*lan tuḥṣūhu*), not the blessing (*lā tuḥṣūhā*). It shares only the verb and the ending: *you could not count it → He relented → **istaghfirū llāh** → ghafūr raḥīm*.
- **[interpretive]** The text never says "seek forgiveness for thanking too little". It sets the uncountable gift beside God's forgiveness (16:18) and, in the twin verse, beside human ingratitude (14:34). The joining is ours.

**(b) Forgiveness as an occasion of thanks**: *We pardoned you … that you may be grateful* (2:52). This is the only case among the 14 purpose clauses.

**(c) Thanks and *tawba* in one breath.**

> رَبِّ أَوۡزِعۡنِيٓ أَنۡ أَشۡكُرَ نِعۡمَتَكَ ٱلَّتِيٓ أَنۡعَمۡتَ عَلَيَّ وَعَلَىٰ وَٰلِدَيَّ وَأَنۡ أَعۡمَلَ صَٰلِحࣰا تَرۡضَىٰهُ وَأَصۡلِحۡ لِي فِي ذُرِّيَّتِيٓۖ إِنِّي تُبۡتُ إِلَيۡكَ وَإِنِّي مِنَ ٱلۡمُسۡلِمِينَ (46:15, part)
> Saheeh: *My Lord, enable me to be grateful for Your favor … and to work righteousness of which You will approve and make righteous for me my offspring. Indeed, I have repented to You, and indeed, I am of the Muslims.*

- ***Tubtu ilayka* occurs exactly twice, 46:15 and 7:143, both beside a `shkr` word.** In Moses's case the turning comes first, and God answers *be among the grateful* (7:144).
- At 4:146-147, *those who turn and set right* is followed by *what would God do with your punishment **if you thank and believe**?* 46:16 answers the prayer: *We overlook their misdeeds.*

**(d) The pair is God's names.**
- ***Ghafūr shakūr*** 3× (35:30, 35:34, 42:23), *ghafūr* always first. Also 64:17 (*He multiplies it and forgives you; God is Shakūr, Ḥalīm*) and 34:15 (*thank Him: a good land and a forgiving Lord*).
- **[interpretive]** On God's side, forgiving the bad and thanking the good form one pair. On the human side they are two acts, asking forgiveness for one's faults and thanking for His gifts, and they never share a sentence.

**(e) The istighfār synthesis** pairs istighfār with tawba, prior remembrance, tawḥīd and glorify-with-praise. Of its 15 commands, 13 carry a second imperative, and **none of them is *ushkurū***. **The two acts share neighbours, not sentences**: remembrance before, faith beside (4:147; 40:7), turning after.

---

## 4. Glorification and thanks

**Data.**
- `sbḥ` and `shkr` share 0 ayahs, with 5 contacts within ±2 ayahs:
  - **36:35-36**: *will they not then thank?* → *subḥāna lladhī khalaqa l-azwāja kullahā*;
  - **39:66-67**: *be among the grateful* → *subḥānahu … ʿammā yushrikūn*;
  - **21:79-80**: mountains glorify with David → *will you then be grateful?*;
  - also 7:143-144 and 17:1-3.
- At least 15 of the 41 *subḥān* ayahs end *above what they associate/ascribe* (*ʿammā*).
- All creation glorifies *bi-ḥamdihi* (17:44, which closes *ḥalīm ghafūr*; 13:13).

> لِتَسۡتَوُۥاْ عَلَىٰ ظُهُورِهِۦ ثُمَّ تَذۡكُرُواْ نِعۡمَةَ رَبِّكُمۡ إِذَا ٱسۡتَوَيۡتُمۡ عَلَيۡهِ وَتَقُولُواْ سُبۡحَٰنَ ٱلَّذِي سَخَّرَ لَنَا هَٰذَا وَمَا كُنَّا لَهُۥ مُقۡرِنِينَ ۝ وَإِنَّآ إِلَىٰ رَبِّنَا لَمُنقَلِبُونَ (43:13-14)
> Saheeh: *…then remember the favor of your Lord when you have settled upon them and say, "Exalted is He who has subjected this to us, and we could not have [otherwise] subdued it. And indeed we, to our Lord, will [surely] return."*

**The commanded words for remembering a blessing**: glorify the giver; ***disown your own power*** (*wa mā kunnā lahu muqrinīn*); name the return.

**The *mā kunnā* disavowal occurs exactly twice. The other is Paradise's *ḥamd*:** *we would never have been guided had God not guided us* (7:43). It inverts ingratitude's *I was given it only because of knowledge I have* (28:78, 39:49). The commonest relapse verb after rescue, *yushrik-* (5 of 9), is what *subḥānahu ʿammā yushrikūn* denies.

**Verdict.**
- **The Quran never calls tasbīḥ thanks.** It is a separate act: declaring God above partner, need or defect.
- **"Tasbīḥ is the spoken form of thanks" rests on one verse (43:13).** The other prescribed speech over a blessing is *ḥamd* (23:28).
- **[interpretive]** The text shows a division of labour. *Shukr* names the stance and the deed (7 imperatives; *work in thanks*, 34:13). *Ḥamd* is what is said, naming what He did. *Tasbīḥ* keeps the gift from being credited to anyone else, oneself included. **Glorification is not thanks. It is what keeps thanks from going wrong.**

---

## 5. The hereafter's last words

> دَعۡوَىٰهُمۡ فِيهَا سُبۡحَٰنَكَ ٱللَّهُمَّ وَتَحِيَّتُهُمۡ فِيهَا سَلَٰمࣱۚ وَءَاخِرُ دَعۡوَىٰهُمۡ أَنِ ٱلۡحَمۡدُ لِلَّهِ رَبِّ ٱلۡعَٰلَمِينَ (10:10)
> Saheeh: *Their call therein will be, "Exalted are You, O Allah," and their greeting therein will be, "Peace." And the last of their call will be, "Praise to Allah, Lord of the worlds!"*

**Data.**
- **10:10**: glorify → peace → **praise last**.
- **39:73-75**: the keepers' *salām* → the saved praise (*who fulfilled His promise*) → angels glorify with praise → judgment → *al-ḥamdu li-llāhi rabbi l-ʿālamīn*.
- **35:34-35**: praise (*who removed grief*) → ***our Lord is ghafūr shakūr*** → *who settled us … out of His bounty*.
- **52:26-28**, also Paradise speech: *God conferred favour on us (fa-manna)*, with no *ḥamd*.

**Absent.**
- **No istighfār and no *ighfir* inside Paradise.** The last recorded request for forgiveness is on the Day: *rabbanā atmim lanā nūranā wa-ghfir lanā* (66:8).
- **No human `shkr`.** *Shakūr* is God's, in their own mouths (35:34). Their effort is *mashkūr* (76:22).

**[interpretive]** Tasbīḥ survives unchanged, and *ḥamd* survives with the last word. Istighfār ends at the Day and survives only as the *name* *Ghafūr*, spoken in praise: the asking has become a statement that He forgave. Human thanks is absorbed into *ḥamd*, and the Thanker is now God. **The final speech is acknowledgement with no request in it.**

---

## 6. A practical sequence (*our suggestion*, built only from the verses above)

1. **Name the gift.** Remember it and speak of it (43:13; 2:152; 93:11).
2. **Glorify Him and disown your own power.** *Subḥāna lladhī sakhkhara lanā hādhā wa mā kunnā lahu muqrinīn* (43:13). Extending it beyond a mount is ours.
3. **Praise Him for what He did.** *Al-ḥamdu li-llāhi lladhī …* (23:28; 14:39; 35:34).
4. **Ask to thank in deed.** *Rabbi awziʿnī an ashkura niʿmataka llatī anʿamta ʿalayya wa ʿalā wālidayya wa an aʿmala ṣāliḥan tarḍāhu* (27:19; 46:15).
5. **Ask forgiveness.** *Rabbanā fa-ghfir lanā dhunūbanā wa kaffir ʿannā sayyiʾātinā* (3:193; command at 110:3).
6. **Turn.** *Innī tubtu ilayka wa innī mina l-muslimīn* (46:15). *Wa innā ilā rabbinā la-munqalibūn* (43:14).
7. **Close.** *Al-ḥamdu li-llāhi rabbi l-ʿālamīn* (10:10).
8. **Then use the gift.** Feed someone (22:36), or *work in thanks* (34:13).

**Times the text gives:** glorify with praise evening and morning, beside istighfār (40:55); istighfār before dawn (51:18); magnify and thank at the fast's end (2:185).

**Traditional, not Quranic:** the after-prayer ×33, *sayyid al-istighfār*, *subḥān Allāh wa bi-ḥamdihi* 100×, the prostration of thanks, and *Allāhu akbar* / *astaghfiru llāh* as fixed formulas. The Quran commands the acts; its istighfār model is a request, *rabbi ighfir*.

---

## Corrections

1. **40:55 is forgiveness first, then glorify with praise.** This corrects the ḥamd file (*"Order is fixed … in 40:55 and 110:3"*) and the istighfār synthesis (*"Glorify with praise, then ask: 4×"*). The correct figure is 3 of 4.
2. **Ḥamd file, "every recorded Paradise sentence … is a *ḥamd*":** 52:26-28 recalls *mann* with no *ḥamd*.
3. **73:20's "you cannot count it"** counts the night, not the blessing. It shares only the verb and the *ghafūr raḥīm* ending with 16:18.
4. **43:14's *return* is `qlb`, not `twb`.**
5. **New data:** shkr × istighfār = 0 even within ±5 ayahs; ḥmd × ḏkr = 0; *li-tukabbirū llāha ʿalā mā hadākum* 2×, both beside thanks.

## For practice

- When good arrives, glorify Him and say you could not have done it (43:13). That guards against *I got this by my own knowledge* (28:78).
- Then praise Him, naming what He did (23:28, 35:34).
- Ask to be *enabled* to thank in deed (46:15), then do the deed.
- After a gift, the commanded pair is *glorify with praise, and ask forgiveness* (110:3).
- Thanks meets forgiveness through turning back: after thanking, *innī tubtu ilayka* (46:15). What you were given cannot be counted, and the text answers that with *God is Forgiving, Merciful* (16:18).
- End as Paradise ends: *al-ḥamdu li-llāhi rabbi l-ʿālamīn* (10:10).
