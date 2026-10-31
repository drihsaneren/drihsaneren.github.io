# -*- coding: utf-8 -*-
# Boyun ağrısı + boyun fıtığı sayfaları. build_pages.py içinden exec ile çalışır
# (fig, vbox, A, BACK, UPDATED, WA, OMUZ_CSS, YT_JS, page tanımlı olmalı).

GRD = '<line class="grd" x1="6" y1="112" x2="114" y2="112"/>'
LEGS_F = 'M60 80 L52 112 M60 80 L68 112'
SPL = 'calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"'

def anim_t(values, dur="3.2s", kt="0;0.5;1", typ="translate"):
    n = len(values.split(";")) - 1
    ks = ";".join(["0.45 0 0.55 1"] * n)
    return (f'<animateTransform attributeName="transform" type="{typ}" values="{values}" dur="{dur}" '
            f'keyTimes="{kt}" repeatCount="indefinite" calcMode="spline" keySplines="{ks}"/>')

def anim_d(values, dur="3.2s", kt="0;0.5;1"):
    n = len(values.split(";")) - 1
    ks = ";".join(["0.45 0 0.55 1"] * n)
    return (f'<animate attributeName="d" values="{values}" dur="{dur}" keyTimes="{kt}" '
            f'repeatCount="indefinite" calcMode="spline" keySplines="{ks}"/>')

FACE_SIDE = '<circle class="hd" cx="62" cy="22" r="8"/><path d="M69 20 L74 23 L69 25 Z" fill="#2A6F6B"/><circle cx="65" cy="20" r="1.4" fill="#efe9d6"/>'

