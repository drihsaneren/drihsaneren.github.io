# -*- coding: utf-8 -*-
# Evde rehabilitasyon: multipl skleroz (MS) ve egzersiz.
# cond5_part.py'den sonra exec edilir.

_ex2("ms_sts", "sts", "Sandalyeden kalkıp oturma", "Sağlam bir sandalyenin önüne oturun, ayaklarınızı biraz geriye alın. Öne eğilerek ayağa kalkın ve kontrollü şekilde oturun. Zorlanıyorsanız sandalyenin kollarından ya da önünüzdeki tezgâhtan destek alın. Bacak gücü, yürümenin ve yataktan sandalyeye geçişlerin temelidir.", "8–10 tekrar, 1–2 set")
_ex2("ms_bridge", "bridge", "Köprü", "Sırtüstü yatın, dizleriniz bükülü, ayaklarınız yerde. Kalçanızı sıkarak omuzlarınızdan dizlerinize düz bir çizgi oluşana kadar kaldırın, 3 saniye tutup yavaşça inin. Yatarak yapıldığı için yorgun günlerde de uygundur.", "8–10 tekrar, 1–2 set")
_ex2("ms_heel", "heel", "Tezgâha tutunarak topuk yükseltme", "Mutfak tezgâhına iki elinizle tutunun. Parmak uçlarınıza yükselin, bir an bekleyip yavaşça inin. Ardından topuklarınızın üzerinde durup ayak uçlarınızı yerden kaldırın. Baldır ve ayak bileği kasları adım atarken ayağı taşır.", "Her birinden 10 tekrar")
_ex2("ms_sls", "sls", "Tek ayak üzerinde durma", "Tezgâhın önünde dik durun, bir ya da iki elinizle hafifçe tutunun. Bir ayağınızı yerden kaldırıp dengede kalın. Kolaylaştıkça tek parmağınızla tutunun. Arkanızda bir sandalye dursun; ilk zamanlarda yanınızda biri bulunsun.", "10–15 saniye, her ayakla 3 kez")
_ex2("ms_calf", "calf", "Duvarda baldır germe", "Ellerinizi duvara dayayın, bir bacağınızı arkaya alın. Arkadaki diziniz düz, topuğunuz yerde olsun; öndeki dizinizi bükerek baldırınızda gerginlik hissedin. Yaylanmadan, yavaşça gerin; ani ve hızlı germe kas sertliğini artırabilir.", "30 saniye, her bacakla 3 tekrar")
_ex2("ms_walk", "walk", "Yürüyüş ya da sabit bisiklet", "Konuşabileceğiniz bir tempoda yürüyün ya da sabit bisiklet çevirin. Birkaç dakikalık bölümlerle başlayın, aralara dinlenme koyun ve süreyi haftadan haftaya artırın. Serin saatleri seçin, yanınızda soğuk su bulundurun.", "5–10 dakikayla başlayın; hedef haftada toplam 150 dakika")

MS_FAQ = [
 ("Egzersiz atak tetikler mi?", "Araştırmalar bunu göstermiyor. 26 çalışmayı ve 1.295 kişiyi inceleyen bir derlemede atak oranı egzersiz yapanlarda %4,6, yapmayanlarda %6,3 idi; egzersiz atak riskini artırmadı. İngiltere kılavuzu (NICE) da düzenli egzersizin MS üzerinde zararlı bir etkisi olmadığını belirtiyor."),
 ("Egzersizden sonra belirtilerim artıyor; zarar mı veriyorum?", "Vücut ısısı yükseldiğinde MS belirtileri geçici olarak artabilir. Bu genellikle yeni bir hasar anlamına gelmez; vücut soğuyunca belirtilerin birkaç saat içinde yatışması beklenir. Serin ortamda, molalarla ve soğuk su içerek çalışmak yardımcı olur. Yeni bir belirti ya da kötüleşme 24 saatten uzun sürerse nöroloğunuza başvurun."),
 ("Çok yorgunum; yine de egzersiz yapmalı mıyım?", "Evet, ama az ve yavaş başlayarak. 45 çalışmayı kapsayan Cochrane derlemesinde egzersiz, MS'e bağlı yorgunluğu egzersiz yapmamaya göre anlamlı şekilde azalttı. Egzersizi enerjinizin en iyi olduğu saatlere koyun ve kısa bölümlere ayırın. Uyku sorunları, depresyon ya da kansızlık gibi durumlar da yorgunluğu artırabilir; bunları hekiminizle konuşun."),
 ("Ne kadar egzersiz yapmalıyım?", "Uzman önerilerine göre hedef haftada en az 150 dakika egzersiz ve/veya en az 150 dakika günlük fiziksel aktivitedir (yürüyerek alışveriş, ev ve bahçe işleri gibi). Bu hedefe kademeli olarak ulaşılır ve program kişinin durumuna göre ayarlanır."),
]

