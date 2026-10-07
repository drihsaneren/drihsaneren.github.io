# -*- coding: utf-8 -*-
# Yeni rehberler (7): KOAH'ta akciğer rehabilitasyonu.
# cond7_part.py'den sonra exec edilir. Videolar Bob & Brad dışı kaynaklardan (kullanıcı izniyle: düzenli yayın yapan
# güvenilir kurum kanalları); kimlikler YouTube oEmbed ile doğrulandı (başlık + kanal adı).

# ---- yeni çizimler -----------------------------------------------------------------
# Büzük dudak nefesi: sandalyede dik oturan kişi, ağızdan uzun ve yavaş nefes verir (altın çizgiler).
SV["plb"] = fig(GRD + CHAIR_L +
    '<path class="fig" d="M46 74 H80 V112"/>'
    '<path class="fig hl" d="M46 74 L48 42"/><circle class="hd" cx="50" cy="33" r="8"/>'
    '<path class="fig" d="M48 48 L60 62 L72 66"/>'
    '<g><animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.3;0.42;0.9;1" dur="6s" repeatCount="indefinite"/>'
    '<animateTransform attributeName="transform" type="translate" values="0 0;0 0;8 0" keyTimes="0;0.3;1" dur="6s" repeatCount="indefinite"/>'
    '<path d="M62 35 H73 M63 30 L73 27 M63 40 L73 43" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round"/></g>',
    "Büzük dudak nefesi")

# Öne eğilerek toparlanma: gövde hafif öne eğik, ön kollar uyluklarda; gövde nefesle hafifçe oynar.
SV["fwdlean"] = fig(GRD + CHAIR_L +
    '<path class="fig" d="M46 74 H80 V112"/>'
    f'<g>{anim_t("32 46 74;28 46 74;32 46 74", typ="rotate", dur="5s")}'
    '<path class="fig hl" d="M46 74 L48 42"/><circle class="hd" cx="50" cy="33" r="8"/></g>'
    '<path class="fig" d="M61 54 L68 66 L78 71"/>',
    "Öne eğilerek toparlanma")

EXT["plb"] = ("Büzük dudak nefesi", "Burnunuzdan sakin bir nefes alın. Dudaklarınızı mum üfler gibi büzün ve nefesinizi, alırken harcadığınız sürenin yaklaşık iki katı sürede yavaşça verin. Zorlamayın; yanaklarınız şişmesin. Yürürken, merdiven çıkarken ve nefes darlığı anında kullanın.", "5–10 nefes, gün içinde gerektikçe")
EXT["fwdlean"] = ("Öne eğilerek toparlanma", "Nefes darlığınız arttığında oturun, gövdenizi hafifçe öne eğin ve ön kollarınızı uyluklarınıza dayayın. Omuzlarınızı gevşetin; soluğunuz yatışana kadar büzük dudak nefesiyle bekleyin. Ayaktaysanız bir duvara ya da tezgâha yaslanarak da yapabilirsiniz.", "Nefesiniz yatışana kadar")
_ex2("copd_sts", "sts", "Sandalyeden kalkıp oturma", "Sağlam bir sandalyenin önüne oturun. Nefes verirken ayağa kalkın, nefes alırken yavaşça oturun. Gerekirse ellerinizden destek alın; kolaylaştıkça kollarınızı göğsünüzde çaprazlayın.", "8–10 tekrar, 2 set")
_ex2("copd_heel", "heel2", "Tezgâha tutunarak topuk yükseltme", "Tezgâha hafifçe tutunun. Nefes verirken iki topuğunuzu birlikte kaldırıp parmak uçlarınızda yükselin, nefes alırken yavaşça inin.", "10–15 tekrar, 2 set")
_ex2("copd_row", "row", "Lastik bantla kürek çekme", "Lastik bandı göğüs hizasında sağlam bir yere bağlayın. Nefes verirken dirseklerinizi geriye çekip kürek kemiklerinizi birbirine yaklaştırın, nefes alırken yavaşça geri dönün. Omuzlarınızı kulaklarınıza doğru kaldırmayın.", "10 tekrar, 2 set")
_ex2("copd_walk", "walk", "Aralıklı yürüyüş", "Orta düzeyde nefes darlığı hissedeceğiniz bir tempoda yürüyün. Zorlandığınızda durup büzük dudak nefesiyle dinlenin, sonra devam edin. Toplam süreyi haftadan haftaya birkaç dakika artırın.", "Günde toplam 20–30 dakika, molalarla")

