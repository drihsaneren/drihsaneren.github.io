# -*- coding: utf-8 -*-
# Yeni rehber (55): Kaburga kırığı ve morarması. cond54_part.py'den sonra exec edilir. Video yok.
# NHS (Broken or bruised ribs, 10 Ocak 2024) ve Worcestershire Acute NHS (rib fractures, sürüm 2.1) broşürüne göre.

# Oturarak derin nefes: eller alt kaburgalarda, göğüs kafesi genişler
SV["kb_breath"] = fig(GRD + CHAIR_L +
    '<path class="fig" d="M46 74 H80 V112"/>'
    '<path class="fig" d="M46 74 L48 42"/><circle class="hd" cx="50" cy="33" r="8"/>'
    f'<ellipse cx="48" cy="58" rx="9" ry="12" fill="none" stroke="#C8963E" stroke-width="3">'
    f'<animate attributeName="rx" values="7;12;12;7" keyTimes="0;0.4;0.6;1" dur="5s" repeatCount="indefinite"/></ellipse>'
    '<path class="fig" d="M48 48 L60 58 L54 64"/>',
    "Derin nefes")
# Yastıkla destekli öksürük: yastık göğse bastırılır
SV["kb_cough"] = fig(GRD + CHAIR_L +
    '<path class="fig" d="M46 74 H80 V112"/>'
    '<path class="fig" d="M46 74 L48 42"/><circle class="hd" cx="50" cy="33" r="8"/>'
    '<rect x="50" y="48" width="14" height="22" rx="6" fill="#C8963E"/>'
    '<path class="fig" d="M48 48 L66 54 L60 64"/>'
    '<g fill="none" stroke="#C8963E" stroke-width="2.5" stroke-linecap="round"><animate attributeName="opacity" values="0;0;1;0" keyTimes="0;0.45;0.55;1" dur="3.2s" repeatCount="indefinite"/>'
    '<path d="M62 30 H72 M62 26 L71 21 M62 35 L71 39"/></g>',
    "Destekli öksürük")

_ex2("kb_deep", "kb_breath", "Yavaş ve derin nefes", "Dik oturun, ellerinizi alt kaburgalarınıza koyun. Burnunuzdan kaburgalarınızın yanlara genişlediğini hissedecek kadar derin nefes alın, 2–3 saniye tutun ve yavaşça verin. Ağrı kesicinin etkili olduğu saatlere denk getirin.", "4 tekrar, günde en az 4 kez")
_ex2("kb_sup", "kb_cough", "Yastıkla destekli öksürük", "Öksürmeniz gerektiğinde kırık bölgenin üzerine bir yastık ya da katlanmış bir havlu bastırın ve öyle öksürün. Balgamı tutmayın: öksürmek göğüs enfeksiyonunu önlemeye yardım eder.", "Her öksürmeniz gerektiğinde")
_ex2("kb_shrug", "ly_shrug", "Omuzları hareket ettirme", "Gün içinde ara sıra omuzlarınızı yavaşça yukarı kaldırıp indirin ve geriye doğru çevirin. Omuz ve sırtınızın tutulmasını önler; ağrıya doğru zorlamayın.", "Gün içinde ara sıra, birkaç tekrar")
_ex2("kb_walk", "walk", "Kısa ve sık yürüyüş", "Uzun süre yatmayın ve hareketsiz kalmayın. Evde ya da dışarıda az az ve sık yürüyün; kendinizi zorlamadan süreyi kademeli artırın.", "Gün içinde sık sık")

