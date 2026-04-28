# Translation Divergence Across Four English Translators

_Generated from 4 translations across 6236 ayahs._


Translators compared: Saheeh International (modern, conservative), Pickthall (1930, archaic), Khattab / The Clear Quran (2016, fluent), Arberry (1955, literary).


## Scoring methodology

For each of 6,236 ayahs we compute three components on the four English translations:


- **Token Jaccard (averaged over the 6 translator pairs).** Lowercase word-level Jaccard. Captures whether translators are using the same vocabulary at all. We invert this for the divergence score (`1 - jaccard`).

- **Lexical disagreement (normalized).** After stripping a hand-curated stopword list (articles, pronouns, archaic particles like _thee/thou/lo/verily_) and tokens of length <= 2, we count content words present in some translations but not all, divided by the size of the union. Captures noun/verb-level word choice disputes.

- **Length variance (coefficient of variation).** Standard deviation of word counts divided by mean. Captures cases where one translator expands a phrase or compresses it.


**Combined divergence score** = `0.50 * (1 - jaccard) + 0.35 * lex_disagreement_norm + 0.15 * length_cv`. Jaccard is weighted highest because it is the most stable signal (immune to inflated content words from a single verbose translator); length variance is weighted lowest because sentence expansion is partly stylistic, not semantic.


**Outlier translator.** For each ayah we compute mean Jaccard between each translator and the other three. The lowest-mean-Jaccard translator is flagged as outlier _only_ if the gap between it and the second-lowest is >= 0.05 (5pp), to suppress noise.


**Regimes.** _High_ = top 5% combined score (>= 0.7584). _Low_ = bottom 5% (<= 0.4830). _Mid_ = the rest.


---

## Top 30 highest-divergence ayahs

_Ayahs where the four translators agree least. These are research-priority candidates — the Arabic is doing something English struggles with. Filtered to ayahs with at least 4 tokens in every translation, to suppress noise from tiny disjointed letters._


### 100:5 (Al-Adiyat)  combined=0.850  jaccard=0.068  lex=13  len-cv=0.222  outlier=—

- **Saheeh International**: Arriving thereby in the center collectively,

- **Pickthall (1930)**: Cleaving, as one, the centre (of the foe),

- **Khattab / Clear Quran (2016)**: and penetrating into the heart of enemy lines

- **Arberry (1955)**: cleaving there with a host!


_Likely cause: general lexical/syntactic disagreement_


### 79:4 (An-Nazi'at)  combined=0.847  jaccard=0.114  lex=10  len-cv=0.360  outlier=pickthall

- **Saheeh International**: And those who race each other in a race

- **Pickthall (1930)**: By the angels hastening,

- **Khattab / Clear Quran (2016)**: and those taking the lead vigorously

- **Arberry (1955)**: and those that outstrip suddenly


_Likely cause: general lexical/syntactic disagreement; outlier: pickthall_


### 81:16 (At-Takwir)  combined=0.846  jaccard=0.093  lex=10  len-cv=0.286  outlier=—

- **Saheeh International**: Those that run [their courses] and disappear -

- **Pickthall (1930)**: The stars which rise and set,

- **Khattab / Clear Quran (2016)**: which travel and hide

- **Arberry (1955)**: the runners, the sinkers,


_Likely cause: cosmological imagery_


### 36:59 (Ya-Sin)  combined=0.845  jaccard=0.110  lex=19  len-cv=0.334  outlier=—

- **Saheeh International**: [Then He will say], "But stand apart today, you criminals.

- **Pickthall (1930)**: But avaunt ye, O ye guilty, this day!

- **Khattab / Clear Quran (2016)**: ˹Then the disbelievers will be told,˺ “Step away ˹from the believers˺ this Day, O wicked ones

- **Arberry (1955)**: 'Now keep yourselves apart, you sinners, upon this day!


_Likely cause: general lexical/syntactic disagreement_


### 77:33 (Al-Mursalat)  combined=0.845  jaccard=0.103  lex=11  len-cv=0.309  outlier=arberry

- **Saheeh International**: As if they were yellowish [black] camels.

- **Pickthall (1930)**: (Or) as it might be camels of bright yellow hue.

- **Khattab / Clear Quran (2016)**: and ˹as dark˺ as black camels.”

- **Arberry (1955)**: sparks like to golden herds.


_Likely cause: general lexical/syntactic disagreement; outlier: arberry_


