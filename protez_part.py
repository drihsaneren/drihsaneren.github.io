# -*- coding: utf-8 -*-
# Protez (diz ve kalça) sonrası evde rehabilitasyon sayfası. falls_part.py'den sonra exec edilir.

# Ayak bileği pompası (sırtüstü, yandan)
SV["apump"] = fig(GRD +
    '<circle class="hd" cx="12" cy="100" r="7"/>'
    '<path class="fig" d="M20 105 H100 M24 104 L42 108"/>'
    f'<g>{anim_t("0 100 105;-25 100 105;0 100 105;35 100 105;0 100 105", dur="3.2s", kt="0;0.25;0.5;0.75;1", typ="rotate")}'
    '<path class="fig hl" d="M100 105 L102 91"/></g>'
    '<path d="M110 84 A14 14 0 0 1 114 104" fill="none" stroke="#C8963E" stroke-width="2.5" stroke-dasharray="3 4" stroke-linecap="round"/>',
    "Ayak bileği pompası")

# Topuk kaydırma (sırtüstü, yandan)
SV["hslide"] = fig(GRD +
    '<circle class="hd" cx="12" cy="100" r="7"/>'
    '<path class="fig" d="M20 105 H58 M24 104 L42 108"/>'
    f'<path class="fig hl" d="M58 105 L84 105 L108 105">{anim_d("M58 105 L84 105 L108 105;M58 105 L78 84 L90 106;M58 105 L84 105 L108 105")}</path>'
    '<path d="M104 112 H86 M90 108 L86 112 L90 116" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    "Topuk kaydırma")

SV["quad2"] = SV["quad"]
SV["kext2"] = SV["kext"]
SV["slr2"] = SV["slr"]
SV["sts4"] = SV["sts"]

EXT.update({
 "apump": ("Ayak bileği pompası", "Sırtüstü yatın ya da oturun, bacaklarınız uzansın. Ayak uçlarınızı önce kendinize doğru çekin, sonra aşağı doğru itin. Baldır kaslarını çalıştırarak kan dolaşımını hızlandırır; ameliyattan sonraki ilk günlerden itibaren sık sık yapılır.", "Saatte bir, 10–20 tekrar"),
 "quad2": ("Havluya bastırma", "Sırtüstü yatın, ameliyatlı bacağınızın dizinin altına rulo yapılmış küçük bir havlu koyun. Dizinizin arkasıyla havluyu aşağı bastırarak uyluğunuzun ön kasını sıkın, 5 saniye tutun. Dizin tam düzleşmesine yardım eder.", "10 tekrar, günde 3 kez"),
 "hslide": ("Topuk kaydırma", "Sırtüstü yatın. Topuğunuzu yatağın üzerinde kaydırarak kalçanıza doğru çekin ve dizinizi rahat ettiğiniz kadar bükün, sonra yavaşça düzeltin. Topuğun altına poşet koymak kaymayı kolaylaştırır. Kalça protezinde bükme sınırı için cerrahınızın önerisine uyun.", "10 tekrar, günde 3 kez"),
 "kext2": ("Oturarak diz düzeltme", "Sandalyeye dik oturun. Ameliyatlı bacağınızın dizini yavaşça düzeltip uyluğunuzun ön kasını sıkın, 5 saniye tutup yavaşça indirin.", "10 tekrar, günde 2–3 kez"),
 "slr2": ("Düz bacak kaldırma", "Sırtüstü yatın, sağlam dizinizi bükün. Ameliyatlı bacağınızı dizi düz kalacak şekilde, uyluğunuzu sıkarak diğer dizinizin hizasına kadar kaldırın, yavaşça indirin. Uygun olup olmadığını fizyoterapistinize danışın.", "10 tekrar, günde 2 kez"),
 "sts4": ("Sandalyeden kalkıp oturma", "Kollu ve yeterince yüksek bir sandalyede ameliyatlı bacağınızı hafifçe öne alın. Ellerinizle kolçaklardan destek alarak kalkın, sonra kontrollü şekilde oturun. Günlük bağımsızlığın temel hareketidir.", "5–10 tekrar, günde 2–3 kez"),
})

PROTEZ_FAQ = [
 ("Ne zaman yürümeye başlayabilirim?", "Yürümeye genellikle ameliyattan kısa süre sonra, hastanede, koltuk değneği ya da yürüteçle başlanır. Diz protezinde güvendikçe önce tek değneğe, sonra bastona geçilir; yaklaşık 6 hafta sonra, kendinizi hazır hissediyorsanız yardımcısız yürümeyi deneyebilirsiniz."),
 ("Ne zaman araba kullanabilirim?", "Tam diz ve kalça protezinden sonra en az 6 hafta beklemeniz önerilir; yarım (kısmi) diz protezinde bu süre 3 hafta olabilir. Araç kullanmaya başlamadan önce hekiminizden onay alın."),
 ("Kalça protezinden sonra hangi hareketlerden kaçınmalıyım?", "Birçok merkez ilk haftalarda bacak bacak üstüne atmamayı, kalçayı 90 dereceden fazla bükmemeyi ve alçak koltuklardan kaçınmayı önerir. Ancak 8.835 hastayı kapsayan bir derlemede bu kısıtlamaların rutin olarak uygulanmasının çıkık riskini azalttığı gösterilemedi; bu yüzden bazı merkezler kısıtlamaları azaltıyor. Hangi hareketlerden kaçınmanız gerektiğine ameliyat tekniğinize göre cerrahınız karar verir."),
 ("Dizimin altına yastık koyabilir miyim?", "Uyurken dizinizin altına yastık koymayın. Diz bükük pozisyonda uzun süre kalırsa tam düzleşmesi zorlaşır. Bacağınızı yükseltmek istiyorsanız yastığı dizin değil, baldır ve topuğun altına koyun."),
 ("Ne zaman işe dönebilirim?", "Kendinizi hazır hissettiğinizde; diz protezinden sonra bu genellikle 6–12 hafta, kalça protezinden sonra yaklaşık 6 haftadır. Ağır bedensel işlerde süre uzayabilir."),
 ("Ameliyattan önce egzersiz yapmalı mıyım?", "Evet. Amerikan Fizyoterapi Derneği'nin diz protezi kılavuzu ameliyat öncesinde kuvvet ve esneklik egzersizleri öneriyor. Ameliyata güçlü kaslarla girmek sonrasındaki süreci kolaylaştırır."),
]

PROTEZ_SRC = [
 "Jette DU, Hunter SJ, et al. " + ext("https://academic.oup.com/ptj/article/100/9/1603/5857258", "Physical therapist management of total knee arthroplasty") + ". Phys Ther. 2020;100(9):1603.",
 "Korfitsen CB, et al. " + ext("https://actaorthop.org/actao/article/view/11958", "Hip precautions after posterior-approach total hip arthroplasty among patients with primary hip osteoarthritis do not influence early recovery: a systematic review and meta-analysis of randomized and non-randomized studies with 8,835 patients") + ". Acta Orthop. 2023;94.",
 "NHS. " + ext("https://www.nhs.uk/tests-and-treatments/knee-replacement/recovery/", "Recovering from a knee replacement") + ".",
 "NHS. " + ext("https://www.nhs.uk/tests-and-treatments/knee-replacement/complications/", "Complications of a knee replacement") + ".",
 "NHS. " + ext("https://www.nhs.uk/tests-and-treatments/hip-replacement/recovering-from-a-hip-replacement/", "Recovering from a hip replacement") + ".",
]

PROTEZ_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Rehabilitasyon rehberi</p>
    <h1>Diz ve kalça protezi sonrası evde rehabilitasyon</h1>
    <p class="lede">Protez ameliyatı ağrıyı azaltmak ve hareketi geri kazandırmak için yapılır; sonucun önemli bir kısmı ise ameliyattan sonraki haftalarda yapılan egzersizlere bağlıdır. Evde doğru egzersiz, güvenli bir ev düzeni ve kademeli olarak artan aktivite bu sürecin temelidir.</p>
    <p class="meta">Son güncelleme: {UPDATED}</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>1–3 gün</b><span>Kalça protezinde genel durumu iyi olanlarda taburculuk zamanı</span></div>
        <div class="stat"><b>6 hafta</b><span>Diz protezinde yardımcısız yürümeyi denemek için yaklaşık süre</span></div>
        <div class="stat"><b>En az 6 hafta</b><span>Tam diz ve kalça protezinden sonra araç kullanmadan önce</span></div>
        <div class="stat"><b>6–12 hafta</b><span>Diz protezinden sonra işe dönüş için genel süre</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>İlk haftalarda ne beklemeli?</h2>
        <p class="soft">Ameliyattan sonraki haftalarda eklemde şişlik, morarma, ısı artışı ve özellikle geceleri ağrı olması beklenen bir durumdur ve zamanla azalır. Tam iyileşme aylar sürebilir.</p>
        <p class="soft">Yürümeye genellikle hastanedeyken, koltuk değneği ya da yürüteçle başlanır. Güvendikçe önce tek değneğe, sonra bastona geçilir. Fizyoterapistinizin önerdiği egzersizleri düzenli yapmak iyileşmeye yardım eder ve komplikasyonları önler.</p>
      </div>
      <div>
        <h2>İlk günlerden itibaren</h2>
        <ul class="dots">
          <li>Şişliği azaltmak için dinlenirken bacağınızı yüksekte tutun.</li>
          <li>Ağrı kesicilerinizi hekiminizin önerdiği şekilde, egzersizlerden önce alın.</li>
          <li>Ayak bileği pompasını gün içinde sık sık yapın.</li>
          <li>Kısa ama sık yürüyüşler yapın, uzun süre hareketsiz kalmayın.</li>
          <li>Pıhtı önleyici ilaçlarınızı ya da çoraplarınızı önerildiği süre boyunca kullanın.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Diz ve kalça protezinde dikkat edilecekler</h2>
      <ul class="tx">
        <li><b>Diz protezi: tam düzleşme</b><span>Uyurken dizinizin altına yastık koymayın; bükük kalan diz zamanla tam düzleşmeyebilir. Bacağınızı yükseltirken yastığı baldır ve topuğun altına koyun.</span></li>
        <li><b>Diz protezi: bükme</b><span>Dizin bükülme açısını artırmak ilk haftaların en önemli hedeflerinden biridir. Topuk kaydırma ve oturarak diz bükme egzersizleri bunun için kullanılır.</span></li>
        <li><b>Diz protezi: ilk 6 hafta</b><span>İlk 6 hafta bacak bacak üstüne atarak oturmayın.</span></li>
        <li><b>Kalça protezi: hareket kısıtlamaları</b><span>Birçok merkez ilk haftalarda kalçayı 90 dereceden fazla bükmemeyi, bacak bacak üstüne atmamayı, ayaklara doğru eğilmemeyi ve alçak koltuk ya da klozetten kaçınmayı önerir. Son çalışmalar rutin kısıtlamaların çıkık riskini azaltmadığını gösteriyor; hangilerine uymanız gerektiğine cerrahınız karar verir.</span></li>
        <li><b>Kalça protezi: aktivite</b><span>İlk aylarda zıplama, ani dönme ve düşme riski yüksek hareketlerden kaçının; her gün, rahat ettiğiniz ölçüde yürüyün.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Protez sonrası altı temel egzersiz</h2>
      <p class="soft">Bu egzersizler diz ve kalça protezinden sonra sık kullanılan temel hareketlerdir. Hangilerinin, ne zaman ve hangi sınırlar içinde size uygun olduğunu cerrahınız ve fizyoterapistiniz belirler. Egzersiz sırasında hafif ağrı olabilir; keskin ağrı, yarada akıntı ya da belirgin şişlik artışı olursa durun.</p>
      {ex_grid(["apump", "quad2", "hslide", "kext2", "slr2", "sts4"])}
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Evde güvenli günlük yaşam</h2>
        <p class="soft">Ev düzenini ameliyattan önce hazırlamak, ilk haftaları çok daha kolay ve güvenli hale getirir.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Merdiven çıkarken önce sağlam bacağınızla, inerken önce ameliyatlı bacağınız ve bastonunuzla adım atın.</li>
        <li>Kollu, yeterince yüksek bir sandalye kullanın; kalça protezinde klozet yükseltici işinizi kolaylaştırır.</li>
        <li>Kaygan halıları kaldırın, yerdeki kabloları toplayın, geceleri yolunuzu aydınlatın.</li>
        <li>Banyoya tutunma barı ve kaydırmaz paspas koyun.</li>
        <li>Uzun saplı ayakkabı çekeceği ve uzanma aparatı eğilmeden işlerinizi yapmanızı sağlar.</li>
      </ul>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Protez sonrası egzersiz videoları</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz. Egzersizleri cerrahınızın ve fizyoterapistinizin izin verdiği ölçüde yapın.</p>
      <div class="vids">
        <div class="vid">
          {vbox("GQp73wn6Ha8", "Diz protezi egzersizleri videosunu oynat", "2 Critical Exercises For Complete Success After Knee Replacement")}
          <h3>Diz protezi sonrası iki kritik egzersiz</h3>
          <p>Dizin düzleşmesi ve bükülmesi için temel iki hareket.</p>
        </div>
        <div class="vid">
          {vbox("fgY6k1hkH0E", "Kalça protezi egzersizleri videosunu oynat", "Total Hip Replacement - Exercises 4-6 Weeks After Surgery")}
          <h3>Kalça protezinden 4–6 hafta sonra egzersizler</h3>
          <p>Ameliyattan sonraki ilk haftaları izleyen dönem için egzersiz programı.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(PROTEZ_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Ameliyattan sonra şu durumlarda beklemeden cerrahınıza ya da bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Bacağınızda ve özellikle baldırınızda zonklayan ya da kramp tarzında ağrı, şişlik (pıhtı olabilir)</li>
        <li>Bacakta ağrı ve şişlikle birlikte nefes darlığı ya da göğüs ağrısı (akciğere pıhtı atmış olabilir, <strong>112</strong>'yi arayın)</li>
        <li>Ateş, üşüme, titreme; yarada akıntı ya da iltihap</li>
        <li>Eklemde düzelmeyen, giderek artan kızarıklık, hassasiyet, şişlik ya da ağrı</li>
        <li>Kalçada ani şiddetli ağrı, bacağın kısalmış ya da dönmüş görünmesi, basamama (çıkık olabilir)</li>
      </ul>
      {CTA_CARD("Protez sonrası rehabilitasyon süreciniz", "protez sonrası rehabilitasyon")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(PROTEZ_SRC)}
    </div>
  </section>
</main>'''

page("protez-sonrasi.html", "Protez Sonrası Evde Rehabilitasyon",
     "Diz ve kalça protezi ameliyatından sonra evde rehabilitasyon: ilk haftalarda ne beklenir, hangi egzersizler yapılır, ne zaman yürünür, araç kullanılır ve işe dönülür? Güvenli ev önerileri, videolar ve uyarı işaretleri.",
     "protez-sonrasi.html", NECK_CSS, PROTEZ_BODY, YT_JS,
     seo_title="Diz ve Kalça Protezi Sonrası Evde Rehabilitasyon ve Egzersizler | İhsan Eren",
     about=[{"@type": "MedicalCondition", "name": "Diz protezi sonrası rehabilitasyon"}, {"@type": "MedicalCondition", "name": "Kalça protezi sonrası rehabilitasyon"}],
     faq_items=pick(PROTEZ_FAQ, 0, 1, 2, 3))
