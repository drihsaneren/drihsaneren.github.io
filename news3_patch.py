# -*- coding: utf-8 -*-
"""Tıpta yenilikler: 9 yeni haber, 'Kalp ve metabolizma' grubu, 2 SSS. build_pages.py'yi yerinde yamalar."""
import re
P = "build_pages.py"
s = open(P, encoding="utf-8").read()

def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:90], s.count(a))
    s = s.replace(a, b)

BG = '<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>\n'
BRAIN = ('<path d="M206 70c0-22 16-38 36-38 10 0 18 4 24 10 10 2 18 11 18 22 0 6-2 11-6 15 3 5 4 10 2 16-3 9-12 15-22 14-5 7-13 11-22 10-12-1-22-10-24-22-4-6-6-11-6-17z" fill="none" stroke="#8fa476" stroke-width="2.2"/>'
         '<path d="M232 44c-4 10 2 16 10 18m10-18c6 8 2 18-6 22m-30 6c10-2 16 4 16 12m20 4c8-4 18-2 22 6m-50 8c6 2 10 8 8 16" fill="none" stroke="#8fa476" stroke-width="1.8" stroke-linecap="round"/>')
def hexa(cx, cy, r=9):
    import math
    pts = " ".join(f"{cx + r * math.cos(math.radians(60 * k + 30)):.1f},{cy + r * math.sin(math.radians(60 * k + 30)):.1f}" for k in range(6))
    return f'<polygon points="{pts}" fill="rgba(143,164,118,.25)" stroke="#8fa476" stroke-width="2.5"/>'
def pill(x, y, w, h, rot, cx=None, cy=None):
    r = h / 2
    cx = x + w / 2 if cx is None else cx; cy = y + h / 2 if cy is None else cy
    return (f'<g transform="rotate({rot} {cx} {cy})"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="rgba(236,229,207,.10)" stroke="#ece5cf" stroke-width="2.5"/>'
            f'<path d="M{x + w / 2} {y} H{x + r} A{r} {r} 0 0 0 {x + r} {y + h} H{x + w / 2} Z" fill="#d8b25e"/></g>')

IL = {}
IL["HD"] = BG + (
    '<circle cx="232" cy="84" r="70" fill="rgba(143,164,118,.10)"/>\n'
    f'<g transform="translate(-110 -30) scale(1.4)">{BRAIN}</g>\n'
    '<path d="M64 22 L224 82" stroke="#ece5cf" stroke-width="3" stroke-linecap="round"/>\n'
    '<rect x="44" y="10" width="30" height="16" rx="4" transform="rotate(20 59 18)" fill="#d8b25e"/>\n'
    '<g fill="#e2ab47"><circle cx="230" cy="86" r="4.5"/><circle cx="238" cy="80" r="3.5"/><circle cx="238" cy="92" r="4"/><circle cx="224" cy="94" r="3"/></g>\n'
    '<circle cx="232" cy="87" r="17" fill="none" stroke="#e2ab47" stroke-width="2" stroke-dasharray="4 4"/>\n'
    + hexa(86, 118) + hexa(108, 130) + hexa(84, 144) + hexa(130, 118, 7) + '</svg>')
IL["TAVA"] = BG + (
    '<path d="M112 14C112 58 132 76 160 76C188 76 208 58 208 14" fill="rgba(143,164,118,.16)" stroke="#8fa476" stroke-width="3.5"/>\n'
    '<path d="M86 152Q160 116 234 152" fill="none" stroke="#8fa476" stroke-width="4" stroke-linecap="round"/>\n'
    '<g fill="none" stroke-width="3.5" stroke-linecap="round"><path d="M126 124v7a6 6 0 0 0 12 0v-7" stroke="#e2ab47"/><path d="M154 122v7a6 6 0 0 0 12 0v-7" stroke="rgba(236,229,207,.45)"/><path d="M182 124v7a6 6 0 0 0 12 0v-7" stroke="#e2ab47"/></g>\n'
    '<g fill="#e2ab47"><circle cx="150" cy="96" r="4"/><circle cx="166" cy="102" r="3.5"/><circle cx="158" cy="110" r="3"/><circle cx="176" cy="92" r="3"/><circle cx="142" cy="108" r="3.5"/></g>\n'
    + pill(40, 50, 52, 22, -28) +
    '\n<path d="M96 78Q112 116 128 118" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5" stroke-linecap="round"/>\n'
    '<circle cx="132" cy="128" r="16" fill="none" stroke="#e2ab47" stroke-width="2" stroke-dasharray="4 4"/><circle cx="188" cy="128" r="16" fill="none" stroke="#e2ab47" stroke-width="2" stroke-dasharray="4 4"/></svg>')