### 23:67 (Al-Mu'minun)  combined=0.845  jaccard=0.076  lex=23  len-cv=0.216  outlier=—

- **Saheeh International**: In arrogance regarding it, conversing by night, speaking evil.

- **Pickthall (1930)**: In scorn thereof. Nightly did ye rave together.

- **Khattab / Clear Quran (2016)**: boasting of the Sacred House, and babbling ˹nonsense about the Quran˺ by night.”

- **Arberry (1955)**: waxing proud against it, talking foolish talk by night.'


_Likely cause: general lexical/syntactic disagreement_


### 56:19 (Al-Waqi'ah)  combined=0.842  jaccard=0.115  lex=14  len-cv=0.328  outlier=—

- **Saheeh International**: No headache will they have therefrom, nor will they be intoxicated -

- **Pickthall (1930)**: Wherefrom they get no aching of the head nor any madness,

- **Khattab / Clear Quran (2016)**: that will cause them neither headache nor intoxication

- **Arberry (1955)**: (no brows throbbing, no intoxication)


_Likely cause: major length disparity (one translator expands or compresses)_


### 37:160 (As-Saffat)  combined=0.841  jaccard=0.157  lex=12  len-cv=0.464  outlier=—

- **Saheeh International**: Except the chosen servants of Allah [who do not share in that sin].

- **Pickthall (1930)**: Save single-minded slaves of Allah.

- **Khattab / Clear Quran (2016)**: But not the chosen servants of Allah

- **Arberry (1955)**: except for God's sincere servants.


_Likely cause: theological vocabulary; major length disparity (one translator expands or compresses)_


### 51:8 (Adh-Dhariyat)  combined=0.840  jaccard=0.121  lex=13  len-cv=0.339  outlier=—

- **Saheeh International**: Indeed, you are in differing speech.

- **Pickthall (1930)**: Lo! ye, forsooth, are of various opinion (concerning the truth).

- **Khattab / Clear Quran (2016)**: Surely you are ˹lost˺ in conflicting views ˹regarding the truth˺

- **Arberry (1955)**: surely you speak at variance,


_Likely cause: general lexical/syntactic disagreement_


### 77:3 (Al-Mursalat)  combined=0.839  jaccard=0.114  lex=11  len-cv=0.304  outlier=—

- **Saheeh International**: And [by] the winds that spread [clouds]

- **Pickthall (1930)**: By those which cause earth's vegetation to revive;

- **Khattab / Clear Quran (2016)**: and those scattering ˹rainclouds˺ widely

- **Arberry (1955)**: by the scatterers scattering


_Likely cause: cosmological imagery_


### 20:107 (Ta-Ha)  combined=0.836  jaccard=0.080  lex=16  len-cv=0.171  outlier=saheeh

- **Saheeh International**: You will not see therein a depression or an elevation."

- **Pickthall (1930)**: Wherein thou seest neither curve nor ruggedness.

- **Khattab / Clear Quran (2016)**: with neither depressions nor elevations to be seen.”

- **Arberry (1955)**: wherein thou wilt see no crookedness neither any curving.'


_Likely cause: general lexical/syntactic disagreement; outlier: saheeh_


### 69:23 (Al-Haqqah)  combined=0.835  jaccard=0.076  lex=12  len-cv=0.153  outlier=—

- **Saheeh International**: Its [fruit] to be picked hanging near.

- **Pickthall (1930)**: Whereof the clusters are in easy reach.

- **Khattab / Clear Quran (2016)**: whose fruit will hang within reach

- **Arberry (1955)**: its clusters nigh to gather.


_Likely cause: general lexical/syntactic disagreement_


### 56:2 (Al-Waqi'ah)  combined=0.834  jaccard=0.092  lex=10  len-cv=0.202  outlier=—

- **Saheeh International**: There is, at its occurrence, no denial.

- **Pickthall (1930)**: There is no denying that it will befall -

- **Khattab / Clear Quran (2016)**: then no one can deny it has come

- **Arberry (1955)**: (and none denies its descending)


_Likely cause: general lexical/syntactic disagreement_


### 77:4 (Al-Mursalat)  combined=0.834  jaccard=0.128  lex=11  len-cv=0.320  outlier=—

- **Saheeh International**: And those [angels] who bring criterion

- **Pickthall (1930)**: By those who winnow with a winnowing,

- **Khattab / Clear Quran (2016)**: And ˹by˺ those ˹angels˺ fully distinguishing ˹truth from falsehood˺