MS_SRC = [
 "Multiple Sclerosis International Federation. " + ext("https://www.msif.org/wp-content/uploads/2026/09/Atlas-Epidemiology-report-text-core-data-2026-FINAL.pdf", "Atlas of MS 2026: a global update on MS prevalence, incidence, and the gaps that remain") + ". London: MSIF; 2026.",
 "National Institute for Health and Care Excellence. " + ext("https://www.nice.org.uk/guidance/ng220", "Multiple sclerosis in adults: management (NG220)") + ". London: NICE; 2022.",
 "Kalb R, Brown TR, Coote S, et al. " + ext("https://journals.sagepub.com/doi/10.1177/1352458520915629", "Exercise and lifestyle physical activity recommendations for people with multiple sclerosis throughout the disease course") + ". Mult Scler. 2020;26(12):1459-1469.",
 "Heine M, van de Port I, Rietberg MB, et al. " + ext("https://www.cochrane.org/evidence/CD009956_exercise-therapy-fatigue-multiple-sclerosis", "Exercise therapy for fatigue in multiple sclerosis") + ". Cochrane Database Syst Rev. 2015;(9):CD009956.",
 "Pilutti LA, Platta ME, Motl RW, Latimer-Cheung AE. " + ext("https://www.sciencedirect.com/science/article/abs/pii/S0022510X14003062", "The safety of exercise training in multiple sclerosis: a systematic review") + ". J Neurol Sci. 2014;343(1-2):3-7.",
 "Nilsagård Y, Gunn H, Freeman J, et al. " + ext("https://journals.sagepub.com/doi/10.1177/1352458514538884", "Falls in people with MS—an individual data meta-analysis from studies from Australia, Sweden, United Kingdom and the United States") + ". Mult Scler. 2015;21(1):92-100.",
 "MS Trust. " + ext("https://mstrust.org.uk/a-z/heat-sensitivity-uhthoffs-phenomenon", "Heat sensitivity and MS (Uhthoff's phenomenon)") + ". 2026.",
]

