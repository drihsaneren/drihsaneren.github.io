# -*- coding: utf-8 -*-
# Tenisçi dirseği sayfası. hip_part.py'den sonra exec edilir.

TABLE = '<path class="obj" d="M8 70 H72 M64 70 V112"/>'

# İzometrik bilek açma: ön kol masada, avuç aşağı; diğer el elin üstüne bastırır, el yerinde kalır.
SV["isowe"] = fig(TABLE +
    '<path class="fig" d="M14 64 H62"/>'
    '<path class="fig hl" d="M62 64 H86"/>'
    '<path class="fig" d="M76 30 V56"/><rect x="70" y="54" width="14" height="6" rx="2" fill="#2A6F6B"/>'
    '<g fill="none" stroke="#C8963E" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M92 38 V50 M88 46 L92 50 L96 46"><animate attributeName="opacity" values="0;1;0" dur="1.6s" repeatCount="indefinite"/></path>'
    '<path d="M100 74 V62 M96 66 L100 62 L104 66"><animate attributeName="opacity" values="0;1;0" dur="1.6s" begin="0.8s" repeatCount="indefinite"/></path></g>',
    "İzometrik bilek açma")

# Eksantrik bilek açma: ön kol masada, el masanın kenarından taşar; ağırlık yavaşça indirilir.
SV["eccwe"] = fig(TABLE +
    '<path class="fig" d="M14 64 H62"/>'
    f'<g>{anim_t("-40 62 64;45 62 64;-40 62 64", dur="4s", kt="0;0.75;1", typ="rotate")}'
    '<path class="fig hl" d="M62 64 H82"/><rect x="80" y="54" width="9" height="20" rx="3" fill="#C8963E"/></g>',
    "Eksantrik bilek açma")

# Top sıkma (yandan)
SV["grip"] = fig(
    '<path class="fig" d="M56 116 L56 84"/>'
    '<rect x="48" y="54" width="16" height="32" rx="7" fill="#2A6F6B"/>'
    '<circle cx="72" cy="46" r="9" fill="#C8963E"><animate attributeName="r" values="9.5;7.5;9.5" dur="2.4s" repeatCount="indefinite"/></circle>'
    f'<path class="fig hl" d="M58 56 Q60 34 74 34 Q86 38 82 52">{anim_d("M58 56 Q60 34 74 34 Q86 38 82 52;M58 56 Q62 38 73 37 Q82 40 79 50;M58 56 Q60 34 74 34 Q86 38 82 52", dur="2.4s")}</path>'
    '<path class="fig" d="M60 76 L72 60"/>',
    "Top sıkma")

SV["wext_st"] = SV["wflex"]
SV["scap3"] = SV["scap"]
SV["row2"] = SV["row"]

EXT.update({
 "isowe": ("İzometrik bilek açma", "Ön kolunuzu masaya koyun, avucunuz aşağı baksın, eliniz masanın kenarından taşsın. Bileğinizi yukarı kaldırmaya çalışırken diğer elinizle elinizin üstüne bastırın; el yerinden oynamasın. Ağrıyı belirgin artırmayan bir kuvvetle tutun. Ağrılı dönemde de genellikle iyi tolere edilir.", "30–45 saniye, 5 tekrar, günde 1–2 kez"),
 "eccwe": ("Eksantrik bilek açma", "Ön kolunuzu masaya koyun, avucunuz aşağı baksın. Elinize dolu bir su şişesi ya da hafif bir ağırlık alın. Diğer elinizle yardım ederek bileğinizi yukarı kaldırın, sonra yardımı bırakıp ağırlığı 3–4 saniyede yavaşça aşağı indirin. Kolaylaştıkça ağırlığı artırın.", "15 tekrar, 3 set, günde 1 kez"),
 "wext_st": ("Bilek açıcı germe", "Kolunuzu önünüze uzatın, dirseğiniz düz, avucunuz aşağı baksın. Diğer elinizle elinizin sırtından tutup bileğinizi nazikçe aşağı ve kendinize doğru bükün; ön kolunuzun dış yüzünde gerilme hissedin.", "20–30 saniye, 3 tekrar"),
 "grip": ("Top sıkma", "Elinize yumuşak bir top ya da rulo yapılmış bir havlu alın. Ağrıyı artırmayacak bir kuvvetle sıkın, birkaç saniye tutun ve bırakın. Kavrama gücünü artırır; ağrı artıyorsa daha yumuşak bir nesne seçin.", "10 tekrar, günde 2–3 kez"),
 "scap3": EXT["scap"],
 "row2": EXT["row"],
})

