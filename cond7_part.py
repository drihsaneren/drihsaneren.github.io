# -*- coding: utf-8 -*-
# Yeni hastalık rehberleri (6): ön çapraz bağ yaralanması.
# cond6_part.py'den sonra exec edilir. Videolar: Bob & Brad (kimlikler oEmbed ile doğrulandı).

_ex2("acl_hslide", "hslide", "Topuk kaydırma", "Sırtüstü yatın. Topuğunuzu yatağın üzerinde kaydırarak kalçanıza doğru çekin ve dizinizi rahat ettiğiniz kadar bükün, sonra yavaşça düzeltin. Topuğun altına poşet koymak kaymayı kolaylaştırır. Amaç dizi her gün biraz daha rahat büküp tam açabilmektir.", "10 tekrar, günde 3 kez")

# ============================================================== ÖN ÇAPRAZ BAĞ
ACL_FAQ = [
 ("Ön çapraz bağ kendiliğinden iyileşir mi?", "Tam yırtılan bağın eski sağlamlığına kendiliğinden kavuşması genellikle beklenmez. Ancak güçlü uyluk ve kalça kasları ve iyi bir denge kontrolüyle diz, pek çok kişide bağ olmadan da sorunsuz çalışabilir. Çalışmalarda rehabilitasyonla başlayanların yaklaşık yarısı ameliyata gerek duymadı."),
 ("Ameliyat olmadan spor yapabilir miyim?", "Düz koşu, bisiklet ve yüzme gibi dönme içermeyen sporları pek çok kişi ameliyatsız sürdürebilir. Futbol, basketbol ya da kayak gibi ani dönüş ve sıçrama içeren sporlarda dizin boşalma riski daha yüksektir; bu sporlara dönmek isteyenlerde ameliyat daha sık önerilir. Diziniz boşalıyorsa o aktiviteyi bırakıp hekiminize danışın."),
 ("Ameliyattan sonra spora ne zaman dönebilirim?", "Çoğu program en az 9 ayı hedefler. Bir çalışmada, ilk 9 ay içinde spora dönüş her ay ertelendiğinde yeniden yaralanma oranı %51 azaldı. Süre kadar ölçüm de önemlidir: kas gücü ve sıçrama testlerinde sağlam bacağınıza yaklaşmış olmanız gerekir."),
 ("Herkes eski spor düzeyine dönebiliyor mu?", "Hayır. 69 çalışmayı (7.556 kişi) birleştiren derlemede ameliyat olanların %81'i bir spora, %65'i yaralanma öncesindeki düzeyine, %55'i yarışma düzeyinde spora döndü. Genç yaş, sıçrama testlerinde iki bacağın dengeli olması ve dönüşe psikolojik olarak hazır hissetmek bu olasılığı artırıyor."),
]

ACL_SRC = [
 "Frobell RB, Roos HP, Roos EM, Roemer FW, Ranstam J, Lohmander LS. " + ext("https://www.bmj.com/content/346/bmj.f232", "Treatment for acute anterior cruciate ligament tear: five year outcome of randomised trial") + ". BMJ. 2013;346:f232.",
 "Reijman M, Eggerding V, van Es E, et al. " + ext("https://www.bmj.com/content/372/bmj.n375", "Early surgical reconstruction versus rehabilitation with elective delayed reconstruction for patients with anterior cruciate ligament rupture: COMPARE randomised controlled trial") + ". BMJ. 2021;372:n375.",
 "Beard DJ, Davies L, Cook JA, et al. " + ext("https://search.pedro.org.au/search-results/record-detail/71720", "Rehabilitation versus surgical reconstruction for non-acute anterior cruciate ligament injury (ACL SNNAP): a pragmatic randomised controlled trial") + ". Lancet. 2022;400(10352):605-615.",
 "Grindem H, Snyder-Mackler L, Moksnes H, Engebretsen L, Risberg MA. " + ext("https://bjsm.bmj.com/content/50/13/804", "Simple decision rules can reduce reinjury risk by 84% after ACL reconstruction: the Delaware-Oslo ACL cohort study") + ". Br J Sports Med. 2016;50(13):804-808.",
 "Ardern CL, Taylor NF, Feller JA, Webster KE. " + ext("https://bjsm.bmj.com/content/48/21/1543", "Fifty-five per cent return to competitive sport following anterior cruciate ligament reconstruction surgery: an updated systematic review and meta-analysis including aspects of physical functioning and contextual factors") + ". Br J Sports Med. 2014;48(21):1543-1552.",
 "Webster KE, Hewett TE. " + ext("https://lida.sport-iat.de/ta/Record/4054906", "Meta-analysis of meta-analyses of anterior cruciate ligament injury reduction training programs") + ". J Orthop Res. 2018;36(10):2696-2708.",
]