IL["OREX"] = BG + (
    '<path d="M110 50a38 38 0 1 0 26 66a30 30 0 1 1 -26 -66z" fill="rgba(143,164,118,.35)" stroke="#8fa476" stroke-width="3"/>\n'
    '<g fill="#ece5cf" opacity=".6"><circle cx="58" cy="44" r="2"/><circle cx="70" cy="132" r="2.5"/><circle cx="46" cy="96" r="1.8"/></g>\n'
    '<circle cx="232" cy="84" r="22" fill="#e2ab47"/>\n'
    '<g stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round"><path d="M232 48v-12M232 120v12M196 84h-12M268 84h12M207 59l-8-8M257 59l8-8M207 109l-8 8M257 109l8 8"/></g>\n'
    '<path d="M130 40Q170 6 204 44" fill="none" stroke="#ece5cf" stroke-width="3" stroke-dasharray="6 6" stroke-linecap="round"/><path d="M194 40l10 5-2 11" fill="none" stroke="#ece5cf" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>\n'
    + pill(136, 132, 56, 24, 0) + '</svg>')
IL["RAS"] = BG + (
    '<g transform="translate(-14 22) scale(.86)"><path d="M50 104c0-26 30-38 60-36 26 2 44-14 72-14 34 0 58 18 58 40 0 24-26 34-52 30-22-4-40 14-72 12-36-2-66-8-66-32z" fill="rgba(143,164,118,.16)" stroke="#8fa476" stroke-width="3.5"/></g>\n'
    '<circle cx="66" cy="112" r="13" fill="#b5483a"/><circle cx="66" cy="112" r="22" fill="none" stroke="#e2ab47" stroke-width="2" stroke-dasharray="4 4"/>\n'
    '<rect x="222" y="52" width="66" height="32" rx="16" fill="rgba(236,229,207,.08)" stroke="#ece5cf" stroke-width="3"/><circle cx="239" cy="68" r="11" fill="#d8b25e"/>\n'
    '<path d="M280 40H246" stroke="#ece5cf" stroke-width="3" stroke-linecap="round"/><path d="M254 34l-8 6 8 6" fill="none" stroke="#ece5cf" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>\n'
    + pill(226, 112, 56, 22, -18) +
    '\n<path d="M218 96C170 124 120 124 90 116" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5" stroke-linecap="round"/></svg>')
IL["MCED"] = BG + (
    '<g transform="rotate(-18 86 96)"><rect x="70" y="30" width="32" height="118" rx="16" fill="rgba(236,229,207,.08)" stroke="#ece5cf" stroke-width="3"/>'
    '<rect x="70" y="88" width="32" height="60" rx="16" fill="#b5483a"/><rect x="70" y="88" width="32" height="14" fill="#b5483a"/><rect x="64" y="24" width="44" height="12" rx="4" fill="#d8b25e"/></g>\n'
    '<circle cx="232" cy="36" r="14" fill="none" stroke="#8fa476" stroke-width="3.5"/>\n'
    '<rect x="202" y="56" width="60" height="100" rx="26" fill="rgba(143,164,118,.14)" stroke="#8fa476" stroke-width="3.5"/>\n'
    '<g fill="#e2ab47"><circle cx="222" cy="82" r="5"/><circle cx="244" cy="88" r="5"/><circle cx="232" cy="110" r="5.5"/><circle cx="220" cy="128" r="4.5"/><circle cx="246" cy="132" r="4.5"/></g>\n'
    '<circle cx="232" cy="110" r="14" fill="none" stroke="#e2ab47" stroke-width="2" stroke-dasharray="4 4"/>\n'
    '<path d="M122 92H190" stroke="#d8b25e" stroke-width="3" stroke-dasharray="4 6" stroke-linecap="round"/><path d="M182 86l8 6-8 6" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>')
