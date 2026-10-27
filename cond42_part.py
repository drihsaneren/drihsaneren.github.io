# -*- coding: utf-8 -*-
# Yeni rehber (42): Boyun incinmesi (whiplash). cond41_part.py'den sonra exec edilir. Video yok.
# Egzersizler Berkshire Healthcare NHS (Şubat 2026) ve NHS Fife broşürlerindeki hareketlere göre, hazır çizimlerle.

_ex2("wh_chin", "chin", "Çene içe çekme", "Sırtüstü yatın ya da dik oturun. Başınızı kaldırmadan çenenizi hafifçe içeri çekin; başınızın arkasından bir ip çekiliyormuş gibi enseniz uzasın. 5 saniye tutun, sonra gevşeyin.", "10–20 tekrar, günde 2–3 kez")
_ex2("wh_rot", "rot", "Başı yana çevirme", "Çeneniz hafifçe içeride, gözleriniz karşıda olsun. Başınızı rahat edebildiğiniz kadar bir yana çevirin, ortaya dönün, sonra öbür yana çevirin.", "10–20 tekrar, günde 2–3 kez")
_ex2("wh_side", "side", "Başı yana eğme", "Dik oturun. Kulağınızı aynı taraftaki omzunuza doğru, karşı tarafta hafif bir gerilme hissedene kadar yaklaştırın. 5–10 saniye tutun, sonra öbür yana tekrarlayın.", "Her yöne 10 tekrara kadar, 1–2 saatte bir")
_ex2("wh_nod", "bt_nod", "Başı öne eğme", "Dik oturun. Başınızı ensenizde hafif bir gerilme hissedene kadar öne eğin, 5–10 saniye tutun, sonra dik konuma dönün.", "10 tekrara kadar, 1–2 saatte bir")
_ex2("wh_roll", "ly_shrug", "Omuz çevirme", "Oturarak ya da ayakta, omuzlarınızı yuvarlak bir hareketle önce bir yöne, sonra öbür yöne çevirin.", "Her yöne 5–10 kez")
_ex2("wh_child", "childp", "Sırtı açan esneme", "Diz çökün ve kalçanızı topuklarınıza doğru geri oturtun. Göğsünüzü yere doğru indirip kollarınızı öne uzatın, başınızı gevşek bırakın. Derin nefes alarak rahat ettiğiniz kadar kalın.", "Rahat ettiğiniz süre, günde 2–3 kez")

WH_FAQ = [
 ("Boyunluk takmalı mıyım?", "Hayır. NHS, boyunluğun iyileşmeye yardım etmediğini belirtiyor; bir NHS fizyoterapi broşüründe araştırmaların boyunluğun iyileşmeyi geciktirdiğini gösterdiği yazıyor. Boynunuzu uzun süre dinlendirmek yerine günlük işlerinize devam etmeniz önerilir."),
 ("Ne kadar sürer?", "Whiplash çoğu zaman 2–3 ay içinde iyileşir, ama bazı kişilerde belirtiler daha uzun sürebilir. Bir hafta içinde düzelme yoksa ya da 6 hafta içinde günlük işlerinizin çoğuna dönemediyseniz hekiminize başvurabilirsiniz."),
 ("Fizyoterapi gerekli mi?", "Çoğu kişi basit önerilerle ve hareketli kalarak iyileşir. İngiltere’de yapılan büyük bir araştırmada belirtileri süren 599 kişide, altı seansa kadar fizyoterapi, tek seanslık danışmanlığa göre 4. ayda biraz daha hızlı iyileşme sağladı; 8. ve 12. aylarda fark kalmadı. Belirtileriniz geçmiyorsa kişiye özel bir değerlendirme yol gösterici olabilir. Belirtileri 3 aydan uzun süren 172 kişiyle Avustralya'da yapılan bir çalışmada da 20 seanslık kapsamlı bir fizyoterapi egzersiz programı, tek seanslık danışmanlık ve telefon desteğine göre ağrıyı 14. haftada, 6. ayda ve 12. ayda daha fazla azaltmadı."),
 ("Ne zaman araba kullanabilirim?", "Başınızı çevirip iki omzunuzun üzerinden rahatça ve güvenle bakabildiğinizde. Kollarınızda ya da bacaklarınızda uyuşma, güçsüzlük gibi uyarı belirtileri varsa hekiminizle konuşmadan araç ya da bisiklet kullanmayın."),
 ("Nasıl uyumalıyım?", "Sırtüstü ya da yan yatmak boynunuz için daha iyi bir pozisyondur. Boynunuzu yastıklarla destekleyebilirsiniz."),
]

WH_SRC = [
 "NHS. " + ext("https://www.nhs.uk/conditions/whiplash/", "Whiplash") + ". Page last reviewed: 19 August 2026.",
 "Berkshire Healthcare NHS Foundation Trust. " + ext("https://www.berkshirehealthcare.nhs.uk/media/b3ygh1f0/bh1165u-whiplash-v1-feb-2026.pdf", "Whiplash: physiotherapy advice and exercises") + ". February 2026.",
 "NHS Fife. " + ext("https://www.nhsfife.org/media/33112/whiplash_neck_pain_v7.pdf", "Whiplash neck pain") + ". 2016.",
 "Lamb SE, Gates S, Williams MA, et al. " + ext("https://search.pedro.org.au/search-results/record-detail/35109", "Emergency department treatments and physiotherapy for acute whiplash: a pragmatic, two-step, randomised controlled trial") + ". Lancet. 2013;381(9866):546–556.",
 "Michaleff ZA, Maher CG, Lin CWC, et al. " + ext("https://research.bond.edu.au/en/publications/comprehensive-physiotherapy-exercise-programme-or-advice-for-chro/", "Comprehensive physiotherapy exercise programme or advice for chronic whiplash (PROMISE): a pragmatic randomised controlled trial") + ". Lancet. 2014;384(9938):133–141.",
 "Bussières AE, Stewart G, Al-Zoubi F, et al. " + ext("https://pubmed.ncbi.nlm.nih.gov/27836071/", "The treatment of neck pain-associated disorders and whiplash-associated disorders: a clinical practice guideline") + ". J Manipulative Physiol Ther. 2016;39(8):523–564",
]

