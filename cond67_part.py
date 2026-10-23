# -*- coding: utf-8 -*-
# Yeni rehber (67): Diyabette egzersiz. cond66_part.py'den sonra exec edilir. Video yok.
# Kaynaklar (23 Ekim 2026'da okundu): Kanaley 2022 ACSM (Consultant360 özeti), ADA Standards of Care 2026 Bölüm 5 (S102, S104), Umpierre 2011 JAMA (MDedge),
# Colberg 2016 ADA (AJMC), Reynolds 2016 (HCPLive), IDF Atlas 2025 (IDF basın sayfası), UHCW 2025 broşürü, Know Diabetes, NHS 111 Wales, NHS Orthotic Managers Group 2025.

_ex2("dy_walk", "walk", "Tempolu yürüyüş", "Konuşabildiğiniz ama biraz nefes nefese kaldığınız bir tempoda yürüyün. Mümkünse yemeklerden sonra yürüyün; birkaç dakika yavaş başlayıp yavaşlayarak bitirin.", "Haftada en az 150 dakika; 10’ar dakikalık bölümler de sayılır")
_ex2("dy_sts", "sts", "Sandalyeden kalkıp oturma", "Sağlam bir sandalyenin önüne oturun. Nefes verirken ayağa kalkın, nefes alırken yavaşça oturun. Kolaylaşınca ellerinizi göğsünüzde çaprazlayın.", "10–15 tekrar, 2–3 set")
_ex2("dy_push", "sk_push", "Duvar şınavı", "Ellerinizi göğüs hizasında duvara koyun. Dirseklerinizi bükerek göğsünüzü duvara yaklaştırın ve itin. Kolaylaşınca tezgâha geçebilirsiniz.", "10–15 tekrar, 2–3 set")
_ex2("dy_row", "row", "Lastik bantla kürek çekme", "Bandı sağlam bir yere sabitleyin ya da ayaklarınızın altından geçirin. Dirseklerinizi gövdenize yakın tutarak bandı kendinize doğru çekin, kürek kemiklerinizi sıkın ve yavaşça bırakın.", "10–15 tekrar, 2–3 set")
_ex2("dy_heel", "heel2", "Topuk yükseltme", "Tezgâha hafifçe tutunun. İki topuğunuzu birlikte kaldırıp parmak uçlarınızda yükselin, yavaşça inin. Baldır kaslarını güçlendirir ve dolaşımı destekler.", "10–15 tekrar, 2 set")
_ex2("dy_sls", "sls", "Tek ayak üzerinde denge", "Tezgâha hafifçe tutunarak tek ayağınızın üzerinde durun; kolaylaştıkça tutunmayı azaltın. Ayaklarınızda uyuşma varsa mutlaka tutunarak yapın.", "10–30 saniye, her ayakla 3 kez")