IL["LDL"] = BG + (
    '<g fill="none" stroke="#8fa476" stroke-width="4" stroke-linecap="round"><path d="M16 50C80 44 140 56 200 50S280 46 304 52"/><path d="M16 126C80 132 140 120 200 126S280 130 304 124"/></g>\n'
    '<path d="M50 50Q76 82 104 49Z" fill="rgba(226,171,71,.55)" stroke="#e2ab47" stroke-width="2"/><path d="M60 128Q80 104 100 127Z" fill="rgba(226,171,71,.55)" stroke="#e2ab47" stroke-width="2"/>\n'
    '<path d="M214 50Q226 60 238 50Z" fill="rgba(226,171,71,.45)" stroke="#e2ab47" stroke-width="2"/>\n'
    '<g fill="#e2ab47"><circle cx="40" cy="92" r="5"/><circle cx="70" cy="100" r="5"/><circle cx="118" cy="84" r="5"/><circle cx="96" cy="110" r="4.5"/><circle cx="140" cy="100" r="4.5"/><circle cx="252" cy="90" r="4.5"/><circle cx="280" cy="104" r="4"/></g>\n'
    '<path d="M160 88H224" stroke="#ece5cf" stroke-width="3" stroke-dasharray="5 6" stroke-linecap="round" opacity=".8"/><path d="M216 82l8 6-8 6" fill="none" stroke="#ece5cf" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" opacity=".8"/>\n'
    + pill(128, 146, 60, 24, 0) + '</svg>')
IL["BAX"] = BG + (
    '<path d="M84 64c-26 0-40 22-40 46s14 46 40 46c16 0 22-10 18-21-3-8-11-12-11-24s8-16 11-25c4-12-2-22-18-22z" fill="rgba(143,164,118,.25)" stroke="#8fa476" stroke-width="3.5"/>\n'
    '<path d="M62 64L84 34L106 62Z" fill="rgba(226,171,71,.35)" stroke="#e2ab47" stroke-width="3" stroke-linejoin="round"/>\n'
    '<circle cx="86" cy="50" r="24" fill="none" stroke="#ece5cf" stroke-width="3"/><path d="M69 67L103 33" stroke="#ece5cf" stroke-width="3" stroke-linecap="round"/>\n'
    '<g fill="none" stroke-width="10"><path d="M172 124A60 60 0 0 1 202 72" stroke="#8fa476"/><path d="M202 72A60 60 0 0 1 262 72" stroke="#d8b25e"/><path d="M262 72A60 60 0 0 1 292 124" stroke="#b5483a"/></g>\n'
    '<path d="M232 124L196 94" stroke="#ece5cf" stroke-width="4.5" stroke-linecap="round"/><circle cx="232" cy="124" r="8" fill="#ece5cf"/>\n'
    '<path d="M258 56Q226 42 204 64" fill="none" stroke="#ece5cf" stroke-width="2.5" stroke-dasharray="4 5" stroke-linecap="round" opacity=".7"/>\n'
    + pill(126, 128, 50, 22, -20) + '</svg>')
