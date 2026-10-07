# -*- coding: utf-8 -*-
# Yeni rehberler (18): sarkopeni (yaşa bağlı kas kaybı) ve demansta egzersiz.
# cond18_part.py'den sonra exec edilir. Videolar: Mayo Clinic, National Institute on Aging, NHS Greater Glasgow and Clyde (oEmbed ile doğrulandı).

# ---- yeni çizimler
# Duvar şınavı (yandan): ayaklar sabit, gövde duvara yaklaşır, dirsekler bükülür.
SV["sk_push"] = fig(GRD +
    '<path class="obj" d="M100 14 V112"/>'
    f'<path class="fig" d="M52 112 L60 72 L66 38">{anim_d("M52 112 L60 72 L66 38;M52 112 L66 73 L78 42;M52 112 L60 72 L66 38")}</path>'
    f'<path class="fig hl" d="M66 40 L82 43 L98 44">{anim_d("M66 40 L82 43 L98 44;M78 44 L86 58 L98 44;M66 40 L82 43 L98 44")}</path>'
    f'<g>{anim_t("0 0;12 4;0 0")}<circle class="hd" cx="68" cy="27" r="7"/></g>',
    "Duvar şınavı")
# Oturarak kol bükme: üst kol sabit, ön kol elde ağırlıkla omuza doğru bükülür.
SV["sk_curl"] = fig(GRD + CHAIR_L +
    '<path class="fig" d="M46 74 H80 V112"/>'
    '<path class="fig" d="M46 74 L48 42"/><circle class="hd" cx="50" cy="33" r="8"/>'
    '<path class="fig" d="M48 48 L52 66"/>'
    f'<g>{anim_t("25 52 66;-100 52 66;25 52 66", typ="rotate")}<path class="fig hl" d="M52 66 H70"/><circle cx="74" cy="66" r="5.5" fill="#C8963E"/></g>',
    "Kol bükme")
# Oturarak yerinde yürüyüş: bir diz kalkar, iner.
SV["dm_march"] = fig(GRD + CHAIR_L +
    '<path class="fig" d="M46 74 H80 V112"/>'
    '<path class="fig" d="M46 74 L48 42"/><circle class="hd" cx="50" cy="33" r="8"/>'
    '<path class="fig" d="M48 48 L56 62 L66 68"/>'
    f'<path class="fig hl" d="M46 74 L80 74 L80 112">{anim_d("M46 74 L80 74 L80 112;M46 74 L78 60 L82 96;M46 74 L80 74 L80 112", dur="2.4s")}</path>',
    "Oturarak yerinde yürüyüş")
# Oturarak topuk ve parmak ucu kaldırma: önce ayak ucu, sonra topuk kalkar.
SV["dm_toe"] = fig(GRD + CHAIR_L +
    '<path class="fig" d="M46 74 L48 42"/><circle class="hd" cx="50" cy="33" r="8"/>'
    '<path class="fig" d="M48 48 L56 62 L66 68"/>'
    f'<path class="fig" d="M46 74 L80 74 L80 108">{anim_d("M46 74 L80 74 L80 108;M46 74 L80 74 L80 108;M46 74 L80 74 L80 108;M46 74 L80 70 L80 101;M46 74 L80 74 L80 108", dur="5s", kt="0;0.25;0.5;0.75;1")}</path>'
    f'<path class="fig hl" d="M80 108 L96 110">{anim_d("M80 108 L96 110;M80 108 L94 99;M80 108 L96 110;M80 101 L96 110;M80 108 L96 110", dur="5s", kt="0;0.25;0.5;0.75;1")}</path>',
    "Topuk ve parmak ucu")
# Oturarak kolları yukarı kaldırma.
SV["dm_arm"] = fig(GRD + CHAIR_L +
    '<path class="fig" d="M46 74 H80 V112"/>'
    '<path class="fig" d="M46 74 L48 42"/><circle class="hd" cx="50" cy="33" r="8"/>'
    f'<path class="fig hl" d="M48 48 L58 62 L74 70">{anim_d("M48 48 L58 62 L74 70;M48 48 L56 30 L62 10;M48 48 L58 62 L74 70", dur="4s")}</path>',
    "Kolları yukarı kaldırma")

