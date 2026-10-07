# -*- coding: utf-8 -*-
# Yeni rehberler (10): sürekli üşüme (soğuğa duyarlılık). Belirti rehberi: önce tıbbi nedenler ve testler,
# sonra günlük önlemler, sonra tamamlayıcı yaklaşımlar için kanıtın ne dediği. Kullanıcı isteğiyle bu sayfada akupunktur geçmez (titreme sayfasında var).
# cond10_part.py'den sonra exec edilir. Bu sayfada bilerek "seans planla" kartı yok: ilk adım hekim muayenesi.

_ex2("cold_apump", "apump", "Ayak bileği pompası", "Otururken ayaklarınızı yerden hafifçe kaldırın. Ayak uçlarınızı kendinize doğru çekin, sonra ileri uzatın; ritmik ve canlı bir tempoda yapın.", "30 saniye, 2–3 tur")
_ex2("cold_heel", "heel2", "Tezgâha tutunarak topuk yükseltme", "Tezgâha hafifçe tutunun. İki topuğunuzu birlikte kaldırıp parmak uçlarınızda yükselin ve yavaşça inin. Baldır kaslarını çalıştırır, bacaklardaki dolaşımı hareketlendirir.", "15–20 tekrar")
_ex2("cold_hand", "tglide", "El açıp kapama", "Ellerinizi önünüze uzatın. Parmaklarınızı sıkıca yumruk yapın, sonra olabildiğince açıp gerin; canlı bir tempoda tekrarlayın.", "20 tekrar, 2 tur")

# ============================================================== SÜREKLİ ÜŞÜME
COLD_FAQ = [
 ("Testlerim normal çıktı ama hâlâ üşüyorum. Ne yapmalıyım?", "Normal testler sık görülen nedenleri dışlamaya yardımcı olur, ama şikâyetinizi geçersiz kılmaz. Bazı insanlar soğuğa yapısal olarak daha duyarlıdır. Günlük önlemleri birkaç hafta düzenli uygulayın. Şikâyet artarsa ya da kilo değişikliği, belirgin yorgunluk, parmaklarda renk değişikliği gibi yeni belirtiler eklenirse yeniden hekiminize başvurun."),
 ("Ellerim ve ayaklarım hep soğuk; bu Raynaud mu?", "Her soğuk el Raynaud değildir. Raynaud'da parmaklar soğukta ya da stres altında belirgin şekilde renk değiştirir, uyuşur, karıncalanır ya da ağrır; belirtiler dakikalar ile saatler arasında sürebilir. Renk değişikliği yoksa tablo Raynaud'dan çok soğuğa duyarlılığı düşündürür. Emin olmak için hekiminize danışın."),
 ("Tamamlayıcı yöntemler üşümeye iyi gelir mi?", "Kanıt sınırlı. Raynaud fenomeninde 20 çalışmayı inceleyen derlemeye göre biyogeribildirim işe yaramıyor; ısı koruyucu eldiven tek bir çalışmada yararlı bulundu; ginkgo, antioksidanlar ve yağ asitleri için anlamlı bir yarar gösterilemedi. Bir yöntem denemek isterseniz önce altta yatan nedenin araştırıldığından emin olun."),
 ("Egzersiz üşümeyi azaltır mı?", "Küçük bir çalışma bunu destekliyor: üşüyen 16 genç kadından iki hafta boyunca düzenli yürüyüş ve hafif koşu yapanlarda parmak uçları ve ayaklardaki üşüme hissi azaldı, uyku da iyileşti. Çalışma küçük olduğu için sonuç kesin sayılmaz; yine de düzenli hareket, denemeye değer güvenli bir adımdır."),
]

