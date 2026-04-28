"""Buckwalter <-> Arabic transliteration.

The Quranic Arabic Corpus encodes Arabic in Buckwalter so the data can travel
through ASCII-only pipelines. This module converts back to Unicode Arabic so
text is human-readable.
"""

# Map: Buckwalter char -> Arabic Unicode char.
BUCK_TO_AR = {
    "'": "ء",  # ء  hamza
    "|": "آ",  # آ  alif madda
    ">": "أ",  # أ  alif with hamza above
    "&": "ؤ",  # ؤ  waw with hamza
    "<": "إ",  # إ  alif with hamza below
    "}": "ئ",  # ئ  yeh with hamza
    "A": "ا",  # ا  alif
    "b": "ب",  # ب
    "p": "ة",  # ة  ta marbuta
    "t": "ت",  # ت
    "v": "ث",  # ث
    "j": "ج",  # ج
    "H": "ح",  # ح
    "x": "خ",  # خ
    "d": "د",  # د
    "*": "ذ",  # ذ
    "r": "ر",  # ر
    "z": "ز",  # ز
    "s": "س",  # س
    "$": "ش",  # ش
    "S": "ص",  # ص
    "D": "ض",  # ض
    "T": "ط",  # ط
    "Z": "ظ",  # ظ
    "E": "ع",  # ع
    "g": "غ",  # غ
    "_": "ـ",  # ـ  tatweel
    "f": "ف",  # ف
    "q": "ق",  # ق
    "k": "ك",  # ك
    "l": "ل",  # ل
    "m": "م",  # م
    "n": "ن",  # ن
    "h": "ه",  # ه
    "w": "و",  # و
    "Y": "ى",  # ى  alif maksura
    "y": "ي",  # ي
    "F": "ً",  # ً  fathatan
    "N": "ٌ",  # ٌ  dammatan
    "K": "ٍ",  # ٍ  kasratan
    "a": "َ",  # َ  fatha
    "u": "ُ",  # ُ  damma
    "i": "ِ",  # ِ  kasra
    "~": "ّ",  # ّ  shadda
    "o": "ْ",  # ْ  sukun
    "`": "ٰ",  # ٰ  superscript alif (dagger alif)
    "{": "ٱ",  # ٱ  alif wasla
    # Extended (very rare in Quranic text; included for completeness):
    "P": "پ",  # پ
    "J": "چ",  # چ
    "V": "ڤ",  # ڤ
    "G": "گ",  # گ
}

AR_TO_BUCK = {v: k for k, v in BUCK_TO_AR.items()}


def to_arabic(s: str) -> str:
    return "".join(BUCK_TO_AR.get(c, c) for c in s)


def to_buckwalter(s: str) -> str:
    return "".join(AR_TO_BUCK.get(c, c) for c in s)