ACL_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Ön çapraz bağ yaralanması</h1>
    <p class="lede">Ön çapraz bağ, dizin ortasında uyluk kemiğini kaval kemiğine bağlayan ve dönme hareketlerinde dizin boşalmasını önleyen bağdır. Çoğunlukla sporda ani duruş, yön değiştirme ya da sıçrayıp yere inme sırasında yırtılır. Her yırtık ameliyat gerektirmez: iki çalışmada, önce rehabilitasyonla başlayan hastaların yaklaşık yarısı ameliyata gerek duymadı.</p>
    <p class="meta">Son güncelleme: 7 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>2'de 1</b><span>Önce rehabilitasyonla başlayan genç ve aktif yetişkinlerden 5 yıl içinde ameliyata gerek duymayanlar</span></div>
        <div class="stat"><b>9 ay</b><span>Ameliyattan sonra spora dönüş için çoğu programın hedeflediği en kısa süre</span></div>
        <div class="stat"><b>%65</b><span>Ameliyattan sonra yaralanma öncesindeki spor düzeyine dönenler (69 çalışma, 7.556 kişi)</span></div>
        <div class="stat"><b>%50</b><span>Isınmaya eklenen önleme egzersizleriyle ön çapraz bağ yaralanmalarındaki azalma</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Dizin içinde çapraz duran iki bağdan öndeki olan ön çapraz bağ, kaval kemiğinin öne kaymasını ve diz dönerken boşalmasını engeller. Yaralanmaların çoğu kimseyle çarpışmadan olur: koşarken aniden durmak, ayak yerdeyken gövdeyi döndürmek ya da sıçrayıp diz içe çökerek yere inmek.</p>
        <p class="soft">Bağ kısmen ya da tamamen yırtılabilir; menisküs ve diğer bağlar da birlikte zarar görebilir. Tanı muayeneyle konur; MR eşlik eden yaralanmaları gösterir.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Yaralanma anında dizde “pat” sesi ya da kopma hissi</li>
          <li>İlk birkaç saat içinde gelişen şişlik</li>
          <li>Üzerine basarken dizde güvensizlik ve boşalma hissi</li>
          <li>Dizi tam açamama ya da bükememe</li>
          <li>Yön değiştirirken ya da merdiven inerken dizin “kaçması”</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ameliyat mı, rehabilitasyon mu?</h2>
      <p class="soft">Yaş ortalaması 26 olan 121 genç ve aktif yetişkinle yapılan bir çalışmada hastaların yarısı rehabilitasyonla birlikte erken ameliyat oldu; diğer yarısı rehabilitasyonla başladı ve yalnızca gerek görülürse sonradan ameliyat edildi. Beş yıl sonra diz şikâyetleri ve işlevi açısından iki grup arasında fark yoktu; rehabilitasyonla başlayanların %51'i bu sürede ameliyat olmuştu. 167 hastalık benzer bir çalışmada erken ameliyat olanların 2. yıldaki diz puanı biraz daha yüksekti (84,7'ye karşı 79,4), ancak araştırmacılar bu farkı klinik açıdan önemli bulmadı; rehabilitasyonla başlayanların yarısı ameliyat olmadı.</p>
      <p class="soft">Yaralanmanın üzerinden zaman geçmiş ve dizi hâlâ boşalan hastalarda tablo farklı. 316 hastayla yapılan bir çalışmada ameliyat, 18. ayda rehabilitasyondan daha iyi sonuç verdi (diz puanı 73,0'a karşı 64,6); rehabilitasyon grubundakilerin %41'i sonradan ameliyat oldu.</p>
      <div class="callout">
        <p>Bu yüzden karar kişiye özeldir. Yaralanmadan hemen sonra kimin ameliyatsız iyi olacağını kesin söylemek mümkün değildir; birkaç aylık iyi bir rehabilitasyon bunu gösterir. Dönme ve sıçrama içeren sporlara dönmek isteyenlerde, rehabilitasyona rağmen dizi boşalmaya devam edenlerde ve menisküs gibi eşlik eden yaralanması olanlarda ameliyat daha sık önerilir. Kararı ortopedi hekiminizle birlikte verin.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <ul class="tx">
        <li><b>İlk günler</b><span>Şişliği azaltmak için dizinizi dinlendirin, yükseğe alın ve soğuk uygulayın. Hekiminizin izin verdiği ölçüde üzerine basın; dizi uzun süre hareketsiz bırakmak sertliğe ve kas kaybına yol açar.</span></li>
        <li><b>Rehabilitasyon</b><span>Önce şişliği gidermek ve dizi tam açabilmek; sonra uyluk ve kalça kaslarını güçlendirmek, dengeyi ve sıçrayıp yere inme tekniğini çalışmak. Aylar süren, aşama aşama ilerleyen bir programdır.</span></li>
        <li><b>Ameliyat öncesi hazırlık</b><span>Ameliyat kararı verilse bile genellikle önce şişliğin inmesi, dizin tam açılması ve uyluk kasının güçlenmesi beklenir.</span></li>
        <li><b>Ameliyat</b><span>Yırtık bağ çoğunlukla dikilmez; yerine hastanın kendi tendonundan alınan bir parça yerleştirilir. Ameliyat rehabilitasyonun yerini tutmaz; sonrasında da aylar süren bir program gerekir.</span></li>
        <li><b>Spora dönüş</b><span>Takvime göre değil, ölçüme göre karar verilir. Bir çalışmada kas gücü ve sıçrama testlerini de içeren ölçütleri geçemeden spora dönenlerin %38'i dizini yeniden yaraladı; ölçütleri geçenlerde bu oran %5,6 idi.</span></li>
        <li><b>Önleme</b><span>Isınmaya eklenen denge, güç ve yere inme tekniği egzersizleri, sekiz meta-analizin ortak sonucuna göre ön çapraz bağ yaralanmalarını yaklaşık yarı yarıya azaltıyor. Verilerin çoğu kadın sporculardan geliyor.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Ön çapraz bağ yaralanmasında altı egzersiz</h2>
      <p class="soft">Bu hareketler yaralanmadan sonraki ilk dönem ve ameliyat öncesi hazırlık içindir. Ameliyat olduysanız cerrahınızın ve fizyoterapistinizin verdiği programa uyun. Hareket sırasında diziniz boşalıyor, kilitleniyor ya da şişlik artıyorsa durun.</p>
      {ex_grid(["mn_quad", "acl_hslide", "mn_slr", "mn_bridge", "mn_wall", "mn_sls"])}
      <div class="callout">
        <p>Koşu, sıçrama ve yön değiştirme çalışmalarına fizyoterapistiniz diz gücünüzü ve dengenizi ölçtükten sonra, onun gözetiminde geçin.</p>
      </div>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Ön çapraz bağ için videolar</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("_gF6llBpol0", "Ön çapraz bağ yaralanması videosunu oynat", "ACL (Knee) Injury as explained by Physical Therapy")}
          <h3>Ön çapraz bağ yaralanması</h3>
          <p>İki fizyoterapist yaralanmayı ve tedavi seçeneklerini anlatıyor.</p>
        </div>
        <div class="vid">
          {vbox("m-G-r_MgL_4", "Ameliyat sonrası diz hareket açıklığı egzersizleri videosunu oynat", "Top 3 ACL Range of Motion Exercises &amp; Stretches After Surgery")}
          <h3>Ameliyat sonrası üç hareket açıklığı egzersizi</h3>
          <p>Dizi yeniden tam açıp bükebilmek için hareketler.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(ACL_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Yaralanmadan sonra dizin üzerine hiç basamama</li>
        <li>Dizde belirgin şekil bozukluğu</li>
        <li>Dizin kilitlenip açılmaması</li>
        <li>Ayakta ya da bacakta uyuşma, soğukluk ya da renk değişikliği (acil)</li>
        <li>Baldırda şişlik, ağrı ve kızarıklık</li>
        <li>Ameliyattan sonra ateş, yarada akıntı ya da artan kızarıklık</li>
      </ul>
      {CTA_CARD("Diz yaralanmanız", "ön çapraz bağ yaralanması")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(ACL_SRC)}
    </div>
  </section>
</main>'''

page("on-capraz-bag.html", "Ön Çapraz Bağ Yaralanması",
     "Ön çapraz bağ yırtığı nedir, her yırtık ameliyat gerektirir mi? Rehabilitasyonla ameliyatı karşılaştıran çalışmalar, spora dönüş ölçütleri ve evde altı egzersiz.",
     "on-capraz-bag.html", NECK_CSS, ACL_BODY, YT_JS,
     seo_title="Ön Çapraz Bağ Yırtığı: Ameliyat mı, Rehabilitasyon mu? | İhsan Eren",
     condition="Ön çapraz bağ yaralanması", faq_items=ACL_FAQ)
