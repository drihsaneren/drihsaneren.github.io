# -*- coding: utf-8 -*-
# Yeni rehber (64): Kalp yetmezliğinde egzersiz. cond63_part.py'den sonra exec edilir. Video yok.
# Kaynaklar (22 Ekim 2026'da okundu): Molloy 2023 Cochrane (Exeter deposu özeti), ESC 2021 (Hadjiphilippou & Lane 2022 BJC özeti), NICE NG106 halk bilgisi,
# NHS belirtiler + tedavi (26 Haziran 2026), BHF Heart Matters (27 Ocak 2026), UHB "Top tips" broşürü (Haziran 2025), Queensland HF egzersiz föyleri (2010), Liu 2024 GBD.

_ex2("hf_walk", "walk", "Yürüyüş", "Düz bir yolda, konuşabildiğiniz bir tempoda yürüyün. Birkaç dakika yavaş başlayın, sonunda da yavaşlayarak bitirin. Gün içinde kısa yürüyüşler de sayılır.", "5–10 dakikayla başlayın; hedef günde 30 dakika")
_ex2("hf_march", "dm_march", "Oturarak yerinde yürüme", "Ayakta durmak yorucuysa: sağlam bir sandalyede dik oturun, dizlerinizi sırayla kaldırıp indirin, kollarınızı da sallayın. Isınmak için de kullanabilirsiniz.", "2–5 dakika")
_ex2("hf_sts", "sts", "Sandalyeden kalkıp oturma", "Sağlam bir sandalyenin önüne oturun. Nefes verirken ayağa kalkın, nefes alırken yavaşça oturun. Gerekirse ellerinizden destek alın.", "8–10 tekrar, 1–2 set")
_ex2("hf_heel", "heel2", "Tezgâha tutunarak topuk yükseltme", "Tezgâha hafifçe tutunun. İki topuğunuzu birlikte kaldırıp parmak uçlarınızda yükselin, yavaşça inin. Nefesinizi tutmayın.", "10 tekrar, 1–2 set")
_ex2("hf_curl", "sk_curl", "Hafif ağırlıkla kol bükme", "Dik oturun. Elinize hafif bir ağırlık, dolu bir su şişesi ya da açılmamış bir konserve alın. Dirseğinizi bükerek ağırlığı omzunuza doğru kaldırın, yavaşça indirin. Kaldırırken nefes verin.", "Her kolla 8–10 tekrar")
_ex2("hf_kext", "kext", "Oturarak diz açma", "Sandalyeye dik oturun. Dizinizi yavaşça düzeltip uyluğunuzun ön kasını sıkın, 3 saniye tutun ve indirin.", "Her bacakla 8–10 tekrar")

HF_FAQ = [
 ("Egzersiz kalbimi yorar mı?", "Doğru şiddette yapılan egzersiz kalbi zorlamaz; kasların ve akciğerlerin daha verimli çalışmasını sağlayarak günlük işlerde kalbe binen yükü azaltır. İngiliz Kalp Vakfı, düzenli hareketin belirtileri ve yaşam kalitesini iyileştirebileceğini, hastaneye yatış riskini azaltabileceğini belirtiyor. Ancak egzersiz kalp yetmezliğini iyileştirmez ya da geri döndürmez; ilaçlarınızı sürdürmeniz gerekir."),
 ("Ne kadar ve hangi şiddette?", "İngiltere’de yetişkinlere haftada en az 150 dakika orta şiddette hareket öneriliyor; bu süre günde 5–10 dakikalık kısa bölümlere ayrılabilir. Orta şiddette biraz ısınır, daha sık nefes alırsınız ama konuşmayı sürdürebilirsiniz. Bir Avustralya kalp yetmezliği programı, 6–20 arası efor ölçeğinde 9–13’ü, yani “çok hafif” ile “biraz zor” arasını hedef gösteriyor; zor gelen bir etkinlikte dinlenin."),
 ("Merkezde mi, evde mi yapmalıyım?", "60 çalışmayı birleştiren 2023 tarihli Cochrane derlemesinde egzersize dayalı kalp rehabilitasyonu merkezde, evde (dijital destekli programlar dahil) ve karma programlarda yarar sağladı. Avrupa Kardiyoloji Derneği, hastalığı daha ağır olanlara, kırılganlığı ya da başka hastalıkları bulunanlara gözetim altında yapılan bir program öneriyor. Hangisine düzenli devam edebilecekseniz onu seçebilirsiniz; ev programı da hekim onayı ve izlem gerektirir."),
 ("Hangi egzersizlerden kaçınmalıyım?", "Ağır kaldırma, nefes tutarak yapılan zorlamalar ve tüm vücut ağırlığını taşıyan şınav ve plank gibi hareketler önerilmez. Yüzerken dikkatli olun; suda egzersiz, hissettirdiğinden daha yorucu olabilir. Belirtileriniz son zamanlarda kötüleştiyse suda egzersiz yapmayın."),
 ("Hangi günlerde egzersiz yapmamalıyım?", "Kendinizi hasta hissettiğiniz, her zamankinden daha yorgun ya da nefesi daha daralmış olduğunuz günlerde egzersiz yapmayın. Kısa sürede kilo aldıysanız ya da bilekleriniz daha çok şiştiyse önce ekibinize danışın. İyi günlerde de aşırıya kaçmayın; kendinizi en enerjik hissettiğiniz saati seçebilirsiniz."),
 ("Neden her gün tartılmalıyım?", "Kalp yetmezliğinde vücutta sıvı birikebilir ve bunun ilk işareti çoğu zaman ani kilo artışıdır. Her sabah aynı saatte, aynı tartıyla ve az giysiyle tartılıp sonucu not edin. 3–4 gün içinde yaklaşık 2 kilo artış olursa hekiminize ya da kalp yetmezliği hemşirenize haber verin."),
]

