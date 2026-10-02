# -*- coding: utf-8 -*-
# Yeni hastalık rehberleri (4): dar kanal (lomber spinal stenoz).
# cond4_part.py'den sonra exec edilir.

# ---- yeni çizimler -----------------------------------------------------------------
# Topuklara oturarak öne uzanma: eller ve dizler üzerinden kalça topuklara doğru geri gider, bel yuvarlanır.
_CH_KT = "0;0.35;0.7;1"
SV["childp"] = fig(GRD +
    f'<path class="fig" d="M82 76 L82 108 L106 108">{anim_d("M82 76 L82 108 L106 108;M99 92 L82 108 L106 108;M99 92 L82 108 L106 108;M82 76 L82 108 L106 108", dur="5s", kt=_CH_KT)}</path>'
    f'<path class="fig" d="M32 76 L32 108">{anim_d("M32 76 L32 108;M52 99 L24 108;M52 99 L24 108;M32 76 L32 108", dur="5s", kt=_CH_KT)}</path>'
    f'<path class="fig hl" d="M32 76 Q57 70 82 76">{anim_d("M32 76 Q57 70 82 76;M52 99 Q76 87 99 92;M52 99 Q76 87 99 92;M32 76 Q57 70 82 76", dur="5s", kt=_CH_KT)}</path>'
    f'<g>{anim_t("0 0;20 24;20 24;0 0", dur="5s", kt=_CH_KT)}<path class="fig" d="M32 76 L25 75"/><circle class="hd" cx="20" cy="75" r="7"/></g>'
    '<g><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.35;0.7;1" dur="5s" repeatCount="indefinite"/>'
    '<path d="M70 62 H86 M82 58 L86 62 L82 66" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>',
    "Topuklara oturarak öne uzanma")

# Oturarak öne eğilme: gövde kalçadan öne eğilir, eller ayak bileklerine doğru iner.
_SF_KT = "0;0.35;0.7;1"
SV["sitflex"] = fig(GRD + CHAIR_L +
    '<path class="fig" d="M46 74 H80 V112"/>'
    f'<g>{anim_t("0 46 74;60 46 74;60 46 74;0 46 74", typ="rotate", dur="5s", kt=_SF_KT)}'
    '<path class="fig hl" d="M46 74 L48 42"/><circle class="hd" cx="50" cy="33" r="8"/></g>'
    f'<path class="fig" d="M48 48 L60 62 L72 66">{anim_d("M48 48 L60 62 L72 66;M68 62 L84 84 L90 104;M68 62 L84 84 L90 104;M48 48 L60 62 L72 66", dur="5s", kt=_SF_KT)}</path>',
    "Oturarak öne eğilme")

_ex2("ls_k2c", "k2c", "Dizi göğse çekme", "Sırtüstü yatın. Bir dizinizi iki elinizle tutup göğsünüze doğru yavaşça çekin; belinizin yere doğru düzleştiğini hissedin. Rahat yapabiliyorsanız iki dizinizi birlikte çekin. Beli öne eğen pozisyonlar dar kanalda genellikle rahatlatır.", "20–30 saniye tutun, 3–5 tekrar, günde 2 kez")
_ex2("ls_ptilt", "ptilt", "Pelvik eğme", "Sırtüstü yatın, dizleriniz bükülü, ayak tabanlarınız yerde olsun. Karın kaslarınızı sıkarak belinizdeki boşluğu yere doğru bastırın, 5 saniye tutup gevşeyin. Aynı hareketi ayakta, sırtınızı duvara yaslayarak da yapabilirsiniz.", "10 tekrar, günde 2 kez")
EXT["childp"] = ("Topuklara oturarak öne uzanma", "Ellerinizin ve dizlerinizin üzerinde durun. Ellerinizi yerinden oynatmadan kalçanızı yavaşça topuklarınıza doğru geriye götürün, belinizin yuvarlanıp gerildiğini hissedin. Dizleriniz izin vermiyorsa bu hareketi atlayıp sandalyede öne eğilmeyi yapın.", "20–30 saniye tutun, 3 tekrar")
EXT["sitflex"] = ("Oturarak öne eğilme", "Sağlam bir sandalyeye oturun, ayaklarınızı biraz açın. Ellerinizi bacaklarınızdan aşağı kaydırarak gövdenizi yavaşça öne eğin ve ayak bileklerinize doğru uzanın. Birkaç nefes bekleyip ellerinizden destek alarak doğrulun. Yürürken bacaklarınız ağrıdığında bir banka oturup bu hareketi yapabilirsiniz.", "10–15 saniye tutun, 5 tekrar")
_ex2("ls_bridge", "bridge", "Köprü", "Sırtüstü yatın, dizleriniz bükülü, ayaklarınız yerde. Önce belinizi yere bastırın, sonra kalçanızı sıkarak omuzlarınızdan dizlerinize düz bir çizgi oluşana kadar kaldırın. Belinizi çukurlaştırmayın; 3 saniye tutup yavaşça inin.", "10 tekrar, günde 1–2 kez")
_ex2("ls_walk", "walk", "Molalı yürüyüş", "Yürümeyi bırakmayın, bölün. Bacak şikâyetiniz başlamadan hemen önce oturup birkaç dakika dinlenin ya da öne eğilin, sonra devam edin. Süreyi haftadan haftaya azar azar artırın. Sabit bisiklet de iyi bir seçenektir; öne eğik oturulduğu için genellikle yürümekten daha rahat tolere edilir.", "Günde toplam 20–30 dakika, molalarla")

