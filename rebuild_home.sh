set -e
S="$(cd "$(dirname "$0")" && pwd)"; cd "$S"
cp site/index.bak_fb.html site/index.html
python3 fb_hero.py && python3 fb_misc.py && python3 fb_report.py && python3 fb_book.py && python3 fb_day.py && python3 fb_lx.py && python3 fb_trim.py && python3 fb_qr.py && python3 fb_reg.py && python3 fb_face.py
