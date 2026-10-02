import re, json, html, sys, glob, os
NEW = sys.argv[1]; REPO = "/home/claude/drihsaneren.github.io"
def vis(s):
    b = s[s.find('<body'):]
    b = re.sub(r'<(script|style|svg)[\s\S]*?</\1>', ' ', b)
    b = re.sub(r'<[^>]+>', ' ', b)
    return re.sub(r'\s+', ' ', html.unescape(b)).strip()
def vis_tight(s):  # etiketleri boşluksuz sil (satır içi <strong> için)
    b = s[s.find('<body'):]
    b = re.sub(r'<(script|style|svg)[\s\S]*?</\1>', ' ', b)
    b = re.sub(r'</?(strong|b|em|i|a)[^>]*>', '', b)
    b = re.sub(r'<[^>]+>', ' ', b)
    return re.sub(r'\s+', ' ', html.unescape(b)).strip()
ok = True
for f in sorted(glob.glob(NEW + "/*.html")):
    n = os.path.basename(f); s = open(f, encoding="utf-8").read()
    head = s[:s.index("</head>")]
    blocks = re.findall(r'<script type="application/ld\+json">([\s\S]*?)</script>', s)
    last_close = head.rstrip().endswith("</script>")
    types = []
    for bl in blocks:
        d = json.loads(bl); types.append(d.get("@type", "graph"))
        if d.get("@type") == "MedicalWebPage":
            assert d["author"]["@id"] == "https://drihsaneren.com/#ihsan-eren", n
        if d.get("@type") == "FAQPage":
            V = vis_tight(s)
            for q in d["mainEntity"]:
                qn, at = q["name"], q["acceptedAnswer"]["text"]
                if qn not in V or at not in V:
                    ok = False; print("  MISMATCH", n, qn, qn in V, at in V)
            print(f"  {n}: {len(d['mainEntity'])} soru -> " + " | ".join(q['name'] for q in d['mainEntity']))
    print(n, types, "script </head> öncesinde" if blocks and last_close else ("şema yok" if not blocks else "YER HATALI"))
    op = os.path.join(REPO, n)
    old = open(op, encoding="utf-8").read() if os.path.exists(op) else s
    if vis(old) != vis(s):
        a, b = vis(old), vis(s)
        i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), min(len(a), len(b)))
        print("  görünür metin değişti @", i, "| eski:", a[i:i+60], "| yeni:", b[i:i+60])
    bad = re.findall(r"(?i)biruni|alumniOf|affiliation|recognizedBy", s)
    if bad: ok = False; print("  OKUL İZİ:", set(bad))
print("OK" if ok else "SORUN VAR")
