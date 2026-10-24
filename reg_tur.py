# -*- coding: utf-8 -*-
"""Yeni sayfaları ve haberleri build_pages.py / i18n_map.py'ye kaydeder (22 Ekim 2026 1. tur, 23 Ekim 2026 2. ve 3. tur, 24 Ekim 2026 4. tur).
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


# ------------------------------------------------------------------ sayfalar (24 Ekim 2026, 4. tur; önceki turların listeleri git geçmişinde)
CONDS = [
    # dosya, en, part, kategori, başlık, hap, C_, TH, kısa açıklama, bölge (None = REHAB), (AGR'de/REHAB'da kimden sonra)
    ("kosucu-dizi.html", "iliotibial-band-syndrome.html", "cond70_part.py", "Hastalık rehberi",
     "Koşucu dizi (iliotibial bant sendromu)", "Koşucu dizi", "C_ITB",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M40 136 H280" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><circle cx="118" cy="26" r="10" fill="#8fa476"/><path d="M118 38 L112 78 L132 100 L120 132 M112 78 L92 96 L72 104 M116 48 L134 64 M116 48 L98 60" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M124 64 C130 76 134 88 132 100" fill="none" stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round"/><circle cx="131" cy="99" r="7" fill="none" stroke="#e2ab47" stroke-width="3"/><path d="M196 56 C210 70 210 92 196 106 M214 46 C236 68 236 96 214 116" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" opacity=".7"/><path d="M246 120 L270 96" stroke="rgba(236,229,207,.35)" stroke-width="3" stroke-linecap="round" stroke-dasharray="4 6"/></svg>""",
     "Koşarken dizin dış yanında başlayan ağrı: neden olur, ne işe yarar, kalça güçlendirme egzersizleri ve koşuya güvenli dönüş.",
     "diz", "C_JK"),
    ("uzun-covid.html", "long-covid.html", "cond71_part.py", "Rehabilitasyon rehberi",
     "Uzun COVID'de hareket ve nefes", "Uzun COVID", "C_LCOV",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M50 136 H270" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M70 100 H150 M80 100 V136 M140 100 V136" stroke="#8a6a44" stroke-width="6" stroke-linecap="round" fill="none"/><circle cx="112" cy="40" r="10" fill="#8fa476"/><path d="M112 52 L114 96 M114 96 L94 98 L92 134 M112 62 L98 82 L104 96" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M176 52 C190 46 200 58 214 52 C228 46 236 56 248 52 M176 74 C190 68 200 80 214 74 C228 68 236 78 248 74" fill="none" stroke="#d8b25e" stroke-width="3.5" stroke-linecap="round"/><path d="M184 104 H202 L208 94 L216 114 L222 104 H246" fill="none" stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>""",
     "COVID-19 sonrası aylarca süren yorgunluk ve nefes darlığında güvenli hareket: egzersiz sonrası alevlenme, enerji planlaması ve hafif ev hareketleri.",
     None, "C_HT"),
    ("zayiflama-ilaci-ve-kas.html", "weight-loss-medication-and-muscle.html", "cond72_part.py", "Rehabilitasyon rehberi",
     "Zayıflama ilacı kullanırken kaslarınızı koruyun", "Zayıflama ilacı ve kas", "C_GLP",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M50 136 H270" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><rect x="62" y="56" width="70" height="20" rx="10" fill="none" stroke="#d8b25e" stroke-width="4" transform="rotate(-30 97 66)"/><path d="M84 76 L110 58" stroke="#d8b25e" stroke-width="4"/><circle cx="206" cy="28" r="10" fill="#8fa476"/><path d="M206 40 V82 M206 82 L194 106 L194 134 M206 82 L218 106 L218 134 M206 52 L180 52 M206 52 L232 52" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M168 44 V60 M244 44 V60" stroke="#e2ab47" stroke-width="8" stroke-linecap="round"/></svg>""",
     "Semaglutid ve tirzepatid gibi ilaçlarla kilo verirken kas kaybını sınırlamak: güç egzersizi, protein ve evde altı egzersiz.",
     None, "C_LCOV"),
]
SELFS = [
    # dosya, en, part, başlık, hap, C_, TH, açıklama, SELF'te kimden sonra, SELF_GROUPS grubu, grupta kimden sonra
    ("sakatlanmayi-onleyen-isinma.html", "injury-prevention-warm-up.html", "self15_part.py", "Sakatlanmayı önleyen ısınma", "Sakatlanmayı önleyen ısınma", "C_ISN",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M40 136 H280" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M58 134 L66 112 L74 134 Z M246 134 L254 112 L262 134 Z" fill="#e2ab47"/><circle cx="150" cy="30" r="10" fill="#8fa476"/><path d="M150 42 L144 78 L128 92 L118 116 M144 78 L162 98 L176 108 M148 52 L132 66 M148 52 L168 62" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><circle cx="198" cy="122" r="12" fill="none" stroke="#ece5cf" stroke-width="3"/><path d="M192 116 L204 128 M204 116 L192 128" stroke="#ece5cf" stroke-width="2" opacity=".5"/><path d="M96 70 C88 78 88 90 96 98" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" opacity=".7"/></svg>""",
     "Futbolda sakatlanmaları azalttığı gösterilen FIFA 11+ programından uyarlanmış 20 dakikalık ısınma: zamanlayıcı ve haftalık takip.",
     "C_DB", "Zamanlayıcıyla birlikte yapın", "denge-antrenmani.html"),
    ("adim-hedefi.html", "step-goal-planner.html", "self15_part.py", "Adım hedefi planlayıcısı", "Adım hedefi", "C_AH",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M50 136 H270" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><g fill="#8fa476"><ellipse cx="96" cy="112" rx="10" ry="16" transform="rotate(-14 96 112)"/><ellipse cx="128" cy="82" rx="10" ry="16" transform="rotate(14 128 82)"/><ellipse cx="160" cy="52" rx="10" ry="16" transform="rotate(-14 160 52)"/></g><g fill="#d8b25e"><circle cx="90" cy="92" r="3"/><circle cx="134" cy="62" r="3"/><circle cx="154" cy="32" r="3"/></g><path d="M206 120 V98 M226 120 V84 M246 120 V66 M266 120 V50" stroke="#e2ab47" stroke-width="10" stroke-linecap="round"/></svg>""",
     "Günlük adım ortalamanıza göre haftalık hedef ve plan: 7.000 adım eşiği, yaşa göre hedef aralığı ve haftalık kayıt.",
     "C_MOVE", "Kendinizi ölçün", "hareket.html"),
]
RELATED_NEW = {
    "kosucu-dizi.html": ["diz-onu-agrisi.html", "kalca-yan-agrisi.html", "sakatlanmayi-onleyen-isinma.html"],
    "uzun-covid.html": ["yogun-bakim-sonrasi.html", "ic-cekis.html", "koah.html"],
    "zayiflama-ilaci-ve-kas.html": ["sarkopeni.html", "guc-devresi.html", "diyabette-egzersiz.html"],
    "sakatlanmayi-onleyen-isinma.html": ["on-capraz-bag.html", "arka-uyluk-zorlanmasi.html", "ayak-bilegi-burkulmasi.html"],
    "adim-hedefi.html": ["hareket.html", "tempolu-yuruyus.html", "yemek-sonrasi-yuruyus.html"],
}
RELATED_ADD = [  # (var olan sayfa, eklenecek)
    ("diz-onu-agrisi.html", "kosucu-dizi.html"),
    ("kalca-yan-agrisi.html", "kosucu-dizi.html"),
    ("yogun-bakim-sonrasi.html", "uzun-covid.html"),
    ("sarkopeni.html", "zayiflama-ilaci-ve-kas.html"),
    ("diyabette-egzersiz.html", "zayiflama-ilaci-ve-kas.html"),
    ("on-capraz-bag.html", "sakatlanmayi-onleyen-isinma.html"),
    ("arka-uyluk-zorlanmasi.html", "sakatlanmayi-onleyen-isinma.html"),
    ("hareket.html", "adim-hedefi.html"),
    ("tempolu-yuruyus.html", "adim-hedefi.html"),
]

