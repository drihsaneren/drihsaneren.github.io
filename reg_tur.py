# -*- coding: utf-8 -*-
"""Yeni sayfaları ve haberleri build_pages.py / i18n_map.py'ye kaydeder (22 Ekim 2026 1. tur, 23 Ekim 2026 2. tur).
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


# ------------------------------------------------------------------ sayfalar (23 Ekim 2026, 2. tur; 1. turun listeleri git geçmişinde: fcf2047)
CONDS = [
    # dosya, en, part, kategori, başlık, hap, C_, TH, kısa açıklama, bölge (None = REHAB), (AGR'de/REHAB'da kimden sonra)
    ("kalp-yetmezligi.html", "heart-failure.html", "cond64_part.py", "Rehabilitasyon rehberi",
     "Kalp yetmezliğinde egzersiz", "Kalp yetmezliği", "C_HF",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 136 H260" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><circle cx="104" cy="34" r="11" fill="#8fa476"/><path d="M104 48 L100 88 L86 110 L82 134 M100 88 L116 108 L122 132 M102 58 L88 78 M102 58 L120 72" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M214 112 C186 92 166 74 166 54 C166 40 176 30 190 30 C200 30 208 36 214 46 C220 36 228 30 238 30 C252 30 262 40 262 54 C262 74 242 92 214 112 Z" fill="none" stroke="#d8b25e" stroke-width="6" stroke-linejoin="round"/><path d="M174 70 H196 L204 54 L214 88 L224 62 L230 70 H254" fill="none" stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>""",
     "Nefes darlığı ve yorgunluk varken egzersiz güvenli mi? Kimler başlayabilir, nasıl ilerlenir, her gün tartılmak ve altı ev egzersizi.",
     None, "C_PAD"),
    ("dupuytren-kontrakturu.html", "dupuytrens-contracture.html", "cond65_part.py", "Hastalık rehberi",
     "Dupuytren kontraktürü", "Dupuytren", "C_DUP",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M120 136 V96 C120 84 126 76 136 74 L196 70 C206 70 212 78 212 88 V136" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M140 74 V28 M160 72 V20 M180 71 V26" stroke="#8fa476" stroke-width="12" stroke-linecap="round"/><path d="M200 72 C206 58 212 54 220 60 C226 66 222 78 214 82" fill="none" stroke="#8fa476" stroke-width="12" stroke-linecap="round"/><path d="M206 120 C206 104 208 90 212 82" fill="none" stroke="#e2ab47" stroke-width="4" stroke-linecap="round"/><circle cx="208" cy="104" r="5" fill="#d8b25e"/><path d="M236 104 H282" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M240 100 C252 84 268 84 280 100" fill="none" stroke="#ece5cf" stroke-width="3" stroke-dasharray="4 5" stroke-linecap="round" opacity=".7"/></svg>""",
     "Avuç içinde sertlik, parmak bükülüp düzelmiyor mu? Masa testi, tedavi seçenekleri, işlemden sonra el egzersizleri ve atel.",
     "omuz", "C_TF"),
    ("omurga-kirigi.html", "vertebral-fracture.html", "cond66_part.py", "Hastalık rehberi",
     "Kemik erimesine bağlı omurga kırığı", "Omurga kırığı", "C_VF",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><g fill="#8fa476"><rect x="128" y="14" width="44" height="16" rx="5"/><rect x="126" y="36" width="48" height="17" rx="5"/><rect x="124" y="82" width="52" height="18" rx="5"/><rect x="122" y="106" width="56" height="19" rx="5"/></g><path d="M124 60 L176 60 L176 76 L124 72 Z" fill="#e2ab47"/><path d="M180 66 H198" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/><g fill="none" stroke="#d8b25e" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><circle cx="242" cy="40" r="10" fill="#d8b25e" stroke="none"/><path d="M240 54 V96 L232 132 M240 96 L250 132 M240 64 L224 82 M240 64 L258 80"/></g><path d="M214 40 V132" stroke="rgba(236,229,207,.35)" stroke-width="3" stroke-dasharray="5 6"/></svg>""",
     "Ani sırt ağrısı, boy kısalması? Kemik erimesine bağlı omurga kırığında tanı, ağrıyla başa çıkma, güvenli egzersizler ve uyarı işaretleri.",
     "bel", "C_KY"),
]
SELFS = [
    # dosya, en, part, başlık, hap, C_, TH, açıklama, SELF'te kimden sonra, SELF_GROUPS grubu, grupta kimden sonra
    ("yemek-sonrasi-yuruyus.html", "walk-after-meals.html", "self13_part.py", "Yemek sonrası yürüyüş", "Yemek sonrası yürüyüş", "C_YY",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 136 H260" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><ellipse cx="104" cy="104" rx="42" ry="12" fill="none" stroke="rgba(236,229,207,.35)" stroke-width="4"/><ellipse cx="104" cy="100" rx="26" ry="6" fill="#d8b25e" opacity=".75"/><path d="M58 70 V96 M54 70 V80 M62 70 V80 M150 70 V96" stroke="rgba(236,229,207,.45)" stroke-width="3" stroke-linecap="round"/><circle cx="214" cy="32" r="11" fill="#8fa476"/><path d="M214 46 L210 86 L196 108 L192 132 M210 86 L226 106 L232 130 M212 56 L198 76 M212 56 L230 70" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M252 54 A16 16 0 1 1 252 86 A16 16 0 1 1 252 54" fill="none" stroke="#e2ab47" stroke-width="4"/><path d="M252 70 V60 M252 70 L260 74" stroke="#ece5cf" stroke-width="3" stroke-linecap="round"/></svg>""",
     "Yemekten sonra 10 dakika yürüyüş kan şekerinin yükselmesini yumuşatır: öğün ve süre seçimi, zamanlayıcı ve günlük takip.",
     "C_GD", "Zamanlayıcıyla birlikte yapın", "tempolu-yuruyus.html"),
    ("denge-antrenmani.html", "balance-training.html", "self13_part.py", "Denge antrenmanı", "Denge antrenmanı", "C_DB",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 136 H260" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M188 76 H260 M200 76 V136 M250 76 V136" stroke="#8a6a44" stroke-width="6" stroke-linecap="round" fill="none"/><circle cx="146" cy="26" r="11" fill="#8fa476"/><path d="M146 40 V88 M146 88 L142 134 M146 88 L152 110 L150 134 M146 50 L174 72 L190 74 M146 50 L124 66" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M134 136 H162" stroke="#e2ab47" stroke-width="5" stroke-linecap="round"/><path d="M96 48 C88 60 88 76 96 88 M84 56 C80 64 80 72 84 80" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" opacity=".7"/></svg>""",
     "Düşmeleri önlemek için Otago programından uyarlanmış altı denge hareketi: üç destek seviyesi, duruş zamanlayıcısı ve 12 haftalık takip.",
     "C_YY", "Zamanlayıcıyla birlikte yapın", "yemek-sonrasi-yuruyus.html"),
]
RELATED_NEW = {
    "kalp-yetmezligi.html": ["kalp-rehabilitasyonu.html", "tempolu-yuruyus.html", "koah.html"],
    "dupuytren-kontrakturu.html": ["tetik-parmak.html", "el-kireclenmesi.html", "karpal-tunel-sendromu.html"],
    "omurga-kirigi.html": ["kemik-erimesi.html", "kambur-durus.html", "dusme-onleme.html"],
    "yemek-sonrasi-yuruyus.html": ["tempolu-yuruyus.html", "oturma-suresi.html", "guc-devresi.html"],
    "denge-antrenmani.html": ["dort-asamali-denge-testi.html", "dusme-onleme.html", "guc-devresi.html"],
}
RELATED_ADD = [  # (var olan sayfa, eklenecek)
    ("kalp-rehabilitasyonu.html", "kalp-yetmezligi.html"),
    ("koah.html", "kalp-yetmezligi.html"),
    ("tetik-parmak.html", "dupuytren-kontrakturu.html"),
    ("kemik-erimesi.html", "omurga-kirigi.html"),
    ("kambur-durus.html", "omurga-kirigi.html"),
    ("dusme-onleme.html", "denge-antrenmani.html"),
    ("dort-asamali-denge-testi.html", "denge-antrenmani.html"),
    ("tempolu-yuruyus.html", "yemek-sonrasi-yuruyus.html"),
]