KB_FAQ = [
 ("Röntgen çekilmesi gerekir mi?", "Çoğu zaman gerekmez. Kaburgalar diğer kemikler gibi alçıya alınamaz ya da sarılamaz; kırık da olsa morarma da olsa genellikle kendiliğinden iyileşir. Hekiminiz akciğer ya da başka bir organın etkilendiğinden şüphelenirse görüntüleme isteyebilir."),
 ("Neden nefes egzersizleri bu kadar önemli?", "Ağrı, derin nefes almanızı ve öksürmenizi engelleyebilir. Akciğerleriniz tam havalanmaz ve balgam birikirse göğüs enfeksiyonu riski artar. Düzenli derin nefes, gerektiğinde öksürme ve hareketli kalmak bunu önlemeye yardım eder."),
 ("Ne zaman işe ve spora dönerim?", "Gerekirse işe ara verip dinlenin. Bir NHS broşürüne göre ağır yük kaldırma ve bedensel işlerden en az 4 hafta, temas sporlarından en az 6 hafta uzak durun. Ağrınızı artıran spor ve egzersizleri yapmayın."),
 ("İyileşme ne kadar sürer?", "Kaburga kırığı ya da morarması genellikle 2–6 haftada iyileşir; kırıklar için bu süre çoğunlukla 4–6 haftadır. Bu süreden sonra da bir süre hafif bir sızı kalabilir. Ağrınız birkaç hafta içinde azalmıyorsa hekiminize başvurun."),
 ("Kimler daha dikkatli olmalı?", "Göğüs duvarı yaralanmalarını inceleyen sistematik derlemelere göre 65 yaş ve üstü olmak, üç ya da daha fazla kaburganın kırılması ve önceden var olan bir hastalık, özellikle kalp ya da akciğer hastalığı, ciddi sonuç riskini yaklaşık iki kat artırıyor; sonradan gelişen zatürre de riski belirgin şekilde yükseltiyor. Bu gruptaysanız hekiminizle bir takip planı konuşabilir; ateş, renkli balgam ya da artan nefes darlığında beklemeden başvurabilirsiniz."),
 ("Sigara içiyorum, önemli mi?", "Evet. Sigara göğüs enfeksiyonu riskini artırır; iyileşme döneminde içmeyin. Bırakmak için hekiminizden destek isteyebilirsiniz."),
]

KB_SRC = [
 "NHS. " + ext("https://www.nhs.uk/conditions/rib-injuries", "Broken or bruised ribs") + ". Page last reviewed: 10 January 2024.",
 "Worcestershire Acute Hospitals NHS Trust. " + ext("https://www.worcsacute.nhs.uk/leaflets/physiotherapy-advice-and-exercises-following-rib-fractures/", "Physiotherapy advice and exercises following rib fractures") + ". Version 2.1.",
 "Battle CE, Hutchings H, Evans PA. " + ext("https://doi.org/10.1016/j.injury.2011.01.004", "Risk factors that predict mortality in patients with blunt chest wall trauma: a systematic review and meta-analysis") + ". Injury. 2012;43(1):8–17.",
 "Battle C, Carter K, Newey L, Giamello JD, Melchio R, Hutchings H. " + ext("https://emj.bmj.com/content/40/5/369", "Risk factors that predict mortality in patients with blunt chest wall trauma: an updated systematic review and meta-analysis") + ". Emerg Med J. 2023;40(5):369.",
]