- **Arberry (1955)**: and the severally severing


_Likely cause: general lexical/syntactic disagreement_


### 92:19 (Al-Layl)  combined=0.832  jaccard=0.128  lex=15  len-cv=0.306  outlier=—

- **Saheeh International**: And not [giving] for anyone who has [done him] a favor to be rewarded

- **Pickthall (1930)**: And none hath with him any favour for reward,

- **Khattab / Clear Quran (2016)**: not in return for someone’s favours

- **Arberry (1955)**: and confers no favour on any man for recompense,


_Likely cause: major length disparity (one translator expands or compresses)_


### 79:3 (An-Nazi'at)  combined=0.832  jaccard=0.107  lex=10  len-cv=0.236  outlier=—

- **Saheeh International**: And [by] those who glide [as if] swimming

- **Pickthall (1930)**: By the lone stars floating,

- **Khattab / Clear Quran (2016)**: and those gliding ˹through heavens˺ swiftly

- **Arberry (1955)**: by those that swim serenely


_Likely cause: cosmological imagery_


### 25:46 (Al-Furqan)  combined=0.830  jaccard=0.100  lex=16  len-cv=0.204  outlier=khattab

- **Saheeh International**: Then We hold it in hand for a brief grasp.

- **Pickthall (1930)**: Then We withdraw it unto Us, a gradual withdrawal?

- **Khattab / Clear Quran (2016)**: causing the shade to retreat gradually

- **Arberry (1955)**: thereafter We seize it to Ourselves, drawing it gently.


_Likely cause: general lexical/syntactic disagreement; outlier: khattab_


### 75:25 (Al-Qiyamah)  combined=0.830  jaccard=0.128  lex=17  len-cv=0.295  outlier=—

- **Saheeh International**: Expecting that there will be done to them [something] backbreaking.

- **Pickthall (1930)**: Thou wilt know that some great disaster is about to fall on them.

- **Khattab / Clear Quran (2016)**: anticipating something devastating to befall them

- **Arberry (1955)**: thou mightest think the Calamity has been wreaked on them.


_Likely cause: rare lexicon_


### 51:9 (Adh-Dhariyat)  combined=0.830  jaccard=0.139  lex=12  len-cv=0.327  outlier=arberry

- **Saheeh International**: Deluded away from the Qur'an is he who is deluded.

- **Pickthall (1930)**: He is made to turn away from it who is (himself) averse.

- **Khattab / Clear Quran (2016)**: Only those ˹destined to be˺ deluded are turned away from it

- **Arberry (1955)**: and perverted therefrom are some.


_Likely cause: major length disparity (one translator expands or compresses); outlier: arberry_


### 52:12 (At-Tur)  combined=0.829  jaccard=0.087  lex=12  len-cv=0.153  outlier=arberry

- **Saheeh International**: Who are in [empty] discourse amusing themselves.

- **Pickthall (1930)**: Who play in talk of grave matters;

- **Khattab / Clear Quran (2016)**: those who amuse themselves with falsehood

- **Arberry (1955)**: such as play at plunging,


_Likely cause: general lexical/syntactic disagreement; outlier: arberry_


### 38:11 (Sad)  combined=0.824  jaccard=0.123  lex=15  len-cv=0.233  outlier=—

- **Saheeh International**: [They are but] soldiers [who will be] defeated there among the companies [of disbelievers].

- **Pickthall (1930)**: A defeated host are (all) the factions that are there.

- **Khattab / Clear Quran (2016)**: This is just another ˹enemy˺ force bound for defeat out there

- **Arberry (1955)**: A very host of parties is routed there!


_Likely cause: general lexical/syntactic disagreement_


### 79:2 (An-Nazi'at)  combined=0.823  jaccard=0.125  lex=11  len-cv=0.236  outlier=pickthall

- **Saheeh International**: And [by] those who remove with ease

- **Pickthall (1930)**: By the meteors rushing,

- **Khattab / Clear Quran (2016)**: and those pulling out ˹good souls˺ gently

- **Arberry (1955)**: and those that draw out violently,


_Likely cause: theological vocabulary; outlier: pickthall_


### 91:11 (Ash-Shams)  combined=0.822  jaccard=0.129  lex=17  len-cv=0.245  outlier=—

- **Saheeh International**: Thamud denied [their prophet] by reason of their transgression,