WH_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Boyun incinmesi (whiplash)</h1>
    <p class="lede">Bir trafik kazasında, düşmede ya da spor sırasında başınız ani bir hareketle öne arkaya mı savruldu? Bu tür boyun incinmesine whiplash (kamçı yaralanması) denir. Çoğu zaman 2–3 ay içinde iyileşir. Boyunluk takmak yerine hareketli kalmak, iyileşmenin en önemli parçasıdır.</p>
    <p class="meta">Son güncelleme: 24 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>2–3 ay</b><span>Çoğu kişide iyileşme süresi; bazı kişilerde daha uzun sürebilir</span></div>
        <div class="stat"><b>Birkaç saat</b><span>Belirtilerin ortaya çıkması, incinmeden sonra birkaç saat sürebilir</span></div>
        <div class="stat"><b>Boyunluk yok</b><span>Boyunluk iyileşmeye yardım etmez; hareketli kalmak önerilir</span></div>
        <div class="stat"><b>4. ay</b><span>Süren belirtilerde fizyoterapinin sağladığı küçük ek yararın görüldüğü dönem; 12. ayda fark kalmadı</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Boyun ağrısı ve tutukluk, başı hareket ettirmekte zorluk.</li>
          <li>Baş ağrısı.</li>
          <li>Omuzlarda ve kollarda ağrı, kas spazmı.</li>
          <li>Belirtiler incinmeden hemen sonra değil, birkaç saat sonra başlayabilir.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Başın ani bir hareketle öne, arkaya ya da yana savrulması boyundaki dokuları zorlar.</li>
          <li>En sık nedenler trafik kazaları, kayıp düşmeler ve spor yaralanmalarıdır.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Hareketli kalın</h3><p>Günlük işlerinize devam edin. Biraz ağrıtabilir ama iyileşmeyi hızlandırır. Boynunuzu uzun süre dinlendirmeyin, sık sık pozisyon değiştirin.</p></div>
        <div class="kind"><span class="n">2</span><h3>Boyunluk takmayın</h3><p>Boyunluk iyileşmeye yardım etmez. Araştırmalar iyileşmeyi geciktirdiğini gösteriyor.</p></div>
        <div class="kind"><span class="n">3</span><h3>Ağrıyı kontrol edin</h3><p>Hekiminize danışarak ağrı kesici kullanabilirsiniz. Ağrının azalması hareketli kalmanızı kolaylaştırır.</p></div>
        <div class="kind"><span class="n">4</span><h3>Isı ya da soğuk</h3><p>Nemli bir havluya sarılı sıcak ya da soğuk uygulamayı en fazla 10 dakika kullanabilirsiniz. Ciltte his azalması varsa ısı uygulamayın.</p></div>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Boynu rahatlatan altı egzersiz</h2>
      <p class="soft">Hareketleri az ama sık yapın; belirtilerinizi belirgin şekilde artırmamalı. Ağrı artarsa tekrar sayısını azaltın ve hareketleri küçültün. Başınızı daire çizerek döndürmeyin.</p>
      {ex_grid(["wh_chin", "wh_rot", "wh_side", "wh_nod", "wh_roll", "wh_child"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(WH_FAQ)}
      <p class="soft" style="margin-top:18px">Ani başlayan, kaza ya da düşme olmadan gelişen boyun ağrısı için <a href="boyun-tutulmasi.html">boyun tutulması</a>, uzun süren ağrı için <a href="boyun-agrisi.html">boyun ağrısı</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Ağrı kesicilere rağmen şiddetli ağrı varsa</li>
        <li>Vücudunuzun bir ya da iki yanında karıncalanma, uyuşma varsa</li>
        <li>Ellerinizde, kollarınızda ya da bacaklarınızda güçsüzlük varsa</li>
        <li>Yürümekte ya da dik oturmakta zorlanıyorsanız</li>
        <li>Boyundan sırta, kollara ya da bacaklara yayılan ani “elektrik çarpması” hissi varsa</li>
        <li>Ani başlayan ya da giderek kötüleşen şiddetli baş ağrısı varsa</li>
      </ul>
      <p class="soft">Bu belirtiler sinir hasarına işaret edebilir; beklemeden bir hekime ya da acil servise başvurun. Belirtileriniz bir hafta içinde düzelmediyse de hekiminize görünebilirsiniz.</p>
      {CTA_CARD("Boyun ağrınız", "boyun incinmesi (whiplash)")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(WH_SRC)}
    </div>
  </section>
</main>'''

page("boyun-incinmesi.html", "Boyun İncinmesi (Whiplash)",
     "Kaza ya da düşme sonrası boyun ağrısı mı? Whiplash ne kadar sürer, boyunluk takmalı mısınız, ne zaman hekime gitmelisiniz? Uyarı işaretleri ve evde altı egzersiz.",
     "boyun-incinmesi.html", NECK_CSS, WH_BODY, "",
     seo_title="Boyun İncinmesi (Whiplash): Belirtiler, İyileşme Süresi ve Egzersizler | İhsan Eren",
     condition="Whiplash", faq_items=WH_FAQ)
