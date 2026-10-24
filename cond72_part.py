# -*- coding: utf-8 -*-
# Yeni rehber (72): Zayıflama ilacı kullanırken kasları korumak. cond71_part.py'den sonra exec edilir. Video yok.
# Kaynaklar (24 Ekim 2026'da okundu): DSÖ GLP-1 kılavuzu haberi (1 Ara 2025), Mozaffarian 2025 AJCN ortak tavsiye (Patient Care özeti), Wilding STEP 1 DXA alt çalışması (Newswise özet PDF),
# Wilding 2022 DOM STEP 1 uzantısı (Leicester deposu), Lundgren 2021 NEJM (McMaster Optimal Aging özeti), D'Souza 2022 BJSM yorumu, Villareal 2017 NEJM (AAFP + MedicalXpress),
# Alawadhi 2026 BMJ Open LEAN-PREP protokolü (tam metin), Bull 2020 DSÖ fiziksel aktivite kılavuzu (önceki turlarda okundu).

_ex2("gl_sts", "sts", "Sandalyeden kalkıp oturma", "Sağlam bir sandalyenin önüne oturun. Ellerinizi kullanmadan, nefes verirken ayağa kalkın ve yavaşça oturun. Kolaylaşınca elinize su şişesi gibi bir ağırlık alın ya da daha alçak bir sandalye kullanın.", "8–12 tekrar, 2–3 set")
_ex2("gl_push", "sk_push", "Duvar şınavı", "Ellerinizi göğüs hizasında duvara koyun. Dirseklerinizi bükerek göğsünüzü duvara yaklaştırın ve iterek geri dönün. Kolaylaşınca tezgâha, sonra yere geçin.", "8–12 tekrar, 2–3 set")
_ex2("gl_row", "row", "Lastik bantla kürek çekme", "Bandı sağlam bir yere sabitleyin. Dirseklerinizi gövdenize yakın tutarak bandı kendinize doğru çekin, kürek kemiklerinizi sıkın ve yavaşça bırakın. Zorlandıkça daha sert bant kullanın.", "8–12 tekrar, 2–3 set")
_ex2("gl_bridge", "bridge", "Köprü", "Sırtüstü uzanın, dizleriniz bükülü, ayaklarınız yerde. Kalçanızı sıkarak kaldırın, kısa bir süre tutun ve yavaşça indirin. Kolaylaşınca tek bacak üzerinde yapın.", "10–15 tekrar, 2–3 set")
_ex2("gl_heel", "heel2", "Topuk yükseltme", "Tezgâha hafifçe tutunun. İki topuğunuzu birlikte kaldırıp parmak uçlarınızda yükselin, yavaşça inin. Kolaylaşınca tek ayakla yapın.", "12–15 tekrar, 2–3 set")
_ex2("gl_walk", "walk", "Tempolu yürüyüş", "Konuşabildiğiniz ama biraz nefes nefese kaldığınız bir tempoda yürüyün. Güç egzersizlerini yapmadığınız günlerde de hareketli kalmanın kolay bir yoludur.", "Haftada en az 150 dakika; günlere yayın")