- **Pickthall (1930)**: (The tribe of) Thamud denied (the truth) in their rebellious pride,

- **Khattab / Clear Quran (2016)**: Thamûd rejected ˹the truth˺ out of arrogance

- **Arberry (1955)**: Thamood cried lies in their insolence


_Likely cause: theological vocabulary_


### 37:12 (As-Saffat)  combined=0.822  jaccard=0.162  lex=12  len-cv=0.354  outlier=—

- **Saheeh International**: But you wonder, while they mock,

- **Pickthall (1930)**: Nay, but thou dost marvel when they mock

- **Khattab / Clear Quran (2016)**: In fact, you are astonished ˹by their denial˺, while they ridicule ˹you˺

- **Arberry (1955)**: Nay, thou marvellest; and they scoff


_Likely cause: general lexical/syntactic disagreement_


### 53:53 (An-Najm)  combined=0.820  jaccard=0.204  lex=14  len-cv=0.478  outlier=—

- **Saheeh International**: And the overturned towns He hurled down

- **Pickthall (1930)**: And Al-Mu'tafikah He destroyed

- **Khattab / Clear Quran (2016)**: And ˹it was˺ He ˹Who˺ turned the cities ˹of Sodom and Gomorrah˺ upside down

- **Arberry (1955)**: and the Subverted City He also overthrew,


_Likely cause: major length disparity (one translator expands or compresses)_


### 74:18 (Al-Muddaththir)  combined=0.820  jaccard=0.180  lex=10  len-cv=0.396  outlier=—

- **Saheeh International**: Indeed, he thought and deliberated.

- **Pickthall (1930)**: For lo! he did consider; then he planned -

- **Khattab / Clear Quran (2016)**: for he contemplated and determined ˹a degrading label for the Quran˺

- **Arberry (1955)**: Lo! He reflected, and determined --


_Likely cause: general lexical/syntactic disagreement_


### 77:30 (Al-Mursalat)  combined=0.820  jaccard=0.153  lex=12  len-cv=0.306  outlier=—

- **Saheeh International**: Proceed to a shadow [of smoke] having three columns

- **Pickthall (1930)**: Depart unto the shadow falling threefold,

- **Khattab / Clear Quran (2016)**: Proceed into the shade ˹of smoke˺ which rises in three columns

- **Arberry (1955)**: Depart to a triple-massing shadow


_Likely cause: general lexical/syntactic disagreement_


### 43:77 (Az-Zukhruf)  combined=0.819  jaccard=0.202  lex=18  len-cv=0.469  outlier=arberry

- **Saheeh International**: And they will call, "O Malik, let your Lord put an end to us!" He will say, "Indeed, you will remain."

- **Pickthall (1930)**: And they cry: O master! Let thy Lord make an end of us. He saith: Lo! here ye must remain.

- **Khattab / Clear Quran (2016)**: They will cry, “O Mâlik! Let your Lord finish us off.” He will answer, “You are definitely here to stay.”

- **Arberry (1955)**: And they shall call, 'O


_Likely cause: theological vocabulary; major length disparity (one translator expands or compresses); outlier: arberry_


### 15:76 (Al-Hijr)  combined=0.817  jaccard=0.099  lex=13  len-cv=0.109  outlier=—

- **Saheeh International**: And indeed, those cities are [situated] on an established road.

- **Pickthall (1930)**: And lo! it is upon a road still uneffaced.

- **Khattab / Clear Quran (2016)**: Their ruins still lie along a known route

- **Arberry (1955)**: surely it is on a way yet remaining;


_Likely cause: general lexical/syntactic disagreement_


### 20:62 (Ta-Ha)  combined=0.816  jaccard=0.131  lex=19  len-cv=0.212  outlier=—

- **Saheeh International**: So they disputed over their affair among themselves and concealed their private conversation.

- **Pickthall (1930)**: Then they debated one with another what they must do, and they kept their counsel secret.

- **Khattab / Clear Quran (2016)**: So the magicians disputed the matter among themselves, conversing privately

- **Arberry (1955)**: And they disputed upon their plan between them, and communed secretly


_Likely cause: general lexical/syntactic disagreement_


---

## Top 30 lowest-divergence ayahs (most stable English)

_Ayahs where translators agree most. Confirms the 'stable English' set: short formulas, isolated disjointed letters, simple narrative beats._


### 7:122 (Al-A'raf)  combined=0.000  jaccard=1.000

