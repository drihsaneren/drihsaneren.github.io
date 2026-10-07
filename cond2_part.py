# -*- coding: utf-8 -*-
# Yeni hastalık rehberleri: menisküs yırtığı, fibromiyalji, baş dönmesi (BPPV), ankilozan spondilit.
# rehab_part.py'den sonra exec edilir.

def _ex2(key, base, title, text, dose):
    SV[key] = SV[base]
    EXT[key] = (title, text, dose)

MOTION = '<path d="M20 42 H32 M16 54 H30 M20 66 H32" stroke="#B9CBC6" stroke-width="2.5" stroke-linecap="round"/>'
W_A = "M59 40 L50 56 L46 70"
W_B = "M59 40 L68 54 L76 64"
L_A = "M58 72 L70 92 L76 112"
L_B = "M58 72 L50 92 L42 112"
SV["walk"] = fig(GRD + MOTION +
    f'<path class="fig" d="{W_B}">{anim_d(f"{W_B};{W_A};{W_B}", dur="1.6s")}</path>'
    f'<path class="fig" d="{L_B}">{anim_d(f"{L_B};{L_A};{L_B}", dur="1.6s")}</path>'
    '<path class="fig" d="M60 32 L58 72"/>'
    f'<path class="fig hl" d="{L_A}">{anim_d(f"{L_A};{L_B};{L_A}", dur="1.6s")}</path>'
    f'<path class="fig" d="{W_A}">{anim_d(f"{W_A};{W_B};{W_A}", dur="1.6s")}</path>'
    '<circle class="hd" cx="61" cy="22" r="8"/><path d="M68 20 L73 23 L68 25 Z" fill="#2A6F6B"/>',
    "Tempolu yürüyüş")