SV = {}
# 1 · Çene içe çekme (yandan)
SV["chin"] = fig(GRD +
    '<path d="M34 22 H94" stroke="#B9CBC6" stroke-width="2" stroke-dasharray="3 4" fill="none"/>'
    '<path class="fig" d="M58 40 V80 M58 80 L54 112 M58 80 L62 112 M58 44 L60 66 L67 75"/>'
    f'<path class="fig hl" d="M58 40 L62 30">{anim_d("M58 40 L62 30;M58 40 L56 30;M58 40 L62 30")}</path>'
    f'<g>{anim_t("0 0;-6 0;0 0")}{FACE_SIDE}</g>'
    '<path d="M40 10 H30 M34 6 L30 10 L34 14" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    "Çene içe çekme")

# 2 · Boyun döndürme (önden)
SV["rot"] = fig(GRD +
    f'<path class="fig" d="M44 40 H76 M60 40 V80 {LEGS_F} M44 40 L40 62 L42 78 M76 40 L80 62 L78 78 M60 32 V40"/>'
    '<circle class="hd" cx="60" cy="22" r="10"/>'
    f'<g>{anim_t("0 0;-5 0;0 0;5 0;0 0", dur="4.8s", kt="0;0.25;0.5;0.75;1")}'
    '<circle cx="56" cy="20" r="1.6" fill="#efe9d6"/><circle cx="64" cy="20" r="1.6" fill="#efe9d6"/>'
    '<path d="M60 22 V26" stroke="#efe9d6" stroke-width="2" stroke-linecap="round"/></g>'
    '<path d="M42 8 Q60 1 78 8 M46 5 L42 8 L46 11 M74 5 L78 8 L74 11" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    "Boyun döndürme")

# 3 · Yana germe (önden)
SV["side"] = fig(GRD +
    f'<path class="fig" d="M44 40 H76 M60 40 V80 {LEGS_F} M44 40 L40 64 L42 80 M76 40 L80 62 L78 78"/>'
    f'<path class="band" d="M45 40 Q50 32 56 28">{anim_d("M45 40 Q50 32 56 28;M45 40 Q52 31 61 27;M45 40 Q50 32 56 28")}</path>'
    f'<g>{anim_t("0 60 40;22 60 40;0 60 40", typ="rotate")}'
    '<path class="fig hl" d="M60 40 V30"/><circle class="hd" cx="60" cy="21" r="8"/></g>',
    "Yana germe")

# 4 · Kürek kemiği sıkıştırma (arkadan)
SV["scap"] = fig(GRD +
    f'<path class="fig" d="M40 40 H80 M60 32 V80 {LEGS_F} M40 40 L36 62 L38 78 M80 40 L84 62 L82 78"/>'
    '<circle class="hd" cx="60" cy="22" r="8"/>'
    f'<g>{anim_t("0 0;3 0;0 0")}<path d="M42 45 L55 45 L50 64 Z" fill="#C8963E" stroke="#C8963E" stroke-width="2" stroke-linejoin="round"/></g>'
    f'<g>{anim_t("0 0;-3 0;0 0")}<path d="M78 45 L65 45 L70 64 Z" fill="#C8963E" stroke="#C8963E" stroke-width="2" stroke-linejoin="round"/></g>',
    "Kürek kemiği sıkıştırma")

# 5 · İzometrik güçlendirme (yandan)
SV["iso"] = fig(GRD +
    '<path class="fig" d="M58 40 V80 M58 80 L54 112 M58 80 L62 112 M58 40 L62 30"/>'
    + FACE_SIDE +
    '<path class="fig hl" d="M58 44 L74 40 L76 22"/><rect x="73" y="10" width="7" height="15" rx="3" fill="#C8963E"/>'
    '<g fill="none" stroke="#C8963E" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M86 14 L90 18 L86 22"><animate attributeName="opacity" values="0;1;0" dur="1.6s" repeatCount="indefinite"/></path>'
    '<path d="M92 14 L96 18 L92 22"><animate attributeName="opacity" values="0;1;0" dur="1.6s" begin="0.4s" repeatCount="indefinite"/></path></g>',
    "İzometrik güçlendirme")

# 6 · Göğüs kafesini açma (sandalyede, yandan)
SV["thor"] = fig(GRD +
    '<path class="obj" d="M38 84 H76 M40 84 V112 M74 84 V112 M38 84 V62"/>'
    '<path class="fig" d="M46 82 H80 V112 M46 82 L44 64"/>'
    f'<g>{anim_t("0 44 64;-24 44 64;0 44 64", typ="rotate")}'
    '<path class="fig hl" d="M44 64 L44 42"/><path class="fig" d="M44 46 L56 40 L50 28"/><circle class="hd" cx="46" cy="32" r="8"/></g>',
    "Göğüs kafesini açma")

# 7 · Sinir kaydırma (önden)
# Kişi bize dönük: kişinin sağı = görüntünün solu.
# Baş sağa eğilirken sağ dirsek 90°→180° açılır; baş sola eğilirken sol dirsek açılır.
GL_DUR, GL_KT = "4.8s", "0;0.25;0.5;0.75;1"
SV["glide"] = fig(GRD +
    f'<path class="fig" d="M44 40 H76 M60 40 V80 {LEGS_F} M44 40 H26 M76 40 H94"/>'
    f'<g>{anim_t("0 26 40;-90 26 40;0 26 40;0 26 40;0 26 40", dur=GL_DUR, kt=GL_KT, typ="rotate")}'
    '<path class="fig hl" d="M26 40 V21"/><circle cx="26" cy="18" r="3.5" fill="#C8963E"/></g>'
    f'<g>{anim_t("0 94 40;0 94 40;0 94 40;90 94 40;0 94 40", dur=GL_DUR, kt=GL_KT, typ="rotate")}'
    '<path class="fig hl" d="M94 40 V21"/><circle cx="94" cy="18" r="3.5" fill="#C8963E"/></g>'
    f'<g>{anim_t("0 60 40;-22 60 40;0 60 40;22 60 40;0 60 40", dur=GL_DUR, kt=GL_KT, typ="rotate")}'
    '<path class="fig" d="M60 40 V30"/><circle class="hd" cx="60" cy="21" r="8"/></g>',
    "Sinir kaydırma")

# 8 · Rahatlama pozisyonu (önden)
SV["relief"] = fig(GRD +
    f'<path class="fig" d="M44 40 H76 M60 40 V80 {LEGS_F} M76 40 L80 64 L78 80 M60 30 V40"/>'
    '<circle class="hd" cx="60" cy="22" r="8"/>'
    f'<path class="fig hl" d="M44 40 L38 64 L40 80">{anim_d("M44 40 L38 64 L40 80;M44 40 L30 24 L50 12;M44 40 L30 24 L50 12;M44 40 L38 64 L40 80", dur="5s", kt="0;0.35;0.75;1")}</path>',
    "Elini başa koyma")

def ex_card(key, title, text, dose):
    return f'<article class="exc">{SV[key]}<div class="body"><h3>{title}</h3><p>{text}</p><span class="dose">{dose}</span></div></article>'

EXT = {
 "chin": ("Çene içe çekme", "Dik oturun, gözleriniz karşıya baksın. Başınızı eğmeden çenenizi düz bir çizgide geriye çekin, çift çene yapar gibi. Ensenizin uzadığını hissedin, 5 saniye tutup bırakın.", "10 tekrar, günde 2–3 kez"),
 "rot": ("Boyun döndürme", "Omuzlarınızı sabit tutun. Başınızı yavaşça sağa çevirin, rahat olan son noktada 2–3 saniye bekleyin, sonra aynı şekilde sola çevirin.", "Her yöne 10 tekrar"),
 "side": ("Yana germe", "Sağ elinizle oturduğunuz sandalyenin kenarını tutun. Sol kulağınızı sol omzunuza doğru yaklaştırın. Boynunuzun sağ yanında hafif bir gerginlik hissedeceksiniz. Omzunuzu kaldırmayın.", "20–30 saniye tutun, her iki yana 3 kez"),
 "scap": ("Kürek kemiği sıkıştırma", "Dik durun ya da oturun. Omuzlarınızı kulaklarınıza kaldırmadan, kürek kemiklerinizi geriye ve biraz aşağıya doğru birbirine yaklaştırın. 5 saniye tutup bırakın.", "10–15 tekrar, günde 2 kez"),
 "iso": ("İzometrik güçlendirme", "Avucunuzu alnınıza koyun. Başınızı hareket ettirmeden elinize doğru hafifçe itin, eliniz de karşı koysun. Aynısını başınızın arkası ve iki yanı için tekrarlayın. Kuvvetin yarısını kullanmanız yeterli.", "Her yöne 5 saniye, 5 tekrar"),
 "thor": ("Göğüs kafesini açma", "Sırtı alçak bir sandalyeye oturun, ellerinizi ensenizde birleştirin. Sandalyenin üst kenarını dayanak alarak göğsünüzü tavana doğru açın ve hafifçe geriye esneyin. Boynunuzu değil sırtınızı esnetin.", "5–10 tekrar"),
 "glide": ("Sinir kaydırma", "Kollarınızı omuz hizasında yana açın, dirsekleriniz 90 derece bükülü, avuç içleriniz öne baksın. Başınızı sağa eğerken sağ dirseğinizi açarak ön kolunuzu yana indirin, sağ kolunuz dümdüz olsun. Ortaya dönün. Sonra başınızı sola eğerken aynısını sol kolunuzla yapın. Sinir bir uçtan gerilirken diğer uçtan gevşer, böylece gerilmeden kayar.", "Her iki yana yavaşça 10 tekrar. Uyuşma artarsa bırakın"),
 "relief": ("Elinizi başınıza koyun", "Kol ağrısı şiddetliyken ağrılı taraftaki elinizi başınızın üstüne koyun ve öyle dinlenin. Bu pozisyon sinir kökü üzerindeki gerginliği azaltır. Bazı kişilerde kol ağrısını belirgin şekilde hafifletir.", "Rahatlatıyorsa birkaç dakika"),
}

NECK_CSS = OMUZ_CSS + """
  .kinds{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin-top:8px}
  @media (max-width:980px){.kinds{grid-template-columns:repeat(2,minmax(0,1fr))}}
  @media (max-width:560px){.kinds{grid-template-columns:1fr}}
  .kind{border:1px solid var(--line);border-radius:12px;padding:16px;background:var(--ground-2);display:grid;gap:6px;align-content:start}
  .kind .n{font-family:var(--display);font-size:28px;color:var(--foil);line-height:1}
  .kind h3{font-size:19px;margin:0}
  .kind p{font-size:15px;color:var(--ink-soft);margin:0}
  .kind a{font-size:14px;font-weight:600}
  .ex.four{grid-template-columns:repeat(4,minmax(0,1fr))}
  @media (max-width:1000px){.ex.four{grid-template-columns:repeat(2,minmax(0,1fr))}}
  @media (max-width:600px){.ex.four{grid-template-columns:1fr}}
  .callout{border-left:3px solid var(--gold);padding:4px 0 4px 16px;margin:18px 0 0;max-width:760px}
  .callout p{margin:0 0 8px;color:var(--ink-soft)}
  .callout.obs{border-left-color:var(--sage);background:rgba(143,164,118,.09);border-radius:0 12px 12px 0;padding:12px 16px 6px}
  .callout.obs .obs-k{font-size:12px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;color:var(--foil);margin:0 0 6px}
  .callout.obs p:not(.obs-k){color:var(--ink)}
  .rl{list-style:none;margin:0;padding:0;max-width:760px}
  .rl li{display:grid;grid-template-columns:70px minmax(0,1fr) minmax(0,1fr);gap:14px;padding:12px 0;border-top:1px solid var(--line)}
  .rl li:last-child{border-bottom:1px solid var(--line)}
  .rl .r{font-weight:600;display:flex;align-items:center;gap:8px;color:var(--ink)}
  .rl i{width:12px;height:12px;border-radius:3px;display:inline-block;flex:none}
  .rl em{display:block;font-style:normal;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-weight:600}
  .rl span{color:var(--ink-soft);font-size:15px}
  @media (max-width:560px){.rl li{grid-template-columns:1fr;gap:4px}}
  .roots{display:grid;grid-template-columns:minmax(0,1fr) 240px;gap:36px;align-items:center}
  @media (max-width:820px){.roots{grid-template-columns:1fr;gap:18px}}
  .hand{width:100%;max-width:240px;height:auto;display:block;margin:0 auto}
  @media (max-width:820px){.hand{max-width:190px}}
"""

def ex_grid(keys, cls="ex"):
    return f'<div class="{cls}">\n' + "\n".join(ex_card(k, *EXT[k]) for k in keys) + '\n      </div>'


def src_list(items):
    return "<ol>\n" + "\n".join(f"        <li>{s}</li>" for s in items) + "\n      </ol>"

# Kişisel klinik gözlem kutusu: araştırma kanıtından AYRI, açıkça "gözlem" diye etiketli (kullanıcı isteği, 7 Ekim 2026)
OBS_TAIL = "Bunu bir araştırma sonucu olarak değil, kendi gözlemim olarak paylaşıyorum; herkes aynı yanıtı vermeyebilir."
def OBS(text):
    return f'<div class="callout obs"><p class="obs-k">Kişisel klinik gözlemim</p><p>{text} {OBS_TAIL}</p></div>'
ACU_LAW = "Türkiye'de akupunkturu yalnızca ilgili alanda uygulama sertifikası olan hekimler, Sağlık Bakanlığınca yetkilendirilmiş birimlerde yapabilir. Akupunkturu tıbbi tedavinin ve rehabilitasyonun yerine değil, yanında düşünün."

def ext(url, text):
    return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'

def CTA_NOTE(what, svc="Evde değerlendirme, manuel terapi, kuru iğneleme ve kişiye özel egzersiz programı"):
    return (f'<div class="note" style="margin-top:20px"><strong>{what} için destek almak isterseniz:</strong> '
            f'{svc} için <a href="{WA}" target="_blank" rel="noopener">WhatsApp\'tan yazabilirsiniz</a>.</div>')

SRC_BLANPIED = ("Blanpied PR, Gross AR, Elliott JM, et al. " + ext("https://www.jospt.org/doi/10.2519/jospt.2017.0302", "Neck pain: revision 2017. Clinical practice guidelines linked to the International Classification of Functioning, Disability and Health from the Orthopaedic Section of the American Physical Therapy Association") + ". J Orthop Sports Phys Ther. 2017;47(7):A1-A83.")

# ------------------------------------------------------------------ BOYUN AĞRISI
BOYUN_AGRI_FAQ = [
 ("Boyun ağrısı ne kadar sürer?", "Seyri kişiden kişiye değişir. Uluslararası bir uzman grubuna göre boyun ağrısı vakaların en az yarısında tamamen geçmez; araştırmalarda boyun ağrısı yaşayanların %50–85'i 1–5 yıl sonra yine ağrı bildirdi. Bu yüzden ağrı azaldıktan sonra da egzersizlere devam etmek yararlı olabilir."),
 ("Sıcak mı uygulamalıyım, soğuk mu?", "Tutulma ve kas gerginliğinde ılık uygulama bazı kişileri rahatlatır; ancak araştırmalarda sıcak ve soğuk uygulamanın etkisi net değildir. Kullanacaksanız cildinizi bir bezle koruyun ve uyurken uygulamayın. Ağrı bir darbe, düşme ya da kazadan sonra başladıysa önce hekime başvurun."),
 ("Hangi yastığı kullanmalıyım?", "Herkes için en iyi tek bir yastık yok. Yan yatarken başınızı omuz hizasında tutan, sırtüstü yatarken başınızı öne itmeyen bir yükseklik seçin. Yüzüstü yatmak boynu uzun süre bir yana çevirdiği için ağrıyı artırabilir."),
 ("Boyunluk kullanmalı mıyım?", "Sıradan boyun ağrısında ve kaza sonrası boyun zorlanmasında (whiplash) önerilmez; ABD kılavuzu kaza sonrasında da kullanımı en aza indirmeyi öneriyor. Kola yayılan yeni ağrıda kısa süreli kullanılabilir. Kırık şüphesi gibi durumlarda boyunluğa hekiminiz karar verir."),
 ("Röntgen ya da MR çektirmem gerekir mi?", "Çoğu boyun ağrısında gerekmez. Yaşla birlikte görülen aşınma bulguları ağrısı olmayan kişilerde de sıktır ve çoğu zaman ağrıyı açıklamaz. Aşağıdaki uyarı işaretlerinden biri varsa ya da ağrı birkaç haftada düzelmiyorsa hekiminiz karar verir."),
 ("Telefona eğilmek boynumu bozar mı?", "Telefona bakarken boynu eğmenin boyna zarar verdiğine dair kanıt yok; ancak bu konuda çalışma az. Brezilya'da 18–21 yaşındaki 150 gençle yapılan bir çalışmada mesajlaşırken boyun duruşu ile boyun ağrısı arasında ilişki bulunmadı. Çalışma küçük ve kesitseldir; uzun yıllar boyunca eğik duruşun etkisi incelenmedi. Uzun süre aynı pozisyonda kalmak rahatsızlık veriyorsa ara verip pozisyonunuzu değiştirin."),
 ("Boyun düzleşmesi tehlikeli mi?", "Tek başına genellikle hayır. Boyun eğriliğinin azalması ağrısı olmayan kişilerde de görülür ve araştırmalarda ağrıyla tutarlı bir ilişkisi gösterilememiştir. Önemli olan şikâyetleriniz ve muayene bulgularıdır."),
]
BOYUN_TL = [
 ("2008", "Bone and Joint Decade Görev Gücü boyun ağrısını yeniden ele aldı: ağrıyı ciddiyetine göre dört dereceye ayırdı ve ağrının en az yarısında tamamen geçmediğini, iyileşmeyi psikolojik etkenlerin ve iş stresinin fiziksel etkenlerden daha çok etkiliyor göründüğünü bildirdi. Araştırmalarda boyun ağrısı yaşayanların %50–85'i 1–5 yıl sonra yine boyun ağrısı bildirdi."),
 ("2015", "27 çalışmayı inceleyen Cochrane derlemesi, uzun süren boyun ağrısında boyun, kürek kemiği ve kol kaslarını güçlendiren egzersizlerin ağrıyı tedavinin hemen sonunda orta ile belirgin düzeyde azalttığını buldu (orta kalitede kanıt); yalnızca germe egzersizinin yararı gösterilemedi."),
 ("2015", "Ağrısı olmayan 1.211 kişinin boyun MR'larını inceleyen çalışmada disk bombeleşmesi %87,6 oranında görüldü; 20'li yaşlarda bile yaygındı."),
 ("2017", "Amerikan Fizyoterapi Derneği'nin (APTA) ortopedi bölümünün kılavuzu, 2008'deki dört tipli sınıflamayı koruyarak güncellendi; her tip ve süre için farklı egzersiz ve manuel terapi önerdi."),
 ("2018", "Brezilya'da 18–21 yaşındaki 150 gençle yapılan kesitsel bir çalışmada mesajlaşırken boyun duruşu ile boyun ağrısı arasında ilişki bulunmadı."),
 ("2021", "Avrupa'daki altı boyun ağrısı kılavuzunu karşılaştıran bir derleme: egzersiz ve başka tedavilerle birlikte manuel terapi orta düzeyde, bilgilendirme ve güvence verme zayıf düzeyde önerildi; elektroterapi, akupunktur ve kuru iğneleme, traksiyon ve boyunluk konusunda kılavuzlar tutarsızdı ya da kesin bir sonuca varamadı."),
 ("2024", "Küresel Hastalık Yükü çalışması dünyada 2020'de 203 milyon kişinin boyun ağrısı yaşadığını hesapladı."),
]

AGRI_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Boyun ağrısı</h1>
    <p class="lede">Çoğu insanın hayatının bir döneminde yaşadığı, çoğu zaman ciddi bir nedene bağlı olmayan ama sık tekrarlayabilen bir sorun. İyi haber: düzenli hareket ve egzersiz çoğu kişide ağrıyı azaltmaya yardımcı olur.</p>
    <p class="meta">Son güncelleme: 30 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>203 milyon</b><span>Dünyada boyun ağrısı yaşayan kişi (2020)</span></div>
        <div class="stat"><b>%32,5</b><span>2020–2050 arasında boyun ağrılı kişi sayısında beklenen artış (yaşa göre düzeltilmiş görülme oranı ise 1990–2020 arasında sabit kaldı)</span></div>
        <div class="stat"><b>45–74</b><span>En sık etkilenen yaş aralığı</span></div>
        <div class="stat"><b>%50–85</b><span>Bir kez yaşayanlarda 1–5 yıl sonra yine ağrı (süren ya da tekrarlayan)</span></div>
      </div>
      {g_toc([("nedir", "Nedir?"), ("tipler", "Dört tip"), ("derece", "Ne kadar ciddi?"), ("duzlesme", "Düzleşme, MR ve duruş"), ("tarihce", "Geçmişten bugüne"), ("tedavi", "Tedavi seçenekleri"), ("egzersizler", "Egzersizler"), ("masa", "Masa başında"), ("videolar", "Videolar"), ("sss", "Sık sorulan sorular"), ("uyari", "Uyarı işaretleri")])}
    </div>
  </section>

  <section id="nedir">
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Kafatasının alt sınırından omuzlara kadar uzanan bölgedeki ağrıdır. Çoğu zaman belirli bir yapıya bağlanamaz; kasların, bağların ve omurlar arasındaki küçük eklemlerin rol oynadığı düşünülür. Tıpta buna <em>mekanik</em> ya da <em>nonspesifik</em> boyun ağrısı denir: ağrı gerçektir ama altında ciddi bir hastalık yoktur.</p>
        <p class="soft">Ağrı kola ve parmaklara uyuşma, karıncalanma ya da elektriklenmeyle yayılıyorsa bir sinir kökü etkileniyor olabilir. Bu durumu ayrı bir sayfada anlattık: <a href="boyun-fitigi.html">Boyun fıtığı ve sinir sıkışması →</a></p>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Saatlerce aynı pozisyonda kalmak (masa başı çalışma, uzun süre telefona bakmak) rahatsızlık yaratabilir; duruşun tek başına ağrıya yol açtığı gösterilmedi</li>
          <li>Uykuda boynun uzun süre zorlanması ya da ani bir hareketle gelen "tutulma"</li>
          <li>Stres, kaygı ve uykusuzluk: kas gerginliğini ve ağrıya duyarlılığı artırır</li>
          <li>Hareketsizlik, omuz ve sırt kaslarının zayıflığı</li>
          <li>Yaşla birlikte omurgada aşınma (kireçlenme) bulguları sık görülür; ancak ağrısı olmayanlarda da vardır ve çoğu zaman ağrıyı açıklamaz.</li>
          <li>Trafik kazasında olduğu gibi ani savrulma yaralanmaları</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="tipler">
    <div class="wrap">
      <h2>Boyun ağrısının dört tipi</h2>
      <p class="soft">Amerikan Fizyoterapi Derneği'nin kılavuzu boyun ağrısını dört gruba ayırır ve tedaviyi buna göre önerir; her hasta bunlardan birine tam uymayabilir.</p>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Hareket kısıtlılığıyla</h3><p>Bildiğimiz "tutulma". Boyun bazı yönlere dönmez, ağrı hareketle artar.</p></div>
        <div class="kind"><span class="n">2</span><h3>Baş ağrısıyla</h3><p>Ağrı boyundan başın arkasına, bazen alna yayılır ve boyun hareketleriyle tetiklenir. Buna servikojenik baş ağrısı denir.</p></div>
        <div class="kind"><span class="n">3</span><h3>Kola yayılan ağrıyla</h3><p>Bir sinir kökü etkilenir. Kolda ağrı, uyuşma, karıncalanma ya da güçsüzlük olur.</p><a href="boyun-fitigi.html">Boyun fıtığı sayfası →</a></div>
        <div class="kind"><span class="n">4</span><h3>Hareket kontrolü bozukluğuyla</h3><p>Çoğunlukla trafik kazası sonrası görülür. Boyun kaslarının koordinasyonu ve dayanıklılığı azalır.</p></div>
      </div>
    </div>
  </section>

  <section id="derece">
    <div class="wrap">
      <h2>Ne kadar ciddi? Dört derece</h2>
      <p class="soft">Uluslararası bir uzman grubu (Bone and Joint Decade Görev Gücü, 2008) boyun ağrısını ciddiyetine göre dört dereceye ayırdı. Boyun ağrılarının çoğu ilk iki derecededir.</p>
      <div class="kinds">
        <div class="kind"><span class="n">I</span><h3>Günlük işleri hiç ya da az etkileyen ağrı</h3><p>Ciddi bir yapısal neden belirtisi yok. Kapsamlı tetkik ya da girişimsel tedavi genellikle gerekmez.</p></div>
        <div class="kind"><span class="n">II</span><h3>Günlük işleri belirgin kısıtlayan ağrı</h3><p>Ciddi bir neden belirtisi yok. Uzun süreli kısıtlılığı önlemek için ağrı kontrolü ve erken harekete geçme önerilir.</p></div>
        <div class="kind"><span class="n">III</span><h3>Sinir bulgularıyla</h3><p>Reflekslerde azalma ya da kas güçsüzlüğü gibi sinir bulguları var. İleri tetkik gerekebilir.</p><a href="boyun-fitigi.html">Boyun fıtığı ve sinir sıkışması →</a></div>
        <div class="kind"><span class="n">IV</span><h3>Ciddi bir nedenin belirtileriyle</h3><p>Kırık, omurilik basısı, tümör ya da sistemik bir hastalık gibi ciddi bir nedenin belirtileri var. Hemen değerlendirme gerekir.</p><a href="#uyari">Uyarı işaretleri →</a></div>
      </div>
    </div>
  </section>

  <section id="duzlesme">
    <div class="wrap">
      <h2>Boyun düzleşmesi, MR bulguları ve "kötü duruş"</h2>
      <p class="soft">Röntgende "boyun düzleşmesi" yazısını görmek birçok kişiyi endişelendirir. 54'ü boyun ağrılı, 53'ü ağrısız 107 kişinin karşılaştırıldığı bir çalışmada iki grup arasında boyun eğriliği açısından fark bulunmadı. Araştırmacılara göre boyun ağrılı kişilerde görülen bu tür bulgular rastlantısal kabul edilmeli; yani ağrının nedenini göstermeyebilir.</p>
      <p class="soft">MR raporlarındaki "disk bombeleşmesi" için de durum benzer: ağrısı olmayan 1.211 kişinin boyun MR'larının incelendiği çalışmada disk bombeleşmesi %87,6 oranında görüldü; 20'li yaşlarda bile erkeklerin %73'ünde, kadınların %78'inde vardı.</p>
      <div class="callout">
        <p>Telefonla mesajlaşırken duruş için de benzer bir sonuç var: Brezilya'da 18–21 yaşındaki 150 gençle yapılan kesitsel bir çalışmada mesajlaşırken boyun duruşu ile boyun ağrısı arasında ilişki bulunmadı. Çalışma küçüktür ve uzun yıllar boyunca eğik duruşun etkisini incelemedi. Uzun süre aynı pozisyonda kalmak rahatsızlık veriyorsa pozisyonunuzu sık sık değiştirin.</p>
      </div>
    </div>
  </section>

  <section id="tarihce">
    <div class="wrap">
      <p class="eyebrow">Geçmişten bugüne</p>
      <h2>Boyun ağrısı araştırmalarının kısa tarihi</h2>
      <p class="soft">Son 20 yılın araştırmaları egzersizin, hareketli kalmanın ve ağrının tipine göre tedavinin önemini öne çıkardı.</p>
      {g_tl(BOYUN_TL)}
    </div>
  </section>

  <section id="tedavi">
    <div class="wrap">
      <h2>Tedavi</h2>
      <p class="soft">Çoğu boyun ağrısında röntgen ya da MR gerekmez; tanı muayeneyle konur. Tedavi, ağrının tipine ve ne zamandır sürdüğüne göre planlanır.</p>
      <ul class="tx">
        <li><b>Hareketli kalmak</b><span>Yatak istirahati ve uzun süre boyunluk önerilmez. Ağrının izin verdiği ölçüde günlük işlere devam etmek önerilir ve iyileşmeye yardımcı olabilir.</span></li>
        <li><b>Egzersiz</b><span>Tedavinin temelidir. Boyun, kürek kemiği ve kol kaslarını güçlendiren egzersizler uzun süren boyun ağrısını tedavinin hemen sonunda orta ile belirgin düzeyde azalttı (orta kalitede kanıt). Yalnızca germe egzersizlerinin yararı gösterilemedi.</span></li>
        <li><b>Manuel terapi</b><span>Mobilizasyon ve manipülasyon, Avrupa kılavuzlarında egzersiz gibi başka tedavilerle birlikte orta düzeyde öneriliyor; tek başına kullanımı konusunda kılavuzlar tutarsız. ABD kılavuzu boyun ve sırt (torakal) omurgasına uygulamayı ağrının tipine göre öneriyor. Muayeneden sonra, eğitimli bir fizyoterapist tarafından uygulanmalıdır.</span></li>
        <li><b>İlaçlar</b><span>Hekiminizin önerdiği ağrı kesiciler kısa süreli rahatlama sağlayabilir.</span></li>
        <li><b>Stres ve uyku</b><span>Uzun süren ağrıda stres yönetimi ve düzenli uyku da tedavinin parçasıdır. <a href="stres.html">Nefes egzersizlerine göz atın →</a></span></li>
      </ul>
      <h3 class="g-h3">Tedavi seçenekleri: kılavuzlar ne diyor?</h3>
      <p class="soft">Amerikan Fizyoterapi Derneği'nin (APTA) ortopedi bölümünün kılavuzu (2017) ile Avrupa'daki altı boyun ağrısı kılavuzunu karşılaştıran derlemenin (2021) bulguları yan yana. Parantez içindeki harfler ABD kılavuzundaki kanıt düzeyidir (B orta, C zayıf). İki kaynağın derecelendirmesi aynı ölçekte değildir: ABD kılavuzu kanıt düzeyini, Avrupa derlemesi kılavuzların tutarlılığını ve kalitesini değerlendirir. Öneriler ağrının tipine göre değişir; tedavi kişiye göre seçilir.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Bilgilendirme ve güvence</h3><dl><dt>Avrupa (6 kılavuz)</dt><dd>Hareketli kalma ve egzersize teşvik dahil, zayıf düzeyde öneriliyor.</dd><dt>ABD (APTA)</dt><dd>Kaza sonrası boyun ağrısında olağan etkinliklere en kısa sürede dönmek ve iyileşmenin genellikle ilk 2–3 ayda beklendiğini bilmek (B); kola yayılan uzun süren ağrıda (B) ve uzun süren hareket kısıtlılığında (C) bilgilendirme ve danışmanlık.</dd></dl></div>
        <div class="kind"><h3>Egzersiz</h3><dl><dt>Avrupa (6 kılavuz)</dt><dd>Orta düzeyde öneriliyor.</dd><dt>ABD (APTA)</dt><dd>Tipe göre: hareket açıklığı, kürek kemiği ve kol güçlendirme, dayanıklılık ve koordinasyon egzersizleri (çoğunlukla B).</dd></dl></div>
        <div class="kind"><h3>Manuel terapi</h3><dl><dt>Avrupa (6 kılavuz)</dt><dd>Başka tedavilerle birlikte orta düzeyde öneriliyor; tek başına tutarsız.</dd><dt>ABD (APTA)</dt><dd>Sırt (torakal) ve boyun manipülasyonu ya da mobilizasyonu, ağrının tipine ve süresine göre öneriliyor (B ya da C).</dd></dl></div>
        <div class="kind"><h3>Psikolojik yaklaşımlar</h3><dl><dt>Avrupa (6 kılavuz)</dt><dd>Yalnızca belirli gruplarda (ruh hali sorunları, psikososyal risk etkenleri ya da karmaşık, uzun süren ağrı) zayıf düzeyde öneriliyor.</dd><dt>ABD (APTA)</dt><dd>Kaza sonrası uzun süren ağrıda bilişsel davranışçı ilkelerle kişiye özel, kademeli egzersiz (C).</dd></dl></div>
        <div class="kind"><h3>Traksiyon</h3><dl><dt>Avrupa (6 kılavuz)</dt><dd>Kesin bir sonuca varılamadı.</dd><dt>ABD (APTA)</dt><dd>Kola yayılan uzun süren ağrıda aralıklı boyun traksiyonu, egzersiz ve manuel terapiyle birlikte (B).</dd></dl></div>
        <div class="kind"><h3>TENS ve lazer</h3><dl><dt>Avrupa (6 kılavuz)</dt><dd>Elektroterapi (TENS ve lazer ayrı değerlendirilmedi): dört kılavuzdan ikisi önermiyor; genel sonuç kesin değil.</dd><dt>ABD (APTA)</dt><dd>TENS kaza sonrası ağrıda (C); lazer uzun süren hareket kısıtlılığında (B, birleşik tedavinin parçası olarak) ve kola yayılan yeni ağrıda (C).</dd></dl></div>
        <div class="kind"><h3>Kuru iğneleme ve akupunktur</h3><dl><dt>Avrupa (6 kılavuz)</dt><dd>Tutarsız.</dd><dt>ABD (APTA)</dt><dd>Kuru iğneleme, uzun süren hareket kısıtlılığında birleşik tedavinin parçası olarak seçenekler arasında (B).</dd><dt>Not</dt><dd>Türkiye'de yalnızca yetkili hekimler uygulayabilir.</dd></dl></div>
        <div class="kind"><h3>Boyunluk</h3><dl><dt>Avrupa (6 kılavuz)</dt><dd>Kesin bir sonuca varılamadı.</dd><dt>ABD (APTA)</dt><dd>Kaza sonrası kullanımı en aza indirmek (B); kola yayılan yeni ağrıda kısa süreli (C).</dd></dl></div>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Boyun için altı temel egzersiz</h2>
      <p class="soft">Egzersizleri yavaş ve kontrollü yapın. Hafif bir gerginlik normaldir, keskin ağrıya kadar zorlamayın. Ağrı kola yayılmaya başlarsa o egzersizi bırakın ve fizyoterapistinize danışın.</p>
      {ex_grid(["chin", "rot", "side", "scap", "iso", "thor"])}
    </div>
  </section>

  <section id="masa">
    <div class="wrap two">
      <div>
        <h2>Masa başında boynunuz için</h2>
        <p class="soft">Ekran başında saatlerce aynı pozisyonda kalmak boyunda rahatsızlık yapabilir. Duruşun boyun ağrısına yol açtığı araştırmalarda net olarak gösterilmedi; yine de şu küçük düzenlemeler rahat çalışmanıza yardım edebilir.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Ekranın üst kenarı göz hizasında ya da biraz altında olsun.</li>
        <li>Dizüstü bilgisayarla uzun çalışıyorsanız bir yükseltici ve ayrı klavye kullanın.</li>
        <li>Telefonu göz hizasına kaldırın; başınızı değil gözlerinizi indirin.</li>
        <li>Yarım saatte bir kalkın, omuzlarınızı çevirin, birkaç adım yürüyün.</li>
        <li>Telefonla konuşurken telefonu omzunuzla kulağınız arasına sıkıştırmayın.</li>
      </ul>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Boyun ağrısı için egzersiz videoları</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("Wsb78V2UYVA", "Temel boyun egzersizi videosunu oynat", "The One Exercise Everyone Should Do For Neck Pain")}
          <h3>Herkesin yapması gereken tek boyun egzersizi</h3>
          <p>Boyun ağrısında en temel egzersizin doğru yapılışı.</p>
        </div>
        <div class="vid">
          {vbox("W8Lk6E6_cgg", "Tutulan boyun videosunu oynat", "Top 6 Exercises For A Stiff Neck")}
          <h3>Tutulan boyun için altı egzersiz</h3>
          <p>Boyun tutulmasında hareketi geri kazanmaya yönelik kısa bir program.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir. Kanal hakkında: <a href="https://www.startribune.com/meet-the-minnesota-physical-therapists-who-have-become-youtube-superstars/508806552" target="_blank" rel="noopener">Star Tribune, 19 Nisan 2019</a>.</p>
    </div>
  </section>

  <section id="sss">
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(BOYUN_AGRI_FAQ)}
    </div>
  </section>

  <section id="uyari">
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Boyun ağrısı çoğunlukla zararsızdır. Şu durumlarda ise beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Ağrı trafik kazası, düşme ya da darbeden sonra başladıysa</li>
        <li>Kollarda ya da bacaklarda güç kaybı, ellerde beceriksizlik (düğme iliklemede zorlanma), yürürken dengesizlik varsa</li>
        <li>İdrar ya da dışkı kontrolünde değişiklik olduysa</li>
        <li>Ateş, titreme, nedensiz kilo kaybı ya da kanser öyküsüyle birlikte ağrı varsa</li>
        <li>Dinlenmekle geçmeyen, giderek artan şiddetli gece ağrısı varsa</li>
        <li>Ani başlayan, hayatınızın en şiddetli baş ağrısı varsa (<strong>112</strong>)</li>
        <li>Ateşle birlikte ense sertliği varsa (<strong>112</strong>)</li>
        <li>Ani başlayan baş dönmesi, çift görme, konuşma ya da yutma güçlüğü eşlik ediyorsa (<strong>112</strong>)</li>
        <li>Boyun ağrısına göğüs ağrısı, nefes darlığı ya da terleme eşlik ediyorsa (kalp kaynaklı olabilir, <strong>112</strong>)</li>
      </ul>
      {CTA_CARD("Boyun ağrınız", "boyun ağrım")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        SRC_BLANPIED,
        "Carroll LJ, Hogg-Johnson S, van der Velde G, et al. Course and prognostic factors for neck pain in the general population: results of the Bone and Joint Decade 2000–2010 Task Force on Neck Pain and Its Associated Disorders. Spine. 2008;33(4 Suppl):S75-S82.",
        "Corp N, Mansell G, Stynes S, et al. " + ext("https://publications.aston.ac.uk/id/eprint/42010/1/ejp.1679.pdf", "Evidence-based treatment recommendations for neck and low back pain across Europe: a systematic review of guidelines") + ". Eur J Pain. 2021;25(2):275-295.",
        "Damasceno GM, Ferreira AS, Nogueira LAC, Reis FJJ, Andrade ICS, Meziat-Filho N. " + ext("https://www.painscience.com/biblio/no-link-between-text-neck-posture-and-neck-pain-in-150-brazilian-young-adults.html", "Text neck and neck pain in 18–21-year-old young adults") + ". Eur Spine J. 2018.",
        "GBD 2021 Neck Pain Collaborators. " + ext("https://www.thelancet.com/journals/lanrhe/article/PIIS2665-9913(23)00321-1/fulltext", "Global, regional, and national burden of neck pain, 1990–2020, and projections to 2050: a systematic analysis of the Global Burden of Disease Study 2021") + ". Lancet Rheumatol. 2024;6(3):e142-e155.",
        "Grob D, Frauenfelder H, Mannion AF. " + ext("https://link.springer.com/article/10.1007/s00586-006-0254-1", "The association between cervical spine curvature and neck pain") + ". Eur Spine J. 2007;16(5):669-678.",
        "Gross A, Kay TM, Paquin JP, et al. " + ext("https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD004250.pub5/full", "Exercises for mechanical neck disorders") + ". Cochrane Database Syst Rev. 2015;1:CD004250.",
        "Haldeman S, Carroll L, Cassidy JD, et al. The Bone and Joint Decade 2000–2010 Task Force on Neck Pain and Its Associated Disorders: executive summary. Spine. 2008;33(4 Suppl). Özet: " + ext("https://www.newswise.com/articles/task-force-presents-evidence-based-recommendations-on-neck-pain", "Wolters Kluwer basın bülteni, 2008") + ".",
        "Nakashima H, Yukawa Y, Suda K, et al. " + ext("https://www.qxmd.com/r/25584950", "Abnormal findings on magnetic resonance images of the cervical spines in 1211 asymptomatic subjects") + ". Spine. 2015.",
        "Physiopedia. " + ext("https://www.physio-pedia.com/Mechanical_Neck_Pain", "Mechanical Neck Pain") + ".",
      ])}
    </div>
  </section>