IL["ORFO"] = BG + (
    pill(40, 74, 110, 42, -18) +
    '\n<circle cx="160" cy="46" r="18" fill="none" stroke="#8fa476" stroke-width="3.5"/><path d="M160 36v10l8 5" fill="none" stroke="#8fa476" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>\n'
    '<path d="M204 34V144H296" fill="none" stroke="rgba(236,229,207,.35)" stroke-width="3" stroke-linecap="round"/>\n'
    '<path d="M214 52L234 66L254 88L274 104L292 110" fill="none" stroke="#e2ab47" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>\n'
    '<g fill="#e2ab47"><circle cx="214" cy="52" r="5"/><circle cx="234" cy="66" r="4.5"/><circle cx="254" cy="88" r="4.5"/><circle cx="274" cy="104" r="4.5"/><circle cx="292" cy="110" r="5"/></g>\n'
    '<path d="M214 136H292" stroke="#8fa476" stroke-width="2.5" stroke-dasharray="4 6" stroke-linecap="round"/></svg>')
IL["RETA"] = BG + (
    '<path d="M104 10L138 90L118 170" fill="none" stroke="#8fa476" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>\n'
    '<circle cx="138" cy="90" r="10" fill="#d8b25e"/>\n'
    '<g fill="none" stroke="#b5483a" stroke-width="3" stroke-linecap="round"><path d="M160 72a26 26 0 0 1 0 36" opacity=".8"/><path d="M172 62a40 40 0 0 1 0 56" opacity=".45"/><path d="M184 52a54 54 0 0 1 0 76" opacity=".2"/></g>\n'
    '<rect x="212" y="112" width="84" height="40" rx="10" fill="rgba(236,229,207,.08)" stroke="#ece5cf" stroke-width="3"/>\n'
    '<path d="M238 128a16 16 0 0 1 32 0" fill="none" stroke="#ece5cf" stroke-width="2.5"/><path d="M254 128L246 120" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/>\n'
    '<path d="M254 28V88" stroke="#e2ab47" stroke-width="5" stroke-linecap="round"/><path d="M240 76l14 14 14-14" fill="none" stroke="#e2ab47" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')

IL_CODE = "".join(f"IL_{k} = '''{v}'''\n" for k, v in IL.items())
rep("\nNEWS = [\n", "\n" + IL_CODE + "\nNEWS = [\n")

D = lambda **kw: kw
def item(il, g, cat, date, title, text, point, src, feat=False, rel=None):
    out = f' dict(il=IL_{il}, g="{g}", cat="{cat}", ' + ("feat=True, " if feat else "") + f'date="{date}",\n'
    out += f'      title={title!r},\n      text={text!r},\n      point={point!r},\n'
    out += "      src=[" + ", ".join(f"({t!r}, {u!r})" for t, u in src) + "]"
    if rel:
        out += f",\n      rel=({rel[0]!r}, {rel[1]!r})"
    return out + "),\n"

AMT = item("HD", "beyin", "Huntington", "Eylül 2026",
  "Huntington hastalığında ilk gen tedavisi onay kapısında",
  "Huntington, kalıtsal ve ilerleyici bir beyin hastalığı; hareketi, düşünmeyi ve duygu durumunu etkiliyor ve gidişini yavaşlattığı kanıtlanmış bir tedavisi yok. uniQure'un geliştirdiği AMT-130, MR eşliğinde yapılan tek seferlik bir ameliyatla beynin derinindeki striatum bölgesine veriliyor ve hastalığa yol açan huntingtin proteininin üretimini azaltmayı hedefliyor. Yüksek dozu alan hastalarda 3. yılda hastalığın ilerlemesi, karşılaştırma grubuna göre %80 daha yavaştı; şirket Eylül 2026'da FDA'ya onay başvurusu yaptı.",
  "Sonuçlar az sayıda hastaya ve plasebo grubu yerine hastalık kayıtlarından seçilen benzer hastalarla karşılaştırmaya dayanıyor. 29 Eylül'de açıklanan 4. yıl verilerinde ana ölçekteki fark %44'e indi ve istatistiksel olarak anlamlı değildi; günlük işlev ölçeğinde %61'lik yavaşlama sürüyordu. Yüksek dozu alanların %17'sinde beyinde iltihapla ilişkili ciddi yan etki görüldü, hepsi düzeldi.",
  [("uniQure, 29 Eylül 2026", "https://www.globenewswire.com/news-release/2026/09/29/3370692/0/en/uniqure-announces-additional-data-from-ongoing-phase-i-ii-studies-of-ifezuntirgene-inilparvovec-amt-130-in-huntington-s-disease-showing-continued-slowing-of-disease-progression.html"),
   ("uniQure, Haziran 2026", "https://uniqure.gcs-web.com/news-releases/news-release-details/uniqure-announces-plan-bla-submission-amt-130-huntingtons")])