- **Saheeh International**: The Lord of Moses and Aaron."

- **Pickthall (1930)**: The Lord of Moses and Aaron.

- **Khattab / Clear Quran (2016)**: the Lord of Moses and Aaron.”

- **Arberry (1955)**: the Lord of Moses and Aaron.


### 20:30 (Ta-Ha)  combined=0.000  jaccard=1.000

- **Saheeh International**: Aaron, my brother.

- **Pickthall (1930)**: Aaron, my brother.

- **Khattab / Clear Quran (2016)**: Aaron, my brother

- **Arberry (1955)**: Aaron, my brother;


### 89:1 (Al-Fajr)  combined=0.000  jaccard=1.000

- **Saheeh International**: By the dawn

- **Pickthall (1930)**: By the Dawn

- **Khattab / Clear Quran (2016)**: By the dawn

- **Arberry (1955)**: By the dawn


### 90:9 (Al-Balad)  combined=0.013  jaccard=1.000

- **Saheeh International**: And a tongue and two lips?

- **Pickthall (1930)**: And a tongue and two lips,

- **Khattab / Clear Quran (2016)**: a tongue, and two lips

- **Arberry (1955)**: and a tongue, and two lips,


### 26:48 (Ash-Shu'ara)  combined=0.048  jaccard=0.929

- **Saheeh International**: The Lord of Moses and Aaron."

- **Pickthall (1930)**: The Lord of Moses and Aaron.

- **Khattab / Clear Quran (2016)**: the Lord of Moses and Aaron.”

- **Arberry (1955)**: the Lord of Moses and Aaron.'


### 26:66 (Ash-Shu'ara)  combined=0.083  jaccard=0.833

- **Saheeh International**: Then We drowned the others.

- **Pickthall (1930)**: And We drowned the others.

- **Khattab / Clear Quran (2016)**: Then We drowned the others

- **Arberry (1955)**: then We drowned the others.


### 78:8 (An-Naba)  combined=0.096  jaccard=0.849

- **Saheeh International**: And We created you in pairs

- **Pickthall (1930)**: And We have created you in pairs,

- **Khattab / Clear Quran (2016)**: and created you in pairs

- **Arberry (1955)**: And We created you in pairs,


### 52:1 (At-Tur)  combined=0.125  jaccard=0.750

- **Saheeh International**: By the mount

- **Pickthall (1930)**: By the Mount,

- **Khattab / Clear Quran (2016)**: By Mount Ṭûr

- **Arberry (1955)**: By the Mount


### 89:2 (Al-Fajr)  combined=0.141  jaccard=0.767

- **Saheeh International**: And [by] ten nights

- **Pickthall (1930)**: And ten nights,

- **Khattab / Clear Quran (2016)**: and the ten nights

- **Arberry (1955)**: and ten nights,


### 36:4 (Ya-Sin)  combined=0.167  jaccard=0.667

- **Saheeh International**: On a straight path.

- **Pickthall (1930)**: On a straight path,

- **Khattab / Clear Quran (2016)**: upon the Straight Path

- **Arberry (1955)**: on a straight path;


### 52:15 (At-Tur)  combined=0.169  jaccard=0.724

- **Saheeh International**: Then is this magic, or do you not see?

- **Pickthall (1930)**: Is this magic, or do ye not see?

- **Khattab / Clear Quran (2016)**: Is this magic, or do you not see

- **Arberry (1955)**: What, is this magic, or is it you that do not see?


### 73:15 (Al-Muzzammil)  combined=0.180  jaccard=0.646

- **Saheeh International**: Indeed, We have sent to you a Messenger as a witness upon you just as We sent to Pharaoh a messenger.

- **Pickthall (1930)**: Lo! We have sent unto you a messenger as witness against you, even as We sent unto Pharaoh a messenger.

- **Khattab / Clear Quran (2016)**: Indeed, We have sent to you a messenger as a witness over you, just as We sent a messenger to Pharaoh

- **Arberry (1955)**: Surely We have sent unto you a Messenger as a witness over you, even as We sent to Pharaoh a Messenger,


### 88:25 (Al-Ghashiyah)  combined=0.196  jaccard=0.607

- **Saheeh International**: Indeed, to Us is their return.

- **Pickthall (1930)**: Lo! unto Us is their return

- **Khattab / Clear Quran (2016)**: Surely to Us is their return

- **Arberry (1955)**: Truly, to Us is their return;