</main>'''

page("boyun-agrisi.html", "Boyun Ağrısı",
     "Boyun ağrısı neden olur, ne kadar sürer, boyun düzleşmesi önemli mi? Evde yapılabilecek altı egzersiz, masa başı önerileri, videolar ve uyarı işaretleri.",
     "boyun-agrisi.html", NECK_CSS, AGRI_BODY, YT_JS,
     seo_title="Boyun Ağrısı: Nedenleri, Egzersizler ve Tedavi | İhsan Eren", condition="Boyun ağrısı", about=cond("Boyun ağrısı", "neck-pain"),
     faq_items=pick(BOYUN_AGRI_FAQ, 0, 4, 3, 5))

# ------------------------------------------------------------------ BOYUN FITIĞI
C5, C6, C7, C8 = "#b9b37a", "#e2ab47", "#8fa476", "#c96b5a"
HAND = f'''<svg class="hand" viewBox="0 0 200 250" role="img" aria-label="Sağ el, avuç içi: başparmak ve işaret parmağı C6, orta parmak C7, yüzük ve serçe parmak C8 bölgesi">
  <defs><clipPath id="palmclip"><path d="M66 114 Q64 180 86 188 H124 Q146 180 144 114 Q144 104 134 104 H76 Q66 104 66 114 Z"/></clipPath></defs>
  <path d="M82 250 L85 184 H105 V250 Z" fill="{C6}" opacity=".35"/><path d="M105 250 V184 H125 L128 250 Z" fill="{C8}" opacity=".35"/>
  <path d="M66 114 Q64 180 86 188 H124 Q146 180 144 114 Q144 104 134 104 H76 Q66 104 66 114 Z" fill="#2d3b29"/>
  <g clip-path="url(#palmclip)" opacity=".38"><rect x="60" y="100" width="28" height="92" fill="{C6}"/><rect x="88" y="100" width="20" height="92" fill="{C7}"/><rect x="108" y="100" width="42" height="92" fill="{C8}"/></g>
  <g fill="none" stroke-linecap="round">
    <path d="M74 160 L44 118" stroke="{C6}" stroke-width="19"/>
    <path d="M77 120 V50" stroke="{C6}" stroke-width="17"/>
    <path d="M98 118 V38" stroke="{C7}" stroke-width="17"/>
    <path d="M119 120 V46" stroke="{C8}" stroke-width="17"/>
    <path d="M138 124 V66" stroke="{C8}" stroke-width="15"/>
  </g>
  <g font-family="Figtree,system-ui,sans-serif" font-size="15" font-weight="600">
    <text x="22" y="104" fill="{C6}">C6</text><text x="87" y="24" fill="{C7}">C7</text><text x="150" y="58" fill="{C8}">C8</text>
  </g>