TAV = item("TAVA", "beyin", "Parkinson", "Eylül 2026",
  "Parkinson'da yeni etki biçimli ilaç: tavapadon",
  "FDA, 28 Eylül 2026'da AbbVie'nin tavapadon (JUVMO) adlı ilacını onayladı. Günde bir kez alınan tablet, beyindeki dopamin reseptörlerinden D1 ve D5'i seçici olarak uyaran ilk ilaç; bugün kullanılan dopamin agonistleri ağırlıklı olarak D2 ve D3 reseptörlerine etki ediyor. Tek başına ya da levodopayla birlikte kullanılabiliyor. Levodopa alan hastalarda, istemsiz hareketler olmadan iyi geçen “açık” süreyi günde 1,7 saat artırdı; plaseboda artış 0,6 saatti.",
  "En sık yan etkiler bulantı, baş ağrısı, tat bozukluğu ve yorgunluk. Yeni ilaçlar hareketi kolaylaştırsa da Parkinson hastalığında düzenli egzersiz tedavinin temel parçası olmaya devam ediyor.",
  [("AbbVie, 28 Eylül 2026", "https://news.abbvie.com/2026-09-28-U-S-FDA-Approves-AbbVies-JUVMO-TM-tavapadon-for-Parkinsons-Disease")],
  rel=("Parkinson rehberi", "parkinson.html"))
OVE = item("OREX", "beyin", "Uyku", "Ağustos 2026",
  "Narkolepside hastalığın kökenine yönelik ilk ilaç",
  "Tip 1 narkolepside beyinde uyanıklığı düzenleyen oreksin (hipokretin) adlı maddeyi üreten hücreler kaybolur; kişi gün içinde karşı konulamaz uyku ataklarıyla boğuşur, güldüğünde ya da heyecanlandığında kasları aniden gevşeyebilir (katapleksi). FDA, 5 Ağustos 2026'da Takeda'nın oveporekston (Orzeyful) adlı ilacını, eksik oreksin sinyalinin yerini tutan ilk ilaç olarak onayladı. 273 hastalık iki çalışmada gündüz uyanıklığı arttı, uykululuk ve katapleksi atakları belirgin şekilde azaldı.",
  "FDA'ya göre hastalığın altta yatan biyolojisini etkileyen ilk ilaç. Günde iki kez alınıyor; en sık yan etkiler uykusuzluk, sık idrara çıkma ve tükürük artışı. 18 yaş altında güvenliği ve etkinliği henüz bilinmiyor.",
  [("FDA, 5 Ağustos 2026", "https://www.fda.gov/news-events/press-announcements/fda-approves-first-drug-treat-full-range-narcolepsy-type-1-symptoms")])
DAR = item("RAS", "gen", "Kanser", "Ağustos 2026",
  "Pankreas kanserinde “hedeflenemez” sanılan RAS'a ilk ilaç",
  "Pankreas kanserlerinin %90'dan fazlasında tümörü büyüten RAS genlerinde (çoğunlukla KRAS) mutasyon bulunuyor. Yıllarca ilaçla hedeflenemez sanılan RAS proteinini engelleyen daraksonrasib (Rasonque), 26 Ağustos 2026'da FDA onayı aldı. Daha önce tedavi görmüş, yayılmış pankreas kanseri olan 500 hastalık RASolute 302 çalışmasında ortanca yaşam süresi kemoterapiyle 6,7 ay, daraksonrasiple 13,2 ay oldu.",
  "Günde bir kez tablet olarak alınıyor. En sık yan etkiler döküntü, ishal, ağız yaraları ve bulantı. Uzmanlar onu pankreas kanserinde onlarca yılın en önemli gelişmesi olarak niteliyor; ilacın tedavinin ilk basamağında kullanıldığı çalışmalar sürüyor.",
  [("FDA, 26 Ağustos 2026", "https://www.fda.gov/news-events/press-announcements/fda-approves-first-class-targeted-therapy-metastatic-pancreatic-cancer"),
   ("STAT", "https://www.statnews.com/2026/08/26/pancreatic-cancer-drug-rasonque-approved/")], feat=True)
