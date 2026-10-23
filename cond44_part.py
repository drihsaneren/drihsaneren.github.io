# -*- coding: utf-8 -*-
# Yeni rehber (44): Doğum sonrası karın kası ayrılması (diastazis rekti). cond43_part.py'den sonra exec edilir. Video yok.
# Egzersizler Royal Devon (2020) ve Oxford University Hospitals (2022) NHS broşürlerine göre, hazır çizimlerle.

_ex2("dr_flat", "ptilt", "Karın düzleştirme", "Sırtüstü yatın, dizleriniz bükülü, ayaklarınız yerde olsun. Karın kaslarınızı nazikçe içeri çekin ve belinizin çukurunu yatağa doğru düzleştirin. 3–5 saniye tutun, sonra gevşeyin. Rahat ettikçe yan yatarak, otururken ya da ayakta da deneyin.", "Önce 5 tekrar, günde 5–6 kez")
_ex2("dr_tra", "pf_sit", "Derin karın kasını çalıştırma", "Dik oturun. Göbeğinizin altındaki karın kaslarınızı hafifçe omurganıza doğru ve biraz yukarı çekin; rahat ettiğiniz kadar tutun. Nefesinizi tutmayın: nefesi tutuyorsanız fazla sıkıyorsunuzdur.", "Gün içinde sık sık; kaldırma ve taşıma öncesinde")
_ex2("dr_pfs", "pf_lie", "Pelvik taban: uzun kasılma", "Sırtüstü yatın, dizleriniz bükülü olsun. Gaz ve idrarı tutuyormuş gibi ön ve arka çıkış çevresindeki kasları sıkıp içe ve yukarı çekin. Normal nefes alıp vermeye devam edin.", "10 saniye tutun, 10 tekrara kadar")
_ex2("dr_pfq", "pf_stand", "Pelvik taban: hızlı kasılma", "Aynı kasları hızla sıkın, bir saniye tutun ve tamamen gevşetin. Yatarak rahatça yapabildiğinizde oturarak, sonra ayakta deneyin.", "10–15 tekrar")

DR_FAQ = [
 ("Ayrılmayı kendim nasıl kontrol ederim?", "Sırtüstü yatın, dizleriniz bükülü olsun. Bir elinizin parmaklarını göbeğinizin hemen altına koyun. Karın kaslarınızı içeri çekip başınızı ve omuzlarınızı yavaşça kaldırın; iki kas şeridinin ortada sıkılaştığını hissedersiniz. Aradaki boşluğun kaç parmak genişliğinde olduğunu sayın."),
 ("Mekik ve diğer karın egzersizlerini yapabilir miyim?", "Bir NHS hastane broşürü, aralık iki parmaktan genişse diğer karın egzersizlerini aralık daralana kadar erteleyip yukarıdaki egzersizlere odaklanmayı öneriyor. Bu bir uygulama önerisidir; hangi karın egzersizinin ne zaman güvenli olduğunu gösteren güçlü araştırma kanıtı henüz yok. Gövdeyi aşırı burkan ya da yana büken hareketlerden kaçının. Spora ve ağır egzersize kademeli dönmek, bel ve leğen ağrısı riskini azaltır."),
 ("Egzersiz aralığı kapatır mı?", "Belirli bir egzersiz programının aralığı kapattığına dair kanıt şu an çok zayıf: 381 annenin katıldığı 7 çalışmayı inceleyen bir derleme, belirli bir program önermek için yeterli kanıt bulamadı. Yine de derin karın ve pelvik taban egzersizleri güvenli ve kasları güçlendirmek için iyi bir başlangıçtır. 13 çalışmayı birleştiren 2025 tarihli bir meta-analizde karın egzersizleri göbeğin altındaki aralığı, karın bandına ya da hiçbir şey yapmamaya göre biraz daha çok daralttı; göbeğin üstündeki aralıkta belirgin bir etki görülmedi. Daha eski bir derlemede gebelikte egzersiz yapanlarda doğumdan sonra ayrılma görülme sıklığı %35 daha azdı, ama çalışmaların kalitesi düşüktü."),
 ("Bel ağrısına yol açar mı?", "300 annenin izlendiği bir araştırmada, doğumdan 12 ay sonra karın kası ayrılması olan ve olmayan anneler aynı düzeyde bel ve leğen ağrısı bildirdi."),
 ("Korse işe yarar mı?", "Sıkı giysiler, korse ya da karın bandı iyileşme döneminde destek sağlayabilir. Ancak kaslarınızı çalıştırmanın yerini tutmaz."),
]

DR_SRC = [
 "Sperstad JB, Tennfjord MK, Hilde G, Ellström-Engh M, Bø K. " + ext("https://bjsm.bmj.com/content/50/17/1092", "Diastasis recti abdominis during pregnancy and 12 months after childbirth: prevalence, risk factors and report of lumbopelvic pain") + ". Br J Sports Med. 2016;50(17):1092–1096.",
 "Gluppe S, Engh ME, Bø K. " + ext("https://search.pedro.org.au/search-results/record-detail/66303", "What is the evidence for abdominal and pelvic floor muscle training to treat diastasis recti abdominis postpartum? A systematic review with meta-analysis") + ". Braz J Phys Ther. 2021;25(6):664–675.",
 "Oxford University Hospitals NHS Foundation Trust. " + ext("https://ulive.ouh.nhs.uk/media/gedal1lb/74152pdiastasis.pdf", "Recti diastasis") + ". June 2022.",
 "Royal Devon and Exeter NHS Foundation Trust. " + ext("https://www.royaldevon.nhs.uk/media/n5ojlmrn/patient-information-leaflet-separation-of-the-abdominal-muscles-rde-20-147-001.pdf", "Separation of the abdominal muscles (diastasis recti abdominis)") + ". October 2020.",
 "Abdullah, Rehman KA, Ahmad B, et al. " + ext("https://search.pedro.org.au/search-results/record-detail/82165", "Comparative efficacy of abdominal exercises and abdominal binding on diastasis recti abdominis reduction in postpartum women: a systematic review and meta-analysis of randomized controlled trials") + ". Physiother Res Int. 2025;30(2):e70038.",
 "Benjamin DR, van de Water ATM, Peiris CL. " + ext("https://search.pedro.org.au/search-results/record-detail/38278", "Effects of exercise on diastasis of the rectus abdominis muscle in the antenatal and postnatal periods: a systematic review") + ". Physiotherapy. 2014;100(1):1–8.",
]