</svg>'''

def root_row(color, name, area, move, note=""):
    return (f'<li><span class="r"><i style="background:{color}"></i>{name}</span>'
            f'<span><em>Ağrı ve uyuşma</em>{area}</span><span><em>Zayıflayabilen hareket</em>{move}{note}</span></li>')

DUZ_LINK = '<a href="boyun-agrisi.html#duzlesme">Boyun düzleşmesi hakkında →</a>'
BOYUN_FITIK_FAQ = [
 ("Boyun fıtığı kendiliğinden geçer mi?", "Çoğu kişide evet. Belirtiler genellikle ilk haftalarda en yoğundur ve çoğu kişi 4–6 ay içinde belirgin şekilde düzelir. Bu süreçte egzersiz ve fizyoterapi hem ağrıyı azaltır hem de günlük yaşama dönüşü kolaylaştırır."),
 ("Ameliyat ne zaman gerekir?", "Kolda giderek artan güç kaybı, ellerde beceriksizlik ve yürüme bozukluğu gibi omurilik basısı belirtileri ya da 6–12 haftalık uygun tedaviye rağmen günlük yaşamı bozan ağrı varsa cerrahi değerlendirme gerekir. Kola yayılan sinir sıkışması olan hastaların izlendiği bir nüfus çalışmasında yaklaşık dörtte biri izlem süresinde ameliyat olmuştu; çoğu kişi ameliyatsız iyileşir."),
 ("MR'ımda fıtık var ama ağrım yok. Ne yapmalıyım?", "Endişelenmeyin. Ağrısı olmayan kişilerin büyük çoğunluğunda MR'da disk bombeleşmesi (bulging) görülür; bu bulgu tek başına hastalık anlamına gelmez. Şikâyetiniz yoksa tedavi gerekmez; düzenli egzersizle boyun sağlığınızı koruyabilirsiniz."),
 ("Boyun fıtığında masaj ya da kütletme yapılır mı?", "Yumuşak doku çalışması ve nazik mobilizasyon genellikle güvenlidir. Hızlı ve kuvvetli boyun manipülasyonu (kütletme) ise kola yayılan sinir belirtileri varken ancak ayrıntılı muayeneden sonra ve eğitimli bir uygulayıcı tarafından düşünülmelidir."),
 ("Nasıl yatmalıyım?", "Sırtüstü ya da ağrısız tarafınıza yan yatmak çoğu kişiye daha rahat gelir. Yastık boynunuzu omurganızla aynı hizada tutmalı. Yüzüstü yatmaktan kaçının."),
 ("Boyun fıtığı ile boyun düzleşmesi aynı şey mi?", "Hayır. Boyun düzleşmesi, röntgende boyun omurgasının doğal hafif kavisinin azalmasıdır ve ağrısı olmayan kişilerde de sık görülür. Fıtık ise diskin taşmasıdır. " + DUZ_LINK),
]
FITIK_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Boyun fıtığı ve sinir sıkışması</h1>
    <p class="lede">Boyundaki disklerden birinin taşması ya da omurgadaki kireçlenmenin bir sinir kökünü sıkıştırmasıyla ortaya çıkar. Ağrı kola ve parmaklara vurur; uyuşma ve güçsüzlük olabilir. Çoğu kişi ameliyatsız iyileşir.</p>
    <p class="meta">Son güncelleme: 29 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>83</b><span>Her yıl 100.000 kişide yeni kola yayılan sinir sıkışması</span></div>
        <div class="stat"><b>4–6 ay</b><span>Çoğu kişide belirgin düzelme süresi</span></div>
        <div class="stat"><b>%90</b><span>Uzun dönemde yakınması olmayan ya da hafif kalan (ameliyat olanlar dahil)</span></div>
        <div class="stat"><b>%87,6</b><span>Hiç ağrısı olmayanların MR'ında disk bombeleşmesi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Omurların arasında yastık görevi gören diskler vardır. Diskin dış halkası zayıflayıp yırtıldığında içindeki jel kıvamındaki çekirdek dışarı taşar; buna fıtık denir. Taşan kısım omurilikten kola giden bir sinir köküne baskı yapar ya da onu tahriş eder.</p>
        <p class="soft">Kola yayılan sinir sıkışmasının (servikal radikülopati) tek nedeni fıtık değildir. Özellikle ileri yaşta daha sık neden, kireçlenmeye bağlı kemik çıkıntılarının sinirin çıktığı deliği daraltmasıdır. Genç yaşta ise fıtık daha sık görülür.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Boyundan omuza, kürek kemiğine ve kola yayılan ağrı, çoğunlukla tek tarafta</li>
          <li>Kolda, elde ya da belirli parmaklarda uyuşma, karıncalanma, elektriklenme</li>
          <li>Kolda ya da elde güçsüzlük, kavramada zorlanma</li>
          <li>Başı geriye atmak ya da ağrılı tarafa çevirmek ağrıyı artırabilir</li>
          <li>Bazı kişiler elini başının üstüne koyduğunda kol ağrısının azaldığını fark eder</li>
        </ul>
        <p class="soft">Sadece boyunda ağrı varsa ve kola yayılmıyorsa: <a href="boyun-agrisi.html">Boyun ağrısı sayfası →</a></p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap roots">
      <div>
        <h2>Hangi sinir nereye vurur?</h2>
        <p class="soft">Sıkışan sinir köküne göre ağrı ve uyuşma farklı bölgelere yayılır. En sık etkilenen kök C7, ardından C6'dır.</p>
        <ul class="rl">
          {root_row(C5, "C5", "Omzun dışı ve üst kol", "Kolu yana kaldırma")}
          {root_row(C6, "C6", "Ön kolun dış yanı, başparmak ve işaret parmağı", "Dirseği bükme, bileği yukarı kaldırma")}
          {root_row(C7, "C7", "Orta parmak", "Dirseği düzeltme, itme")}
          {root_row(C8, "C8", "Yüzük ve serçe parmak, elin iç kenarı", "Parmakları kullanma, kavrama")}
        </ul>
      </div>
      {HAND}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tanı: MR her şey değil</h2>
      <p class="soft">Tanı önce muayeneyle konur. Fizyoterapist ya da hekim boyun hareketlerini, kol kaslarının gücünü, refleksleri ve duyuyu değerlendirir. Sinir kökünü zorlayan ya da rahatlatan özel testler yapar; Spurling testi, sinir germe testi ve boyun çekme testi bunlardan bazılarıdır.</p>
      <div class="callout">
        <p>MR fıtığın yerini gösterir ama tek başına karar verdirmez. Hiçbir şikâyeti olmayan 1211 kişinin %87,6'sında MR'da disk bombeleşmesi (bulging) görüldü; 20'li yaşlarda bile bu oran %73–78'di. Önemli olan, MR bulgusunun şikâyetler ve muayeneyle uyuşup uyuşmadığıdır.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Seyri ve tedavi</h2>
      <p class="soft">Belirtiler genellikle ilk haftalarda en yoğundur. Çoğu kişi 4–6 ay içinde belirgin şekilde düzelir; az sayıdaki çalışmada bu düzelme 2–3 yıllık izlemde genellikle korundu. ABD'de 1976–1990 yıllarında kola yayılan sinir sıkışması (fıtık ya da kireçlenmeye bağlı) tanısı alan 561 hastanın yaklaşık 5 yıl izlendiği bir nüfus çalışmasında son kontrolde, ameliyat olanlar dahil hastaların %90'ında hiç yakınma yoktu ya da yakınmalar hafifti; hastaların dörtte biri izlem süresinde ameliyat olmuştu.</p>
      <ul class="tx">
        <li><b>Hareketli kalmak</b><span>Ağrıyı çok artıran hareketlerden birkaç gün kaçınmak yeterlidir. Tam yatak istirahati önerilmez.</span></li>
        <li><b>Egzersiz</b><span>Derin boyun kaslarını ve kürek kemiği çevresini güçlendiren, boynu dengeleyen egzersizler ile sinir kaydırma egzersizleri tedavinin önemli bir parçasıdır.</span></li>
        <li><b>Manuel terapi ve traksiyon</b><span>Egzersizle birlikte uygulanan manuel terapi ve aralıklı boyun traksiyonu (boynun kontrollü çekilmesi), uzun süren kola yayılan ağrıda kılavuzlarda önerilir.</span></li>
        <li><b>Boyunluk</b><span>Ağrının çok şiddetli olduğu ilk günlerde kısa süreli kullanılabilir. Uzun süreli kullanım önerilmez.</span></li>
        <li><b>İlaç ve enjeksiyon</b><span>Hekiminizin önerdiği ağrı kesiciler. Seçilmiş hastalarda sinir köküne yönelik enjeksiyonlar hekim kararıyla uygulanabilir.</span></li>
        <li><b>Ameliyat</b><span>Giderek artan güç kaybı, omurilik basısı belirtileri ya da 6–12 haftalık uygun tedaviye rağmen günlük yaşamı bozan ağrı varsa beyin ve sinir cerrahisi ya da ortopedi değerlendirmesi gerekir.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Sinir sıkışmasında dört egzersiz</h2>
      <p class="soft">Egzersiz sırasında kola yayılan ağrı, uyuşma ya da karıncalanma artıyor ya da parmaklara doğru ilerliyorsa o egzersizi bırakın. Ağrının koldan boyna doğru çekilmesi ise genellikle iyiye işarettir. Güçlendirme ve germe egzersizleri için <a href="boyun-agrisi.html#egzersizler">boyun ağrısı sayfasına</a> da bakabilirsiniz.</p>
      {ex_grid(["relief", "chin", "glide", "scap"], "ex four")}
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Boyunda sinir sıkışması için videolar</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("C_UTuVETXUY", "Sinir sıkışması videosunu oynat", "How To Overcome Cervical Pinched Nerve And Radiculopathy")}
          <h3>Boyunda sinir sıkışmasıyla başa çıkmak</h3>
          <p>Kola yayılan ağrıda neler yapılabileceğine dair genel bir yol haritası.</p>
        </div>
        <div class="vid">
          {vbox("RdgDg9_SL48", "Sinir sıkışması egzersizleri videosunu oynat", "Most Important Exercises to Help Pinched Nerve &amp; Neck Pain")}
          <h3>Sinir sıkışmasında en önemli egzersizler</h3>
          <p>Sinir sıkışması ve boyun ağrısında öne çıkan egzersizler.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir. Kanal hakkında: <a href="https://www.startribune.com/meet-the-minnesota-physical-therapists-who-have-become-youtube-superstars/508806552" target="_blank" rel="noopener">Star Tribune, 19 Nisan 2019</a>.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(BOYUN_FITIK_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu belirtiler omuriliğin ya da sinirlerin ciddi şekilde etkilendiğini gösterebilir. Beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Her iki kolda birden uyuşma ya da güçsüzlük</li>
        <li>Ellerde beceriksizlik: düğme iliklemede, yazı yazmada zorlanma, elden eşya düşürme</li>
        <li>Yürürken dengesizlik, bacaklarda güçsüzlük ya da uyuşma</li>
        <li>İdrar ya da dışkı kontrolünde değişiklik (acil)</li>
        <li>Kolda hızla artan güç kaybı</li>
        <li>Ateş, nedensiz kilo kaybı, kanser öyküsü ya da bir kaza sonrası başlayan ağrı</li>
        <li>Kol ağrısına göğüs ağrısı, nefes darlığı ya da terleme eşlik ediyorsa (kalp kaynaklı olabilir, <strong>112</strong>)</li>
      </ul>
      {CTA_CARD("Boyun fıtığı ve kola yayılan ağrınız", "boyun fıtığı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Australian Physiotherapy Association. " + ext("https://australian.physio/inmotion/cervical-radiculopathy", "Cervical radiculopathy") + ". InMotion.",
        SRC_BLANPIED,
        "Nakashima H, Yukawa Y, Suda K, Yamagata M, Ueta T, Kato F. Abnormal findings on magnetic resonance images of the cervical spines in 1211 asymptomatic subjects. Spine. 2015;40(6):392-398.",
        "Physiopedia. " + ext("https://www.physio-pedia.com/Cervical_Radiculopathy", "Cervical Radiculopathy") + ".",
        "Radhakrishnan K, Litchy WJ, O'Fallon WM, Kurland LT. Epidemiology of cervical radiculopathy. A population-based study from Rochester, Minnesota, 1976 through 1990. Brain. 1994;117(Pt 2):325-335.",
        "Wainner RS, Fritz JM, Irrgang JJ, Boninger ML, Delitto A, Allison S. Reliability and diagnostic accuracy of the clinical examination and patient self-report measures for cervical radiculopathy. Spine. 2003;28(1):52-62.",
        "Wong JJ, Côté P, Quesnele JJ, Stern PJ, Mior SA. The course and prognostic factors of symptomatic cervical disc herniation with radiculopathy: a systematic review of the literature. Spine J. 2014;14(8):1781-1789.",
      ])}
    </div>
  </section>
</main>'''

page("boyun-fitigi.html", "Boyun Fıtığı",
     "Boyun fıtığı ve kola yayılan sinir sıkışması: belirtiler, hangi sinir nereye vurur, MR ne anlatır, ameliyatsız tedavi, evde egzersizler ve ne zaman ameliyat gerekir.",
     "boyun-fitigi.html", NECK_CSS, FITIK_BODY, YT_JS,
     seo_title="Boyun Fıtığı: Belirtiler, Tedavi ve Egzersizler | İhsan Eren", condition="Boyun fıtığı (servikal disk hernisi)", about=cond("Boyun fıtığı (servikal disk hernisi)", "cervical-disc-herniation"),
     faq_items=pick(BOYUN_FITIK_FAQ, 0, 1, 2, 3))
