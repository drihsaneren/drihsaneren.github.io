# -*- coding: utf-8 -*-
"""TR sayfalardan /en/ ve /de/ altındaki çeviri sayfalarını üretir.
Kullanım: make_lang.py <dil> <tr-kaynak-dizini> <cikis-kok-dizini> [sayfa.html ...]     (dil: en | de)
  - i18n/todo/*.json           : çevrilecek birimler (id, kind, tr), iki dil için ortak
  - i18n/done/*.json           : İngilizce çeviriler {id: en};  i18n/done_de/*.json : Almanca {id: de}
  - i18n/js.json, js_de.json   : sayfa başına [tr, çeviri] betik metni çiftleri
  - i18n/extra.json, extra_de.json : sayfa başına [eski, yeni] ham değişiklikler (çeviriden sonra)
"""
import sys, os, re, json, glob, html as _html
from urllib.parse import quote
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from i18n_core import units, plain, ld_blocks, SKIP_KEYS, LETTER
from i18n_map import EN, MAPS, LANGS, HTML_LOCALE, SITE, switcher, tr_url, lang_url

I18N = os.path.join(HERE, "i18n")
DONE = {"en": "done", "de": "done_de"}
SIDE = {"en": ("js.json", "extra.json"), "de": ("js_de.json", "extra_de.json")}


def load_mem(lang="en"):
    mem = {}
    for tf in sorted(glob.glob(os.path.join(I18N, "todo", "*.json"))):
        df = os.path.join(I18N, DONE[lang], os.path.basename(tf))
        if not os.path.exists(df):
            continue
        todo = json.load(open(tf, encoding="utf-8"))
        done = json.load(open(df, encoding="utf-8"))
        for it in todo:
            if it["id"] in done and done[it["id"]] is not None:
                mem[it["tr"]] = done[it["id"]]
    ident = os.path.join(I18N, "identity.json")
    if os.path.exists(ident):
        for k in json.load(open(ident, encoding="utf-8")):
            mem.setdefault(k, k)
    return mem


def _unph(t):
    return re.sub(r"\[\[\d+\]\]", " ", t)


def rewrite_url(v, lang="en"):
    if not v or v.startswith(("http:", "https:", "mailto:", "tel:", "#", "data:", "javascript:", "../", "/")):
        return v
    m = re.match(r"([^#?]*)(.*)", v)
    p, rest = m.group(1), m.group(2)
    if not p:
        return v
    if p in MAPS[lang]:
        return MAPS[lang][p] + rest
    if p in set(MAPS[lang].values()):
        return v
    return "../" + v



_NUM_NODE = re.compile(r">([^<>]*\d[^<>]*)<")
def _num_fix(t):
    if LETTER.search(t):
        return t
    t = re.sub(r"(?<![\d.,])(\d{1,3}(?:\.\d{3})+)(?![\d.,])", lambda m: m.group(1).replace(".", ","), t)
    t = re.sub(r"(\d),(\d{1,2})(?!\d)", r"\1.\2", t)
    t = re.sub(r"%(\d[\d.,]*(?:\s*[–-]\s*\d[\d.,]*)?)(\+?)", r"\1%\2", t)
    return t
def en_numbers(s):
    parts = re.split(r"(<script[^>]*>.*?</script>|<style[^>]*>.*?</style>)", s, flags=re.S)
    for i in range(0, len(parts), 2):
        parts[i] = _NUM_NODE.sub(lambda m: ">" + _num_fix(m.group(1)) + "<", parts[i])
    return "".join(parts)

def de_numbers(s):
    """Almanca: ondalık virgül ve binlik nokta Türkçeyle aynı; yalnızca yüzde işareti sona gelir (%47 -> 47 %)."""
    def fix(t):
        if LETTER.search(t):
            return t
        return re.sub(r"%(\d[\d.,]*(?:\s*[–-]\s*\d[\d.,]*)?)(\+?)", "\\1\u00a0%\\2", t)
    parts = re.split(r"(<script[^>]*>.*?</script>|<style[^>]*>.*?</style>)", s, flags=re.S)
    for i in range(0, len(parts), 2):
        parts[i] = _NUM_NODE.sub(lambda m: ">" + fix(m.group(1)) + "<", parts[i])
    return "".join(parts)