### 74:2 (Al-Muddaththir)  combined=0.202  jaccard=0.875

- **Saheeh International**: Arise and warn

- **Pickthall (1930)**: Arise and warn!

- **Khattab / Clear Quran (2016)**: Arise and warn ˹all˺

- **Arberry (1955)**: arise, and warn!


### 80:35 (Abasa)  combined=0.208  jaccard=0.639

- **Saheeh International**: And his mother and his father

- **Pickthall (1930)**: And his mother and his father

- **Khattab / Clear Quran (2016)**: and ˹even˺ their mother and father

- **Arberry (1955)**: his mother, his father,


### 95:1 (At-Tin)  combined=0.211  jaccard=0.857

- **Saheeh International**: By the fig and the olive

- **Pickthall (1930)**: By the fig and the olive,

- **Khattab / Clear Quran (2016)**: By the fig and the olive ˹of Jerusalem˺

- **Arberry (1955)**: By the fig and the olive


### 95:2 (At-Tin)  combined=0.212  jaccard=0.625

- **Saheeh International**: And [by] Mount Sinai

- **Pickthall (1930)**: By Mount Sinai,

- **Khattab / Clear Quran (2016)**: and Mount Sinai

- **Arberry (1955)**: and the Mount Sinai


### 74:51 (Al-Muddaththir)  combined=0.217  jaccard=0.800

- **Saheeh International**: Fleeing from a lion?

- **Pickthall (1930)**: Fleeing from a lion?

- **Khattab / Clear Quran (2016)**: fleeing from a lion

- **Arberry (1955)**: fleeing -- before a lion?


### 29:57 (Al-Ankabut)  combined=0.221  jaccard=0.686

- **Saheeh International**: Every soul will taste death. Then to Us will you be returned.

- **Pickthall (1930)**: Every soul will taste of death. Then unto Us ye will be returned.

- **Khattab / Clear Quran (2016)**: Every soul will taste death, then to Us you will ˹all˺ be returned

- **Arberry (1955)**: Every soul shall taste of death; then unto Us you shall be returned.


### 97:3 (Al-Qadr)  combined=0.226  jaccard=0.849

- **Saheeh International**: The Night of Decree is better than a thousand months.

- **Pickthall (1930)**: The Night of Power is better than a thousand months.

- **Khattab / Clear Quran (2016)**: The Night of Glory is better than a thousand months

- **Arberry (1955)**: The Night of Power is better than a thousand months;


### 53:49 (An-Najm)  combined=0.230  jaccard=0.818

- **Saheeh International**: And that it is He who is the Lord of Sirius

- **Pickthall (1930)**: And that He it is Who is the Lord of Sirius;

- **Khattab / Clear Quran (2016)**: And He alone is the Lord of Sirius

- **Arberry (1955)**: and that it is He who is the Lord of Sirius,


### 77:26 (Al-Mursalat)  combined=0.249  jaccard=0.762

- **Saheeh International**: Of the living and the dead?

- **Pickthall (1930)**: Both for the living and the dead,

- **Khattab / Clear Quran (2016)**: for the living and the dead

- **Arberry (1955)**: for the living and for the dead?


### 91:1 (Ash-Shams)  combined=0.251  jaccard=0.756

- **Saheeh International**: By the sun and its brightness

- **Pickthall (1930)**: By the sun and his brightness,

- **Khattab / Clear Quran (2016)**: By the sun and its brightness

- **Arberry (1955)**: By the sun and his morning brightness


### 113:2 (Al-Falaq)  combined=0.269  jaccard=0.696

- **Saheeh International**: From the evil of that which He created

- **Pickthall (1930)**: From the evil of that which He created;

- **Khattab / Clear Quran (2016)**: from the evil of whatever He has created

- **Arberry (1955)**: from the evil of what He has created,


### 19:22 (Maryam)  combined=0.272  jaccard=0.819

- **Saheeh International**: So she conceived him, and she withdrew with him to a remote place.

- **Pickthall (1930)**: And she conceived him, and she withdrew with him to a far place.

- **Khattab / Clear Quran (2016)**: So she conceived him and withdrew with him to a remote place

- **Arberry (1955)**: So she conceived him, and withdrew with him to a distant place.


### 23:15 (Al-Mu'minun)  combined=0.277  jaccard=0.481

- **Saheeh International**: Then indeed, after that you are to die.

- **Pickthall (1930)**: Then lo! after that ye surely die.

