# -*- coding: utf-8 -*-
"""sitemap.xml'i TR + EN sayfalar ve hreflang (xhtml:link) alternatifleriyle yeniden yazar.
Kullanım: sitemap_i18n.py <repo> [bugün]"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from i18n_map import EN, tr_url, en_url

repo = sys.argv[1]
today = sys.argv[2] if len(sys.argv) > 2 else "2026-09-29"
p = os.path.join(repo, "sitemap.xml")
old = open(p, encoding="utf-8").read()
order, plain = [], []
for loc in re.findall(r"<loc>https://drihsaneren\.com/([^<]*)</loc>", old):
    f = loc or "index.html"
    if f.startswith("en/"):
        continue
    if f in EN and f not in order:
        order.append(f)
    elif f not in EN and f not in plain:
        plain.append(f)
for f in EN:
    if f not in order and os.path.exists(os.path.join(repo, f)):
        order.append(f)


def entry(loc, f):
    alts = (f'    <xhtml:link rel="alternate" hreflang="tr" href="{tr_url(f)}"/>\n'
            f'    <xhtml:link rel="alternate" hreflang="en" href="{en_url(f)}"/>\n'
            f'    <xhtml:link rel="alternate" hreflang="x-default" href="{tr_url(f)}"/>\n')
    return f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{today}</lastmod>\n{alts}  </url>\n"


out = ['<?xml version="1.0" encoding="UTF-8"?>\n',
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n']
for f in order:
    out.append(entry(tr_url(f), f))
for f in plain:
    out.append(f"  <url>\n    <loc>https://drihsaneren.com/{f}</loc>\n    <lastmod>{today}</lastmod>\n  </url>\n")
for f in order:
    if os.path.exists(os.path.join(repo, "en", EN[f])):
        out.append(entry(en_url(f), f))
out.append("</urlset>\n")
open(p, "w", encoding="utf-8").write("".join(out))
print(len(order), "sayfa çifti")