_ex2("sk_sts", "sts", "Sandalyeden kalkıp oturma", "Sağlam, kolsuz bir sandalyenin ön kısmına oturun; ayaklarınız kalça genişliğinde açık olsun. Hafifçe öne eğilin ve kollarınızı değil bacaklarınızı kullanarak yavaşça ayağa kalkın. Dik durun, sonra yavaşça oturun. Ne kadar yavaş yaparsanız o kadar iyi.", "5 tekrar; kolaylaştıkça artırın")
_ex2("sk_heel", "heel2", "Topuk yükseltme", "Bir sandalyenin arkalığına ya da tezgâha tutunun. İki topuğunuzu rahatça çıkabildiğiniz kadar yerden kaldırın, yavaş ve kontrollü inin. Kolaylaşınca tutunmadan deneyin.", "5 tekrar; kolaylaştıkça artırın")
_ex2("sk_sabd", "sabd", "Bacağı yana kaldırma", "Bir sandalyenin arkalığına ya da tezgâha tutunun. Bir bacağınızı rahatça gidebildiği kadar yana kaldırın; sırtınız ve kalçanız düz kalsın, gövdeniz yana eğilmesin. Yavaşça indirin, diğer bacakla tekrarlayın.", "Her bacakla 5 tekrar")
_ex2("sk_hext", "hext", "Bacağı arkaya kaldırma", "Bir sandalyenin arkalığına ya da tezgâha tutunup dik durun. Bir bacağınızı dizinizi bükmeden arkaya kaldırın; beliniz çukurlaşmasın. Uyluğunuzun arkasında ve kalçanızda çalışma hissedersiniz.", "Her bacakla 5 tekrar; yukarıda 5 saniyeye kadar tutun")
EXT["sk_push"] = ("Duvar şınavı", "Duvardan bir kol boyu uzakta durun. Ellerinizi göğüs hizasında, parmaklar yukarı bakacak şekilde duvara koyun. Sırtınız düz kalsın; dirseklerinizi gövdenize yakın tutarak yavaşça bükün ve duvara yaklaşın. Sonra yavaşça itin.", "5–10 tekrar, 3 set")
EXT["sk_curl"] = ("Kol bükme", "Elinize hafif bir ağırlık alın; dolu bir su şişesi yeterlidir. Kolunuz yanınızda dursun. Dirseğinizi yavaşça bükerek ağırlığı omzunuza getirin, yavaşça indirin. Ayakta ya da oturarak yapabilirsiniz.", "Her kolla 5 tekrar, 3 set")

EXT["dm_march"] = ("Oturarak yerinde yürüyüş", "Sağlam bir sandalyede dik oturun. Dizlerinizi sırayla, yürür gibi kaldırıp indirin; isterseniz kollarınızı da sallayın. Sevilen bir müzik eşliğinde yapmak hareketi kolaylaştırır.", "1–2 dakika; arada dinlenin")
EXT["dm_toe"] = ("Topuk ve parmak ucu kaldırma", "Otururken ayaklarınız yerde düz dursun. Önce ayak uçlarınızı kaldırın, topuklarınız yerde kalsın; sonra ayak uçlarınızı indirip topuklarınızı kaldırın.", "10 tekrar")
EXT["dm_arm"] = ("Kolları yukarı kaldırma", "Dik oturun. Kollarınızı yavaşça tavana doğru kaldırın, sonra indirin. Omzunuz ağrıyorsa yalnızca rahat ettiğiniz yere kadar kaldırın.", "8–10 tekrar")
_ex2("dm_kext", "kext", "Bacağı sırayla düzleştirme", "Sandalyede dik oturun. Bir dizinizi yavaşça düzleştirin, kısa bir an tutun ve indirin. Sonra diğer bacakla yapın.", "Her bacakla 8–10 tekrar")
_ex2("dm_sts", "sts", "Sandalyeden kalkıp oturma", "Sandalyenin ön kısmına oturun, hafifçe öne eğilin ve yavaşça ayağa kalkın; sonra yavaşça oturun. Gerekirse ellerinizden destek alın. Yanında biri bulunsun.", "5 tekrar")
_ex2("dm_walk", "walk", "Birlikte yürüyüş", "Bildiğiniz bir yolda, rahat bir tempoda yürüyün. Yürürken konuşabiliyor olmalısınız. Birlikte yürümek hem güvenlidir hem de sohbet için fırsattır.", "Her gün, kısa da olsa")