GL_FAQ = [
 ("Zayıflama ilacı kullanırken ne kadar kas kaybederim?", "Kişiden kişiye değişiyor. Semaglutidin büyük çalışmasındaki vücut kompozisyonu ölçümlerinde, yağ kütlesi %19,3, yağsız (kas dahil) doku kütlesi %9,7 azaldı. Yağ daha fazla azaldığı için vücuttaki yağsız doku oranı aslında arttı. Araştırmacılar bu ilaçlarla kaybedilen kilonun yaklaşık %15–50'sinin yağsız dokudan geldiğini tahmin ediyor."),
 ("Kas kaybı her zaman kötü mü?", "Kilo verirken bir miktar yağsız doku kaybı beklenir. Ancak güç ve hareket kabiliyeti, özellikle ileri yaşta ve zaten kas kütlesi az olanlarda önemlidir. Yaşlı ve obez 160 kişiyle yapılan bir çalışmada, kilo vermeyi aerobik ve güç egzersizleriyle birlikte yapanların bedensel işlevi en çok iyileşti."),
 ("Ne kadar protein almalıyım?", "Amerikan beslenme ve obezite dernekleri, kas kaybını sınırlamak için güç egzersiziyle birlikte yeterli protein alınmasını öneriyor. İştah azaldığında her öğüne bir protein kaynağı (yumurta, yoğurt, peynir, baklagil, et, tavuk ya da balık) eklemek işe yarar. Devam eden bir araştırmada günde vücut ağırlığının kilogramı başına 1,6 gram protein hedefleniyor. Böbrek hastalığınız varsa protein miktarını hekiminizle belirleyin."),
 ("Egzersiz ilacın etkisini artırır mı?", "Bir çalışma bunu destekliyor. Düşük kalorili diyetle ortalama 13 kilo vermiş 195 kişi bir yıl izlendiğinde, kiloyu en iyi koruyanlar liraglutid ile egzersizi birlikte uygulayanlardı: plaseboya göre 9,5 kilo daha az kiloya sahiplerdi ve vücut yağ oranları en çok bu grupta azaldı. Yağsız dokuyu koruyan tek grup ise egzersiz grubuydu."),
 ("İlacı bırakınca ne olur?", "Kilonun bir kısmı geri gelebilir. Semaglutidi 68 hafta kullanıp bırakan 327 kişinin izlendiği çalışmada, bir yıl içinde verilen kilonun yaklaşık üçte ikisi geri alındı ve kalp-damar sağlığındaki iyileşmeler de büyük ölçüde başa döndü. Bu yüzden güç egzersizi ve beslenme alışkanlıklarını ilaç kullanırken kazanmak önemlidir."),
 ("Güç egzersizinin bu ilaçlarla birlikte yararı kanıtlandı mı?", "Henüz tam değil. 2026'da yayımlanan bir araştırma protokolünün yazarlarına göre semaglutid ya da tirzepatid kullanırken güç egzersizinin etkisini sınayan tamamlanmış bir çalışma yok; bu soruyu yanıtlamak için 232 kişilik bir çalışma sürüyor. Yine de güç egzersizinin diyetle kilo verirken kası koruduğu iyi biliniyor ve kılavuzlar bu ilaçlarla birlikte güç egzersizini öneriyor."),
]

GL_SRC = [
 "World Health Organization. " + ext("https://www.who.int/news/item/01-12-2025-who-issues-global-guideline-on-the-use-of-glp-1-medicines-in-treating-obesity", "WHO issues global guideline on the use of GLP-1 medicines in treating obesity") + ". 1 December 2025.",
 "Mozaffarian D, Agarwal M, Alexander L, et al. Nutritional priorities to support GLP-1 therapy for obesity: a joint Advisory from the American College of Lifestyle Medicine, the American Society for Nutrition, the Obesity Medicine Association, and The Obesity Society. Am J Clin Nutr. 2025;122:344–367. Özet: " + ext("https://patientcareonline.com/view/glp-1-therapy-for-obesity-requires-substantial-nutritional-framework-multidisciplinary-support-joint-advisory-warns", "Patient Care, 9 July 2025") + ".",
 "Wilding JPH, et al. STEP 1 çalışmasının vücut kompozisyonu (DXA) alt çalışması, bildiri özeti: " + ext("https://www.newswise.com/pdf_docs/16159288255831_Wilding%20Abstract.pdf", "Newswise") + ".",
 "Wilding JPH, Batterham RL, Davies M, et al. " + ext("https://figshare.le.ac.uk/articles/journal_contribution/Weight_regain_and_cardiometabolic_effects_after_withdrawal_of_semaglutide_The_STEP_1_trial_extension/20012732/1", "Weight regain and cardiometabolic effects after withdrawal of semaglutide: the STEP 1 trial extension") + ". Diabetes Obes Metab. 2022;24(8):1553–1564.",
 "Lundgren JR, Janus C, Jensen SBK, et al. Healthy weight loss maintenance with exercise, liraglutide, or both combined. N Engl J Med. 2021;384(18):1719–1730. Özet: " + ext("https://www.mcmasteroptimalaging.org/full-article/plus/healthy-weight-loss-maintenance-exercise-liraglutide-combined-98902", "McMaster Optimal Aging Portal") + ".",
 "D'Souza AC, Lau KJ, Phillips SM. " + ext("https://bjsm.bmj.com/content/56/13/771", "Exercise in the maintenance of weight loss: health benefits beyond lost weight on the scale") + ". Br J Sports Med. 2022;56(13):771.",
 "Villareal DT, Aguirre L, Gurney AB, et al. Aerobic or resistance exercise, or both, in dieting obese older adults. N Engl J Med. 2017;376(20):1943–1955. Özet: " + ext("https://aafp.org/pubs/afp/issues/2017/0901/p331.html", "American Family Physician") + ".",
 "Alawadhi AA, Alroudhan D, Alsaeed DJ, et al. " + ext("https://eprints.gla.ac.uk/384367/2/384367.pdf", "LEAN mass Preservation with Resistance Exercise and Protein during semaglutide and tirzepatide therapy (LEAN-PREP study): a protocol for a randomised controlled trial") + ". BMJ Open. 2026;16:e116911.",
 "Bull FC, Al-Ansari SS, Biddle S, et al. " + ext("https://bjsm.bmj.com/content/54/24/1451", "World Health Organization 2020 guidelines on physical activity and sedentary behaviour") + ". Br J Sports Med. 2020;54(24):1451–1462.",
 "Patient Care. " + ext("https://www.patientcareonline.com/view/fda-approves-orforglipron-first-oral-glp-1-receptor-agonist-for-weight-loss-with-no-food-or-water-restrictions", "FDA approves orforglipron, first oral GLP-1 receptor agonist for weight loss with no food or water restrictions") + ". 1 April 2026 (ilaç sınıfının yan etki ve uyarıları: pankreatit, sıvı kaybına bağlı böbrek hasarı, insülin ya da sülfonilürelerle şeker düşmesi).",
]