def make(fname, s, mem, js_pairs, extra, lang="en"):
    miss = []
    # 1) dil seçici
    s, n = re.subn(r'<div class="lang" role="group" aria-label="Dil seçimi">.*?</div>', switcher(fname, lang), s, flags=re.S)
    # 2) metin birimleri
    us = units(s)
    tr_plain = {}
    for u in reversed(us):
        en = mem.get(u.key)
        if en is None:
            miss.append((u.kind, u.key))
            continue
        if u.kind == "text":
            out = en
            for i, (_, _, sv) in enumerate(u.ph):
                tag = f"[[{i + 1}]]"
                assert tag in out, (fname, "yer tutucu yok", tag, u.key[:80])
                out = out.replace(tag, sv, 1)
            tr_plain[plain(_unph(u.key))] = plain(_unph(en))
        elif u.kind == "attr":
            out = en.replace('"', "&quot;")
            tr_plain[plain(u.key)] = plain(en)
        else:  # wa
            out = quote(en, safe="")
        s = s[:u.a] + out + s[u.b:]
    # 3) betik metinleri
    for tr, en in js_pairs:
        cnt = 0
        def rep(m):
            nonlocal cnt
            body = m.group(2)
            if m.group(1).find("ld+json") >= 0:
                return m.group(0)
            c = body.count(tr)
            cnt += c
            return m.group(1) + body.replace(tr, en) + m.group(3)
        s = re.sub(r"(<script[^>]*>)(.*?)(</script>)", rep, s, flags=re.S)
        if cnt == 0:
            miss.append(("js", tr))
    # 4) JSON-LD
    def tx(o, key=None):
        if isinstance(o, dict):
            return {k: tx(v, k) for k, v in o.items()}
        if isinstance(o, list):
            return [tx(v, key) for v in o]
        if isinstance(o, str):
            if key == "inLanguage":
                return lang
            if key in ("@id", "url"):
                if fname != "index.html" and o.startswith(tr_url(fname)):
                    return lang_url(fname, lang) + o[len(tr_url(fname)):]
                if fname == "index.html" and key == "url" and o == SITE:
                    return o
                return o
            if key in SKIP_KEYS or not LETTER.search(o) or o.startswith("http"):
                return o
            if o in tr_plain:
                return tr_plain[o]
            if o in mem:
                return mem[o]
            miss.append(("ld", o))
            return o
        return o
    for a, b, body in reversed(ld_blocks(s)):
        obj = json.loads(body)
        new = "\n" + json.dumps(tx(obj), ensure_ascii=False, indent=2).replace("</", "<\\/") + "\n"
        s = s[:a] + new + s[b:]
    # 5) ek değişiklikler
    for old, new in extra:
        if old not in s:
            miss.append(("extra", old[:80]))
        s = s.replace(old, new)
    # 5b) harf içermeyen metinlerde Türkçe sayı biçimi: EN %47 -> 47%, 3,7 -> 3.7, 871.000 -> 871,000; DE yalnızca %47 -> 47 %
    s = en_numbers(s) if lang == "en" else de_numbers(s)
    # 6) head ve dil
    s = s.replace('<html lang="tr">', f'<html lang="{lang}">', 1).replace('<div lang="tr">', f'<div lang="{lang}">', 1)
    alts = "".join(f'\n<meta property="og:locale:alternate" content="{HTML_LOCALE[l]}">' for l in LANGS if l != lang)
    s = s.replace('<meta property="og:locale" content="tr_TR">',
                  f'<meta property="og:locale" content="{HTML_LOCALE[lang]}">' + alts, 1)
    s = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{lang_url(fname, lang)}">', s, count=1)
    s = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{lang_url(fname, lang)}">', s, count=1)
    # 7) bağlantı ve dosya yolları
    s = re.sub(r'(\s(?:href|src|poster)=")([^"]*)(")', lambda m: m.group(1) + rewrite_url(m.group(2), lang) + m.group(3), s)
    s = re.sub(r'url\((["\']?)([^)"\']+)\1\)', lambda m: "url(" + m.group(1) + rewrite_url(m.group(2), lang) + m.group(1) + ")", s)
    return s, miss


def main(lang, argv):
    src, outroot = argv[0], argv[1]
    M = MAPS[lang]
    pages = argv[2:] or sorted(M)
    mem = load_mem(lang)
    jf, ef = (os.path.join(I18N, x) for x in SIDE[lang])
    jsj = json.load(open(jf, encoding="utf-8")) if os.path.exists(jf) else {}
    exj = json.load(open(ef, encoding="utf-8")) if os.path.exists(ef) else {}
    os.makedirs(os.path.join(outroot, lang), exist_ok=True)
    total = 0
    for f in pages:
        p = os.path.join(src, f)
        if not os.path.exists(p):
            print("yok:", f)
            continue
        s = open(p, encoding="utf-8").read()
        out, miss = make(f, s, mem, jsj.get(f, []), exj.get(f, []), lang)
        open(os.path.join(outroot, lang, M[f]), "w", encoding="utf-8").write(out)
        total += len(miss)
        print(f"{f} -> {lang}/{M[f]}  eksik: {len(miss)}")
        for k, t in miss[:6]:
            print("   ", k, repr(t[:100]))
    print("toplam eksik:", total)


if __name__ == "__main__":
    assert sys.argv[1] in MAPS, "dil: " + " | ".join(MAPS)
    main(sys.argv[1], sys.argv[2:])
