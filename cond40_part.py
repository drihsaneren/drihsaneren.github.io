# -*- coding: utf-8 -*-
# Yeni rehber (40): Eklem hipermobilitesi (eklem gevşekliği). cond39_part.py'den sonra exec edilir. Video yok.
# Egzersizler hazır çizimlerle; güç, denge ve eklemi sona kadar zorlamamaya odaklı.

_ex2("jh_sls", "sls", "Tek ayak üzerinde durma", "Tezgâhın önünde dik durun, gerekirse bir elinizle hafifçe tutunun. Bir ayağınızı kaldırın; duran bacağınızın dizini geriye kilitlemeden, hafif bükük tutun. Kolaylaşınca tutunmadan ya da gözleriniz kapalı deneyin. Eklem konum duyusunu ve dengeyi geliştirir.", "30 saniye, her ayakla 3 kez")
_ex2("jh_bridge", "bridge", "Köprü", "Sırtüstü yatın, dizleriniz bükülü, ayaklarınız yerde. Kalçanızı sıkarak kaldırın; omuzlarınızdan dizlerinize kadar düz bir çizgi oluşsun, belinizi fazla çukurlaştırmayın. 3–5 saniye bekleyip yavaşça inin.", "10–15 tekrar, 2–3 set")
_ex2("jh_birddog", "birddog", "Kuş-köpek", "Ellerinizin ve dizlerinizin üzerinde durun; dirseklerinizi geriye kilitlemeyin, hafif bükük tutun. Bir kolunuzu öne, karşı bacağınızı arkaya uzatın; beliniz çukurlaşmasın, kalçanız dönmesin. 5 saniye tutup değiştirin.", "Her iki yana 8–10 tekrar")
_ex2("jh_wall", "wall", "Duvarda yarım çömelme", "Sırtınızı duvara yaslayın, ayaklarınızı duvardan yarım adım öne alın. Dizleriniz ayak uçlarınızla aynı yöne baksın, içe kaçmasın. Yavaşça biraz çömelin ve doğrulun; doğrulurken dizlerinizi geriye kilitlemeyin.", "10 tekrar, 2–3 set")
_ex2("jh_scap", "scap", "Kürek kemiği sıkıştırma", "Dik durun ya da oturun. Omuzlarınızı kulaklarınıza kaldırmadan kürek kemiklerinizi geriye ve biraz aşağıya doğru birbirine yaklaştırın. 5 saniye tutup bırakın. Omuz eklemini çevresindeki kaslarla desteklemeye yardım eder.", "10–15 tekrar, günde 2 kez")
_ex2("jh_walk", "walk", "Düşük darbeli hareket", "Yürüyüş, yüzme ve bisiklet gibi eklemleri az zorlayan aktivitelerle başlayın. Süreyi yavaş yavaş artırın ve gün içine düzenli molalar koyun; iyi bir günde aşırıya kaçıp ertesi gün çökmemeye çalışın.", "10 dakikayla başlayın, her hafta birkaç dakika artırın")

JH_FAQ = [
 ("Esnek olmak hastalık mı?", "Hayır. Eklemleri esnek olan birçok kişinin hiçbir şikâyeti yoktur. Ancak bazı kişilerde esneklik ağrı, sık burkulma ya da çıkıklar ve yorgunlukla birlikte görülür; bu durumda eklem hipermobilite sendromu ya da hipermobilite spektrum bozukluğu adı kullanılır."),
 ("Beighton puanı nedir?", "Hekimlerin eklem hareketliliğini değerlendirmek için kullandığı 9 puanlık basit bir muayenedir: serçe parmağın geriye 90 dereceden fazla bükülmesi, başparmağın ön kola değmesi, dirseğin ve dizin 10 dereceden fazla geriye açılması (her biri sağ ve sol için birer puan) ve dizler düzken avuçların yere düz basması (bir puan). 2017 uluslararası ölçütlerine göre yaygın eklem hipermobilitesi için eşik, çocuk ve ergenlerde 6, 50 yaşına kadar yetişkinlerde 5, 50 yaş üstünde 4 puandır. Bu bir kendi kendine tanı testi değildir; tanıyı bir hekim koyar."),
 ("Esneme egzersizleri yapmalı mıyım?", "Eklemleriniz zaten fazla açılıyorsa, onları sona kadar zorlayan esnemeler genellikle önerilmez. Amaç esnekliği artırmak değil, eklemleri çevresindeki kaslarla güçlendirip korumaktır. Aynı hareketi uzun süre tekrarlamaktan da kaçınmanız önerilir."),
 ("Egzersizin yararı kanıtlanmış mı?", "Kanıtlar sınırlı ama umut verici. Az sayıdaki çalışmada güç, denge ve dayanıklılık egzersizleri ağrıyı azalttı ve gücü artırdı; ancak hangi egzersiz türünün en iyi olduğu henüz bilinmiyor. Bu yüzden program kişiye göre, kademeli artırılarak hazırlanır. Omuz yakınmaları olan hipermobil yetişkinlerle yapılmış 4 çalışmayı inceleyen 2024 tarihli bir derlemede egzersiz programları ağrı, omuz dengesizliği, günlük işler ve kas gücünde olumlu değişiklikler gösterdi; ancak en etkili egzersiz türü ve dozu konusunda bilgi hâlâ eksik."),
]