MS_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Rehabilitasyon rehberi</p>
    <h1>Multipl sklerozda (MS) egzersiz ve evde rehabilitasyon</h1>
    <p class="lede">MS, bağışıklık sisteminin beyin ve omurilikteki sinir liflerinin kılıfına zarar verdiği, belirtileri kişiden kişiye çok değişen bir hastalıktır. Güncel kılavuzlara göre düzenli egzersiz MS'te güvenlidir; araştırmalarda atak riskini artırmadığı, yorgunluğu ise azalttığı görülmüştür.</p>
    <p class="meta">Son güncelleme: 4 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>3,1 milyon</b><span>Dünyada MS ile yaşayan kişi (Atlas of MS, 2026)</span></div>
        <div class="stat"><b>32</b><span>Tanının konulduğu ortalama yaş; her 10 hastanın 7'si kadın</span></div>
        <div class="stat"><b>150 dk</b><span>Uzman önerilerinde haftalık egzersiz ve/veya günlük fiziksel aktivite hedefi</span></div>
        <div class="stat"><b>%56</b><span>537 kişilik bir analizde 3 ay içinde en az bir kez düşen MS'liler</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Multipl sklerozda bağışıklık sistemi, beyin ve omurilikteki sinir liflerini saran koruyucu kılıfa (miyelin) zarar verir; sinirlerin taşıdığı sinyaller yavaşlar ya da kesintiye uğrar. Belirtiler hasarın yerine göre değişir: yorgunluk, yürüme ve denge güçlüğü, kaslarda sertlik, uyuşma, görme ve idrar sorunları görülebilir. Çoğu kişide hastalık ataklar ve düzelme dönemleriyle seyreder; bir kısmında belirtiler yavaş yavaş ilerler.</p>
        <p class="soft">MS'in ilaç tedavisini nöroloji uzmanı yürütür. Rehabilitasyon bu tedavinin yerini tutmaz; onu tamamlar ve günlük hayatta bağımsızlığı korumayı hedefler.</p>
      </div>
      <div>
        <h2>Evde rehabilitasyon neleri hedefler?</h2>
        <ul class="dots">
          <li>Yorgunluğu azaltmak ve enerjiyi gün içine yaymak</li>
          <li>Yürümeyi ve dengeyi geliştirmek, düşmeleri önlemek</li>
          <li>Kas gücünü ve kondisyonu korumak</li>
          <li>Kaslardaki sertlikle başa çıkmak</li>
          <li>Sandalyeden kalkma, merdiven çıkma gibi günlük işleri kolaylaştırmak</li>
          <li>Gerektiğinde yürüme yardımcılarını ve ev düzenini kişiye göre ayarlamak</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Egzersiz güvenli mi, işe yarıyor mu?</h2>
      <p class="soft">İngiltere kılavuzu (NICE, 2022) MS'lilerin egzersize teşvik edilmesini öneriyor: düzenli egzersizin MS üzerinde yararlı etkileri olabilir ve zararlı bir etkisi yoktur. 26 çalışmayı ve 1.295 kişiyi inceleyen bir derlemede atak oranı egzersiz yapanlarda %4,6, yapmayanlarda %6,3 idi; egzersiz atak riskini artırmadı.</p>
      <p class="soft">45 çalışmayı ve 2.250 MS'liyi kapsayan Cochrane derlemesinde egzersiz, yorgunluğu egzersiz yapmamaya göre anlamlı şekilde azalttı. Dayanıklılık egzersizi, birden çok türü birleştiren programlar ve yoga gibi egzersizler etkili bulundu. 2020'de yayımlanan uzman önerileri, MS'li herkes için haftada en az 150 dakika egzersiz ve/veya en az 150 dakika günlük fiziksel aktivite hedefliyor ve tanıdan sonra erken dönemde MS'te deneyimli bir fizyoterapist ya da iş ve uğraşı terapistince değerlendirilmeyi öneriyor.</p>
      <div class="callout">
        <p>NICE'a göre aerobik, direnç ve denge egzersizleri, yoga ve pilates MS'e bağlı yorgunluğa iyi gelebilir. Ayakta dengesi kısıtlı olan kişilerde vestibüler rehabilitasyon da düşünülebilir. Hareket sorunu olan MS'lilerin, MS'te deneyimli rehabilitasyon uzmanları ve fizyoterapistlerce değerlendirilmesi ve kişisel hedefler belirlenmesi önerilir.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Sıcak ve yorgunluk</h2>
        <p class="soft">MS'li her 10 kişiden yaklaşık 6'sı sıcağa duyarlıdır. Vücut ısısı yükseldiğinde (egzersiz, sıcak hava, sıcak banyo, ateş) belirtiler geçici olarak artabilir. Bu genellikle yeni bir hasar anlamına gelmez; vücut ısısı normale dönünce belirtilerin birkaç saat içinde yatışması beklenir.</p>
        <p class="soft">NICE, MS'e bağlı yorgunluğun sıcakla ya da bedensel ve duygusal stresle ortaya çıkabileceğini belirtiyor. Bu yüzden egzersizi bırakmak yerine koşullarını ayarlamak gerekir.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Günün serin saatlerinde ve serin, havadar bir odada egzersiz yapın.</li>
        <li>Egzersizden önce ve egzersiz sırasında soğuk su için.</li>
        <li>Egzersizi kısa bölümlere ayırın, aralarda dinlenin.</li>
        <li>Enerjinizin en iyi olduğu saatleri seçin; yorucu işleri gün içine yayın.</li>
        <li>Egzersizden sonra yavaşça soğuyun; ılık ya da serin bir duş yardımcı olabilir.</li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Kuvvet, denge ve dayanıklılık: altı egzersiz</h2>
      <p class="soft">Ayakta yapılan hareketlerde tezgâh gibi sağlam bir desteğin yanında durun. Yorgunluk ya da belirtileriniz artarsa durup dinlenin. Program kişinin durumuna göre değişir; aşağıdakiler genel bir başlangıçtır.</p>
      {ex_grid(["ms_sts", "ms_bridge", "ms_heel", "ms_sls", "ms_calf", "ms_walk"])}
      <div class="callout">
        <p>Hareketiniz çok kısıtlıysa ya da tekerlekli sandalye kullanıyorsanız egzersiz yine önerilir. Uzman önerilerine göre bu durumda egzersiz, eğitimli bir yardımcının desteğiyle yapılmalıdır.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Günlük hayatta pratik öneriler</h2>
        <p class="soft">537 MS'linin izlendiği analizde düşmelerin %65'i ev içinde oldu. Küçük değişiklikler hem güvenliği artırır hem de bağımsızlığı korur.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Kaygan halıları kaldırın, geceleri koridoru aydınlatın, banyoya tutunma barı taktırın.</li>
        <li>Sık kullandığınız eşyaları kolay uzanabileceğiniz yerlere koyun.</li>
        <li>Yorucu işlerin arasına kısa dinlenmeler koyun; her şeyi aynı güne sığdırmayın.</li>
        <li>Sigara içmeyin; NICE, sigaranın MS'te engelliliğin ilerlemesini artırdığını belirtiyor.</li>
        <li>Düşme riskiniz varsa <a href="dusme-onleme.html">düşmeleri önleme rehberine</a> göz atın.</li>
      </ul>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>MS için videolar</h2>
      <p class="soft">İngiltere MS Derneği'nin (MS Society UK) ve Cleveland Clinic'in YouTube kanallarından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("0DTnlCCxS7s", "Denge ve stabilite çalışması videosunu oynat", "Improve your balance and stability workout | Move more with MS")}
          <h3>Denge ve stabilite çalışması</h3>
          <p>MS Derneği'nin “Move more with MS” dizisinden.</p>
        </div>
        <div class="vid">
          {vbox("X8nkMFcBIvA", "MS için egzersizler videosunu oynat", "Exercises for Individuals with Multiple Sclerosis (MS) - Warm-up, Strength, Core and Balance")}
          <h3>Isınma, güç, gövde ve denge egzersizleri</h3>
          <p>Cleveland Clinic'in MS'li kişiler için hazırladığı egzersiz videosu.</p>
        </div>
      </div>
      <p class="meta">Videolar MS Society UK ve Cleveland Clinic kanallarına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(MS_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden nöroloğunuza ya da bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>24 saatten uzun süren yeni bir belirti ya da mevcut belirtilerde belirgin kötüleşme (atak olabilir)</li>
        <li>Görmede ani azalma, çift görme ya da göz hareketiyle artan göz ağrısı</li>
        <li>Ateş, idrar yaparken yanma gibi enfeksiyon belirtileri</li>
        <li>Yutkunma güçlüğü, yemek sırasında sık öksürme ya da boğulma hissi</li>
        <li>Yaralanmayla sonuçlanan düşme ya da sık tekrarlayan düşmeler</li>
        <li>Yüzde, kolda ya da bacakta ani güçsüzlük ya da konuşma bozukluğu (<strong>112</strong>)</li>
      </ul>
      {CTA_CARD("MS'te evde rehabilitasyon", "multipl skleroz (MS)")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(MS_SRC)}
    </div>
  </section>
</main>'''

page("multipl-skleroz.html", "Multipl Sklerozda (MS) Egzersiz",
     "MS'te egzersiz güvenli mi, atak tetikler mi, yorgunluğa iyi gelir mi? Sıcağa duyarlılıkla başa çıkma, kılavuz önerileri, evde altı egzersiz ve günlük hayat önerileri.",
     "multipl-skleroz.html", NECK_CSS, MS_BODY, YT_JS,
     seo_title="Multipl Sklerozda (MS) Egzersiz ve Evde Rehabilitasyon | İhsan Eren",
     condition="Multipl skleroz (MS)", faq_items=MS_FAQ)
