import re, sys
from i18n_map import hreflang, LANG_CSS, switcher
from search_ui import SEARCH_BTN, SEARCH_CSS, SEARCH_TAG
src = open("site/index.html", encoding="utf-8").read()
i = src.index('<div lang="tr">')
head, body = src[:i].strip(), src[i:].strip()
head = re.sub(r'<link rel="preconnect"[^>]*>\n?', '', head)
head = re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com[^>]*>\n?', '', head)
# Site Core v2: yazı tipleri /assets/site-core.css içinde (sayfa içinde @font-face yok)
assert "<style>\n  :root{" in head
old_icon = '<link rel="icon" type="image/png" href="img/logo.png">'
assert head.count(old_icon) == 1
head = head.replace(old_icon, '<link rel="icon" type="image/png" href="logo.png">\n<link rel="stylesheet" href="/assets/site-core.css">')
body = body.replace('src="img/', 'src="').replace('href="img/', 'href="').replace("'img/p'", "'p'").replace("'img/rapor-", "'rapor-")
assert "img/" not in body
nav_end = '    </nav>\n    <a class="cta"'
assert body.count(nav_end) == 1
body = body.replace(nav_end, '    </nav>\n    ' + SEARCH_BTN + '\n    ' + switcher("index.html") + '\n    <a class="cta"', 1)
head = head.replace("\n</style>", LANG_CSS + SEARCH_CSS + "</style>", 1); assert LANG_CSS in head
old = 'href="https://claude.ai/artifact/EwXHr8e7gUFxdpY8Xev6A7" target="_blank" rel="noopener"'
assert body.count(old) == 1; body = body.replace(old, 'href="recete.html"')
meta = '''<meta property="og:type" content="website">
<meta property="og:title" content="İhsan Eren · Evde fizyoterapi">
<meta property="og:description" content="İstanbul'da evde fizyoterapi: kapsamlı değerlendirme, kişiye özel tedavi ve egzersiz programı.">
<meta property="og:image" content="https://drihsaneren.com/logo.png">
<meta property="og:locale" content="tr_TR">
<meta name="theme-color" content="#1c2819">
<meta property="og:url" content="https://drihsaneren.com/">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="İhsan Eren · Evde fizyoterapi">
<meta name="twitter:description" content="İstanbul'da evde fizyoterapi: kapsamlı değerlendirme, kişiye özel tedavi ve egzersiz programı.">
<meta name="twitter:image" content="https://drihsaneren.com/logo.png">
<link rel="canonical" href="https://drihsaneren.com/">'''
meta += '\n' + hreflang('index.html').rstrip()
meta += '\n<script type="application/ld+json">\n' + open("schema_home.json", encoding="utf-8").read() + '\n</script>'
html = f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="color-scheme" content="dark">
{head}
{meta}
</head>
<body>
{body}
{SEARCH_TAG}<script src="/assets/site-core.js" defer></script>
</body>
</html>
'''
open(sys.argv[1], "w", encoding="utf-8").write(html)
