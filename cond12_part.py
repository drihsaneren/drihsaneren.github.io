# -*- coding: utf-8 -*-
# Yeni rehberler (11): titreme (tremor). Belirti rehberi: türler ve tıbbi araştırma, tedavi, günlük hayat önerileri,
# tamamlayıcı yaklaşımlar için kanıt (akupunktur: umut verici ama kesinliği düşük; hizmet olarak sunulmaz).
# cond11_part.py'den sonra exec edilir. Videolar IETF ve VCU Health kanallarından (oEmbed ile doğrulandı).

_ex2("tr_grip", "grip", "Top sıkma", "Elinize yumuşak bir top ya da rulo yapılmış bir havlu alın. Sıkın, 3–5 saniye tutun ve yavaşça bırakın.", "10 tekrar, 2 set")
_ex2("tr_wrist", "eccwe", "Ağırlıkla bilek kaldırma", "Ön kolunuzu masaya koyun, avucunuz aşağı baksın. Elinize dolu bir su şişesi ya da hafif bir ağırlık alın. Bileğinizi yukarı kaldırın, 3–4 saniyede yavaşça indirin. Sonra avucunuzu yukarı çevirip aynı hareketi yapın.", "8–10 tekrar, 2 set")
_ex2("tr_iso", "isowe", "İzometrik bilek bastırma", "Ön kolunuzu masaya koyun. Bileğinizi yukarı kaldırmaya çalışırken diğer elinizle üstünden bastırın; el yerinden oynamasın. 5 saniye tutup gevşeyin.", "8 tekrar")
_ex2("tr_breath", "plb", "Yavaş nefes", "Rahatça oturun, omuzlarınızı gevşetin. Burnunuzdan sakin bir nefes alın; dudaklarınızı hafifçe büzerek, aldığınızdan daha uzun sürede verin. Heyecan ve gerginlik titremenizi artırdığında kullanın.", "5–10 nefes")

# ============================================================== TİTREME
TR_FAQ = [
 ("Ellerim titriyor; Parkinson mu?", "Titreyen her el Parkinson değildir. Parkinson titremesi çoğunlukla el dinlenirken görülür; en sık tür olan esansiyel tremorda ise el bir iş yaparken titrer. Ayrımı muayeneyle nöroloji hekimi yapar; titremeniz zamanla artıyorsa başvurun."),
 ("Testlerim normal çıktı; titremem neden geçmiyor?", "Normal testler tiroid ve kan şekeri gibi nedenleri dışlamaya yardımcı olur. Bu durumda sık karşılaşılan iki olasılık artmış fizyolojik titreme ve esansiyel tremordur. Kafein, uykusuzluk, stres ve kullandığınız ilaçlar gibi tetikleyicileri gözden geçirin; titreme günlük hayatınızı etkiliyorsa nöroloğunuzla ilaç seçeneklerini konuşun."),
 ("Akupunktur titremeye iyi gelir mi?", "Esansiyel tremorda 20 çalışmayı birleştiren bir derleme iyileşme bildiriyor; ancak çalışmaların tümü Çin'de yapılmış, küçük ve körleme yok. Kanıt umut verici ama kesin değil. Denemek isterseniz nöroloğunuzun önerdiği tedavinin yerine değil, yanında düşünün. Türkiye'de akupunkturu yalnızca bu alanda sertifikası olan hekimler uygulayabilir."),
 ("Egzersiz titremeyi artırır mı?", "Yorgunluk titremeyi geçici olarak artırabilir; bu zararlı değildir. Küçük çalışmalarda altı haftalık kol güçlendirme programı esansiyel tremorda el becerisini iyileştirdi. Hareketleri oturarak, yavaş ve kontrollü yapın."),
]