KB_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Kaburga kırığı ve morarması</h1>
    <p class="lede">Bir düşme, göğse alınan bir darbe ya da çok şiddetli öksürük kaburgaları kırabilir ya da morartabilir. Nefes alırken ve öksürürken ağrı çok rahatsız edici olabilir, ama kaburgalar çoğu zaman kendiliğinden iyileşir. Bu dönemde en önemli iş, ağrıya rağmen derin nefes almayı ve hareket etmeyi sürdürmektir: böylece göğüs enfeksiyonunun önüne geçilir.</p>
    <p class="meta">Son güncelleme: 19 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>2–6 hafta</b><span>Kaburga kırığı ya da morarmasının genellikle iyileştiği süre</span></div>
        <div class="stat"><b>Günde 4 kez</b><span>Nefes egzersizlerini en az bu sıklıkla yapın</span></div>
        <div class="stat"><b>4 hafta</b><span>Ağır yük kaldırmaktan ve bedensel işten uzak durma süresi</span></div>
        <div class="stat"><b>6 hafta</b><span>Temas sporlarına ara verme süresi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Özellikle nefes alırken ya da öksürürken şiddetli göğüs ağrısı.</li>
          <li>Kaburgaların üzerinde şişlik ya da hassasiyet.</li>
          <li>Bazen deride morluk.</li>
          <li>Kaburga kırıldıysa bir çatırtı hissetmek ya da duymak.</li>
        </ul>
      </div>
      <div>
        <h2>Neler iyi gelir?</h2>
        <ul class="dots">
          <li>Hekiminize ya da eczacınıza danışarak düzenli ağrı kesici kullanın; ağrı kontrol altındayken nefes almak ve hareket etmek kolaylaşır.</li>
          <li>İlk günlerde havluya sarılı buzu ya da donmuş bezelye paketini düzenli olarak kaburgalarınıza tutun.</li>
          <li>Normal nefes alın ve öksürmeniz gerektiğinde öksürün; göğsünüze bir yastık bastırın.</li>
          <li>İlk birkaç gece biraz daha dik uyuyun.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Aktif nefes döngüsü</h2>
      <p class="soft">Bir NHS broşürünün önerdiği bu döngüyü günde en az 4 kez, balgam çıkarmakta zorlanıyorsanız daha sık yapın. En iyisi oturarak yapmaktır; göğsünüze katlanmış bir havlu ya da yastık tutabilirsiniz.</p>
      <ol class="steps">
        <li><span><strong>Rahat nefes:</strong> Bir elinizi karnınıza koyun, sakinleşene kadar burnunuzdan yavaşça nefes alıp verin.</span></li>
        <li><span><strong>Derin nefes:</strong> Kaburgalarınızın yanlara genişlediğini hissedecek kadar derin nefes alın, 2–3 saniye tutun, yavaşça verin. 4 kez tekrarlayın.</span></li>
        <li><span><strong>Yeniden rahat nefes.</strong></span></li>
        <li><span><strong>Hırıltılı nefes verme:</strong> Ağzınız açık, aynayı buğulandırır gibi uzun ve sürekli nefes verin. Balgam yukarı geldiğinde derin bir nefes alıp kısa ve hızlı bir nefes verin.</span></li>
        <li><span><strong>Yeniden rahat nefes.</strong></span></li>
        <li><span><strong>Destekli öksürük:</strong> Balgam varsa kırık bölgeye yastık bastırarak öksürün.</span></li>
      </ol>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Akciğerleri ve gövdeyi hareketli tutan dört egzersiz</h2>
      <p class="soft">Uzun süre yatmak ya da hareketsiz kalmak iyileşmeyi zorlaştırır. Zorlanmayın, ağır yük kaldırmayın ve ağrınızı artıran hareketlerden kaçının.</p>
      {ex_grid(["kb_deep", "kb_sup", "kb_shrug", "kb_walk"], "ex four")}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(KB_FAQ)}
      <p class="soft" style="margin-top:18px">Sırtın üst kısmındaki ağrılar için <a href="kurek-kemigi-arasi-agri.html">kürek kemiği arası ağrı</a>, kemikleri güçlendirmek için <a href="kemik-erimesi.html">kemik erimesi</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman acile ya da hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Yaralanma araba kazası gibi ciddi bir kazada olduysa</li>
        <li>Nefes darlığınız ya da göğüs ağrınız giderek artıyorsa</li>
        <li>Karnınızda ya da omzunuzda ağrı varsa</li>
        <li>Kanlı öksürüyorsanız</li>
        <li>Sarı ya da yeşil balgam çıkarıyorsanız, yüksek ateşiniz varsa ya da üşüyüp titriyorsanız</li>
        <li>Ağrınız birkaç hafta içinde azalmadıysa</li>
      </ul>
      <p class="soft">İlk dört durumda hemen 112’yi arayın ya da acil servise başvurun; kırık bir kaburga akciğere, karaciğere ya da dalağa zarar vermiş olabilir. Kendiniz araç kullanarak gitmeyin. Son iki durumda kısa sürede hekiminize başvurun.</p>
      {CTA_CARD("Kaburga kırığı sonrası nefes ve hareket", "kaburga kırığı sonrası nefes egzersizleri ve rehabilitasyon")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(KB_SRC)}
    </div>
  </section>
</main>'''

page("kaburga-kirigi.html", "Kaburga Kırığı ve Morarması",
     "Kaburga kırığı ya da morarması ne kadar sürede iyileşir, ağrı varken nasıl nefes alınır ve öksürülür? Aktif nefes döngüsü, dört egzersiz ve acil uyarı işaretleri.",
     "kaburga-kirigi.html", NECK_CSS, KB_BODY, "",
     seo_title="Kaburga Kırığı ve Morarması: İyileşme Süresi, Nefes Egzersizleri | İhsan Eren",
     condition="Kaburga kırığı", faq_items=KB_FAQ)