GL_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Rehabilitasyon rehberi</p>
    <h1>Zayıflama ilacı kullanırken kaslarınızı koruyun</h1>
    <p class="lede">Semaglutid ve tirzepatid gibi GLP-1 ilaçları, obezite tedavisinde güçlü bir kilo kaybı sağlıyor. Ancak hızlı kilo kaybında yağın yanında kas da kaybedilebilir; bu da güç ve hareket kabiliyetini etkileyebilir. Bu rehber, ilaç kullanırken kaslarınızı korumak için güç egzersizinin, yeterli proteinin ve düzenli hareketin neden önemli olduğunu ve evde yapabileceğiniz altı egzersizi anlatıyor.</p>
    <p class="meta">Son güncelleme: 24 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>1 milyar+</b><span>Dünyada obeziteyle yaşayan kişi (Dünya Sağlık Örgütü)</span></div>
        <div class="stat"><b>%19 / %10</b><span>Semaglutid çalışmasında yağ kütlesindeki ve yağsız doku kütlesindeki ortalama azalma</span></div>
        <div class="stat"><b>%15–50</b><span>Bu ilaçlarla kaybedilen kilonun yağsız dokudan gelen tahmini payı</span></div>
        <div class="stat"><b>2/3</b><span>İlaç bırakıldıktan sonraki bir yılda geri alınan kilo payı (semaglutid çalışması)</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Kilo verirken kas neden azalır?</h2>
        <p class="soft">Vücut, az enerji aldığında yağın yanında kas dahil yağsız dokuyu da kullanır. Semaglutidin büyük çalışmasında vücut kompozisyonu ölçülen 140 kişide, ilaç alanlarda yağ kütlesi %19,3, yağsız doku kütlesi %9,7 azaldı. Yağ daha fazla azaldığı için vücuttaki yağsız doku oranı arttı; yani vücut kompozisyonu genel olarak düzeldi.</p>
        <p class="soft">Yine de kaybedilen yağsız dokunun bir kısmı kastır. Kas; güç, denge, şeker kullanımı ve yaşlılıkta bağımsızlık için önemlidir. Bu yüzden özellikle ileri yaşta, kas kütlesi zaten az olanlarda ve hareketsiz yaşayanlarda kası korumak daha da önem kazanır.</p>
      </div>
      <div>
        <h2>Kılavuzlar ne öneriyor?</h2>
        <ul class="dots">
          <li><b>Dünya Sağlık Örgütü (2025):</b> GLP-1 ilaçlarının yetişkinlerde uzun süreli obezite tedavisinde kullanılabileceğini, bunlarla birlikte sağlıklı beslenme ve fiziksel aktivite programları gibi yoğun davranışsal destek sunulabileceğini belirtiyor. İlacın tek başına yeterli olmadığını, uzun dönem verilerinin sınırlı olduğunu vurguluyor.</li>
          <li><b>Amerikan beslenme ve obezite dernekleri (2025):</b> Kilo kaybı sırasında kas ve kemik kaybını sınırlamak için güç egzersizi ve yeterli protein; demir, B vitaminleri, kalsiyum ve D vitamini eksikliklerinin izlenmesi; mide-bağırsak yan etkilerinin yönetilmesi öneriliyor.</li>
          <li><b>Genel öneri:</b> Dünya Sağlık Örgütü yetişkinlere haftada 150–300 dakika orta şiddette aerobik aktivite ve haftada en az 2 gün büyük kas gruplarını çalıştıran güç egzersizi öneriyor.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Egzersizin yararı</h2>
      <p class="soft">Danimarka'da düşük kalorili diyetle ortalama 13,1 kilo vermiş 195 kişi bir yıl boyunca egzersiz, liraglutid, ikisi birden ya da plasebo grubuna ayrıldı. Plaseboya göre egzersiz grubu 4,1, liraglutid grubu 6,8, ikisini birlikte uygulayanlar 9,5 kilo daha az kiloya sahipti. Vücut yağ oranı birlikte uygulayanlarda 3,9 puanla en çok azaldı; yağsız dokuyu koruyan tek grup ise egzersiz grubuydu.</p>
      <p class="soft">Obez ve kırılganlığı olan 65 yaş üstü 160 kişiyle yapılan 6 aylık bir çalışmada, kilo vermeyi aerobik ve güç egzersizlerinin ikisiyle birlikte yapanların bedensel işlevi en çok iyileşti.</p>
      <div class="callout">
        <p>Semaglutid ya da tirzepatid kullanırken güç egzersizinin kası ne kadar koruduğunu sınayan tamamlanmış bir çalışma henüz yok; bu konuda 232 kişilik bir randomize çalışma sürüyor. Bu çalışmada haftada 3 gün evde güç egzersizi ve günde kilogram başına 1,6 gram protein hedefleniyor.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Pratikte</h2>
      <ul class="tx">
        <li><b>Güç</b><span>Haftada en az 2–3 gün, büyük kas gruplarını çalıştıran egzersizler yapın. Bir seti son birkaç tekrar zorlayacak kadar yapın; kolaylaştıkça direnci artırın.</span></li>
        <li><b>Protein</b><span>İştahınız azaldığında öncelikle proteinli yiyecekleri tüketin; her öğüne bir protein kaynağı ekleyin.</span></li>
        <li><b>Hareket</b><span>Haftada en az 150 dakika tempolu yürüyüş ya da benzeri bir aktiviteyle günlük hareketi sürdürün.</span></li>
        <li><b>Sıvı ve yan etkiler</b><span>Bulantı, kabızlık ya da ishal varsa ekibinize bildirin; az az ve sık yemek yardımcı olabilir.</span></li>
        <li><b>Takip</b><span>Kilonun yanında gücünüzü de izleyin; örneğin <a href="sandalye-testi.html">30 saniye sandalye testini</a> birkaç haftada bir tekrarlayın.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Kasları korumak için altı egzersiz</h2>
      <p class="soft">İlk beş hareket bacak, kalça, göğüs, sırt ve baldır kaslarını çalıştıran güç egzersizleridir; altıncısı günlük hareketi destekler. Tekrar sayıları genel önerilerdir; yeni başlıyorsanız ya da bir sağlık sorununuz varsa programı hekiminiz ya da fizyoterapistinizle birlikte belirleyin.</p>
      {ex_grid(["gl_sts", "gl_push", "gl_row", "gl_bridge", "gl_heel", "gl_walk"])}
      <p class="soft" style="margin-top:14px">Haftalık bir güç programı için <a href="guc-devresi.html">evde güç devresine</a>, kas kaybı hakkında daha fazla bilgi için <a href="sarkopeni.html">sarkopeni</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(GL_FAQ)}
      <p class="soft" style="margin-top:18px">Kan şekeri için egzersiz önerileri <a href="diyabette-egzersiz.html">tip 2 diyabette egzersiz</a> rehberinde.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Şiddetli ve geçmeyen karın ağrısı, sırta yayılan ağrı ya da kusma: hemen</li>
        <li>Sıvı tutamayacak kadar kusma ya da ishal, baş dönmesi, idrarın belirgin azalması</li>
        <li>Belirgin güçsüzlük, merdiven çıkmakta ya da sandalyeden kalkmakta zorlanmaya başlama</li>
        <li>Diyabet ilacı da kullanıyorsanız titreme, terleme, çarpıntı gibi şeker düşmesi belirtileri</li>
      </ul>
      {CTA_CARD("Zayıflama ilacı kullanırken güç programı", "zayıflama ilacı kullanırken kas koruyucu egzersiz programı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(GL_SRC)}
    </div>
  </section>
</main>'''

page("zayiflama-ilaci-ve-kas.html", "Zayıflama İlacı Kullanırken Kaslarınızı Koruyun",
     "Semaglutid ve tirzepatid gibi zayıflama ilaçlarını kullanırken kas kaybını sınırlamak: araştırmalar, kılavuzlar, güç egzersizi, protein ve evde altı egzersiz.",
     "zayiflama-ilaci-ve-kas.html", NECK_CSS, GL_BODY, "",
     seo_title="Zayıflama İlacı (GLP-1) Kullanırken Kas Kaybını Önlemek: Egzersiz ve Protein | İhsan Eren",
     condition="Obezite", faq_items=GL_FAQ)