DR_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Doğum sonrası karın kası ayrılması (diastazis rekti)</h1>
    <p class="lede">Doğumdan sonra yataktan kalkarken ya da öksürürken karnınızın ortasında kubbe gibi bir kabarıklık mı görüyorsunuz? Gebelikte karın kaslarını ortada birleştiren bağ dokusu, bebeğe yer açmak için yumuşar ve gerilir; kaslar arasında bir aralık oluşur. Bu tehlikeli değildir ve çok sık görülür. Doğru günlük alışkanlıklar ve basit egzersizlerle karın duvarınızı yeniden güçlendirebilirsiniz.</p>
    <p class="meta">Son güncelleme: 16 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%60</b><span>İlk doğumunu yapan annelerde doğumdan 6 hafta sonra görülme oranı</span></div>
        <div class="stat"><b>%33</b><span>Aynı annelerde doğumdan 12 ay sonraki oran</span></div>
        <div class="stat"><b>6–8 hafta</b><span>Küçük ayrılmaların çoğu zaman kapandığı süre</span></div>
        <div class="stat"><b>2 parmak</b><span>Bir NHS broşürüne göre aralık bundan genişse diğer karın egzersizlerini ertelemek öneriliyor</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Yataktan doğrulurken, öksürürken ya da hapşırırken karnın ortasında kubbe gibi kabarma.</li>
          <li>Göbek çevresinde, karın kasları arasında parmakla hissedilen bir aralık.</li>
          <li>Karın duvarında gevşeklik hissi.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Gebelikte karın kaslarını ortada birleştiren ince bağ dokusu yumuşar ve gerilir.</li>
          <li>Bu, gebeliğin olağan bir parçasıdır; sorun yalnızca kaslar doğumdan sonra eski yerlerine dönmezse ortaya çıkar.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Yana dönerek kalkın</h3><p>Sırtüstü yatarken doğrudan doğrulmayın. Önce yana dönün, sonra dirseklerinizle iterek kalkın.</p></div>
        <div class="kind"><span class="n">2</span><h3>Yükü ayarlayın</h3><p>İlk dönemde bebeğinizden ağır şeyleri kaldırmayın. Bebeğinizi kaldırmadan önce karın kaslarınızı hafifçe sıkın.</p></div>
        <div class="kind"><span class="n">3</span><h3>Derin kasları çalıştırın</h3><p>Doğumdan sonraki ilk günlerden itibaren derin karın ve pelvik taban kaslarınızı nazikçe çalıştırmaya başlayabilirsiniz.</p></div>
        <div class="kind"><span class="n">4</span><h3>Kademeli dönün</h3><p>Spora ve ağır işlere erken ve hızlı dönmeyin. Adımları atlamak derin karın kaslarında zayıflık bırakabilir.</p></div>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Karın duvarını güçlendiren dört egzersiz</h2>
      <p class="soft">Egzersizler ağrı ya da rahatsızlık yapmamalı. Pelvik tabanınızda aşağı doğru bir baskı hissediyorsanız teknik doğru değildir; bırakın ve bir fizyoterapiste danışın. Nefesinizi tutmayın.</p>
      {ex_grid(["dr_flat", "dr_tra", "dr_pfs", "dr_pfq"], "ex four")}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(DR_FAQ)}
      <p class="soft" style="margin-top:18px">Pelvik taban için <a href="idrar-kacirma.html">idrar kaçırma</a>, gebelik dönemi için <a href="gebelikte-bel-agrisi.html">gebelikte bel ağrısı</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman bir uzmana başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Ayrılma doğumdan 6–8 hafta sonra hâlâ azalmadıysa</li>
        <li>Egzersiz sırasında ağrı ya da pelvik tabanda aşağı doğru baskı hissediyorsanız</li>
        <li>Bel ya da leğen ağrınız varsa</li>
        <li>Dışkılamada zorlanıyor ya da kabızlık yaşıyorsanız</li>
        <li>Günlük işlerinizde süregelen güçlük çekiyorsanız</li>
      </ul>
      {CTA_CARD("Doğum sonrası karın ve pelvik taban sağlığınız", "doğum sonrası karın kası ayrılması")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(DR_SRC)}
    </div>
  </section>
</main>'''

page("karin-kasi-ayrilmasi.html", "Doğum Sonrası Karın Kası Ayrılması (Diastazis Rekti)",
     "Doğumdan sonra karnınızın ortasında kabarıklık mı var? Karın kası ayrılması ne kadar sık, kendiliğinden kapanır mı, hangi egzersizler güvenli? Kendi kendine kontrol ve evde dört egzersiz.",
     "karin-kasi-ayrilmasi.html", NECK_CSS, DR_BODY, "",
     seo_title="Doğum Sonrası Karın Kası Ayrılması (Diastazis Rekti): Kontrol, Egzersizler | İhsan Eren",
     condition="Diastazis rekti", faq_items=DR_FAQ)