- **Khattab / Clear Quran (2016)**: After that you will surely die

- **Arberry (1955)**: Then after that you shall surely die,


### 83:25 (Al-Mutaffifin)  combined=0.282  jaccard=0.590

- **Saheeh International**: They will be given to drink [pure] wine [which was] sealed.

- **Pickthall (1930)**: They are given to drink of a pure wine, sealed,

- **Khattab / Clear Quran (2016)**: They will be given a drink of sealed, pure wine

- **Arberry (1955)**: as they are given to drink of a wine sealed


### 106:3 (Quraysh)  combined=0.291  jaccard=0.786

- **Saheeh International**: Let them worship the Lord of this House,

- **Pickthall (1930)**: So let them worship the Lord of this House,

- **Khattab / Clear Quran (2016)**: let them worship the Lord of this ˹Sacred˺ House

- **Arberry (1955)**: So let them serve the Lord of this House


### 20:1 (Ta-Ha)  combined=0.293  jaccard=0.500

- **Saheeh International**: Ta, Ha.

- **Pickthall (1930)**: Ta. Ha.

- **Khattab / Clear Quran (2016)**: Ṭâ-Hâ

- **Arberry (1955)**: Ta Ha


### 85:2 (Al-Buruj)  combined=0.293  jaccard=0.695

- **Saheeh International**: And [by] the promised Day

- **Pickthall (1930)**: And by the Promised Day.

- **Khattab / Clear Quran (2016)**: and the promised Day ˹of Judgment˺

- **Arberry (1955)**: by the promised day,


---

## Outlier-translator distribution

Across all 6,236 ayahs we flag a translator as outlier only when its mean Jaccard to the other three is at least 5 percentage points below the next-lowest translator.


| Translator | Outlier count (all ayahs) | Share of all ayahs | Outlier count (high-divergence regime) | Share of high-divergence |

|---|---:|---:|---:|---:|

| _(no clear outlier)_ | 3910 | 62.7% | 185 | 59.3% |

| saheeh | 119 | 1.9% | 8 | 2.6% |

| pickthall | 613 | 9.8% | 27 | 8.7% |

| khattab | 831 | 13.3% | 54 | 17.3% |

| arberry | 763 | 12.2% | 38 | 12.2% |


**Across the whole Quran**, _khattab_ is flagged as the lone outlier most often (831 ayahs, 13.3% of all ayahs), ahead of the next translator by 1.1 percentage points.


**Within the high-divergence regime** (top 5% of ayahs), _khattab_ is the lone outlier in 54 of 312 ayahs (17.3%). Note that 185 of the high-divergence ayahs (59.3%) have no clear outlier — meaning all four translations diverge from each other roughly equally, rather than one translator going its own way. Those are arguably the most 'genuinely contested' verses.


---

## Surahs with the highest average divergence

Ranked by mean combined-divergence across all ayahs in the surah.


| Rank | Surah | Avg combined | # Ayahs |

|---:|---|---:|---:|

| 1 | 110 An-Nasr | 0.704 | 3 |

| 2 | 112 Al-Ikhlas | 0.701 | 4 |

| 3 | 103 Al-Asr | 0.700 | 3 |

| 4 | 102 At-Takathur | 0.699 | 8 |

| 5 | 79 An-Nazi'at | 0.693 | 46 |

| 6 | 100 Al-Adiyat | 0.692 | 11 |

| 7 | 104 Al-Humazah | 0.689 | 9 |

| 8 | 88 Al-Ghashiyah | 0.685 | 26 |

| 9 | 68 Al-Qalam | 0.685 | 52 |

| 10 | 56 Al-Waqi'ah | 0.684 | 96 |

| 11 | 82 Al-Infitar | 0.680 | 19 |

| 12 | 80 Abasa | 0.675 | 42 |

| 13 | 70 Al-Ma'arij | 0.674 | 44 |

| 14 | 94 Ash-Sharh | 0.668 | 8 |

| 15 | 81 At-Takwir | 0.668 | 29 |


And the most-stable surahs (lowest average divergence):


| Rank | Surah | Avg combined | # Ayahs |

|---:|---|---:|---:|

| 1 | 113 Al-Falaq | 0.435 | 5 |

| 2 | 97 Al-Qadr | 0.493 | 5 |

| 3 | 95 At-Tin | 0.512 | 8 |

| 4 | 114 An-Nas | 0.523 | 6 |