WALL_L = '<path class="obj" d="M34 8 V112" stroke-width="5"/>'
SP_A, SP_B = "M42 76 Q52 58 48 40", "M42 76 Q41 58 42 40"
AR_A, AR_B = "M48 44 L56 60 L58 74", "M42 44 L48 60 L50 74"
SV["wallpost"] = fig(GRD + WALL_L +
    '<path class="fig" d="M42 76 L42 112 M42 76 L48 112"/>'
    f'<path class="fig hl" d="{SP_A}">{anim_d(f"{SP_A};{SP_B};{SP_A}", dur="4s")}</path>'
    f'<path class="fig" d="{AR_A}">{anim_d(f"{AR_A};{AR_B};{AR_A}", dur="4s")}</path>'
    f'<g>{anim_t("0 0;-8 -2;0 0", dur="4s")}<circle class="hd" cx="50" cy="30" r="8"/><path d="M57 28 L62 31 L57 33 Z" fill="#2A6F6B"/></g>'
    '<path d="M80 34 H66 M70 30 L66 34 L70 38" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    "Duvara yaslanarak dik duruş")

# ---- Epley manevrası (sağ kulak) ------------------------------------------------
BED = '<path class="obj" d="M8 88 H112 M12 88 V112 M108 88 V112"/>'
BED_S = '<path class="obj" d="M8 88 H80 M12 88 V112 M76 88 V112"/>'
PILLOW = '<rect x="24" y="79" width="22" height="9" rx="4" fill="#B9CBC6"/>'


def head_inset(a0, a1, label):
    """Sağ üstte yukarıdan görülen baş: burun yönü başın dönüş açısını gösterir (saat yönü = sağa)."""
    anim = ""
    if a0 != a1:
        anim = (f'<animateTransform attributeName="transform" type="rotate" values="{a0} 98 22;{a1} 98 22;{a1} 98 22" '
                'keyTimes="0;0.4;1" dur="4s" repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1;0 0 1 1"/>')
    return ('<circle cx="98" cy="22" r="15" fill="#ffffff" fill-opacity=".5" stroke="#B9CBC6" stroke-width="1.5"/>'
            '<path d="M98 8 V36" stroke="#B9CBC6" stroke-width="1.5" stroke-dasharray="2 3"/>'
            f'<g transform="rotate({a1} 98 22)">{anim}<circle class="hd" cx="98" cy="22" r="7"/>'
            '<path d="M94.5 16 L98 9.5 L101.5 16 Z" fill="#C8963E"/></g>'
            f'<text x="98" y="49" text-anchor="middle" font-size="10" font-weight="600" fill="#C8963E" '
            f'font-family="Figtree,system-ui,sans-serif">{label}</text>')


LYING = ('<path class="fig" d="M60 84 H102 M60 84 L34 77 M38 78 L52 84"/>'
         '<path class="fig" d="M34 77 L25 81"/><circle class="hd" cx="18" cy="82" r="7"/>')

SV["ep1"] = fig(GRD + BED + PILLOW +
    '<path class="fig" d="M60 84 H102 M60 84 L58 54 M58 58 L66 72 L72 82"/>'
    '<circle class="hd" cx="58" cy="45" r="8"/><path d="M65 43 L70 46 L65 48 Z" fill="#2A6F6B"/>'
    + head_inset(0, 45, "45°"), "Başı sağa çevirme")

SV["ep2"] = fig(GRD + BED + PILLOW +
    '<path class="fig" d="M60 84 H102"/>'
    '<g transform="rotate(0 60 84)"><animateTransform attributeName="transform" type="rotate" '
    'values="90 60 84;0 60 84;0 60 84" keyTimes="0;0.3;1" dur="4.5s" repeatCount="indefinite" '
    'calcMode="spline" keySplines="0.45 0 0.55 1;0 0 1 1"/>'
    '<path class="fig hl" d="M60 84 L34 77"/><path class="fig" d="M38 78 L52 84 M34 77 L25 81"/>'
    '<circle class="hd" cx="18" cy="82" r="7"/></g>'
    + head_inset(45, 45, "45°"), "Sırtüstü uzanma")

SV["ep3"] = fig(GRD + BED + PILLOW + LYING +
    '<path d="M6 66 A14 14 0 0 1 30 66 M26 61 L30 66 L24 68" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    + head_inset(45, -45, "90°"), "Başı sola çevirme")

SV["ep4"] = fig(GRD + BED + PILLOW +
    '<path class="fig" d="M60 84 L80 77 L100 84 M60 84 L34 77 M34 77 L25 81"/>'
    '<path class="fig hl" d="M40 76 L52 70 L60 76"/><circle class="hd" cx="18" cy="82" r="7"/>'
    '<path d="M36 60 Q58 44 80 58 M74 52 L80 58 L72 60" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    + head_inset(-45, -135, "90°"), "Sol yana dönme")

SV["ep5"] = fig(GRD + BED_S + PILLOW +
    '<path class="fig" d="M70 84 L86 86 L88 112 M70 84 L66 54 M66 58 L58 72 L54 84"/>'
    '<circle class="hd" cx="65" cy="45" r="8"/><path d="M72 43 L77 46 L72 48 Z" fill="#2A6F6B"/>'
    '<path d="M44 76 V54 M39 59 L44 54 L49 59" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round">'
    '<animate attributeName="opacity" values="0.2;1;0.2" dur="2s" repeatCount="indefinite"/></path>',
    "Sol taraftan oturma")

EXT.update({
 "walk": ("Tempolu yürüyüş", "Rahat ayakkabılarla, konuşabileceğiniz ama şarkı söyleyemeyeceğiniz bir tempoda yürüyün. Kötü günlerde süreyi kısaltın ama tamamen bırakmayın.", "5–10 dakikayla başlayın; her hafta birkaç dakika artırın"),
 "wallpost": ("Duvara yaslanarak dik duruş", "Sırtınızı duvara verin; topuklarınız, kalçanız ve kürek kemikleriniz duvara değsin. Çenenizi hafifçe içeri çekerek başınızın arkasını duvara yaklaştırın, 5 saniye tutun. Başınızın duvara ne kadar yaklaştığını zaman zaman kontrol etmek duruşunuzu izlemenize yardım eder.", "10 tekrar, her gün"),
 "ep1": ("1. Başınızı sağa çevirin", "Yatağın üzerinde, bacaklarınız önde uzanmış olarak oturun. Arkanızda, uzandığınızda omuzlarınızın altına gelecek bir yastık olsun. Başınızı 45 derece sağa çevirin.", "Başlangıç pozisyonu"),
 "ep2": ("2. Hızla sırtüstü uzanın", "Başınız sağa dönük kalacak şekilde hızla sırtüstü uzanın. Omuzlarınız yastıkta, başınız hafifçe geriye düşmüş ve yatağa değiyor olsun. Baş dönmesi olabilir; geçmesini bekleyin.", "En az 30 saniye, baş dönmesi geçene kadar"),
 "ep3": ("3. Başınızı sola çevirin", "Başınızı kaldırmadan 90 derece sola çevirin. Artık 45 derece sola bakıyor olacaksınız.", "En az 30 saniye"),
 "ep4": ("4. Sol yanınıza dönün", "Başınızla birlikte gövdenizi de 90 derece sola, yatağın içine doğru çevirin. Yüzünüz aşağıya, yatağa doğru bakacak.", "En az 30 saniye"),
 "ep5": ("5. Sol taraftan oturun", "Yavaşça sol tarafınızdan yatağın kenarına oturun. Birkaç dakika oturarak bekleyin, hemen ayağa kalkmayın.", "Günde 3 kez, 24 saat baş dönmesi olmayana kadar"),
})
_ex2("ep6", "tandem", "Denge egzersizi", "Baş dönmesi geçtikten sonra da bir süre dengesizlik hissi kalabilir. Tezgâha hafifçe tutunarak bir ayağınızı diğerinin tam önüne koyun ve dengede durun. Kolaylaştıkça tutunmayı azaltın.", "30 saniye, 3 kez")

# ============================================================== MENİSKÜS YIRTIĞI
_ex2("mn_quad", "quad", "Havluya bastırma", "Sırtüstü uzanın, dizinizin altına rulo yapılmış bir havlu koyun. Dizinizin arkasını havluya bastırarak uyluğunuzun ön kasını sıkın, 5 saniye tutun ve gevşeyin. Ağrılı dönemde de yapılabilir.", "10 tekrar, günde 3 kez")
_ex2("mn_slr", "slr", "Düz bacak kaldırma", "Sırtüstü uzanın, diğer dizinizi bükün. Uyluğunuzu sıkıp dizinizi düz tutarak bacağınızı diğer dizinizin hizasına kadar kaldırın, 2–3 saniye bekleyip yavaşça indirin.", "10 tekrar, 2–3 set")
_ex2("mn_kext", "kext", "Oturarak diz açma", "Sandalyeye dik oturun. Dizinizi yavaşça düzeltip uyluğunuzun ön kasını sıkın, 3 saniye tutun ve yavaşça indirin. Kolaylaştıkça ayak bileğinize hafif bir ağırlık ekleyebilirsiniz.", "10 tekrar, 2–3 set")
_ex2("mn_bridge", "bridge", "Köprü", "Sırtüstü yatın, dizleriniz bükülü, ayaklarınız yerde. Kalçanızı sıkarak yavaşça kaldırın, 2–3 saniye bekleyip indirin.", "10 tekrar, 2 set")
_ex2("mn_wall", "wall", "Duvarda yarım çömelme", "Sırtınızı duvara dayayın, ayaklarınız duvardan bir adım önde olsun. Dizlerinizi en fazla yarım çömelme kadar bükerek sırtınızı aşağı kaydırın, birkaç saniye bekleyip yukarı çıkın. Ağrı artıyorsa daha az bükün.", "8–10 tekrar, 2 set")
_ex2("mn_sls", "sls", "Tek ayak üzerinde denge", "Mutfak tezgâhına hafifçe tutunarak tek ayağınızın üzerinde durun, dizinizi hafifçe bükülü tutun. Kolaylaştıkça tutunmayı azaltın.", "30 saniye, her bacakta 3 kez")

MN_FAQ = [
 ("MR'ımda menisküs yırtığı çıktı, ameliyat olmam gerekiyor mu?", "Çoğu zaman hayır. 50 yaşın üzerinde MR'da menisküs yırtığı çok sık görülür ve bu kişilerin yarısından fazlasında hiç diz şikâyeti yoktur. Yıpranmaya bağlı yırtıklarda egzersiz tedavisi, çalışmalarda ameliyat kadar etkili bulundu. Karar MR görüntüsüne göre değil, şikâyetlerinize ve muayeneye göre verilir."),
 ("Menisküs kendiliğinden iyileşir mi?", "Menisküsün yalnızca dış kenarı kanlanır; bu bölgedeki küçük yırtıklar iyileşebilir, iç kısımdaki yırtıklar ise genellikle kendiliğinden kaynamaz. Ancak yırtık yerinde kalsa bile ağrı ve işlev çoğu zaman egzersizle belirgin şekilde düzelir."),
 ("Dizim takılıyor ya da kilitleniyor, ne yapmalıyım?", "Kısa süreli takılma hissi sık görülür ve çoğu zaman egzersizle azalır. Dizin bir konumda takılıp kalması ve düzeltilememesi ise yırtık bir parçanın eklemin arasına sıkışmasına bağlı olabilir. Bu durumda bir ortopedi uzmanına başvurun."),
 ("Koşabilir, spor yapabilir miyim?", "Ağrı ve şişlik kontrol altına alınıp uyluk kas gücü diğer bacağa yaklaştığında sporlara kademeli olarak dönülebilir. Önce yürüyüş, bisiklet ve yüzme gibi düşük yüklü aktivitelerle başlayın; zıplama ve ani dönüş gerektiren sporları en sona bırakın."),
]

MN_SRC = [
 "Englund M, Guermazi A, Gale D, et al. " + ext("https://www.nejm.org/doi/full/10.1056/NEJMoa0800777", "Incidental meniscal findings on knee MRI in middle-aged and elderly persons") + ". N Engl J Med. 2008;359(11):1108-1115.",
 "Kise NJ, Risberg MA, Stensrud S, et al. " + ext("https://pmc.ncbi.nlm.nih.gov/articles/PMC5136715/", "Exercise therapy versus arthroscopic partial meniscectomy for degenerative meniscal tear in middle aged patients: randomised controlled trial with two year follow-up") + ". BMJ. 2016;354:i3740.",
 "van de Graaf VA, Noorduyn JCA, Willigenburg NW, et al. " + ext("https://pubmed.ncbi.nlm.nih.gov/30285177/", "Effect of early surgery vs physical therapy on knee function among patients with nonobstructive meniscal tears: the ESCAPE randomized clinical trial") + ". JAMA. 2018;320(13):1328-1337.",
 "Noorduyn JCA, van de Graaf VA, Willigenburg NW, et al. " + ext("https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2794027", "Effect of physical therapy vs arthroscopic partial meniscectomy in people with degenerative meniscal tears: five-year follow-up of the ESCAPE randomized clinical trial") + ". JAMA Netw Open. 2022.",
 "Siemieniuk RAC, Harris IA, Agoritsas T, et al. " + ext("https://www.bmj.com/content/357/bmj.j1982", "Arthroscopic surgery for degenerative knee arthritis and meniscal tears: a clinical practice guideline") + ". BMJ. 2017;357:j1982.",
]

MN_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Menisküs yırtığı</h1>
    <p class="lede">Menisküs, dizde uyluk kemiği ile kaval kemiği arasında yastık görevi gören C şeklindeki kıkırdaktır. Gençlerde çoğunlukla dizin burkulmasıyla, 40 yaşından sonra ise çoğunlukla yıpranmayla yırtılır. Yıpranmaya bağlı yırtıklarda egzersiz tedavisi, çalışmalarda ameliyat kadar etkili bulunuyor.</p>
    <p class="meta">Son güncelleme: 29 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%61</b><span>MR'da menisküs yırtığı görülen 50 yaş üstü kişilerde son bir ayda hiç diz şikâyeti olmayanlar</span></div>
        <div class="stat"><b>%19–56</b><span>50–90 yaş arasında MR'da menisküs yırtığı görülme sıklığı; yaşa ve cinsiyete göre değişiyor</span></div>
        <div class="stat"><b>12 hafta</b><span>İki yıllık takipte ameliyat kadar etkili bulunan denetimli egzersiz programının süresi</span></div>
        <div class="stat"><b>5 yıl</b><span>Fizyoterapinin ameliyattan geri kalmadığını gösteren ESCAPE çalışmasının takip süresi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Burkulma mı, yıpranma mı?</h2>
        <p class="soft">Her dizde iç ve dış olmak üzere iki menisküs bulunur. Yük dağıtır, eklemi korur ve dize denge sağlar. Gençlerde ve sporcularda yırtık çoğunlukla ayak yerdeyken dizin dönmesiyle oluşur; ön çapraz bağ yaralanmasıyla birlikte olabilir. 40 yaşından sonra ise belirgin bir olay olmadan, yıpranmayla ortaya çıkan yırtıklar daha sıktır ve çoğu zaman kireçlenmenin erken bir parçasıdır.</p>
        <p class="soft">MR'da yırtık görülmesi, ağrının nedeninin o yırtık olduğu anlamına gelmez: 50–90 yaş arasında şikâyeti olmayan pek çok kişide de menisküs yırtığı bulunur.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Dizin iç ya da dış yan tarafında, eklem çizgisi boyunca ağrı</li>
          <li>Şişlik; burkulmadan birkaç saat sonra ya da ertesi gün ortaya çıkabilir</li>
          <li>Çömelirken, dönerken ve merdiven inerken artan ağrı</li>
          <li>Takılma hissi ya da dizin tam açılamaması</li>
          <li>Dizin boşalması, güvensizlik hissi</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ameliyat mı, egzersiz mi?</h2>
      <p class="soft">Norveç'te 35–60 yaş arası, yıpranmaya bağlı menisküs yırtığı olan 140 kişiyle yapılan bir çalışmada 12 haftalık denetimli egzersiz programı ile artroskopik menisküs kesimi (parsiyel menisektomi) karşılaştırıldı. İki yılın sonunda iki grup arasında anlamlı bir fark bulunmadı; egzersiz grubunda uyluk kas gücü ise daha fazla arttı.</p>
      <p class="soft">Hollanda'da 45–70 yaş arası 321 hastayla yapılan ESCAPE çalışmasında da fizyoterapi, hem 2 yılda hem 5 yılda ameliyattan geri kalmadı ve iki grupta kireçlenmenin ilerlemesi benzerdi. Fizyoterapi grubundaki hastaların yaklaşık üçte biri sonradan ameliyat olmayı seçti.</p>
      <div class="callout">
        <p>Uluslararası bir uzman panelinin 2017'de BMJ'de yayımlanan kılavuzu, yıpranmaya bağlı diz sorunlarında (menisküs yırtığı dahil) artroskopik ameliyatın yapılmamasını güçlü şekilde öneriyor. Ani bir yaralanmadan sonra ortaya çıkan yırtıklar ve dizin kilitlenip açılamadığı durumlar ise bir ortopedi uzmanınca ayrıca değerlendirilir.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <ul class="tx">
        <li><b>Egzersiz</b><span>Uyluğun ön ve arka kasları ile kalça kaslarını güçlendiren, denge ve diz kontrolünü geliştiren egzersizler tedavinin temelidir. Çalışmalarda programlar genellikle 12 hafta sürdü.</span></li>
        <li><b>Yükü ayarlama</b><span>Ağrıyı belirgin artıran derin çömelme, diz üstü oturma ve ani dönüşler bir süre azaltılır; yürüyüş ve günlük hareket sürdürülür.</span></li>
        <li><b>Ağrı kontrolü</b><span>Soğuk uygulama ve hekiminizin önerdiği ağrı kesiciler ağrılı dönemde egzersize devam etmeyi kolaylaştırır.</span></li>
        <li><b>Kilo kontrolü</b><span>Fazla kiloların verilmesi diz ekleminin yükünü azaltır.</span></li>
        <li><b>Ameliyat</b><span>Kilitlenen diz, genç hastalarda travmatik yırtıklar ve düzenli egzersize rağmen düzelmeyen şikâyetler ortopedi uzmanıyla değerlendirilir. Bazı yırtıklar kesilmek yerine dikilerek onarılabilir.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Menisküs için altı egzersiz</h2>
      <p class="soft">Egzersiz sırasında hafif ve katlanılabilir bir ağrı olabilir; ağrı ve şişlik ertesi gün artmıyorsa devam edin. Yeni bir yaralanmadan sonraki ilk günlerde hareketleri zorlamadan yapın.</p>
      {ex_grid(["mn_quad", "mn_slr", "mn_kext", "mn_bridge", "mn_wall", "mn_sls"])}
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Menisküs ve diz için videolar</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("ucUGxOHdDvQ", "Menisküs egzersizleri videosunu oynat", "Meniscus Tear Top 3 Rehab Exercises")}
          <h3>Menisküs yırtığında üç temel egzersiz</h3>
          <p>Menisküs yırtığından sonra rehabilitasyonun ilk adımları.</p>
        </div>
        <div class="vid">
          {vbox("iL-swm4th_o", "Ameliyatsız tedavi videosunu oynat", "Treating Knee Arthritis Without Surgery")}
          <h3>Ameliyatsız diz tedavisi</h3>
          <p>Yıpranmaya bağlı diz sorunlarında ameliyatsız tedavi yaklaşımı.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(MN_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Dizin kilitlenip düzeltilememesi</li>
        <li>Yaralanmadan sonraki ilk saatlerde dizin hızla ve belirgin şişmesi ya da bacağa hiç yük verememe</li>
        <li>Dizde kızarıklık, sıcaklık ve ateş</li>
        <li>Baldırda şişlik, ağrı ve kızarıklık</li>
        <li>Dizin sık sık boşalması, düşmelere yol açması</li>
      </ul>
      {CTA_CARD("Diz ağrınız", "menisküs yırtığı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(MN_SRC)}
    </div>
  </section>
</main>'''

page("menisku-yirtigi.html", "Menisküs Yırtığı",
     "Menisküs yırtığı nedir, her yırtık ameliyat gerektirir mi? MR bulgusu ne anlama gelir, egzersiz ne kadar etkili? Evde altı egzersiz, videolar ve uyarı işaretleri.",
     "menisku-yirtigi.html", NECK_CSS, MN_BODY, YT_JS,
     seo_title="Menisküs Yırtığı: Ameliyat Gerekir mi? Tedavi ve Egzersizler | İhsan Eren",
     condition="Menisküs yırtığı", faq_items=MN_FAQ)

# ============================================================== FİBROMİYALJİ
_ex2("fb_sts", "sts", "Sandalyeden kalkıp oturma", "Sağlam bir sandalyenin önüne oturun. Ayağa kalkın ve kontrollü şekilde oturun. Zorlanıyorsanız ellerinizden destek alın.", "5–10 tekrar, 1–2 set")
_ex2("fb_row", "row", "Lastik bantla kürek çekme", "Lastik bandı göğüs hizasında sağlam bir yere bağlayın. Dirseklerinizi gövdenize yakın tutarak bandı geriye çekin, kürek kemiklerinizi birbirine yaklaştırın ve yavaşça bırakın. Hafif bir bantla başlayın.", "8–10 tekrar, 1–2 set")
_ex2("fb_bridge", "bridge", "Köprü", "Sırtüstü yatın, dizleriniz bükülü, ayaklarınız yerde. Kalçanızı sıkarak yavaşça kaldırın, 2–3 saniye bekleyip indirin.", "8–10 tekrar")
_ex2("fb_cat", "cat", "Kedi-deve", "Ellerinizin ve dizlerinizin üzerinde durun. Nefes verirken sırtınızı yukarı doğru yuvarlayın, nefes alırken belinizi yavaşça aşağı bırakın. Hareketi yavaş ve rahat bir aralıkta yapın.", "8–10 tekrar")
_ex2("fb_side", "side", "Boyun yana germe", "Dik oturun. Bir elinizle sandalyenin kenarını tutun ve kulağınızı karşı omzunuza doğru yavaşça yaklaştırın. Boynunuzun yanında hafif bir gerginlik hissedin; omzunuzu kaldırmayın.", "20–30 saniye, her iki yana 2 kez")

FB_FAQ = [
 ("Fibromiyalji gerçek bir hastalık mı?", "Evet. Ağrı gerçektir; ancak kaynağı kaslarda ya da eklemlerde bir hasar değil, sinir sisteminin ağrı sinyallerini işleme biçimindeki değişikliktir. Bu yüzden kan tahlilleri ve görüntülemeler çoğunlukla normal çıkar."),
 ("Egzersiz yapınca ağrım artıyor, yine de devam etmeli miyim?", "Evet, ama dozu ayarlayarak. İlk haftalarda hafif bir artış olağandır ve vücut alıştıkça azalır. Ağrı ertesi gün belirgin şekilde artmışsa bir sonraki seansta süreyi ve yoğunluğu azaltın; tamamen bırakmayın."),
 ("Hangi egzersiz daha iyi?", "Düzenli yapabileceğiniz egzersiz. Aerobik egzersizin, güçlendirmenin ve su içi egzersizin faydası gösterildi; tai chi de bir çalışmada aerobik egzersiz kadar ya da daha etkili bulundu. Yürüyüşü birkaç güçlendirme hareketiyle birleştirmek iyi bir başlangıçtır."),
 ("Fibromiyalji geçer mi?", "Genellikle uzun süreli bir durumdur ve şikâyetler dönem dönem artıp azalabilir. Düzenli egzersiz, uyku düzeni ve ağrıyla başa çıkma becerileriyle belirtiler çoğu zaman belirgin şekilde hafifler."),
]

FB_SRC = [
 "Macfarlane GJ, Kronisch C, Dean LE, et al. " + ext("https://abdn.elsevierpure.com/en/publications/eular-revised-recommendations-for-the-management-of-fibromyalgia/", "EULAR revised recommendations for the management of fibromyalgia") + ". Ann Rheum Dis. 2017;76(2):318-328.",
 "Bidonde J, Busch AJ, Schachter CL, et al. " + ext("https://www.cochrane.org/CD012700/MUSKEL_aerobic-exercise-adults-fibromyalgia", "Aerobic exercise training for adults with fibromyalgia") + ". Cochrane Database Syst Rev. 2017;6:CD012700.",
 "Wang C, Schmid CH, Fielding RA, et al. " + ext("https://www.nccih.nih.gov/research/research-results/tai-chi-has-similar-or-greater-benefits-than-aerobic-exercise-for-fibromyalgia-study-shows", "Effect of tai chi versus aerobic exercise for fibromyalgia: comparative effectiveness randomized controlled trial") + ". BMJ. 2018;360:k851.",
 "Deare JC, Zheng Z, Xue CCL, et al. " + ext("https://www.cochrane.org/CD007070/MUSKEL_acupuncture-for-fibromyalgia", "Acupuncture for treating fibromyalgia") + ". Cochrane Database Syst Rev. 2013;(5):CD007070.",
 "Heidari F, Afshari M, Moosazadeh M. " + ext("https://link.springer.com/article/10.1007/s00296-017-3725-2", "Prevalence of fibromyalgia in general population and patients, a systematic review and meta-analysis") + ". Rheumatol Int. 2017;37(9):1527-1539.",
]

FB_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Fibromiyalji</h1>
    <p class="lede">Vücudun birçok yerinde süren yaygın ağrı, yorgunluk ve dinlendirmeyen uykuyla seyreden bir durumdur. Ağrı gerçektir, ama kaslarda ya da eklemlerde bir hasar yoktur; sinir sisteminin ağrıyı işleme biçimi değişmiştir. Tedavide en güçlü kanıta sahip yöntem egzersizdir.</p>
    <p class="meta">Son güncelleme: 29 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%2</b><span>Toplumda fibromiyalji görülme sıklığı; kadınlarda çok daha sık</span></div>
        <div class="stat"><b>Tek</b><span>Avrupa Romatoloji Birliği (EULAR) önerilerinde güçlü öneri alan tek tedavi: egzersiz</span></div>
        <div class="stat"><b>107</b><span>EULAR'ın önerilerini hazırlarken incelediği sistematik derleme sayısı</span></div>
        <div class="stat"><b>226</b><span>Tai chi'nin aerobik egzersiz kadar ya da daha etkili bulunduğu çalışmadaki hasta sayısı</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Fibromiyaljide beyin ve omurilik ağrı sinyallerine karşı aşırı duyarlı hale gelir; normalde rahatsız etmeyecek uyarılar ağrılı algılanır. Neden tam olarak bilinmiyor; genetik yatkınlık, uzun süreli stres, uyku bozukluğu, geçirilmiş enfeksiyonlar ya da başka ağrılı hastalıklar tetikleyici olabilir.</p>
        <p class="soft">Tanı; belirtilerin en az 3 aydır sürmesi, muayene ve benzer belirtilere yol açabilecek diğer hastalıkların (tiroit hastalıkları, romatizmal hastalıklar, vitamin eksiklikleri gibi) dışlanmasıyla konur. Tanıyı koyduracak tek bir kan testi ya da görüntüleme yoktur.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Vücudun iki yanında, belin üstünde ve altında süren yaygın ağrı</li>
          <li>Dinlenmekle geçmeyen yorgunluk, dinlendirmeyen uyku</li>
          <li>Sabah tutukluğu</li>
          <li>Dikkat ve bellek güçlüğü</li>
          <li>Baş ağrısı, huzursuz bağırsak, kaygı ve çökkünlük eşlik edebilir</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Egzersiz neden temel tedavi?</h2>
      <p class="soft">Avrupa Romatoloji Birliği (EULAR) 2016'da güncellediği önerilerini hazırlarken 107 sistematik derlemeyi inceledi. Güçlü öneri alan tek tedavi egzersiz oldu. Psikolojik destek, tai chi ve yoga gibi hareket temelli uygulamalar ve şiddetli ağrı ya da uyku sorunu olanlarda ilaç tedavisi daha zayıf öneriler aldı.</p>
      <p class="soft">13 çalışmayı ve 839 kişiyi kapsayan Cochrane derlemesinde aerobik egzersiz yaşam kalitesini, günlük işlevi ve ağrıyı iyileştirdi. ABD'de 226 fibromiyalji hastasıyla yapılan bir çalışmada ise haftada bir ya da iki kez yapılan tai chi, aerobik egzersiz kadar ya da daha fazla fayda sağladı; en iyi sonuç 24 hafta boyunca haftada iki kez yapılan tai chi ile alındı.</p>
      <div class="callout">
        <p>Fibromiyaljide egzersizin püf noktası “az başla, yavaş artır” ilkesidir. Birkaç dakikalık yürüyüşle başlayın ve süreyi her hafta biraz artırın. İlk haftalarda ağrının biraz artması olağandır ve genellikle geçicidir; kötü günlerde bırakmak yerine azaltın.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <ul class="tx">
        <li><b>Bilgilendirme</b><span>Durumun ne olduğunu ve neden ağrıdığını anlamak, ağrıyla ilgili kaygıyı azaltır ve tedavinin ilk adımıdır.</span></li>
        <li><b>Egzersiz</b><span>Yürüyüş, bisiklet ya da su içi egzersiz gibi aerobik egzersizler; güçlendirme ve esneme hareketleriyle birlikte.</span></li>
        <li><b>Hareket temelli uygulamalar</b><span>Tai chi, yoga ve qigong hem hareket hem gevşeme sağlar.</span></li>
        <li><b>Uyku düzeni</b><span>Düzenli uyku saatleri ve uyku alışkanlıkları ağrıyı ve yorgunluğu etkiler. Ayrıntılar için <a href="uyku.html">iyi uyku rehberine</a> bakın.</span></li>
        <li><b>Psikolojik destek</b><span>Bilişsel davranışçı terapi ve ağrıyla başa çıkma becerileri, özellikle kaygı ve çökkünlük eşlik ediyorsa faydalıdır. <a href="stres.html">Stres rehberi</a> de yardımcı olabilir.</span></li>
        <li><b>İlaç</b><span>Şiddetli ağrı ya da uyku sorunu olanlarda hekim tarafından bazı ilaçlar düşük dozda başlanabilir.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Az ve yavaş başlayan altı egzersiz</h2>
      <p class="soft">Kendinizi iyi hissettiğiniz bir saati seçin ve hareketleri ağrıyı belirgin artırmayacak bir tempoda yapın. Güçlendirme hareketlerini haftada 2–3 gün, yürüyüşü mümkünse her gün yapın.</p>
      {ex_grid(["walk", "fb_sts", "fb_row", "fb_bridge", "fb_cat", "fb_side"])}
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Tai chi'ye başlangıç</h2>
      <p class="soft">Avustralyalı hekim ve tai chi eğitmeni Dr. Paul Lam'in YouTube kanalından. Video İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("tAOuEpa01j4", "Tai chi başlangıç videosunu oynat", "Tai Chi for Arthritis | Dr Paul Lam | Free Lesson and Introduction")}
          <h3>Eklem dostu tai chi dersi</h3>
          <p>Yavaş ve akıcı hareketlerle tai chi'ye giriş.</p>
        </div>
      </div>
      <p class="meta">Video Dr. Paul Lam'e aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Akupunktur: araştırmalar ve klinik gözlemim</h2>
      <p class="soft">Dokuz çalışmayı (395 kişi) inceleyen Cochrane derlemesinde, ilaç ve egzersizden oluşan standart tedaviye eklenen akupunktur ağrıyı 100 üzerinden yaklaşık 30 puan azalttı. İğnelerden hafif elektrik verilen akupunktur, sahte uygulamaya göre de ağrıyı bir miktar azalttı; elle yapılan akupunkturda bu fark görülmedi. Etki yaklaşık bir ay sürdü, altıncı ayda korunmadı. Kanıt düzeyi düşük–orta; yan etkiler hafif ve kısa süreliydi.</p>
      {OBS("Kendi klinik gözlemimde akupunkturun fibromiyaljide çok etkili olduğunu gördüm.")}
      <div class="callout">
        <p>{ACU_LAW}</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(FB_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlar fibromiyalji dışında bir soruna işaret edebilir. Beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Eklemlerde şişlik, kızarıklık ve sıcaklık</li>
        <li>Ateş, gece terlemesi ya da nedensiz kilo kaybı</li>
        <li>Kas gücünde azalma; merdiven çıkmakta ya da kolları kaldırmakta giderek artan güçlük</li>
        <li>Yeni başlayan uyuşma ya da idrar ve dışkı kontrolünde sorun</li>
        <li>Yoğun umutsuzluk ya da kendinize zarar verme düşünceleri (acil durumda <strong>112</strong>)</li>
      </ul>
      {CTA_CARD("Fibromiyalji ağrınız", "fibromiyalji")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(FB_SRC)}
    </div>
  </section>
</main>'''

page("fibromiyalji.html", "Fibromiyalji",
     "Fibromiyalji nedir, neden ağrır, nasıl tedavi edilir? Güçlü öneri alan tek tedavi olan egzersize nasıl başlanır? Evde altı egzersiz, tai chi videosu ve uyarı işaretleri.",
     "fibromiyalji.html", NECK_CSS, FB_BODY, YT_JS,
     seo_title="Fibromiyalji: Belirtiler, Tedavi ve Egzersizler | İhsan Eren",
     condition="Fibromiyalji", faq_items=FB_FAQ)

# ============================================================== BAŞ DÖNMESİ (BPPV)
BP_FAQ = [
 ("Baş dönmem geçti ama yeniden başladı, normal mi?", "BPPV tekrarlayabilir. Belirtiler aynıysa aynı manevra genellikle yine işe yarar. Sık tekrarlıyorsa ya da belirtiler değiştiyse yeniden değerlendirilmeniz gerekir; kılavuz tedaviden sonra bir ay içinde yeniden değerlendirme öneriyor."),
 ("Hangi kulağımın etkilendiğini nasıl bilebilirim?", "Kesin olarak Dix-Hallpike testiyle anlaşılır. Etkilenen kulak tarafına dönerek yatınca baş dönmesi genellikle daha belirgin olur, ama bu tek başına yeterli değildir. Yanlış tarafa yapılan manevra işe yaramaz; bu yüzden ilk değerlendirmenin bir uzman tarafından yapılması önerilir."),
 ("Manevradan sonra dik oturmam ya da başımı hareket ettirmemem gerekiyor mu?", "Hayır. Kılavuz, manevradan sonra hareket kısıtlaması önermiyor; bu tür kısıtlamaların sonuca ek bir katkısı gösterilmedi."),
 ("Baş dönmesi ilacı kullanmalı mıyım?", "Genellikle hayır. Kılavuz, baş dönmesi ilaçlarının BPPV'de rutin olarak kullanılmamasını öneriyor; bu ilaçlar kristalleri yerine götürmez. Şiddetli bulantıda kısa süreli kullanım için hekiminize danışabilirsiniz."),
]

BP_SRC = [
 "Bhattacharyya N, Gubbels SP, Schwartz SR, et al. " + ext("https://aao-hnsfjournals.onlinelibrary.wiley.com/doi/10.1177/0194599816689667", "Clinical practice guideline: benign paroxysmal positional vertigo (update)") + ". Otolaryngol Head Neck Surg. 2017;156(3 Suppl):S1-S47.",
 "Hilton MP, Pinder DK. " + ext("https://www.cochrane.org/evidence/CD003162_epley-manoeuvre-benign-paroxysmal-positional-vertigo-bppv", "The Epley (canalith repositioning) manoeuvre for benign paroxysmal positional vertigo") + ". Cochrane Database Syst Rev. 2014;(12):CD003162.",
 "Radtke A, von Brevern M, Tiel-Wilck K, et al. " + ext("https://www.neurology.org/doi/10.1212/01.WNL.0000130250.62842.C9", "Self-treatment of benign paroxysmal positional vertigo: Semont maneuver vs Epley procedure") + ". Neurology. 2004;63(1):150-152.",
 "von Brevern M, Radtke A, Lezius F, et al. " + ext("https://pubmed.ncbi.nlm.nih.gov/17135456/", "Epidemiology of benign paroxysmal positional vertigo: a population based study") + ". J Neurol Neurosurg Psychiatry. 2007;78(7):710-715.",
 "Johns Hopkins Medicine. " + ext("https://www.hopkinsmedicine.org/health/treatment-tests-and-therapies/home-epley-maneuver", "Home Epley maneuver") + ".",
]

BP_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Pozisyonel baş dönmesi (BPPV)</h1>
    <p class="lede">Yatağa uzanırken, yatakta dönerken ya da yukarı bakarken birden başlayan ve genellikle bir dakikadan kısa süren dönme hissi, çoğunlukla iç kulaktaki küçük kristallerin yer değiştirmesinden kaynaklanır. Baş dönmesinin en sık nedenidir ve basit bir baş manevrasıyla çoğu zaman düzelir.</p>
    <p class="meta">Son güncelleme: 29 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%2,4</b><span>Hayatı boyunca BPPV yaşayan kişilerin oranı</span></div>
        <div class="stat"><b>%56</b><span>Epley manevrasıyla baş dönmesi tamamen geçenler; manevra yapılmayanlarda %21</span></div>
        <div class="stat"><b>%95</b><span>Manevrayı kendisi uygulamayı öğrenen hastalarda bir hafta sonra iyileşme oranı</span></div>
        <div class="stat"><b>30 sn</b><span>Epley manevrasının her adımında en az bekleme süresi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">İç kulakta dengeyi algılayan, sıvıyla dolu üç yarım daire kanalı bulunur. İç kulağın başka bir bölümündeki küçük kalsiyum kristalleri yerinden koparak bu kanallardan birine, çoğunlukla arka kanala kaçabilir. Baş pozisyon değiştirdiğinde kristaller kanaldaki sıvıyı hareket ettirir ve beyin, gerçekte olmayan bir dönme algılar.</p>
        <p class="soft">Yaşla birlikte sıklaşır; baş darbesinden sonra da ortaya çıkabilir. Çoğu zaman belirgin bir neden bulunmaz.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Yatağa uzanırken, yatakta dönerken ya da yataktan kalkarken başlayan dönme hissi</li>
          <li>Yukarı bakınca ya da öne eğilince tetiklenmesi</li>
          <li>Genellikle bir dakikadan kısa sürmesi</li>
          <li>Bulantı ve dengesizlik hissi</li>
          <li>İşitme kaybı ya da başka nörolojik belirti olmaması</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tanı ve tedavi</h2>
      <p class="soft">Tanı, Dix-Hallpike testiyle konur: hekim ya da fizyoterapist başınızı belli bir açıyla çevirip sizi hızla sırtüstü yatırır ve gözlerinizde oluşan karakteristik hareketi izler. Test hangi kulağın etkilendiğini de gösterir. Amerikan Kulak Burun Boğaz Akademisi'nin kılavuzu, tanı ölçütlerini karşılayan hastalarda rutin olarak MR ya da tomografi çekilmemesini öneriyor.</p>
      <p class="soft">Tedavi, kristalleri kanaldan çıkarıp ait oldukları yere geri götüren yeniden konumlandırma manevralarıdır; en bilineni Epley manevrasıdır. 11 çalışmayı ve 745 hastayı kapsayan Cochrane derlemesinde baş dönmesi tamamen geçenlerin oranı Epley yapılanlarda %56, sahte manevra ya da tedavi uygulanmayanlarda %21 oldu ve ciddi bir yan etki görülmedi. Tek bir Epley manevrası, bir hafta boyunca günde üç kez yapılan Brandt-Daroff egzersizlerinden daha etkiliydi.</p>
      <div class="callout">
        <p>Kılavuz, baş dönmesi ilaçlarının (antihistaminikler, sakinleştiriciler) BPPV tedavisinde rutin olarak kullanılmamasını öneriyor. Bu ilaçlar kristalleri yerine götürmez, dengeyi daha da bozabilir ve özellikle yaşlılarda düşme riskini artırabilir.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde uygulama</p>
      <h2>Sağ kulak için Epley manevrası: adım adım</h2>
      <p class="soft">Etkilenen kulak testle belirlendikten sonra manevra evde de uygulanabilir. Aşağıdaki adımlar sağ kulak içindir; sol kulakta başınızı ve gövdenizi ters yöne çevirerek aynı adımları uygulayın. Baş dönmesi olabileceği için ilk uygulamalarda yanınızda biri bulunsun. Çizimlerin sağ üst köşesindeki küçük daire, başınızın yukarıdan görünüşünü ve dönüş açısını gösterir.</p>
      {ex_grid(["ep1", "ep2", "ep3", "ep4", "ep5", "ep6"])}
      <div class="callout" style="margin-top:22px">
        <p>Kendi başına uygulamayı öğrenen 70 hastalık bir çalışmada, Epley manevrasını evde uygulayanların %95'inde bir hafta içinde baş dönmesi geçti. Boyun ya da sırt hastalığınız, damar hastalığınız ya da retina yırtığı öykünüz varsa manevrayı uygulamadan önce hekiminize danışın.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(BP_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda baş dönmesi BPPV'den değil, inme (felç) gibi acil bir durumdan kaynaklanıyor olabilir. Beklemeden <strong>112</strong>'yi arayın:</p>
      <ul class="dots redflags">
        <li>Baş dönmesiyle birlikte konuşma bozukluğu, yüzde kayma, kol ya da bacakta güçsüzlük veya uyuşma</li>
        <li>Çift görme ya da yutma güçlüğü</li>
        <li>Ani ve çok şiddetli baş ya da boyun ağrısı</li>
        <li>Yürüyememe, ayakta duramama</li>
        <li>Baş pozisyonundan bağımsız, saatlerce ya da günlerce kesintisiz süren baş dönmesi</li>
        <li>Ani işitme kaybı</li>
      </ul>
      {CTA_CARD("Baş dönmeniz", "pozisyonel baş dönmesi (BPPV)")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(BP_SRC)}
    </div>
  </section>
</main>'''

page("bas-donmesi.html", "Baş Dönmesi (BPPV)",
     "Yatarken, dönerken ya da yukarı bakınca başlayan kısa süreli baş dönmesi: BPPV nedir, Epley manevrası nasıl yapılır, ne zaman acil başvurmalı? Adım adım çizimler ve kanıtlar.",
     "bas-donmesi.html", NECK_CSS, BP_BODY, "",
     seo_title="Baş Dönmesi (BPPV): Epley Manevrası Adım Adım | İhsan Eren",
     condition="Benign paroksismal pozisyonel vertigo (BPPV)", faq_items=BP_FAQ)

# ============================================================== ANKİLOZAN SPONDİLİT
_ex2("as_chin", "chin", "Çene içe çekme", "Dik oturun ya da durun, gözleriniz karşıya baksın. Başınızı eğmeden çenenizi düz bir çizgide geriye çekin; ensenizin uzadığını hissedin. 5 saniye tutup bırakın.", "10 tekrar, günde 2 kez")
_ex2("as_thor", "thor", "Göğüs kafesini açma", "Sırtı alçak bir sandalyeye oturun, ellerinizi ensenizde birleştirin. Göğsünüzü tavana doğru kaldırarak sırtınızı sandalyenin üst kenarı üzerinden hafifçe geriye esnetin. Bu sırada derin bir nefes alın.", "10 tekrar, her gün")
_ex2("as_cat", "cat", "Kedi-deve", "Ellerinizin ve dizlerinizin üzerinde durun. Nefes verirken sırtınızı yukarı doğru yuvarlayın, nefes alırken belinizi aşağı bırakıp başınızı kaldırın. Hareketi tüm omurganızla, yavaş yapın.", "10 tekrar, her gün")
_ex2("as_press", "pressup", "Yüzüstü doğrulma", "Yüzüstü uzanın. Dirseklerinizi omuzlarınızın altına getirip göğsünüzü yavaşça yerden kaldırın, kalçanız yerde kalsın. Birkaç saniye tutup yavaşça inin. Öne eğilen duruşa karşı iyi bir egzersizdir.", "10 tekrar, her gün")
_ex2("as_bird", "birddog", "Kuş-köpek", "Ellerinizin ve dizlerinizin üzerinde, sırtınız düz durun. Bir kolunuzu öne, karşı bacağınızı arkaya uzatın; beliniz çukurlaşmasın. 5 saniye tutun, sonra taraf değiştirin.", "Her iki yana 8–10 tekrar")

AS_FAQ = [
 ("Ankilozan spondilit kalıtsal mı?", "Genetik yatkınlık önemlidir; hastaların büyük bölümünde HLA-B27 adlı doku grubu bulunur. Ancak HLA-B27 taşıyanların çoğunda hastalık gelişmez; bu test tek başına tanı koydurmaz."),
 ("Egzersiz ağrımı artırmaz mı?", "İltihaplı bel ağrısı hareketle azalır, dinlenmekle artar. Düzenli egzersiz tutukluğu azaltır, hareket açıklığını ve duruşu korur. Ağrılı ataklarda yoğunluğu azaltın ama hareketi bırakmayın."),
 ("Hangi sporları yapabilirim?", "Yüzme, su içi egzersiz, yürüyüş, bisiklet, pilates ve yoga uygun seçeneklerdir. Omurgası ileri derecede sertleşmiş kişiler düşme ve darbe riski olan sporlardan kaçınmalıdır; çünkü sertleşmiş omurga küçük darbelerle bile kırılabilir."),
 ("İlaç kullanıyorum, yine de egzersiz yapmalı mıyım?", "Evet. İlaçlar iltihabı kontrol eder; egzersiz ise hareketliliği, duruşu ve kas gücünü korur. Kılavuzlar ikisinin birlikte uygulanmasını öneriyor."),
]

AS_SRC = [
 "Ramiro S, Nikiphorou E, Sepriano A, et al. " + ext("https://ard.eular.org/article/S0003-4967(24)08620-5/fulltext", "ASAS-EULAR recommendations for the management of axial spondyloarthritis: 2022 update") + ". Ann Rheum Dis. 2023;82(1):19-34.",
 "Regnaux JP, Davergne T, Palazzo C, et al. " + ext("https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD011321.pub2/full", "Exercise programmes for ankylosing spondylitis") + ". Cochrane Database Syst Rev. 2019;10:CD011321.",
 "Zhao SS, Pittam B, Harrison NL, et al. " + ext("https://livrepository.liverpool.ac.uk/3081611/", "Diagnostic delay in axial spondyloarthritis: a systematic review and meta-analysis") + ". Rheumatology (Oxford). 2021;60(4):1620-1628.",
 "NHS. " + ext("https://www.nhs.uk/conditions/ankylosing-spondylitis/symptoms/", "Ankylosing spondylitis: symptoms") + ".",
 "National Axial Spondyloarthritis Society. " + ext("https://nass.co.uk/managing-my-as/exercise/", "Exercise") + ".",
]

AS_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Ankilozan spondilit</h1>
    <p class="lede">Genellikle 40 yaşından önce başlayan, belde ve sırtta iltihaplı ağrı ve tutukluğa yol açan romatizmal bir hastalıktır. Ağrının dinlenmekle artıp hareketle azalması en tipik özelliğidir. İlaç tedavisinin yanında düzenli egzersiz, tedavinin vazgeçilmez bir parçasıdır.</p>
    <p class="meta">Son güncelleme: 29 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>18–40</b><span>Hastalığın genellikle başladığı yaş aralığı</span></div>
        <div class="stat"><b>3 ay</b><span>Aksiyel spondiloartritten şüphelenmek için bel ağrısının en az sürmesi gereken süre; başlangıç yaşı 45'in altında</span></div>
        <div class="stat"><b>6,8 yıl</b><span>Belirtilerin başlamasından tanıya kadar geçen ortalama süre</span></div>
        <div class="stat"><b>14</b><span>Egzersiz programlarını inceleyen Cochrane derlemesindeki çalışma sayısı (1.579 hasta)</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Ankilozan spondilit; omurgayı ve omurganın leğen kemiğiyle birleştiği sakroiliak eklemleri tutan iltihaplı bir romatizmal hastalıktır. Bugün aksiyel spondiloartrit adı verilen daha geniş bir grubun parçası olarak ele alınıyor. İltihap uzun süre kontrol altına alınmazsa omurgada yeni kemik oluşumu ve kalıcı hareket kısıtlılığı gelişebilir.</p>
        <p class="soft">Belirtiler sinsi başladığı ve sıradan bel ağrısıyla karıştırıldığı için tanı çoğu zaman yıllarca gecikir. Erken tanı ve tedavi, hareketliliği korumak için önemlidir.</p>
      </div>
      <div>
        <h2>İltihaplı bel ağrısını nasıl tanırsınız?</h2>
        <ul class="dots">
          <li>40 yaşından önce, sinsi başlayan ve 3 aydan uzun süren bel ağrısı</li>
          <li>Dinlenmekle geçmeyen, hareketle azalan ağrı</li>
          <li>Geceleri, özellikle sabaha karşı uyandıran, kalkıp hareket edince hafifleyen ağrı</li>
          <li>Sabahları yarım saatten uzun süren tutukluk</li>
          <li>Kalçalarda sırayla yer değiştiren ağrı</li>
          <li>Topukta, aşil kirişinde ya da göğüs kafesinde ağrı; gözde kızarıklık ve ağrı</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi: ilaç ve egzersiz birlikte</h2>
      <p class="soft">Uluslararası Spondiloartrit Değerlendirme Derneği (ASAS) ile EULAR'ın 2022'de güncellenen önerilerine göre tedavinin temeli; hastalık hakkında bilgilendirme, düzenli egzersiz, sigarayı bırakma ve gerektiğinde fizyoterapidir. İlaç tedavisinde ilk basamak iltihap giderici ağrı kesicilerdir. Hastalık aktif kalmaya devam ederse romatoloji uzmanı biyolojik ilaçlar ya da JAK inhibitörleri gibi ileri tedavileri planlar. Uzun süreli kortizon tedavisi, omurga tutulumunda önerilmiyor.</p>
      <p class="soft">14 çalışmayı ve 1.579 hastayı kapsayan 2019 tarihli Cochrane derlemesinde, çoğunlukla ilaç tedavisine eklenen ve ortalama 12 hafta süren egzersiz programları, hiç egzersiz yapmamaya göre günlük işlevi biraz iyileştirdi ve hastaların değerlendirdiği hastalık aktivitesini biraz azalttı. Ağrı da azalabildi: 10 üzerinden 6,2 puan olan ağrı, egzersiz yapanlarda yaklaşık 2 puan daha düşüktü. Egzersiz, zaten fizyoterapi ya da düzenli tedavi alanlarda ise daha küçük bir ek fayda sağladı.</p>
      <div class="callout">
        <p>Sigara, hastalığın daha aktif seyretmesi ve omurgada yeni kemik oluşumunun hızlanmasıyla ilişkili; sigarayı bırakmak tedavinin bir parçasıdır.</p>
      </div>
      <ul class="tx" style="margin-top:22px">
        <li><b>Düzenli egzersiz</b><span>Esneklik, duruş, güçlendirme ve aerobik egzersizler. Su içi egzersiz de iyi bir seçenektir.</span></li>
        <li><b>Fizyoterapi</b><span>Denetimli ve kişiye özel programlar, özellikle hareket kısıtlılığı başladıysa faydalıdır.</span></li>
        <li><b>Duruş ve nefes</b><span>Gün içinde dik durmaya dikkat etmek ve derin nefes egzersizleri, göğüs kafesinin esnekliğini korumaya yardım eder.</span></li>
        <li><b>İlaç tedavisi</b><span>İltihap giderici ağrı kesiciler ve gerektiğinde romatoloji uzmanının planladığı ileri tedaviler.</span></li>
        <li><b>Göz ve eşlik eden sorunlar</b><span>Gözde kızarıklık ve ağrı gibi belirtilerde hızlı başvuru, kalıcı hasarı önler.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Duruş ve esneklik için altı egzersiz</h2>
      <p class="soft">Çalışmalardaki programlar çoğunlukla güçlendirme, esneklik, germe ve nefes egzersizlerinden oluşuyordu. Bu egzersizleri her gün, tercihen sabah tutukluğunu çözmek için sıcak bir duştan sonra yapın. Hareketleri tüm açıklıkta, yavaş ve nefesinizi tutmadan yapın.</p>
      {ex_grid(["wallpost", "as_chin", "as_thor", "as_cat", "as_press", "as_bird"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(AS_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Gözde kızarıklık, ağrı, ışığa hassasiyet ya da bulanık görme (aynı gün göz hekimine)</li>
        <li>Küçük bir düşme ya da darbeden sonra yeni başlayan, şiddetli sırt ya da boyun ağrısı</li>
        <li>Kol ya da bacaklarda uyuşma, güç kaybı; idrar ya da dışkı kontrolünde sorun</li>
        <li>Ateş ya da nedensiz kilo kaybı</li>
        <li>Göğüs ağrısı ve nefes darlığı (<strong>112</strong>)</li>
      </ul>
      {CTA_CARD("Bel ve sırt tutukluğunuz", "ankilozan spondilit")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(AS_SRC)}
    </div>
  </section>
</main>'''

page("ankilozan-spondilit.html", "Ankilozan Spondilit",
     "Dinlenmekle artan, hareketle azalan bel ağrısı: ankilozan spondilit nedir, nasıl anlaşılır ve tedavi edilir? Kılavuz önerileri, evde altı duruş ve esneklik egzersizi.",
     "ankilozan-spondilit.html", NECK_CSS, AS_BODY, "",
     seo_title="Ankilozan Spondilit: Belirtiler, Tedavi ve Egzersizler | İhsan Eren",
     condition="Ankilozan spondilit", faq_items=AS_FAQ)
