# -*- coding: utf-8 -*-
"""Yeni sayfaları ve haberleri build_pages.py / i18n_map.py'ye kaydeder (22 Ekim 2026 1. tur, 23 Ekim 2026 2. ve 3. tur).
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


# ------------------------------------------------------------------ sayfalar (23 Ekim 2026, 3. tur; önceki turların listeleri git geçmişinde: fcf2047, 2. tur kaynak dalındaki önceki commit)
CONDS = [
    # dosya, en, part, kategori, başlık, hap, C_, TH, kısa açıklama, bölge (None = REHAB), (AGR'de/REHAB'da kimden sonra)
    ("diyabette-egzersiz.html", "exercise-and-diabetes.html", "cond67_part.py", "Rehabilitasyon rehberi",
     "Tip 2 diyabette egzersiz", "Diyabet", "C_DIA",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 136 H260" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><circle cx="112" cy="30" r="11" fill="#8fa476"/><path d="M112 44 L108 84 L94 106 L90 132 M108 84 L124 104 L130 130 M110 54 L94 74 M110 54 L130 66" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M212 28 C200 46 184 64 184 84 C184 100 197 112 212 112 C227 112 240 100 240 84 C240 64 224 46 212 28 Z" fill="none" stroke="#d8b25e" stroke-width="5" stroke-linejoin="round"/><path d="M212 60 V94 M201 83 L212 94 L223 83" fill="none" stroke="#e2ab47" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M146 62 H170" stroke="rgba(236,229,207,.4)" stroke-width="3" stroke-linecap="round" stroke-dasharray="4 5"/></svg>""",
     "Kan şekeri kontrolü için yürüyüş ve güç çalışması: ne kadar, ne zaman, düşük şekerden ve ayak sorunlarından korunma, altı ev egzersizi.",
     None, "C_HF"),
    ("yogun-bakim-sonrasi.html", "recovery-after-intensive-care.html", "cond68_part.py", "Rehabilitasyon rehberi",
     "Yoğun bakımdan sonra iyileşme", "Yoğun bakım sonrası", "C_ICU",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M40 136 H280" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M60 98 H196 M60 98 V136 M196 98 V136 M60 78 V98" fill="none" stroke="#8a6a44" stroke-width="6" stroke-linecap="round"/><rect x="66" y="84" width="42" height="11" rx="5" fill="rgba(236,229,207,.35)"/><circle cx="168" cy="36" r="10" fill="#8fa476"/><path d="M168 48 L170 90 M170 90 L200 92 L202 134 M168 58 L184 80 L188 94" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><rect x="220" y="22" width="68" height="46" rx="7" fill="none" stroke="rgba(236,229,207,.45)" stroke-width="3"/><path d="M226 46 H240 L247 34 L255 58 L262 46 H282" fill="none" stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>""",
     "Yoğun bakımdan sonra güçsüzlük, yorgunluk ve unutkanlık sık görülür: ilk haftalarda neler beklenir, nasıl güçlenilir, hangi destekler var.",
     None, "C_DIA"),
    ("yuksek-tansiyon.html", "high-blood-pressure.html", "cond69_part.py", "Rehabilitasyon rehberi",
     "Yüksek tansiyonda egzersiz", "Yüksek tansiyon", "C_HT",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M50 136 H270" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M66 20 V136" stroke="rgba(236,229,207,.45)" stroke-width="5" stroke-linecap="round"/><circle cx="84" cy="38" r="10" fill="#8fa476"/><path d="M80 50 V92 L118 92 L118 134 M80 62 L104 80" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><circle cx="216" cy="70" r="42" fill="none" stroke="#d8b25e" stroke-width="5"/><path d="M186 92 L192 88 M216 34 V40 M246 92 L240 88 M184 58 L190 60 M248 58 L242 60" stroke="#ece5cf" stroke-width="3" stroke-linecap="round" opacity=".7"/><path d="M216 70 L240 50" stroke="#e2ab47" stroke-width="4.5" stroke-linecap="round"/><circle cx="216" cy="70" r="5" fill="#ece5cf"/></svg>""",
     "Düzenli egzersiz tansiyonu birkaç puan düşürür: yürüyüş, güç çalışması ve izometrik duvar oturuşu, evde doğru ölçüm ve dikkat edilecekler.",
     None, "C_ICU"),
]
SELFS = [
    # dosya, en, part, başlık, hap, C_, TH, açıklama, SELF'te kimden sonra, SELF_GROUPS grubu, grupta kimden sonra
    ("tansiyon-gunlugu.html", "blood-pressure-diary.html", "self14_part.py", "Ev tansiyon günlüğü", "Tansiyon günlüğü", "C_TG",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><rect x="70" y="40" width="92" height="80" rx="12" fill="none" stroke="#8fa476" stroke-width="5"/><rect x="84" y="54" width="64" height="32" rx="5" fill="rgba(236,229,207,.12)"/><path d="M94 64 H122 M94 76 H112" stroke="#e2ab47" stroke-width="4" stroke-linecap="round"/><circle cx="116" cy="104" r="6" fill="#d8b25e"/><path d="M162 80 C178 80 176 112 192 112" fill="none" stroke="rgba(236,229,207,.4)" stroke-width="3"/><rect x="206" y="24" width="72" height="104" rx="8" fill="none" stroke="rgba(236,229,207,.45)" stroke-width="3"/><g fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M218 48 l4 4 l8 -9" stroke="#8fa476" stroke-width="3.5"/><path d="M238 48 H266" stroke="rgba(236,229,207,.4)" stroke-width="3"/><path d="M218 74 l4 4 l8 -9" stroke="#8fa476" stroke-width="3.5"/><path d="M238 74 H262" stroke="rgba(236,229,207,.4)" stroke-width="3"/><path d="M218 100 l4 4 l8 -9" stroke="#e2ab47" stroke-width="3.5"/><path d="M238 100 H258" stroke="rgba(236,229,207,.4)" stroke-width="3"/></g></svg>""",
     "Evde doğru tansiyon ölçümü: 5 dakika dinlenme ve 1 dakika ara zamanlayıcısı, sabah-akşam kayıt, ilk gün hariç ortalama ve hekime götürülecek dosya.",
     "C_PULSE", "Kendinizi ölçün", "nabiz-olcer.html"),
    ("alti-dakika-yurume-testi.html", "six-minute-walk-test.html", "self14_part.py", "6 dakika yürüme testi", "6 dk yürüme testi", "C_AW",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M40 136 H280" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M50 134 L60 108 L70 134 Z M250 134 L260 108 L270 134 Z" fill="#e2ab47"/><path d="M80 124 H240" stroke="rgba(236,229,207,.4)" stroke-width="3" stroke-dasharray="6 7" stroke-linecap="round"/><path d="M228 116 L240 124 L228 132 M92 116 L80 124 L92 132" fill="none" stroke="rgba(236,229,207,.5)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><circle cx="150" cy="30" r="10" fill="#8fa476"/><path d="M150 42 L146 78 L134 96 L130 116 M146 78 L160 96 L166 114 M148 52 L134 70 M148 52 L166 64" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><circle cx="240" cy="54" r="22" fill="none" stroke="#d8b25e" stroke-width="4"/><path d="M240 54 V40 M240 54 L250 60 M234 28 H246" stroke="#ece5cf" stroke-width="3" stroke-linecap="round"/></svg>""",
     "6 dakikada ne kadar yürüyebiliyorsunuz? Standart yönlendirmeli süreölçer, parkur sayacı, yaşa göre beklenen mesafe ve sonuç kaydı.",
     "C_AD", "Kendinizi ölçün", "iki-dakika-adim-testi.html"),
]
RELATED_NEW = {
    "diyabette-egzersiz.html": ["yemek-sonrasi-yuruyus.html", "diyabetik-noropati.html", "guc-devresi.html"],
    "yogun-bakim-sonrasi.html": ["sarkopeni.html", "ic-cekis.html", "alti-dakika-yurume-testi.html"],
    "yuksek-tansiyon.html": ["duvar-oturusu.html", "tansiyon-gunlugu.html", "tempolu-yuruyus.html"],
    "tansiyon-gunlugu.html": ["yuksek-tansiyon.html", "duvar-oturusu.html", "nabiz-olcer.html"],
    "alti-dakika-yurume-testi.html": ["iki-dakika-adim-testi.html", "kalp-yetmezligi.html", "koah.html"],
}
RELATED_ADD = [  # (var olan sayfa, eklenecek)
    ("yemek-sonrasi-yuruyus.html", "diyabette-egzersiz.html"),
    ("diyabetik-noropati.html", "diyabette-egzersiz.html"),
    ("duvar-oturusu.html", "yuksek-tansiyon.html"),
    ("nabiz-olcer.html", "tansiyon-gunlugu.html"),
    ("kalp-yetmezligi.html", "alti-dakika-yurume-testi.html"),
    ("koah.html", "alti-dakika-yurume-testi.html"),
    ("sarkopeni.html", "yogun-bakim-sonrasi.html"),
]

