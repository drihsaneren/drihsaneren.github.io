# -*- coding: utf-8 -*-
# Yeni rehber (23): boyun düzleşmesi. cond22_part.py'den sonra exec edilir. Video yok.
# Egzersizler boyun ağrısı ve ankilozan spondilit rehberlerindekilerle aynı (çevirileri hazır).

BD_FAQ = [
 ("Boyun düzleşmesi düzelir mi?", "Asıl hedef eğriliği değiştirmek değil, ağrıyı azaltmak ve boynun rahat hareket etmesini sağlamaktır; bunun için düzenli egzersiz ve gün içinde boynu hareketli tutmak işe yarar."),
 ("Özel yastık ya da boyunluk kullanmalı mıyım?", "İngiltere Ulusal Sağlık Sistemi (NHS) boyun ağrısında alçak ve sert bir yastık öneriyor; boyunluk ise önerilmiyor, çünkü boynu hareketli tutmak daha iyi. Size rahat gelen bir yastığı deneyerek seçebilirsiniz."),
 ("Baş dönmesi ve baş ağrısı boyun düzleşmesinden mi?", "Boyun kaynaklı baş ağrısı olabilir, ancak baş dönmesinin pek çok başka nedeni vardır. Bu belirtileri yalnızca röntgendeki düzleşmeye bağlamak yerine bir hekimin değerlendirmesi daha doğru olur. Baş ağrısı ve baş dönmesi rehberlerimize de bakabilirsiniz."),
 ("Telefona eğilmek boyun düzleşmesi yapar mı?", "Uzun süre aynı pozisyonda öne eğik durmak boyunda gerginlik ve ağrıya yol açabilir. Ekranı göz hizasına yaklaştırmak, sık mola vermek ve boynu farklı yönlere hareket ettirmek rahatlatır."),
]

BD_SRC = [
 "Grob D, Frauenfelder H, Mannion AF. The association between cervical spine curvature and neck pain. Eur Spine J. 2007;16(5):669–678. Özet: " + ext("https://www.painscience.com/biblio/detailed-study-of-correlations-between-neck-pain-and-curvature-finds-none.html", "PainScience, Detailed study of correlations between neck pain and curvature finds none") + ".",
 "McAviney J, Schulz D, Bock R, Harrison DE, Holland B. Determining the relationship between cervical lordosis and neck complaints. J Manipulative Physiol Ther. 2005;28(3):187–193. Özet: " + ext("https://www.painscience.com/biblio/painful-necks-about-10-degree-straighter-in-x-rays.html", "PainScience, Painful necks about 10 degree straighter in X-rays") + ".",
 "Bussières AE, Stewart G, Al-Zoubi F, et al. " + ext("https://pubmed.ncbi.nlm.nih.gov/27836071/", "The treatment of neck pain-associated disorders and whiplash-associated disorders: a clinical practice guideline") + ". J Manipulative Physiol Ther. 2016;39(8):523–564",
 "NHS. " + ext("https://www.nhs.uk/conditions/neck-pain/", "Neck pain") + ". Page last reviewed 27 April 2023.",
]

