# -*- coding: utf-8 -*-
# Yeni rehber (62): Beyin sarsıntısı (konküzyon) sonrası iyileşme ve kademeli harekete dönüş. cond61_part.py'den sonra exec edilir. Video yok.
# Kaynaklar (22 Ekim 2026'da okundu): BMJ basın bülteni (Amsterdam 2022 uzlaşısı, 14 Haziran 2023), UK Concussion Guidelines for Non-Elite (Grassroots) Sport
# (Kasım 2024 güncellemesi, HTML sürümü), NHS 111 Wales Head injury and concussion (19 Kasım 2024), Leddy 2019 (UB haberi + PEDro künyesi),
# Thomas 2015 (Contemporary Pediatrics özeti), Schneider 2014 (PEDro özeti), Sydney Children's Hospitals Network denge bilgi notu (4 Ağustos 2026).

_ex2("bs_walk", "walk", "Kısa yürüyüş", "Rahat bir tempoda, düz bir yolda yürüyün. Belirtileriniz en fazla hafifçe artıyor ve kısa sürede yatışıyorsa süreyi gün gün uzatabilirsiniz.", "Birkaç dakikayla başlayın; 3. aşamada 10–15 dakika")
_ex2("bs_gaze", "rot", "Göz sabitleme: baş çevirme", "Bir kalemi ya da kartı kol boyu uzaklıkta tutun ve gözünüzü ondan ayırmayın. Gözleriniz cisme kilitliyken başınızı yavaşça sağa sola çevirin. Hız ancak hazır olduğunuzda artırılır.", "5–10 tekrar, rahat ettiğiniz kadar")
_ex2("bs_nod", "bt_nod", "Yukarı ve aşağı bakma", "Dik oturun. Başınızı yavaşça kaldırıp tavana, sonra indirip yere bakın. Amaç, beynin baş hareketine yeniden alışmasıdır; baş dönmesi hafif kalmalı ve kısa sürede geçmeli.", "5–10 tekrar")
_ex2("bs_side", "side", "Başı yana eğme", "Dik oturun. Kulağınızı yavaşça omzunuza doğru yaklaştırın, ortaya dönün ve diğer yana eğin. Omzunuzu kaldırmayın.", "Her yana 5–10 tekrar")
_ex2("bs_tandem", "tandem", "Tandem duruş ve yürüyüş", "Bir duvarın yanında durun. Önce bir ayağınızı diğerinin hafif önüne koyarak 10 saniye durun, sonra ayaklarınızı değiştirin. Kolaylaşınca topuğunuzu öndeki ayağın parmak ucuna değdirerek bir koridor boyunca yürüyün.", "Her ayak önde 10 saniye; ardından 20 adım")
_ex2("bs_sls", "sls", "Tek ayak üstünde durma", "Sağlam bir sandalyeye tutunarak tek ayağınızın üstünde durun. Kolaylaşınca tutunmayı bırakın, süreyi uzatın; daha sonra gözlerinizi kapatmak ya da havaya harf çizmek gibi zorlaştırmalar ekleyebilirsiniz.", "10 saniyeyle başlayın, 30 saniyeye kadar")