JH_SRC = [
 "NHS. " + ext("https://www.nhs.uk/conditions/joint-hypermobility/", "Joint hypermobility syndrome") + ". Page last reviewed 30 August 2023.",
 "Engelbert RHH, Juul-Kristensen B, Pacey V, et al. " + ext("https://discovery-pp.ucl.ac.uk/id/eprint/1556240/1/Engelbert_Evidence-Based_Rationale.pdf", "The evidence-based rationale for physical therapy treatment of children, adolescents and adults diagnosed with joint hypermobility syndrome/hypermobile Ehlers Danlos syndrome") + ". American Journal of Medical Genetics Part C. 2017.",
 "Castori M, Tinkle B, Levy H, Grahame R, Malfait F, Hakim A. " + ext("https://www.ehlers-danlos.com/2017-eds-classification-non-experts/framework-classification-joint-hypermobility-related-conditions/", "A framework for the classification of joint hypermobility and related conditions") + ". Am J Med Genet C Semin Med Genet. 2017;175(1):148–157.",
 "Malfait F, Francomano C, Byers P, et al. " + ext("https://www.ehlers-danlos.com/wp-content/uploads/2017/03/2017-EDS-Classification_March_2017.pdf", "The 2017 international classification of the Ehlers–Danlos syndromes") + ". Am J Med Genet C Semin Med Genet. 2017;175(1):8–26",
 "Higo A, Palmer S, Liaghat B, Tallis J, Silvester L, Pearce G. " + ext("https://doaj.org/article/2ffea81c31d4445094184b2a4327f497", "The effectiveness of conservative interventions on pain, function, and quality of life in adults with hypermobile Ehlers-Danlos syndrome/hypermobility spectrum disorders and shoulder symptoms: a systematic review") + ". Arch Rehabil Res Clin Transl. 2024;6(3):100360.",
]