HF_SRC = [
 "Molloy CD, Long L, Mordi IR, et al. " + ext("https://doi.org/10.1002/ejhf.3046", "Exercise-based cardiac rehabilitation for adults with heart failure – 2023 Cochrane systematic review and meta-analysis") + ". Eur J Heart Fail. 2023.",
 "McDonagh TA, Metra M, Adamo M, et al. 2021 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure. Eur Heart J. 2021;42:3599–3726. Özet: Hadjiphilippou S, Lane R. " + ext("https://bjcardio.co.uk/?p=49552", "Guidance on lifestyle, rehabilitation and devices in heart failure patients") + ". Br J Cardiol. 2022;29(suppl 2):S13–S16.",
 "National Institute for Health and Care Excellence. " + ext("https://www.nice.org.uk/guidance/NG106/InformationForPublic", "Chronic heart failure: the care you should expect") + ". NICE guideline NG106.",
 "NHS. " + ext("https://www.nhs.uk/conditions/heart-failure/symptoms/", "Symptoms of heart failure") + " ve " + ext("https://www.nhs.uk/conditions/heart-failure/treatment", "Treatment") + ". Page last reviewed 26 June 2026.",
 "British Heart Foundation. " + ext("https://www.bhf.org.uk/informationsupport/heart-matters-magazine/activity/exercise-for-heart-failure", "Exercise for heart failure") + ". Heart Matters, updated 27 January 2026.",
 "University Hospitals Birmingham NHS Foundation Trust. " + ext("https://www.uhb.nhs.uk/media/eqhbajpm/heart-failure-cardiac-patients-top-ten-tips-cardiology-pi.pdf", "Top tips for heart failure patients") + ". PI25/3263/04, June 2025.",
 "Queensland Heart Failure Services. " + ext("https://www.health.qld.gov.au/heart_failure/pdf/hf_exercise_sheets.pdf", "Heart failure patient information: exercise sheets") + ". Revised May 2010.",
 "Liu Z, Li Z, Li X, et al. " + ext("https://doi.org/10.1002/ehf2.14915", "Global trends in heart failure from 1990 to 2019: an age-period-cohort analysis from the Global Burden of Disease study") + ". ESC Heart Fail. 2024;11(5):3264–3278.",
]

