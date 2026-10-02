# -*- coding: utf-8 -*-
"""Her sayfa için henüz çevrilmemiş birimleri i18n/todo/<sayfa>.json olarak yazar.
Kullanım: export_todo.py <tr-kaynak-dizini> [sayfa.html ...]"""
import sys, os, re, json, glob
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from i18n_core import units, plain, ld_blocks, ld_strings
from i18n_map import EN
from make_en import load_mem, _unph

I18N = os.path.join(HERE, "i18n")
TRCH = re.compile(r"[çğıöşüÇĞİÖŞÜ]")
TRWORDS = re.compile(r"\b(Londra|Cenevre|Erişim|erişim|Türkçe|güncelleme|sayfa|Yayın|ve|ile|için|bir|Ankara|Sağlık|Bakanlığı)\b")


def english_ref(k):
    t = plain(k)
    return (not TRCH.search(t) and not TRWORDS.search(t) and re.search(r"\b(19|20)\d\d\b", t)
            and re.search(r"et al\.|doi|;\s*\d|Physiopedia|NICE|WHO|NHS|\d+\(\d+\)", t))


def main():
    src = sys.argv[1]
    pages = sys.argv[2:] or sorted(EN)
    mem = load_mem()
    ident = set(json.load(open(os.path.join(I18N, "identity.json"), encoding="utf-8"))) if os.path.exists(os.path.join(I18N, "identity.json")) else set()
    for f in pages:
        s = open(os.path.join(src, f), encoding="utf-8").read()
        us = units(s)
        seen, items = set(), []
        derivable = set()
        for u in us:
            derivable.add(plain(_unph(u.key)))
            k = u.key
            if k in mem or k in seen:
                continue
            if u.kind == "text" and english_ref(k):
                ident.add(k)
                continue
            seen.add(k)
            items.append({"kind": u.kind, "tr": k})
        for a, b, body in ld_blocks(s):
            for v in ld_strings(json.loads(body)):
                if v in derivable or v in mem or v in seen:
                    continue
                seen.add(v)
                items.append({"kind": "ld", "tr": v})
        name = f[:-5]
        for i, it in enumerate(items):
            it["id"] = f"{name[:3]}{i}"
        items = [{"id": it["id"], "kind": it["kind"], "tr": it["tr"]} for it in items]
        json.dump(items, open(os.path.join(I18N, "todo", name + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f, len(items), sum(len(it["tr"]) for it in items))
    json.dump(sorted(ident), open(os.path.join(I18N, "identity.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("özdeş (İngilizce kaynakça):", len(ident))


if __name__ == "__main__":
    main()
