# Per-Surah Cluster Signatures

Structural fingerprint of each surah, computed from 666 root clusters of which 15 carry thematic names. 
Each surah's vocabulary is decomposed into cluster shares so that 'what is this surah about' becomes a measurement, not a guess.

- **Source:** `data/morphology/words.jsonl` (77,429 words; ~52K root-bearing).
- **Cluster map:** `notes/full-quran-graph/clusters.json` (666 clusters; 15 named).
- **Concentration:** Gini over per-cluster word counts. 0 = perfectly spread, 1 = fully mono-thematic.

## Headline findings

### Most mono-thematic surahs (highest Gini)

Surahs whose root vocabulary collapses heavily onto a few clusters.

| # | Surah | Revelation | Ayāt | Root words | Gini | Dominant cluster | Dom. share |
|---|---|---|---|---|---|---|---|
| 4 | An-Nisaa | Medinan | 176 | 2462 | 0.833 | Revelation, Speech & Disbelief | 25.6% |
| 2 | Al-Baqara | Medinan | 286 | 3884 | 0.832 | Revelation, Speech & Disbelief | 28.9% |
| 3 | Aal-i-Imraan | Medinan | 200 | 2274 | 0.821 | Revelation, Speech & Disbelief | 31.0% |
| 6 | Al-An'aam | Meccan | 165 | 1946 | 0.814 | Revelation, Speech & Disbelief | 37.4% |
| 7 | Al-A'raaf | Meccan | 206 | 2144 | 0.812 | Revelation, Speech & Disbelief | 35.6% |
| 9 | At-Tawba | Medinan | 129 | 1646 | 0.805 | Revelation, Speech & Disbelief | 22.5% |
| 5 | Al-Maaida | Medinan | 120 | 1798 | 0.805 | Revelation, Speech & Disbelief | 28.3% |
| 11 | Hud | Meccan | 123 | 1162 | 0.797 | Revelation, Speech & Disbelief | 35.4% |
| 26 | Ash-Shu'araa | Meccan | 227 | 821 | 0.794 | Revelation, Speech & Disbelief | 43.4% |
| 10 | Yunus | Meccan | 109 | 1129 | 0.792 | Revelation, Speech & Disbelief | 41.1% |
| 12 | Yusuf | Meccan | 111 | 1126 | 0.782 | Revelation, Speech & Disbelief | 39.9% |
| 18 | Al-Kahf | Meccan | 110 | 1057 | 0.778 | Revelation, Speech & Disbelief | 32.6% |
| 27 | An-Naml | Meccan | 93 | 737 | 0.776 | Revelation, Speech & Disbelief | 40.8% |
| 40 | Ghafir | Meccan | 85 | 788 | 0.773 | Revelation, Speech & Disbelief | 34.4% |
| 16 | An-Nahl | Meccan | 128 | 1184 | 0.772 | Revelation, Speech & Disbelief | 27.1% |

### Most poly-thematic surahs (lowest Gini)

Surahs where root vocabulary is spread across many clusters more evenly.

