#!/bin/bash
# Kullanım: publish.sh <up-dizini> <yeni-sayfa.html>
set -e
OLD="$(cd "$(dirname "$0")" && pwd)"; R="${REPO:-/home/claude/drihsaneren.github.io}"; export REPO="$R"
cd $OLD
cp $1/_home_section.txt $1/_home_css.txt $1/_home_trio.txt site/
python3 splice_home.py
rm -f site/_home_*.txt $1/_home_*.txt
python3 to_github.py $R/index.html && cp $1/*.html $R/
python3 - "$2" <<'PY'
import sys
import os
page=sys.argv[1]; p=os.environ["REPO"]+"/sitemap.xml"
s=open(p,encoding="utf-8").read()
line=f'  <url><loc>https://drihsaneren.com/{page}</loc><lastmod>2026-09-29</lastmod></url>\n'
if page not in s:
    s=s.replace('  <url><loc>https://drihsaneren.com/stres.html</loc>', line+'  <url><loc>https://drihsaneren.com/stres.html</loc>',1)
open(p,"w",encoding="utf-8").write(s)
PY
python3 make_en.py $R $R | tail -8   # İngilizce sayfalar (eksik çeviri varsa listeler)
python3 sitemap_i18n.py $R $(date +%F)
python3 -c "import xml.dom.minidom;xml.dom.minidom.parse('$R/sitemap.xml')"
cd $R && git status --short && git diff --stat | tail -1
