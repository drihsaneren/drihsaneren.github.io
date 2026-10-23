# -*- coding: utf-8 -*-
# Yeni rehber (69): Yüksek tansiyonda egzersiz. cond68_part.py'den sonra exec edilir. Video yok.
# Kaynaklar (23 Ekim 2026'da okundu): ESC 2024 (McEvoy; PCR ve ACC özetleri), DSÖ 2025 küresel hipertansiyon raporu (HIFA), Cornelissen & Smart 2013 (PEDro),
# Edwards 2023 BJSM (duvar oturuşu sayfasından), Hansford 2021 (UNE deposu), Naci 2019 BJSM, NICE NG136 ev ölçümü (GPnotebook özeti), NHS 111 Wales (4 Ara 2024),
# nidirect (26 Şub 2026), UHB PI25/3366/06 (Eki 2025), Blood Pressure UK.

_ex2("ht_walk", "walk", "Tempolu yürüyüş", "Konuşabildiğiniz ama biraz nefes nefese kaldığınız bir tempoda yürüyün. Birkaç dakika yavaş başlayıp sonunda yavaşlayarak bitirin.", "Haftada en az 150 dakika; örneğin 5 gün 30 dakika")
_ex2("ht_wall", "wallsit", "Duvar oturuşu", "Sırtınızı duvara dayayıp dizleriniz bükülü, sanki görünmez bir sandalyeye oturur gibi durun. Zorlayıcı ama dayanılabilir bir yükseklik seçin; nefesinizi tutmayın.", "2 dakika, arada 2 dakika dinlenerek 4 kez; haftada 3 gün")
_ex2("ht_sts", "sts", "Sandalyeden kalkıp oturma", "Sağlam bir sandalyenin önüne oturun. Nefes verirken ayağa kalkın, nefes alırken yavaşça oturun.", "10–15 tekrar, 2–3 set")
_ex2("ht_push", "sk_push", "Duvar şınavı", "Ellerinizi göğüs hizasında duvara koyun. Dirseklerinizi bükerek göğsünüzü duvara yaklaştırın ve iterek geri dönün. Nefesinizi tutmayın.", "10–15 tekrar, 2–3 set")
_ex2("ht_row", "row", "Lastik bantla kürek çekme", "Bandı sağlam bir yere sabitleyin. Dirseklerinizi gövdenize yakın tutarak bandı kendinize doğru çekin, kürek kemiklerinizi sıkın ve yavaşça bırakın.", "10–15 tekrar, 2–3 set")
_ex2("ht_bridge", "bridge", "Köprü", "Sırtüstü uzanın, dizleriniz bükülü, ayaklarınız yerde. Kalçanızı sıkarak yavaşça kaldırın, kısa bir süre tutun ve indirin; nefes almayı sürdürün.", "10–15 tekrar, 2 set")

HT_FAQ = [
 ("Egzersiz yapınca ilacımı bırakabilir miyim?", "Kendi kendinize bırakmayın. Egzersiz tansiyonu düşürür ve bazı kişilerde ilaç ihtiyacını azaltabilir, ama ilaç kararını tansiyon ölçümlerinize ve genel riskinize bakarak hekiminiz verir. Bir İngiltere hastanesinin broşürü de tek tek ölçümlere bakarak ilaç değiştirmemeyi, önce hekime danışmayı öneriyor."),
 ("Hangi egzersiz en etkili?", "Hepsi işe yarıyor. 93 çalışmayı birleştiren bir meta-analizde dayanıklılık egzersizi tansiyonu ortalama 3,5/2,5 mmHg, tansiyonu yüksek olanlarda 8,3/5,2 mmHg düşürdü; en büyük düşüş izometrik egzersizlerdeydi (10,9/6,2 mmHg), ama bu sonuç az sayıda çalışmaya dayanıyordu. Daha yeni ve büyük bir analizde de duvar oturuşu gibi izometrik egzersizler öne çıktı. En iyi egzersiz, düzenli yapabileceğiniz egzersizdir."),
 ("Ağırlık kaldırmak tansiyonumu yükseltir mi?", "Düzenli direnç egzersizi dinlenme tansiyonunu yükseltmez, tersine düşürür; Avrupa Kardiyoloji Derneği haftada 2–3 gün direnç egzersizini öneriyor. Egzersiz sırasında nefesinizi tutmayın ve çok ağır yüklerden kaçının. Tansiyonunuz kontrol altında değilse önce hekiminize danışın."),
 ("Evde ölçtüğüm değer neden muayenedekinden farklı?", "Bazı kişilerde tansiyon yalnızca muayenehanede yüksek çıkar (“beyaz önlük” etkisi), bazılarında ise muayenede normal görünürken gün içinde yüksektir. Bu yüzden Avrupa Kardiyoloji Derneği tanı için muayene dışı ölçümleri, yani ev ölçümünü ya da 24 saatlik ölçümü öneriyor. Evde ortalama 135/85’in altı (80 yaş ve üzerinde 145/85’in altı) normal kabul ediliyor."),
 ("Evde nasıl ve ne zaman ölçmeliyim?", "İngiltere’nin kılavuzu (NICE) tanı için 4–7 gün boyunca sabah ve akşam, 1 dakika arayla ikişer ölçüm yapılmasını, ilk günün ölçümlerinin atılıp kalanların ortalamasının alınmasını öneriyor. Ölçmeden önce 5 dakika dinlenin, sırtınız destekli ve bacaklarınız çapraz olmadan oturun, kolunuzu kalp hizasında bir masaya koyun ve ölçüm sırasında konuşmayın."),
 ("Ne kadar tuz yemeliyim?", "Avrupa Kardiyoloji Derneği günde 2 gramdan az sodyum, yani yaklaşık 5 gram tuz (bir çay kaşığı) öneriyor. Ayrıca böbrek hastalığı olmayanlarda meyve ve sebzeyle potasyum alımının artırılmasını, alkolden kaçınılmasını ve sağlıklı kilonun korunmasını öneriyor."),
]