# ============================================================== DAR KANAL
LS_FAQ = [
 ("Dar kanal kendiliğinden geçer mi?", "Daralan kanal yeniden genişlemez; ancak şikâyetler çoğu kişide yıllar içinde kötüleşmez. Ameliyatsız izlenen hastaların yaklaşık üçte biri 3 yıl içinde düzeldiğini, yaklaşık yarısı şikâyetlerinin aynı kaldığını bildiriyor; %10–20'sinde şikâyetler artıyor."),
 ("MR'da dar kanal çıktı, ameliyat olmalı mıyım?", "Her zaman değil. 60 yaş üstündeki her beş kişiden birinde görüntülemede kanal daralması görülür ve bunların %80'inden fazlasında hiç şikâyet yoktur. Tedavi kararını MR değil, şikâyetleriniz ve günlük hayatınızın ne kadar kısıtlandığı belirler. Genellikle önce egzersiz, aktiviteyi ayarlama ve ağrı kontrolü denenir."),
 ("Yürüyünce ağrım artıyor; yürümeyi bırakmalı mıyım?", "Hayır. Yürümeyi bırakmak bacak kaslarını ve dayanıklılığı zayıflatır. Yürüyüşü kısa bölümlere ayırın, şikâyet başlamadan oturup dinlenin ve süreyi yavaş yavaş artırın. Sabit bisiklet gibi öne eğik yapılan aktiviteler genellikle daha rahat tolere edilir."),
 ("Bel fıtığından farkı nedir?", "Bel fıtığında bacak ağrısı çoğunlukla oturunca ve öne eğilince artar. Dar kanalda ise tam tersine ayakta durmak ve yürümek şikâyeti artırır, oturmak ve öne eğilmek rahatlatır. Dar kanal genellikle ileri yaşta görülür ve çoğu zaman iki bacağı birden etkiler."),
]

LS_SRC = [
 "Katz JN, Zimmerman ZE, Mass H, Makhni MC. " + ext("https://jamanetwork.com/journals/jama/article-abstract/2791689", "Diagnosis and management of lumbar spinal stenosis: a review") + ". JAMA. 2022;327(17):1688-1699.",
 "Schneider MJ, Ammendolia C, Murphy DR, et al. " + ext("https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2720073", "Comparative clinical effectiveness of nonsurgical treatment methods in patients with lumbar spinal stenosis: a randomized clinical trial") + ". JAMA Netw Open. 2019;2(1):e186828.",
 "Delitto A, Piva SR, Moore CG, et al. " + ext("https://www.acpjournals.org/doi/10.7326/M14-1420", "Surgery versus nonsurgical treatment of lumbar spinal stenosis: a randomized trial") + ". Ann Intern Med. 2015;162(7):465-473.",
 "Zaina F, Tomkins-Lane C, Carragee E, Negrini S. " + ext("https://www.cochrane.org/CD010264/BACK_surgical-versus-non-surgical-treatment-lumbar-spinal-stenosis", "Surgical versus non-surgical treatment for lumbar spinal stenosis") + ". Cochrane Database Syst Rev. 2016;(1):CD010264.",
 "Friedly JL, Comstock BA, Turner JA, et al. " + ext("https://www.nejm.org/doi/full/10.1056/NEJMoa1313265", "A randomized trial of epidural glucocorticoid injections for spinal stenosis") + ". N Engl J Med. 2014;371(1):11-21.",
]