DIRSEK_FAQ = [
 ("Tenis oynamıyorum, neden tenisçi dirseği oldum?", "Adına rağmen hastaların çoğu tenis oynamaz. Sorun, bileği ve parmakları açan kasların dirseğin dış yüzüne yapıştığı ortak kirişin aşırı yüklenmesidir. El ve bileğin yoğun kullanıldığı işlerde görülme sıklığı %29'a kadar çıkabiliyor; en sık 40–60 yaş arasında görülür."),
 ("Kortizon iğnesi yaptırmalı mıyım?", "Kortizon iğnesi kısa sürede ağrıyı azaltabilir, ancak uzun vadede sonuçları kötüleştirebilir. 165 hastalık bir çalışmada 1 yılın sonunda tamamen ya da çok iyileşenlerin oranı kortizon grubunda %83, plasebo iğne grubunda %96 oldu; nüks ise kortizon grubunda %54, plasebo grubunda %12 idi."),
 ("Dirsek bandı işe yarar mı?", "Ön kola takılan bant ya da bilek desteği, aktivite sırasında kullanıldığında ağrıyı hemen hafifletebilir. Uzun vadeli etkisi konusunda ise kılavuz bir öneride bulunamıyor. Bant tedavinin tamamı değil, yük ayarlamaya yardımcı bir araçtır."),
 ("Ne kadar sürede geçer?", "Sabır gerektirir. Genel sağlık hizmetine başvuranların yarısından fazlasında şikâyetler 1 yıl sonra da sürebiliyor ve 6–12 ay içinde nüks oranı %20–38 arasında bildiriliyor. Yükü kademeli artırılan bir egzersiz programına düzenli devam etmek bu süreci yönetmenin temelidir."),
 ("Kolumu tamamen dinlendirmeli miyim?", "Hayır. Ağrıyı belirgin artıran kavrama ve kaldırma işlerini geçici olarak azaltın, ama kolu askıya almayın. Kiriş, kademeli olarak artırılan yüke uyum sağlayarak güçlenir; kılavuz da yükün aşamalı olarak yeniden artırılmasını öneriyor."),
]

DIRSEK_SRC = [
 "Coombes BK, Bisset L, Brooks P, Khan A, Vicenzino B. " + ext("https://jamanetwork.com/journals/jama/fullarticle/1568252", "Effect of corticosteroid injection, physiotherapy, or both on clinical outcomes in patients with unilateral lateral epicondylalgia: a randomized controlled trial") + ". JAMA. 2013;309(5):461-469.",
 "Lucado AM, Day JM, et al. " + ext("https://www.jospt.org/doi/10.2519/jospt.2022.0302", "Lateral elbow pain and muscle function impairments: clinical practice guidelines linked to the International Classification of Functioning, Disability and Health") + ". J Orthop Sports Phys Ther. 2022;52(12).",
 "Physiopedia. " + ext("https://www.physio-pedia.com/Lateral_Epicondylitis", "Lateral Epicondylitis") + ".",
]