DY_FAQ = [
 ("Egzersiz ilaçlarımın yerine geçer mi?", "Hayır. Egzersiz kan şekerini düşürmeye yardım eder ve tedavinin önemli bir parçasıdır, ama ilaçların yerini tutmaz. Düzenli egzersize başladıktan sonra bazı ilaçların dozunun azaltılması gerekebilir; bu kararı diyabet ekibiniz verir."),
 ("Günün hangi saatinde egzersiz yapmalıyım?", "Amerikan Spor Hekimliği Koleji’nin 2022 uzlaşı raporuna göre yemeklerden sonra harcanan enerji, egzersizin türü ve şiddeti ne olursa olsun kan şekerini düşürüyor. Tip 2 diyabetli 41 kişiyle yapılan bir çalışmada her ana öğünden sonra 10 dakika yürümek, aynı süreyi günde bir kez yürümekten daha etkiliydi. En önemlisi düzenli yapabileceğiniz saati seçmek."),
 ("Kuvvet egzersizi şart mı?", "Önerilir. Amerikan Diyabet Derneği haftada 2–3 gün, art arda olmayan günlerde direnç egzersizi öneriyor; 65 yaş üstündekilere haftada 2–3 kez esneklik ve denge çalışmalarını da ekliyor. Sandalyeden kalkma, duvar şınavı ve lastik bant egzersizleri evde başlamak için yeterli."),
 ("Ne kadar sürede fark ederim?", "Kan şekeri tek bir egzersiz seansından sonra bile düşebilir. Uzun dönem göstergesi olan HbA1c’deki düşüş ise araştırmalarda en az 12 hafta süren programlarda gösterildi. Gelişmeyi hekiminizin istediği aralıklarla yapılan HbA1c ölçümleriyle izleyebilirsiniz."),
 ("Egzersiz sırasında şekerim düşerse ne yapmalıyım?", "Hemen durun ve şekerinizi hızla yükseltecek bir şey alın: küçük bir bardak meyve suyu ya da şekerli içecek veya birkaç glikoz tableti. 10–15 dakika sonra yeniden ölçün; hâlâ 4 mmol/L’nin (yaklaşık 72 mg/dL) altındaysa tekrarlayın. Düzelince bisküvi, sandviç ya da bir sonraki öğün gibi daha uzun etkili bir şey yiyin. Şeker düşmesi sık oluyorsa diyabet ekibinize haber verin."),
 ("Ayaklarımda uyuşma var, egzersiz yapabilir miyim?", "Evet, ama önlem alarak. Amerikan Diyabet Derneği egzersize başlamadan önce sinir hasarı, denge sorunu ve geçmişte ayak yarası olup olmadığının değerlendirilmesini öneriyor. Ayaklarınızı her gün kontrol edin, iyi oturan ayakkabı ve temiz çorap giyin, çıplak ayakla yürümeyin. Ayağınızda yara varsa üzerine yük bindiren egzersizlere başlamadan hekiminize danışın."),
]

DY_SRC = [
 "Kanaley JA, Colberg SR, Corcoran MH, et al. " + ext("https://doi.org/10.1249/MSS.0000000000002800", "Exercise/physical activity in individuals with type 2 diabetes: a consensus statement from the American College of Sports Medicine") + ". Med Sci Sports Exerc. 2022;54(2):353–368.",
 "American Diabetes Association Professional Practice Committee. " + ext("https://education.weitzmaninstitute.org/sites/default/files/course/2025-12/Facilitating%20Positive%20Health%20Behaviors%20and%20Well-being%20to%20Improve%20Health%20Outcomes%20-%20Standards%20of%20Care%20in%20Diabetes-2026.pdf", "5. Facilitating positive health behaviors and well-being to improve health outcomes: Standards of Care in Diabetes—2026") + ". Diabetes Care. 2026;49(Suppl 1):S89–S131.",
 "Umpierre D, Ribeiro PAB, Kramer CK, et al. Physical activity advice only or structured exercise training and association with HbA1c levels in type 2 diabetes: a systematic review and meta-analysis. JAMA. 2011;305(17):1790–1799. Haber: " + ext("https://mdedge.com/content/structured-exercise-training-lowers-hba1c-067", "MDedge") + ".",
 "Colberg SR, Sigal RJ, Yardley JE, et al. " + ext("https://doi.org/10.2337/dc16-1728", "Physical activity/exercise and diabetes: a position statement of the American Diabetes Association") + ". Diabetes Care. 2016;39(11):2065–2079.",
 "Reynolds AN, Mann JI, Williams S, Venn BJ. " + ext("https://doi.org/10.1007/s00125-016-4085-2", "Advice to walk after meals is more effective for lowering postprandial glycaemia in type 2 diabetes mellitus than advice that does not specify timing: a randomised crossover study") + ". Diabetologia. 2016;59(12):2572–2578.",
 "International Diabetes Federation. " + ext("https://idf.org/news-and-resources/news/idf-diabetes-atlas-11th-edition/", "IDF Diabetes Atlas, 11th edition") + ". 7 April 2025.",
 "University Hospitals Coventry and Warwickshire NHS Trust. " + ext("https://www.uhcw.nhs.uk/download/clientfiles/files/Patient%20Information%20Leaflets/Clinical%20Support%20Services/Dietetics/Physical%20Activity%20and%20Insulin%20-%20Type%202%20Diabetes.pdf", "Physical activity and insulin: type 2 diabetes") + ". HIC/LFT/2055/16, updated April 2025.",
 "Know Diabetes (NHS West and North London). " + ext("https://www.knowdiabetes.org.uk/be-healthier/move-more/exercise-and-staying-safe/", "Exercise and staying safe") + ".",
 "NHS 111 Wales. " + ext("https://111.wales.nhs.uk/hypoglycaemia", "Hypoglycaemia (low blood sugar)") + ". Updated 6 June 2025.",
 "NHS Orthotic Managers Group; Royal Berkshire NHS Foundation Trust. " + ext("https://royalberkshire.nhs.uk/media/2lypw13q/foot-care-advice-for-people-with-diabetes_may25.pdf", "Foot care advice for people with diabetes") + ". May 2025.",
]