TR_SRC = [
 "National Institute of Neurological Disorders and Stroke. " + ext("https://www.ninds.nih.gov/health-information/disorders/tremor", "Tremor") + ". Last reviewed 23 July 2026.",
 "NHS. " + ext("https://www.nhs.uk/conditions/tremor-or-shaking-hands/", "Tremor or shaking hands") + ". Page last reviewed 14 November 2023.",
 "Kavanagh JJ, Wedderburn-Bisshop J, Keogh JWL. " + ext("https://research.bond.edu.au/en/publications/resistance-training-reduces-force-tremor-and-improves-manual-dext/", "Resistance training reduces force tremor and improves manual dexterity in older individuals with essential tremor") + ". J Mot Behav. 2016;48(1):20-30.",
 "Sequeira G, Keogh JW, Kavanagh JJ. " + ext("https://research.bond.edu.au/en/publications/resistance-training-can-improve-fine-manual-dexterity-in-essentia/", "Resistance training can improve fine manual dexterity in essential tremor patients: a preliminary study") + ". Arch Phys Med Rehabil. 2012;93(8):1466-1468.",
 "Shen M, Shi Q, Han J, Chen B, Gao S. " + ext("https://www.mdpi.com/2227-9032/14/6/803", "Comparative efficacy of acupuncture therapy in primary essential tremor: a network meta-analysis and systematic review") + ". Healthcare. 2026;14(6):803.",
 ext("https://www.alomaliye.com/2014/10/27/geleneksel-ve-tamamlayici-tip-uygulamalari-yonetmeligi/", "Geleneksel ve Tamamlayıcı Tıp Uygulamaları Yönetmeliği") + ". Resmî Gazete, 27 Ekim 2014, sayı 29158.",
]

