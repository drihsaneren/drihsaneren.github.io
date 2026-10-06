# -*- coding: utf-8 -*-
"""TR sayfalardan /en/ altındaki İngilizce sayfaları üretir.
Kullanım: make_en.py <tr-kaynak-dizini> <cikis-kok-dizini> [sayfa.html ...]
  - i18n/todo/*.json : çevrilecek birimler (id, kind, tr)
  - i18n/done/*.json : çeviriler {id: en}
  - i18n/js.json     : sayfa başına [tr, en] betik metni çiftleri
  - i18n/extra.json  : sayfa başına [eski, yeni] ham değişiklikler (çeviriden sonra)
"""
import sys, os, re, json, glob, html as _html
from urllib.parse import quote
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from i18n_core import units, plain, ld_blocks, SKIP_KEYS, LETTER
from i18n_map import EN, SITE, switcher, tr_url, en_url

I18N = os.path.join(HERE, "i18n")
EN_FILES = set(EN.values())


def load_mem():
    mem = {}
    for tf in sorted(glob.glob(os.path.join(I18N, "todo", "*.json"))):
        df = os.path.join(I18N, "done", os.path.basename(tf))
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


def rewrite_url(v):
    if not v or v.startswith(("http:", "https:", "mailto:", "tel:", "#", "data:", "javascript:", "../", "/")):
        return v
    m = re.match(r"([^#?]*)(.*)", v)
    p, rest = m.group(1), m.group(2)
    if not p:
        return v
    if p in EN:
        return EN[p] + rest
    if p in EN_FILES:
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

def make(fname, s, mem, js_pairs, extra):
    miss = []
    # 1) dil seçici
    s, n = re.subn(r'<div class="lang" role="group" aria-label="Dil seçimi">.*?</div>', switcher(fname, "en"), s, flags=re.S)
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
                return "en"
            if key in ("@id", "url"):
                if fname != "index.html" and o.startswith(tr_url(fname)):
                    return en_url(fname) + o[len(tr_url(fname)):]
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
    # 5b) harf içermeyen metinlerde Türkçe sayı biçimi: %47 -> 47%, 3,7 -> 3.7, 871.000 -> 871,000
    s = en_numbers(s)
    # 6) head ve dil
    s = s.replace('<html lang="tr">', '<html lang="en">', 1).replace('<div lang="tr">', '<div lang="en">', 1)
    s = s.replace('<meta property="og:locale" content="tr_TR">',
                  '<meta property="og:locale" content="en_GB">\n<meta property="og:locale:alternate" content="tr_TR">', 1)
    s = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{en_url(fname)}">', s, 1)
    s = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{en_url(fname)}">', s, 1)
    # 7) bağlantı ve dosya yolları
    s = re.sub(r'(\s(?:href|src|poster)=")([^"]*)(")', lambda m: m.group(1) + rewrite_url(m.group(2)) + m.group(3), s)
    s = re.sub(r'url\((["\']?)([^)"\']+)\1\)', lambda m: "url(" + m.group(1) + rewrite_url(m.group(2)) + m.group(1) + ")", s)
    return s, miss


def main():
    src, outroot = sys.argv[1], sys.argv[2]
    pages = sys.argv[3:] or sorted(EN)
    mem = load_mem()
    jsj = json.load(open(os.path.join(I18N, "js.json"), encoding="utf-8")) if os.path.exists(os.path.join(I18N, "js.json")) else {}
    exj = json.load(open(os.path.join(I18N, "extra.json"), encoding="utf-8")) if os.path.exists(os.path.join(I18N, "extra.json")) else {}
    os.makedirs(os.path.join(outroot, "en"), exist_ok=True)
    total = 0
    for f in pages:
        p = os.path.join(src, f)
        if not os.path.exists(p):
            print("yok:", f)
            continue
        s = open(p, encoding="utf-8").read()
        out, miss = make(f, s, mem, jsj.get(f, []), exj.get(f, []))
        open(os.path.join(outroot, "en", EN[f]), "w", encoding="utf-8").write(out)
        total += len(miss)
        print(f"{f} -> en/{EN[f]}  eksik: {len(miss)}")
        for k, t in miss[:6]:
            print("   ", k, repr(t[:100]))
    print("toplam eksik:", total)


if __name__ == "__main__":
    main()
