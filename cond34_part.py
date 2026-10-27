# -*- coding: utf-8 -*-
# Yeni rehber (34): Kaval kemiği ağrısı (shin splints, medial tibial stres sendromu). cond33_part.py'den sonra exec edilir. Video yok.
# Egzersizler hazır çizimlerle; metinler bu sayfaya göre.

_ex2("ss_calf", "calf", "Duvarda baldır germe", "Ellerinizi duvara dayayın, bir bacağınızı arkaya alın. Arkadaki dizinizi düz, topuğunuzu yerde tutarak kalçanızı duvara doğru ilerletin; baldırınızda gerginlik hissedin. Egzersizden sonra yapmanız önerilir.", "20–30 saniye, her bacakla 2–3 kez")
_ex2("ss_soleus", "soleus", "Dizi bükük baldır germe", "Aynı pozisyonda arkadaki ayağınızı biraz öne alın ve dizinizi bükün. Topuğunuz yerden kalkmadan kalçanızı aşağı indirin; gerilmeyi baldırın alt kısmında hissedin.", "20–30 saniye, her bacakla 2–3 kez")
_ex2("ss_toe", "dm_toe", "Ayak ucu ve topuk kaldırma", "Oturun, ayaklarınız yere düz bassın. Topuklarınız yerde kalarak ayak uçlarınızı kaldırın, sonra indirip bu kez topuklarınızı kaldırın. Kaval kemiğinin önündeki ve baldırdaki kasları ağrısız çalıştırır.", "10–15 tekrar, günde 2 kez")
_ex2("ss_heel", "heel", "Tezgâha tutunarak topuk yükseltme", "Tezgâha tutunarak dik durun. İki topuğunuzu birlikte kaldırıp parmak uçlarınızda yükselin, 2 saniye bekleyip yavaşça inin. Ağrı yapmıyorsa zamanla tek ayakla yapabilirsiniz.", "10–15 tekrar, 2–3 set")
_ex2("ss_arch", "ff_short", "Ayak kavsini kaldırma", "Oturun, ayağınız yere düz bassın. Ayak tabanınızdaki kasları sıkarak ayağınızı kısaltır gibi kavsinizi yükseltin; parmaklarınız kıvrılmasın, yerde düz kalsın. Birkaç saniye tutup gevşetin.", "10 tekrar, günde 2 kez")
_ex2("ss_sls", "sls", "Tek ayak üzerinde durma", "Tezgâhın önünde dik durun, gerekirse bir elinizle hafifçe tutunun. Bir ayağınızı yerden kaldırıp dengede durun. Kolaylaştıkça tutunmadan ya da gözleriniz kapalı deneyin.", "30 saniye, her ayakla 3 kez")

SS_FAQ = [
 ("Ne kadar dinlenmeliyim?", "Ağrıya yol açan aktiviteye en az iki-üç hafta ara verip sonra kademeli olarak dönmeniz önerilir. Bu sürede yüzme, bisiklet, eliptik bisiklet ya da yoga gibi kaval kemiğini daha az zorlayan hareketlerle aktif kalabilirsiniz."),
 ("Stres kırığı olup olmadığını nasıl anlarım?", "Kaval kemiği ağrısı genellikle iki bacakta ve 5 santimetreden geniş bir alanda olur. Ağrı küçük bir noktada toplanıyorsa, çoğunlukla tek bacaktaysa ve şişlik varsa stres kırığı olabilir. Röntgen başlangıçta normal görünebilir; bu durumda hekiminize başvurabilirsiniz. Kaval kemiği ağrısının tanısı çoğunlukla öykü ve muayeneyle konur: 46 sporcuyla yapılan bir çalışmada iki hekim birbirinden habersiz olarak hastaların %96’sında aynı tanıya vardı."),
 ("Tabanlık kullanmalı mıyım?", "Düz tabanlık ya da içe basma varsa bir ayak uzmanı tabanlık önerebilir. Ancak bir araştırmada tabanlık kullananlarda kaval kemiği ağrısı daha sık görülmüştü; bu, tabanlığın ağrıya yol açtığını değil, zaten risk taşıyan kişilerin tabanlık kullandığını gösteriyor olabilir. Kararı bir uzmanla birlikte verebilirsiniz."),
 ("Kimlerde daha sık görülür?", "Koşucuların yüzde 5 ile 35’inde görülür. Araştırmalarda kadınlarda, vücut kitle indeksi yüksek olanlarda, ayak kavsi belirgin çökenlerde, daha önce aynı ağrıyı yaşamış olanlarda ve koşuya yeni başlayanlarda daha sık bulunmuştur."),
]

SS_SRC = [
 "NHS. " + ext("https://www.nhs.uk/conditions/shin-splints", "Shin splints") + ". Page last reviewed 9 February 2023.",
 "nidirect. " + ext("https://nidirect.gov.uk/conditions/shin-splints", "Shin splints") + ". Last updated 10 January 2025.",
 "Newman P, Witchalls J, Waddington G, Adams R. " + ext("https://doaj.org/article/63035df9eaf04e42ac9b4e87e645fcc3", "Risk factors associated with medial tibial stress syndrome in runners: a systematic review and meta-analysis") + ". Open Access Journal of Sports Medicine. 2013;4:229–241.",
 "Winters M, Eskes M, Weir A, et al. " + ext("https://doi.org/10.1007/s40279-013-0087-0", "Treatment of medial tibial stress syndrome: a systematic review") + ". Sports Med. 2013;43(12):1315–1333",
 "Winters M, Bakker EWP, Moen MH, Barten CC, Teeuwen R, Weir A. " + ext("https://bjsm.bmj.com/content/52/19/1267", "Medial tibial stress syndrome can be diagnosed reliably using history and physical examination") + ". Br J Sports Med. 2018;52(19):1267.",
]

