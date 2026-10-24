import re, sys, html
for f in sys.argv[1:]:
    s = open(f"/home/claude/main/{f}.html", encoding="utf-8").read()
    qs = re.findall(r'<summary[^>]*>(.*?)</summary>', s, re.S)
    i = s.find('class="wrap col sources"'); j = s.find('</ol>', i)
    urls = re.findall(r'href="(https?://[^"]+)"', s[i:j])
    print("==", f)
    for q in qs: print("  Q:", html.unescape(re.sub(r'<[^>]+>', '', q)).strip())
    for u in urls: print("  U:", u)
