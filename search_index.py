# -*- coding: utf-8 -*-
"""Yayındaki sayfalardan arama dizini üretir: <repo>/ara-tr.json, ara-en.json ve ara-de.json
Kullanım: search_index.py <repo>"""
import json, os, re, sys
from bs4 import BeautifulSoup
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from i18n_map import EN, MAPS

R = sys.argv[1]
SKIP_PAGES = {"bilgi.html"}          # kategori sayfası: kartlar zaten diğer sayfaları tekrarlar
BLOCK = {"h1", "h2", "h3", "h4", "summary", "p", "li", "td", "th", "figcaption", "blockquote", "dt", "dd"}
HEAD = {"h1", "h2", "h3", "h4", "summary"}
BLOCK_CLS = {"stat", "dose"}
EX_TAGS = {"script", "style", "noscript", "svg", "template", "button", "nav", "footer", "dialog", "select", "iframe"}
EX_CLS = {"sources", "more", "ctacard", "bar", "fab", "lang", "eyebrow", "meta", "back", "kose", "kose-more",
          "cats", "sfield", "mr-strings", "m-strings", "sr-only", "trio", "trio-k", "hx"}
TYPE = {"hastalik rehberi": "c", "condition guide": "c", "krankheitsratgeber": "c",
        "rehabilitasyon rehberi": "r", "rehabilitation guide": "r", "reha-ratgeber": "r",
        "kendine iyi bak": "s", "look after yourself": "s", "gut fur sich sorgen": "s"}
HOME = {"tr": ("Ana sayfa", "Evde fizyoterapi hizmeti"), "en": ("Home", "Home physiotherapy service"),
        "de": ("Startseite", "Physiotherapie zu Hause")}
TOOL = {"tr": "Egzersiz reçetesi", "en": "Exercise plan", "de": "Übungsplan"}


def clean(t):
    return re.sub(r"\s+", " ", t).strip()


def fold(t):
    return t.lower().translate(str.maketrans("çğıöşüİä", "cgiosuia"))


def excluded(el):
    for a in [el] + list(el.parents):
        if a.name in EX_TAGS:
            return True
        cls = set(a.get("class") or []) if hasattr(a, "get") else set()
        if cls & EX_CLS:
            return True
        if hasattr(a, "get") and (a.get("hidden") is not None or a.get("aria-hidden") == "true"):
            return True
        if a.name == "section" and a.get("id") == "bilgi":
            return True
    return False


def is_block(el):
    return el.name in BLOCK or bool(set(el.get("class") or []) & BLOCK_CLS)


def page(path, fname, lang):
    soup = BeautifulSoup(open(path, encoding="utf-8").read(), "lxml")
    desc = soup.find("meta", attrs={"name": "description"})
    desc = clean(desc["content"]) if desc else ""
    body = soup.body
    h1 = body.find("h1")
    title = clean(h1.get_text(" ")) if h1 else clean(soup.title.get_text()).split(" | ")[0]
    k = ""
    hdr = body.find("header", class_="page")
    if hdr:
        eb = hdr.find(class_="eyebrow")
        k = clean(eb.get_text(" ")) if eb else ""
    typ = TYPE.get(fold(k), "c")
    if fname == "yenilikler.html":
        typ = "n"
    if fname == "index.html":
        k, title = HOME[lang]
        typ = "h"
    if fname == "recete.html":
        k, typ = TOOL[lang], "t"
    for s in body.find_all(["svg", "script", "style"]):
        s.decompose()
    blocks = [el for el in body.find_all(True) if is_block(el) and not excluded(el)]
    bset = set(map(id, blocks))
    blocks = [el for el in blocks if not any(id(p) in bset for p in el.parents)]
    secs, cur, seen = [], ["", []], set()
    for el in blocks:
        t = clean(el.get_text(" "))
        if len(t) < 2:
            continue
        if el.name == "h1":
            continue
        if el.name in HEAD:
            if cur[1] or cur[0]:
                secs.append(cur)
            cur = [t, []]
            continue
        if t in seen or t == desc:
            continue
        seen.add(t)
        cur[1].append(t)
    if cur[1] or cur[0]:
        secs.append(cur)
    secs = [s for s in secs if s[1] or s[0]]
    rel = fname if lang == "tr" else lang + "/" + MAPS[lang][fname]
    return {"u": rel, "t": title, "k": k, "i": typ, "d": desc, "s": secs}


def build(lang):
    pages = []
    for f in EN:
        if f in SKIP_PAGES:
            continue
        path = os.path.join(R, f) if lang == "tr" else os.path.join(R, lang, MAPS[lang][f])
        if not os.path.exists(path):
            continue
        pages.append(page(path, f, lang))
    out = os.path.join(R, f"ara-{lang}.json")
    data = json.dumps({"v": 1, "p": pages}, ensure_ascii=False, separators=(",", ":"))
    open(out, "w", encoding="utf-8").write(data)
    print(lang, len(pages), "sayfa,", sum(len(p["s"]) for p in pages), "bölüm,", len(data.encode()) // 1024, "KB")


build("tr")
for _l in MAPS:
    if os.path.isdir(os.path.join(R, _l)):
        build(_l)