| 5 | 106 Quraysh | 0.526 | 4 |

| 6 | 1 Al-Fatihah | 0.542 | 7 |

| 7 | 111 Al-Masad | 0.574 | 5 |

| 8 | 61 As-Saff | 0.575 | 14 |

| 9 | 63 Al-Munafiqun | 0.587 | 11 |

| 10 | 96 Al-Alaq | 0.592 | 19 |

| 11 | 66 At-Tahrim | 0.596 | 12 |

| 12 | 45 Al-Jathiyah | 0.596 | 37 |

| 13 | 64 At-Taghabun | 0.598 | 18 |

| 14 | 23 Al-Mu'minun | 0.601 | 118 |

| 15 | 108 Al-Kawthar | 0.602 | 3 |


---

## Categories of high-divergence ayahs

Categories overlap (an ayah can be tagged with several). Counts among the 312 high-divergence ayahs:


- **theological**: 71 (23%)

- **very short / disjointed letters**: 70 (22%)

- **eschatological**: 24 (8%)

- **cosmological**: 19 (6%)

- **legal/ritual**: 4 (1%)


This distribution suggests divergence is driven less by any single category and more by a combination of theological/cosmological vocabulary and short, oblique formulas (oaths, disjointed letters, dense legal injunctions).


---

## Surprises

### Low-divergence ayahs in heavyweight theological territory

These ayahs sit in the bottom 5% of divergence yet contain heavyweight terms (spirit, throne, decree, guidance/misguidance, covenant). The English translation tradition appears to have settled on a stable rendering despite the conceptual weight.


- **7:54 (Al-A'raf)** — Indeed, your Lord is Allah, who created the heavens and earth in six days and then established Himself above the Throne. He covers the night with the day, [another night] chasing it rapidly; and [He created] the sun, the moon, and the stars, subjected by His command. Unquestionably, His is the creation and the command; blessed is Allah, Lord of the worlds.

- **7:154 (Al-A'raf)** — And when the anger subsided in Moses, he took up the tablets; and in their inscription was guidance and mercy for those who are fearful of their Lord.

- **17:42 (Al-Isra)** — Say, [O Muhammad], "If there had been with Him [other] gods, as they say, then they [each] would have sought to the Owner of the Throne a way."

- **18:13 (Al-Kahf)** — It is We who relate to you, [O Muhammad], their story in truth. Indeed, they were youths who believed in their Lord, and We increased them in guidance.

- **23:86 (Al-Mu'minun)** — Say, "Who is Lord of the seven heavens and Lord of the Great Throne?"

- **27:23 (An-Naml)** — Indeed, I found [there] a woman ruling them, and she has been given of all things, and she has a great throne.

- **27:77 (An-Naml)** — And indeed, it is guidance and mercy for the believers.

- **31:3 (Luqman)** — As guidance and mercy for the doers of good


### High-divergence ayahs in apparently mundane territory

These ayahs sit in the top 5% of divergence but do not match obvious theological/legal keyword flags. They may reveal hidden complexity — rare verbs, ambiguous pronouns, or narrative idioms that don't translate cleanly.


- **100:5 (Al-Adiyat)** — Saheeh: "Arriving thereby in the center collectively,"; Arberry: "cleaving there with a host!"

- **79:4 (An-Nazi'at)** — Saheeh: "And those who race each other in a race"; Arberry: "and those that outstrip suddenly"

- **81:16 (At-Takwir)** — Saheeh: "Those that run [their courses] and disappear -"; Arberry: "the runners, the sinkers,"

- **36:59 (Ya-Sin)** — Saheeh: "[Then He will say], "But stand apart today, you criminals."; Arberry: "'Now keep yourselves apart, you sinners, upon this day!"

- **77:33 (Al-Mursalat)** — Saheeh: "As if they were yellowish [black] camels."; Arberry: "sparks like to golden herds."

- **23:67 (Al-Mu'minun)** — Saheeh: "In arrogance regarding it, conversing by night, speaking evil."; Arberry: "waxing proud against it, talking foolish talk by night.'"

- **56:19 (Al-Waqi'ah)** — Saheeh: "No headache will they have therefrom, nor will they be intoxicated -"; Arberry: "(no brows throbbing, no intoxication)"

- **37:160 (As-Saffat)** — Saheeh: "Except the chosen servants of Allah [who do not share in that sin]."; Arberry: "except for God's sincere servants."