# ============================================================== SARKOPENİ
SK_FAQ = [
 ("Kaybedilen kas geri kazanılır mı?", "Yaşa bağlı kas kaybı tümüyle önlenemez; ancak yavaşlatılabilir ve kas gücü ileri yaşta da artırılabilir. 121 çalışmayı inceleyen Cochrane derlemesinde, kaslarını dirence karşı çalıştıran yaşlıların kas gücü belirgin biçimde arttı; sandalyeden kalkmaları hızlandı."),
 ("Yürüyüş yapıyorum; yeterli değil mi?", "Yürüyüş kalbiniz ve dayanıklılığınız için değerlidir, bırakmayın. Ancak sarkopenide önerilen egzersiz türü, kasları bir dirence karşı çalıştıran güçlendirme egzersizleridir: kendi vücut ağırlığınız, lastik bantlar ya da ağırlıklarla yapılan hareketler. İkisini birlikte yapın."),
 ("Protein tozu kullanmalı mıyım?", "En iyi kaynak besinlerdir: et, balık, yumurta, süt ürünleri, kuru baklagiller ve kuruyemişler. Proteini tek öğüne yığmak yerine güne yayın. Besinlerle yeterince alamıyorsanız takviye yardımcı olabilir; önce hekiminize danışın. Tek başına protein yetmez, egzersizle birlikte işe yarar. Böbrek hastalığınız ya da böbrek taşı öykünüz varsa proteini hekiminize danışmadan artırmayın."),
 ("İleri yaşta ağırlık çalışmak güvenli mi?", "Cochrane derlemesine göre dirençli egzersizde ciddi yan etkiler nadirdir; en sık bildirilen sorun kas ağrısıdır. Hafif başlayın, yavaş yavaş artırın. Kalp hastalığınız, kontrol altında olmayan tansiyonunuz ya da yeni bir ameliyatınız varsa başlamadan önce hekiminize danışın."),
]

SK_SRC = [
 "Liu CJ, Latham NK. " + ext("https://www.cochrane.org/evidence/CD002759_progressive-resistance-strength-training-improving-physical-function-older-adults", "Progressive resistance strength training for improving physical function in older adults") + ". Cochrane Database Syst Rev. 2009;(3):CD002759.",
 "Cruz-Jentoft AJ, et al. " + ext("https://pubmed.ncbi.nlm.nih.gov/30312372/", "Sarcopenia: revised European consensus on definition and diagnosis") + ". Age Ageing. 2019;48(1):16–31.",
 "Cleveland Clinic. " + ext("https://my.clevelandclinic.org/health/diseases/23167-sarcopenia", "Sarcopenia") + ". Last updated 2 April 2026.",
 "Restivo J. " + ext("https://www.health.harvard.edu/healthy-aging-and-longevity/muscle-loss-and-protein-needs-in-older-adults", "Muscle loss and protein needs in older adults") + ". Harvard Health Publishing. 14 August 2024.",
 "NHS. " + ext("https://www.nhs.uk/live-well/exercise/strength-exercises/", "Strength exercises") + ". Page last reviewed 28 February 2024.",
]

