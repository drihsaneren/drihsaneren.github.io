# -*- coding: utf-8 -*-
# Yeni hastalık rehberleri (9): romatoid artrit ve egzersiz.
# cond9_part.py'den sonra exec edilir. Videolar North Bristol NHS Trust ve Hospital for Special Surgery kanallarından (oEmbed ile doğrulandı).

_ex2("ra_tglide", "tglide", "Tendon kaydırma", "Elinizi dik tutun, parmaklarınız düz olsun. Sırayla kanca, tam yumruk ve düz yumruk yapın; her birinde birkaç saniye bekleyip parmaklarınızı yeniden açın. Parmak eklemlerinin hareketini korumaya yarar; zorlamadan, ağrısız aralıkta yapın.", "5–10 tekrar, günde 1–2 kez")
_ex2("ra_grip", "grip", "Yumuşak top sıkma", "Elinize yumuşak bir top ya da rulo yapılmış bir havlu alın. Ağrıyı artırmayacak bir kuvvetle sıkın, 3–5 saniye tutup bırakın. Eklemleriniz şiş ve sıcaksa bu hareketi o gün atlayın.", "10 tekrar, günde 1 kez")
_ex2("ra_wflex", "wflex", "Bilek ve parmak germe", "Kolunuzu önünüze uzatın, avucunuz yukarı baksın. Diğer elinizle parmaklarınızı nazikçe aşağı ve geriye doğru çekin; ön kolunuzun iç yüzünde hafif bir gerilme hissedin. Zorlamayın.", "20 saniye, 3 tekrar")
_ex2("ra_eccwe", "eccwe", "Bilek güçlendirme", "Ön kolunuzu masaya koyun, avucunuz aşağı baksın. Elinize yarım litrelik bir su şişesi alın. Bileğinizi yukarı kaldırın, sonra 3–4 saniyede yavaşça indirin. Kolay geliyorsa ağırlığı azar azar artırın.", "8–10 tekrar, 2 set")

# ============================================================== ROMATOİD ARTRİT
RA_FAQ = [
 ("Egzersiz eklemlerimi daha çok yıpratır mı?", "Çalışmalar bunu göstermiyor. Sekiz çalışmanın derlemesinde egzersiz programlarının hiçbirinde zararlı etki görülmedi; kas gücü ve dayanıklılık arttı. Programı hastalığınızın dönemine göre ayarlamak yeterlidir."),
 ("Alevlenme dönemindeyken egzersiz yapmalı mıyım?", "Şiddeti azaltın ama hareketi tamamen bırakmayın. Şiş ve sıcak eklemleri dirence karşı çalıştırmayın; ağrısız aralıkta nazikçe hareket ettirin ve dinlenme aralarını artırın. Alevlenme uzun sürüyor ya da her zamankinden şiddetliyse romatoloğunuza haber verin."),
 ("El egzersizleri gerçekten işe yarıyor mu?", "490 hastalık SARAH çalışmasında, olağan bakıma eklenen kişiye özel el egzersiz programı bir yıl sonra el işlevini daha fazla iyileştirdi ve programa bağlı ciddi yan etki kaydedilmedi. Araştırmacılar programı, ilaç tedavisine eklenebilecek düşük maliyetli ve yararlı bir yöntem olarak değerlendirdi."),
 ("Kireçlenmeden farkı nedir?", "Kireçlenme (osteoartrit) eklem kıkırdağının yıpranmasıyla ilgilidir; genellikle hareketle artan ağrıya ve kısa süren sabah sertliğine yol açar. Romatoid artrit ise bağışıklık sisteminin yol açtığı iltihaplı bir hastalıktır; eklemler şişer, sabah sertliği uzun sürer ve çoğunlukla iki taraf birden tutulur. Ayrımı muayene ve kan testleriyle hekim yapar."),
]

RA_SRC = [
 "Hurkmans E, van der Giesen FJ, Vliet Vlieland TPM, Schoones J, Van den Ende ECHM. " + ext("https://www.cochrane.org/CD006853", "Dynamic exercise programs (aerobic capacity and/or muscle strength training) in patients with rheumatoid arthritis") + ". Cochrane Database Syst Rev. 2022;(3):CD006853.",
 "Lamb SE, Williamson EM, Heine PJ, et al. " + ext("https://search.pedro.org.au/search-results/record-detail/42037", "Exercises to improve function of the rheumatoid hand (SARAH): a randomised controlled trial") + ". Lancet. 2015;385(9966):421-429.",
 "Rausch Osthoff AK, Niedermann K, Braun J, et al. " + ext("https://ard.bmj.com/content/77/9/1251", "2018 EULAR recommendations for physical activity in people with inflammatory arthritis and osteoarthritis") + ". Ann Rheum Dis. 2018;77(9):1251-1260.",
 "World Health Organization. " + ext("https://www.who.int/news-room/fact-sheets/detail/rheumatoid-arthritis", "Rheumatoid arthritis") + ". Fact sheet. 28 June 2023.",
]