ENL = item("LDL", "kalp", "Kolesterol", "Temmuz 2026",
  "Kolesterol için ilk PCSK9 hapı",
  "PCSK9 ilaçları kötü kolesterolü (LDL) güçlü şekilde düşürüyor, ama bugüne kadar yalnızca iğne olarak kullanılabiliyordu. FDA, 17 Temmuz 2026'da Merck'in enlisitid (Lipfendra) adlı ilacını günde bir kez alınan ilk PCSK9 hapı olarak onayladı. Kalp-damar hastalığı olan 3.207 kişilik çalışmada LDL kolesterol 24. haftada plaseboya göre %56, ailesel yüksek kolesterolü olanlarda %59 daha fazla düştü.",
  "Diyet ve egzersize ek olarak kullanılmak üzere onaylandı. Kalp krizi ve inmeyi azaltıp azaltmadığını gösterecek sonuç çalışması henüz tamamlanmadı.",
  [("FDA, 17 Temmuz 2026", "https://www.fda.gov/news-events/press-announcements/fda-approves-first-oral-pcsk9-inhibitor-lower-ldl-cholesterol-adults-high-cholesterol")])
MCED = item("MCED", "tani", "Kanser taraması", "Haziran 2026",
  "Tek kan testiyle birçok kanseri erken yakalamak: ilk büyük sonuçlar",
  "İngiltere'de 50–77 yaş arası, şikâyeti olmayan 142.942 kişinin katıldığı NHS-Galleri çalışmasında katılımcıların yarısına 3 yıl boyunca yılda bir, kanda tümörlerin bıraktığı DNA parçalarını arayan Galleri testi yapıldı. Test grubunda taramayla yakalanan kanser sayısı yaklaşık 4 kat arttı; evre IV (yayılmış) kanser tanıları %14 azaldı, evre I–II tanılar %19 arttı.",
  "Çalışmanın ana hedefi olan evre III–IV kanserlerde anlamlı azalma sağlanamadı. Erken tanının yaşam süresini uzatıp uzatmadığı henüz bilinmiyor. Bu test meme, rahim ağzı ve kolon kanseri taramalarının yerine geçmiyor.",
  [("ASCO, Haziran 2026", "https://www.asco.org/about-asco/press-center/galleri-early-detection-shift-timing-cancer-detection"),
   ("The ASCO Post", "https://ascopost.com/news/june-2026/annual-galleri-screening-reduced-stage-iv-cancer-diagnoses-but-missed-primary-endpoint-in-first-randomized-mced-trial/")])
