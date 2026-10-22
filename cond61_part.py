# -*- coding: utf-8 -*-
# Yeni rehber (61): Periferik arter hastalığı (bacak damar tıkanıklığı) ve aralıklı topallamada yürüyüş egzersizi. cond60_part.py'den sonra exec edilir. Video yok.
# Kaynaklar (22 Ekim 2026'da okundu): NICE CG147 öneriler, Lane 2017 Cochrane (PEDro özeti) + NIHR Evidence özeti, NHS PAD ve tedavi sayfaları (10 Nisan 2026),
# ACC/AHA 2024 kılavuzu (ACC "10 nokta" özeti), Mazzolai 2024 ESC uzlaşı belgesi (kabul edilmiş metin), McDermott 2021 LITE (JAMA özeti), Song 2019 (Edinburgh deposu),
# NHS Dumfries & Galloway Right Decisions (29 Nisan 2026), NCEPOD 2025 hasta broşürü.

_ex2("pd_walk", "walk", "Aralıklı yürüyüş", "Birkaç dakika yavaş tempoda ısının. Sonra bacağınızdaki ağrı orta ile şiddetli arası bir düzeye gelene kadar yürüyün, durun ve ağrı geçene kadar dinlenin, ardından yeniden yürüyün. Yürüme-dinlenme döngüsünü toplam süre dolana kadar tekrarlayın.", "20–30 dakikayla başlayın, hedef 30–60 dakika; haftada en az 3 gün")
_ex2("pd_march", "dm_march", "Oturarak yerinde yürüme", "Hava kötüyken ya da yürüyüşten önce ısınmak için: sağlam bir sandalyede dik oturun, dizlerinizi sırayla kaldırıp indirin, kollarınızı da sallayın.", "2–3 dakika")
_ex2("pd_heel", "heel2", "Tezgâha tutunarak topuk yükseltme", "Tezgâha hafifçe tutunun. İki topuğunuzu birlikte kaldırıp parmak uçlarınızda yükselin, yavaşça inin. Baldır kaslarını güçlendirir.", "10–15 tekrar, 2 set")
_ex2("pd_sts", "sts", "Sandalyeden kalkıp oturma", "Sağlam bir sandalyenin önüne oturun. Nefes verirken ayağa kalkın, nefes alırken yavaşça oturun. Gerekirse ellerinizden destek alın.", "10 tekrar, 2 set")
_ex2("pd_kext", "kext", "Oturarak diz açma", "Sandalyeye dik oturun. Dizinizi yavaşça düzeltip uyluğunuzun ön kasını sıkın, 3 saniye tutun ve indirin. Kolaylaştıkça ayak bileğinize hafif bir ağırlık ekleyebilirsiniz.", "Her bacakla 10 tekrar, 2 set")
_ex2("pd_stair", "sn_stair", "Merdiven çıkma", "Tırabzana tutunarak birkaç basamak çıkın ve yavaşça inin. Ağrı başlarsa durup dinlenin, geçince devam edin.", "1–3 kat, gün içinde birkaç kez")