HT_SRC = [
 "McEvoy JW, McCarthy CP, Bruno RM, et al. 2024 ESC Guidelines for the management of elevated blood pressure and hypertension. Eur Heart J. 2024;45(38):3912–4018. Özet: " + ext("https://pcronline.com/Cases-resources-images/Tools-and-Practice/The-Essentials/Hypertension/A-review-of-the-2024-ESC-Guidelines-on-elevated-blood-pressure-and-hypertension", "PCR") + " ve " + ext("https://www.acc.org/Latest-in-Cardiology/ten-points-to-remember/2024/09/05/14/11/2024-esc-guidelines-for-bp-esc-2024", "American College of Cardiology") + ".",
 "World Health Organization. Global report on hypertension 2025. Özet: " + ext("https://hifa.org/node/96856099", "HIFA, 28 September 2025") + ".",
 "Cornelissen VA, Smart NA. " + ext("https://search.pedro.org.au/search-results/record-detail/35306", "Exercise training for blood pressure: a systematic review and meta-analysis") + ". J Am Heart Assoc. 2013;2(1):e004473.",
 "Edwards JJ, Deenmamode AHP, Griffiths M, et al. " + ext("https://bjsm.bmj.com/content/57/20/1317", "Exercise training and resting blood pressure: a large-scale pairwise and network meta-analysis of randomised controlled trials") + ". Br J Sports Med. 2023;57(20):1317–1326.",
 "Hansford HJ, Parmenter BJ, McLeod KA, et al. " + ext("https://rune.une.edu.au/web/handle/1959.11/31894", "The effectiveness and safety of isometric resistance training for adults with high blood pressure: a systematic review and meta-analysis") + ". Hypertens Res. 2021;44(11):1373–1384.",
 "Naci H, Salcher-Konrad M, Dias S, et al. " + ext("https://bjsm.bmj.com/content/53/14/859.abstract", "How does exercise treatment compare with antihypertensive medications? A network meta-analysis of 391 randomised controlled trials assessing exercise and medication effects on systolic blood pressure") + ". Br J Sports Med. 2019;53(14):859–869.",
 "National Institute for Health and Care Excellence. Hypertension in adults: diagnosis and management. NICE guideline NG136. Ev ölçümü özeti: " + ext("https://gpnotebook.com/pages/cardiovascular-medicine/home-self-blood-pressure-monitoring", "GPnotebook") + ".",
 "NHS 111 Wales. " + ext("https://111.wales.nhs.uk/Bloodpressure(high)", "Blood pressure (high)") + ". Last updated 4 December 2024.",
 "nidirect (Northern Ireland). " + ext("https://www.nidirect.gov.uk/articles/high-blood-pressure-hypertension", "High blood pressure (hypertension)") + ". Last updated 26 February 2026.",
 "University Hospitals Birmingham NHS Foundation Trust. " + ext("https://www.uhb.nhs.uk/media/cdkdecer/pi-renal-blood-pressure-self-monitoring.pdf", "Self-blood pressure monitoring: key points") + ". PI25/3366/06, October 2025.",
 "Blood Pressure UK. " + ext("https://www.bloodpressureuk.org/BloodPressureandyou/Homemonitoring/Howtomeasure", "How to measure your blood pressure at home") + ".",
]