# ============================================================== KOAH
COPD_FAQ = [
 ("Nefes darlığım varken egzersiz yapmak zararlı mı?", "Hayır. Egzersizde nefes nefese kalmak akciğerlerinize zarar vermez; hareketsiz kalmak ise kasları zayıflatır ve aynı iş için daha çok nefes harcamanıza yol açar. Egzersizde orta düzeyde nefes darlığı hedeflenir. Nefes darlığınız her zamankinden belirgin şekilde fazlaysa ya da alevlenme belirtileriniz varsa o gün egzersizi erteleyip hekiminize danışın."),
 ("Rehabilitasyonla akciğerlerim düzelir mi?", "Rehabilitasyon akciğerdeki hasarı geri çevirmez. Güçlenen kaslar ve artan dayanıklılık sayesinde aynı akciğerle daha uzun yürüyebilir, günlük işleri daha az nefes darlığıyla yapabilirsiniz. Derlemede 6 dakikada yürünen mesafe ortalama 44 metre arttı."),
 ("Rehabilitasyonu evde yapabilir miyim?", "Evet. 166 hastalık bir çalışmada, bir fizyoterapist ev ziyareti ve ardından haftalık telefon görüşmeleriyle yürütülen 8 haftalık ev programı kısa vadede hastanedeki programla eşdeğer sonuç verdi. Programın size göre ayarlanması ve düzenli izlenmesi önemlidir."),
 ("Oksijen kullanıyorum, egzersiz yapabilir miyim?", "Çoğu zaman evet; ancak egzersiz sırasında oksijen akışının ne olacağına hekiminiz karar verir. Ayarı kendiniz değiştirmeyin; programınızı hekiminiz ve fizyoterapistinizle birlikte planlayın."),
]

COPD_SRC = [
 "McCarthy B, Casey D, Devane D, Murphy K, Murphy E, Lacasse Y. " + ext("https://www.cochrane.org/CD003793/AIRWAYS_pulmonary-rehabilitation-chronic-obstructive-pulmonary-disease", "Pulmonary rehabilitation for chronic obstructive pulmonary disease") + ". Cochrane Database Syst Rev. 2015;(2):CD003793.",
 "Puhan MA, Gimeno-Santos E, Cates CJ, Troosters T. " + ext("https://www.cochrane.org/CD005305/AIRWAYS_pulmonary-rehabilitation-following-exacerbations-chronic-obstructive-pulmonary-disease", "Pulmonary rehabilitation following exacerbations of chronic obstructive pulmonary disease") + ". Cochrane Database Syst Rev. 2016;(12):CD005305.",
 "Holland AE, Mahal A, Hill CJ, et al. " + ext("https://thorax.bmj.com/content/72/1/57", "Home-based rehabilitation for COPD using minimal resources: a randomised, controlled equivalence trial") + ". Thorax. 2017;72(1):57-65.",
 "Holland AE, Hill CJ, Jones AY, McDonald CF. " + ext("https://www.cochrane.org/CD008250/AIRWAYS_breathing-exercises-for-chronic-obstructive-pulmonary-disease", "Breathing exercises for chronic obstructive pulmonary disease") + ". Cochrane Database Syst Rev. 2012;(10):CD008250.",
 "World Health Organization. " + ext("https://www.who.int/news-room/fact-sheets/detail/chronic-obstructive-pulmonary-disease-(copd)", "Chronic obstructive pulmonary disease (COPD)") + ". Fact sheet. 10 June 2026.",
]

