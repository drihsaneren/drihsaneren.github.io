# -*- coding: utf-8 -*-
"""(8 Kasım 2026: yalnız dis-sikma.html) Yeni sayfaları ve haberleri build_pages.py / i18n_map.py'ye kaydeder (22 Ekim 2026 1. tur, 23 Ekim 2026 2. ve 3. tur, 24 Ekim 2026 4. tur).
Kullanım: python3 reg_tur.py   (çalışma dizininde; tekrar çalıştırılırsa zaten eklenenleri atlar)
Sonraki turlarda: CONDS / SELFS / NEWS_ADD listelerini yeni sayfalara göre değiştirip yeniden kullanın.
Her eklemede "çapa" (anchor) metninin build_pages.py'de tam bir kez geçtiği denetlenir."""
import re, sys

B = "build_pages.py"
s = open(B, encoding="utf-8").read()


def once(anchor, new, after=True, where=None):
    """anchor metninin tek geçtiği yere new'i ekler (önceden eklendiyse atlar)."""
    global s
    if new.strip() and new.strip() in s:
        return
    hay = s if where is None else where
    n = hay.count(anchor)
    assert n == 1, f"çapa {n} kez geçiyor: {anchor[:70]!r}"
    i = s.index(anchor)
    s = s[:i + len(anchor)] + new + s[i + len(anchor):] if after else s[:i] + new + s[i:]


def add_to_set(name, item):
    """KOSE_PAGES / SELF_PAGES gibi tek satırlık kümelerin başına ekler."""
    global s
    m = re.search(rf'^{name} = \{{', s, re.M)
    line_end = s.index("\n", m.start())
    if f'"{item}"' in s[m.start():line_end]:
        return
    s = s[:m.end()] + f'"{item}", ' + s[m.end():]


def add_to_list_after(list_name, after_item, new_item):
    """Tek satırlık listede (REHAB, SELF) after_item'dan sonra new_item ekler."""
    global s
    m = re.search(rf'^{list_name} = \[', s, re.M)
    line_end = s.index("\n", m.start())
    line = s[m.start():line_end]
    if re.search(rf'\b{new_item}\b', line):
        return
    assert line.count(after_item + ",") + line.count(after_item + "]") == 1, (list_name, after_item)
    line2 = re.sub(rf'\b{after_item}\b', f'{after_item}, {new_item}', line, count=1)
    s = s[:m.start()] + line2 + s[line_end:]


# ------------------------------------------------------------------ sayfalar (8 Kasım 2026: diş sıkma / bruksizm)
CONDS = [
    ("dis-sikma.html", "teeth-grinding-bruxism.html", "cond73_part.py", "Hastalık rehberi",
     "Diş sıkma ve gıcırdatma (bruksizm)", "Diş sıkma", "C_BRX",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M136 94 Q112 68 126 42 Q142 18 172 22 Q198 28 200 54 L208 68 L199 71 L199 80" stroke="#8fa476" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M152 82 L158 104 Q164 112 188 106 L199 92" stroke="#d8b25e" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M142 110 L140 146 M168 114 L172 146" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/><path d="M182 84 l4 -6 l4 6 l4 -6 l4 6" stroke="#e2ab47" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M222 50 l10 -8 M224 66 h14 M222 82 l10 8" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/><path d="M150 46 Q160 36 176 40" stroke="#d8b25e" stroke-width="2.5" fill="none" stroke-dasharray="4 5" stroke-linecap="round"/></svg>""",
     "Diş sıkma ve gıcırdatma diş, çene eklemi, boyun ve uykuyu nasıl etkiler? Plağın yeri, çok yönlü tedavi ve evde egzersizler.",
     "boyun", "C_TMJ"),
]
SELFS = []
RELATED_NEW = {
    "dis-sikma.html": ["cene-eklemi.html", "bas-agrisi.html", "fibromiyalji.html"],
}
RELATED_ADD = [
    ("cene-eklemi.html", "dis-sikma.html"),
    ("bas-agrisi.html", "dis-sikma.html"),
]

