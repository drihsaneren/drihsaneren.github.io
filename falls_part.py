# -*- coding: utf-8 -*-
# Düşmeleri önleme ve denge sayfası. cts_part.py'den sonra exec edilir.

COUNTER_R = '<path class="obj" d="M82 60 H112 M104 60 V112"/>'

# Tezgâha tutunarak tek ayak üzerinde durma (yandan)
SV["sls"] = fig(GRD + COUNTER_R +
    '<circle class="hd" cx="50" cy="20" r="7"/>'
    '<path class="fig" d="M50 28 L50 70 M50 38 L68 50 L84 60"/>'
    '<path class="fig" d="M50 70 L50 108 L60 110"/>'
    f'<path class="fig hl" d="M50 70 L50 108 L58 110">{anim_d("M50 70 L50 108 L58 110;M50 70 L54 90 L42 98;M50 70 L50 108 L58 110", dur="4s")}</path>',
    "Tek ayak üzerinde durma")

# Topuk-parmak yürüyüşü (yukarıdan ayak izleri)
def _foot(x, y, i, n=5, dur="5s"):
    a = i / (n + 1)
    return (f'<rect x="{x-6}" y="{y-10}" width="12" height="20" rx="6" fill="#2A6F6B" opacity="0">'
            f'<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;{a:.2f};{a+0.06:.2f};0.92;1" dur="{dur}" repeatCount="indefinite"/></rect>'
            f'<circle cx="{x}" cy="{y-13}" r="3" fill="#C8963E" opacity="0">'
            f'<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;{a:.2f};{a+0.06:.2f};0.92;1" dur="{dur}" repeatCount="indefinite"/></circle>')
SV["tandem"] = fig(
    '<path d="M60 116 V4" stroke="#B9CBC6" stroke-width="2" stroke-dasharray="3 4" fill="none"/>'
    + "".join(_foot(57 if i % 2 == 0 else 63, 104 - i * 23, i) for i in range(5)),
    "Topuk-parmak yürüyüşü")