COLD_SRC = [
 "MedlinePlus. " + ext("https://medlineplus.gov/ency/article/003095.htm", "Cold intolerance") + ". US National Library of Medicine. Updated 27 February 2026.",
 "NHS. " + ext("https://www.nhs.uk/conditions/raynauds/", "Raynaud's") + ". Page last reviewed 20 July 2023.",
 "NHS. " + ext("https://www.nhs.uk/conditions/underactive-thyroid-hypothyroidism/symptoms/", "Underactive thyroid (hypothyroidism): symptoms") + ". Page last reviewed 28 April 2025.",
 "Malenfant D, Catton M, Pope JE. " + ext("https://pubmed.ncbi.nlm.nih.gov/19433434/", "The efficacy of complementary and alternative medicine in the treatment of Raynaud's phenomenon: a literature review and meta-analysis") + ". Rheumatology (Oxford). 2009;48(7):791-795.",
 "Yamazaki F, Inoue K, Ohmi N, Okimoto C. " + ext("https://link.springer.com/article/10.1186/s40101-023-00339-y", "A two-week exercise intervention improves cold symptoms and sleep condition in cold-sensitive women") + ". J Physiol Anthropol. 2023;42:22.",
]

COLD_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Sürekli üşüme (soğuğa duyarlılık)</h1>
    <p class="lede">Herkes üşürken üşümek doğaldır; ama çevrenizdekiler rahatken siz hep üşüyorsanız buna soğuğa duyarlılık denir. Çoğu zaman altta tiroid bezinin az çalışması, kansızlık ya da düşük kilo gibi bulunup düzeltilebilen bir neden vardır; bu yüzden ilk adım hekim muayenesi ve birkaç kan testidir. Bu rehber olası nedenleri, günlük önlemleri ve tamamlayıcı yöntemler için kanıtın ne dediğini özetliyor.</p>
    <p class="meta">Son güncelleme: 7 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>4 test</b><span>İlk aşamada çoğunlukla istenenler: tam kan sayımı, genel biyokimya, TSH ve tiroid hormonları</span></div>
        <div class="stat"><b>30 yaş</b><span>Parmaklarda renk değişikliği ilk kez bu yaştan sonra başladıysa hekime görünmek gerekir</span></div>
        <div class="stat"><b>2 hafta</b><span>Küçük bir çalışmada el ve ayak üşümesini azaltan yürüyüş ve hafif koşu programının süresi</span></div>
        <div class="stat"><b>20 çalışma</b><span>Raynaud'da tamamlayıcı yöntemleri inceleyen derleme; sonuçların çoğu kesin değil</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Neden hep üşürüm?</h2>
        <p class="soft">Vücut ısısını tiroid hormonları, kan dolaşımı, kas kütlesi ve deri altındaki yağ tabakası birlikte ayarlar. Bunlardan biri aksadığında aynı ortamda başkalarından daha çok üşürsünüz. Üşüme çoğu zaman tek başına bir hastalık değil, altta yatan bir durumun belirtisidir.</p>
        <p class="soft">Bu yüzden uzun süredir devam eden ya da aşırı üşümede ilk yapılacak şey hekime başvurmaktır. Neden bulunursa tedavi o nedene yöneliktir.</p>
      </div>
      <div>
        <h2>Olası nedenler</h2>
        <ul class="dots">
          <li>Tiroid bezinin az çalışması: üşümeye yorgunluk, kilo alma, kabızlık, cilt ve saç kuruluğu eşlik edebilir</li>
          <li>Kansızlık (anemi)</li>
          <li>Düşük kilo ve vücut yağının az olması; özellikle zayıf ve ileri yaştaki kadınlarda</li>
          <li>Raynaud fenomeni gibi damar sorunları</li>
          <li>Uzun süren ağır hastalıklar ve genel sağlık durumunun bozulması</li>
          <li>Yeme bozuklukları (anoreksiya nervoza)</li>
          <li>Nadiren, beynin ısı ayarını yapan bölgesiyle (hipotalamus) ilgili sorunlar</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>İlk adım: muayene ve testler</h2>
      <p class="soft">Hekiminiz öykünüzü dinler, muayene eder ve çoğunlukla şu testleri ister: tam kan sayımı, genel biyokimya, TSH ve tiroid hormonları. Öykünüze göre başka testler eklenebilir. Kullandığınız ilaçları da söyleyin; bazı ilaçlar parmaklardaki dolaşımı etkileyebilir.</p>
      <p class="soft">Soğukta ya da stres altında parmaklarınız belirgin şekilde renk değiştiriyor, uyuşuyor, karıncalanıyor ya da ağrıyorsa bu Raynaud fenomeni olabilir. Çoğu kişide zararsızdır; ancak belirtiler şiddetliyse, yalnızca tek taraftaysa, 30 yaşından sonra başladıysa ya da eklem ağrısı, cilt döküntüsü ve kas güçsüzlüğü eşlik ediyorsa altta yatan bir romatizmal hastalık açısından değerlendirilmelidir.</p>
      <div class="callout">
        <p>Testlerinizin normal çıkması şikâyetinizin gerçek olmadığı anlamına gelmez. Bazı insanlar soğuğa yapısal olarak daha duyarlıdır; aşağıdaki önlemler bu durumda da işe yarayabilir. Şikâyet değişir ya da yeni belirtiler eklenirse yeniden değerlendirilmek üzere hekiminize başvurun.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Günlük önlemler</h2>
      <ul class="tx">
        <li><b>Sıcak tutun</b><span>Soğuk havada sıcak giyinin, özellikle ellerinizi ve ayaklarınızı koruyun; evinizi ılık tutun.</span></li>
        <li><b>Ani ısı değişikliği</b><span>Sıcak ortamdan soğuğa birden çıkmaktan kaçının; dışarı çıkmadan önce giyinin.</span></li>
        <li><b>Düzenli hareket</b><span>Düzenli egzersiz dolaşımı destekler. Üşüyen 16 genç kadınla yapılan küçük bir çalışmada, iki hafta boyunca haftada en az dört gün yürüyüş ve hafif koşu yapanlarda parmak uçları ve ayaklardaki üşüme hissi azaldı; cilt sıcaklığı ise değişmedi.</span></li>
        <li><b>Sigara</b><span>Sigara dolaşımı olumsuz etkiler; bırakmak için hekiminizden destek isteyin.</span></li>
        <li><b>Kafein</b><span>Çay, kahve, kola ve çikolatadaki kafeini azaltmak bazı kişilerde belirtileri hafifletebilir.</span></li>
        <li><b>Gevşeme</b><span>Stres ve kaygı belirtileri tetikleyebilir; nefes egzersizleri ya da yoga gibi gevşeme yöntemlerini deneyin.</span></li>
        <li><b>Beslenme</b><span>Dengeli ve yeterli beslenin; çok düşük kilo üşümeyi artırır.</span></li>
      </ul>
      <p class="soft" style="margin-top:14px">Nefesle gevşemek için <a href="ic-cekis.html">5 dakikalık iç çekiş nefesi</a>, haftalık hareketinizi görmek için <a href="hareket.html">Haftalık hareket ölçer</a> sayfasına bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tamamlayıcı yaklaşımlar: kanıt ne diyor?</h2>
      <p class="soft">Tamamlayıcı yöntemler en çok Raynaud fenomeninde araştırıldı. 20 rastgele kontrollü çalışmayı inceleyen derlemeye göre:</p>
      <ul class="dots">
        <li>Biyogeribildirim: beş çalışmada işe yaramadı; sonuçlar sahte uygulamadan daha iyi değildi.</li>
        <li>Isı koruyucu (terapötik) eldiven: tek bir çalışmada yararlı bulundu; sonucun genellenebilirliği sınırlı.</li>
        <li>Düşük düzeyli lazer: üç çalışmada atak sayısını biraz azalttı; farkın klinik önemi belirsiz.</li>
        <li>Ginkgo biloba, antioksidanlar ve esansiyel yağ asitleri: anlamlı bir yarar gösterilemedi ya da veri yetersiz.</li>
      </ul>
      <p class="soft" style="margin-top:14px">Derlemenin sonucu açık: iyi tasarlanmış çalışmalara ihtiyaç var ve biyogeribildirimin işe yaramadığı dışında kesin bir şey söylenemiyor. Bitkisel ürünler ilaçlarla etkileşebilir; kullanmadan önce hekiminize ya da eczacınıza danışın.</p>
      <div class="callout">
        <p>Tamamlayıcı bir yöntem denemek isterseniz önce altta yatan nedenin araştırıldığından emin olun ve yöntemi tıbbi tedavinin yerine değil, yanında düşünün.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Isınmak için altı hareket</h2>
      <p class="soft">Kaslar çalışırken ısı üretir. Üşüdüğünüzde yerinizde durmak yerine birkaç dakika hareket edin; bu hareketler evde ya da masa başında yapılabilir.</p>
      {ex_grid(["cold_apump", "cold_heel", "cold_hand", "fb_sts", "cr_wall", "cr_walk"])}
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Raynaud fenomeni için videolar</h2>
      <p class="soft">ABD'deki Johns Hopkins Romatoloji bölümünün ve Avera Health'in YouTube kanallarından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("Jv0kEFCYF5M", "Raynaud fenomeni videosunu oynat", "Raynaud's Phenomenon : What You Should Know | Johns Hopkins Medicine")}
          <h3>Raynaud fenomeni: bilmeniz gerekenler</h3>
          <p>Johns Hopkins Romatoloji'nin hastalar için hazırladığı bilgilendirme videosu.</p>
        </div>
        <div class="vid">
          {vbox("yjG_BmcfpNo", "Raynaud fenomeni nedir videosunu oynat", "What is Raynaud's Phenomenon?")}
          <h3>Raynaud fenomeni nedir?</h3>
          <p>Raynaud fenomenini tanıtan kısa video.</p>
        </div>
      </div>
      <p class="meta">Videolar Johns Hopkins Rheumatology ve Avera Health kanallarına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(COLD_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Parmaklarda geçmeyen beyazlık ya da morluk, yara ya da siyahlaşma (acil)</li>
        <li>Soğukta kalmanın ardından durdurulamayan titreme, bilinç bulanıklığı ya da konuşmada yavaşlama (acil)</li>
        <li>Üşümeyle birlikte açıklanamayan kilo değişikliği ya da belirgin yorgunluk</li>
        <li>Parmaklardaki renk değişikliğinin yalnızca tek tarafta olması ya da 30 yaşından sonra başlaması</li>
        <li>Eklem ağrısı, cilt döküntüsü ya da kas güçsüzlüğünün eşlik etmesi</li>
        <li>Yürürken baldırlarda ağrı ve ayaklarda soğukluk ya da renk değişikliği</li>
      </ul>
      <div class="note" style="margin-top:22px"><strong>Bu rehberin sınırı:</strong> Üşümenin nedenini bulmak hekim muayenesi ve test gerektirir. Buradaki önlemler tanının ve tedavinin yerini tutmaz; onları tamamlar.</div>
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(COLD_SRC)}
    </div>
  </section>
</main>'''

page("surekli-usume.html", "Sürekli Üşüme (Soğuğa Duyarlılık)",
     "Herkes rahatken siz neden üşüyorsunuz? Tiroid, kansızlık ve Raynaud gibi olası nedenler, istenen testler, günlük önlemler ve tamamlayıcı yöntemler için kanıtın ne dediği.",
     "surekli-usume.html", NECK_CSS, COLD_BODY, YT_JS,
     seo_title="Sürekli Üşüme: Nedenleri, Testler ve Yapılabilecekler | İhsan Eren",
     condition="Soğuğa duyarlılık", faq_items=COLD_FAQ)
