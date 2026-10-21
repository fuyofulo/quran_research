#!/usr/bin/env python3
"""Phase-0 census for the regret investigation.

Deterministic layer, plus ONE clearly-marked orchestrator annotation table
(setting / person / kind for each core ayah), which is a reading, not a count.

  1. Marker inventory — every hit of each regret marker (morphology or exact
     formula over diacritic-stripped Arabic).
  2. Core set — ayahs with an explicit regret marker, annotated:
       setting: L = this life, D = at death / as punishment arrives, H = hereafter
       person:  S = singular speaker, P = plural, N = narrated (no speech)
       kind:    self = regret over one's own conduct; other = lament over others;
                false = regret aimed at the wrong object; wish = non-culpable wish;
                control = same marker, not regret
  3. Root lift — which roots are over-represented in self-regret ayahs vs the corpus.
  4. Translator divergence (global combined score) over the core set.

Emits data/structural/regret-census.json.
"""
import json, os, re, unicodedata
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def norm(t):
    t = unicodedata.normalize("NFD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub("[ٱأإآ]", "ا", t).replace("ى", "ي").replace("ـ", "")
    # quran.json writes open-fathatan (U+08F0) tanwin as "Xࣰ ا" with a SPACE before the
    # alif (2,054 tokens / 1,533 ayahs). Rejoin it, or every accusative-indefinite
    # formula (ghafuran rahiman, tawbatan nasuha ...) silently misses.
    return re.sub(r" ا(?= |$)", "ا", t)


# Morphology markers: (root, lemma) -> label
LEMMA_MARKERS = {
    ("ndm", "na`dimiyn"): "nadim (regretful)", ("ndm", "n~adaAmap"): "nadama (regret)",
    ("Hsr", "Hasorap"): "hasra", ("Hsr", "Hasorat"): "hasra", ("Hsr", "HasorataY`"): "ya hasrata",
    ("Hsr", "m~aHosuwr"): "mahsur (contested)",
    ("krr", "kar~ap"): "karra (a return)", ("frT", "far~aT"): "farrata (neglected)",
    ("EDD", "EaD~u"): "bite", ("Erf", "{Eotarafu"): "i'tarafa (confessed)",
}
LAYTA_PREFIX = "layot"
FORMULAS = {
    "ya waylata / ya waylana": "يويلت|يويلنا",
    "irji'un / farji'na": "ارجعون|فارجعنا",
    "akhkhirna / akhkhartani": "اخرنا الي اجل|اخرتني",
    "akhrijna (from the Fire)": "ربنا اخرجنا",
    "nuradd / maradd (sent back)": "يليتنا نرد|او نرد|مرد من سبيل|لا مرد له",
    "khuruj min sabil": "خروج من سبيل",
    "yuqallibu kaffayhi": "يقلب كفيه", "suqita fi aydihim": "سقط في ايديهم",
    "law kunna nasma'u": "لو كنا نسمع", "law anna lana/li karratan": "لو ان لنا كرة|لو ان لي كرة",
    "innā kunnā zalimin (human)": "انا كنا ظلمين",
    "min qabli an ya'tiya (before it comes)": "من قبل ان ياتي",
    "qaddamat (hands sent forward)": "قدمت ايدي|قدمت يداه|قدمت لحياتي|قدمت لغد",
    "yawm al-hasra / al-taghabun": "يوم الحسرة|يوم التغابن",
    "la tas'aw / la tas (do not grieve over)": "تاسوا|فلا تاس",
}

# ORCHESTRATOR ANNOTATION — a reading, not a count. (setting, person, kind, gloss)
CORE = {
    "5:31": ("L", "S", "self", "Cain: unable even to bury his brother"),
    "5:52": ("L", "N", "self", "hedgers: regret over what they hid in themselves"),
    "23:40": ("D", "N", "self", "rejecters: 'in a little while they will be regretful'"),
    "26:157": ("D", "N", "self", "Thamud after hamstringing the she-camel"),
    "49:6": ("L", "N", "self", "acting on an unverified report"),
    "10:54": ("H", "N", "self", "concealed regret on seeing the punishment"),
    "34:33": ("H", "N", "self", "followers and leaders conceal regret"),
    "2:167": ("H", "P", "self", "followers: deeds shown to them as regrets"),
    "6:31": ("H", "P", "self", "'alas for what we neglected' when the Hour comes suddenly"),
    "8:36": ("L", "N", "self", "wealth spent to block the way becomes regret"),
    # Phase-1 verdict: mahsur = depleted/denuded (0/4 translators say "regretful"); not regret.
    "17:29": ("L", "N", "control", "mahsur = depleted, not regretful (excluded after Phase 1)"),
    "19:39": ("H", "N", "self", "the Day of Regret, 'while they are in heedlessness'"),
    "39:56": ("H", "S", "self", "'alas for what I neglected in regard to God'"),
    "69:50": ("H", "N", "self", "the Quran will be a regret for the deniers"),
    "3:156": ("L", "N", "false", "the 'if only they had stayed' made a regret in their hearts"),
    "35:8": ("L", "N", "other", "do not let your soul go out in regrets over them"),
    "36:30": ("L", "N", "other", "'alas for the servants'"),
    "4:73": ("L", "S", "false", "hanger-back: 'if only I had been with them — great win'"),
    "6:27": ("H", "P", "self", "'if only we were sent back and did not deny'"),
    "18:42": ("L", "S", "self", "garden-owner: 'if only I had not associated anyone'"),
    "19:23": ("L", "S", "wish", "Maryam: 'if only I had died before this'"),
    "25:27": ("H", "S", "self", "wrongdoer bites his hands: 'if only I had taken a way with the Messenger'"),
    "25:28": ("H", "S", "self", "'if only I had not taken so-and-so as a friend'"),
    "28:79": ("L", "P", "false", "admirers of Qarun: 'if only we had what he was given'"),
    "33:66": ("H", "P", "self", "'if only we had obeyed God and the Messenger'"),
    "36:26": ("H", "S", "wish", "the martyr: 'if only my people knew'"),
    "43:38": ("H", "S", "self", "to his companion-devil: 'if only between me and you were the two easts'"),
    "69:25": ("H", "S", "self", "'if only I had not been given my record'"),
    "69:27": ("H", "S", "self", "'if only death had been the end'"),
    "78:40": ("H", "S", "self", "'if only I were dust'"),
    "89:24": ("H", "S", "self", "'if only I had sent ahead for my life'"),
    "18:49": ("H", "P", "self", "the record leaves out nothing small or great"),
    "21:14": ("D", "P", "self", "destroyed towns: 'woe to us, we were wrongdoers'"),
    "21:46": ("D", "P", "self", "a breath of punishment touches them"),
    "21:97": ("H", "P", "self", "'we were in heedlessness of this'"),
    "36:52": ("H", "P", "self", "'who raised us from our sleeping place?'"),
    "37:20": ("H", "P", "self", "'this is the Day of Recompense'"),
    "68:31": ("L", "P", "self", "garden-people: 'woe to us, we were transgressors'"),
    "11:72": ("L", "S", "control", "Sarah: surprise at a son in old age"),
    "26:102": ("H", "P", "self", "'if only we had a return, we would be believers'"),
    "39:58": ("H", "S", "self", "'if only I had a return, I would be a doer of good'"),
    "23:99": ("D", "S", "self", "at death: 'my Lord, send me back'"),
    "23:107": ("H", "P", "self", "'bring us out; if we return, we are wrongdoers'"),
    "32:12": ("H", "P", "self", "'we have seen and heard, send us back'"),
    "35:37": ("H", "P", "self", "'bring us out, we will do righteousness, other than what we did'"),
    "7:53": ("H", "P", "self", "'are there intercessors, or could we be sent back?'"),
    "14:44": ("D", "P", "self", "'delay us for a short term'"),
    "40:11": ("H", "P", "self", "'we confess our sins — is there a way out?'"),
    "42:44": ("H", "P", "self", "'is there any way back?'"),
    "63:10": ("D", "S", "self", "at death: 'if only You would delay me a little, I would give charity'"),
    "3:30": ("H", "N", "self", "a soul wishes a vast distance between it and its evil"),
    "4:42": ("H", "N", "self", "deniers wish the earth were levelled over them"),
    "15:2": ("H", "N", "self", "deniers will wish they had been Muslims"),
    "70:11": ("H", "N", "self", "the guilty would ransom himself with his children"),
    "7:149": ("L", "N", "self", "calf-worshippers: it fell into their hands"),
    "12:80": ("L", "N", "self", "Joseph's brothers: 'what you neglected concerning Joseph'"),
    "67:10": ("H", "P", "self", "'if we had listened or reasoned'"),
    "67:11": ("H", "N", "self", "they confess their sin"),
    "68:29": ("L", "P", "self", "garden-people: 'we were wrongdoers'"),
    "12:91": ("L", "P", "self", "Joseph's brothers: 'we were sinners'"),
    "12:97": ("L", "P", "self", "brothers to Jacob: 'ask forgiveness for us'"),
    "9:102": ("L", "N", "self", "others confessed their sins, mixed deeds"),
    "7:5": ("D", "P", "self", "towns: their only cry 'we were wrongdoers'"),
    "10:90": ("D", "S", "self", "Pharaoh drowning: 'I believe'"),
    "40:84": ("D", "P", "self", "'we believe in God alone' on seeing Our might"),
}


def main():
    q = json.load(open(os.path.join(ROOT, "data/arabic/quran.json")))
    text = {f'{s["number"]}:{a["ayah"]}': norm(a["text"]) for s in q["surahs"] for a in s["ayahs"]}
    revelation = {s["number"]: s["revelation"] for s in q["surahs"]}

    markers = defaultdict(list)
    ayah_roots = defaultdict(set)
    for line in open(os.path.join(ROOT, "data/morphology/words.jsonl")):
        w = json.loads(line)
        ref = f'{w["surah"]}:{w["ayah"]}'
        if w["root"]:
            ayah_roots[ref].add(w["root"])
        lab = LEMMA_MARKERS.get((w["root"], w["lemma"]))
        if lab:
            markers[lab].append(ref)
        if w["lemma"] and w["lemma"].startswith(LAYTA_PREFIX):
            markers["layta (if only)"].append(ref)
    for lab, pat in FORMULAS.items():
        markers[lab] = [r for r, t in text.items() if re.search(pat, t)]
    markers = {k: sorted(set(v), key=lambda r: tuple(map(int, r.split(":")))) for k, v in markers.items()}

    self_set = [r for r, v in CORE.items() if v[2] == "self"]
    setting = Counter(CORE[r][0] for r in self_set)
    person = Counter(CORE[r][1] for r in self_set)
    sp = Counter((CORE[r][0], CORE[r][1]) for r in self_set)
    kinds = Counter(v[2] for v in CORE.values())
    rev = Counter(revelation[int(r.split(":")[0])] for r in self_set)

    # Root lift in self-regret ayahs vs the whole corpus.
    n_all = len(ayah_roots)
    corpus = Counter(r for rs in ayah_roots.values() for r in rs)
    inset = Counter(r for a in self_set for r in ayah_roots[a])
    lift = []
    for r, c in inset.items():
        if c >= 3:
            lift.append({"root": r, "in_regret_ayahs": c, "of": len(self_set),
                         "corpus_ayahs": corpus[r],
                         "lift": round((c / len(self_set)) / (corpus[r] / n_all), 2)})
    lift.sort(key=lambda d: -d["lift"])

    div = json.load(open(os.path.join(ROOT, "data/structural/translation-divergence.json")))
    divergence = sorted(({"ref": r, "combined": div[r]["scores"]["combined"]} for r in CORE if r in div),
                        key=lambda d: -d["combined"])

    out = {
        "note": "Phase-0 census for the regret investigation. 'core' annotations are an "
                "orchestrator reading (setting/person/kind), everything else is counted.",
        "markers": {k: {"count": len(v), "refs": v} for k, v in markers.items()},
        "core": {r: dict(zip(["setting", "person", "kind", "gloss"], v)) for r, v in CORE.items()},
        "summary": {"core_ayahs": len(CORE), "kinds": dict(kinds), "self_regret_ayahs": len(self_set),
                    "self_by_setting": dict(setting), "self_by_person": dict(person),
                    "self_by_setting_person": {f"{a}-{b}": c for (a, b), c in sorted(sp.items())},
                    "self_by_revelation": dict(rev)},
        "root_lift_self_regret": lift[:40],
        "divergence_core": divergence,
    }
    dest = os.path.join(ROOT, "data/structural/regret-census.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, indent=1)
    print(f"wrote {dest}")
    for k, v in out["markers"].items():
        print(f"  {k:42} {v['count']:3}  {v['refs'] if v['count'] <= 16 else v['refs'][:16]}")
    print("summary:", json.dumps(out["summary"]))
    print("lift top:", [(d["root"], d["in_regret_ayahs"], d["lift"]) for d in lift[:30]])
    print("divergence top:", divergence[:12])


if __name__ == "__main__":
    main()