# exec listesi
# cond61, sn_stair çizimi self4_part.py'de tanımlandığı için self12_part.py'den SONRA exec edilir. Yeni partlar zincirin sonuna eklenir.
for part, after in (("self12_part.py", "self11_part.py"), ("cond61_part.py", "self12_part.py"), ("cond62_part.py", "cond61_part.py"), ("cond63_part.py", "cond62_part.py"),
                    ("self13_part.py", "cond63_part.py"), ("cond64_part.py", "self13_part.py"), ("cond65_part.py", "cond64_part.py"), ("cond66_part.py", "cond65_part.py"),
                    ("cond67_part.py", "cond66_part.py"), ("cond68_part.py", "cond67_part.py"), ("cond69_part.py", "cond68_part.py"), ("self14_part.py", "cond69_part.py"),
                    ("cond70_part.py", "self14_part.py"), ("cond71_part.py", "cond70_part.py"), ("cond72_part.py", "cond71_part.py"), ("self15_part.py", "cond72_part.py")):
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

# ------------------------------------------------------------------ Bilim gündemi (4. tur, 24 Ekim 2026)
s = open(B, encoding="utf-8").read()
IL_NEW = {
"IL_LBPG": '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 160 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<rect x="40" y="26" width="104" height="128" rx="8" fill="none" stroke="rgba(236,229,207,.45)" stroke-width="3"/>
<g fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M56 50 l5 5 l9 -10" stroke="#8fa476" stroke-width="3.5"/><path d="M78 50 H128" stroke="rgba(236,229,207,.35)" stroke-width="3"/>
<path d="M56 78 l5 5 l9 -10" stroke="#8fa476" stroke-width="3.5"/><path d="M78 78 H122" stroke="rgba(236,229,207,.35)" stroke-width="3"/>
<path d="M58 100 l10 10 M68 100 l-10 10" stroke="#e2ab47" stroke-width="3.5"/><path d="M78 106 H118" stroke="rgba(236,229,207,.35)" stroke-width="3"/>
<path d="M58 124 l10 10 M68 124 l-10 10" stroke="#e2ab47" stroke-width="3.5"/><path d="M78 130 H114" stroke="rgba(236,229,207,.35)" stroke-width="3"/></g>
<circle cx="228" cy="40" r="10" fill="#8fa476"/>
<path d="M228 54 C226 74 230 90 226 104 M226 104 L216 132 L214 158 M226 104 L240 130 L244 158 M228 64 L210 84 M228 64 L248 80" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="227" cy="96" r="12" fill="none" stroke="#e2ab47" stroke-width="3"/></svg>''',
"IL_RRAD": '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 160 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<circle cx="82" cy="46" r="10" fill="#8fa476"/>
<path d="M82 60 L78 102 L64 126 L60 156 M78 102 L94 124 L100 154 M80 70 L64 90 M80 70 L100 84" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M160 70 C150 56 154 36 172 32 C178 22 196 20 204 30 C216 24 232 32 232 46 C244 50 246 68 236 76 C238 92 222 100 210 94 C202 104 184 104 178 94 C164 98 152 86 160 70 Z" fill="none" stroke="#d8b25e" stroke-width="4" stroke-linejoin="round"/>
<path d="M176 52 C186 58 196 50 206 58 M184 74 C194 68 204 78 214 70" fill="none" stroke="rgba(236,229,207,.4)" stroke-width="3" stroke-linecap="round"/>
<path d="M190 120 H210 M200 110 V130" stroke="rgba(236,229,207,.35)" stroke-width="4" stroke-linecap="round"/>
<path d="M150 142 H170 L176 132 L184 152 L190 142 H250" fill="none" stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>''',
"IL_SMALL": '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 156 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<circle cx="96" cy="78" r="44" fill="none" stroke="#d8b25e" stroke-width="5"/>
<path d="M96 78 V46 M96 78 L118 90" stroke="#ece5cf" stroke-width="4" stroke-linecap="round"/>
<path d="M96 34 A44 44 0 0 1 118 40" fill="none" stroke="#e2ab47" stroke-width="9" stroke-linecap="round"/>
<circle cx="96" cy="78" r="5" fill="#ece5cf"/>
<circle cx="222" cy="42" r="10" fill="#8fa476"/>
<path d="M222 56 L218 96 L204 118 L200 152 M218 96 L234 116 L240 150 M220 66 L204 86 M220 66 L240 80" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M256 96 H284 M262 110 H284" stroke="rgba(236,229,207,.35)" stroke-width="3" stroke-linecap="round"/></svg>''',
}
NEWS_ADD = [
("IL_HTN", ''' dict(il=IL_LBPG, g="hareket", cat="Bel ağrısı", date="Ekim 2026",
      title="Yeni başlayan bel ağrısında yeni kılavuz: Önce bilgi ve hareket, rutin görüntüleme ve opioid yok",
      text="Amerikan Ağrı Tıbbı Akademisi (AAPM), 6 haftadan kısa süren ve bir yaralanmaya bağlı olmayan bel ağrısı için Ekim 2026'da yeni bir klinik kılavuz yayımladı. Kılavuz, 105 çalışmayı inceleyen ve Pain Medicine dergisinde yayımlanan bir sistematik derlemeye dayanıyor. Ciddi bir hastalığı düşündüren belirtisi olmayanlarda erken görüntülemenin (röntgen, MR) ağrıyı ve işlevi iyileştirmediği görüldü; kılavuz bu kişilerde rutin görüntülemeye karşı güçlü bir öneride bulunuyor. İlk adım olarak hasta eğitimi, hafif etkinliklerle aktif kalma ve kendi kendine bakım öneriliyor; güvenle kullanılabiliyorsa kısa süreli reçetesiz ağrı kesici (NSAİİ) ve sıcak uygulama da seçenekler arasında. Opioidler ilk tedavi olarak rutin kullanılmamalı: Plaseboya göre ağrıyı daha fazla azaltmadılar ama daha çok yan etkiye yol açtılar. Parasetamol plasebodan farklı bulunmadı. Ağrı 1–2 hafta içinde azalmaz ya da artarsa, kas gevşeticiler, fizik tedavi ya da akupunktur gibi en az bir ek tedavi önerilebilir.",
      point="Derlemede fizik tedaviye erken yönlendirme, manipülasyon ve mobilizasyon, kas gevşeticiler ve NSAİİ'lerin yararı orta güvenilirlikteydi; ancak yararlar genel olarak küçüktü ve ilk birkaç haftada ortaya çıkıyordu. Ağrının sürüp sürmeyeceğini en iyi psikososyal etkenler öngördü. Yeni başlayan bel ağrılarının %85'inden fazlasında belirli bir hastalık ya da omurga sorunu bulunmuyor ve çoğu kişi günler ya da haftalar içinde iyileşiyor. Kılavuzu hazırlayan proje ABD Gıda ve İlaç Dairesi (FDA) tarafından finanse edildi.",
      src=[("Amerikan Ağrı Tıbbı Akademisi, 5 Ekim 2026", "https://www.painmed.org/news/acute-low-backpain-guideline-systematic-review-available"), ("Pain Medicine, 2026 (sistematik derleme)", "https://doi.org/10.1093/pm/pnag131"), ("Managed Healthcare Executive, 8 Ekim 2026", "https://www.managedhealthcareexecutive.com/view/new-acute-low-back-pain-guideline-steers-clinicians-away-from-routine-imaging-and-opioids"), ("New York Eyaleti Tabipler Derneği, 9 Ekim 2026", "https://www.mssny.org/pulse-10-9-2026new-acute-low-back-pain-guideline-and-free-resources-for-physicians/")],
      rel=("Bel ağrısı rehberi", "bel-agrisi.html")),
'''),
("IL_BCI", ''' dict(il=IL_RRAD, g="beyin", cat="Demans", date="Mart 2026",
      title="Egzersiz ve sıkı tansiyon-kolesterol tedavisi iki yılda düşünme becerilerini iyileştirmedi",
      text="ABD'de dört merkezde yürütülen ve 23 Mart 2026'da JAMA Neurology'de yayımlanan rrAD çalışmasına, demansı olmayan ama yüksek tansiyonu, ailesinde demans öyküsü ya da kendi fark ettiği hafıza yakınmaları olan 60–85 yaş arası 513 kişi katıldı. Katılımcılar dört gruba ayrıldı: haftada yaklaşık 160 dakika orta-yüksek tempolu aerobik egzersiz, büyük tansiyonu 130'un altına indirmeyi ve LDL kolesterolü düşürmeyi hedefleyen yoğun ilaç tedavisi, ikisi birlikte ya da olağan bakım. İki yıl sonunda düşünme ve hafıza testlerinden oluşan bileşik puan tüm gruplarda hafifçe arttı, ama gruplar arasında anlamlı fark yoktu. İlaç tedavisi tansiyonu ve LDL kolesterolü belirgin düşürdü.",
      point="Araştırmacıların ifadesiyle “bedeni iyileştirdik ama beyni değil”. İki yıl, bilişsel gerilemeyi önlemedeki etkiyi görmek için kısa olabilir; katılımcılar başlangıçta bilişsel olarak sağlıklıydı ve tüm gruplarda puanlar arttığı için fark görmek zorlaştı. Sonuç, egzersizin ve tansiyon kontrolünün değersiz olduğu anlamına gelmiyor: ikisi de kalp-damar sağlığı için önemli. Araştırmacılar demansı önlemek için birden fazla risk etkenini birlikte hedefleyen, daha uzun süreli yaklaşımların gerektiğini vurguluyor.",
      src=[("JAMA Neurology, Mart 2026", "https://jamanetwork.com/journals/jamaneurology/article-abstract/2846826"), ("Pennington Biyomedikal Araştırma Merkezi, 23 Mart 2026", "https://www.pbrc.edu/news/media/2026/jamaneurology.aspx"), ("EMJ", "https://www.emjreviews.com/?p=147867")],
      rel=("Demansta egzersiz", "demans-egzersiz.html")),
'''),
("IL_DEPEX", ''' dict(il=IL_SMALL, g="hareket", cat="Hareket", date="Ocak 2026",
      title="Günde 5 dakika daha fazla hareket: küçük değişikliklerin büyük etkisi",
      text="Norveç, İsveç, ABD ve İngiltere'den 135 binden fazla yetişkinin hareketinin cihazlarla ölçüldüğü kohortları birleştiren ve 14 Ocak 2026'da The Lancet'te yayımlanan analizde, ortalama 8 yıllık izlem verileriyle küçük davranış değişikliklerinin kaç ölümü önleyebileceği hesaplandı. En hareketli %20 dışındaki herkes günde 5 dakika daha orta tempolu hareket etse (örneğin tempolu yürüyüş), ölümlerin yaklaşık %10'u önlenebilirdi; günde 10 dakika ek hareketle bu oran %15'e çıkıyordu. En hareketsiz %20'lik grupta 5 dakikalık artış ölümlerin yaklaşık %6'sını önleyebilirdi. Günde 30 dakika daha az oturmak ise ölümlerin yaklaşık %7'sini (en çok oturanlarda %3'ünü) önleyebilirdi.",
      point="Bunlar gözlem verilerine dayanan model tahminleridir; hareketin ölüm riskini doğrudan azalttığını kanıtlamaz. Hareket yalnızca başlangıçta bir kez ölçüldü, hareket kısıtlılığı gibi ölçülmeyen etkenler sonucu etkilemiş olabilir ve veriler yalnızca yüksek gelirli ülkelerden geliyor. Uzmanlar sonuçların kişisel bir egzersiz reçetesi olarak değil, toplum düzeyinde olası bir etki olarak okunması gerektiğini vurguluyor. Yine de mesaj net: Maraton koşmak gerekmiyor, her gün birkaç dakika daha tempolu yürümek bile fark yaratabilir.",
      src=[("The Lancet, 14 Ocak 2026", "https://doi.org/10.1016/S0140-6736(25)02219-6"), ("EurekAlert! (The Lancet), 13 Ocak 2026", "https://www.eurekalert.org/news-releases/1112291"), ("Karolinska Enstitüsü, 14 Ocak 2026", "https://news.ki.se/five-extra-minutes-of-movement-a-day-can-save-lives-study-in-the-lancet-finds"), ("Science Media Centre İspanya, uzman görüşleri", "https://sciencemediacentre.es/en/small-and-feasible-changes-physical-activity-are-associated-lower-mortality-risk")],
      rel=("Adım hedefi planlayıcısı", "adim-hedefi.html")),
'''),
]
for name, svg in IL_NEW.items():
    if f"{name} = " not in s:
        once("NEWS = [", f"{name} = '''{svg}'''\n", after=False)
for anchor_il, entry in NEWS_ADD:
    il = re.search(r"il=(\w+)", entry).group(1)
    if f"dict(il={il}," in s:
        continue
    anchor = f" dict(il={anchor_il},"
    assert s.count(anchor) == 1, anchor
    s = s.replace(anchor, entry + anchor, 1)
open(B, "w", encoding="utf-8").write(s)
print("haberler tamam")