COPD_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Rehabilitasyon rehberi</p>
    <h1>KOAH'ta akciğer rehabilitasyonu</h1>
    <p class="lede">KOAH (kronik obstrüktif akciğer hastalığı), hava yollarının kalıcı olarak daraldığı ve en çok nefes darlığı, öksürük ve çabuk yorulmayla kendini gösteren bir akciğer hastalığıdır. Nefes darlığı insanı hareketten uzaklaştırır; hareketsizlik de kasları zayıflatıp nefes darlığını artırır. Akciğer rehabilitasyonu bu döngüyü kırmayı hedefler: 65 çalışmanın derlemesinde nefes darlığını ve yorgunluğu azalttı, yürüme mesafesini artırdı.</p>
    <p class="meta">Son güncelleme: 7 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>3. sıra</b><span>KOAH'ın dünyada ölüm nedenleri arasındaki yeri; 2023'te 3,4 milyon ölüm (DSÖ)</span></div>
        <div class="stat"><b>65 çalışma</b><span>Akciğer rehabilitasyonunu sınayan rastgele kontrollü çalışmalar; toplam 3.822 hasta</span></div>
        <div class="stat"><b>44 metre</b><span>Rehabilitasyonla 6 dakikada yürünen mesafedeki ortalama artış</span></div>
        <div class="stat"><b>8–12 hafta</b><span>Rehabilitasyon programlarının çoğunun süresi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">KOAH'ta hava yolları daralır ve akciğerlerdeki hava kesecikleri zarar görür; hava içeri girer ama dışarı tam çıkamaz. Yüksek gelirli ülkelerde vakaların %70'inden fazlası tütün kullanımına bağlıdır; ev içi ve dış ortam hava kirliliği de önemli nedenler arasındadır.</p>
        <p class="soft">Hastalık tamamen geçmez; ancak sigarayı bırakmak, hava kirliliğinden kaçınmak, aşıları yaptırmak, ilaçları düzenli kullanmak ve akciğer rehabilitasyonu şikâyetleri azaltabilir.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Özellikle eforla artan nefes darlığı</li>
          <li>Uzun süredir devam eden öksürük, bazen balgamla birlikte</li>
          <li>Çabuk yorulma</li>
          <li>Şikâyetlerin birkaç gün içinde belirgin şekilde arttığı alevlenme dönemleri</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Akciğer rehabilitasyonu ne sağlar?</h2>
      <p class="soft">Akciğer rehabilitasyonu (pulmoner rehabilitasyon), kişiye göre ayarlanan egzersiz eğitimiyle nefes tekniklerini ve hastalıkla yaşama eğitimini birleştiren bir programdır. 65 rastgele kontrollü çalışmayı (3.822 hasta) inceleyen Cochrane derlemesinde rehabilitasyon nefes darlığını ve yorgunluğu azalttı, duygu durumunu ve hastalığı kontrol edebilme duygusunu iyileştirdi; 6 dakikada yürünen mesafe ortalama 44 metre arttı. Program akciğerdeki hasarı geri çevirmez; kasları ve dayanıklılığı güçlendirerek aynı akciğerle daha fazlasını yapabilmenizi sağlar.</p>
      <p class="soft">Alevlenme geçirenlerde rehabilitasyonun etkisi 20 çalışmada (1.477 hasta) incelendi: yaşam kalitesi ve yürüme mesafesi (ortalama 62 metre) belirgin şekilde arttı, yeniden hastaneye yatış azaldı. Yeniden yatış sonuçları çalışmadan çalışmaya değiştiği için bu bulgunun kanıt düzeyi orta olarak değerlendirildi.</p>
      <p class="soft">Avustralya'da 166 hastayla yapılan bir çalışmada, bir fizyoterapist ev ziyareti ve ardından haftada bir telefon görüşmesinden oluşan 8 haftalık ev programı, kısa vadede hastanedeki programla eşdeğer sonuç verdi. Bir yıl sonraki sonuçlar ise ev programının eşdeğer olduğunu göstermeye yetmedi; kazanımı korumak için egzersizi sürdürmek gerekir.</p>
      <div class="callout">
        <p>Egzersizde nefes nefese kalmak zararlı değil, beklenen bir şeydir. Hedef, konuşabildiğiniz ama rahat olmadığınız orta düzeyde bir nefes darlığıdır. Programa başlamadan önce göğüs hastalıkları hekiminizin onayını alın; oksijen kullanıyorsanız egzersiz sırasındaki ayarı hekiminiz belirler.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <ul class="tx">
        <li><b>Sigarayı bırakmak</b><span>Hastalığın seyrini değiştiren en önemli adımdır; hangi evrede olursanız olun yararlıdır. Bırakmak için hekiminizden destek isteyin.</span></li>
        <li><b>İlaçlar</b><span>Hava yollarını genişleten soluk ilaçları tedavinin temelidir. Cihazı doğru kullanmak ilacın kendisi kadar önemlidir; tekniğinizi hekiminize ya da eczacınıza gösterin.</span></li>
        <li><b>Akciğer rehabilitasyonu</b><span>Egzersiz eğitimi, nefes teknikleri ve hastalıkla yaşama eğitiminden oluşur; nefes darlığını ve yorgunluğu azaltır, yürüme mesafesini artırır.</span></li>
        <li><b>Nefes teknikleri</b><span>Büzük dudak nefesi ve diyafram nefesi gibi teknikler, 16 çalışmanın derlemesinde yürüme mesafesini 35–50 metre artırdı; nefes darlığı ve yaşam kalitesi üzerindeki etkileri ise çalışmadan çalışmaya değişti.</span></li>
        <li><b>Aşılar</b><span>Göğüs enfeksiyonları alevlenmeye yol açabilir; size önerilen aşıları hekiminize sorun.</span></li>
        <li><b>Alevlenme planı</b><span>Nefes darlığınız, öksürüğünüz ya da balgamınız belirgin şekilde artarsa ne yapacağınızı önceden hekiminizle konuşun.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>KOAH için altı egzersiz</h2>
      <p class="soft">Zorlandığınız kısımda nefes verin, nefesinizi tutmayın. Nefes darlığınız artarsa durun, öne eğilerek ve büzük dudak nefesiyle toparlanın, sonra devam edin.</p>
      {ex_grid(["plb", "fwdlean", "copd_sts", "copd_heel", "copd_row", "copd_walk"])}
      <div class="callout">
        <p>Göğüs ağrısı, baş dönmesi, çarpıntı ya da dudaklarda morarma olursa egzersizi bırakın ve hekiminize başvurun.</p>
      </div>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>KOAH için videolar</h2>
      <p class="soft">Amerikan Akciğer Derneği'nin (American Lung Association) ve İskoçya sağlık hizmetinin (NHS inform) YouTube kanallarından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("7kpJ0QlRss4", "Büzük dudak nefesi videosunu oynat", "Pursed Lip Breathing")}
          <h3>Büzük dudak nefesi</h3>
          <p>Tekniğin nasıl yapıldığını gösteren kısa video.</p>
        </div>
        <div class="vid">
          {vbox("oSclbDihp2Y", "KOAH'la egzersiz videosunu oynat", "Exercising with COPD")}
          <h3>KOAH'la egzersiz yapmak</h3>
          <p>KOAH'ta egzersizin yerini anlatan bilgilendirme videosu.</p>
        </div>
      </div>
      <p class="meta">Videolar American Lung Association ve NHS inform kanallarına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(COPD_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Dinlenirken bile konuşmayı zorlaştıran nefes darlığı (acil)</li>
        <li>Dudaklarda ya da parmak uçlarında morarma (acil)</li>
        <li>Göğüs ağrısı ya da baskı hissi (acil)</li>
        <li>Bilinç bulanıklığı ya da aşırı uyku hâli (acil)</li>
        <li>Balgamın artması, renginin koyulaşması ya da ateş</li>
        <li>İlaçlara rağmen birkaç gündür artan nefes darlığı</li>
      </ul>
      {CTA_CARD("KOAH'a bağlı nefes darlığınız", "KOAH'ta akciğer rehabilitasyonu")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(COPD_SRC)}
    </div>
  </section>
</main>'''

page("koah.html", "KOAH'ta Akciğer Rehabilitasyonu",
     "KOAH'ta nefes darlığı varken egzersiz yapılır mı? Akciğer (pulmoner) rehabilitasyonun kanıtlanmış yararları, büzük dudak nefesi, evde altı egzersiz ve videolar.",
     "koah.html", NECK_CSS, COPD_BODY, YT_JS,
     seo_title="KOAH'ta Akciğer Rehabilitasyonu: Nefes ve Egzersiz | İhsan Eren",
     condition="KOAH (kronik obstrüktif akciğer hastalığı)", faq_items=COPD_FAQ)