BD_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Boyun düzleşmesi</h1>
    <p class="lede">Boyun düzleşmesi, yandan çekilen röntgende boyun omurlarının normalde öne doğru hafif çukur (lordoz) olan dizilişinin düzleşmiş görünmesidir. Ülkemizde sık konan bir tanıdır ve çoğu zaman endişe yaratır. Oysa araştırmalar, düzleşmenin ağrısı olan ve olmayan kişilerde benzer sıklıkta görüldüğünü gösteriyor. Ağrının tedavisi, röntgendeki eğrilikten çok boynun nasıl kullanıldığına odaklanır.</p>
    <p class="meta">Son güncelleme: 11 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>107 kişi</b><span>Ağrısı olan ve olmayanların boyun röntgenlerinin karşılaştırıldığı çalışma: düzleşme sıklığında fark yoktu</span></div>
        <div class="stat"><b>%23 / %17</b><span>Boyunda bir seviyede geriye bükülme görülen kişiler: ağrısı olanlarda ve olmayanlarda</span></div>
        <div class="stat"><b>Alçak ve sert</b><span>NHS'nin boyun ağrısında önerdiği yastık; boyunluk önerilmiyor</span></div>
        <div class="stat"><b>Birkaç hafta</b><span>Ağrı bu sürede geçmezse hekime başvurmak için yeterli bir süre</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Ağrının nedeni düzleşme mi?</h2>
        <p class="soft">Bir çalışmada 45 yaşın üzerindeki 107 kişinin boyun röntgenleri incelendi; yarısının boyun ağrısı vardı. Düz ya da geriye doğru bükülmüş boyun, ağrısı olanlarda ve olmayanlarda benzer sıklıkta görüldü. Yazarlar, ağrısı olan bir kişide görülen bu bulguların büyük olasılıkla tesadüf olduğunu, ağrının nedenini göstermediğini belirtti.</p>
        <p class="soft">Kiropraktik araştırmacıların yaptığı başka bir çalışmada ise eğriliği 20 derecenin altında olanlarda boyun ağrısı daha sık bulundu. Bu çalışma yalnızca bir anlık ilişki gösteriyor; düzleşmenin ağrıya yol açtığını kanıtlamıyor.</p>
      </div>
      <div>
        <h2>Bu ne anlama geliyor?</h2>
        <ul class="dots">
          <li>Röntgendeki düzleşme tek başına bir hastalık değildir; ağrısı olmayan pek çok kişide de görülür.</li>
          <li>Boyun ağrısının sık nedenleri arasında uykuda boynun rahatsız bir pozisyonda kalması ve masa başında uzun süre aynı pozisyonda çalışmak sayılır; tek bir "doğru duruş" yoktur, önemli olan sık sık pozisyon değiştirmektir.</li>
          <li>Tedavide amaç, eğriliği değiştirmekten çok ağrıyı azaltmak ve boynu yeniden rahat hareket ettirmektir.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Boynu hareketli tutun</h3><p>Hekiminiz aksini söylemedikçe boynunuzu hareket ettirmeye devam etmek daha iyidir; boyunluk önerilmez.</p></div>
        <div class="kind"><span class="n">2</span><h3>Masa başında</h3><p>Dik oturabilir, omuzlarınızı yavaşça geriye döndürebilir ve boynunuzu uzun süre aynı pozisyonda tutmaktan kaçınabilirsiniz.</p></div>
        <div class="kind"><span class="n">3</span><h3>Uyku</h3><p>Alçak ve sert bir yastık kullanabilir, başınızı vücudunuzla aynı hizada tutabilirsiniz. Yüzüstü yatmak boynu zorlar.</p></div>
        <div class="kind"><span class="n">4</span><h3>Sıcak, soğuk, ağrı kesici</h3><p>Havluya sarılı soğuk ya da sıcak uygulama ve kısa süreli ağrı kesiciler rahatlama sağlayabilir.</p></div>
      </div>
      <p class="soft" style="margin-top:18px">Boyun ağrısının nedenleri ve tedavisi için <a href="boyun-agrisi.html">boyun ağrısı</a>, uzun süre bilgisayar başında çalışıyorsanız <a href="masa-basi.html">masa başında çalışanlar için</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Boynu rahatlatan altı egzersiz</h2>
      <p class="soft">Hareketleri yavaş ve ağrısız bir aralıkta yapın. Kola yayılan uyuşma ya da güçsüzlük varsa önce bir hekime ya da fizyoterapiste danışabilirsiniz.</p>
      {ex_grid(["chin", "rot", "side", "scap", "thor", "wallpost"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(BD_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Ağrı ya da tutukluk birkaç haftada geçmiyorsa</li>
        <li>Ağrı kesiciler işe yaramıyorsa</li>
        <li>Kolda karıncalanma, uyuşma, soğukluk ya da güçsüzlük varsa</li>
        <li>Ateş, kilo kaybı ya da düşme ve kaza sonrası başlayan şiddetli ağrı varsa</li>
      </ul>
      {CTA_CARD("Boyun ağrınız", "boyun ağrısı ve boyun düzleşmesi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(BD_SRC)}
    </div>
  </section>
</main>'''

page("boyun-duzlesmesi.html", "Boyun Düzleşmesi",
     "Röntgende boyun düzleşmesi ağrının nedeni mi? Ağrısı olan ve olmayanları karşılaştıran çalışmalar, yastık ve boyunluk, masa başı ve uyku önerileri ve boynu rahatlatan altı egzersiz.",
     "boyun-duzlesmesi.html", NECK_CSS, BD_BODY, "",
     seo_title="Boyun Düzleşmesi: Ağrının Nedeni mi? Yastık, Egzersiz ve Öneriler | İhsan Eren",
     condition="Boyun düzleşmesi (servikal lordoz kaybı)", faq_items=BD_FAQ)
