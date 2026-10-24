# -*- coding: utf-8 -*-
"""Kaynak turu yardımcıları. Çalışma dizini: /home/claude/drihsaneren.github.io"""
import re, os
os.chdir("/home/claude/drihsaneren.github.io")
_cache = {}
def _r(f):
    if f not in _cache: _cache[f] = open(f, encoding="utf-8").read()
    return _cache[f]
def _w(f, s): _cache[f] = s
def save():
    for f, s in _cache.items(): open(f, "w", encoding="utf-8").write(s)
    print("kaydedildi:", ", ".join(sorted(_cache)))
def faq_tail(f, q, text):
    """("q", "...") cevabının sonuna ' text' ekler."""
    s = _r(f); key = f'("{q}", "'
    assert s.count(key) == 1, (f, q, s.count(key))
    i = s.index(key) + len(key); j = s.index('")', i)
    if text in s[i:j]: return
    s = s[:j] + " " + text + s[j:]; _w(f, s)
def after(f, anchor, text, sep=" "):
    """anchor (tek geçen) metninden hemen sonra sep+text ekler."""
    s = _r(f); assert s.count(anchor) == 1, (f, anchor[:60], s.count(anchor))
    if text in s: return
    i = s.index(anchor) + len(anchor); s = s[:i] + sep + text + s[i:]; _w(f, s)
def replace(f, a, b):
    s = _r(f); assert s.count(a) == 1, (f, a[:60], s.count(a)); s = s.replace(a, b); _w(f, s)
def src_after(f, anchor, line):
    """anchor'ı içeren kaynak satırından sonra aynı girintiyle yeni satır ekler (line: Python ifadesi, sonunda virgül yok)."""
    s = _r(f); assert s.count(anchor) == 1, (f, anchor[:60], s.count(anchor))
    if line.strip() in s: return
    i = s.index(anchor); ls = s.rfind("\n", 0, i) + 1; le = s.index("\n", i)
    cur = s[ls:le]; ind = cur[:len(cur) - len(cur.lstrip())]
    if not cur.rstrip().endswith(","): cur2 = cur.rstrip() + ","
    else: cur2 = cur
    s = s[:ls] + cur2 + "\n" + ind + line + "," + s[le:]; _w(f, s)

def bump(f, page_html, date="24 Ekim 2026"):
    """Sayfanın yayımlanmış HTML'indeki h1 başlığını part dosyasında bulup ardından gelen 'Son güncelleme' tarihini günceller."""
    import html as _h
    built = open(f"/home/claude/main/{page_html}", encoding="utf-8").read()
    h1 = re.search(r"<h1>(.*?)</h1>", built, re.S).group(1)
    s = _r(f); key = f"<h1>{h1}</h1>"
    n = s.count(key)
    if n != 1:
        key = f"<h1>{_h.unescape(h1)}</h1>"; n = s.count(key)
    assert n == 1, (f, page_html, h1, n)
    i = s.index(key); j = s.find("Son güncelleme:", i); e = s.find("</p>", j)
    assert 0 < j - i < 4000, (f, page_html, j - i)
    s = s[:j] + "Son güncelleme: " + date + s[e:]; _w(f, s)