HT_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Rehabilitasyon rehberi</p>
    <h1>Yüksek tansiyonda egzersiz</h1>
    <p class="lede">Yüksek tansiyon çoğu zaman hiçbir belirti vermez; bu yüzden ölçülmeden fark edilmez. Düzenli egzersiz tansiyonu düşürmenin en etkili ilaç dışı yollarından biridir ve tansiyonu yüksek olanlarda etkisi bazı ilaçlarınkine yakın olabilir. Bu rehber değerlerin ne anlama geldiğini, hangi egzersizin ne kadar düşürdüğünü, evde nasıl doğru ölçüleceğini ve altı ev egzersizini anlatıyor.</p>
    <p class="meta">Son güncelleme: 23 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>1,4 milyar</b><span>2024’te dünyada tansiyonu yüksek olan 30–79 yaş arası kişi; beşte birinden azında tansiyon kontrol altında</span></div>
        <div class="stat"><b>−8,3/−5,2</b><span>Tansiyonu yüksek olanlarda dayanıklılık egzersiziyle ortalama düşüş, mmHg (93 çalışmalık meta-analiz)</span></div>
        <div class="stat"><b>150 dk + 2–3 gün</b><span>Haftalık orta şiddette aerobik egzersiz ve direnç egzersizi önerisi (Avrupa Kardiyoloji Derneği)</span></div>
        <div class="stat"><b>135/85</b><span>Evde ölçülen ortalamada yüksek tansiyonu düşündüren sınır; 80 yaş ve üzerinde 145/85</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Değerler ne anlama geliyor?</h2>
        <p class="soft">Avrupa Kardiyoloji Derneği’nin 2024 kılavuzu muayenede ölçülen tansiyonu üç gruba ayırıyor:</p>
        <ul class="dots">
          <li><b>Yükselmemiş:</b> büyük tansiyon 120’nin, küçük tansiyon 70’in altında.</li>
          <li><b>Yükselmiş:</b> büyük tansiyon 120–139 ya da küçük tansiyon 70–89.</li>
          <li><b>Yüksek tansiyon (hipertansiyon):</b> 140/90 ve üzeri.</li>
        </ul>
        <p class="soft">Tek bir yüksek ölçüm tanı koydurmaz; tanı için genellikle evde ya da 24 saatlik cihazla yapılan ölçümlerle doğrulama gerekir. 40 yaş üstündeki herkesin en az 5 yılda bir tansiyonunu ölçtürmesi öneriliyor.</p>
      </div>
      <div>
        <h2>Kimlerde daha sık?</h2>
        <ul class="dots">
          <li>65 yaş üstündekiler ve ailesinde yüksek tansiyon olanlar.</li>
          <li>Fazla kilolu olanlar ve hareketsiz yaşayanlar.</li>
          <li>Tuzlu beslenen, az meyve ve sebze yiyenler.</li>
          <li>Sigara ve çok alkol içenler, uykusu yetersiz olanlar.</li>
        </ul>
        <p class="soft">Sürekli yüksek tansiyon kalp krizi, inme, kalp yetmezliği, böbrek hastalığı ve damarsal bunama riskini artırır; tansiyondaki küçük bir düşüş bile bu riskleri azaltır.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Egzersiz tansiyonu ne kadar düşürür?</h2>
      <p class="soft">93 rastgele kontrollü çalışmayı ve 5.223 yetişkini kapsayan bir meta-analizde dinlenme tansiyonu dayanıklılık egzersiziyle ortalama 3,5/2,5, dinamik direnç egzersiziyle 1,8/3,2, izometrik egzersizle 10,9/6,2 mmHg düştü. Dayanıklılık egzersizinin etkisi tansiyonu yüksek olanlarda daha büyüktü (8,3/5,2 mmHg). Tansiyonu yüksek 1.143 yetişkinle yapılan 24 çalışmanın analizinde izometrik egzersiz büyük tansiyonu 7, küçük tansiyonu 4 mmHg düşürdü ve yan etki riskini artırmadı.</p>
      <p class="soft">391 çalışmayı birleştiren bir ağ meta-analizinde, tansiyonu yüksek olanlarda dayanıklılık ve direnç egzersizinin büyük tansiyonu düşürme etkisi, sık kullanılan tansiyon ilaçlarınınkinden belirgin farklı bulunmadı. Ancak egzersiz ile ilacı doğrudan karşılaştıran bir çalışma yoktu ve tansiyonu yüksek kişilerde yapılan egzersiz çalışmaları azdı.</p>
      <div class="callout">
        <p>Avrupa Kardiyoloji Derneği haftada en az 150 dakika orta ya da 75 dakika yüksek şiddette aerobik egzersizin yanında, haftada 2–3 gün dinamik ya da izometrik direnç egzersizi öneriyor. Egzersiz ilaç tedavisinin yerini tutmayabilir; ilacınızı hekiminize danışmadan bırakmayın.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Evde doğru ölçüm</h2>
      <ul class="tx">
        <li><b>Cihaz</b><span>Kolunuza uygun manşonu olan, doğruluğu klinik olarak test edilmiş, üst koldan ölçen bir cihaz kullanın; bilek ve parmak cihazlarını değil.</span></li>
        <li><b>Hazırlık</b><span>Ölçümden önceki 30 dakika yemek yemeyin, sigara, kahve ve egzersizden kaçının; tuvalete gidin.</span></li>
        <li><b>Duruş</b><span>Sırtınız destekli, bacaklarınız çapraz olmadan oturun; kolunuzu kalp hizasında bir masaya koyun. 5 dakika sessizce dinlenin, ölçüm sırasında konuşmayın.</span></li>
        <li><b>Ölçüm</b><span>1 dakika arayla iki ölçüm yapın; sabah (ilaçlardan önce) ve akşam. Her ölçümü, yüksek çıkanlar dahil, olduğu gibi kaydedin.</span></li>
        <li><b>Ortalama</b><span>Tek tek ölçümlere değil, birkaç günün ortalamasına bakın. Tanı için 4–7 gün ölçüp ilk günü atarak ortalama alınması öneriliyor.</span></li>
      </ul>
      <p class="soft" style="margin-top:14px">Ölçümlerinizi kaydetmek ve ortalamanızı hesaplamak için <a href="tansiyon-gunlugu.html">ev tansiyon günlüğünü</a> kullanabilirsiniz.</p>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Yüksek tansiyonda altı egzersiz</h2>
      <p class="soft">Bu program yürüyüşü, izometrik bir egzersizi ve büyük kas gruplarını çalıştıran direnç egzersizlerini bir araya getiriyor. Tekrar sayıları genel önerilerdir. Tansiyonunuz çok yüksekse ya da kontrol altında değilse başlamadan önce hekiminize danışın; hareketler sırasında nefesinizi tutmayın.</p>
      {ex_grid(["ht_walk", "ht_wall", "ht_sts", "ht_push", "ht_row", "ht_bridge"])}
      <p class="soft" style="margin-top:14px">Duvar oturuşunu süre ve dinlenme aralıklarıyla birlikte yapmak için <a href="duvar-oturusu.html">duvar oturuşu zamanlayıcısını</a> kullanabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(HT_FAQ)}
      <p class="soft" style="margin-top:18px">Tempolu yürüyüşün hızını ayarlamak için <a href="tempolu-yuruyus.html">tempolu yürüyüş metronomuna</a>, nabzınızı ölçmek için <a href="nabiz-olcer.html">nabız ölçere</a> bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">“Acil” yazan durumlarda 112’yi arayın; kendiniz araç kullanarak hastaneye gitmeyin:</p>
      <ul class="dots redflags">
        <li>Geçmeyen ani göğüs ağrısı ya da sıkışma; kola, boyna, çeneye, mideye ya da sırta yayılan ağrı; terleme, bulantı, sersemlik ya da nefes darlığıyla birlikte göğüs ağrısı (acil)</li>
        <li>Yüzde kayma, kolda güçsüzlük, konuşma bozukluğu (acil)</li>
        <li>Evde art arda üç ölçümde büyük tansiyonun 200 ya da üzerinde çıkması: hemen hekime</li>
        <li>Sık baş ağrısı, bulanık görme ya da gelip giden göğüs ağrısı: hekiminize</li>
      </ul>
      {CTA_CARD("Yüksek tansiyonda egzersiz programınız", "yüksek tansiyonda egzersiz programı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(HT_SRC)}
    </div>
  </section>
</main>'''

page("yuksek-tansiyon.html", "Yüksek Tansiyonda Egzersiz",
     "Yüksek tansiyonda egzersiz: değerler ne anlama geliyor, hangi egzersiz tansiyonu ne kadar düşürür, evde doğru ölçüm, tuz, ne zaman başvurmalı ve altı ev egzersizi.",
     "yuksek-tansiyon.html", NECK_CSS, HT_BODY, "",
     seo_title="Yüksek Tansiyonda Egzersiz: Ne Kadar Düşürür, Evde Doğru Ölçüm | İhsan Eren",
     condition="Yüksek tansiyon (hipertansiyon)", faq_items=HT_FAQ)
