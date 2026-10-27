# eczacı -> hekim. Kullanım: python3 ecz.py apply   (TR kaynaklarını değiştirir ve TR->EN eşlemesini kaydeder)
import re, sys, os, glob, json
os.chdir("/home/claude/drihsaneren.github.io"); sys.path.insert(0, os.getcwd())
TR = [
 ("çocuğunuzun hekimine ya da eczacınıza", "çocuğunuzun hekimine"),
 ("hekiminize ya da eczacınıza", "hekiminize"), ("Hekiminize ya da eczacınıza", "Hekiminize"),
 ("eczacınıza ya da hekiminize", "hekiminize"), ("Eczacınıza ya da hekiminize", "Hekiminize"),
 ("hekiminizle ya da eczacınızla", "hekiminizle"), ("hekiminize veya eczacınıza", "hekiminize"),
 ("eczacıya ya da hekime", "hekime"),
 ("Uygun ağrı kesiciyi eczacınıza sorabilirsiniz.", "Ağrı kesici kullanmanız gerekiyorsa hekiminize danışın."),
 ("eczacınıza danışabilirsiniz", "hekiminize danışabilirsiniz"), ("eczacınıza danışın", "hekiminize danışın"),
]
def trrep(s):
    for a, b in TR: s = s.replace(a, b)
    return s
EN = [
 ("your child’s doctor or your pharmacist", "your child’s doctor"), ("your child's doctor or your pharmacist", "your child's doctor"),
 ("your doctor or pharmacist", "your doctor"), ("Your doctor or pharmacist", "Your doctor"),
 ("a doctor or pharmacist", "a doctor"), ("your pharmacist or doctor", "your doctor"), ("a pharmacist or doctor", "a doctor"),
 ("pharmacist or doctor", "doctor"), ("doctor or pharmacist", "doctor"), ("your GP or pharmacist", "your doctor"),
 ("your pharmacist", "your doctor"), ("a pharmacist", "a doctor"),
]
def enrep(s):
    for a, b in EN: s = s.replace(a, b)
    return s
if sys.argv[1:] == ["apply"]:
    from make_en import load_mem
    mem = load_mem(); pairs = {}
    for k, v in mem.items():
        if "eczac" in k.lower():
            k2 = trrep(k)
            if k2 != k: pairs[k2] = enrep(v)
    json.dump(pairs, open("ecz_map.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("eşleme:", len(pairs), "| İngilizcede kalan pharmacist:", sum("harmacist" in v for v in pairs.values()))
    ch = []
    for f in glob.glob("*_part.py") + ["build_pages.py"]:
        s = open(f, encoding="utf-8").read(); s2 = trrep(s)
        if s2 != s: open(f, "w", encoding="utf-8").write(s2); ch.append(f)
    print("değişen:", len(ch), sorted(ch))
    left = [(f, m) for f in glob.glob("*_part.py") + ["build_pages.py"] for m in re.findall(r".{40}eczac.{30}", open(f, encoding="utf-8").read())]
    print("kalan:", left)
