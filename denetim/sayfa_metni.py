"""Sayfayı denetim için düz metne çevirir. Kullanım: python3 denetim/sayfa_metni.py skolyoz.html [çıktı.txt]
SVG -> [ÇİZİM], bağlantılar 'metin [URL]', bölümler '===== BÖLÜM #id ====='."""
import re, html, sys, os
REPO = os.environ.get("REPO", "/home/claude/main")
name = sys.argv[1]; out = sys.argv[2] if len(sys.argv) > 2 else name.replace(".html", ".txt")
s = open(os.path.join(REPO, name), encoding="utf-8").read()
body = s[s.index("<main>"):s.index("</main>")]
body = re.sub(r"<svg.*?</svg>", "[ÇİZİM]", body, flags=re.S); body = re.sub(r"<script.*?</script>", "", body, flags=re.S)
body = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', lambda m: f"{m.group(2)} [{m.group(1)}]", body, flags=re.S)
body = re.sub(r'<section id="([^"]+)"', r'\n\n===== BÖLÜM #\1 =====\n<section', body)
body = re.sub(r"<(h2|h3)[^>]*>", r"\n## ", body); body = re.sub(r"<li[^>]*>", "\n- ", body)
body = re.sub(r"<(p|div|summary|figcaption|b)[^>]*>", "\n", body); body = re.sub(r"<[^>]+>", " ", body)
body = html.unescape(body); body = re.sub(r"[ \t]+", " ", body); body = re.sub(r"\n\s*\n+", "\n", body)
h0 = s.index('<header class="page">'); head = s[h0:s.index("</header>", h0)]
head = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", head)))
meta = re.search(r'<meta name="description" content="([^"]*)"', s).group(1)
open(out, "w", encoding="utf-8").write(f"SAYFA: {name} (https://drihsaneren.com/{name})\nAÇIKLAMA (meta): {html.unescape(meta)}\nBAŞLIK/GİRİŞ: {head.strip()}\n{body}")
print(out, len(body), "karakter")
