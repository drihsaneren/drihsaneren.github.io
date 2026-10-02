# -*- coding: utf-8 -*-
"""HTML'den çevrilecek birimleri (metin blokları, öznitelikler, WhatsApp mesajları,
JSON-LD metinleri) konumlarıyla birlikte çıkarır. Yapıya dokunmadan, yalnızca bu
aralıkları değiştirerek çeviri uygulanır."""
import re, json, html as _html
from html.parser import HTMLParser
from urllib.parse import unquote

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
PHRASING = {"a", "abbr", "b", "bdi", "bdo", "br", "cite", "code", "data", "dfn", "em", "i", "kbd", "mark", "q", "s",
            "samp", "small", "span", "strong", "sub", "sup", "time", "u", "var", "wbr", "img", "svg"}
OPAQUE = {"script", "style", "template"}
SVG_TEXT = {"text", "title", "desc"}
TR_ATTRS = {"alt", "aria-label", "title", "placeholder"}
META_TR = {"description", "og:title", "og:description", "twitter:title", "twitter:description"}
LETTER = re.compile(r"[A-Za-zÇĞİÖŞÜçğıöşüÂâÎîÛû]")
ATTR_RE = re.compile(r'''\s([^\s=/>"']+)(?:\s*=\s*("([^"]*)"|'([^']*)'|([^\s>"']+)))?''')


class Node:
    __slots__ = ("tag", "attrs", "s", "se", "es", "e", "kids", "parent", "aspans", "in_svg", "po")

    def __init__(self, tag, attrs, s, se, parent, in_svg):
        self.tag, self.attrs, self.s, self.se = tag, attrs, s, se
        self.es = self.e = None
        self.kids, self.parent, self.aspans, self.in_svg = [], parent, {}, in_svg
        self.po = None


class _P(HTMLParser):
    def __init__(self, src):
        super().__init__(convert_charrefs=False)
        self.src = src
        self.ls = [0] + [m.end() for m in re.finditer("\n", src)]
        self.root = Node("#root", {}, 0, 0, None, False)
        self.stack = [self.root]

    def off(self):
        l, c = self.getpos()
        return self.ls[l - 1] + c

    def _mk(self, tag, attrs):
        s = self.off()
        txt = self.get_starttag_text()
        par = self.stack[-1]
        n = Node(tag, dict(attrs), s, s + len(txt), par, par.in_svg or tag == "svg")
        for m in ATTR_RE.finditer(txt):
            if m.group(2) is None:
                continue
            g = 3 if m.group(3) is not None else 4 if m.group(4) is not None else 5
            n.aspans[m.group(1).lower()] = (s + m.start(g), s + m.end(g))
        par.kids.append(n)
        return n

    def handle_starttag(self, tag, attrs):
        n = self._mk(tag, attrs)
        if tag in VOID:
            n.es = n.e = n.se
        else:
            self.stack.append(n)

    def handle_startendtag(self, tag, attrs):
        n = self._mk(tag, attrs)
        n.es = n.e = n.se

    def handle_endtag(self, tag):
        s = self.off()
        e = self.src.index(">", s) + 1
        if not any(x.tag == tag for x in self.stack[1:]):
            return
        while True:
            n = self.stack.pop()
            if n.tag == tag:
                n.es, n.e = s, e
                return
            n.es = n.e = s  # örtük kapanış


def parse(src):
    p = _P(src)
    p.feed(src)
    p.close()
    for n in p.stack[1:]:
        n.es = n.e = len(src)
    return p.root


def plain(s):
    return re.sub(r"\s+", " ", _html.unescape(re.sub(r"<[^>]+>", "", s))).strip()


def _phr_only(n):
    if n.po is None:
        n.po = n.tag == "svg" or all(c.tag in PHRASING and _phr_only(c) for c in n.kids)
    return n.po


class Unit:
    __slots__ = ("kind", "a", "b", "raw", "ph")

    def __init__(self, kind, a, b, raw, ph=None):
        self.kind, self.a, self.b, self.raw, self.ph = kind, a, b, raw, ph or []

    @property
    def key(self):
        """Çeviri belleğinde anahtar: svg'ler yer tutucuya dönüşmüş, boşlukları sadeleşmiş metin."""
        t = self.raw
        for i, (x, y, sv) in enumerate(self.ph):
            t = t.replace(sv, f"[[{i + 1}]]", 1)
        return re.sub(r"\s+", " ", t).strip() if self.kind == "text" else t


def _trim(src, a, b):
    while a < b and src[a].isspace():
        a += 1
    while b > a and src[b - 1].isspace():
        b -= 1
    return a, b


def _skip(n):
    return n.tag == "div" and "lang" in (n.attrs.get("class") or "").split()