SK_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Sarkopeni: yaşa bağlı kas kaybı</h1>
    <p class="lede">Sarkopeni, yaş ilerledikçe kas kütlesinin, gücünün ve işlevinin azalmasıdır. Sandalyeden kalkmak, merdiven çıkmak, alışveriş torbası taşımak zorlaşır; düşme ve kırık riski artar. Onaylı bir ilacı yoktur; en etkili tedavi kasları dirence karşı çalıştıran egzersiz ve yeterli proteindir.</p>
    <p class="meta">Son güncelleme: 8 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%8</b><span>Her on yılda kaybedilebilen kas kütlesi (Cleveland Clinic)</span></div>
        <div class="stat"><b>2'de 1</b><span>80 yaşın üstündeki yetişkinlerin yaklaşık yarısı etkilenir (Harvard Health)</span></div>
        <div class="stat"><b>121 çalışma</b><span>Yaşlılarda dirençli egzersizi inceleyen Cochrane derlemesi; 6.700 katılımcı</span></div>
        <div class="stat"><b>Haftada 2–3</b><span>Çalışmaların çoğunda kullanılan egzersiz sıklığı</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Kas kaybı 30'lu–40'lı yaşlarda yavaş yavaş başlar, 65–80 yaş arasında hızlanır. Yaşla birlikte vücut proteini eskisi kadar iyi üretemez, hormonlar değişir, kas liflerinin sayısı ve boyutu azalır.</p>
        <p class="soft">Hareketsizlik bu süreci hızlandıran başlıca etkendir. Fazla ya da düşük kilo, kalp hastalığı, diyabet ve KOAH gibi süregelen hastalıklar, kemik erimesi ve kireçlenme, sigara ve alkol de riski artırır. Egzersiz yapmadan kilo vermek de kas kaybına yol açabilir.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Kas güçsüzlüğü (en sık belirti)</li>
          <li>Çabuk yorulma, dayanıklılığın azalması</li>
          <li>Günlük işleri yapmakta zorlanma</li>
          <li>Yavaş yürüme</li>
          <li>Merdiven çıkmakta güçlük</li>
          <li>Denge bozukluğu ve düşmeler</li>
          <li>Kasların gözle görülür biçimde incelmesi</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <p class="eyebrow">Kendinizi yoklayın</p>
      <h2>Beş soruluk tarama: SARC-F</h2>
      <p class="soft">Hekimlerin sarkopeni taramasında kullandığı kısa bir sorgulamadır. Her soruya 0, 1 ya da 2 puan verin ve toplayın.</p>
      <ul class="tx">
        <li><b>Güç</b><span>4,5 kiloluk bir yükü kaldırıp taşımakta ne kadar zorlanıyorsunuz? Hiç: 0 · Biraz: 1 · Çok ya da yapamıyorum: 2</span></li>
        <li><b>Yürüme</b><span>Odanın bir ucundan öbür ucuna yürümekte ne kadar zorlanıyorsunuz? Hiç: 0 · Biraz: 1 · Çok, yardımcı araçla ya da yapamıyorum: 2</span></li>
        <li><b>Sandalyeden kalkma</b><span>Sandalyeden ya da yataktan kalkmakta ne kadar zorlanıyorsunuz? Hiç: 0 · Biraz: 1 · Çok ya da yardımsız yapamıyorum: 2</span></li>
        <li><b>Merdiven</b><span>On basamak merdiven çıkmakta ne kadar zorlanıyorsunuz? Hiç: 0 · Biraz: 1 · Çok ya da yapamıyorum: 2</span></li>
        <li><b>Düşme</b><span>Son bir yılda kaç kez düştünüz? Hiç: 0 · 1–3 kez: 1 · 4 ya da daha fazla: 2</span></li>
      </ul>
      <div class="callout">
        <p><b>Toplam 4 ve üzeri</b> ise ayrıntılı değerlendirme için hekiminize başvurun. Bu sorgulama bir taramadır, tanı koymaz; düşük puan da sarkopeni olmadığını kesinleştirmez.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tanı nasıl konur?</h2>
      <p class="soft">Tek bir test yoktur. Avrupa uzlaşı raporuna göre değerlendirme kas gücüyle başlar: Kas gücü düşükse sarkopeniden şüphelenilir, kas kütlesinin de az olduğu gösterilirse tanı doğrulanır, fiziksel performans da düşükse sarkopeni ağır kabul edilir.</p>
      <ul class="tx">
        <li><b>El kavrama gücü</b><span>El dinamometresiyle ölçülür; kas gücünün basit bir göstergesidir.</span></li>
        <li><b>Sandalyeden kalkma testi</b><span>Kolları kullanmadan art arda kalkıp oturma süresi ölçülür.</span></li>
        <li><b>Yürüme hızı</b><span>Kısa bir mesafedeki olağan yürüme hızı ölçülür.</span></li>
        <li><b>Kalk ve yürü testi</b><span>Sandalyeden kalkıp birkaç metre yürüyüp geri dönme süresi ölçülür.</span></li>
        <li><b>Kas kütlesi ölçümü</b><span>DXA (kemik ölçümünde de kullanılan cihaz) ya da biyoelektrik empedans ile yapılır.</span></li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Kanıt ne diyor?</h2>
      <p class="soft">Yaşlılarda dirençli egzersizi inceleyen Cochrane derlemesi 121 çalışmayı ve 6.700 katılımcıyı kapsıyor. Çalışmaların çoğunda egzersiz haftada 2–3 kez, orta ya da yüksek şiddette yapılmış. Sonuçlar:</p>
      <ul class="dots">
        <li>Kas gücü belirgin biçimde artıyor.</li>
        <li>Sandalyeden kalkma hızlanıyor.</li>
        <li>Yürüme hızı az da olsa artıyor (saniyede 0,08 metre).</li>
        <li>Kireçlenmesi olanlarda ağrı azalıyor.</li>
        <li>Ciddi yan etkiler nadir; en sık bildirilen sorun kas ağrısı.</li>
      </ul>
      <div class="callout">
        <p>Bu derleme yalnızca sarkopeni tanısı konmuş kişileri değil, genel olarak yaşlı yetişkinleri kapsıyor. Yine de sarkopenide güçlendirme egzersizinin önerilmesinin dayanağı bu ve benzeri çalışmalardır.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne yapılabilir?</h2>
      <ul class="tx">
        <li><b>Dirençli egzersiz</b><span>Tedavinin temelidir. Vücut ağırlığı, lastik bant ya da ağırlıklarla, haftada en az iki gün yapılır ve zamanla zorlaştırılır.</span></li>
        <li><b>Protein</b><span>Cleveland Clinic her öğünde 20–35 gram protein hedeflemeyi öneriyor. Proteini tek öğüne yığmak yerine güne yayın.</span></li>
        <li><b>Besin kaynakları</b><span>Et, balık, yumurta, süt ürünleri, kuru baklagiller, kuruyemişler ve soya ürünleri.</span></li>
        <li><b>Böbrek uyarısı</b><span>Böbrek hastalığınız ya da böbrek taşı öykünüz varsa proteini hekiminize danışmadan artırmayın.</span></li>
        <li><b>İlaç</b><span>Sarkopeni için onaylı bir ilaç yoktur.</span></li>
        <li><b>Düzenli kontrol</b><span>Kilo kaybı, iştahsızlık ve düşmeler olursa hekiminize bildirin.</span></li>
      </ul>
      <div class="callout">
        <p>Kas güçsüzlüğü düşme ve kırık riskini artırır. <a href="dusme-onleme.html">Düşmeyi önleme</a> ve <a href="kemik-erimesi.html">kemik erimesi</a> rehberlerine de göz atın.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Kasları güçlendiren altı egzersiz</h2>
      <p class="soft">İngiltere Ulusal Sağlık Sistemi'nin (NHS), uzun süredir egzersiz yapmamış kişiler için önerdiği hareketlerdir. Haftada en az iki gün yapın. Tekerleksiz, sağlam bir sandalye kullanın; yavaş başlayın ve tekrar sayısını zamanla artırın.</p>
      {ex_grid(["sk_sts", "sk_heel", "sk_sabd", "sk_hext", "sk_push", "sk_curl"])}
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Sarkopeni için videolar</h2>
      <p class="soft">ABD'deki Mayo Clinic'in ve ABD Ulusal Yaşlanma Enstitüsü'nün (National Institute on Aging) YouTube kanallarından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("ymcFS1tQrsk", "Kas kaybı ve yaşlanma videosunu oynat", "Muscle Loss and Aging")}
          <h3>Kas kaybı ve yaşlanma</h3>
          <p>Yaşla birlikte görülen kas kaybını konu alan video.</p>
        </div>
        <div class="vid">
          {vbox("TOKxtgKrGCQ", "Alt beden güçlendirme videosunu oynat", "4 Lower Body Strength Exercises for Older Adults")}
          <h3>Alt beden için dört güçlendirme hareketi</h3>
          <p>Yaşlı yetişkinler için dört bacak güçlendirme egzersizi.</p>
        </div>
      </div>
      <p class="meta">Videolar Mayo Clinic ve National Institute on Aging kanallarına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(SK_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Yüzde, kolda ya da bacakta aniden başlayan güçsüzlük; konuşma bozukluğu (112)</li>
        <li>Günler ya da haftalar içinde hızla artan güçsüzlük</li>
        <li>İstemeden, açıklanamayan kilo kaybı</li>
        <li>Tekrarlayan düşmeler</li>
        <li>Egzersiz sırasında göğüs ağrısı, baş dönmesi ya da bayılma hissi</li>
      </ul>
      {CTA_CARD("Kas güçsüzlüğü, denge ve yürüme güçlükleriniz", "kas güçsüzlüğü (sarkopeni)")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(SK_SRC)}
    </div>
  </section>
</main>'''

page("sarkopeni.html", "Sarkopeni: Yaşa Bağlı Kas Kaybı",
     "Sarkopeni nedir, belirtileri nelerdir? Beş soruluk SARC-F taraması, tanı testleri, dirençli egzersiz için kanıt, protein önerileri ve evde altı güçlendirme egzersizi.",
     "sarkopeni.html", NECK_CSS, SK_BODY, YT_JS,
     seo_title="Sarkopeni (Yaşa Bağlı Kas Kaybı): Belirtiler, Egzersiz ve Protein | İhsan Eren",
     condition="Sarkopeni", faq_items=SK_FAQ)

# ============================================================== DEMANSTA EGZERSİZ
DM_FAQ = [
 ("Egzersiz demansı durdurur ya da yavaşlatır mı?", "Eldeki kanıtlara göre hayır: Egzersizin demansın ilerlemesini yavaşlattığı ya da durdurduğu gösterilmemiştir. Cochrane derlemesinde bellek ve düşünme üzerinde belirgin bir yarar bulunmadı. Buna karşın egzersiz günlük işleri yapabilme becerisini koruyabilir; gücü, dengeyi, uykuyu ve ruh hâlini destekler."),
 ("Ne kadar egzersiz yapılmalı?", "Hedef, yapabilenler için haftada toplam 150 dakika orta şiddette hareket ve haftada en az iki gün güç, denge ve esneklik çalışmasıdır. Bu bir zorunluluk değil, ulaşılabilirse iyi bir hedeftir. Az da olsa her hareket yararlıdır; kısa ve sık seanslar uzun tek bir seanstan daha kolay uygulanır."),
 ("Yakınım egzersiz yapmak istemiyor; ne yapabilirim?", "“Egzersiz” demek yerine sevdiği bir işi birlikte yapın: yürüyüş, bahçe işi, müzik eşliğinde dans. Geçmişte keyif aldığı uğraşlara dönün. Hedef ve sayı koymayın; düzenli ve keyifli olması yeterlidir. Televizyondaki reklam arasında ayağa kalkmak gibi küçük hareketler de sayılır."),
 ("Tek başına yürüyüşe çıkabilir mi?", "Hastalığın evresine bağlıdır. Tek başına çıkıyorsa bildiği yollarda yürümesi, yanında telefon ya da konum bildiren bir cihaz taşıması ve birine nereye gittiğini söylemesi önerilir. Üzerinde, yakınlarının telefon numarasının yazılı olduğu bir kimlik kartı bulunsun. Yolunu şaşırmaya başladıysa birlikte yürümek daha güvenlidir."),
]

DM_SRC = [
 "Forbes D, Forbes SC, Blake CM, Thiessen EJ, Forbes S. " + ext("https://www.cochrane.org/evidence/CD006489_exercise-programs-people-dementia", "Exercise programs for people with dementia") + ". Cochrane Database Syst Rev. 2015;(4):CD006489.",
 "World Health Organization. " + ext("https://www.who.int/news-room/fact-sheets/detail/dementia", "Dementia") + ". Fact sheet. 3 July 2026.",
 "Alzheimer's Society. " + ext("https://www.alzheimers.org.uk/get-support/daily-living/exercise", "Physical activity, movement and exercise for people with dementia") + ".",
 "Alzheimer's Society. " + ext("https://www.alzheimers.org.uk/get-support/living-with-dementia/exercise-types-ideas", "Exercise types and ideas for people with dementia") + ".",
 "Alzheimer's Society. " + ext("https://www.alzheimers.org.uk/get-support/daily-living/starting-exercise", "Getting started with exercise as a person with dementia") + ".",
]

DM_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Rehabilitasyon rehberi</p>
    <h1>Demansta egzersiz</h1>
    <p class="lede">Demans; belleği, düşünmeyi ve günlük işleri yapabilmeyi zamanla etkileyen hastalıkların ortak adıdır. Egzersiz demansı iyileştirmez ve ilerlemesini durdurmaz. Ancak günlük işleri yapabilme becerisini koruyabilir; gücü, dengeyi, uykuyu ve ruh hâlini destekler. Bu rehber hem demansla yaşayan kişiler hem de bakım veren yakınları içindir.</p>
    <p class="meta">Son güncelleme: 8 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>57 milyon</b><span>2021'de dünyada demansla yaşayan kişi sayısı (DSÖ)</span></div>
        <div class="stat"><b>%60–70</b><span>Demans olgularında Alzheimer hastalığının payı</span></div>
        <div class="stat"><b>17 çalışma</b><span>Demansta egzersizi inceleyen Cochrane derlemesi; 1.067 katılımcı</span></div>
        <div class="stat"><b>150 dakika</b><span>Yapabilenler için haftalık hareket hedefi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Demans nedir?</h2>
        <p class="soft">Demans tek bir hastalık değildir; beyni etkileyen çeşitli hastalıkların yol açtığı bir tablodur. En sık nedeni Alzheimer hastalığıdır. En güçlü risk etkeni yaştır, ancak demans yaşlanmanın olağan bir parçası değildir.</p>
        <p class="soft">Bugün için demansı iyileştiren bir tedavi yoktur. Dünya Sağlık Örgütü'ne göre ilaç dışı yaklaşımlar yaşam kalitesini artırabilir: rehabilitasyon, fiziksel aktivite, sosyal katılım, zihinsel uyarım ve bakım verenlerin desteklenmesi.</p>
      </div>
      <div>
        <h2>Erken belirtiler</h2>
        <ul class="dots">
          <li>Yakın zamanda olanları unutma, eşyaları kaybetme</li>
          <li>Bildik yerlerde bile yolunu şaşırma</li>
          <li>Zamanı karıştırma</li>
          <li>Karar vermede ve sorun çözmede zorlanma</li>
          <li>Konuşmaları izlemekte ya da sözcük bulmakta güçlük</li>
          <li>Alışılmış işleri yapmakta zorlanma</li>
          <li>Ruh hâlinde ve davranışta değişiklik; içe kapanma</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Egzersiz neye yarar, neye yaramaz?</h2>
      <p class="soft">Cochrane derlemesi 17 çalışmayı ve 1.067 katılımcıyı inceliyor. Sonuçlar ölçülü:</p>
      <ul class="tx">
        <li><b>Günlük işler</b><span>Egzersiz yapanlarda giyinme, yıkanma, yemek yeme gibi günlük işleri yapabilme becerisi daha iyi olabilir. Kanıtın kalitesi çok düşük; kesin konuşulamıyor.</span></li>
        <li><b>Bellek ve düşünme</b><span>Belirgin bir yarar gösterilemedi.</span></li>
        <li><b>Davranış ve depresyon</b><span>Davranış belirtileri ve depresyon üzerinde belirgin bir yarar gösterilemedi.</span></li>
        <li><b>Bakım veren</b><span>Tek bir çalışmada, evde egzersize bakım verenin eşlik etmesi bakım yükünü azalttı.</span></li>
        <li><b>Güvenlik</b><span>Çalışmalarda egzersizin zarar verdiğine dair bir bulgu yok.</span></li>
      </ul>
      <div class="callout">
        <p>Alzheimer's Society de aynı noktayı vurguluyor: Egzersizin, demans başladıktan sonra ilerlemeyi yavaşlattığı gösterilmemiştir. Yararı başka yerdedir: kalp ve damar sağlığı, günlük işler için güç, denge, daha iyi uyku, başkalarıyla vakit geçirme ve daha iyi bir ruh hâli.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Hangi hareketler uygun?</h2>
      <p class="soft">Uygun hareket, hastalığın evresine ve kişinin fiziksel durumuna göre değişir. Kişinin zaten sevdiği etkinlikleri, gerekirse uyarlayarak, olabildiğince sürdürmek en iyi başlangıçtır.</p>
      <ul class="tx">
        <li><b>Günlük işler</b><span>Ev işi, alışveriş, yavaşça ayağa kalkıp oturmak da harekettir.</span></li>
        <li><b>Yürüyüş</b><span>En kolay ulaşılan etkinliktir; birlikte yürümek sohbet için de fırsattır.</span></li>
        <li><b>Bahçe işleri</b><span>Orta şiddette bir etkinliktir; açık havada olmayı sağlar.</span></li>
        <li><b>Dans ve müzik</b><span>Sevilen müzik eşliğinde hareket; oturarak da yapılabilir.</span></li>
        <li><b>Oturarak egzersiz</b><span>Ayakta durmakta zorlananlar için uygundur. Lastik bant ya da hafif ağırlıkla zorlaştırılabilir.</span></li>
        <li><b>Tai chi, yoga, yüzme</b><span>Denge ve esneklik için seçeneklerdir; demans dostu gruplar tercih edilebilir.</span></li>
      </ul>
      <div class="callout">
        <p><b>Şiddeti konuşma testiyle ayarlayın:</b> Orta şiddette harekette nefesiniz hızlanır ve ısınırsınız; konuşabilir ama şarkı söyleyemezsiniz. Başlamadan önce ısının. Ağrı, baş dönmesi, nefes darlığı ya da kendini kötü hissetme olursa durun ve hekiminize danışın.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Bakım verenler için ipuçları</h2>
      <ul class="tx">
        <li><b>Birlikte yapın</b><span>Yanında biri olduğunda hareket hem daha güvenli hem daha keyiflidir.</span></li>
        <li><b>Rutine bağlayın</b><span>Her gün aynı saatte kısa bir yürüyüş, televizyondaki reklam arasında ayağa kalkmak gibi.</span></li>
        <li><b>Adımları gösterin</b><span>Hareketleri yazıp görünür bir yere asın; yapılan günleri takvimde işaretleyin.</span></li>
        <li><b>Hedef koymayın</b><span>Sayı ve süre yerine düzenli ve keyifli olmasına bakın.</span></li>
        <li><b>Güvenlik</b><span>Tek başına yürüyorsa bildiği yollar, yanında telefon ve üzerinde yakınlarının numarası bulunsun.</span></li>
        <li><b>Kendinize de bakın</b><span>Yardım isteyin, düzenli mola verin, kendi sağlığınızı ihmal etmeyin. Dünya Sağlık Örgütü'ne göre bakım verenler günde ortalama beş saatlerini bakıma ayırıyor.</span></li>
      </ul>
      <div class="callout">
        <p>Başlamadan önce hekiminize ya da fizyoterapistinize danışın; özellikle kalp hastalığı, yüksek tansiyon, baş dönmesi ya da bayılma, kemik ve eklem sorunları, nefes darlığı, denge sorunu ya da sık düşme varsa. Oturarak yapılan egzersizler bele yük bindirebilir; bunlar için de önce hekime danışılması önerilir.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Birlikte yapılabilecek altı hareket</h2>
      <p class="soft">İlk dördü oturarak yapılır ve Alzheimer's Society'nin önerdiği oturarak egzersizlerden seçilmiştir. Sağlam, tekerleksiz bir sandalye kullanın. Hareketi önce siz gösterin, sonra birlikte yapın; acele etmeyin.</p>
      {ex_grid(["dm_march", "dm_toe", "dm_arm", "dm_kext", "dm_sts", "dm_walk"])}
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Demans dostu egzersiz videoları</h2>
      <p class="soft">İskoçya'daki NHS Greater Glasgow and Clyde sağlık kurumunun YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("VhnkOhAWf-Q", "Güç ve denge egzersizleri videosunu oynat", "NHSGGC - Dementia Friendly Exercises for Strength and Balance")}
          <h3>Güç ve denge için</h3>
          <p>Demans dostu olarak hazırlanmış güç ve denge egzersizleri.</p>
        </div>
        <div class="vid">
          {vbox("YA5xvvoaVa8", "Güç ve esneklik egzersizleri videosunu oynat", "NHSGGC - Dementia Friendly Exercises for Strength and Flexibility")}
          <h3>Güç ve esneklik için</h3>
          <p>Demans dostu olarak hazırlanmış güç ve esneklik egzersizleri.</p>
        </div>
      </div>
      <p class="meta">Videolar NHS Greater Glasgow and Clyde kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(DM_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden yardım alın:</p>
      <ul class="dots redflags">
        <li>Saatler ya da günler içinde aniden artan şaşkınlık, uykuya eğilim ya da huzursuzluk</li>
        <li>Yüzde, kolda ya da bacakta aniden başlayan güçsüzlük; konuşma bozukluğu (112)</li>
        <li>Düşme sonrası baş çarpması, şiddetli ağrı ya da üzerine basamama</li>
        <li>Egzersiz sırasında göğüs ağrısı, baş dönmesi ya da nefes darlığı</li>
        <li>Yürümede ve dengede kısa sürede belirgin bozulma, sık düşme</li>
      </ul>
      {CTA_CARD("Demansla yaşayan yakınınızın hareket, denge ve yürüme güçlükleri", "demansla yaşayan yakınım")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(DM_SRC)}
    </div>
  </section>
</main>'''

page("demans-egzersiz.html", "Demansta Egzersiz",
     "Egzersiz demansta neye yarar, neye yaramaz? Cochrane kanıtı, uygun etkinlikler, bakım verenler için ipuçları, güvenlik ve birlikte yapılabilecek altı hareket.",
     "demans-egzersiz.html", NECK_CSS, DM_BODY, YT_JS,
     seo_title="Demansta Egzersiz: Kanıt, Güvenli Hareketler ve Bakım Verenler İçin İpuçları | İhsan Eren",
     condition="Demans", faq_items=DM_FAQ)