# exec listesi
# cond61, sn_stair çizimi self4_part.py'de tanımlandığı için self12_part.py'den SONRA exec edilir. Yeni partlar zincirin sonuna eklenir.
for part, after in (("self12_part.py", "self11_part.py"), ("cond61_part.py", "self12_part.py"), ("cond62_part.py", "cond61_part.py"), ("cond63_part.py", "cond62_part.py"),
                    ("self13_part.py", "cond63_part.py"), ("cond64_part.py", "self13_part.py"), ("cond65_part.py", "cond64_part.py"), ("cond66_part.py", "cond65_part.py"),
                    ("cond67_part.py", "cond66_part.py"), ("cond68_part.py", "cond67_part.py"), ("cond69_part.py", "cond68_part.py"), ("self14_part.py", "cond69_part.py")):
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

# ------------------------------------------------------------------ Bilim gündemi (3. tur, 23 Ekim 2026)
s = open(B, encoding="utf-8").read()
IL_NEW = {
"IL_ESPRESSO": '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 160 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<rect x="160" y="30" width="130" height="86" rx="8" fill="none" stroke="rgba(236,229,207,.4)" stroke-width="3"/>
<path d="M172 94 C192 78 212 98 232 84 C248 74 264 84 278 76" fill="none" stroke="rgba(143,164,118,.5)" stroke-width="3" stroke-linecap="round"/>
<path d="M196 70 C206 56 230 52 246 62 C252 66 256 66 262 62 C260 70 254 74 246 74 C232 82 212 82 196 70 Z" fill="#d8b25e"/>
<path d="M222 58 L226 48 L232 58" fill="#d8b25e"/>
<path d="M206 136 V116 M244 136 V116" stroke="rgba(236,229,207,.3)" stroke-width="3"/>
<path d="M44 110 H112 M56 110 V160 M104 110 V160" stroke="#8a6a44" stroke-width="5" stroke-linecap="round" fill="none"/>
<circle cx="84" cy="44" r="10" fill="#8fa476"/>
<path d="M84 58 L86 104 L120 106 L122 158 M84 70 L118 78 L148 72" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="148" cy="72" r="5" fill="#e2ab47"/></svg>''',
"IL_OAEX": '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 156 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<g fill="none" stroke-linecap="round" stroke-linejoin="round"><rect x="40" y="40" width="96" height="110" rx="8" stroke="rgba(236,229,207,.25)" stroke-width="3"/><rect x="50" y="30" width="96" height="110" rx="8" stroke="rgba(236,229,207,.35)" stroke-width="3" fill="#223020"/><rect x="60" y="20" width="96" height="110" rx="8" stroke="rgba(236,229,207,.5)" stroke-width="3" fill="#223020"/>
<path d="M76 44 H140 M76 60 H132 M76 76 H136" stroke="rgba(236,229,207,.35)" stroke-width="3"/></g>
<path d="M76 116 V108 M92 116 V102 M108 116 V110 M124 116 V106" stroke="#e2ab47" stroke-width="7" stroke-linecap="round"/>
<path d="M198 24 C194 50 194 70 202 86 M246 24 C252 50 252 70 244 86" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/>
<path d="M202 96 C196 116 196 136 200 158 M244 96 C250 116 250 136 246 158" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/>
<path d="M200 88 C214 96 232 96 246 88 M200 94 C214 102 232 102 246 94" fill="none" stroke="#d8b25e" stroke-width="3.5" stroke-linecap="round"/>
<circle cx="276" cy="56" r="8" fill="none" stroke="#e2ab47" stroke-width="3"/><path d="M282 62 L292 72" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>''',
"IL_DEPEX": '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 156 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<path d="M58 70 C50 70 44 64 44 57 C44 49 51 43 59 44 C62 36 70 31 79 32 C89 33 96 41 96 50 C103 50 108 55 108 62 C108 66 104 70 99 70 Z" fill="rgba(236,229,207,.22)"/>
<path d="M56 82 L52 92 M72 82 L68 92 M88 82 L84 92" stroke="rgba(236,229,207,.25)" stroke-width="3" stroke-linecap="round"/>
<circle cx="250" cy="48" r="18" fill="#d8b25e"/>
<path d="M250 18 V24 M250 72 V78 M220 48 H226 M274 48 H280 M229 27 L233 31 M267 65 L271 69 M271 27 L267 31 M229 69 L233 65" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/>
<circle cx="164" cy="54" r="10" fill="#8fa476"/>
<path d="M164 68 L160 108 L146 130 L142 156 M160 108 L176 128 L182 154 M162 78 L146 98 M162 78 L182 90" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M120 116 C128 104 134 104 140 110" fill="none" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round" stroke-dasharray="3 5"/></svg>''',
}
NEWS_ADD = [
("IL_BCI", ''' dict(il=IL_ESPRESSO, g="beyin", cat="İnme", date="Mart 2026",
      title="İnmeden hemen sonra üç kat fazla kol terapisi, üç ayda ek yarar sağlamadı",
      text="Yeni Zelanda'da Auckland Üniversitesi'nden araştırmacıların Mart 2026'da Brain Communications'ta yayımladığı ESPRESSO çalışmasına, inmeden sonraki ilk iki hafta içindeki 64 hasta katıldı; katılımcılar kol ve elin toparlanma potansiyelini gösteren bir biyobelirteçle seçildi. Hastalar olağan bakımlarına ek olarak 3 hafta boyunca, hafta içi her gün 90 dakika daha terapi aldı: yarısı ekranda bir yunus gibi deniz canlısını kol hareketleriyle yönlendirdiği oyun tabanlı bir terapi, diğer yarısı aynı sürede klasik terapi. İki grup da terapi süresince belirgin iyileşti; 3. ayda kol ve el işlevini ölçen testte (ARAT) aralarında fark yoktu. Yaklaşık üç kat daha fazla terapi almalarına karşın, aynı merkezde daha önce yalnızca olağan bakım almış hastalardan da daha iyi değillerdi.",
      point="Araştırmacılara göre inmeden sonraki ilk haftalarda kol ve eldeki toparlanma büyük ölçüde beynin kendiliğinden onarım süreçlerine bağlı; bu dönemde terapinin miktarını artırmak sonucu belirgin değiştirmeyebilir. Çalışma küçük, tek merkezli ve keşif amaçlı (faz IIa); olağan bakım grubu aynı dönemde değil, daha önce izlenmiş hastalardan oluşuyordu. Bulgu erken dönemde terapinin gereksiz olduğu anlamına gelmiyor; hangi hastada, hangi zamanlamada ve ne kadar terapinin fark yarattığı daha büyük çalışmalarla netleşecek.",
      src=[("Brain Communications, Mart 2026", "https://academic.oup.com/braincomms/article/8/2/fcag057/8553076"), ("Neuroscience News (Auckland Üniversitesi), 26 Mart 2026", "https://neurosciencenews.com/stroke-rehab-early-intensity-recovery-30396"), ("Auckland Üniversitesi, 22 Nisan 2026", "https://www.auckland.ac.nz/en/news/2026/04/22/-more-therapy--earlier--didn-t-boost--stroke-recovery-.html")],
      rel=("İnme rehabilitasyonu", "inme-rehabilitasyonu.html")),
'''),
("IL_MAMMO", ''' dict(il=IL_OAEX, g="hareket", cat="Kireçlenme", date="Şubat 2026",
      title="Kireçlenmede egzersizin ağrıya etkisi küçük ve kısa süreli olabilir: büyük bir derleme tartışma başlattı",
      text="Şubat 2026'da RMD Open'da yayımlanan bir şemsiye derlemede, kireçlenmede egzersiz tedavisini inceleyen 5 sistematik derleme (8.631 katılımcı) ve 28 randomize çalışma (4.360 katılımcı) bir araya getirildi; çalışmaların 23'ü diz ya da kalça, 3'ü el, 2'si ayak bileği kireçlenmesiyle ilgiliydi. Sahte tedaviye ya da tedavisizliğe göre egzersiz dizde ağrıyı az ve kısa süreli azalttı; kanıtın güvenilirliği çok düşüktü ve büyük, uzun çalışmalarda etki daha da küçüktü. Kalçada etki ihmal edilebilir düzeydeydi (orta güvenilirlik), elde küçüktü. Egzersiz; hasta eğitimi, manuel terapi, ağrı kesiciler, eklem içi kortizon ya da hyaluronik asit iğneleri ve artroskopik diz cerrahisiyle benzer sonuç verdi. Tek tek çalışmalarda, seçilmiş hastalarda uzun vadede diz osteotomisi ve protezden daha az etkiliydi.",
      point="Yazarlar sonuçlarının egzersizin genel sağlığa yararlarını ya da hastaların egzersizi tercih etmesini geçersiz kılmadığını, ancak egzersizin her hastada tek başına ilk basamak tedavi olarak öne çıkarılmasını sorguladığını belirtiyor ve ortak karar vermeyi öneriyor. Derleme bazı sistematik derlemeleri önceliklendirdi; doğrudan karşılaştırmalar azdı, hastaların belirti şiddeti çok farklıydı ve bazı çalışmalarda egzersizle birlikte başka tedaviler de uygulandı. 2025 sonunda The BMJ'de yayımlanan ve 217 çalışmayı kapsayan bir ağ meta-analizi ise diz kireçlenmesinde özellikle aerobik egzersizin ağrıyı ve işlevi orta güvenilirlikle iyileştirdiğini bildirmişti. Egzersiz ucuz ve güvenli; ama beklentiyi gerçekçi tutmak ve programı kişiye göre seçmek önemli.",
      src=[("RMD Open, Şubat 2026", "https://doi.org/10.1136/rmdopen-2025-006275"), ("BMJ Group, 17 Şubat 2026", "https://bmjgroup.com/effectiveness-of-exercise-to-ease-osteoarthritis-symptoms-likely-minimal-and-transient/"), ("Medical Republic, 19 Şubat 2026", "https://www.medicalrepublic.com.au/?p=123345"), ("ScienceDaily, 25 Şubat 2026", "https://www.sciencedaily.com/releases/2026/02/260225081208.htm"), ("The BMJ, 2025 (diz kireçlenmesinde egzersiz türleri)", "https://doi.org/10.1136/bmj-2025-085242")],
      rel=("Diz kireçlenmesi rehberi", "diz-kireclenmesi.html")),
'''),
("IL_MAMMO", ''' dict(il=IL_DEPEX, g="beyin", cat="Depresyon", date="Ocak 2026",
      title="Cochrane: Egzersiz depresyon belirtilerini azaltıyor, etkisi psikoterapiye yakın olabilir",
      text="Ocak 2026'da güncellenen Cochrane derlemesinde, depresyonu olan 4.985 kişiyle yapılmış 73 randomize çalışma incelendi. Hiç tedavi almama ya da kontrol koşullarıyla karşılaştırıldığında egzersiz depresyon belirtilerini orta düzeyde azalttı (standart ortalama fark −0,67; düşük güvenilirlik); yalnızca yöntemi en sağlam 7 çalışmaya bakıldığında etki küçüldü (−0,46) ama sürdü. Psikoterapiyle karşılaştırıldığında egzersiz benzer sonuç verdi (10 çalışma, 414 kişi; orta güvenilirlik); ilaç tedavisiyle karşılaştırıldığında da belirgin fark yoktu (5 çalışma, 330 kişi; düşük güvenilirlik). Orta yoğunlukta, toplam 13–36 seanslık programlar ve karma ya da direnç egzersizleri, yalnızca aerobik egzersize göre biraz daha yararlı görünüyordu.",
      point="Çalışmaların çoğu küçüktü ve yanlılık riski yüksekti; uzun vadeli veriler az. Bağımsız uzmanlar, egzersizin psikoterapi ve ilaçla benzer olduğu sonucunun az sayıda çalışmaya dayandığını, denetimli programların motivasyonu yüksek gönüllüleri çektiğini ve egzersizin en iyi var olan tedavilere ek olarak düşünülebileceğini vurguluyor. Egzersizin yan etkisi azdır; ama tedavinizi değiştirmeden ya da ilacınızı bırakmadan önce mutlaka hekiminizle konuşun.",
      src=[("Cochrane Library, Ocak 2026", "https://doi.org/10.1002/14651858.CD004366.pub7"), ("ScienceDaily, 8 Ocak 2026", "https://www.sciencedaily.com/releases/2026/01/260107225516.htm"), ("Science Media Centre uzman görüşleri, 8 Ocak 2026", "https://www.sciencemediacentre.org/expert-reaction-to-exercise-having-similar-results-as-therapy-for-treating-depression/"), ("HCPLive", "https://www.hcplive.com/view/exercise-may-be-effective-therapy-for-alleviating-depression-symptoms"), ("Medicine Today, Şubat 2026", "https://medicinetoday.com.au/mt/2026/february/in-brief/exercise-depression-similar-effects-other-active-treatments-finds-review")],
      rel=("Ruh sağlığı için egzersiz", "ruh-sagligi-egzersiz.html")),
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

# Var olan Parkinson haberini (IL_PDACT) sayılarla ve iki ek kaynakla güncelle
PD_OLD_TEXT = "Haftada 8 saatten fazla orta ya da yüksek tempolu fiziksel aktivite (iş, ev işleri ve hobiler dahil) yapanlarda, 4 saatten az yapanlara göre düşünme becerilerindeki gerileme ve hareket belirtilerindeki kötüleşme daha yavaştı. Toplam süreye, yoğunlukla ağırlıklandırılmış miktara ve yalnızca yüksek tempolu aktiviteye bakıldığında da benzer ilişki görüldü."
PD_NEW_TEXT = "Katılımcılar iş, ev işleri ve hobiler dahil haftada kaç saat orta ya da yüksek tempolu aktivite yaptıklarını bildirdi ve üç gruba ayrıldı: 4 saate kadar, 4–8 saat ve 8 saatten fazla. 30 puanlık düşünme testinde yıllık düşüş en az hareket edenlerde 0,478 puan, en çok hareket edenlerde yalnızca 0,007 puandı. Hareket belirtileri puanı (0–132; başlangıç ortalaması 23) en az hareket edenlerde yılda 0,143 puan kötüleşirken en çok hareket edenlerde yılda 0,783 puan hafifledi. Toplam süreye, yoğunlukla ağırlıklandırılmış miktara ve yalnızca yüksek tempolu aktiviteye bakıldığında da benzer ilişki görüldü."
PD_OLD_POINT = "Aktivite, kişilerin kendi beyanıyla anketle ölçüldü ve gruplar arasındaki farklar küçüktü; araştırmacılara göre bu küçük farklar yıllar içinde anlam kazanabilir."
PD_NEW_POINT = "Aktivite, kişilerin kendi beyanıyla anketle ölçüldü ve gruplar arasındaki farklar küçüktü; araştırmacılara göre bu küçük farklar yıllar içinde anlam kazanabilir. Katılımcıların düşünme becerileri başlangıçta iyiydi; %98'i beyaz ve üçte ikisi erkekti. Healio'nun aktardığına göre yoğunluk tek başına ele alındığında puanlardaki değişimle anlamlı ilişki göstermedi; araştırmacılar toplam sürenin yoğunluktan daha belirleyici olabileceğini düşünüyor. Yüksek tempolu egzersizin etkisini sınayan SPARX3 adlı randomize çalışma sürüyor."
PD_OLD_SRC = '("Neurology, 7 Ekim 2026", "https://doi.org/10.1212/WNL.0000000000218682")],'
PD_NEW_SRC = '("Neurology, 7 Ekim 2026", "https://doi.org/10.1212/WNL.0000000000218682"), ("Healio, 14 Ekim 2026", "https://www.healio.com/news/neurology/20261014/physical-activity-associated-with-slower-cognitive-motor-decline-in-parkinsons-disease"), ("ScienceDaily, 23 Ekim 2026", "https://www.sciencedaily.com/releases/2026/10/261022081306.htm")],'
if PD_NEW_TEXT not in s:
    for a, b in ((PD_OLD_TEXT, PD_NEW_TEXT), (PD_OLD_POINT, PD_NEW_POINT), (PD_OLD_SRC, PD_NEW_SRC)):
        assert s.count(a) == 1, a[:60]
        s = s.replace(a, b, 1)
open(B, "w", encoding="utf-8").write(s)
print("haberler tamam")