DIRSEK_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Tenisçi dirseği (lateral epikondilit)</h1>
    <p class="lede">Dirseğin dış yüzünde, kavramakla ve bileği kaldırmakla artan ağrıdır. Adına rağmen hastaların çoğu tenis oynamaz: bileği açan kasların ortak kirişinin aşırı yüklenmesiyle ortaya çıkar. Kademeli güçlendirme egzersizleri tedavinin temelidir; sabır gerektirir.</p>
    <p class="meta">Son güncelleme: {UPDATED}</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%3</b><span>ABD'de yıllık görülme sıklığı</span></div>
        <div class="stat"><b>%7–10</b><span>40–60 yaş arasında yıllık görülme sıklığı</span></div>
        <div class="stat"><b>%29'a kadar</b><span>El ve bileğin yoğun kullanıldığı işlerde görülme sıklığı</span></div>
        <div class="stat"><b>%54</b><span>Kortizon iğnesi yapılanlarda 1 yıl içinde nüks; plasebo iğnede %12</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Bileği ve parmakları geriye doğru açan kaslar, dirseğin dış yüzündeki kemik çıkıntısına (lateral epikondil) ortak bir kirişle yapışır. Bu kirişin kaldırabileceğinden fazla ya da alışık olmadığı biçimde yüklenmesi ağrıya yol açar. Sorun iltihaptan çok kirişin yıpranması ve yüke uyum sağlayamamasıdır; bu yüzden "tendinopati" adı da kullanılır.</p>
      </div>
      <div>
        <h2>Belirtiler ve risk etkenleri</h2>
        <ul class="dots">
          <li>Dirseğin dış yüzünde, bazen ön kola yayılan ağrı</li>
          <li>Kavrarken, çanta taşırken, kapı kolu ya da kavanoz kapağı çevirirken artan ağrı</li>
          <li>Kavrama gücünde azalma, fincan tutarken zorlanma</li>
          <li>Risk etkenleri: 40–60 yaş, el ve bileğin yoğun, tekrarlayan kullanıldığı işler, raket sporları</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Kortizon iğnesi: kısa vadede rahatlama, uzun vadede risk</h2>
      <p class="soft">Avustralya'da 165 hastayla yapılan bir çalışmada kortizon iğnesi ilk haftalarda ağrıyı azalttı; ancak 1 yılın sonunda tamamen ya da çok iyileşenlerin oranı kortizon grubunda %83, plasebo iğne grubunda %96 oldu. Nüks oranı ise kortizon grubunda %54, plasebo grubunda %12 idi.</p>
      <div class="callout">
        <p>Yani iğnenin getirdiği kısa süreli rahatlama, uzun vadede iyileşmeyi yavaşlatabiliyor ve ağrının geri dönme olasılığını artırabiliyor. İğne düşünülüyorsa bu risk hekiminizle birlikte değerlendirilmelidir.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <p class="soft">Amerikan Fizyoterapi Derneği'nin 2022 kılavuzu tedavinin merkezine kademeli güçlendirme egzersizlerini koyuyor.</p>
      <ul class="tx">
        <li><b>Güçlendirme egzersizleri</b><span>Bileği açan kaslara yönelik izometrik, konsantrik ve eksantrik direnç egzersizleri önerilir. Yük, kirişin uyum sağlayabileceği hızda, aşamalı olarak artırılır.</span></li>
        <li><b>Manuel terapi</b><span>Dirsek eklemine yönelik mobilizasyon ağrıyı azaltmak ve ağrısız kavrama gücünü artırmak için önerilir; boyun, sırt ve bileğe yönelik uygulamalar destek olarak eklenebilir.</span></li>
        <li><b>Kuru iğneleme</b><span>Kirişe ya da tetik noktalara uygulanan kuru iğneleme, ağrıyı ve işlev kaybını azaltmak için önerilen yöntemler arasındadır.</span></li>
        <li><b>Bantlama ve dirsek bandı</b><span>Sert bantlama kısa vadede ağrıyı azaltır. Ön kol bandı ya da bilek desteği aktivite sırasında kullanıldığında ağrıyı hemen hafifletebilir; uzun vadeli etkisi belirsizdir.</span></li>
        <li><b>Omuz ve kürek kemiği</b><span>Muayenede zayıflık saptanırsa omuz ve kürek kemiği kaslarını güçlendiren egzersizler programa eklenir.</span></li>
        <li><b>Ergonomi</b><span>İş ve günlük hayattaki kavrama, kaldırma ve bilek kullanımının düzenlenmesi şikâyetleri hafifletebilir.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Tenisçi dirseği için altı egzersiz</h2>
      <p class="soft">Egzersiz sırasında hafif ve katlanılabilir bir ağrı olabilir; ağrı ertesi gün başlangıç düzeyine dönüyorsa devam edin. İzometrik egzersizle başlayıp ağrı azaldıkça eksantrik egzersize geçin.</p>
      {ex_grid(["isowe", "eccwe", "wext_st", "grip", "scap3", "row2"])}
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Günlük hayatta dirseğiniz için</h2>
        <p class="soft">Amaç kolu kullanmayı bırakmak değil, kirişin yükünü ayarlamaktır.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Eşyaları avucunuz yukarı bakacak şekilde (alttan) kaldırın.</li>
        <li>Ağır çantaları kolunuzu bükmeden, omzunuzda ya da iki elle taşıyın.</li>
        <li>Kalın saplı aletler ve fincanlar kavramayı kolaylaştırır.</li>
        <li>Klavye ve fare kullanırken bileğinizi düz tutun, sık ara verin.</li>
        <li>Raket sporlarında raket sapı, tel gerginliği ve teknik için destek alın.</li>
      </ul>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Tenisçi dirseği için videolar</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("Wy3vqiB9X9A", "Dirsek ağrısı videosunu oynat", "Elbow Pain Gone! Fast &amp; Easy (Proven)")}
          <h3>Dirsek ağrısı için pozisyonel gevşetme</h3>
          <p>Ağrıyı hafifletmeye yönelik basit bir kendi kendine uygulama.</p>
        </div>
        <div class="vid">
          {vbox("CaYoIOWro_4", "Tenisçi dirseği kendi kendine tedavi videosunu oynat", "Stop Tennis Elbow Pain Now! (3 Minute Self-Treatment)")}
          <h3>Üç dakikalık kendi kendine uygulama</h3>
          <p>Ön kol kaslarına yönelik yumuşak doku uygulaması.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(DIRSEK_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlar tenisçi dirseği dışında bir soruna işaret edebilir. Beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Düşme ya da darbe sonrası dirsekte şişlik, şekil bozukluğu ya da hareket kaybı</li>
        <li>Dirseğin kilitlenmesi, tam bükülüp düzelmemesi</li>
        <li>Dirsekte kızarıklık, sıcaklık ve ateş</li>
        <li>Boyundan kola yayılan ağrı, elde uyuşma, karıncalanma ya da güç kaybı</li>
        <li>Dinlenmekle geçmeyen gece ağrısı ya da nedensiz kilo kaybı</li>
      </ul>
      {CTA_CARD("Dirsek ağrınız", "tenisçi dirseği")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(DIRSEK_SRC)}
    </div>
  </section>
</main>'''

page("tenisci-dirsegi.html", "Tenisçi Dirseği",
     "Tenisçi dirseği (lateral epikondilit) nedir, tenis oynamayanlarda neden olur, kortizon iğnesi yapılmalı mı, ne kadar sürede geçer? Evde altı egzersiz, günlük hayat önerileri, videolar ve uyarı işaretleri.",
     "tenisci-dirsegi.html", NECK_CSS, DIRSEK_BODY, YT_JS,
     seo_title="Tenisçi Dirseği (Lateral Epikondilit): Egzersizler ve Tedavi | İhsan Eren",
     condition="Tenisçi dirseği (lateral epikondilit)", about=cond("Tenisçi dirseği (lateral epikondilit)"),
     faq_items=pick(DIRSEK_FAQ, 0, 1, 2, 3))
