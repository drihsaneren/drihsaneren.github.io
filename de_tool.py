# -*- coding: utf-8 -*-
"""Almanca çeviri için yardımcı: JSON ve tırnak kaçışlarıyla uğraşmadan, satır satır çalışmayı sağlar.

  de_tool.py export <ad> [<ad> ...]      -> stdout:  ## ad  /  id<TAB>tür<TAB>metin
        Metindeki HTML etiketleri {1}, {2}... yer tutucularına çevrilir ([[n]] simge yer tutucuları aynen kalır).
  de_tool.py import <dosya.tsv>          -> i18n/done_de/<ad>.json
        Satırlar:  ## ad   |   id<TAB>Almanca metin   ({n} yer tutucuları her biri tam bir kez)
        Kısayollar:  id<TAB>==   (Türkçe kaynağı aynen kullan: adlar, İngilizce kaynakça)
                     id<TAB>=en  (İngilizce çeviriyi aynen kullan)
  de_tool.py left                        -> henüz Almancası olmayan dosyalar ve birim sayıları
"""
import sys, os, re, json, glob

HERE = os.path.dirname(os.path.abspath(__file__))
I18N = os.path.join(HERE, "i18n")
TAG = re.compile(r"<[^>]+>")


def load(kind, name):
    p = os.path.join(I18N, kind, name + ".json")
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else None


def mask(tr):
    tags = TAG.findall(tr)
    n = [0]
    def sub(m):
        n[0] += 1
        return "{%d}" % n[0]
    return TAG.sub(sub, tr), tags


def export(names):
    for name in names:
        todo = load("todo", name)
        print("## " + name)
        for it in todo:
            t = it["tr"]
            assert not re.search(r"\{\d+\}", t), (name, it["id"])
            if it["kind"] == "text":
                t, _ = mask(t)
            assert "\n" not in t and "\t" not in t, (name, it["id"])
            print(f'{it["id"]}\t{it["kind"]}\t{t}')


def imp(path):
    cur, data, errs = None, {}, []
    for ln, line in enumerate(open(path, encoding="utf-8").read().split("\n"), 1):
        if not line.strip():
            continue
        if line.startswith("## "):
            cur = line[3:].strip(); data[cur] = {}
            continue
        if "\t" not in line:
            errs.append(f"satır {ln}: sekme yok: {line[:60]!r}"); continue
        i, de = line.split("\t", 1)
        if "\t" in de:                      # export satırı aynen yapıştırıldıysa tür sütununu at
            k, rest = de.split("\t", 1)
            if k in ("text", "attr", "wa", "ld"):
                de = rest
        data[cur][i.strip()] = de.strip()
    for name, got in data.items():
        todo = load("todo", name); en = load("done", name) or {}
        if todo is None:
            errs.append(f"{name}: todo dosyası yok"); continue
        out = {}
        ids = [it["id"] for it in todo]
        for x in set(got) - set(ids):
            errs.append(f"{name}/{x}: bilinmeyen kimlik")
        for it in todo:
            i, tr = it["id"], it["tr"]
            if i not in got:
                errs.append(f"{name}/{i}: eksik"); continue
            de = got[i]
            if de == "==":
                out[i] = tr; continue
            if de == "=en":
                out[i] = en[i]; continue
            if it["kind"] == "text":
                _, tags = mask(tr)
                used = [int(x) for x in re.findall(r"\{(\d+)\}", de)]
                if sorted(used) != list(range(1, len(tags) + 1)):
                    errs.append(f"{name}/{i}: yer tutucular {sorted(used)} olmalı 1..{len(tags)}"); continue
                de = re.sub(r"\{(\d+)\}", lambda m: tags[int(m.group(1)) - 1], de)
            elif re.search(r"\{\d+\}", de):
                errs.append(f"{name}/{i}: düz metinde yer tutucu olmamalı"); continue
            for ph in re.findall(r"\[\[\d+\]\]", tr):
                if de.count(ph) != 1:
                    errs.append(f"{name}/{i}: {ph} tam bir kez olmalı")
            out[i] = de
        os.makedirs(os.path.join(I18N, "done_de"), exist_ok=True)
        json.dump(out, open(os.path.join(I18N, "done_de", name + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"{name}: {len(out)}/{len(todo)} birim yazıldı")
    for e in errs:
        print("HATA", e)
    return 1 if errs else 0


def left():
    tot = 0
    for tf in sorted(glob.glob(os.path.join(I18N, "todo", "*.json"))):
        name = os.path.basename(tf)[:-5]
        todo = json.load(open(tf, encoding="utf-8")); done = load("done_de", name) or {}
        miss = [it for it in todo if it["id"] not in done]
        if miss:
            c = sum(len(it["tr"]) for it in miss); tot += c
            print(f"{name}\t{len(miss)}\t{c}")
    print("kalan karakter:", tot)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "export":
        export(sys.argv[2:])
    elif cmd == "import":
        sys.exit(imp(sys.argv[2]))
    elif cmd == "left":
        left()