TR_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Titreme (tremor)</h1>
    <p class="lede">Ellerin hafifçe titremesi herkeste vardır; yorgunluk, heyecan ve kafeinle belirginleşir. Titreme zamanla artıyor ya da yazı yazmak, bardak tutmak gibi günlük işleri zorlaştırıyorsa nedeni araştırılmalıdır. Bu rehber titreme türlerini, hekimin neleri araştırdığını, günlük hayatı kolaylaştıran yolları ve tamamlayıcı yöntemler için kanıtın ne dediğini özetliyor.</p>
    <p class="meta">Son güncelleme: 7 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>7 tür</b><span>ABD Ulusal Nörolojik Hastalıklar Enstitüsü'nün ayırdığı titreme türleri; tedavi türe göre değişir</span></div>
        <div class="stat"><b>%50–70</b><span>En sık tür olan esansiyel tremorda kalıtsal olan vakaların oranı</span></div>
        <div class="stat"><b>6 hafta</b><span>Küçük çalışmalarda el becerisini iyileştiren kol güçlendirme programının süresi</span></div>
        <div class="stat"><b>20 çalışma</b><span>Esansiyel tremorda akupunkturu inceleyen derleme; hepsi Çin'de yapılmış, kanıt kesin değil</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Titreme (tremor), vücudun bir ya da birkaç bölümünde, en sık ellerde görülen istem dışı sallanma hareketidir. Tek başına bir durum olabileceği gibi başka bir hastalığın ya da bir ilacın belirtisi de olabilir.</p>
        <p class="soft">Hafif bir titreme normaldir. Yaş, stres, yorgunluk, kaygı, öfke, kafein, alkol, sigara ve aşırı sıcak ya da soğuk titremeyi artırabilir.</p>
      </div>
      <div>
        <h2>Başlıca türler</h2>
        <ul class="dots">
          <li>Esansiyel tremor: eller bir iş yaparken titrer; vakaların %50–70'i kalıtsaldır</li>
          <li>Artmış fizyolojik titreme: nörolojik bir hastalıktan değil; bazı ilaçlar, alkol yoksunluğu, tiroid bezinin fazla çalışması ya da kan şekeri düşüklüğünden kaynaklanır</li>
          <li>Parkinson titremesi: çoğunlukla el dinlenirken görülür</li>
          <li>Distonik titreme: istem dışı kas kasılmalarıyla birlikte; boyunda, ses tellerinde ya da kol ve bacaklarda</li>
          <li>Serebellar titreme: beyinciğin hasarına bağlı; hareketin sonunda artan yavaş ve geniş titreme</li>
          <li>İşlevsel titreme: dikkat verildiğinde artan, dikkat dağıldığında azalan değişken titreme</li>
          <li>Ortostatik titreme: nadir; ayakta dururken bacaklarda</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Nedeni nasıl araştırılır?</h2>
      <p class="soft">Titremeniz zamanla kötüleşiyorsa ya da günlük işlerinizi etkiliyorsa hekime başvurun. Hekim titremenin ne zaman ortaya çıktığına (dinlenirken mi, bir iş yaparken mi), nerede olduğuna, başka belirtilere, kullandığınız ilaçlara ve ailenizde benzer bir durum olup olmadığına bakar. Nörolojik muayenenin yanında kan ve idrar testleri, gerekirse görüntüleme ve kas-sinir ölçümü (EMG) istenebilir.</p>
      <p class="soft">Testler normal çıktığında sık karşılaşılan iki olasılık kalır: artmış fizyolojik titreme ve esansiyel tremor. İlki tetikleyiciler azaltılınca hafifleyebilir; ikincisinde ilaçlar titremeyi tamamen geçirmese de çoğu zaman azaltır. Titremenizin biçimi değişirse yeniden değerlendirilmeniz gerekir.</p>
      <div class="callout">
        <p>İlaçlarınızı kendi başınıza kesmeyin. Titremenizin bir ilaçla ilişkili olabileceğini düşünüyorsanız bunu hekiminizle konuşun; doz ayarı ya da ilaç değişikliği bir seçenek olabilir.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <ul class="tx">
        <li><b>İlaçlar</b><span>Titremenin türüne göre beta blokerler, nöbet ilaçları ve başka ilaç grupları kullanılır; seçimi nöroloğunuz yapar. İlaçlar titremeyi tamamen geçirmez, ama çoğu zaman azaltır.</span></li>
        <li><b>İğne tedavisi</b><span>Baş ve ses titremesinde sinir iletimini azaltan botulinum toksini iğneleri kullanılabilir.</span></li>
        <li><b>Girişimsel yöntemler</b><span>İlaca yanıt vermeyen ağır titremede derin beyin uyarımı ya da odaklanmış ultrason gibi yöntemler nadiren gündeme gelir.</span></li>
        <li><b>Fizyoterapi ve iş-uğraşı terapisi</b><span>Kas kontrolünü, gücü ve dengeyi geliştirmeye; yazmak ve yemek yemek gibi işleri kolaylaştıran yöntem ve araçları öğrenmeye yardımcı olur.</span></li>
        <li><b>Güçlendirme egzersizi</b><span>Esansiyel tremorlu 10 yaşlı yetişkinle yapılan küçük bir çalışmada 6 haftalık kol güçlendirme programı el becerisini iyileştirdi ve daha çok etkilenen kolda kuvvet titremesini azalttı; altı kişilik bir ön çalışmada da el becerisi arttı. Çalışmalar çok küçük olduğu için bunlar ön bulgudur.</span></li>
        <li><b>Yaşam biçimi</b><span>Kafeini azaltmak, stresi yönetmek ve yeterince uyumak titremeyi hafifletebilir.</span></li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Günlük hayatı kolaylaştıran yollar</h2>
      <ul class="dots">
        <li>Bardağı yarısına kadar doldurun, iki elinizle tutun ya da kapaklı ve pipetli bardak kullanın.</li>
        <li>Yemek yerken ve yazarken dirseğinizi masaya ya da gövdenize dayayın.</li>
        <li>Kalın ve ağır saplı çatal-kaşık ile kalın gövdeli kalem deneyin.</li>
        <li>Düğme ve bağcık yerine cırt cırtlı ya da fermuarlı giysi ve ayakkabıları seçin.</li>
        <li>İnce iş gerektiren şeyleri titremenizin en az olduğu saatlere bırakın ve acele etmeyin.</li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tamamlayıcı yaklaşımlar: kanıt ne diyor?</h2>
      <p class="soft">Esansiyel tremorda akupunkturu inceleyen 2026 tarihli bir derleme, 1.067 katılımcılı 20 rastgele kontrollü çalışmayı birleştirdi ve akupunktur uygulanan gruplarda titreme puanlarında iyileşme bildirdi. Ancak çalışmaların tümü Çin'de yapılmış; yazarların kendisi de örneklemlerin küçük olduğunu, körleme yapılmadığını ve katılımcıların gruplara dağıtımının yeterince gizlenmediğini belirtiyor. Bu yüzden sonuç umut verici bir ön bulgu sayılmalı; kesin konuşmak için daha sağlam çalışmalar gerekiyor.</p>
      <p class="soft">Gevşeme ve nefes çalışmaları titremenin kendisini tedavi etmez; ancak stres ve kaygı titremeyi artırdığı için tetikleyiciyi azaltmaya yardımcı olabilir.</p>
      <div class="callout">
        <p>Türkiye'de akupunktur gibi geleneksel ve tamamlayıcı tıp uygulamalarını yalnızca ilgili alanda uygulama sertifikası olan hekimler, Sağlık Bakanlığınca yetkilendirilmiş birimlerde yapabilir. Tamamlayıcı bir yöntem denemek isterseniz önce altta yatan nedenin araştırıldığından emin olun ve yöntemi tıbbi tedavinin yerine değil, yanında düşünün.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Titreme için altı egzersiz</h2>
      <p class="soft">Amaç titremeyi durdurmak değil; kol ve el kaslarını güçlendirmek, el becerisini korumak ve gerginliği azaltmaktır. Hareketleri yavaş yapın; yorgunluk titremenizi artırırsa ara verin.</p>
      {ex_grid(["tr_grip", "tr_wrist", "tr_iso", "copd_row", "cold_hand", "tr_breath"])}
      <div class="callout">
        <p>Ağırlık kullandığınız hareketleri, düşürme riskine karşı masada ve oturarak yapın.</p>
      </div>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Titreme için videolar</h2>
      <p class="soft">Uluslararası Esansiyel Tremor Vakfı'nın (IETF) ve ABD'deki VCU Health'in YouTube kanallarından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("z-nBScb735E", "Esansiyel tremor videosunu oynat", "Essential Tremor is more than a tremor")}
          <h3>Esansiyel tremor bir titremeden fazlasıdır</h3>
          <p>Vakfın esansiyel tremoru tanıtan videosu.</p>
        </div>
        <div class="vid">
          {vbox("WwIsROk3QA8", "Esansiyel tremorda belirtiler videosunu oynat", "Range of Symptoms in Essential Tremor")}
          <h3>Esansiyel tremorda belirtilerin yelpazesi</h3>
          <p>Belirtilerin kişiden kişiye nasıl değiştiğini konu alan video.</p>
        </div>
      </div>
      <p class="meta">Videolar International Essential Tremor Foundation ve VCU Health kanallarına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(TR_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Aniden başlayan titreme; özellikle konuşma bozukluğu, yüzde kayma ya da kol ve bacakta güçsüzlükle birlikteyse (acil)</li>
        <li>Alkolü bıraktıktan sonraki günlerde titreme, terleme ve huzursuzluk (acil)</li>
        <li>Yeni bir ilaca başladıktan ya da doz değiştikten sonra ortaya çıkan titreme</li>
        <li>Titremeyle birlikte çarpıntı, terleme ve kilo kaybı</li>
        <li>Yürüme ve denge bozukluğu ya da hareketlerde yavaşlama</li>
        <li>Zamanla artan ve günlük işlerinizi engelleyen titreme</li>
      </ul>
      {CTA_CARD("Titremeye bağlı günlük yaşam güçlükleriniz", "titreme")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(TR_SRC)}
    </div>
  </section>
</main>'''

page("titreme.html", "Titreme (Tremor)",
     "Eller neden titrer? Esansiyel tremor ve diğer titreme türleri, nedenin nasıl araştırıldığı, tedavi, günlük hayat önerileri, egzersizler ve akupunktur için kanıtın ne dediği.",
     "titreme.html", NECK_CSS, TR_BODY, YT_JS,
     seo_title="Titreme (Tremor): Nedenleri, Tedavi ve Günlük Öneriler | İhsan Eren",
     condition="Tremor", faq_items=TR_FAQ)