PAD_FAQ = [
 ("Ağrıya rağmen yürümek zararlı mı?", "Hayır. Yürürken ortaya çıkan bu ağrı, çalışan kaslara yeterince kan gidememesinden kaynaklanır ve dinlenince geçer. İngiltere’nin NICE kılavuzu ağrının en yüksek düzeyine kadar yürümeyi, Avrupa Kardiyoloji Derneği’nin uzlaşı belgesi de orta ile şiddetli arası ağrıya kadar yürümeyi öneriyor; ağrısız yürüme de yürüyüşü bir ölçüde iyileştiriyor, ancak kanıtı daha zayıf. Dinlenirken de süren ağrı ya da bacakta ani değişiklik ise başka bir durumdur; aşağıdaki uyarı işaretlerine bakın."),
 ("Yürüyüş tıkanan damarı açar mı?", "Araştırmalarda egzersiz ayak bileği–kol basınç oranını (damar daralmasının ölçüsü) değiştirmedi. Kazanç, yürüyebildiğiniz mesafede ve günlük yaşamda görülüyor. Damar daralmasının ilerlemesini yavaşlatmak için sigarayı bırakmak ve hekiminizin önerdiği ilaçlar ayrıca önemlidir."),
 ("Gözetimli program mı, ev programı mı?", "NICE, aralıklı topallaması olan herkese gözetimli bir egzersiz programı öneriyor: 3 ay boyunca haftada yaklaşık 2 saat. Böyle bir program bulamıyorsanız yapılandırılmış ev programı iyi bir seçenek. Avrupa Kardiyoloji Derneği’nin belgesine göre adım sayar, yürüyüş günlüğü ya da düzenli telefon görüşmeleriyle izlenen ev programları gözetimli programlara yakın sonuç veriyor; izlenmeyen programlar daha az etkili. ABD kılavuzu da davranış değişikliği desteği içeren yapılandırılmış programları öneriyor; plansız, rastgele yürüyüşün yararı belirsiz."),
 ("Ne zaman fark ederim?", "Programlar genellikle en az 12 hafta sürer. Cochrane derlemesindeki çalışmalarda egzersiz programları çoğunlukla haftada en az 2 kez, 3 ile 12 ay arasında yapıldı ve kazanç 2 yıla kadar sürdü. Egzersizi bırakınca yarar azalır; bu yüzden program bittikten sonra da düzenli yürümeye devam etmek gerekir."),
 ("Yürüyemiyorsam ne yapabilirim?", "Avrupa ve ABD kılavuzlarına göre yürüyüş ilk tercih; yürümek mümkün değilse bisiklet, kol bisikleti (kol ergometresi) ya da güç egzersizleri de kullanılabilir. Yürüyüş, yürüme mesafesini genellikle güç egzersizlerinden daha fazla artırıyor; bisiklet ve kol bisikleti ise kalp-akciğer dayanıklılığını artırmada öne çıkıyor."),
 ("Sigara neden bu kadar önemli?", "Sigara, periferik arter hastalığının en önemli risk etkenidir. Bırakmak hastalığın kötüleşme riskini ve kalp krizi gibi diğer ciddi kalp-damar olaylarının riskini azaltır. Tanı konduktan sonra sigaraya devam edenlerde kalp krizi riski belirgin şekilde daha yüksektir."),
]

PAD_SRC = [
 "National Institute for Health and Care Excellence. " + ext("https://www.nice.org.uk/guidance/CG147/chapter/recommendations", "Peripheral arterial disease: diagnosis and management") + ". Clinical guideline CG147.",
 "Lane R, Harwood A, Watson L, Leng GC. " + ext("https://doi.org/10.1002/14651858.CD000990.pub4", "Exercise for intermittent claudication") + ". Cochrane Database Syst Rev. 2017;(12):CD000990.",
 "NIHR Evidence. " + ext("https://evidence.nihr.ac.uk/alert/exercise-improves-intermittent-claudication-leg-pain-on-walking", "Exercise improves intermittent claudication leg pain on walking") + ". 10 April 2018.",
 "Gornik HL, Aronow HD, Goodney PP, et al. " + ext("https://doi.org/10.1016/j.jacc.2024.02.013", "2024 ACC/AHA multisociety guideline for the management of lower extremity peripheral artery disease") + ". J Am Coll Cardiol. 2024. Özet: " + ext("https://www.acc.org/latest-in-cardiology/ten-points-to-remember/2024/05/09/15/00/2024-guideline-for-lower-extremity-pad", "ACC, Key Points") + ".",
 "Mazzolai L, Belch J, Venermo M, et al. " + ext("https://doi.org/10.1024/0301-1526/a001112", "Exercise therapy for chronic symptomatic peripheral artery disease: a clinical consensus document of the ESC Working Group on Aorta and Peripheral Vascular Diseases") + ". Vasa. 2024;53(2):87–108.",
 "McDermott MM, Spring B, Tian L, et al. " + ext("https://doi.org/10.1001/jama.2021.2536", "Effect of low-intensity vs high-intensity home-based walking exercise on walk distance in patients with peripheral artery disease: the LITE randomized clinical trial") + ". JAMA. 2021;325(13):1266–1276.",
 "Song P, Rudan D, Zhu Y, et al. " + ext("https://doi.org/10.1016/S2214-109X(19)30255-4", "Global, regional, and national prevalence and risk factors for peripheral artery disease in 2015: an updated systematic review and analysis") + ". Lancet Glob Health. 2019;7:e1020–e1030.",
 "NHS. " + ext("https://www.nhs.uk/conditions/peripheral-arterial-disease-pad", "Peripheral arterial disease (PAD)") + " ve " + ext("https://www.nhs.uk/conditions/peripheral-arterial-disease-pad/treatment", "Treatment") + ". Page last reviewed 10 April 2026.",
 "NHS Dumfries and Galloway, Right Decisions. " + ext("https://www.rightdecisions.scot.nhs.uk/dgrefhelp-nhs-dumfries-galloway/vascular/peripheral-arterial-disease/", "Peripheral arterial disease") + ". Reviewed 29 April 2026.",
 "National Confidential Enquiry into Patient Outcome and Death (NCEPOD). " + ext("https://www.ncepod.org.uk/2025ali/Risking%20Life%20and%20Limb_Patient_Leaflet.pdf", "Risking life and limb: patient leaflet on acute limb ischaemia") + ". 2025.",
]