SS_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Kaval kemiği ağrısı (shin splints)</h1>
    <p class="lede">Koşmaya yeni başladınız ya da antrenmanı hızla artırdınız ve bacaklarınızın önünde, kaval kemiği boyunca sızı mı başladı? Kaval kemiği ağrısı, bacağa fazla yük binmesiyle, çoğu zaman koşu ve zıplama gibi tekrarlı darbelerle ortaya çıkar. Ciddi bir sorun değildir ve çoğu zaman birkaç haftada düzelir; asıl önemli olan, aynı hatayı tekrarlamadan kademeli olarak geri dönmektir.</p>
    <p class="meta">Son güncelleme: 27 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%5–35</b><span>Koşucularda görülme oranı</span></div>
        <div class="stat"><b>2–3 hafta</b><span>Ağrıya yol açan aktiviteye önerilen ara</span></div>
        <div class="stat"><b>5 cm’den geniş</b><span>Tipik ağrı alanı; daha küçük bir noktadaki ağrı stres kırığını düşündürebilir</span></div>
        <div class="stat"><b>Birkaç hafta</b><span>Düzelmenin başlaması için gereken süre</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Bacağın önünde, kaval kemiği boyunca ağrı ve hassasiyet.</li>
          <li>Genellikle egzersize başladıktan kısa süre sonra başlar, dinlenince azalır.</li>
          <li>Önce künt bir sızıdır; zamanla keskinleşip egzersizi bıraktıracak kadar artabilir, hatta dinlenirken de sürebilir.</li>
          <li>Çoğu zaman iki bacakta birden ve geniş bir alanda olur; hafif şişlik görülebilir.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Bir süre hareketsiz kaldıktan sonra egzersize başlamak ya da yükü aniden artırmak.</li>
          <li>Sert ya da engebeli zeminde koşmak, zıplamak.</li>
          <li>Eskimiş ya da ayağı iyi desteklemeyen spor ayakkabıları.</li>
          <li>Fazla kilo, düz taban ya da içe basma, gergin baldır kasları ve zayıf ayak bilekleri.</li>
          <li>Koşu tekniğinin zayıf olması.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Evde neler yapabilirim?</h2>
        <ul class="dots">
          <li><b>Ara verin:</b> Ağrıya yol açan aktiviteyi en az 2–3 hafta bırakın.</li>
          <li><b>Buz:</b> Havluya sarılı buzu ilk günlerde birkaç saatte bir, 10–20 dakika kaval kemiğinize uygulayabilirsiniz.</li>
          <li><b>Ağrı kesici:</b> Kullanmanız gerekiyorsa hangisinin size uygun olduğunu hekiminize ya da eczacınıza sorun.</li>
          <li><b>Aktif kalın:</b> Yüzme, bisiklet, eliptik bisiklet ve yoga kaval kemiğini daha az zorlar.</li>
        </ul>
      </div>
      <div>
        <h2>Koşuya dönüş</h2>
        <ul class="dots">
          <li>Ağrı geçince doğrudan eski seviyenize dönmeyin; süreyi ve sıklığı kademeli artırın.</li>
          <li>Mümkünse düz ve yumuşak zeminde koşun.</li>
          <li>Yüksek ve düşük darbeli egzersizleri birbirine karıştırın.</li>
          <li>Egzersiz öncesi ısının, sonrasında özellikle baldırlarınızı ve bacak önünü esnetin.</li>
          <li>Ayağınızı iyi destekleyen, yeterince yumuşak spor ayakkabıları seçin.</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Bacakları güçlendiren altı egzersiz</h2>
      <p class="soft">Germe ve güçlendirme hareketlerini ağrısız bir aralıkta yapın. Kaval kemiğinizde ağrı artıyorsa yükü azaltın; küçük bir noktada keskin ağrı olursa egzersizi bırakıp hekiminize başvurun.</p>
      {ex_grid(["ss_calf", "ss_soleus", "ss_toe", "ss_heel", "ss_arch", "ss_sls"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(SS_FAQ)}
      <p class="soft" style="margin-top:18px">Ayak yapınızla ilgili bilgi için <a href="duztabanlik.html">düz tabanlık</a>, baldır ve topuk ağrısı için <a href="asil-tendinopatisi.html">aşil tendinopatisi</a> rehberlerine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Evde önlemlere rağmen ağrı geçmiyor ya da artıyorsa</li>
        <li>Ağrı küçük bir noktada toplanıyor, çoğunlukla tek bacakta ve şişlikle birlikteyse (stres kırığı olabilir)</li>
        <li>Egzersiz sırasında giderek artan, kramp gibi bir ağrı olup dinlenince hızla geçiyorsa</li>
        <li>Aynı gün: ağrı çok şiddetliyse ya da bacağınızı yaraladıysanız</li>
      </ul>
      {CTA_CARD("Kaval kemiği ağrınız", "kaval kemiği ağrısı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(SS_SRC)}
    </div>
  </section>
</main>'''

page("kaval-kemigi-agrisi.html", "Kaval Kemiği Ağrısı (Shin Splints)",
     "Koşarken bacağınızın önünde ağrı mı var? Kaval kemiği ağrısı neden olur, ne kadar dinlenmeli, stres kırığından nasıl ayrılır? Koşuya dönüş ve evde altı egzersiz.",
     "kaval-kemigi-agrisi.html", NECK_CSS, SS_BODY, "",
     seo_title="Kaval Kemiği Ağrısı (Shin Splints): Nedenleri, Tedavisi ve Egzersizler | İhsan Eren",
     condition="Kaval kemiği ağrısı (medial tibial stres sendromu)", faq_items=SS_FAQ)