# exec listesi
# cond61, sn_stair çizimi self4_part.py'de tanımlandığı için self12_part.py'den SONRA exec edilir. Yeni partlar zincirin sonuna eklenir.
for part, after in (("cond73_part.py", "self15_part.py"),):
    if f'"{part}"' not in s:
        once(f'"{after}", ', f'"{part}", ')

for f, en, part, cat, title, pill, C, th, txt, reg, after in CONDS:
    add_to_set("KOSE_PAGES", f)
    once('TOPICS = {\n', f'    "{f}": ("{cat}", "{title}"),\n')
    TH = "TH_" + C[2:]
    once("C_TOR = KC(", "", after=False)  # çapa varlık denetimi
    if f"{TH} = " not in s:
        i = s.index("\n", s.index("C_TOR = KC(")) + 1
        s = s[:i] + f'{TH} = """{th}"""\n{C} = KC("{f}", {TH}, "{cat}", "{title}", "{txt}")\n' + s[i:]
    if reg:
        if f"({C}, " not in s:
            ms = list(re.finditer(rf'\({after}, "([a-z ]+)"\)', s))
            assert len(ms) == 1, (after, len(ms))
            m = ms[0]
            s = s[:m.end()] + f', ({C}, "{reg}")' + s[m.end():]
    else:
        add_to_list_after("REHAB", after, C)

for f, en, part, title, pill, C, th, txt, after, grp, gafter in SELFS:
    add_to_set("SELF_PAGES", f)
    once('TOPICS = {\n', f'    "{f}": ("Kendine iyi bak", "{title}"),\n')
    TH = "TH_" + C[2:]
    if f"{TH} = " not in s:
        i = s.index("\n", s.index("C_SIT = KC(")) + 1
        s = s[:i] + f'{TH} = """{th}"""\n{C} = KC("{f}", {TH}, "Kendine iyi bak", "{title}", "{txt}")\n' + s[i:]
    add_to_list_after("SELF", after, C)
    m = re.search(rf'\("{grp}", \[[^\]]*\]', s)
    if f'"{f}"' not in m.group(0):
        blk = m.group(0).replace(f'"{gafter}"', f'"{gafter}", "{f}"', 1)
        assert blk != m.group(0), (grp, gafter)
        s = s[:m.start()] + blk + s[m.end():]

# PILL
for row in CONDS + [(x[0], x[1], x[2], None, x[3], x[4]) + x[5:] for x in SELFS]:
    f, pill = row[0], row[5]
    if f'"{f}": "{pill}"' not in s:
        once("PILL = {\n", f'    "{f}": "{pill}",\n')

# RELATED
for f, lst in RELATED_NEW.items():
    if f'    "{f}": [' not in s:
        once("RELATED = {\n", f'    "{f}": [' + ", ".join(f'"{x}"' for x in lst) + "],\n")
for f, x in RELATED_ADD:
    m = re.search(rf'^    "{re.escape(f)}": \[([^\]]*)\]', s, re.M)
    if m and f'"{x}"' not in m.group(1):
        s = s[:m.end() - 1] + f', "{x}"' + s[m.end() - 1:]
    elif not m:
        once("RELATED = {\n", f'    "{f}": ["{x}"],\n')

open(B, "w", encoding="utf-8").write(s)

# i18n_map
M = "i18n_map.py"
t = open(M, encoding="utf-8").read()
for row in CONDS + SELFS:
    f, en = row[0], row[1]
    if f'"{f}":' not in t:
        a = '    "bebeklerde-tortikolis.html": "torticollis-in-babies.html",\n'
        assert t.count(a) == 1
        t = t.replace(a, a + f'    "{f}": "{en}",\n', 1)
open(M, "w", encoding="utf-8").write(t)
print("tamam")

