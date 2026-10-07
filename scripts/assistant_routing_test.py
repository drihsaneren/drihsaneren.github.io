#!/usr/bin/env python3
import itertools, re, sys

def norm(s):
    return re.sub(r"\s+"," ", re.sub(r"[^a-z0-9çğıöşü\s-]"," ", s.lower())).strip()

def intent(q):
    n=norm(q)
    rules=[
      ("neck", r"(^|\s)(boyn\w*|boyun\w*)(?=\s|$)"),
      ("back", r"(^|\s)bel\w*(?=\s|$)"),
      ("shoulder", r"(^|\s)(omuz\w*|omz\w*)(?=\s|$)"),
      ("knee", r"(^|\s)diz\w*(?=\s|$)"),
      ("hip", r"(^|\s)(kalç\w*|kalc\w*)(?=\s|$)"),
      ("heel", r"(^|\s)(topuk\w*|topuğ\w*|topug\w*|topu\w*)(?=\s|$)"),
      ("head", r"(^|\s)(baş\w*|bas\w*)(?=\s|$)"),
      ("elbow", r"(^|\s)(dirsek\w*|dirseğ\w*|dirseg\w*|dirse\w*)(?=\s|$)"),
      ("jaw", r"(^|\s)(çene\w*|cene\w*)(?=\s|$)")
    ]
    for name,rx in rules:
        if re.search(rx,n): return name
    return ""

forms={
 "neck":["boynum","boyun","boynumda","boynumun","boyun bölgem","boyun tarafım"],
 "back":["belim","bel","belimde","belimin","bel bölgem","bel tarafım"],
 "shoulder":["omzum","omuzum","omuz","omzumda","omzumun","omuz bölgem"],
 "knee":["dizim","diz","dizimde","dizimin","diz bölgem","diz tarafım"],
 "hip":["kalçam","kalca","kalça","kalçamda","kalçamın","kalça bölgem"],
 "heel":["topuğum","topugum","topuk","topuğumda","topuğumun","topuk bölgem"],
 "head":["başım","basim","baş","başımda","başımın","baş bölgem"],
 "elbow":["dirseğim","dirsegim","dirseği","dirsek","dirseğimde","dirseğimin","dirsek bölgem"],
 "jaw":["çenem","cenem","çene","çenemde","çenemin","çene bölgem"]
}
templates=[
 "{x} ağrıyor","{x} çok ağrıyor","{x} birkaç gündür ağrıyor","{x} sızlıyor","{x} tutuldu",
 "{x} ağrım var","{x} hareket edince ağrıyor","{x} gece ağrıyor","{x} için ne yapabilirim",
 "{x} neden ağrır","{x} ağrısına ne iyi gelir","{x} ağrısı var","{x} acıyor","{x} ağrısı geçmiyor",
 "merhaba {x} ağrıyor","hocam {x} ağrıyor","spor sonrası {x} ağrıyor","sabahları {x} ağrıyor",
 "oturunca {x} ağrıyor","yürürken {x} ağrıyor","uzun süredir {x} ağrıyor","bugün {x} ağrıyor"
]
prefixes=["","çok","hafif","ara sıra","son zamanlarda","yaklaşık iki gündür","bir haftadır"]
suffixes=[""," ne olabilir"," ne yapmalıyım"," egzersiz olur mu"," hangi rehbere bakayım"," bilgi verir misin"]

errors=[]; total=0
for expected, xs in forms.items():
    for x,t,p,s in itertools.product(xs,templates,prefixes,suffixes):
        q=(" ".join(y for y in [p,t.format(x=x),s] if y)).strip()
        total+=1
        got=intent(q)
        if got!=expected:
            errors.append((q,expected,got))
            if len(errors)>=50: break
    if len(errors)>=50: break

# Specific-context checks that must not collapse to generic routing.
special=[
 ("gebelikte bel ağrısı","back"),("hamileyim belim ağrıyor","back"),
 ("bel fıtığım var","back"),("boyun fıtığım var boynum ağrıyor","neck"),
 ("dirseğim ağrıyor","elbow"),("dirseği ağrıyor","elbow"),
 ("omzum ağrıyor","shoulder"),("topuğum ağrıyor","heel")
]
for q,e in special:
    total+=1
    g=intent(q)
    if g!=e: errors.append((q,e,g))

print(f"Assistant routing regression: {total} generated questions tested.")
if errors:
    print(f"FAILED: {len(errors)} mismatches")
    for q,e,g in errors[:50]:
        print(f"- {q!r}: expected {e}, got {g or 'none'}")
    sys.exit(1)
print("PASS: all generated questions routed to the expected body region.")