# exec listesi
# cond61, sn_stair çizimi self4_part.py'de tanımlandığı için self12_part.py'den SONRA exec edilir. Yeni partlar zincirin sonuna eklenir.
for part, after in (("self12_part.py", "self11_part.py"), ("cond61_part.py", "self12_part.py"), ("cond62_part.py", "cond61_part.py"), ("cond63_part.py", "cond62_part.py"),
                    ("self13_part.py", "cond63_part.py"), ("cond64_part.py", "self13_part.py"), ("cond65_part.py", "cond64_part.py"), ("cond66_part.py", "cond65_part.py")):
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

# ------------------------------------------------------------------ Bilim gündemi (2. tur, 23 Ekim 2026)
s = open(B, encoding="utf-8").read()
IL_NEW = {
"IL_ESTEPS": '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 156 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<rect x="44" y="34" width="112" height="78" rx="8" fill="none" stroke="rgba(236,229,207,.4)" stroke-width="3"/>
<path d="M84 112 L78 132 H122 L116 112" fill="none" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linejoin="round"/>
<g stroke-linecap="round" stroke-linejoin="round" fill="none"><path d="M60 56 l5 5 l9 -10" stroke="#8fa476" stroke-width="3.5"/><path d="M82 56 H140" stroke="rgba(236,229,207,.35)" stroke-width="3"/>
<path d="M60 76 l5 5 l9 -10" stroke="#8fa476" stroke-width="3.5"/><path d="M82 76 H130" stroke="rgba(236,229,207,.35)" stroke-width="3"/>
<path d="M60 96 l5 5 l9 -10" stroke="#e2ab47" stroke-width="3.5"/><path d="M82 96 H124" stroke="rgba(236,229,207,.35)" stroke-width="3"/></g>
<path d="M192 92 H284 M204 92 V156 M276 92 V156" stroke="#8a6a44" stroke-width="5" stroke-linecap="round" fill="none"/>
<circle cx="236" cy="44" r="9" fill="#8fa476"/>
<path d="M236 56 V104 M236 104 L232 156 M236 104 L242 128 L240 156 M236 66 L262 86 L274 90 M236 66 L218 80" fill="none" stroke="#8fa476" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>''',
"IL_BELT": '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M124 22 C116 52 112 76 114 100 C116 124 112 146 108 164 M196 22 C204 52 208 76 206 100 C204 124 208 146 212 164" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/>
<path d="M110 86 C140 96 180 96 210 86 L212 124 C180 134 140 134 108 124 Z" fill="#d8b25e" opacity=".85"/>
<path d="M150 92 V130 M170 92 V130" stroke="#223020" stroke-width="2.5" stroke-dasharray="4 4"/>
<path d="M240 60 C256 72 256 92 240 104 M254 52 C276 70 276 98 254 116" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" opacity=".7"/>
<path d="M40 164 H280" stroke="rgba(236,229,207,.18)" stroke-width="2"/></svg>''',
"IL_PACBACK": '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 156 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<circle cx="96" cy="40" r="10" fill="#8fa476"/>
<path d="M96 54 L94 104 L82 130 L80 156 M94 104 L108 130 L112 156 M96 64 L78 86 M96 64 L118 80" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="94" cy="98" r="11" fill="none" stroke="#e2ab47" stroke-width="3"/>
<rect x="170" y="36" width="96" height="104" rx="10" fill="none" stroke="rgba(236,229,207,.4)" stroke-width="3"/>
<g stroke-linecap="round"><path d="M186 62 H250" stroke="#d8b25e" stroke-width="4"/><path d="M186 84 H240" stroke="rgba(236,229,207,.35)" stroke-width="4"/><path d="M186 106 H232" stroke="rgba(236,229,207,.35)" stroke-width="4"/></g>
<path d="M190 124 C204 114 218 132 232 120 C240 114 248 118 252 122" fill="none" stroke="#8fa476" stroke-width="3.5" stroke-linecap="round"/></svg>''',
}
NEWS_ADD = [
("IL_VITAL", ''' dict(il=IL_ESTEPS, g="hareket", cat="Düşme", date="Ekim 2026",
      title="Aile hekimliğinde elektronik kayıt üzerinden önerilen ev egzersizleri düşmeleri biraz azalttı",
      text="ABD'de Brigham and Women's Hastanesi ve Teksas Üniversitesi Tıp Fakültesi'nden (UTMB) araştırmacıların 16 Ekim 2026'da JAMA Network Open'da yayımladığı eSTEPS çalışmasında, tek bir sağlık sistemine bağlı 22 aile hekimliği muayenehanesi rastgele iki gruba ayrıldı. Düşme riski taramasında riskli çıkan 65 yaş üstü 11.945 kişi (yaş ortalaması 77, üçte ikisi kadın) 12–23 ay izlendi. Müdahale grubundaki muayenehanelerde elektronik hasta kaydına eklenen bir araç, hekimlere hastaya göre ayarlanmış ev egzersizleri önermeyi hatırlattı. Egzersizler Otago programından sadeleştirilmişti: dört zorluk seviyesi, yaklaşık 10 dakika süren ve ekipman gerektirmeyen bir program; hastalara el kitabı, web sitesi ve videolu bir uygulama da sunuldu. Kayıtlara geçen düşmeler müdahale grubunda 100 hasta-yılında 19,3, olağan bakım grubunda 21,2 oldu; yani %9 daha azdı. Düşmeye bağlı yaralanmalar 15,7'ye karşı 16,7 idi; ölümlerde fark görülmedi.",
      point="Etki küçük; üstelik müdahale grubundaki hastaların yalnızca yaklaşık %22'sine egzersiz reçetesi verildi ve hastaların egzersizleri yapıp yapmadığı izlenmedi. Düşmeler tanı kodlarından sayıldığı için bildirilmeyen düşmeler gözden kaçmış olabilir; çalışma tek bir sağlık sisteminde yapıldı ve gruplar başlangıçta bazı açılardan farklıydı. Yine de sonuç, kısa ve düzenli ev egzersizlerinin günlük muayene akışı içinde, çok sayıda kişiye önerilebileceğini gösteriyor. Benzer hareketleri Kendine iyi bak bölümündeki denge antrenmanıyla yapabilirsiniz.",
      src=[("JAMA Network Open, 16 Ekim 2026", "https://doi.org/10.1001/jamanetworkopen.2026.39240"), ("Medical Daily, 17 Ekim 2026", "https://www.medicaldaily.com/older-adults-falls-home-strength-balance-exercise-trial-480083"), ("UTMB, 19 Ekim 2026", "https://www.utmb.edu/scoa/news-and-events/archive/2026/10/19/study-finds-electronic-health-record-tool-can-help-reduce-falls-among-older-adults")],
      rel=("Denge antrenmanı", "denge-antrenmani.html")),
'''),
("IL_DEMPA", ''' dict(il=IL_BELT, g="hareket", cat="Bel ağrısı", date="Ağustos 2026",
      title="Bel ağrısında yumuşak bel korsesi: 12 haftada günlük işlevde ılımlı ek iyileşme",
      text="Fransa'da 17 merkezde yürütülen ve 19 Ağustos 2026'da JAMA Network Open'da yayımlanan LOMBACT çalışmasına, 1–6 aydır süren ve belirli bir nedene bağlanamayan bel ağrısı olan 168 yetişkin (yaş ortalaması 49) katıldı. Katılımcıların yarısı olağan bakımın yanında gün içinde 4–8 saat yumuşak, ayarlanabilir bir bel korsesi taktı; diğer yarısı yalnızca olağan bakım aldı. İki gruba da aktif kalmaları önerildi. 12 haftada günlük kısıtlılık puanı (Oswestry, 0–100) korse grubunda 10, diğer grupta 5,3 puan iyileşti; kısıtlılığı en az %30 azalanlar korse grubunda yaklaşık %61, diğer grupta %41 oldu. Korse grubunda ağrı, özellikle hareket sırasındaki ağrı, daha çok azaldı; ağrı kesici kullananların oranı da daha düşüktü (yaklaşık yarıya karşı üçte iki). Korsenin sensör verilerine göre katılımcılar onu taktıkları günlerde ortalama 4 saat kadar kullandı; altı kişide rahatsızlık ya da ciltte tahriş gibi hafif sorunlar görüldü.",
      point="Katılımcılar hangi grupta olduklarını biliyordu ve sahte bir korseyle karşılaştırma yapılmadı; beklentiler sonucu etkilemiş olabilir. İzlem yalnızca 12 hafta sürdü, korse bırakıldıktan sonraki durum incelenmedi ve çalışmayı korseyi üreten şirket finanse etti. Dünya Sağlık Örgütü 2023'te, kronik bel ağrısında korse ya da destek kemerlerinin rutin olarak önerilmemesini tavsiye etmişti. Araştırmacılar da korsenin aktif tedavinin yerine geçmemesi gerektiğini, hareket sırasındaki rahatsızlığı azaltarak bazı hastaların aktif kalmasına yardımcı olabileceğini vurguluyor.",
      src=[("JAMA Network Open, 19 Ağustos 2026", "https://doi.org/10.1001/jamanetworkopen.2026.29793"), ("ScienceAlert, 5 Eylül 2026", "https://www.sciencealert.com/?p=217137"), ("Harvard Health Publishing, 16 Ekim 2026", "https://www.health.harvard.edu/bones-and-joints/a-lumbar-belt-may-help-ease-low-back-pain")],
      rel=("Bel ağrısı rehberi", "bel-agrisi.html")),
'''),
("IL_FAST4", ''' dict(il=IL_PACBACK, g="hareket", cat="Bel ağrısı", date="Haziran 2026",
      title="Yeni başlayan bel ağrısında destekli kendi kendine yönetim, ağrının bir yıl sonraki etkisini biraz azalttı",
      text="ABD'de Minnesota ve Pittsburgh üniversitelerinde yürütülen ve Haziran 2026'da JAMA Internal Medicine'de yayımlanan PACBACK çalışmasına, yeni başlamış ya da birkaç haftadır süren bel ağrısı olan ve bir tarama testine göre ağrısı kronikleşme riski orta ya da yüksek bulunan 1.000 yetişkin katıldı. Katılımcılar 8 hafta boyunca dört yaklaşımdan birine ayrıldı: kılavuzlara dayalı tıbbi bakım (çoğunlukla ağrı kesici ve kas gevşetici ilaçlar), omurga manipülasyonu, klinisyen destekli kendi kendine yönetim (ağrı eğitimi, egzersiz, gevşeme, olumsuz düşünceleri yeniden çerçeveleme ve aktif kalma) ya da son ikisinin birlikte uygulanması. 10–12. aylarda ağrının günlük hayata etkisi (8–50 puanlık bir ölçekte) destekli kendi kendine yönetim grubunda tıbbi bakıma göre ortalama 1,7 puan daha düşüktü; ağrının etkisi en az yarı yarıya azalanlar %64'e karşı %55 oldu. Omurga manipülasyonu tek başına tıbbi bakımdan farklı değildi ve kendi kendine yönetime eklendiğinde ek yarar sağlamadı.",
      point="Araştırmacılar ortalama farkın küçük olduğunu belirtiyor. Kendi kendine yönetimin etkisinin yaklaşık %76'sı, katılımcıların 6. aya kadar hareket etmekten daha az korkması, ağrıyla başa çıkabileceğine daha çok güvenmesi ve ağrıyla ilgili olumsuz düşüncelerinin azalmasıyla açıklandı. Sonuçlar katılımcıların kendi bildirimlerine dayanıyor ve katılımcılar hangi yaklaşımı aldıklarını biliyordu. Bulgu, yeni başlayan bel ağrısında yalnızca ilaca değil, hareket etmeye ve ağrıyı anlamaya dayalı bir yaklaşıma da yer verilmesini destekliyor.",
      src=[("JAMA Internal Medicine, Haziran 2026", "https://doi.org/10.1001/jamainternmed.2026.1893"), ("ReachMD, 9 Haziran 2026", "https://reachmd.com/news/pacback-prevention-chronic-back-pain/2487393/"), ("News-Medical, 1 Temmuz 2026", "https://www.news-medical.net/news/20260701/Personalized-self-management-effectively-prevents-chronic-back-pain.aspx")],
      rel=("Bel ağrısı rehberi", "bel-agrisi.html")),
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