RETA = item("RETA", "hareket", "Kas-iskelet", "Haziran 2026",
  "Kilo verdiren yeni ilaç diz kireçlenmesi ağrısını da azalttı",
  "Eli Lilly'nin geliştirdiği retatrutid, iştah ve metabolizmayla ilgili üç hormon reseptörünü (GLP-1, GIP ve glukagon) birlikte uyaran, haftada bir yapılan bir iğne. Obezite ve diz kireçlenmesi olan 445 kişilik TRIUMPH-4 çalışmasında en yüksek dozu alanlar 68 haftada vücut ağırlıklarının ortalama %28,7'sini kaybetti; diz ağrısı %75,8 azaldı, plasebo grubunda ise %40,3. Haziran 2026'da açıklanan 2.339 kişilik TRIUMPH-1 çalışmasında da diz kireçlenmesi olan katılımcılarda ağrı %73'e kadar azaldı.",
  "Retatrutid henüz onaylı değil, yalnızca klinik çalışmalarda kullanılıyor; internette satılan “retatrutid” ürünleri yasa dışı ve güvenilmez. Bulantı, ishal ve kusma sık görüldü; en yüksek dozda hastaların yaklaşık %18'i yan etki nedeniyle ilacı bıraktı. Diz kireçlenmesinde kilo vermeyi güçlendirme egzersizleriyle birleştirmek önemini koruyor.",
  [("Eli Lilly, 11 Aralık 2025", "https://investor.lilly.com/news-releases/news-release-details/lillys-triple-agonist-retatrutide-delivered-weight-loss-average"),
   ("Eli Lilly, 6 Haziran 2026", "https://investor.lilly.com/news-releases/news-release-details/lillys-triple-agonist-retatrutide-drove-substantial-improvements")],
  rel=("Diz kireçlenmesi rehberi", "diz-kireclenmesi.html"))
BAX = item("BAX", "kalp", "Tansiyon", "Mayıs 2026",
  "Zor kontrol edilen tansiyonda yeni ilaç sınıfı",
  "Birden fazla ilaca rağmen tansiyonu yüksek kalan hastalarda, vücutta tuz ve su tutulmasına yol açan aldosteron hormonu önemli bir etken. AstraZeneca'nın baksdrostat (Baxfendy) adlı ilacı, böbrek üstü bezinde aldosteron üretimini engelleyen ilk ilaç olarak Mayıs 2026'da FDA onayı aldı. En az iki tansiyon ilacı kullanan 796 hastalık BaxHTN çalışmasında büyük tansiyon 12 haftada plaseboya göre 8,7–9,8 mmHg daha fazla düştü.",
  "Başlıca dikkat edilmesi gereken yan etki kanda potasyum yükselmesi (yüksek dozda %3). Tansiyon ilacınızı hekiminize danışmadan değiştirmeyin. İlaçların yanında düzenli egzersizin, özellikle izometrik egzersizlerin de tansiyonu düşürdüğü gösterildi.",
  [("New England Journal of Medicine, 2025", "https://www.nejm.org/doi/full/10.1056/NEJMoa2507109"),
   ("Pharmacy Times, Mayıs 2026", "https://www.pharmacytimes.com/view/fda-approves-baxdrostat-as-first-in-class-aldosterone-synthase-inhibitor-for-hypertension")],
  rel=("Tansiyon için duvar oturuşu", "duvar-oturusu.html"))
ORFO = item("ORFO", "kalp", "Obezite", "Nisan 2026",
  "Zayıflama iğnesinin kuralsız hapı",
  "GLP-1 ilaçları şimdiye kadar çoğunlukla haftalık iğne olarak kullanılıyordu; Aralık 2025'te onaylanan ağızdan semaglutidin (Wegovy hap) ise aç karnına alınması gerekiyor. FDA, 1 Nisan 2026'da Eli Lilly'nin orforglipron (Foundayo) adlı hapını, günün herhangi bir saatinde yemek ve su kısıtlaması olmadan alınabilen ilk GLP-1 hapı olarak onayladı. 72 haftalık ATTAIN-1 çalışmasında en yüksek dozu alanlar vücut ağırlıklarının ortalama %12,4'ünü kaybetti; plaseboda kayıp %0,9'du.",
  "Azaltılmış kalorili beslenme ve daha fazla hareketle birlikte kullanılmak üzere onaylandı. Bulantı, kabızlık ve ishal sık; tiroid tümörü riski, pankreatit ve safra kesesi sorunlarıyla ilgili uyarılar bu ilaç için de geçerli. Kilo verirken kas kaybını azaltmak için güçlendirme egzersizleri önemli.",
  [("Eli Lilly, 1 Nisan 2026", "https://investor.lilly.com/news-releases/news-release-details/fda-approves-lillys-foundayotm-orforglipron-only-glp-1-pill")],
  rel=("Ne kadar hareket yeterli?", "hareket.html"))

