# -*- coding: utf-8 -*-
"""Çeviri dosyasını doğrular.  Kullanım: python3 check.py <ad>   (ör. bel-agrisi)
todo/<ad>.json ile done/<ad>.json karşılaştırılır."""
import sys, os, re, json, collections

D = os.path.dirname(os.path.abspath(__file__))
TRCH = re.compile(r"[çğıöşüÇĞŞÖÜ]|İ(?!hsan)")
TAG = re.compile(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)([^>]*)>")
ALLOW_TR = ("Stresli Anlarda Ne Yapmalı?: Resimli Rehber", "Özerkan", "İhsan", "Türkçe", "Kadıköy", "Üsküdar", "Beşiktaş", "Şişli", "Ataşehir", "Bakırköy", "Rosén", "Peña", "Araújo", "Ölçüm", "Yıldız", "Maçka", "Gülhane", "Atatürk", "Rumelihisarı", "Validebağ", "Fenerbahçe", "Göztepe", "Çamlıca", "Polonezköy", "Büyükada", "Büyük Çamlıca")


def tags(h):
    out = collections.Counter()
    for m in TAG.finditer(h):
        close, name, attrs = m.groups()
        keep = ""
        if not close:
            hrefs = re.findall(r'(?:href|src|class)="[^"]*"', attrs)
            keep = " ".join(sorted(hrefs))
        out[(close, name.lower(), keep)] += 1
    return out


def main(name):
    todo = json.load(open(os.path.join(D, "todo", name + ".json"), encoding="utf-8"))
    try:
        done = json.load(open(os.path.join(D, "done", name + ".json"), encoding="utf-8"))
    except Exception as e:
        print("JSON OKUNAMADI:", e)
        return 1
    errs = []
    for it in todo:
        i, tr = it["id"], it["tr"]
        if i not in done:
            errs.append(f"{i}: eksik")
            continue
        en = done[i]
        if not isinstance(en, str) or not en.strip():
            errs.append(f"{i}: boş")
            continue
        for ph in re.findall(r"\[\[\d+\]\]", tr):
            if en.count(ph) != 1:
                errs.append(f"{i}: yer tutucu {ph} tam bir kez olmalı")
        if it["kind"] == "text":
            if tags(tr) != tags(en):
                errs.append(f"{i}: etiketler farklı\n    tr={sorted(tags(tr).items())}\n    en={sorted(tags(en).items())}")
        else:
            if "<" in en and "<" not in tr:
                errs.append(f"{i}: düz metinde etiket olmamalı")
        t = en
        for a in sorted(ALLOW_TR, key=len, reverse=True):
            t = t.replace(a, "")
        if TRCH.search(re.sub(r'href="[^"]*"', "", t)):
            errs.append(f"{i}: Türkçe karakter kaldı: {en[:90]!r}")
        if re.search(r"appointment|randevu", en, re.I):
            errs.append(f"{i}: 'appointment/randevu' kullanılmamalı")
        if re.search(r"(?<![&\w#])(amp|quot|lt|gt);", en):
            errs.append(f"{i}: bozuk karakter referansı olabilir")
    extra = set(done) - {it["id"] for it in todo}
    if extra:
        errs.append(f"fazladan id: {sorted(extra)[:10]}")
    for e in errs:
        print(e)
    print(f"{name}: {len(todo)} birim, {len(errs)} sorun")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(max(main(n) for n in sys.argv[1:]))