JH_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Eklem hipermobilitesi (eklem gevşekliği)</h1>
    <p class="lede">Çocukluğunuzdan beri “lastik gibi” esnek misiniz, ama eklemleriniz sık ağrıyor, ayak bileğiniz kolay burkuluyor, çabuk yoruluyor musunuz? Eklem hipermobilitesinde eklemleri destekleyen bağlar daha gevşektir. Birçok kişide hiçbir sorun yapmaz; şikâyet olduğunda ise en etkili yol, eklemleri çevresindeki kaslarla güçlendirmek ve günlük yükü dengeli dağıtmaktır.</p>
    <p class="meta">Son güncelleme: 14 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>9 puan</b><span>Eklem esnekliğini değerlendiren Beighton muayenesinin toplam puanı</span></div>
        <div class="stat"><b>5 ve üzeri</b><span>50 yaşına kadar yetişkinlerde uluslararası eşik puan (50 yaş üstünde 4, çocuklarda 6)</span></div>
        <div class="stat"><b>%30–55</b><span>Fizyoterapiye kas-iskelet şikâyetiyle başvuran yetişkinlerde bildirilen oran</span></div>
        <div class="stat"><b>Güç ve denge</b><span>Tedavinin temeli: eklemleri kaslarla desteklemek</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Ne zaman sorun olur?</h2>
        <ul class="dots">
          <li>Dinlenmeye rağmen sık yorgunluk.</li>
          <li>Süregen eklem ya da kas ağrısı ve tutukluk.</li>
          <li>Tekrarlayan burkulma ve zorlanmalar.</li>
          <li>Eklemlerin yerinden çıkması ya da “kayması”.</li>
          <li>Denge ve koordinasyonda zayıflık.</li>
          <li>İnce, esnek cilt; mesane ya da bağırsak sorunları.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Eklemleri destekleyen bağların yapısındaki kolajenin farklı olması nedeniyle bağlar gevşek ve esnektir.</li>
          <li>Ailede görülebilir; önlenemez.</li>
          <li>Ehlers-Danlos sendromunu da içeren bir hipermobilite yelpazesinin parçası olarak görülür.</li>
          <li>En çok çocuk ve gençleri etkiler; belirtiler yaşla birlikte azalabilir.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Güçlendirin</h3><p>Hareketsizlik belirtileri kötüleştirebilir. Yüzme, bisiklet gibi düşük darbeli egzersizlerle yavaş başlayıp kas gücünü ve kondisyonu artırabilirsiniz.</p></div>
        <div class="kind"><span class="n">2</span><h3>Zorlamayın</h3><p>Eklemlerinizi sona kadar germekten ve aynı hareketi uzun süre tekrarlamaktan kaçının. Dirsek ve dizleri geriye kilitlememeye dikkat edin.</p></div>
        <div class="kind"><span class="n">3</span><h3>Temponuzu ayarlayın</h3><p>Gün içine düzenli molalar koyun. İyi bir günde her şeyi yapıp ertesi gün çökmek yerine, işleri güne yaymayı deneyin.</p></div>
        <div class="kind"><span class="n">4</span><h3>Destekleyin</h3><p>Sağlıklı kiloyu korumak, ayağı destekleyen ayakkabılar ve gerekirse bir ayak uzmanının önerdiği tabanlıklar eklemlerin yükünü azaltır. Ilık banyo ya da sıcak su torbası tutukluğu rahatlatabilir.</p></div>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Eklemleri koruyan altı egzersiz</h2>
      <p class="soft">Az tekrarla, kontrollü ve yavaş başlayın; hareketleri eklemin orta açıklığında yapın, sona kadar zorlamayın. Ertesi gün ağrı ya da yorgunluk belirgin artıyorsa miktarı azaltın, sonra yeniden yavaşça artırın.</p>
      {ex_grid(["jh_sls", "jh_bridge", "jh_birddog", "jh_wall", "jh_scap", "jh_walk"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(JH_FAQ)}
      <p class="soft" style="margin-top:18px">Sık çıkık ve yaygın ağrı için <a href="omuz-cikigi.html">omuz çıkığı</a>, <a href="ayak-bilegi-burkulmasi.html">ayak bileği burkulması</a> ve <a href="fibromiyalji.html">fibromiyalji</a> rehberlerine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Kendinizde ya da çocuğunuzda eklem hipermobilitesinden şüpheleniyor ve ağrı, yorgunluk ya da sık burkulma yaşıyorsanız</li>
        <li>Eklemleriniz sık sık yerinden çıkıyorsa</li>
        <li>Ağrı şiddetliyse ve günlük yaşamınızı kısıtlıyorsa</li>
        <li>Ayağa kalkınca baş dönmesi, çarpıntı ya da bayılma hissi oluyorsa</li>
      </ul>
      {CTA_CARD("Eklem ağrılarınız", "eklem hipermobilitesi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(JH_SRC)}
    </div>
  </section>
</main>'''

page("eklem-hipermobilitesi.html", "Eklem Hipermobilitesi (Eklem Gevşekliği)",
     "Eklemleriniz çok esnek, ama sık ağrıyor, burkuluyor ya da yoruluyor musunuz? Eklem hipermobilitesi nedir, Beighton puanı neyi gösterir, hangi egzersizler eklemleri korur?",
     "eklem-hipermobilitesi.html", NECK_CSS, JH_BODY, "",
     seo_title="Eklem Hipermobilitesi (Eklem Gevşekliği): Belirtiler, Beighton Puanı ve Egzersizler | İhsan Eren",
     condition="Eklem hipermobilite sendromu / hipermobilite spektrum bozukluğu", faq_items=JH_FAQ)