HF_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Rehabilitasyon rehberi</p>
    <h1>Kalp yetmezliğinde egzersiz</h1>
    <p class="lede">Nefes darlığı, çabuk yorulma ya da ayak bileklerinde şişlik nedeniyle hareket etmekten çekiniyor musunuz? Kalp yetmezliği, kalbin vücudun ihtiyacını karşılayacak kadar güçlü pompalayamaması demektir. Bugün kılavuzlar, durumu izin veren herkese egzersizi öneriyor. Hekim onayıyla ve kademeli yapılan egzersiz yaşam kalitesini artırır ve hastaneye yatışı azaltır.</p>
    <p class="meta">Son güncelleme: 23 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%31</b><span>Egzersize dayalı rehabilitasyonla ilk 12 ayda hastaneye yatış riskindeki azalma (60 çalışma, 8.728 kişi)</span></div>
        <div class="stat"><b>13’te 1</b><span>Rehabilitasyona katılan yaklaşık her 13 kişiden birinde bir hastane yatışı önlendi</span></div>
        <div class="stat"><b>150 dk</b><span>Haftalık orta şiddette hareket hedefi; 5–10 dakikalık bölümlere ayrılabilir</span></div>
        <div class="stat"><b>56 milyon</b><span>2019’da dünyada kalp yetmezliğiyle yaşadığı tahmin edilen kişi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Günlük işlerde ya da yatarken nefes darlığı; hareket ederken beklenenden fazla nefes nefese kalma.</li>
          <li>Halsizlik, yorgunluk, özellikle hareketten sonra sersemlik ya da baş dönmesi.</li>
          <li>Ayak, ayak bileği, bacak ya da karında şişlik; kendini şişkin hissetme.</li>
          <li>Ani kilo artışı.</li>
          <li>Geceleri öksürük.</li>
        </ul>
        <p class="soft">Kalp yetmezliğine en çok koroner kalp hastalığı ve yüksek tansiyon yol açar. Dünyada kalp yetmezliğiyle yaşayanların sayısı 1990–2019 arasında iki katından fazla arttı.</p>
      </div>
      <div>
        <h2>Kimler egzersiz yapabilir?</h2>
        <ul class="dots">
          <li>Avrupa Kardiyoloji Derneği, egzersiz yapabilecek durumdaki her kalp yetmezliği hastasına egzersizi öneriyor; amaç egzersiz kapasitesini ve yaşam kalitesini artırmak, hastaneye yatışı azaltmak.</li>
          <li>Hastalığı daha ağır olanlar, kırılgan olanlar ya da başka hastalıkları bulunanlar için gözetim altında yapılan bir rehabilitasyon programı öneriliyor.</li>
          <li>İngiltere’de tanı alan herkese kalp rehabilitasyonu öneriliyor; güvenle nasıl egzersiz yapacağınızı öğrenmek için değerlendirmeye yönlendirilmeniz gerekir.</li>
        </ul>
        <p class="soft">Başlamadan önce kardiyoloğunuzla görüşün. Ne zaman ve hangi şiddette başlayacağınıza kalbinizin durumuna ve ilaçlarınıza göre o karar verir.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Araştırmalar ne gösteriyor?</h2>
      <p class="soft">2023’te yayımlanan Cochrane derlemesi, kalp yetmezliği olan 8.728 kişiyle yapılmış 60 rastgele kontrollü çalışmayı inceledi. Egzersize dayalı kalp rehabilitasyonu ilk 12 ayda herhangi bir nedenle hastaneye yatış riskini %31 azalttı: yaklaşık her 13 kişiden birinde bir yatış önlendi. Yaşam kalitesi kısa vadede klinik açıdan anlamlı düzeyde iyileşti; uzun vadede de iyileşme sürdü. Ölüm riskinde belirgin bir fark gösterilemedi. Merkezde, evde (dijital destekli programlar dahil) ve ikisinin karması olan programların hepsinde yarar görüldü.</p>
      <div class="callout">
        <p>Egzersiz kalp yetmezliğini iyileştirmez ve ilaçların yerini tutmaz. İlaçlarınızı hekiminizin söylediği gibi kullanmayı sürdürün; egzersiz tedavinizin bir parçasıdır.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Güvenle egzersiz yapmak için</h2>
      <ul class="tx">
        <li><b>Isınma ve soğuma</b><span>Her seansa yavaş başlayıp nabzınızı kademeli yükseltin; sonunda da yavaşlayarak bitirin. Egzersizden hemen sonra uzanmayın.</span></li>
        <li><b>Konuşma testi</b><span>Orta şiddette biraz ısınır, daha sık nefes alırsınız ama tam bir cümle kurabilirsiniz. Konuşamıyorsanız fazla zorluyorsunuz.</span></li>
        <li><b>Az ve sık</b><span>Hedef haftada en az 150 dakika; günde 5–10 dakikalık bölümlerle başlayabilirsiniz. Biraz hareket hiç yoktan iyidir.</span></li>
        <li><b>Hafif güçlendirme</b><span>Hafif ağırlıklar, lastik bantlar ya da açılmamış konserve kutuları ve su şişeleri kullanın; yavaş hareket edin, nefesinizi tutmayın, kaldırırken nefes verin.</span></li>
        <li><b>Kötü günlerde dinlenin</b><span>Hasta hissettiğiniz ya da her zamankinden daha yorgun ve nefessiz olduğunuz günlerde egzersiz yapmayın; iyi günlerde de aşırıya kaçmayın.</span></li>
        <li><b>Hemen durun</b><span>Çarpıntı, aşırı nefes darlığı, göğüs ağrısı, sersemlik ya da enerjinizin tükendiğini hissettiğinizde egzersizi bırakın.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Kalp yetmezliğinde altı hafif egzersiz</h2>
      <p class="soft">Bu hareketler kardiyoloğunuz egzersize izin verdikten sonra evde yapılabilecek hafif örneklerdir; seçim ve tekrar sayıları genel önerilerdir, rehabilitasyon ekibinizin programı önceliklidir. Ayakta durmak yorucuysa oturarak yapılan hareketlerle başlayın.</p>
      {ex_grid(["hf_walk", "hf_march", "hf_sts", "hf_heel", "hf_curl", "hf_kext"])}
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Her gün tartılın</h2>
        <p class="soft">Her sabah aynı saatte, aynı tartıyla ve az giysiyle tartılıp sonucu not edin. 3–4 gün içinde yaklaşık 2 kilo artış, vücutta sıvı birikmesinin işareti olabilir; hekiminize ya da kalp yetmezliği hemşirenize haber verin.</p>
      </div>
      <div>
        <h2>Tuz ve sıvı</h2>
        <p class="soft">Yemeğe tuz eklemeyin, tuzu yüksek yiyecekleri sınırlayın ve tuz yerine geçen ürünleri hekiminize sormadan kullanmayın. Bir İngiltere hastanesinin broşürü, aksi söylenmedikçe günde yaklaşık 2 litre sıvıyı öneriyor; size uygun miktarı ekibiniz belirler. Sigarayı bırakın, alkolü azaltın, grip aşınızı yaptırın.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(HF_FAQ)}
      <p class="soft" style="margin-top:18px">Kalp krizi, stent ya da bypass sonrası egzersiz için <a href="kalp-rehabilitasyonu.html">kalp rehabilitasyonu</a>, nabzınızı ölçmek için <a href="nabiz-olcer.html">nabız ölçer</a> sayfasına bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">“Acil” yazan durumlarda 112’yi arayın; kendiniz araç kullanarak hastaneye gitmeyin:</p>
      <ul class="dots redflags">
        <li>Şiddetli nefes darlığı: soluk soluğa kalma, boğulur gibi olma, konuşamama (acil)</li>
        <li>Dudaklarda ya da deride solukluk, morarma ya da grileşme (acil)</li>
        <li>Bayılma ya da çevresine normal tepki vermeme (acil)</li>
        <li>Dinlenmekle geçmeyen göğüs ağrısı ya da baskı hissi (acil)</li>
        <li>Yatarken ya da günlük işlerde nefes darlığı, köpüklü pembe balgam, ani kilo artışı (aynı gün hekime)</li>
        <li>Yeni ya da artan bilek-bacak şişliği, gece nefes darlığıyla uyanma ya da rahat nefes almak için daha fazla yastık gerekmesi</li>
      </ul>
      {CTA_CARD("Kalp yetmezliğinde egzersiz programınız", "kalp yetmezliğinde egzersiz")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(HF_SRC)}
    </div>
  </section>
</main>'''

page("kalp-yetmezligi.html", "Kalp Yetmezliğinde Egzersiz",
     "Kalp yetmezliğinde egzersiz güvenli mi? Belirtiler, araştırmaların söyledikleri, konuşma testi, hafif ev egzersizleri, her gün tartılma ve ne zaman hemen başvurmalı.",
     "kalp-yetmezligi.html", NECK_CSS, HF_BODY, "",
     seo_title="Kalp Yetmezliğinde Egzersiz: Güvenli Hareket, Belirtiler ve Rehabilitasyon | İhsan Eren",
     condition="Kalp yetmezliği", faq_items=HF_FAQ)