def _run_unit(src, items, out):
    els = [it[3] for it in items if it[0] == "el"]
    if els and all(not src[it[1]:it[2]].strip() for it in items if it[0] == "text"):
        # yalnızca öğelerden oluşan dizi: her öğeyi ayrı birim yap
        if len(els) > 1 or els[0].tag != "svg":
            for el in els:
                if el.tag != "svg" and not _skip(el):
                    sub = _items(el)
                    if sub:
                        _run_unit(src, sub, out)
            return
    a, b = items[0][1], items[-1][2]
    a, b = _trim(src, a, b)
    if a >= b:
        return
    raw = src[a:b]
    # svg'leri çıkarıp harf var mı bak
    svgs = []
    def col(n):
        if n.tag == "svg":
            svgs.append((n.s, n.e, src[n.s:n.e]))
        else:
            for c in n.kids:
                col(c)
    for it in items:
        if it[0] == "el":
            col(it[3])
    probe = raw
    for _, _, sv in svgs:
        probe = probe.replace(sv, " ")
    if not LETTER.search(plain(probe)):
        return
    # yalnızca baştaki/sondaki svg'yi birim dışında bırak
    while svgs and svgs[0][0] == a:
        a = _trim(src, svgs[0][1], b)[0]
        svgs.pop(0)
    while svgs and svgs[-1][1] == b:
        b = _trim(src, a, svgs[-1][0])[1]
        svgs.pop()
    out.append(Unit("text", a, b, src[a:b], svgs))


def _walk(src, n, out):
    if n.tag in OPAQUE or _skip(n):
        return
    if n.tag == "svg" or n.in_svg:
        for c in n.kids:
            if c.tag in SVG_TEXT and LETTER.search(plain(src[c.se:c.es])):
                a, b = _trim(src, c.se, c.es)
                out.append(Unit("text", a, b, src[a:b]))
            elif c.tag not in SVG_TEXT:
                _walk(src, c, out)
        return
    if n.tag != "#root" and n.tag not in PHRASING and _phr_only(n):
        it = _items(n)
        if it:
            _run_unit(src, it, out)
        return
    run = []
    for it in _items(n):
        if it[0] == "text" or (it[3].tag in PHRASING and _phr_only(it[3])):
            run.append(it)
        else:
            if run:
                _run_unit(src, run, out)
            run = []
            _walk(src, it[3], out)
    if run:
        _run_unit(src, run, out)


def _items(n):
    items, pos = [], n.se
    for k in n.kids:
        if k.s > pos:
            items.append(("text", pos, k.s))
        items.append(("el", k.s, k.e, k))
        pos = k.e
    if n.es is not None and n.es > pos:
        items.append(("text", pos, n.es))
    return items


def _all(n):
    for k in n.kids:
        yield k
        yield from _all(k)


def units(src):
    root = parse(src)
    out = []
    _walk(src, root, out)
    spans = [(u.a, u.b) for u in out]

    def inside(p):
        return any(a <= p < b for a, b in spans)

    for n in _all(root):
        if n.in_svg and n.tag in SVG_TEXT and not inside(n.s) and LETTER.search(plain(src[n.se:n.es])):
            a, b = _trim(src, n.se, n.es)
            out.append(Unit("text", a, b, src[a:b]))
            spans.append((n.s, n.e))
    for n in _all(root):
        if inside(n.s) or _skip(n) or (n.parent and _skip(n.parent)):
            continue
        for at in TR_ATTRS:
            if at in n.aspans and LETTER.search(n.attrs.get(at) or ""):
                a, b = n.aspans[at]
                out.append(Unit("attr", a, b, src[a:b]))
        if n.tag == "meta" and "content" in n.aspans:
            nm = n.attrs.get("name") or n.attrs.get("property") or ""
            if nm in META_TR:
                a, b = n.aspans["content"]
                out.append(Unit("attr", a, b, src[a:b]))
        if "href" in n.aspans and "wa.me/" in (n.attrs.get("href") or "") and "?text=" in n.attrs["href"]:
            a, b = n.aspans["href"]
            v = src[a:b]
            i = v.index("?text=") + 6
            out.append(Unit("wa", a + i, b, unquote(_html.unescape(v[i:]))))
    out.sort(key=lambda u: u.a)
    for x, y in zip(out, out[1:]):
        assert x.b <= y.a, ("örtüşme", x.raw[:60], y.raw[:60])
    return out


SKIP_KEYS = {"@context", "@type", "@id", "url", "image", "logo", "telephone", "email", "sameAs", "inLanguage",
             "dateModified", "datePublished", "lastReviewed", "priceRange", "latitude", "longitude", "addressCountry",
             "postalCode", "hasMap", "embedUrl", "contentUrl", "thumbnailUrl", "uploadDate", "duration", "opens",
             "closes", "dayOfWeek", "currenciesAccepted", "paymentAccepted", "isAccessibleForFree"}


def ld_blocks(src):
    return [(m.start(1), m.end(1), m.group(1)) for m in
            re.finditer(r'<script type="application/ld\+json">(.*?)</script>', src, re.S)]


def ld_strings(obj, key=None):
    """JSON-LD içindeki çevrilebilir metin değerleri."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in SKIP_KEYS:
                continue
            yield from ld_strings(v, k)
    elif isinstance(obj, list):
        for v in obj:
            yield from ld_strings(v, key)
    elif isinstance(obj, str):
        if LETTER.search(obj) and not obj.startswith("http"):
            yield obj
