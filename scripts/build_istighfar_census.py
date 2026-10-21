#!/usr/bin/env python3
"""Phase-0 census for the istighfar investigation. Deterministic.

  1. gfr lemma table.
  2. istaghfara (form X, "seek forgiveness") and ghafara (form I) by tense/person —
     the imperative audit: who is told to seek forgiveness, and who asks God directly.
  3. The petition set (every quoted request to God for forgiveness) with the roots
     that travel inside the same ayah: mercy, repentance, pardon, expiation, faith,
     self-wrong confession.
  4. Root lift: what is over-represented in istighfar ayahs vs the corpus.
  5. The divine names paired with ghafur, and where they fall.
  6. Translator divergence over the core set.
Emits data/structural/istighfar-census.json.
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


def key(r):
    return tuple(map(int, r.split(":")))


# Quoted petitions to God for forgiveness that are NOT `ighfir` imperatives.
EXTRA_PETITIONS = {"7:23": "wa-in lam taghfir lana (conditional)", "11:47": "wa-illa taghfir li (conditional)",
                   "2:285": "ghufranaka (verbal noun)", "26:82": "atma'u an yaghfira li (hope)",
                   "5:118": "wa-in taghfir lahum (Isa, for others)"}
INSIDE = {"rHm": "mercy", "twb": "repentance", "Efw": "pardon", "kfr": "expiation/denial",
          "Amn": "faith", "Zlm": "wrong", "*nb": "sin", "slm": "peace/submission", "nwr": "light"}
NAME_PAIRS = {"ghafur rahim": "غفور رحيم|الغفور الرحيم|غفورا رحيما", "afuww ghafur": "عفو غفور|عفوا غفورا",
              "ghafur halim": "غفور حليم|غفورا حليما", "ghafur shakur": "غفور شكور",
              "al-ghafur al-wadud": "الغفور الودود", "aziz + ghafur/ghaffar": "العزيز الغفور|العزيز الغفر|عزيز غفور",
              "wasi al-maghfira": "وسع المغفرة", "dhu maghfira": "ذو مغفرة|لذو مغفرة",
              "tawwab rahim": "تواب رحيم|التواب الرحيم|توابا رحيما"}


def main():
    q = json.load(open(os.path.join(ROOT, "data/arabic/quran.json")))
    text = {f'{s["number"]}:{a["ayah"]}': norm(a["text"]) for s in q["surahs"] for a in s["ayahs"]}
    rev = {s["number"]: s["revelation"] for s in q["surahs"]}
    lem = Counter(); lem_refs = defaultdict(list)
    forms = defaultdict(list)
    ayah_roots = defaultdict(set)
    for line in open(os.path.join(ROOT, "data/morphology/words.jsonl")):
        w = json.loads(line)
        ref = f'{w["surah"]}:{w["ayah"]}'
        if w["root"]:
            ayah_roots[ref].add(w["root"])
        if w["root"] != "gfr":
            continue
        lem[(w["lemma"], w["pos"])] += 1
        lem_refs[f'{w["lemma"]} {w["pos"]}'].append(ref)
        if w["pos"] == "V":
            fl = w.get("flags", [])
            t = "/".join(x for x in fl if x in ("PERF", "IMPF", "IMPV"))
            p = "/".join(x for x in fl if x[:1] in "123")
            forms[f'{w["lemma"]} {t} {p}'].append(ref)

    istighfar = sorted({r for k, v in forms.items() if k.startswith("{sotagofara") for r in v}, key=key)
    istighfar_ayahs = sorted(set(istighfar) | set(lem_refs.get("musotagofiriyn N", []))
                             | set(lem_refs.get("{sotigofaAr N", [])), key=key)
    ighfir = sorted(set(forms.get("gafara IMPV 2MS", [])), key=key)
    petitions = sorted(set(ighfir) | set(EXTRA_PETITIONS), key=key)
    pet_rows = []
    for r in petitions:
        pet_rows.append({"ref": r, "form": EXTRA_PETITIONS.get(r, "ighfir (imperative to God)"),
                         "with": [f"{k} ({v})" for k, v in INSIDE.items() if k in ayah_roots[r]],
                         "revelation": rev[key(r)[0]]})
    inside_counts = Counter(k for r in petitions for k in INSIDE if k in ayah_roots[r])

    n_all = len(ayah_roots)
    corpus = Counter(r for rs in ayah_roots.values() for r in rs)
    core = sorted(set(istighfar_ayahs) | set(petitions), key=key)
    inset = Counter(r for a in core for r in ayah_roots[a] if r != "gfr")
    lift = sorted(({"root": r, "in_core": c, "of": len(core), "corpus_ayahs": corpus[r],
                    "lift": round((c / len(core)) / (corpus[r] / n_all), 2)}
                   for r, c in inset.items() if c >= 3), key=lambda d: -d["lift"])

    pairs = {k: [r for r, t in text.items() if re.search(p, t)] for k, p in NAME_PAIRS.items()}
    div = json.load(open(os.path.join(ROOT, "data/structural/translation-divergence.json")))
    divergence = sorted(({"ref": r, "combined": div[r]["scores"]["combined"]} for r in core if r in div),
                        key=lambda d: -d["combined"])

    out = {
        "note": "Phase-0 census for the istighfar investigation. All counted.",
        "lemmas": [{"lemma": l, "pos": p, "count": c} for (l, p), c in lem.most_common()],
        "lemma_refs": lem_refs,
        "verb_forms": {k: sorted(set(v), key=key) for k, v in sorted(forms.items(), key=lambda kv: -len(kv[1]))},
        "istighfar_ayahs": istighfar_ayahs,
        "petitions": pet_rows,
        "petition_inside_counts": dict(inside_counts),
        "core_ayahs": core,
        "core_by_revelation": dict(Counter(rev[key(r)[0]] for r in core)),
        "root_lift_core": lift[:40],
        "divine_name_pairs": {k: {"count": len(v), "refs": v} for k, v in pairs.items()},
        "divergence_core": divergence,
    }
    dest = os.path.join(ROOT, "data/structural/istighfar-census.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, indent=1)
    print(f"wrote {dest}")
    print("istighfar ayahs", len(istighfar_ayahs), "| petitions", len(petitions), "| core", len(core),
          out["core_by_revelation"])
    print("inside petitions:", dict(inside_counts))
    for r in pet_rows: print("  ", r["ref"], r["form"][:28], r["with"])
    print("lift:", [(d["root"], d["in_core"], d["lift"]) for d in lift[:28]])
    print("pairs:", {k: v["count"] for k, v in out["divine_name_pairs"].items()})
    print("divergence:", divergence[:12])


if __name__ == "__main__":
    main()