# Tezgâh boyunca yana adım (önden)
SS_DUR, SS_KT = "4.8s", "0;0.25;0.5;0.75;1"
SV["sidestep"] = fig(GRD +
    '<path class="obj" d="M12 64 H108"/>'
    f'<g>{anim_t("0 0;4 0;8 0;4 0;0 0", dur=SS_DUR, kt=SS_KT)}'
    '<circle class="hd" cx="60" cy="20" r="8"/><path class="fig" d="M44 38 H76 M60 30 V78 M44 38 L40 64 M76 38 L80 64"/></g>'
    f'<path class="fig hl" d="M60 78 L52 112 M60 78 L68 112">{anim_d("M60 78 L52 112 M60 78 L68 112;M64 78 L52 112 M64 78 L80 112;M68 78 L60 112 M68 78 L76 112;M64 78 L52 112 M64 78 L76 112;M60 78 L52 112 M60 78 L68 112", dur=SS_DUR, kt=SS_KT)}</path>'
    '<path d="M86 96 H100 M96 92 L100 96 L96 100" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    "Yana adım")

SV["sts3"] = SV["sts"]
SV["heel2"] = SV["heel"]
SV["wshift2"] = SV["wshift"]

EXT.update({
 "sls": ("Tek ayak üzerinde durma", "Mutfak tezgâhının önünde dik durun, bir ya da iki elinizle hafifçe tutunun. Bir ayağınızı yerden kaldırıp dizinizi arkaya doğru bükün ve dengede kalın. Kolaylaştıkça tek elle, sonra parmak ucuyla tutunun.", "10–15 saniye, her ayakla 3–5 kez"),
 "tandem": ("Topuk-parmak yürüyüşü", "Tezgâh ya da duvar boyunca, bir elinizi dayanak için hazır tutarak yürüyün. Her adımda öndeki ayağınızın topuğunu arkadaki ayağınızın parmak uçlarının hemen önüne koyun, bakışınız ileride olsun. İpte yürür gibi düz bir çizgi izleyin.", "10–15 adım, 2–3 tur"),
 "sidestep": ("Yana adım", "Tezgâha önden tutunun. Yan yan adımlarla tezgâh boyunca bir yöne, sonra diğer yöne ilerleyin; ayak parmaklarınız öne baksın, ayaklarınız birbirine çarpmasın. Kalçanın yan kaslarını güçlendirir.", "10 adım sağa, 10 adım sola, 2 tur"),
 "sts3": ("Sandalyeden kalkıp oturma", "Kollu, sağlam bir sandalyede kalçanızı öne kaydırın, ayaklarınızı biraz geriye alın. Öne eğilerek kalkın, tamamen doğrulun, sonra kontrollü şekilde oturun. Zorlanıyorsanız ellerinizden destek alın; kolaylaştıkça kollarınızı göğsünüzde çaprazlayın.", "10 tekrar, günde 1–2 kez"),
 "heel2": ("Tezgâha tutunarak topuk yükseltme", "Tezgâha tutunarak dik durun. İki topuğunuzu birlikte kaldırıp parmak uçlarınızda yükselin, 2 saniye bekleyip yavaşça inin. Baldır kasları yürürken ayağı yerden itmek ve dengeyi toparlamak için önemlidir.", "10–15 tekrar"),
 "wshift2": ("Ağırlık aktarma", "Tezgâha iki elinizle tutunun, ayaklarınız omuz genişliğinde açık olsun. Ağırlığınızı yavaşça bir bacağınıza, sonra diğerine aktarın; vücudunuz dik kalsın. Kolaylaştıkça ağırlığı öne ve arkaya da aktarın.", "Her yöne 10 tekrar"),
})

DUSME_FAQ = [
 ("Düştüğümde nasıl kalkmalıyım?", "Önce sakin olun ve bir yerinizin ağrıyıp ağrımadığını kontrol edin. Yaralanmadıysanız yan dönün, yavaşça ellerinizin ve dizlerinizin üzerine gelin, sağlam bir sandalyeye ya da merdivene doğru emekleyin. Ona tutunarak bir ayağınızı yere basın, kollarınız ve bacaklarınızla itip yavaşça ayağa kalkın ya da oturun, sonra dinlenin. Yaralandıysanız ya da kalkamıyorsanız yardım çağırın, üşümemek için üzerinizi örtün ve yardım gelene kadar bacaklarınızı hafifçe hareket ettirin."),
 ("Düşme korkum var, hareket etmemek daha güvenli değil mi?", "Hayır. Hareketsizlik kasları zayıflatır ve dengeyi bozar; bu da düşme riskini artırır. Güvenli bir ortamda, destekle ve kademeli olarak hareket etmek hem gücü hem de güveni geri kazandırır."),
 ("Denge egzersizlerini ne sıklıkla yapmalıyım?", "Etkili programlarda denge ve güçlendirme egzersizleri haftada birkaç kez, aylarca düzenli olarak yapılır ve zorluğu kademeli olarak artırılır. Kısa süreli ya da düzensiz egzersizin etkisi sınırlı kalır."),
 ("Baston ya da yürüteç kullanmalı mıyım?", "Doğru seçilip doğru ayarlandığında yürüme yardımcıları güvenliği artırır. Boyu yanlış ayarlanmış ya da ihtiyaca uymayan bir baston ise dengeyi bozabilir. Hangi yardımcının size uygun olduğunu fizyoterapistinizle birlikte belirleyin."),
 ("Düştükten sonra hekime söylemeli miyim?", "Evet. Yaralanmamış olsanız bile düştüğünüzü hekiminize söyleyin. Düşmelerin altında yatan birçok neden, örneğin ilaç yan etkileri, tansiyon düşmesi ya da görme sorunları tedavi edilebilir ya da düzeltilebilir."),
]

DUSME_SRC = [
 "Montero-Odasso M, van der Velde N, Martin FC, et al. " + ext("https://academic.oup.com/ageing/article/51/9/afac205/6730755", "World guidelines for falls prevention and management for older adults: a global initiative") + ". Age Ageing. 2022;51(9):afac205.",
 "NHS inform. " + ext("https://www.nhsinform.scot/healthy-living/preventing-falls/dealing-with-a-fall/what-to-do-if-you-fall/", "What to do if you fall") + ".",
 "Sherrington C, Fairhall NJ, Wallbank GK, et al. " + ext("https://www.cochrane.org/evidence/CD012424_exercise-preventing-falls-older-people-living-community", "Exercise for preventing falls in older people living in the community") + ". Cochrane Database Syst Rev. 2019;1:CD012424.",
 "World Health Organization. " + ext("https://www.who.int/news-room/fact-sheets/detail/falls", "Falls") + ". Fact sheet.",
]

DUSME_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Rehabilitasyon rehberi</p>
    <h1>Düşmeleri önleme ve denge</h1>
    <p class="lede">65 yaş üstünde her yıl yaklaşık üç kişiden biri düşer. Düşmeler kırıklara, hareket etme korkusuna ve bağımsızlığın azalmasına yol açabilir. İyi haber: düzenli denge ve güçlendirme egzersizleri düşmeleri belirgin şekilde azaltıyor.</p>
    <p class="meta">Son güncelleme: {UPDATED}</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%30</b><span>65 yaş üstünde her yıl düşen kişi</span></div>
        <div class="stat"><b>684 bin</b><span>Dünyada her yıl düşmelere bağlı ölüm; kaza kaynaklı ölümlerde ikinci sıra</span></div>
        <div class="stat"><b>%23</b><span>Egzersizle düşme sayısında sağlanan azalma</span></div>
        <div class="stat"><b>%34</b><span>Denge, günlük hareket ve güçlendirme egzersizlerini birleştiren programlarla azalma</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Neden düşeriz?</h2>
        <p class="soft">Düşme çoğu zaman tek bir nedene bağlı değildir; birkaç risk etkeni bir araya geldiğinde olasılık artar. Bu yüzden düşme riskinin değerlendirilmesi kas gücünden ilaçlara, görmeden ev ortamına kadar geniş bir bakış ister.</p>
        <p class="soft">Daha önce düşmüş olmak, yeniden düşme riskinin en güçlü işaretlerinden biridir. Tek bir düşme bile değerlendirme için yeterli bir nedendir.</p>
      </div>
      <div>
        <h2>Başlıca risk etkenleri</h2>
        <ul class="dots">
          <li>Bacak kaslarında güçsüzlük, denge ve yürüme bozukluğu</li>
          <li>Daha önce düşmüş olmak ve düşme korkusu</li>
          <li>Çok sayıda ilaç, özellikle uyku ilaçları, sakinleştiriciler ve bazı tansiyon ilaçları</li>
          <li>Ayağa kalkınca baş dönmesi, görme sorunları</li>
          <li>Evdeki tehlikeler: kaygan halılar, kablolar, yetersiz aydınlatma</li>
          <li>Uygun olmayan ayakkabı ya da terlik</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Egzersiz düşmeleri önler</h2>
      <p class="soft">Toplumda yaşayan yaşlılarla yapılan çalışmaların Cochrane derlemesinde egzersiz, düşme sayısını %23, düşen kişi sayısını %15 azalttı. Denge ve günlük hareketleri çalıştıran egzersizler düşme sayısını %24; bunları güçlendirme egzersizleriyle birleştiren programlar %34 azalttı. Tai Chi de düşmeleri azaltabiliyor.</p>
      <div class="callout">
        <p>Düşme korkusu kişiyi hareketsizliğe iter; hareketsizlik kasları zayıflatır ve düşme riskini daha da artırır. Bu kısır döngüyü kırmanın yolu, güvenli bir ortamda ve kademeli olarak hareket etmektir. Bacak gücünüzü ve dengenizi merak ediyorsanız ana sayfadaki <a href="index.html#hizli-test">2 dakikalık hızlı teste</a> göz atın.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Denge ve güç için altı egzersiz</h2>
      <p class="soft">Ayakta yapılan tüm hareketleri mutfak tezgâhı gibi sağlam bir desteğin önünde yapın; mümkünse ilk zamanlarda yanınızda biri bulunsun. Baş dönmesi, göğüs ağrısı ya da nefes darlığı olursa durun. Hareketler kolaylaştıkça desteği azaltarak zorluğu artırın.</p>
      {ex_grid(["sls", "tandem", "sidestep", "sts3", "heel2", "wshift2"])}
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Evde güvenlik kontrol listesi</h2>
        <p class="soft">Düşmelerin önemli bir kısmı evde olur. Küçük düzenlemeler büyük fark yaratır.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Kaygan halıları kaldırın ya da kaydırmaz bantla sabitleyin; yerdeki kabloları toplayın.</li>
        <li>Yatak odasından banyoya giden yola gece lambası koyun.</li>
        <li>Banyoya tutunma barı ve kaydırmaz paspas, merdivenlere iki taraflı tırabzan taktırın.</li>
        <li>Sık kullandığınız eşyaları uzanmadan ya da tabureye çıkmadan alabileceğiniz yüksekliğe koyun.</li>
        <li>Arkası kapalı, kaymayan tabanlı ayakkabı ya da terlik giyin.</li>
        <li>Yataktan ya da sandalyeden kalkarken önce birkaç saniye oturup bekleyin, sonra yavaşça kalkın.</li>
        <li>Gözlüğünüzü ve ilaçlarınızı düzenli olarak hekiminize kontrol ettirin.</li>
      </ul>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Denge ve düşme videoları</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("uSCWsP0hR14", "Denge egzersizi videosunu oynat", "Best Standing Balance Exercise For Seniors To Stay Active &amp; Alert")}
          <h3>Yaşlılar için ayakta denge egzersizi</h3>
          <p>Evde güvenle yapılabilecek bir denge çalışması.</p>
        </div>
        <div class="vid">
          {vbox("3H7eSIvife4", "Düştükten sonra kalkma videosunu oynat", "The Life-Saving Trick to Get Up After a Fall")}
          <h3>Düştükten sonra güvenle kalkmak</h3>
          <p>Yerden adım adım ve güvenli şekilde kalkma yöntemi.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(DUSME_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Düşmeden sonra şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Kalçada ya da bacakta şiddetli ağrı, bacağa yük verememe (kalça kırığı olabilir)</li>
        <li>Başın çarpması, özellikle kan sulandırıcı ilaç kullanıyorsanız; sonrasında baş ağrısında artış, kusma ya da uyku hali</li>
        <li>Düşmeden önce bayılma, göğüs ağrısı ya da çarpıntı</li>
        <li>Yüzde kayma, bir kolda ya da bacakta ani güçsüzlük, konuşma bozukluğu (inme olabilir, <strong>112</strong>'yi arayın)</li>
        <li>Uzun süre yerde kalmış olmak ya da düşmeden sonra yeni başlayan kafa karışıklığı</li>
      </ul>
      {CTA_CARD("Dengeniz ve düşme riskiniz", "denge ve düşmeyi önleme")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(DUSME_SRC)}
    </div>
  </section>
</main>'''

page("dusme-onleme.html", "Düşmeleri Önleme ve Denge",
     "Yaşlılarda düşmeler neden olur, nasıl önlenir? Evde altı denge ve güç egzersizi, ev güvenliği kontrol listesi, düştükten sonra güvenle kalkma, videolar ve uyarı işaretleri.",
     "dusme-onleme.html", NECK_CSS, DUSME_BODY, YT_JS,
     seo_title="Yaşlılarda Düşmeleri Önleme ve Denge Egzersizleri | İhsan Eren",
     about={"@type": "MedicalCondition", "name": "Yaşlılarda düşme"},
     faq_items=pick(DUSME_FAQ, 0, 1, 3, 4))