BS_FAQ = [
 ("Karanlık bir odada dinlenmem gerekmiyor mu?", "Hayır. Uzun ve sıkı dinlenme artık önerilmiyor. 11–22 yaş arası 88 hastayla yapılan bir çalışmada 5 gün evde tam dinlenme önerilenler, 1–2 gün dinlenip kademeli olarak etkinliğe dönenlere göre daha fazla belirti bildirdi ve belirtileri daha yavaş geçti. İlk 24–48 saat görece dinlenin, uyuyabildiğiniz kadar uyuyun; ardından günlük işlere ve hafif yürüyüşlere kademeli olarak dönün."),
 ("Telefon ve bilgisayar kullanabilir miyim?", "İlk 48 saatte ekran süresini en aza indirmek iyileşmeye yardımcı olabilir. Sonra ekranı kısa sürelerle ve aralarda mola vererek kullanabilirsiniz; 3. aşamada zihinsel işler 20–30 dakikalık bloklar hâlinde önerilir."),
 ("Ne zaman okula ya da işe dönebilirim?", "Kendinizi daha iyi hissettiğinizde, önce kısa sürelerle. İngiltere’nin taban sporu kılavuzu okul ve işe dönüşü spora dönüşten önce tutuyor: dinlenirken belirtiniz kalmadığında, genellikle 2. hafta civarında yarı zamanlı okul ya da işe dönülebilir. Bu dönemde ödevler ve sınavlar için ek süre gibi düzenlemeler istenebilir."),
 ("Ne zaman spora dönebilirim?", "Antrenmana kademeli olarak dönülür; temaslı ve rekabetçi spora ise yaralanmadan sonraki 21. günden önce dönülmez ve bunun için dinlenirken en az 14 gün belirtisiz olmak gerekir. NHS de temas sporlarından en az 3 hafta uzak durmayı öneriyor. Çocuklar ilk birkaç gün sert oyunlardan kaçınmalı. Uluslararası uzlaşıya göre çoğu kişi yaklaşık bir ay içinde sporuna tam olarak döner."),
 ("Egzersiz iyileşmeyi hızlandırır mı?", "Hafif aerobik egzersiz yardımcı olabilir. Sporda beyin sarsıntısı geçiren 13–18 yaş arası 103 gençle yapılan bir çalışmada, ilk 10 gün içinde başlayıp belirtileri artırmayan bir şiddette günde yaklaşık 20 dakika yürüyüş ya da sabit bisiklet yapanlar ortalama 13 günde iyileşti; yalnızca germe yapanlarda bu süre 17 gündü. Egzersizin şiddeti, belirtilerinizi en fazla hafifçe artıracak düzeyde kalmalı."),
 ("Belirtilerim geçmezse ne yapmalıyım?", "Belirtiler 2 haftada düzelmez ya da kötüleşirse hekiminize başvurun; 4 haftayı aşarsa farklı uzmanlık alanlarından bir değerlendirme önerilir. Baş dönmesi, boyun ağrısı ya da baş ağrısı 10 günden uzun sürerse uluslararası uzlaşı boyun ve denge (servikovestibüler) rehabilitasyonunu öneriyor. Sporda beyin sarsıntısı geçiren 12–30 yaş arası 31 kişiyle yapılan küçük bir çalışmada, bu rehabilitasyonu alanların %73’ü 8 hafta içinde spora dönüş izni aldı; yalnızca olağan bakım alanlarda bu oran %7’ydi."),
]

BS_SRC = [
 "Patricios JS, Schneider KJ, Dvorak J, et al. " + ext("https://doi.org/10.1136/bjsports-2023-106898", "Consensus statement on concussion in sport: the 6th International Conference on Concussion in Sport – Amsterdam, October 2022") + ". Br J Sports Med. 2023;57(11):695–711. Özet: " + ext("https://bmjgroup.com/international-expert-panel-revises-management-of-concussion-in-sport", "BMJ Group, 14 June 2023") + ".",
 "Sport and Recreation Alliance, UK Government. " + ext("https://sportandrecreation.org.uk/campaigns-and-policy/concussion/concussion-guidelines-for-grassroots-sport-html-version", "UK Concussion Guidelines for Non-Elite (Grassroots) Sport") + ". November 2024 update.",
 "NHS 111 Wales. " + ext("https://111.wales.nhs.uk/headinjuryandconcussion", "Head injury and concussion") + ". Last updated 19 November 2024.",
 "HSE (Health Service Executive, Ireland). " + ext("https://www2.hse.ie/conditions/head-injury-concussion/", "Head injury and concussion") + ". Last reviewed 20 September 2024.",
 "Leddy JJ, Haider MN, Ellis MJ, et al. " + ext("https://doi.org/10.1001/jamapediatrics.2018.4397", "Early subthreshold aerobic exercise for sport-related concussion: a randomized clinical trial") + ". JAMA Pediatr. 2019;173(4):319–325. Özet: " + ext("https://www.buffalo.edu/news/releases/2019/02/002.html", "University at Buffalo, February 2019") + ".",
 "Thomas DG, et al. Benefits of strict rest after acute concussion: a randomized controlled trial. Pediatrics. 2015;135(2):213–223. Özet: " + ext("https://www.contemporarypediatrics.com/view/prolonged-rest-does-not-improve-acute-concussion-outcomes-adolescents", "Contemporary Pediatrics") + ".",
 "Schneider KJ, Meeuwisse WH, Nettel-Aguirre A, et al. " + ext("https://doi.org/10.1136/bjsports-2013-093267", "Cervicovestibular rehabilitation in sport-related concussion: a randomised controlled trial") + ". Br J Sports Med. 2014;48(17):1294–1298.",
 "Sydney Children’s Hospitals Network. " + ext("https://www.schn.health.nsw.gov.au/concussion-aftercare-balance-information-sheet", "Concussion aftercare: balance information sheet") + ". Last updated 4 August 2026.",
]