LS_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Dar kanal (lomber spinal stenoz)</h1>
    <p class="lede">Dar kanal, belde sinirlerin geçtiği kanalın yaşla birlikte daralmasıdır. En tipik belirtisi, ayakta durunca ve yürüyünce kalçalara ve bacaklara yayılan, oturunca ya da öne eğilince hafifleyen ağrı ve uyuşmadır. Çoğu kişide şikâyetler yıllar içinde kötüleşmez; ilk tedavi egzersiz, aktiviteyi ayarlama ve ağrı kontrolüdür.</p>
    <p class="meta">Son güncelleme: 2 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>103 milyon</b><span>Dünyada dar kanal şikâyetleriyle yaşadığı tahmin edilen kişi sayısı</span></div>
        <div class="stat"><b>5'te 1</b><span>60 yaş üstünde görüntülemede kanal daralması görülenler; bunların %80'inden fazlasında şikâyet yok</span></div>
        <div class="stat"><b>3'te 1</b><span>Ameliyatsız izlenen hastalardan 3 yıl içinde düzeldiğini bildirenler; yaklaşık yarısında şikâyetler aynı kalıyor</span></div>
        <div class="stat"><b>%10–20</b><span>Aynı sürede bel ağrısı, bacak ağrısı ve yürümesi kötüleşenler</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Yaşla birlikte omurlar arasındaki diskler taşar, omurganın arkasındaki küçük eklemler büyür ve kanalın içindeki bağ kalınlaşır; bazen bir omur diğerinin üzerinde öne kayar. Bunların birleşimi, belde sinirlerin geçtiği kanalı daraltır.</p>
        <p class="soft">Ayakta dururken ve yürürken bel arkaya doğru çukurlaşır; bu duruşta şikâyetler artar. Oturunca ya da öne eğilince şikâyetler hafifler. Görüntülemedeki daralma ise her zaman şikâyete yol açmaz: 60 yaş üstündeki her beş kişiden birinde kanal daralması görülür ve bunların %80'inden fazlasında hiç şikâyet yoktur.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Ayakta durunca ya da yürüyünce kalçalarda ve bacaklarda ağrı, uyuşma ya da ağırlık hissi</li>
          <li>Oturunca ya da öne eğilince rahatlama</li>
          <li>Alışveriş arabasına yaslanarak yürürken daha rahat etme</li>
          <li>Yürüme mesafesinin kısalması, sık sık oturup dinlenme ihtiyacı</li>
          <li>Bel ağrısı (her hastada olmayabilir)</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Damar tıkanıklığından farkı</h2>
      <p class="soft">Bacak atardamarlarındaki daralma da yürürken bacak ağrısına yol açar. Ancak damar kaynaklı ağrı genellikle yalnızca ayakta durmakla artmaz; dar kanalda ise ayakta durmak bile şikâyeti başlatabilir ve rahatlamak için oturmak ya da öne eğilmek gerekir. İki durum birlikte de bulunabilir; ayırt etmek için hekim muayenesi gerekir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ameliyat mı, fizyoterapi mi?</h2>
      <p class="soft">2022'de JAMA dergisinde yayımlanan derlemeye göre ilk tedavi aktiviteyi ayarlama, ağrı kontrolü ve fizyoterapidir. ABD'de ortalama 72 yaşındaki 259 hastayla yapılan bir çalışmada, manuel terapiyle birlikte kişiye özel egzersiz programı 2. ayda şikâyetleri ve yürüme kapasitesini ilaç tedavisinden ve grup egzersizinden daha fazla iyileştirdi. 6. ayda gruplar arasında fark kalmadı; üç grupta da yürüme mesafesi başlangıca göre artmıştı.</p>
      <p class="soft">Ameliyat adayı 169 hastanın ameliyat (dekompresyon) ya da standart bir fizyoterapi programına ayrıldığı bir başka çalışmada, 2 yılın sonunda fiziksel işlev açısından iki grup arasında anlamlı fark bulunmadı; ancak fizyoterapi grubundaki hastaların önemli bir bölümü bu süre içinde ameliyat oldu. Beş çalışmayı (643 hasta) inceleyen Cochrane derlemesi, ameliyatın mı ameliyatsız tedavinin mi daha iyi olduğu konusunda kesin bir sonuca varılamayacağını belirtiyor; ameliyat edilenlerin %10–24'ünde komplikasyon görülürken ameliyatsız tedavilerde yan etki bildirilmedi.</p>
      <div class="callout">
        <p>Bu yüzden karar kişiye özeldir. Çoğu hastada önce düzenli bir egzersiz programı denenir. Buna rağmen ağrısı süren ve günlük hayatı belirgin şekilde kısıtlanan hastalarda ameliyat bir seçenektir ve omurga cerrahınca değerlendirilir. Bacaklarda ilerleyen güçsüzlük ya da idrar ve dışkı kontrolünde bozulma varsa beklenmez.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <ul class="tx">
        <li><b>Egzersiz</b><span>Beli öne eğen hareketler, karın ve kalça kaslarını güçlendirme ve yürüme dayanıklılığını artırma; program kişiye göre ayarlanır.</span></li>
        <li><b>Aktiviteyi ayarlama</b><span>Uzun süre ayakta durmayı ve yürümeyi bölün. Sabit bisiklet gibi öne eğik yapılan aktiviteler genellikle daha rahat tolere edilir.</span></li>
        <li><b>Manuel terapi</b><span>Egzersizle birlikte uygulandığında kısa vadede şikâyetleri azaltmaya ve yürümeyi artırmaya yardımcı olabilir.</span></li>
        <li><b>Ağrı kontrolü</b><span>Hekiminizin önerdiği ağrı kesiciler egzersize ve yürümeye devam etmeyi kolaylaştırır.</span></li>
        <li><b>Epidural kortizon iğnesi</b><span>400 hastalık bir çalışmada, lokal anestezik iğneye kortizon eklemek 6. haftada çok az fayda sağladı ya da hiç sağlamadı. Uzun vadeli faydası gösterilmemiştir; karar hekiminizle verilir.</span></li>
        <li><b>Ameliyat</b><span>Sinirlerin üzerindeki baskıyı kaldıran dekompresyon ameliyatı, ameliyatsız tedaviye rağmen şikâyetleri süren seçilmiş hastalarda değerlendirilir.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Dar kanal için altı egzersiz</h2>
      <p class="soft">Hareketleri yavaş ve ağrısız aralıkta yapın. Bacağa yayılan ağrı ya da uyuşma artıyorsa o hareketi bırakın. Beli arkaya doğru esneten hareketler şikâyetleri artırabilir.</p>
      {ex_grid(["ls_k2c", "ls_ptilt", "childp", "sitflex", "ls_bridge", "ls_walk"])}
      <div class="callout">
        <p>Kemik erimeniz ya da omurganızda çökme kırığı varsa öne eğilme hareketlerine başlamadan önce hekiminize ya da fizyoterapistinize danışın; program size göre uyarlanır.</p>
      </div>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Dar kanal için videolar</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("V4YDcYS3dyo", "Dar kanal egzersizleri videosunu oynat", "TOP 7 Exercises to STOP the Pain of Lumbar Stenosis (Back &amp; Leg)")}
          <h3>Dar kanal için yedi egzersiz</h3>
          <p>Bel ve bacak ağrısını hafifletmeye yönelik temel hareketler.</p>
        </div>
        <div class="vid">
          {vbox("623T_bNbyM0", "Dar kanal için germe hareketleri videosunu oynat", "Top 10 Stretches for Spinal Stenosis of the Low Back (Lumbar)")}
          <h3>Dar kanal için on germe hareketi</h3>
          <p>Yatarak, oturarak ve ayakta yapılabilen germe hareketleri.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(LS_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>İdrar yapamama ya da idrar ve dışkı kaçırma (acil)</li>
        <li>Makat, kasık ve genital bölgede his kaybı (acil)</li>
        <li>Bacaklarda hızla artan güçsüzlük</li>
        <li>Ateş, açıklanamayan kilo kaybı ya da kanser öyküsüyle birlikte bel ağrısı</li>
        <li>Düşme ya da darbeden sonra başlayan şiddetli bel ağrısı</li>
        <li>Dinlenirken de geçmeyen bacak ağrısı, ayakta soğukluk ya da renk değişikliği</li>
      </ul>
      {CTA_CARD("Dar kanal şikâyetiniz", "dar kanal (spinal stenoz)")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(LS_SRC)}
    </div>
  </section>
</main>'''

page("dar-kanal.html", "Dar Kanal (Lomber Spinal Stenoz)",
     "Belde dar kanal (spinal stenoz) nedir, neden yürüyünce bacaklar ağrır, MR'daki daralma ameliyat gerektirir mi? Fizyoterapinin yeri, evde altı egzersiz ve videolar.",
     "dar-kanal.html", NECK_CSS, LS_BODY, YT_JS,
     seo_title="Dar Kanal (Spinal Stenoz): Belirtiler, Tedavi ve Egzersizler | İhsan Eren",
     condition="Dar kanal (lomber spinal stenoz)", faq_items=LS_FAQ)