PAD_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Rehabilitasyon rehberi</p>
    <h1>Periferik arter hastalığı: yürürken bacak ağrısı ve egzersiz</h1>
    <p class="lede">Yürürken baldırınızda, uyluğunuzda ya da kalçanızda kramp gibi bir ağrı başlıyor ve birkaç dakika durunca geçiyor mu? Bacak atardamarlarındaki daralma, çalışan kaslara giden kanı azaltabilir. Bu duruma periferik arter hastalığı, yürürken gelen ağrıya da aralıklı topallama (klodikasyon) denir. Düzenli yürüyüş egzersizi ağrısız yürüyebildiğiniz mesafeyi belirgin şekilde uzatır ve kılavuzlarda tedavinin ilk adımları arasında yer alır.</p>
    <p class="meta">Son güncelleme: 22 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>+82 m</b><span>Egzersizle ağrısız yürüme mesafesinde ortalama artış (Cochrane, 9 çalışma, 391 kişi)</span></div>
        <div class="stat"><b>+120 m</b><span>En uzun yürüme mesafesinde ortalama artış (10 çalışma, 500 kişi)</span></div>
        <div class="stat"><b>Haftada en az 3</b><span>30–60 dakikalık yürüyüş seansı, en az 12 hafta (Avrupa Kardiyoloji Derneği uzlaşı belgesi)</span></div>
        <div class="stat"><b>236 milyon</b><span>2015’te dünyada periferik arter hastalığıyla yaşadığı tahmin edilen 25 yaş üstü kişi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Yürürken baldır, uyluk ya da kalçada başlayan ve birkaç dakika dinlenince geçen ağrı, kramp ya da yorgunluk.</li>
          <li>Bacaklarda uyuşma ya da güçsüzlük.</li>
          <li>Bacak ve ayaklarda tüy dökülmesi, parlak ve soluk ya da morumsu deri.</li>
          <li>Kırılgan, yavaş uzayan ayak tırnakları; ayak ve bacakta iyileşmeyen yaralar.</li>
          <li>Erkeklerde sertleşme sorunu.</li>
        </ul>
        <p class="soft">Hastalığı olan pek çok kişide hiçbir belirti yoktur. Egzersiz sırasında tekrarlayan bacak ağrısı, başka açıdan sağlıklı biri için yaşlanmanın olağan bir parçası değildir; hekiminize başvurabilirsiniz.</p>
      </div>
      <div>
        <h2>Kimlerde daha sık?</h2>
        <ul class="dots">
          <li>Sigara içenlerde: en önemli risk etkenidir.</li>
          <li>Diyabeti (şeker hastalığı) olanlarda.</li>
          <li>Yüksek tansiyonu ya da yüksek kolesterolü olanlarda.</li>
          <li>Yaş ilerledikçe: 2015 verilerine göre görülme sıklığı 40’lı yaşların başında %3,5–4,3 iken 80’li yaşların başında %12–21’e çıkıyor.</li>
        </ul>
        <p class="soft">Daralmanın nedeni çoğunlukla damar duvarında yağlı birikintilerin (ateroskleroz) oluşmasıdır. Aynı süreç başka damarları da etkileyebildiği için periferik arter hastalığı olanlarda koroner kalp hastalığı, kalp krizi ve inme gibi diğer kalp-damar hastalıklarının görülme olasılığı da artar.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tanı nasıl konur?</h2>
      <p class="soft">Hekiminiz önce belirtilerinizi sorar ve bacaklarınızı, ayak nabızlarınızı muayene eder. En sık kullanılan test, ayak bileğindeki ve koldaki tansiyonun karşılaştırıldığı ayak bileği–kol basınç oranıdır (ABPI ya da ABİ). Bir İskoç sağlık kurumunun yönlendirme rehberine göre 0,9–1,4 arası normal kabul edilir; 0,9’un altı damar daralmasını, 0,5’in altı ise ileri daralmayı düşündürür. Diyabeti ya da ileri böbrek hastalığı olanlarda ve çok yaşlılarda damar duvarı sertleştiği için değer yanıltıcı biçimde yüksek çıkabilir.</p>
      <div class="callout">
        <p>Yürürken bacak ağrısının tek nedeni damar değildir. <a href="dar-kanal.html">Bel kanal darlığında</a> da yürürken bacak ağrısı olur; ancak bu ağrı çoğunlukla oturunca ya da öne eğilince geçer, ayakta durmak bile şikâyeti başlatabilir. Gece uykudan uyandıran kısa kramplar için <a href="gece-bacak-kramplari.html">gece bacak krampları</a> rehberine bakabilirsiniz.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Araştırmalar ne gösteriyor?</h2>
      <p class="soft">2017 tarihli Cochrane derlemesi 32 rastgele kontrollü çalışmayı ve 1.835 kişiyi inceledi. Olağan bakımla karşılaştırıldığında egzersiz, ağrısız yürüme mesafesini ortalama 82 metre, en uzun yürüme mesafesini ortalama 120 metre artırdı; bu sonuçlar yüksek kaliteli kanıta dayanıyor ve kazanç 2 yıla kadar sürdü. Egzersiz ayak bileği–kol basınç oranını değiştirmedi; ölüm ve ampütasyon üzerine bir etki gösterilemedi, yaşam kalitesi ise iyileşebilir.</p>
      <p class="soft">Yürüyüşün şiddeti de önemli görünüyor. ABD’de 305 kişiyle yapılan LITE çalışmasında katılımcılar 12 ay boyunca evde, haftada 5 kez, seans başına 50 dakikaya kadar yürüdü. Bacakta orta-şiddetli ağrı oluşturan tempoda yürüyenlerin 6 dakikalık yürüme mesafesi 34,5 metre arttı; ağrı oluşturmayan rahat tempoda yürüyenlerde ise artış olmadı ve sonuçları egzersiz yapmayan gruptan farklı değildi.</p>
      <p class="soft">Avrupa Kardiyoloji Derneği’nin 2024 uzlaşı belgesi gözetimli yürüyüş egzersizini ilk basamak tedavi olarak görüyor: haftada en az 3 seans, seans başına en az 30 dakika, en az 3 ay. Belge, ağrı egzersize devamı zorlaştırabildiği için esnek ve kişiye göre bir yaklaşım öneriyor: hafif-orta şiddetle başlayıp tolere edildikçe artırmak.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Yürüyüş programı nasıl yapılır?</h2>
      <ul class="tx">
        <li><b>Önce değerlendirme</b><span>Başlamadan önce hekiminizle görüşün. Kalp hastalığınız varsa kardiyoloğunuz efor testi isteyebilir.</span></li>
        <li><b>Isınma</b><span>Birkaç dakika yavaş tempoda yürüyerek başlayın.</span></li>
        <li><b>Ağrıya kadar yürüyün</b><span>Bacağınızdaki ağrı orta ile şiddetli arası bir düzeye gelene kadar yürüyün.</span></li>
        <li><b>Durun ve dinlenin</b><span>Ağrı tamamen geçene kadar durun, sonra yeniden yürümeye başlayın.</span></li>
        <li><b>Döngüyü tekrarlayın</b><span>Yürüme ve dinlenme döngüsünü toplam süre dolana kadar sürdürün. İngiltere’nin ulusal sağlık hizmeti NHS en az 30 dakikayı, haftada birkaç kez öneriyor; Avrupa belgesi 20 dakika civarında başlayıp 60 dakikaya doğru ilerlemeyi anlatıyor.</span></li>
        <li><b>Kayıt tutun</b><span>Adım sayar, telefon uygulaması ya da basit bir yürüyüş günlüğü kullanın. İzlenen ev programları, izlenmeyenlerden daha etkili.</span></li>
        <li><b>Ömür boyu sürdürün</b><span>Program bittiğinde yürümeyi bırakmayın; düzenli egzersiz bırakılınca kazanılan yarar azalır.</span></li>
      </ul>
      <p class="soft" style="margin-top:14px">Adımlarınızı bir tempoya oturtmak için <a href="tempolu-yuruyus.html">tempolu yürüyüş metronomunu</a> kullanabilirsiniz.</p>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Yürüyüşe eşlik eden altı hareket</h2>
      <p class="soft">Programın temeli aralıklı yürüyüştür. Diğer hareketler bacak kaslarını güçlendirmek, ısınmak ya da yürüyüşe çıkamadığınız günler içindir; güç egzersizlerinin seçimi ve tekrar sayıları genel önerilerdir. Göğüs ağrısı, baş dönmesi ya da alışılmadık nefes darlığı olursa hemen durun.</p>
      {ex_grid(["pd_walk", "pd_march", "pd_heel", "pd_sts", "pd_kext", "pd_stair"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Diğer tedaviler</h2>
      <ul class="tx">
        <li><b>Sigarayı bırakmak</b><span>Hastalığın kötüleşme riskini ve kalp krizi gibi ciddi olayların riskini azaltır.</span></li>
        <li><b>İlaçlar</b><span>Hekiminiz kolesterol düşürücü (statin), pıhtı oluşumunu azaltan ilaçlar ve tansiyon ilaçları önerebilir. Diyabeti olanlarda şeker kontrolü de önemlidir.</span></li>
        <li><b>Damar açma işlemleri</b><span>NICE, balon anjiyoplastiyi ancak risk etkenleriyle ilgili öneriler uygulandığı, gözetimli egzersiz programı yeterli düzelme sağlamadığı ve görüntüleme işlemin uygun olduğunu gösterdiği durumlarda öneriyor. Bypass ameliyatı da bir seçenektir.</span></li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(PAD_FAQ)}
      <p class="soft" style="margin-top:18px">Kalp krizi ya da bypass sonrası egzersiz için <a href="kalp-rehabilitasyonu.html">kalp rehabilitasyonu</a>, şeker hastalığında ayak sinirlerinin etkilenmesi için <a href="diyabetik-noropati.html">diyabetik nöropati</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">“Acil” yazan durumlarda 112’yi arayın ya da en yakın acil servise gidin:</p>
      <ul class="dots redflags">
        <li>Bacağınızda ya da kolunuzda ani başlayan ağrı, soğukluk, solukluk, uyuşma ya da güçsüzlük: ani damar tıkanması olabilir (acil)</li>
        <li>Dinlenirken de süren, özellikle gece artan ve bacağınızı yataktan sarkıtınca hafifleyen ayak ya da parmak ağrısı (en kısa sürede hekime)</li>
        <li>Diz altında 2 haftadan uzun süredir iyileşmeyen yara ya da ayak parmağında kararma</li>
        <li>Yürürken göğüs ağrısı, baskı hissi ya da alışılmadık nefes darlığı: egzersizi bırakın ve hekiminize başvurun</li>
      </ul>
      {CTA_CARD("Periferik arter hastalığında egzersiz programınız", "periferik arter hastalığında yürüyüş egzersizi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(PAD_SRC)}
    </div>
  </section>
</main>'''

page("periferik-arter-hastaligi.html", "Periferik Arter Hastalığı: Yürürken Bacak Ağrısı ve Egzersiz",
     "Yürürken baldırda kramp gibi ağrı, birkaç dakika durunca geçiyor mu? Periferik arter hastalığı ve aralıklı topallama: belirtiler, tanı, ağrıya kadar yürüme programı ve uyarı işaretleri.",
     "periferik-arter-hastaligi.html", NECK_CSS, PAD_BODY, "",
     seo_title="Periferik Arter Hastalığı (Bacak Damar Tıkanıklığı): Yürüyüş Egzersizi | İhsan Eren",
     condition="Periferik arter hastalığı", faq_items=PAD_FAQ)