DY_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Rehabilitasyon rehberi</p>
    <h1>Diyabette egzersiz</h1>
    <p class="lede">Tip 2 diyabette düzenli egzersiz, kan şekerini düşürmenin ve ilaçlarla birlikte uzun dönem kontrolünü iyileştirmenin en etkili yollarından biridir. Kasların çalışırken kandaki şekeri kullanması, yemekten sonra yapılan kısa yürüyüşlerin bile işe yaramasını sağlar. Bu rehber ne kadar ve nasıl egzersiz yapacağınızı, şeker düşmesine karşı alınacak önlemleri ve evde yapabileceğiniz altı egzersizi anlatıyor.</p>
    <p class="meta">Son güncelleme: 23 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>−0,67</b><span>Yapılandırılmış egzersiz programlarıyla HbA1c’de ortalama düşüş, yüzde puan (47 çalışma)</span></div>
        <div class="stat"><b>−0,89</b><span>Haftada 150 dakikadan fazla egzersizle ortalama düşüş; daha azında −0,36</span></div>
        <div class="stat"><b>150 dk + 2–3 gün</b><span>Haftalık aerobik egzersiz ve direnç egzersizi önerisi (Amerikan Diyabet Derneği)</span></div>
        <div class="stat"><b>589 milyon</b><span>Dünyada diyabetle yaşayan 20–79 yaş arası yetişkin; %90’ından fazlası tip 2</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Ne kadar egzersiz?</h2>
        <p class="soft">Amerikan Diyabet Derneği’nin 2026 önerileri:</p>
        <ul class="dots">
          <li>Haftada en az 150 dakika orta ya da yüksek şiddette aerobik egzersiz; en az 3 güne yayılmış ve art arda 2 günden fazla ara vermeden. Kondisyonu iyi olanlarda haftada en az 75 dakika yüksek şiddetli ya da aralıklı egzersiz de yeterli olabilir.</li>
          <li>Haftada 2–3 gün, art arda olmayan günlerde direnç (kuvvet) egzersizi.</li>
          <li>65 yaş üstünde haftada 2–3 kez esneklik ve denge çalışması.</li>
          <li>Uzun süre oturmayı en az 30 dakikada bir kısa hareket aralarıyla bölmek.</li>
        </ul>
      </div>
      <div>
        <h2>Neden işe yarıyor?</h2>
        <p class="soft">Amerikan Spor Hekimliği Koleji’nin 2022 uzlaşı raporuna göre düzenli aerobik egzersiz, gün içinde kan şekerinin yüksek kaldığı süreyi ve genel yüksekliğini azaltıyor. Yemeklerden sonra harcanan enerji, egzersizin türü ve şiddeti ne olursa olsun kan şekerini düşürüyor. Rapor, diyabeti olan herkesin düzenli hareket etmesini, oturarak geçen süreyi azaltmasını ve uzun oturmaları sık hareket aralarıyla bölmesini öneriyor.</p>
        <p class="soft">Yemekten sonra yürümek için <a href="yemek-sonrasi-yuruyus.html">yemek sonrası yürüyüş zamanlayıcısını</a> kullanabilirsiniz.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Araştırmalar ne gösteriyor?</h2>
      <p class="soft">47 rastgele kontrollü çalışmayı birleştiren bir meta-analizde, en az 12 hafta süren yapılandırılmış egzersiz programları HbA1c’yi ortalama 0,67 puan düşürdü: aerobik egzersiz 0,73, direnç egzersizi 0,57, ikisinin birlikte yapıldığı programlar 0,51 puan. Haftada 150 dakikadan fazla egzersiz yapılan programlarda düşüş 0,89, daha az egzersizde 0,36 puandı. Yalnızca “daha çok hareket edin” önerisi, beslenme önerisiyle birlikte verilmediğinde HbA1c’yi tek başına düşürmedi. Araştırmacılar çalışmaların genel kalitesini düşük buldu.</p>
      <div class="callout">
        <p>Egzersiz ilaçların yerine geçmez. Düzenli egzersize başladığınızda bazı ilaçların, özellikle insülinin ya da gliklazid gibi tabletlerin dozunun azaltılması gerekebilir; bu kararı diyabet ekibinizle birlikte verin.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Güvenle egzersiz yapmak için</h2>
      <ul class="tx">
        <li><b>Başlamadan önce</b><span>Amerikan Diyabet Derneği, egzersize başlamadan önce kalp-damar risk etkenlerinizin gözden geçirilmesini öneriyor. Riski yüksek olanların kısa ve hafif egzersizle başlaması öneriliyor. Tedavi edilmemiş ileri göz hasarı (proliferatif retinopati), bazı egzersiz türlerini sakıncalı kılabilir.</span></li>
        <li><b>Şeker düşmesi</b><span>İnsülin ya da gliklazid gibi bazı tabletler egzersizle birlikte şekerinizi düşürebilir. Şekerinizi ölçüyorsanız egzersizden önce, sırasında ve sonra bakın; yanınızda her zaman hızlı etkili bir şeker bulundurun.</span></li>
        <li><b>Belirtileri tanıyın</b><span>Terleme, titreme, baş dönmesi, açlık, çarpıntı, dudaklarda karıncalanma ve bulanık görme düşük şekerin belirtileri olabilir. Bu durumda egzersizi bırakıp şeker alın.</span></li>
        <li><b>Ayaklarınızı koruyun</b><span>Ayaklarınızı her gün kesik, morluk, şişlik, yara ve nasır açısından kontrol edin; iyi oturan ayakkabı ve temiz çorap giyin, çıplak ayakla yürümeyin.</span></li>
        <li><b>Tek başınıza değilseniz</b><span>İnsülin kullanıyor ve yalnız egzersiz yapıyorsanız, birine nereye gittiğinizi ve ne zaman döneceğinizi söyleyin.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Diyabette altı egzersiz</h2>
      <p class="soft">Bu hareketler, yürüyüşü kuvvet ve denge çalışmalarıyla birleştiren bir ev programına örnektir. Tekrar sayıları genel önerilerdir; size uygun yoğunluğu hekiminiz ya da fizyoterapistiniz belirleyebilir. Hareketler sırasında nefesinizi tutmayın.</p>
      {ex_grid(["dy_walk", "dy_sts", "dy_push", "dy_row", "dy_heel", "dy_sls"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(DY_FAQ)}
      <p class="soft" style="margin-top:18px">Ayaklarda uyuşma ve yanma için <a href="diyabetik-noropati.html">diyabetik nöropati</a> rehberine, haftalık kuvvet çalışması için <a href="guc-devresi.html">evde güç devresine</a> bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">“Acil” yazan durumlarda 112’yi arayın:</p>
      <ul class="dots redflags">
        <li>Şeker düşmesiyle birlikte bilinç bulanıklığı, nöbet ya da bilinç kaybı (acil)</li>
        <li>Egzersiz sırasında göğüs ağrısı, aşırı nefes darlığı ya da bayılacak gibi olma (acil)</li>
        <li>Şeker alıp yeniden ölçtüğünüz hâlde düzelmeyen ya da sık tekrarlayan düşük şeker</li>
        <li>Ayakta yeni bir yara, kızarıklık, şişlik ya da ayak şeklinde değişiklik</li>
      </ul>
      {CTA_CARD("Diyabette size uygun bir egzersiz programı", "diyabette egzersiz programı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(DY_SRC)}
    </div>
  </section>
</main>'''

page("diyabette-egzersiz.html", "Diyabette Egzersiz",
     "Tip 2 diyabette egzersiz: ne kadar ve nasıl, araştırmaların gösterdikleri, şeker düşmesine karşı önlemler, ayak bakımı ve evde altı egzersiz.",
     "diyabette-egzersiz.html", NECK_CSS, DY_BODY, "",
     seo_title="Diyabette Egzersiz: Kan Şekeri, Güvenli Hareket ve Ev Egzersizleri | İhsan Eren",
     condition="Tip 2 diyabet", faq_items=DY_FAQ)