rep(" dict(il=IL_VACCINE,", AMT + TAV + OVE + DAR + " dict(il=IL_VACCINE,")
rep(" dict(il=IL_CART,", ENL + " dict(il=IL_CART,")
rep(" dict(il=IL_FORK,", MCED + RETA + BAX + ORFO + " dict(il=IL_FORK,")

rep('GROUPS = [("tum", "Tümü"), ("beyin", "Beyin ve sinirler"), ("hareket", "Hareket ve ağrı"), ("gen", "Gen ve hücre tedavileri"), ("tani", "Tanı ve teknoloji")]',
    'GROUPS = [("tum", "Tümü"), ("beyin", "Beyin ve sinirler"), ("hareket", "Hareket ve ağrı"), ("kalp", "Kalp ve metabolizma"), ("gen", "Gen ve hücre tedavileri"), ("tani", "Tanı ve teknoloji")]')
rep('chip = {"Alzheimer": "chip", "Parkinson": "chip", "Nöroteknoloji": "chip",',
    'chip = {"Alzheimer": "chip", "Parkinson": "chip", "Huntington": "chip", "Uyku": "chip", "Nöroteknoloji": "chip",')

FAQ_NEW = (' ("Zayıflama ilaçları artık hap olarak da var mı?", "Evet. ABD\'de Aralık 2025\'te ağızdan semaglutid (Wegovy hap), Nisan 2026\'da da yemek ve su kısıtlaması olmadan alınabilen orforglipron (Foundayo) onaylandı. 72 haftalık çalışmada orforglipronun en yüksek dozuyla ortalama kilo kaybı %12,4 oldu. Bu ilaçlar beslenme düzeni ve hareketle birlikte, hekim kontrolünde kullanılır."),\n'
           ' ("Kanseri kandan erken yakalayan testler kullanıma hazır mı?", "Henüz değil. 142.942 kişilik NHS-Galleri çalışmasında test, taramayla yakalanan kanser sayısını yaklaşık 4 kat artırdı ve evre IV tanıları %14 azalttı; ancak evre III–IV kanserlerde hedeflenen azalma sağlanamadı ve yaşam süresine etkisi henüz bilinmiyor. Bu testler mevcut tarama programlarının yerine geçmez."),\n')
rep(' ("Parkinson hastalığında kök hücre tedavisi var mı?",', FAQ_NEW + ' ("Parkinson hastalığında kök hücre tedavisi var mı?",')

rep('<p class="lede">Tıbbın öncü alanlarındaki önemli gelişmelerin kısa ve anlaşılır özetleri. Her haberin altında kaynağı var.</p>\n    <p class="meta">Son güncelleme: 29 Eylül 2026</p>',
    '<p class="lede">Tıbbın öncü alanlarındaki önemli gelişmelerin kısa ve anlaşılır özetleri. Her haberin altında kaynağı var.</p>\n    <p class="meta">Son güncelleme: 30 Eylül 2026</p>')
rep('"Alzheimer kan testleri, Parkinson\'da kök hücre nakli, mRNA kanser aşısı, beyin-bilgisayar arayüzü, domuz böbreği nakli, mamografide yapay zekâ ve daha fazlası: kısa, kaynaklı özetler."',
    '"Huntington gen tedavisi, pankreas kanserinde yeni ilaç, zayıflama hapları, Alzheimer kan testleri, Parkinson\'da kök hücre nakli, mRNA kanser aşısı ve daha fazlası: kısa, kaynaklı özetler."')
rep('cond("Tip 1 diyabet"), cond("Amiyotrofik lateral skleroz (ALS)")]',
    'cond("Tip 1 diyabet"), cond("Amiyotrofik lateral skleroz (ALS)"), cond("Huntington hastalığı"), cond("Narkolepsi"), cond("Pankreas kanseri"), cond("Yüksek tansiyon (hipertansiyon)"), cond("Yüksek kolesterol"), cond("Obezite")]')
open(P, "w", encoding="utf-8").write(s)
print("ok")
