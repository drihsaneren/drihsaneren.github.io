#!/bin/bash
# Yeniden derle + yayımla (sessiz). Kullanım: bash denetim/rb.sh <sayfa.html>
K="$(cd "$(dirname "$0")/.." && pwd)"; cd "$K"; export REPO=${REPO:-/home/claude/main}
python3 build_pages.py github up40 >/dev/null && bash rebuild_home.sh >/dev/null 2>&1 && bash publish.sh up40 ${1:-bilgi.html} 2>&1 | grep -i "eksik\|error\|Traceback"; python3 fb_recete.py >/dev/null; echo rb-ok