| # | Surah | Revelation | Ayāt | Root words | Gini | Dominant cluster | Dom. share |
|---|---|---|---|---|---|---|---|
| 111 | Al-Masad | Meccan | 5 | 17 | 0.102 | Allegiance & the Object of Worship | 11.8% |
| 106 | Quraish | Meccan | 4 | 12 | 0.133 | (unnamed #78) | 16.7% |
| 112 | Al-Ikhlaas | Meccan | 4 | 10 | 0.133 | Revelation, Speech & Disbelief | 20.0% |
| 105 | Al-Fil | Meccan | 5 | 18 | 0.183 | Revelation, Speech & Disbelief | 16.7% |
| 104 | Al-Humaza | Meccan | 9 | 21 | 0.188 | The Believers' Reward | 14.3% |
| 107 | Al-Maa'un | Meccan | 7 | 14 | 0.222 | (unnamed #157) | 21.4% |
| 103 | Al-Asr | Meccan | 3 | 10 | 0.233 | The Believers' Reward | 30.0% |
| 100 | Al-Aadiyaat | Meccan | 11 | 24 | 0.260 | Revelation, Speech & Disbelief | 25.0% |
| 94 | Ash-Sharh | Meccan | 8 | 16 | 0.263 | (unnamed #145) | 25.0% |
| 110 | An-Nasr | Medinan | 3 | 16 | 0.292 | Revelation, Speech & Disbelief | 25.0% |
| 113 | Al-Falaq | Meccan | 5 | 15 | 0.311 | Revelation, Speech & Disbelief | 26.7% |
| 93 | Ad-Dhuhaa | Meccan | 11 | 28 | 0.321 | Revelation, Speech & Disbelief | 21.4% |
| 87 | Al-A'laa | Meccan | 19 | 49 | 0.332 | Revelation, Speech & Disbelief | 14.3% |
| 88 | Al-Ghaashiya | Meccan | 26 | 60 | 0.341 | Revelation, Speech & Disbelief | 13.3% |
| 99 | Az-Zalzala | Medinan | 8 | 27 | 0.344 | The Believers' Reward | 18.5% |

### Highest single-cluster domination (largest dominant share)

Surahs where the top cluster alone owns a huge fraction of the vocabulary.

| # | Surah | Revelation | Ayāt | Root words | Dominant cluster | Dom. share |
|---|---|---|---|---|---|---|
| 109 | Al-Kaafiroon | Meccan | 6 | 12 | Allegiance & the Object of Worship | 66.7% |
| 102 | At-Takaathur | Meccan | 8 | 16 | Revelation, Speech & Disbelief | 50.0% |
| 55 | Ar-Rahmaan | Medinan | 78 | 256 | Revelation, Speech & Disbelief | 46.5% |
| 114 | An-Naas | Meccan | 6 | 16 | Revelation, Speech & Disbelief | 43.8% |
| 26 | Ash-Shu'araa | Meccan | 227 | 821 | Revelation, Speech & Disbelief | 43.4% |
| 10 | Yunus | Meccan | 109 | 1129 | Revelation, Speech & Disbelief | 41.1% |
| 15 | Al-Hijr | Meccan | 99 | 410 | Revelation, Speech & Disbelief | 41.0% |
| 27 | An-Naml | Meccan | 93 | 737 | Revelation, Speech & Disbelief | 40.8% |
| 43 | Az-Zukhruf | Meccan | 89 | 512 | Revelation, Speech & Disbelief | 40.6% |
| 12 | Yusuf | Meccan | 111 | 1126 | Revelation, Speech & Disbelief | 39.9% |
| 34 | Saba | Meccan | 54 | 544 | Revelation, Speech & Disbelief | 39.7% |
| 45 | Al-Jaathiya | Meccan | 37 | 320 | Revelation, Speech & Disbelief | 39.1% |
| 28 | Al-Qasas | Meccan | 88 | 882 | Revelation, Speech & Disbelief | 38.5% |
| 46 | Al-Ahqaf | Meccan | 35 | 405 | Revelation, Speech & Disbelief | 38.5% |
| 6 | Al-An'aam | Meccan | 165 | 1946 | Revelation, Speech & Disbelief | 37.4% |

## Named-cluster ubiquity (out of 114 surahs)

How widely each thematic cluster spreads. 'Universal' clusters are background motifs; rare ones are surah-specific signatures.

| Cluster | Name | Surahs present |
|---|---|---|
| 4 | Revelation, Speech & Disbelief | 114 |
| 8 | Allegiance & the Object of Worship | 105 |
| 0 | The Believers' Reward | 102 |
| 19 | Household Law & Lineage | 100 |
| 5 | The Commanded Self | 98 |
| 17 | Bodily Purity & Prayer | 93 |
| 43 | Divine Will & Dominion | 92 |
| 90 | Sin–Mercy Economy | 90 |
| 75 | Witnessing the Visible Sign | 88 |
| 62 | The Prepared Fire | 84 |
| 77 | Creation & the Appointed Term | 84 |
| 96 | Dunya vs. Ākhirah | 83 |
| 7 | Sea-Rescue / Bounty / Gratitude | 76 |
| 66 | Jihād fī Sabīl Allāh | 75 |
| 11 | Vegetative Signs / Reflective Gaze | 69 |

**Universal clusters** (>=100 surahs): `Revelation, Speech & Disbelief`, `Allegiance & the Object of Worship`, `The Believers' Reward`, `Household Law & Lineage`.

## Top surahs per named cluster

For each thematic cluster, the surahs where it owns the largest share of vocabulary. 
Use this to find 'the most X-dense surah' at a glance.

### Cluster 0 — The Believers' Reward

| # | Surah | Revelation | Ayāt | Words in cluster | Share of surah |
|---|---|---|---|---|---|
| 103 | Al-Asr | Meccan | 3 | 3 | 30.0% |
| 98 | Al-Bayyina | Medinan | 8 | 16 | 26.7% |
| 95 | At-Tin | Meccan | 8 | 6 | 24.0% |
| 85 | Al-Burooj | Meccan | 22 | 15 | 22.7% |
| 64 | At-Taghaabun | Medinan | 18 | 33 | 19.3% |
| 99 | Az-Zalzala | Medinan | 8 | 5 | 18.5% |
| 66 | At-Tahrim | Medinan | 12 | 29 | 17.0% |
| 92 | Al-Lail | Meccan | 21 | 8 | 16.7% |
| 47 | Muhammad | Medinan | 38 | 55 | 15.7% |
| 104 | Al-Humaza | Meccan | 9 | 3 | 14.3% |
| 108 | Al-Kawthar | Meccan | 3 | 1 | 14.3% |
| 57 | Al-Hadid | Medinan | 29 | 55 | 14.1% |
| 48 | Al-Fath | Medinan | 29 | 54 | 13.4% |
| 101 | Al-Qaari'a | Meccan | 11 | 3 | 12.5% |
| 61 | As-Saff | Medinan | 14 | 18 | 12.4% |
| 49 | Al-Hujuraat | Medinan | 18 | 28 | 12.0% |
| 88 | Al-Ghaashiya | Meccan | 26 | 7 | 11.7% |
| 58 | Al-Mujaadila | Medinan | 22 | 34 | 11.4% |
| 65 | At-Talaaq | Medinan | 12 | 23 | 11.4% |
| 9 | At-Tawba | Medinan | 129 | 182 | 11.1% |

### Cluster 4 — Revelation, Speech & Disbelief

| # | Surah | Revelation | Ayāt | Words in cluster | Share of surah |
|---|---|---|---|---|---|
| 102 | At-Takaathur | Meccan | 8 | 8 | 50.0% |
| 55 | Ar-Rahmaan | Medinan | 78 | 119 | 46.5% |
| 114 | An-Naas | Meccan | 6 | 7 | 43.8% |
| 26 | Ash-Shu'araa | Meccan | 227 | 356 | 43.4% |
| 108 | Al-Kawthar | Meccan | 3 | 3 | 42.9% |
| 10 | Yunus | Meccan | 109 | 464 | 41.1% |
| 15 | Al-Hijr | Meccan | 99 | 168 | 41.0% |
| 27 | An-Naml | Meccan | 93 | 301 | 40.8% |
| 43 | Az-Zukhruf | Meccan | 89 | 208 | 40.6% |
| 12 | Yusuf | Meccan | 111 | 449 | 39.9% |
| 34 | Saba | Meccan | 54 | 216 | 39.7% |
| 45 | Al-Jaathiya | Meccan | 37 | 125 | 39.1% |
| 28 | Al-Qasas | Meccan | 88 | 340 | 38.5% |
| 46 | Al-Ahqaf | Meccan | 35 | 156 | 38.5% |
| 6 | Al-An'aam | Meccan | 165 | 727 | 37.4% |
| 83 | Al-Mutaffifin | Meccan | 36 | 37 | 36.6% |
| 19 | Maryam | Meccan | 98 | 237 | 36.1% |
| 23 | Al-Muminoon | Meccan | 118 | 228 | 35.8% |
| 7 | Al-A'raaf | Meccan | 206 | 764 | 35.6% |
| 21 | Al-Anbiyaa | Meccan | 112 | 254 | 35.5% |

### Cluster 5 — The Commanded Self

| # | Surah | Revelation | Ayāt | Words in cluster | Share of surah |
|---|---|---|---|---|---|
| 65 | At-Talaaq | Medinan | 12 | 29 | 14.4% |
| 94 | Ash-Sharh | Meccan | 8 | 2 | 12.5% |
| 91 | Ash-Shams | Meccan | 15 | 4 | 10.3% |
| 82 | Al-Infitaar | Meccan | 19 | 5 | 10.0% |
| 103 | Al-Asr | Meccan | 3 | 1 | 10.0% |
| 97 | Al-Qadr | Meccan | 5 | 2 | 9.5% |
| 96 | Al-Alaq | Meccan | 19 | 4 | 8.2% |
| 31 | Luqman | Meccan | 34 | 26 | 7.4% |
| 49 | Al-Hujuraat | Medinan | 18 | 17 | 7.3% |
| 2 | Al-Baqara | Medinan | 286 | 252 | 6.5% |
| 66 | At-Tahrim | Medinan | 12 | 11 | 6.4% |
| 33 | Al-Ahzaab | Medinan | 73 | 56 | 6.4% |
| 61 | As-Saff | Medinan | 14 | 9 | 6.2% |
| 77 | Al-Mursalaat | Meccan | 50 | 7 | 6.1% |
| 47 | Muhammad | Medinan | 38 | 20 | 5.7% |
| 105 | Al-Fil | Meccan | 5 | 1 | 5.6% |
| 3 | Aal-i-Imraan | Medinan | 200 | 124 | 5.5% |
| 16 | An-Nahl | Meccan | 128 | 63 | 5.3% |
| 68 | Al-Qalam | Meccan | 52 | 10 | 5.2% |
| 26 | Ash-Shu'araa | Meccan | 227 | 41 | 5.0% |

### Cluster 7 — Sea-Rescue / Bounty / Gratitude

| # | Surah | Revelation | Ayāt | Words in cluster | Share of surah |
|---|---|---|---|---|---|
| 58 | Al-Mujaadila | Medinan | 22 | 13 | 4.4% |
| 82 | Al-Infitaar | Meccan | 19 | 2 | 4.0% |
| 31 | Luqman | Meccan | 34 | 13 | 3.7% |
| 62 | Al-Jumu'a | Medinan | 11 | 4 | 3.4% |
| 35 | Faatir | Meccan | 45 | 17 | 3.4% |
| 81 | At-Takwir | Meccan | 29 | 2 | 3.0% |
| 76 | Al-Insaan | Medinan | 31 | 5 | 2.9% |
| 45 | Al-Jaathiya | Meccan | 37 | 9 | 2.8% |
| 55 | Ar-Rahmaan | Medinan | 78 | 7 | 2.7% |
| 17 | Al-Israa | Meccan | 111 | 28 | 2.7% |
| 37 | As-Saaffaat | Meccan | 182 | 14 | 2.6% |
| 36 | Yaseen | Meccan | 83 | 10 | 2.3% |
| 44 | Ad-Dukhaan | Meccan | 59 | 5 | 2.3% |
| 10 | Yunus | Meccan | 109 | 25 | 2.2% |
| 27 | An-Naml | Meccan | 93 | 16 | 2.2% |
| 92 | Al-Lail | Meccan | 21 | 1 | 2.1% |
| 87 | Al-A'laa | Meccan | 19 | 1 | 2.0% |
| 18 | Al-Kahf | Meccan | 110 | 21 | 2.0% |
| 83 | Al-Mutaffifin | Meccan | 36 | 2 | 2.0% |
| 38 | Saad | Meccan | 88 | 9 | 1.9% |

### Cluster 8 — Allegiance & the Object of Worship

| # | Surah | Revelation | Ayāt | Words in cluster | Share of surah |
|---|---|---|---|---|---|
| 109 | Al-Kaafiroon | Meccan | 6 | 8 | 66.7% |
| 1 | Al-Faatiha | Meccan | 7 | 8 | 34.8% |
| 61 | As-Saff | Medinan | 14 | 32 | 22.1% |
| 112 | Al-Ikhlaas | Meccan | 4 | 2 | 20.0% |
| 62 | Al-Jumu'a | Medinan | 11 | 23 | 19.7% |
| 58 | Al-Mujaadila | Medinan | 22 | 56 | 18.9% |
| 110 | An-Nasr | Medinan | 3 | 3 | 18.8% |
| 64 | At-Taghaabun | Medinan | 18 | 31 | 18.1% |
| 48 | Al-Fath | Medinan | 29 | 72 | 17.8% |
| 22 | Al-Hajj | Medinan | 78 | 145 | 17.6% |
| 39 | Az-Zumar | Meccan | 75 | 135 | 17.5% |
| 72 | Al-Jinn | Meccan | 28 | 31 | 17.4% |
| 42 | Ash-Shura | Meccan | 53 | 90 | 17.4% |
| 60 | Al-Mumtahana | Medinan | 13 | 37 | 17.2% |
| 9 | At-Tawba | Medinan | 129 | 281 | 17.1% |
| 8 | Al-Anfaal | Medinan | 75 | 135 | 16.8% |
| 98 | Al-Bayyina | Medinan | 8 | 10 | 16.7% |
| 96 | Al-Alaq | Meccan | 19 | 8 | 16.3% |
| 40 | Ghafir | Meccan | 85 | 125 | 15.9% |
| 71 | Nooh | Meccan | 28 | 24 | 15.7% |

### Cluster 11 — Vegetative Signs / Reflective Gaze

| # | Surah | Revelation | Ayāt | Words in cluster | Share of surah |
|---|---|---|---|---|---|
| 80 | Abasa | Meccan | 42 | 7 | 8.0% |
| 97 | Al-Qadr | Meccan | 5 | 1 | 4.8% |
| 100 | Al-Aadiyaat | Meccan | 11 | 1 | 4.2% |
| 82 | Al-Infitaar | Meccan | 19 | 2 | 4.0% |
| 95 | At-Tin | Meccan | 8 | 1 | 4.0% |
| 89 | Al-Fajr | Meccan | 30 | 3 | 3.3% |
| 55 | Ar-Rahmaan | Medinan | 78 | 7 | 2.7% |
| 91 | Ash-Shams | Meccan | 15 | 1 | 2.6% |
| 50 | Qaaf | Meccan | 45 | 6 | 2.4% |
| 78 | An-Naba | Meccan | 40 | 3 | 2.3% |
| 76 | Al-Insaan | Medinan | 31 | 4 | 2.3% |
| 83 | Al-Mutaffifin | Meccan | 36 | 2 | 2.0% |
| 56 | Al-Waaqia | Meccan | 96 | 5 | 2.0% |
| 71 | Nooh | Meccan | 28 | 3 | 2.0% |
| 75 | Al-Qiyaama | Meccan | 40 | 2 | 1.9% |
| 36 | Yaseen | Meccan | 83 | 8 | 1.8% |
| 61 | As-Saff | Medinan | 14 | 2 | 1.4% |
| 44 | Ad-Dukhaan | Meccan | 59 | 3 | 1.4% |
| 49 | Al-Hujuraat | Medinan | 18 | 3 | 1.3% |
| 16 | An-Nahl | Meccan | 128 | 15 | 1.3% |

### Cluster 17 — Bodily Purity & Prayer

| # | Surah | Revelation | Ayāt | Words in cluster | Share of surah |
|---|---|---|---|---|---|
| 112 | Al-Ikhlaas | Meccan | 4 | 2 | 20.0% |
| 107 | Al-Maa'un | Meccan | 7 | 2 | 14.3% |
| 108 | Al-Kawthar | Meccan | 3 | 1 | 14.3% |
| 93 | Ad-Dhuhaa | Meccan | 11 | 3 | 10.7% |
| 103 | Al-Asr | Meccan | 3 | 1 | 10.0% |
| 80 | Abasa | Meccan | 42 | 8 | 9.1% |
| 72 | Al-Jinn | Meccan | 28 | 15 | 8.4% |
| 92 | Al-Lail | Meccan | 21 | 4 | 8.3% |
| 87 | Al-A'laa | Meccan | 19 | 3 | 6.1% |
| 111 | Al-Masad | Meccan | 5 | 1 | 5.9% |
| 62 | Al-Jumu'a | Medinan | 11 | 6 | 5.1% |
| 75 | Al-Qiyaama | Meccan | 40 | 5 | 4.7% |
| 73 | Al-Muzzammil | Meccan | 20 | 6 | 4.2% |
| 24 | An-Noor | Medinan | 64 | 36 | 4.2% |
| 18 | Al-Kahf | Meccan | 110 | 41 | 3.9% |
| 90 | Al-Balad | Meccan | 20 | 2 | 3.8% |
| 74 | Al-Muddaththir | Meccan | 56 | 6 | 3.7% |
| 5 | Al-Maaida | Medinan | 120 | 62 | 3.4% |
| 67 | Al-Mulk | Meccan | 30 | 7 | 3.4% |
| 88 | Al-Ghaashiya | Meccan | 26 | 2 | 3.3% |

### Cluster 19 — Household Law & Lineage

| # | Surah | Revelation | Ayāt | Words in cluster | Share of surah |
|---|---|---|---|---|---|
| 103 | Al-Asr | Meccan | 3 | 2 | 20.0% |
| 112 | Al-Ikhlaas | Meccan | 4 | 2 | 20.0% |
| 109 | Al-Kaafiroon | Meccan | 6 | 2 | 16.7% |
| 107 | Al-Maa'un | Meccan | 7 | 2 | 14.3% |
| 90 | Al-Balad | Meccan | 20 | 6 | 11.5% |
| 82 | Al-Infitaar | Meccan | 19 | 5 | 10.0% |
| 80 | Abasa | Meccan | 42 | 8 | 9.1% |
| 87 | Al-A'laa | Meccan | 19 | 4 | 8.2% |
| 54 | Al-Qamar | Meccan | 55 | 19 | 7.5% |
| 93 | Ad-Dhuhaa | Meccan | 11 | 2 | 7.1% |
| 89 | Al-Fajr | Meccan | 30 | 6 | 6.5% |
| 4 | An-Nisaa | Medinan | 176 | 158 | 6.4% |
| 92 | Al-Lail | Meccan | 21 | 3 | 6.2% |
| 94 | Ash-Sharh | Meccan | 8 | 1 | 6.2% |
| 110 | An-Nasr | Medinan | 3 | 1 | 6.2% |
| 74 | Al-Muddaththir | Meccan | 56 | 10 | 6.2% |
| 81 | At-Takwir | Meccan | 29 | 4 | 6.1% |
| 111 | Al-Masad | Meccan | 5 | 1 | 5.9% |
| 66 | At-Tahrim | Medinan | 12 | 10 | 5.8% |
| 73 | Al-Muzzammil | Meccan | 20 | 8 | 5.6% |

### Cluster 43 — Divine Will & Dominion

| # | Surah | Revelation | Ayāt | Words in cluster | Share of surah |
|---|---|---|---|---|---|
| 97 | Al-Qadr | Meccan | 5 | 5 | 23.8% |
| 42 | Ash-Shura | Meccan | 53 | 38 | 7.3% |
| 74 | Al-Muddaththir | Meccan | 56 | 11 | 6.8% |
| 65 | At-Talaaq | Medinan | 12 | 13 | 6.4% |
| 34 | Saba | Meccan | 54 | 34 | 6.2% |
| 110 | An-Nasr | Medinan | 3 | 1 | 6.2% |
| 114 | An-Naas | Meccan | 6 | 1 | 6.2% |
| 85 | Al-Burooj | Meccan | 22 | 4 | 6.1% |
| 82 | Al-Infitaar | Meccan | 19 | 3 | 6.0% |
| 67 | Al-Mulk | Meccan | 30 | 12 | 5.8% |
| 80 | Abasa | Meccan | 42 | 5 | 5.7% |
| 54 | Al-Qamar | Meccan | 55 | 14 | 5.6% |
| 13 | Ar-Ra'd | Medinan | 43 | 29 | 5.2% |
| 76 | Al-Insaan | Medinan | 31 | 9 | 5.1% |
| 36 | Yaseen | Meccan | 83 | 22 | 5.0% |
| 86 | At-Taariq | Meccan | 17 | 2 | 4.9% |
| 104 | Al-Humaza | Meccan | 9 | 1 | 4.8% |
| 78 | An-Naba | Meccan | 40 | 6 | 4.6% |
| 81 | At-Takwir | Meccan | 29 | 3 | 4.5% |
| 16 | An-Nahl | Meccan | 128 | 53 | 4.5% |

### Cluster 62 — The Prepared Fire

| # | Surah | Revelation | Ayāt | Words in cluster | Share of surah |
|---|---|---|---|---|---|
| 109 | Al-Kaafiroon | Meccan | 6 | 1 | 8.3% |
| 86 | At-Taariq | Meccan | 17 | 3 | 7.3% |
| 54 | Al-Qamar | Meccan | 55 | 16 | 6.3% |
| 70 | Al-Ma'aarij | Meccan | 44 | 9 | 6.3% |
| 67 | Al-Mulk | Meccan | 30 | 13 | 6.2% |
| 85 | Al-Burooj | Meccan | 22 | 4 | 6.1% |
| 64 | At-Taghaabun | Medinan | 18 | 10 | 5.8% |
| 84 | Al-Inshiqaaq | Meccan | 25 | 4 | 5.8% |
| 48 | Al-Fath | Medinan | 29 | 21 | 5.2% |
| 88 | Al-Ghaashiya | Meccan | 26 | 3 | 5.0% |
| 44 | Ad-Dukhaan | Meccan | 59 | 11 | 5.0% |
| 76 | Al-Insaan | Medinan | 31 | 8 | 4.6% |
| 46 | Al-Ahqaf | Meccan | 35 | 18 | 4.4% |
| 34 | Saba | Meccan | 54 | 24 | 4.4% |
| 89 | Al-Fajr | Meccan | 30 | 4 | 4.3% |
| 32 | As-Sajda | Meccan | 30 | 10 | 4.2% |
| 58 | Al-Mujaadila | Medinan | 22 | 12 | 4.0% |
| 41 | Fussilat | Meccan | 54 | 20 | 4.0% |
| 9 | At-Tawba | Medinan | 129 | 64 | 3.9% |
| 8 | Al-Anfaal | Medinan | 75 | 31 | 3.9% |

### Cluster 66 — Jihād fī Sabīl Allāh

| # | Surah | Revelation | Ayāt | Words in cluster | Share of surah |
|---|---|---|---|---|---|
| 104 | Al-Humaza | Meccan | 9 | 2 | 9.5% |
| 63 | Al-Munaafiqoon | Medinan | 11 | 11 | 9.4% |
| 9 | At-Tawba | Medinan | 129 | 97 | 5.9% |
| 111 | Al-Masad | Meccan | 5 | 1 | 5.9% |
| 60 | Al-Mumtahana | Medinan | 13 | 11 | 5.1% |
| 92 | Al-Lail | Meccan | 21 | 2 | 4.2% |
| 61 | As-Saff | Medinan | 14 | 6 | 4.1% |
| 8 | Al-Anfaal | Medinan | 75 | 33 | 4.1% |
| 4 | An-Nisaa | Medinan | 176 | 100 | 4.1% |
| 47 | Muhammad | Medinan | 38 | 13 | 3.7% |
| 73 | Al-Muzzammil | Meccan | 20 | 5 | 3.5% |
| 74 | Al-Muddaththir | Meccan | 56 | 5 | 3.1% |
| 85 | Al-Burooj | Meccan | 22 | 2 | 3.0% |
| 33 | Al-Ahzaab | Medinan | 73 | 25 | 2.8% |
| 57 | Al-Hadid | Medinan | 29 | 11 | 2.8% |
| 72 | Al-Jinn | Meccan | 28 | 5 | 2.8% |
| 59 | Al-Hashr | Medinan | 24 | 8 | 2.8% |
| 71 | Nooh | Meccan | 28 | 4 | 2.6% |
| 3 | Aal-i-Imraan | Medinan | 200 | 52 | 2.3% |
| 80 | Abasa | Meccan | 42 | 2 | 2.3% |

### Cluster 75 — Witnessing the Visible Sign

| # | Surah | Revelation | Ayāt | Words in cluster | Share of surah |
|---|---|---|---|---|---|
| 99 | Az-Zalzala | Medinan | 8 | 4 | 14.8% |
| 107 | Al-Maa'un | Meccan | 7 | 2 | 14.3% |
| 102 | At-Takaathur | Meccan | 8 | 2 | 12.5% |
| 96 | Al-Alaq | Meccan | 19 | 5 | 10.2% |
| 110 | An-Nasr | Medinan | 3 | 1 | 6.2% |
| 90 | Al-Balad | Meccan | 20 | 3 | 5.8% |
| 105 | Al-Fil | Meccan | 5 | 1 | 5.6% |
| 53 | An-Najm | Meccan | 62 | 9 | 4.2% |
| 100 | Al-Aadiyaat | Meccan | 11 | 1 | 4.2% |
| 79 | An-Naazi'aat | Meccan | 46 | 5 | 4.1% |
| 95 | At-Tin | Meccan | 8 | 1 | 4.0% |
| 67 | Al-Mulk | Meccan | 30 | 8 | 3.8% |
| 70 | Al-Ma'aarij | Meccan | 44 | 5 | 3.5% |
| 30 | Ar-Room | Meccan | 60 | 18 | 3.4% |
| 89 | Al-Fajr | Meccan | 30 | 3 | 3.3% |
| 59 | Al-Hashr | Medinan | 24 | 9 | 3.1% |
| 81 | At-Takwir | Meccan | 29 | 2 | 3.0% |
| 60 | Al-Mumtahana | Medinan | 13 | 6 | 2.8% |
| 63 | Al-Munaafiqoon | Medinan | 11 | 3 | 2.6% |
| 86 | At-Taariq | Meccan | 17 | 1 | 2.4% |

### Cluster 77 — Creation & the Appointed Term

| # | Surah | Revelation | Ayāt | Words in cluster | Share of surah |
|---|---|---|---|---|---|
| 86 | At-Taariq | Meccan | 17 | 3 | 7.3% |
| 113 | Al-Falaq | Meccan | 5 | 1 | 6.7% |
| 96 | Al-Alaq | Meccan | 19 | 3 | 6.1% |
| 95 | At-Tin | Meccan | 8 | 1 | 4.0% |
| 90 | Al-Balad | Meccan | 20 | 2 | 3.8% |
| 75 | Al-Qiyaama | Meccan | 40 | 4 | 3.8% |
| 80 | Abasa | Meccan | 42 | 3 | 3.4% |
| 36 | Yaseen | Meccan | 83 | 14 | 3.2% |
| 23 | Al-Muminoon | Meccan | 118 | 19 | 3.0% |
| 50 | Qaaf | Meccan | 45 | 7 | 2.9% |
| 46 | Al-Ahqaf | Meccan | 35 | 11 | 2.7% |
| 71 | Nooh | Meccan | 28 | 4 | 2.6% |
| 65 | At-Talaaq | Medinan | 12 | 5 | 2.5% |
| 56 | Al-Waaqia | Meccan | 96 | 6 | 2.4% |
| 38 | Saad | Meccan | 88 | 11 | 2.4% |
| 53 | An-Najm | Meccan | 62 | 5 | 2.3% |
| 13 | Ar-Ra'd | Medinan | 43 | 13 | 2.3% |
| 78 | An-Naba | Meccan | 40 | 3 | 2.3% |
| 76 | Al-Insaan | Medinan | 31 | 4 | 2.3% |
| 30 | Ar-Room | Meccan | 60 | 12 | 2.3% |

### Cluster 90 — Sin–Mercy Economy

| # | Surah | Revelation | Ayāt | Words in cluster | Share of surah |
|---|---|---|---|---|---|
| 1 | Al-Faatiha | Meccan | 7 | 5 | 21.7% |
| 110 | An-Nasr | Medinan | 3 | 2 | 12.5% |
| 100 | Al-Aadiyaat | Meccan | 11 | 2 | 8.3% |
| 60 | Al-Mumtahana | Medinan | 13 | 17 | 7.9% |
| 49 | Al-Hujuraat | Medinan | 18 | 18 | 7.7% |
| 66 | At-Tahrim | Medinan | 12 | 11 | 6.4% |
| 63 | Al-Munaafiqoon | Medinan | 11 | 7 | 6.0% |
| 19 | Maryam | Meccan | 98 | 29 | 4.4% |
| 5 | Al-Maaida | Medinan | 120 | 79 | 4.4% |
| 87 | Al-A'laa | Meccan | 19 | 2 | 4.1% |
| 9 | At-Tawba | Medinan | 129 | 66 | 4.0% |
| 95 | At-Tin | Meccan | 8 | 1 | 4.0% |
| 71 | Nooh | Meccan | 28 | 6 | 3.9% |
| 4 | An-Nisaa | Medinan | 176 | 96 | 3.9% |
| 2 | Al-Baqara | Medinan | 286 | 150 | 3.9% |
| 57 | Al-Hadid | Medinan | 29 | 15 | 3.8% |
| 67 | Al-Mulk | Meccan | 30 | 8 | 3.8% |
| 90 | Al-Balad | Meccan | 20 | 2 | 3.8% |
| 30 | Ar-Room | Meccan | 60 | 20 | 3.8% |
| 25 | Al-Furqaan | Meccan | 77 | 23 | 3.8% |

### Cluster 96 — Dunya vs. Ākhirah

| # | Surah | Revelation | Ayāt | Words in cluster | Share of surah |
|---|---|---|---|---|---|
| 87 | Al-A'laa | Meccan | 19 | 5 | 10.2% |
| 102 | At-Takaathur | Meccan | 8 | 1 | 6.2% |
| 53 | An-Najm | Meccan | 62 | 12 | 5.6% |
| 74 | Al-Muddaththir | Meccan | 56 | 7 | 4.3% |
| 57 | Al-Hadid | Medinan | 29 | 16 | 4.1% |
| 82 | Al-Infitaar | Meccan | 19 | 2 | 4.0% |
| 71 | Nooh | Meccan | 28 | 6 | 3.9% |
| 75 | Al-Qiyaama | Meccan | 40 | 4 | 3.8% |
| 93 | Ad-Dhuhaa | Meccan | 11 | 1 | 3.6% |
| 62 | Al-Jumu'a | Medinan | 11 | 4 | 3.4% |
| 79 | An-Naazi'aat | Meccan | 46 | 4 | 3.3% |
| 73 | Al-Muzzammil | Meccan | 20 | 4 | 2.8% |
| 45 | Al-Jaathiya | Meccan | 37 | 9 | 2.8% |
| 15 | Al-Hijr | Meccan | 99 | 11 | 2.7% |
| 77 | Al-Mursalaat | Meccan | 50 | 3 | 2.6% |
| 10 | Yunus | Meccan | 109 | 29 | 2.6% |
| 63 | Al-Munaafiqoon | Medinan | 11 | 3 | 2.6% |
| 91 | Ash-Shams | Meccan | 15 | 1 | 2.6% |
| 31 | Luqman | Meccan | 34 | 9 | 2.6% |
| 43 | Az-Zukhruf | Meccan | 89 | 13 | 2.5% |

## Spotlight surahs

### 1. Al-Faatiha — The Opening

_Meccan, 7 ayāt, 23 root-bearing words; Gini = 0.427; dominant share = 34.8%._

Top clusters:

- `8` **Allegiance & the Object of Worship** — 8 words (34.8%)
- `90` **Sin–Mercy Economy** — 5 words (21.7%)
- `4` **Revelation, Speech & Disbelief** — 2 words (8.7%)
- `1` **(unnamed #1)** — 1 words (4.3%)
- `67` **(unnamed #67)** — 1 words (4.3%)

Named clusters present:
- `8` Allegiance & the Object of Worship — 34.8%
- `90` Sin–Mercy Economy — 21.7%
- `4` Revelation, Speech & Disbelief — 8.7%
- `43` Divine Will & Dominion — 4.3%
- `19` Household Law & Lineage — 4.3%
- `5` The Commanded Self — 4.3%

### 2. Al-Baqara — The Cow

_Medinan, 286 ayāt, 3884 root-bearing words; Gini = 0.832; dominant share = 28.9%._

Top clusters:

- `4` **Revelation, Speech & Disbelief** — 1124 words (28.9%)
- `8` **Allegiance & the Object of Worship** — 486 words (12.5%)
- `0` **The Believers' Reward** — 276 words (7.1%)
- `5` **The Commanded Self** — 252 words (6.5%)
- `90` **Sin–Mercy Economy** — 150 words (3.9%)

Named clusters present:
- `4` Revelation, Speech & Disbelief — 28.9%
- `8` Allegiance & the Object of Worship — 12.5%
- `0` The Believers' Reward — 7.1%
- `5` The Commanded Self — 6.5%
- `90` Sin–Mercy Economy — 3.9%
- `19` Household Law & Lineage — 3.7%
- `43` Divine Will & Dominion — 3.0%
- `66` Jihād fī Sabīl Allāh — 2.3%
- `62` The Prepared Fire — 2.1%
- `17` Bodily Purity & Prayer — 2.0%

### 18. Al-Kahf — The Cave

_Meccan, 110 ayāt, 1057 root-bearing words; Gini = 0.778; dominant share = 32.6%._

Top clusters:

- `4` **Revelation, Speech & Disbelief** — 345 words (32.6%)
- `8` **Allegiance & the Object of Worship** — 95 words (9.0%)
- `0` **The Believers' Reward** — 86 words (8.1%)
- `5` **The Commanded Self** — 48 words (4.5%)
- `17` **Bodily Purity & Prayer** — 41 words (3.9%)

Named clusters present:
- `4` Revelation, Speech & Disbelief — 32.6%
- `8` Allegiance & the Object of Worship — 9.0%
- `0` The Believers' Reward — 8.1%
- `5` The Commanded Self — 4.5%
- `17` Bodily Purity & Prayer — 3.9%
- `19` Household Law & Lineage — 2.8%
- `43` Divine Will & Dominion — 2.6%
- `7` Sea-Rescue / Bounty / Gratitude — 2.0%
- `62` The Prepared Fire — 1.8%
- `90` Sin–Mercy Economy — 1.5%

### 36. Yaseen — Yaseen

_Meccan, 83 ayāt, 438 root-bearing words; Gini = 0.700; dominant share = 33.6%._

Top clusters:

- `4` **Revelation, Speech & Disbelief** — 147 words (33.6%)
- `8` **Allegiance & the Object of Worship** — 35 words (8.0%)
- `19` **Household Law & Lineage** — 23 words (5.3%)
- `43` **Divine Will & Dominion** — 22 words (5.0%)
- `0` **The Believers' Reward** — 21 words (4.8%)

Named clusters present:
- `4` Revelation, Speech & Disbelief — 33.6%
- `8` Allegiance & the Object of Worship — 8.0%
- `19` Household Law & Lineage — 5.3%
- `43` Divine Will & Dominion — 5.0%
- `0` The Believers' Reward — 4.8%
- `90` Sin–Mercy Economy — 3.4%
- `77` Creation & the Appointed Term — 3.2%
- `7` Sea-Rescue / Bounty / Gratitude — 2.3%
- `17` Bodily Purity & Prayer — 2.1%
- `11` Vegetative Signs / Reflective Gaze — 1.8%

### 55. Ar-Rahmaan — The Beneficent

_Medinan, 78 ayāt, 256 root-bearing words; Gini = 0.687; dominant share = 46.5%._

Top clusters:

- `4` **Revelation, Speech & Disbelief** — 119 words (46.5%)
- `0` **The Believers' Reward** — 18 words (7.0%)
- `1` **(unnamed #1)** — 9 words (3.5%)
- `34` **(unnamed #34)** — 8 words (3.1%)
- `11` **Vegetative Signs / Reflective Gaze** — 7 words (2.7%)

Named clusters present:
- `4` Revelation, Speech & Disbelief — 46.5%
- `0` The Believers' Reward — 7.0%
- `11` Vegetative Signs / Reflective Gaze — 2.7%
- `7` Sea-Rescue / Bounty / Gratitude — 2.7%
- `8` Allegiance & the Object of Worship — 2.3%
- `43` Divine Will & Dominion — 1.6%
- `5` The Commanded Self — 1.6%
- `77` Creation & the Appointed Term — 1.2%
- `19` Household Law & Lineage — 1.2%
- `96` Dunya vs. Ākhirah — 0.8%

### 67. Al-Mulk — The Sovereignty

_Meccan, 30 ayāt, 208 root-bearing words; Gini = 0.593; dominant share = 24.5%._

Top clusters:

- `4` **Revelation, Speech & Disbelief** — 51 words (24.5%)
- `62` **The Prepared Fire** — 13 words (6.2%)
- `8` **Allegiance & the Object of Worship** — 13 words (6.2%)
- `43` **Divine Will & Dominion** — 12 words (5.8%)
- `0` **The Believers' Reward** — 11 words (5.3%)

Named clusters present:
- `4` Revelation, Speech & Disbelief — 24.5%
- `62` The Prepared Fire — 6.2%
- `8` Allegiance & the Object of Worship — 6.2%
- `43` Divine Will & Dominion — 5.8%
- `0` The Believers' Reward — 5.3%
- `90` Sin–Mercy Economy — 3.8%
- `75` Witnessing the Visible Sign — 3.8%
- `17` Bodily Purity & Prayer — 3.4%
- `5` The Commanded Self — 2.4%
- `77` Creation & the Appointed Term — 1.9%

### 78. An-Naba — The Announcement

_Meccan, 40 ayāt, 131 root-bearing words; Gini = 0.495; dominant share = 23.7%._

Top clusters:

- `4` **Revelation, Speech & Disbelief** — 31 words (23.7%)
- `0` **The Believers' Reward** — 9 words (6.9%)
- `78` **(unnamed #78)** — 7 words (5.3%)
- `43` **Divine Will & Dominion** — 6 words (4.6%)
- `44` **(unnamed #44)** — 5 words (3.8%)

Named clusters present:
- `4` Revelation, Speech & Disbelief — 23.7%
- `0` The Believers' Reward — 6.9%
- `43` Divine Will & Dominion — 4.6%
- `62` The Prepared Fire — 3.8%
- `17` Bodily Purity & Prayer — 3.1%
- `77` Creation & the Appointed Term — 2.3%
- `19` Household Law & Lineage — 2.3%
- `11` Vegetative Signs / Reflective Gaze — 2.3%
- `7` Sea-Rescue / Bounty / Gratitude — 1.5%
- `5` The Commanded Self — 1.5%

### 87. Al-A'laa — The Most High

_Meccan, 19 ayāt, 49 root-bearing words; Gini = 0.332; dominant share = 14.3%._

Top clusters:

- `4` **Revelation, Speech & Disbelief** — 7 words (14.3%)
- `96` **Dunya vs. Ākhirah** — 5 words (10.2%)
- `19` **Household Law & Lineage** — 4 words (8.2%)
- `8` **Allegiance & the Object of Worship** — 3 words (6.1%)
- `17` **Bodily Purity & Prayer** — 3 words (6.1%)

Named clusters present:
- `4` Revelation, Speech & Disbelief — 14.3%
- `96` Dunya vs. Ākhirah — 10.2%
- `19` Household Law & Lineage — 8.2%
- `8` Allegiance & the Object of Worship — 6.1%
- `17` Bodily Purity & Prayer — 6.1%
- `43` Divine Will & Dominion — 4.1%
- `90` Sin–Mercy Economy — 4.1%
- `5` The Commanded Self — 4.1%
- `77` Creation & the Appointed Term — 2.0%
- `75` Witnessing the Visible Sign — 2.0%

### 93. Ad-Dhuhaa — The Morning Hours

_Meccan, 11 ayāt, 28 root-bearing words; Gini = 0.321; dominant share = 21.4%._

Top clusters:

- `4` **Revelation, Speech & Disbelief** — 6 words (21.4%)
- `0` **The Believers' Reward** — 3 words (10.7%)
- `17` **Bodily Purity & Prayer** — 3 words (10.7%)
- `19` **Household Law & Lineage** — 2 words (7.1%)
- `8` **Allegiance & the Object of Worship** — 2 words (7.1%)

Named clusters present:
- `4` Revelation, Speech & Disbelief — 21.4%
- `0` The Believers' Reward — 10.7%
- `17` Bodily Purity & Prayer — 10.7%
- `19` Household Law & Lineage — 7.1%
- `8` Allegiance & the Object of Worship — 7.1%
- `96` Dunya vs. Ākhirah — 3.6%
- `5` The Commanded Self — 3.6%

### 97. Al-Qadr — The Power, Fate

_Meccan, 5 ayāt, 21 root-bearing words; Gini = 0.367; dominant share = 23.8%._

Top clusters:

- `4` **Revelation, Speech & Disbelief** — 5 words (23.8%)
- `43` **Divine Will & Dominion** — 5 words (23.8%)
- `24` **(unnamed #24)** — 3 words (14.3%)
- `5` **The Commanded Self** — 2 words (9.5%)
- `78` **(unnamed #78)** — 1 words (4.8%)

Named clusters present:
- `4` Revelation, Speech & Disbelief — 23.8%
- `43` Divine Will & Dominion — 23.8%
- `5` The Commanded Self — 9.5%
- `19` Household Law & Lineage — 4.8%
- `11` Vegetative Signs / Reflective Gaze — 4.8%

### 108. Al-Kawthar — Abundance

_Meccan, 3 ayāt, 7 root-bearing words; Gini = 0.229; dominant share = 42.9%._

Top clusters:

- `4` **Revelation, Speech & Disbelief** — 3 words (42.9%)
- `0` **The Believers' Reward** — 1 words (14.3%)
- `17` **Bodily Purity & Prayer** — 1 words (14.3%)
- `459` **(unnamed #459)** — 1 words (14.3%)
- `267` **(unnamed #267)** — 1 words (14.3%)

Named clusters present:
- `4` Revelation, Speech & Disbelief — 42.9%
- `0` The Believers' Reward — 14.3%
- `17` Bodily Purity & Prayer — 14.3%

### 109. Al-Kaafiroon — The Disbelievers

_Meccan, 6 ayāt, 12 root-bearing words; Gini = 0.458; dominant share = 66.7%._

Top clusters:

- `8` **Allegiance & the Object of Worship** — 8 words (66.7%)
- `19` **Household Law & Lineage** — 2 words (16.7%)
- `4` **Revelation, Speech & Disbelief** — 1 words (8.3%)
- `62` **The Prepared Fire** — 1 words (8.3%)

Named clusters present:
- `8` Allegiance & the Object of Worship — 66.7%
- `19` Household Law & Lineage — 16.7%
- `4` Revelation, Speech & Disbelief — 8.3%
- `62` The Prepared Fire — 8.3%

### 112. Al-Ikhlaas — Sincerity

_Meccan, 4 ayāt, 10 root-bearing words; Gini = 0.133; dominant share = 20.0%._

Top clusters:

- `4` **Revelation, Speech & Disbelief** — 2 words (20.0%)
- `8` **Allegiance & the Object of Worship** — 2 words (20.0%)
- `17` **Bodily Purity & Prayer** — 2 words (20.0%)
- `19` **Household Law & Lineage** — 2 words (20.0%)
- `216` **(unnamed #216)** — 1 words (10.0%)

Named clusters present:
- `4` Revelation, Speech & Disbelief — 20.0%
- `8` Allegiance & the Object of Worship — 20.0%
- `17` Bodily Purity & Prayer — 20.0%
- `19` Household Law & Lineage — 20.0%

### 113. Al-Falaq — The Dawn

_Meccan, 5 ayāt, 15 root-bearing words; Gini = 0.311; dominant share = 26.7%._

Top clusters:

- `4` **Revelation, Speech & Disbelief** — 4 words (26.7%)
- `34` **(unnamed #34)** — 4 words (26.7%)
- `9` **(unnamed #9)** — 1 words (6.7%)
- `301` **(unnamed #301)** — 1 words (6.7%)
- `77` **Creation & the Appointed Term** — 1 words (6.7%)

Named clusters present:
- `4` Revelation, Speech & Disbelief — 26.7%
- `77` Creation & the Appointed Term — 6.7%

### 114. An-Naas — Mankind

_Meccan, 6 ayāt, 16 root-bearing words; Gini = 0.375; dominant share = 43.8%._

Top clusters:

- `4` **Revelation, Speech & Disbelief** — 7 words (43.8%)
- `20` **(unnamed #20)** — 2 words (12.5%)
- `9` **(unnamed #9)** — 1 words (6.2%)
- `43` **Divine Will & Dominion** — 1 words (6.2%)
- `8` **Allegiance & the Object of Worship** — 1 words (6.2%)

Named clusters present:
- `4` Revelation, Speech & Disbelief — 43.8%
- `43` Divine Will & Dominion — 6.2%
- `8` Allegiance & the Object of Worship — 6.2%
- `0` The Believers' Reward — 6.2%

## Notable named-cluster co-occurrences (>=2% share each)

Pairs of named clusters that show up together inside the same surah.

| Cluster A | Cluster B | Surahs co-present |
|---|---|---|
| Revelation, Speech & Disbelief | Allegiance & the Object of Worship | 101 |
| The Believers' Reward | Revelation, Speech & Disbelief | 100 |
| The Believers' Reward | Allegiance & the Object of Worship | 91 |
| Household Law & Lineage | Revelation, Speech & Disbelief | 86 |
| Revelation, Speech & Disbelief | The Commanded Self | 85 |
| Household Law & Lineage | Allegiance & the Object of Worship | 79 |
| The Commanded Self | Allegiance & the Object of Worship | 78 |
| The Believers' Reward | Household Law & Lineage | 76 |
| The Believers' Reward | The Commanded Self | 76 |
| Household Law & Lineage | The Commanded Self | 69 |
| Revelation, Speech & Disbelief | Divine Will & Dominion | 69 |
| Revelation, Speech & Disbelief | Sin–Mercy Economy | 66 |
| The Believers' Reward | Divine Will & Dominion | 65 |
| Divine Will & Dominion | Allegiance & the Object of Worship | 64 |
| Allegiance & the Object of Worship | Sin–Mercy Economy | 63 |
| The Believers' Reward | Sin–Mercy Economy | 63 |
| Divine Will & Dominion | The Commanded Self | 57 |
| The Commanded Self | Sin–Mercy Economy | 55 |
| Household Law & Lineage | Divine Will & Dominion | 53 |
| Revelation, Speech & Disbelief | The Prepared Fire | 52 |

## Surprises and anomalies

Cases where the data-driven dominant cluster doesn't track the surah's traditional theme, 
or where a surah's named-cluster mix is unusual.

### Surahs where a single named cluster owns >=20% of root vocabulary (filter: >=30 root words)

| Share | # | Surah | Named cluster |
|---|---|---|---|
| 46.5% | 55 | Ar-Rahmaan | Revelation, Speech & Disbelief |
| 43.4% | 26 | Ash-Shu'araa | Revelation, Speech & Disbelief |
| 41.1% | 10 | Yunus | Revelation, Speech & Disbelief |
| 41.0% | 15 | Al-Hijr | Revelation, Speech & Disbelief |
| 40.8% | 27 | An-Naml | Revelation, Speech & Disbelief |
| 40.6% | 43 | Az-Zukhruf | Revelation, Speech & Disbelief |
| 39.9% | 12 | Yusuf | Revelation, Speech & Disbelief |
| 39.7% | 34 | Saba | Revelation, Speech & Disbelief |
| 39.1% | 45 | Al-Jaathiya | Revelation, Speech & Disbelief |
| 38.5% | 28 | Al-Qasas | Revelation, Speech & Disbelief |
| 38.5% | 46 | Al-Ahqaf | Revelation, Speech & Disbelief |
| 37.4% | 6 | Al-An'aam | Revelation, Speech & Disbelief |
| 36.6% | 83 | Al-Mutaffifin | Revelation, Speech & Disbelief |
| 36.1% | 19 | Maryam | Revelation, Speech & Disbelief |
| 35.8% | 23 | Al-Muminoon | Revelation, Speech & Disbelief |
| 35.6% | 7 | Al-A'raaf | Revelation, Speech & Disbelief |
| 35.5% | 21 | Al-Anbiyaa | Revelation, Speech & Disbelief |
| 35.4% | 41 | Fussilat | Revelation, Speech & Disbelief |
| 35.4% | 11 | Hud | Revelation, Speech & Disbelief |
| 35.1% | 44 | Ad-Dukhaan | Revelation, Speech & Disbelief |
| 35.0% | 62 | Al-Jumu'a | Revelation, Speech & Disbelief |
| 34.5% | 51 | Adh-Dhaariyat | Revelation, Speech & Disbelief |
| 34.4% | 20 | Taa-Haa | Revelation, Speech & Disbelief |
| 34.4% | 40 | Ghafir | Revelation, Speech & Disbelief |
| 34.1% | 29 | Al-Ankaboot | Revelation, Speech & Disbelief |

### Short surahs (<10 ayāt) where the dominant cluster is unnamed

These are textually small enough that a single rare root can dominate. Useful sanity check.

| # | Surah | Ayāt | Root words | Dominant cluster id | Dom. share |
|---|---|---|---|---|---|
| 94 | Ash-Sharh | 8 | 16 | 145 | 25.0% |
| 106 | Quraish | 4 | 12 | 78 | 16.7% |
| 107 | Al-Maa'un | 7 | 14 | 157 | 21.4% |
