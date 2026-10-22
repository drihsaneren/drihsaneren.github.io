# -*- coding: utf-8 -*-
"""Yeni sayfaları ve haberleri build_pages.py / i18n_map.py'ye kaydeder (22 Ekim 2026 turu).
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


# ------------------------------------------------------------------ sayfalar
CONDS = [
    # dosya, en, part, kategori, başlık, hap, C_, TH, kısa açıklama, bölge (None = REHAB), (AGR'de/REHAB'da kimden sonra)
    ("periferik-arter-hastaligi.html", "peripheral-arterial-disease.html", "cond61_part.py", "Rehabilitasyon rehberi",
     "Periferik arter hastalığı ve yürüyüş egzersizi", "Periferik arter hastalığı", "C_PAD",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 136 H260" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><circle cx="118" cy="30" r="11" fill="#8fa476"/><path d="M118 44 L114 84 L98 108 L92 132 M114 84 L132 106 L144 130 M116 54 L100 74 M116 54 L136 66" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M134 108 C138 116 140 122 142 128" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/><path d="M196 42 C214 42 222 54 230 54 C238 54 246 42 264 42 M196 74 C214 74 222 62 230 62 C238 62 246 74 264 74" fill="none" stroke="#d8b25e" stroke-width="4" stroke-linecap="round"/><path d="M200 58 H222 M238 58 H260" stroke="rgba(181,72,58,.8)" stroke-width="4" stroke-linecap="round"/><path d="M206 104 V126 M218 104 V126" stroke="#ece5cf" stroke-width="5" stroke-linecap="round" opacity=".7"/></svg>""",
     "Yürürken baldırda kramp gibi ağrı, birkaç dakika durunca geçiyor mu? Ağrıya kadar yürüyüp dinlenerek yürüme mesafenizi uzatan program ve uyarı işaretleri.",
     None, "C_CARDIAC"),
    ("beyin-sarsintisi.html", "concussion.html", "cond62_part.py", "Hastalık rehberi",
     "Beyin sarsıntısı (konküzyon)", "Beyin sarsıntısı", "C_CONC",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M134 128 C120 128 112 116 112 100 V86 C98 84 96 76 104 70 L112 62 C112 34 136 18 162 18 C192 18 212 40 212 68 C212 92 200 104 192 112 V128" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M150 52 C158 44 172 44 178 54 C186 50 196 58 192 68 C198 74 192 86 182 84 C178 92 164 92 160 84 C150 88 140 80 146 70 C138 64 142 54 150 52 Z" fill="#d8b25e" opacity=".85"/><g fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"><path d="M226 40 l12 -8 M230 60 h14 M226 80 l12 8"/></g><path d="M234 126 h10 v-10 h10 v-10 h10 v-10" fill="none" stroke="#ece5cf" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" opacity=".7"/></svg>""",
     "Kafa darbesinden sonra baş ağrısı, sersemlik, baş dönmesi? Acil belirtiler, ilk 48 saat ve okula, işe, spora altı aşamada kademeli dönüş.",
     "boyun", "C_VERTIGO"),
    ("pelvik-organ-sarkmasi.html", "pelvic-organ-prolapse.html", "cond63_part.py", "Hastalık rehberi",
     "Pelvik organ sarkması (rahim sarkması)", "Rahim sarkması", "C_POP",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M104 36 C96 84 124 120 160 120 C196 120 224 84 216 36" fill="none" stroke="#8fa476" stroke-width="8" stroke-linecap="round"/><path d="M122 104 C140 116 180 116 198 104" fill="none" stroke="#d8b25e" stroke-width="6" stroke-linecap="round"/><ellipse cx="160" cy="80" rx="20" ry="16" fill="#e2ab47" opacity=".8"/><path d="M160 136 V126 M152 132 l8 -8 l8 8" fill="none" stroke="#ece5cf" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M236 52 c10 -12 24 -12 34 0 M240 62 c8 -8 18 -8 26 0" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" opacity=".6"/></svg>""",
     "Haznede ağırlık ya da aşağı inme hissi mi var? Rahim, mesane ve bağırsak sarkması: pelvik taban egzersizleri, pesser ve günlük öneriler.",
     "kadin", "C_UI"),
]
SELFS = [
    # dosya, en, part, başlık, hap, C_, TH, açıklama, SELF'te kimden sonra, SELF_GROUPS grubu, grupta kimden sonra
    ("guc-devresi.html", "home-strength-circuit.html", "self12_part.py", "Evde güç devresi", "Güç devresi", "C_GD",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 136 H260" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M90 136 V98 H132 V136 M90 98 V56" stroke="#8a6a44" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="148" cy="38" r="11" fill="#8fa476"/><path d="M146 52 L138 86 L156 108 L152 134 M138 86 L122 100 M144 62 L166 78 M144 62 L164 58" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="226" cy="74" r="30" fill="none" stroke="rgba(236,229,207,.25)" stroke-width="6"/><path d="M226 44 A30 30 0 1 1 196 74" fill="none" stroke="#e2ab47" stroke-width="6" stroke-linecap="round"/><path d="M226 74 V58 M226 74 L238 80" stroke="#ece5cf" stroke-width="3.5" stroke-linecap="round"/></svg>""",
     "Haftada 2 gün kas güçlendirme: 4 ya da 6 hareketlik ev devresi, sesli çalışma-dinlenme zamanlayıcısı ve haftalık takip.",
     "C_SNACK", "Zamanlayıcıyla birlikte yapın", "hareket-atistirmaliklari.html"),
    ("iki-dakika-adim-testi.html", "two-minute-step-test.html", "self12_part.py", "2 dakika adım testi", "2 dakika adım testi", "C_AD",
     """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 136 H260" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M96 20 V136" stroke="rgba(236,229,207,.35)" stroke-width="5" stroke-linecap="round"/><path d="M96 84 H188" stroke="#e2ab47" stroke-width="3" stroke-dasharray="6 6" stroke-linecap="round"/><circle cx="150" cy="26" r="11" fill="#8fa476"/><path d="M150 40 V84 M150 84 L148 110 L150 134 M150 84 L176 84 L172 110 M148 50 L132 70 M150 50 L168 64" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><rect x="208" y="44" width="56" height="70" rx="9" fill="none" stroke="rgba(236,229,207,.35)" stroke-width="4"/><text x="236" y="86" text-anchor="middle" font-family="Georgia,serif" font-size="20" fill="#ece5cf">2:00</text></svg>""",
     "2 dakika yerinde adım atarak kondisyonunuzu ölçün: adım sayacı, yaşa ve cinsiyete göre değerler ve bağımsızlık eşiği.",
     "C_YH", "Kendinizi ölçün", "yurume-hizi-testi.html"),
]
RELATED_NEW = {
    "periferik-arter-hastaligi.html": ["kalp-rehabilitasyonu.html", "dar-kanal.html", "tempolu-yuruyus.html"],
    "beyin-sarsintisi.html": ["boyun-incinmesi.html", "bas-agrisi.html", "bas-donmesi.html"],
    "pelvik-organ-sarkmasi.html": ["idrar-kacirma.html", "pelvik-taban-zamanlayicisi.html", "karin-kasi-ayrilmasi.html"],
    "guc-devresi.html": ["sandalye-testi.html", "hareket-atistirmaliklari.html", "sarkopeni.html"],
    "iki-dakika-adim-testi.html": ["sandalye-testi.html", "yurume-hizi-testi.html", "tempolu-yuruyus.html"],
}
RELATED_ADD = [  # (var olan sayfa, eklenecek)
    ("kalp-rehabilitasyonu.html", "periferik-arter-hastaligi.html"),
    ("gece-bacak-kramplari.html", "periferik-arter-hastaligi.html"),
    ("boyun-incinmesi.html", "beyin-sarsintisi.html"),
    ("idrar-kacirma.html", "pelvik-organ-sarkmasi.html"),
    ("pelvik-taban-zamanlayicisi.html", "pelvik-organ-sarkmasi.html"),
    ("sandalye-testi.html", "guc-devresi.html"),
    ("yurume-hizi-testi.html", "iki-dakika-adim-testi.html"),
]

# exec listesi
# cond61, sn_stair çizimi self4_part.py'de tanımlandığı için self12_part.py'den SONRA exec edilir.
for part, after in (("self12_part.py", "self11_part.py"), ("cond61_part.py", "self12_part.py"), ("cond62_part.py", "cond61_part.py"), ("cond63_part.py", "cond62_part.py")):
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

# ------------------------------------------------------------------ Bilim gündemi (yen11)
s = open(B, encoding="utf-8").read()
IL_NEW = {
"IL_ACLX": '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M40 156 H280" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<path d="M118 22 C112 54 116 74 130 90 M130 90 C146 108 146 128 136 156" fill="none" stroke="#8fa476" stroke-width="16" stroke-linecap="round"/>
<ellipse cx="134" cy="92" rx="15" ry="11" fill="#d8b25e"/>
<path d="M120 84 L148 102" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" stroke-dasharray="3 4"/>
<rect x="196" y="58" width="16" height="64" rx="6" fill="rgba(236,229,207,.25)"/><rect x="220" y="40" width="16" height="82" rx="6" fill="#8fa476"/>
<path d="M188 122 H246" stroke="rgba(236,229,207,.35)" stroke-width="2"/></svg>''',
"IL_HIPOA": '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M58 40 C82 30 118 34 132 54" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/>
<circle cx="120" cy="74" r="20" fill="#d8b25e"/>
<path d="M120 94 L104 156" stroke="#8fa476" stroke-width="16" stroke-linecap="round"/>
<path d="M40 156 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<path d="M190 40 V150 H290" fill="none" stroke="rgba(236,229,207,.3)" stroke-width="2"/>
<rect x="208" y="118" width="24" height="32" rx="5" fill="#e2ab47"/>
<path d="M196 94 H286" stroke="rgba(236,229,207,.6)" stroke-width="2" stroke-dasharray="5 5"/>
<g font-family="Georgia,serif" font-size="12" fill="#ece5cf" text-anchor="middle"><text x="220" y="112">7</text><text x="268" y="88">12</text></g></svg>''',
"IL_FAST4": '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 156 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<g fill="none" stroke="#8fa476" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">
<circle cx="56" cy="74" r="8" fill="#8fa476" stroke="none"/><path d="M56 84 L54 112 L46 138 M54 112 L64 138 M56 92 L74 98"/>
<circle cx="124" cy="62" r="8" fill="#8fa476" stroke="none"/><path d="M122 72 L116 100 L130 116 L128 138 M116 100 L104 110 M120 80 L138 90"/>
<circle cx="188" cy="64" r="8" fill="#8fa476" stroke="none"/><path d="M188 74 V108 L184 138 M188 108 L194 138 M188 84 L172 92 M188 84 L204 92"/>
<circle cx="252" cy="62" r="8" fill="#8fa476" stroke="none"/><path d="M252 72 L250 106 L262 118 L262 138 M250 106 L240 138 M250 82 L236 98 M250 82 L266 94"/></g>
<path d="M232 138 H276 V124 H262" fill="none" stroke="#d8b25e" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M76 98 C90 96 100 90 104 84" fill="none" stroke="#e2ab47" stroke-width="2.5" stroke-dasharray="3 4"/>
<circle cx="160" cy="28" r="14" fill="none" stroke="#e2ab47" stroke-width="3"/><path d="M160 28 V20 M160 28 L166 32" stroke="#ece5cf" stroke-width="2.5" stroke-linecap="round"/></svg>''',
}
NEWS_ADD = [
("IL_ISOWEEK", ''' dict(il=IL_ACLX, g="hareket", cat="Diz", date="Eylül 2026",
      title="Ön çapraz bağ ameliyatından sonra süren diz yakınmalarında gözetimli egzersiz güvenli, yararı ılımlı",
      text="Avustralya'da La Trobe Üniversitesi'nin yürüttüğü ve 29 Eylül 2026'da Annals of Internal Medicine'de yayımlanan SUPER-Knee çalışmasına, ön çapraz bağ ameliyatından 9–36 ay sonra hâlâ diz yakınmaları olan 18–40 yaş arası 184 kişi katıldı. Yarısı 4 ay boyunca fizyoterapist gözetiminde ilerleyici egzersiz ve eğitim aldı; diğer yarısı tek bir eğitim seansı ve kendi başına egzersiz için kaynaklar. 4. ayda diz yakınma ve işlev puanı (KOOS4, 0–100) gözetimli grupta 14,1, diğer grupta 9,4 puan iyileşti; aradaki fark 4,8 puandı. Ağrıda anlamlı düzelme bildirenler %73'e karşı %40'tı ve uyluk kas gücü gözetimli grupta daha çok arttı. MR'da kıkırdak kalınlığı ve yapısında iki grup arasında 4. ve 12. ayda fark görülmedi.",
      point="Aradaki fark ılımlı ve 12. ayda, kontrol grubu da iyileşmeye devam ettiği için daraldı. Çalışma körlenmemişti; katılımcılar hangi grupta olduklarını biliyordu ve sonuçların çoğu kendi bildirimlerine dayanıyor. Ön çapraz bağ ameliyatı olan genç yetişkinler erken diz kireçlenmesi açısından risk altında; bu çalışmada yoğun egzersizin kıkırdağa zarar verdiğine dair bir işaret görülmedi.",
      src=[("Annals of Internal Medicine, 29 Eylül 2026", "https://doi.org/10.7326/ANNALS-26-02460"), ("News-Medical, 29 Eylül 2026", "https://news-medical.net/news/20260929/Exercise-therapy-reduces-knee-osteoarthritis-risk-after-ACL-surgery.aspx"), ("Medical Dialogues, 5 Ekim 2026", "https://medicaldialogues.in/orthopaedics/news/supervised-physical-therapy-provides-greater-pain-relief-after-acl-surgery-jama-180518")],
      rel=("Ön çapraz bağ rehberi", "on-capraz-bag.html")),
'''),
("IL_PARK", ''' dict(il=IL_HIPOA, g="hareket", cat="Kireçlenme", date="Temmuz 2026",
      title="Kalça kireçlenmesinde egzersizin ortalama etkisi beklenenden küçük: Cochrane güncellemesi",
      text="Sidney ve Melbourne üniversitelerinden araştırmacıların 23 Temmuz 2026'da yayımladığı Cochrane derlemesi, kalça kireçlenmesi olan 1.368 kişiyle yapılmış 18 çalışmayı inceledi; programlar 2 ile 52 hafta sürdü ve güçlendirme, aerobik ve beden-zihin egzersizlerini kapsıyordu. Hiç tedavi almama, olağan bakım ya da yalnızca bilgilendirmeyle karşılaştırıldığında egzersiz ağrıyı 100 puanlık ölçekte ortalama 7,2, işlevi 8,8 puan iyileştirdi; oysa kişinin günlük hayatta fark etmesi için genellikle 12–13 puanlık bir iyileşme gerektiği kabul ediliyor. Sahte tedaviyle karşılaştırıldığında ağrıda etki çok az ya da hiç yoktu; başka bir tedaviye eklenen egzersiz de ağrı ve işlevi belirgin değiştirmedi. Yaşam kalitesinde de anlamlı bir iyileşme görülmedi.",
      point="Bu, egzersizin işe yaramadığı anlamına gelmiyor: Yazarlar egzersizin kalça kireçlenmesinde temel tedavi olarak önerilmeye devam etmesi gerektiğini, ucuz ve zararının az olduğunu vurguluyor. Ancak hastalara beklentilerin gerçekçi anlatılması ve kimin hangi egzersizden yarar gördüğünü gösterecek daha büyük çalışmalar gerektiğini söylüyorlar. Çalışmaların çoğu küçüktü, katılımcılar hangi grupta olduklarını biliyordu ve katılımcıların %63'ü kadın, yaşları 53 ile 74 arasındaydı.",
      src=[("Cochrane Library, 23 Temmuz 2026", "https://doi.org/10.1002/14651858.CD007912.pub3"), ("Cochrane sade dil özeti", "https://www.cochrane.org/evidence/CD007912_exercise-osteoarthritis-hip"), ("Sidney Üniversitesi, 23 Temmuz 2026", "https://www.sydney.edu.au/news-opinion/news/2026/07/23/exercise-benefit-for-hip-arthritis-pain-may-be-more-modest-than-expected.html")],
      rel=("Kalça kireçlenmesi rehberi", "kalca-kireclenmesi.html")),
'''),
("IL_CART", ''' dict(il=IL_FAST4, g="hareket", cat="Kas gücü", date="Haziran 2026",
      title="65 yaş üstünde günde 4 dakikalık güç egzersizi bacak gücünü ve dengeyi artırdı",
      text="ABD'de Penn State Tıp Fakültesi'nden araştırmacıların 2026'da PLOS One'da yayımladığı FAST-2 çalışmasında, haftada ortalama yalnızca 18 dakika egzersiz yapan, yaş ortalaması 74 olan 97 kişi rastgele iki gruba ayrıldı. Egzersiz grubu her gün yaklaşık 4 dakika süren bir program yaptı: şınav, sandalyeden kalkma, lastik bantla kürek çekme ve basamak çıkma; her hareket 30 saniye, ardından 30 saniye dinlenme. Katılımcılara lastik bantlar ve yüksekliği ayarlanabilen bir basamak verildi, hareketler güç arttıkça zorlaştırıldı. Egzersiz yapmayan gruba göre 30 saniyede sandalyeden kalkma sayısı 4,2 tekrar, tek ayak üstünde durma süresi 3,6 saniye arttı; oturup kalkma 2,3 saniye hızlandı. Katılımcılar programı günlerin %81'inde yaptı.",
      point="Haberlerde grupların başlangıç ve son değerleri ile güven aralıkları yer almıyor; bazı başlıklardaki “zindeliği dört katına çıkardı” ifadesi de verilen sayılarla desteklenmiyor. Yine de sonuç, kısa ama her gün yapılan güçlendirmenin yaşlılarda işe yarayabileceğini gösteren randomize bir kanıt. Benzer bir devreyi evde yapmak için Kendine iyi bak bölümündeki güç devresini kullanabilirsiniz.",
      src=[("PLOS One, 2026", "https://doi.org/10.1371/journal.pone.0336748"), ("Penn State, 9 Haziran 2026", "https://www.psu.edu/news/research/story/four-minute-daily-workout-improves-strength-balance-older-adults"), ("Penn State Health News, 12 Haziran 2026", "https://pennstatehealthnews.org/2026/06/four-minutes-of-daily-resistance-training-can-quadruple-fitness-in-older-adults/")],
      rel=("Evde güç devresi", "guc-devresi.html")),
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