RA_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Romatoid artrit ve egzersiz</h1>
    <p class="lede">Romatoid artrit, bağışıklık sisteminin eklemleri hedef aldığı; en çok el ve ayaklardaki küçük eklemlerde ağrı, şişlik ve sabah sertliğiyle seyreden iltihaplı bir romatizmadır. Tedavinin temeli romatoloğunuzun düzenlediği ilaçlardır; egzersiz ise bu tedaviyi tamamlar. Çalışmalarda egzersiz programları zararlı bulunmadı; kas gücünü, dayanıklılığı ve el işlevini iyileştirdi.</p>
    <p class="meta">Son güncelleme: 7 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>18 milyon</b><span>2019'da dünyada romatoid artritle yaşayan kişi sayısı; yaklaşık %70'i kadın (DSÖ)</span></div>
        <div class="stat"><b>8 çalışma</b><span>Aerobik ve güçlendirme egzersizini inceleyen Cochrane derlemesi; hiçbirinde zararlı etki görülmedi</span></div>
        <div class="stat"><b>490 kişi</b><span>Kişiye özel el egzersiz programını sınayan SARAH çalışmasının katılımcı sayısı</span></div>
        <div class="stat"><b>7,9 / 3,6</b><span>Bir yılda el işlevi puanındaki artış (100 üzerinden): el egzersiz programı ile olağan bakım</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Romatoid artritte bağışıklık sistemi eklemleri saran zarı hedef alır; eklem şişer, ağrır ve zamanla hasar görebilir. Çoğunlukla iki elde ya da iki ayakta birden, simetrik olarak ortaya çıkar. Hastaların yarıdan fazlası 55 yaşın üzerindedir.</p>
        <p class="soft">Hastalık tamamen geçmez; ancak erken tanı ve tedavi şikâyetleri azaltabilir, hastalığı yavaşlatabilir ve kalıcı kısıtlılığı önleyebilir. Bu yüzden haftalardır süren eklem şişliği ve sabah sertliğinde romatoloji değerlendirmesi geciktirilmemelidir.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Eklemlerde ağrı, şişlik ve hassasiyet; çoğunlukla iki tarafta birden</li>
          <li>Sabahları uzun süren eklem sertliği</li>
          <li>En çok el ve ayaklardaki küçük eklemlerin tutulması</li>
          <li>Yorgunluk ve hâlsizlik</li>
          <li>Şikâyetlerin arttığı alevlenme ve azaldığı yatışma dönemleri</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Egzersiz eklemlere zarar verir mi?</h2>
      <p class="soft">Uzun yıllar iltihaplı eklemlerin dinlendirilmesi gerektiği düşünüldü. Sekiz çalışmayı inceleyen Cochrane derlemesi bunun tersini gösterdi: aerobik ve kas güçlendirme egzersizlerini birleştiren programlar dayanıklılığı ve kas gücünü artırdı, ağrıyı bir miktar azalttı; hiçbir çalışmada zararlı etki görülmedi. Avrupa romatoloji derneği EULAR da fiziksel aktivitenin romatoid artritte standart bakımın ayrılmaz bir parçası olmasını öneriyor.</p>
      <p class="soft">Ellere özel egzersiz de işe yarıyor. İlaç tedavisi en az üç aydır değişmemiş 490 hastayla yapılan SARAH çalışmasında, olağan bakıma eklenen kişiye özel germe ve güçlendirme programı bir yılın sonunda el işlevini daha fazla iyileştirdi (100 üzerinden 7,9 puana karşı 3,6 puan). Programa bağlı ciddi bir yan etki kaydedilmedi.</p>
      <div class="callout">
        <p>Egzersiz ilaç tedavisinin yerini tutmaz, onu tamamlar. Alevlenme dönemlerinde şiddeti azaltın ama hareketi tamamen bırakmayın: şiş ve sıcak eklemi zorlamadan, ağrısız aralıkta hareket ettirin; alevlenme yatışınca programı kademeli olarak eski düzeyine getirin.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <ul class="tx">
        <li><b>İlaç tedavisi</b><span>Hastalığı baskılayan ilaçlar ve gerektiğinde biyolojik ilaçlar tedavinin temelidir; romatoloğunuz düzenler ve izler.</span></li>
        <li><b>Egzersiz</b><span>Yürüyüş, bisiklet ya da yüzme gibi dayanıklılık egzersizleri kas güçlendirmeyle birlikte önerilir; program hastalığın dönemine göre ayarlanır.</span></li>
        <li><b>El egzersizleri</b><span>Germe ve güçlendirme içeren, kişiye özel bir el programı el işlevini iyileştirir.</span></li>
        <li><b>Eklem koruma</b><span>İşleri bölmek, yükü büyük eklemlere dağıtmak, kalın saplı ve hafif aletler seçmek günlük hayatta küçük eklemlerdeki yükü azaltır.</span></li>
        <li><b>Dinlenme dengesi</b><span>Aktiviteyle dinlenmeyi gün içine dengeli yaymak, yorgunlukla baş etmeyi kolaylaştırabilir.</span></li>
        <li><b>Ameliyat sonrası rehabilitasyon</b><span>Eklem ameliyatı gerekirse, en iyi sonuç için sonrasında rehabilitasyon şarttır.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Romatoid artrit için altı egzersiz</h2>
      <p class="soft">Hareketleri ağrısız aralıkta, zorlamadan yapın. Egzersizden sonra uzun süren bir ağrı artışı, bir sonraki sefer daha az yapmanız gerektiğini gösterir. Eklemleriniz şiş ve sıcakken dirençli hareketleri atlayın.</p>
      {ex_grid(["ra_tglide", "ra_grip", "ra_wflex", "ra_eccwe", "copd_sts", "cr_walk"])}
      <div class="callout">
        <p>El eklemlerinizde belirgin şekil bozukluğu varsa ya da yakın zamanda el ameliyatı olduysanız egzersizlere başlamadan önce romatoloğunuza ya da el terapistinize danışın.</p>
      </div>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Romatoid artrit için videolar</h2>
      <p class="soft">İngiltere'deki North Bristol NHS Trust'ın ve New York'taki Hospital for Special Surgery'nin YouTube kanallarından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("mIxCSJNbfhU", "El egzersizleri videosunu oynat", "Hand Exercises 1")}
          <h3>El egzersizleri</h3>
          <p>Hastanenin hazırladığı el egzersizleri videosu.</p>
        </div>
        <div class="vid">
          {vbox("oQvMzkBxqbQ", "Romatoid artrit ve egzersiz videosunu oynat", "Rheumatoid Arthritis (RA), Inflammatory Arthritis (IA) and Exercise (HSS)")}
          <h3>Romatoid artrit ve egzersiz</h3>
          <p>İltihaplı romatizmada egzersizin yerini anlatan bilgilendirme videosu.</p>
        </div>
      </div>
      <p class="meta">Videolar North Bristol NHS Trust ve Hospital for Special Surgery kanallarına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(RA_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Tek bir eklemde aniden gelişen şiddetli ağrı, şişlik ve kızarıklık; özellikle ateşle birlikteyse (acil)</li>
        <li>Bağışıklığı baskılayan ilaç kullanırken ateş, titreme ya da geçmeyen enfeksiyon belirtileri</li>
        <li>Göğüs ağrısı ya da nefes darlığı (acil)</li>
        <li>Ellerde ya da ayaklarda yeni başlayan uyuşma ve güçsüzlük</li>
        <li>Boyun ağrısıyla birlikte kollarda ve bacaklarda uyuşma ya da dengesizlik</li>
        <li>Haftalardır süren, birden çok eklemde şişlik ve uzun sabah sertliği</li>
      </ul>
      {CTA_CARD("Romatoid artrite bağlı şikâyetleriniz", "romatoid artrit")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(RA_SRC)}
    </div>
  </section>
</main>'''

page("romatoid-artrit.html", "Romatoid Artrit ve Egzersiz",
     "Romatoid artritte egzersiz eklemlere zarar verir mi? Araştırmaların gösterdikleri, alevlenme döneminde ne yapmalı, el egzersizleri, evde altı egzersiz ve videolar.",
     "romatoid-artrit.html", NECK_CSS, RA_BODY, YT_JS,
     seo_title="Romatoid Artrit: Egzersiz, El Egzersizleri ve Tedavi | İhsan Eren",
     condition="Romatoid artrit", faq_items=RA_FAQ)
