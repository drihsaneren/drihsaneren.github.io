# Değişen sayfaların bellekte olmayan çeviri birimlerini tek bir yeni i18n/todo/<ad>.json dosyasında toplar (export_todo ve mevcut todo dosyalarına dokunmaz).
# Kullanım: REPO=<main-dizini> python3 collect_todo.py <ad> <sayfa.html> [...]  ->  i18n/done/<ad>.json yaz, python3 i18n/check.py <ad>
import sys, os, json
sys.path.insert(0, os.getcwd())
from i18n_core import units, plain, ld_blocks, ld_strings
from make_en import load_mem, _unph
import export_todo as X
src = os.environ["REPO"]; name = sys.argv[1]; pages = sys.argv[2:]
mem = load_mem()
I18N = os.path.join(os.getcwd(), "i18n")
ident = set(json.load(open(os.path.join(I18N, "identity.json"), encoding="utf-8")))
seen, items = set(), []
for f in pages:
    s = open(os.path.join(src, f), encoding="utf-8").read()
    derivable = set()
    for u in units(s):
        derivable.add(plain(_unph(u.key)))
        k = u.key
        if k in mem or k in seen or k in ident: continue
        if u.kind == "text" and X.english_ref(k):
            ident.add(k); continue
        seen.add(k); items.append({"kind": u.kind, "tr": k, "page": f})
    for a, b, body in ld_blocks(s):
        for v in ld_strings(json.loads(body)):
            if v in derivable or v in mem or v in seen: continue
            seen.add(v); items.append({"kind": "ld", "tr": v, "page": f})
out = [{"id": f"{name}-{i}", "kind": it["kind"], "tr": it["tr"]} for i, it in enumerate(items)]
json.dump(out, open(os.path.join(I18N, "todo", name + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(sorted(ident), open(os.path.join(I18N, "identity.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for i, it in enumerate(items): print(f"{name}-{i}\t{it['page']}\t{it['kind']}\t{it['tr']}")