BS_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Beyin sarsıntısı: iyileşme ve harekete kademeli dönüş</h1>
    <p class="lede">Başınıza aldığınız bir darbe, düşme ya da ani bir sarsıntıdan sonra baş ağrısı, baş dönmesi, sersemlik ya da odaklanma güçlüğü mü yaşıyorsunuz? Beyin sarsıntısı (konküzyon), beynin geçici olarak etkilendiği bir yaralanmadır. Belirtiler çoğu zaman birkaç gün ile birkaç hafta içinde geçer. Eskiden önerilen uzun ve sıkı dinlenme artık önerilmiyor: ilk 24–48 saatlik görece dinlenmenin ardından günlük işlere ve hafif harekete adım adım dönmek iyileşmeye yardım ediyor.</p>
    <p class="meta">Son güncelleme: 27 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>24–48 saat</b><span>Görece dinlenme; ardından hafif etkinliklere kademeli dönüş</span></div>
        <div class="stat"><b>21. gün</b><span>Rekabetçi spora en erken dönüş (İngiltere taban sporu kılavuzu)</span></div>
        <div class="stat"><b>13’e karşı 17 gün</b><span>Hafif aerobik egzersiz yapan ve yalnızca germe yapan gençlerde ortalama iyileşme süresi</span></div>
        <div class="stat"><b>10 gün</b><span>Baş dönmesi, boyun ya da baş ağrısı bundan uzun sürerse boyun ve denge rehabilitasyonu önerilir</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Önce şunları kontrol edin</h2>
      <p class="soft">Kafa darbesinden sonra aşağıdakilerden biri varsa bu rehber yerine hemen tıbbi yardım alın. Kendiniz araç kullanarak acile gitmeyin.</p>
      <div class="two">
        <div>
          <h3>112’yi arayın</h3>
          <ul class="dots redflags">
            <li>Bayılıp ayılmadıysa ya da uyanık kalmakta zorlanıyorsa</li>
            <li>Nöbet geçirdiyse</li>
            <li>Konuşmakta, anlamakta, yürümekte ya da dengesini korumakta güçlük, vücudunun bir bölümünde uyuşma ya da güçsüzlük varsa</li>
            <li>Görme ya da işitme sorunu varsa</li>
            <li>Kulağından ya da burnundan berrak sıvı ya da kan geliyorsa, kulaklarının arkasında morarma varsa</li>
            <li>1 metreden ya da 5 basamaktan yüksekten düştüyse, araç ya da bisiklet kazası gibi hızlı bir darbe aldıysa</li>
          </ul>
        </div>
        <div>
          <h3>Acil servise gidin</h3>
          <ul class="dots redflags">
            <li>Kısa süre bayılıp ayıldıysa</li>
            <li>Kustuysa ya da kusması tekrarlıyorsa</li>
            <li>Ağrı kesiciyle geçmeyen ya da giderek artan baş ağrısı varsa</li>
            <li>Bellek sorunları, artan sersemlik, huzursuzluk ya da davranış değişikliği varsa; bebek ve küçük çocuk her zamankinden çok ağlıyorsa</li>
            <li>Kan sulandırıcı ilaç kullanıyor, kanama bozukluğu ya da beyin ameliyatı geçmişi varsa</li>
            <li>Darbeden hemen önce alkol ya da uyuşturucu almışsa</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Baş ağrısı, baş dönmesi, bulantı.</li>
          <li>Sersemlik, “sisli” hissetme, odaklanma ve hatırlama güçlüğü.</li>
          <li>Işığa ya da gürültüye hassasiyet, yorgunluk, uyku düzeninde değişiklik.</li>
          <li>Huzursuzluk, kaygı, ağlamaklı olma gibi duygu durum değişiklikleri.</li>
        </ul>
        <p class="soft">Belirtiler genellikle ilk 24 saat içinde başlar, ama 3 haftaya kadar gecikebilir. Hafif belirtiler 2 haftaya kadar sürebilir; çoğu kişi 4 hafta içinde iyileşir.</p>
      </div>
      <div>
        <h2>İlk 24–48 saat</h2>
        <ul class="dots">
          <li>İlk 24 saat yanınızda bir yetişkin bulunsun; yalnız kalmayın.</li>
          <li>İhtiyaç duyduğunuz kadar dinlenin ve uyuyun; telefon, bilgisayar ve ekran süresini en aza indirin.</li>
          <li>Alkol almayın; hekiminiz önermedikçe uyku ilacı kullanmayın.</li>
          <li>İlk 24 saatte bisiklete binmeyin, makine kullanmayın; tamamen iyileşene kadar araç kullanmayın.</li>
          <li>Baş ağrısı için ağrı kesici kullanmadan önce hekiminize ya da eczacınıza danışın; İrlanda sağlık servisi (HSE), kanamayı artırabileceği için bu dönemde ibuprofen ve aspirin yerine parasetamolü öneriyor. Şişlik olan yere havluya sarılı buz koyabilirsiniz.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Harekete ve spora kademeli dönüş</h2>
      <p class="soft">İngiltere’nin taban sporu için hazırladığı ve hükümetin desteklediği kılavuz, dönüşü altı aşamada anlatıyor. Bir sonraki aşamaya geçerken belirtilerinizin hafifçe artması sorun değil; yeter ki etkinlik onları en fazla hafifçe artırsın ve artış birkaç dakika ile birkaç saat içinde yatışsın. Belirtiler belirgin şekilde artarsa bir önceki aşamaya dönün.</p>
      <ul class="tx">
        <li><b>1. Görece dinlenme</b><span>İlk 24–48 saat: sakin etkinlikler, en az ekran.</span></li>
        <li><b>2. Günlük işler ve hafif etkinlik</b><span>Kısa ve kolay okumalar, kısa yürüyüşler, hafif ev işleri.</span></li>
        <li><b>3. Dayanıklılığı artırma</b><span>Zihinsel işler 20–30 dakikalık bloklar hâlinde; 10–15 dakikalık hafif aerobik egzersiz (yürüyüş, sabit bisiklet).</span></li>
        <li><b>4. Yarı zamanlı okul ya da iş, temassız antrenman</b><span>Dinlenirken belirtiniz kalmadığında, genellikle 2. hafta civarında.</span></li>
        <li><b>5. Tam zamanlı okul ya da iş, kısıtlamasız antrenman</b><span>En erken 15. gün; dinlenirken 14 gün belirtisiz olduktan sonra.</span></li>
        <li><b>6. Rekabete dönüş</b><span>21. günden önce değil; dinlenirken 14 gün belirtisiz olduktan sonra.</span></li>
      </ul>
      <div class="callout">
        <p>Okula ya da işe dönüş, spora dönüşten önce gelir. Kılavuzun ilkesi açık: şüphe varsa oyundan çıkın. Beyin sarsıntısından şüphelenilen kişi o gün oyuna, antrenmana ya da beden eğitimi dersine geri dönmez ve en az 24 saat bunlardan uzak durur.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Araştırmalar ne gösteriyor?</h2>
      <p class="soft">2022’de Amsterdam’da toplanan ve 2023’te yayımlanan uluslararası uzlaşıya göre sıkı dinlenme önerilmiyor; günlük işler ve yürüyüş ya da sabit bisiklet gibi hafif aerobik egzersiz iyileşmeye yardımcı olabilir, ekranı ilk 48 saatte sınırlamak da yararlı olabilir. Uzlaşı, baş dönmesi, boyun ağrısı ya da baş ağrısı 10 günden uzun sürenlere boyun ve denge rehabilitasyonu, belirtileri 4 haftayı aşanlara ise farklı uzmanlık alanlarından değerlendirme öneriyor.</p>
      <p class="soft">Bu önerilere dayanak olan çalışmalardan biri ABD’de 103 genç sporcuyla yapıldı: ilk 10 gün içinde, belirtileri artırmayan bir şiddette (koşu bandı testinde belirtilerin arttığı nabzın %80’i) günde yaklaşık 20 dakika aerobik egzersiz yapanlar ortalama 13 günde, yalnızca germe yapanlar 17 günde iyileşti. İyileşmesi 4 haftayı aşanlar egzersiz grubunda 52 kişiden 2, germe grubunda 51 kişiden 7’ydi; ancak bu fark istatistiksel olarak anlamlı değildi. Çalışmalar çoğunlukla genç sporcularda yapıldı; yetişkinlerde ve spor dışı yaralanmalarda kanıt daha sınırlı.</p>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Hafif hareket ve denge için altı egzersiz</h2>
      <p class="soft">Bu hareketler 2. ve 3. aşamada, dinlenme döneminden sonra başlanır. Baş hareketi ve denge egzersizleri bir çocuk hastanesinin beyin sarsıntısı sonrası denge bilgi notundan alındı. Her hareket belirtilerinizi en fazla hafifçe artırmalı; baş dönmesi sürüyorsa ya da düşme korkusu yaşıyorsanız bir fizyoterapist ya da hekimle değerlendirin.</p>
      {ex_grid(["bs_walk", "bs_gaze", "bs_nod", "bs_side", "bs_tandem", "bs_sls"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(BS_FAQ)}
      <p class="soft" style="margin-top:18px">Kafa darbesinden sonra boyun ağrısı için <a href="boyun-incinmesi.html">boyun incinmesi</a>, baş ağrısı için <a href="bas-agrisi.html">baş ağrısı</a>, başı çevirince başlayan kısa süreli dönme hissi için <a href="bas-donmesi.html">baş dönmesi (BPPV)</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Belirtileriniz kötüleşiyor ya da 2 hafta içinde düzelmiyorsa</li>
        <li>Araç kullanmaya, işe, okula ya da spora dönmenin güvenli olup olmadığından emin değilseniz</li>
        <li>Belirtileriniz 4 haftadan uzun sürüyorsa: değerlendirilene kadar spora dönmeyin</li>
        <li>Yukarıdaki acil belirtilerden herhangi biri sonradan ortaya çıkarsa hemen 112’yi arayın ya da acile gidin</li>
      </ul>
      {CTA_CARD("Beyin sarsıntısı sonrası boyun ve denge rehabilitasyonunuz", "beyin sarsıntısı sonrası boyun ve denge rehabilitasyonu")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(BS_SRC)}
    </div>
  </section>
</main>'''

page("beyin-sarsintisi.html", "Beyin Sarsıntısı (Konküzyon): İyileşme ve Harekete Dönüş",
     "Kafa darbesinden sonra beyin sarsıntısı: acil belirtiler, ilk 24–48 saatte yapılacaklar, okula, işe ve spora altı aşamada dönüş, denge egzersizleri ve araştırmaların söyledikleri.",
     "beyin-sarsintisi.html", NECK_CSS, BS_BODY, "",
     seo_title="Beyin Sarsıntısı (Konküzyon): Belirtiler, İyileşme ve Spora Dönüş | İhsan Eren",
     condition="Beyin sarsıntısı", faq_items=BS_FAQ)
