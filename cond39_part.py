# -*- coding: utf-8 -*-
# Yeni rehber (39): El bileği kırığı sonrası (alçı çıktıktan sonra). cond38_part.py'den sonra exec edilir. Video yok.
# Egzersizler bir NHS broşüründeki hareketlere göre, hazır çizimlerle.

_ex2("wb_wrist", "dq_wrist", "Bileği aşağı yukarı hareket ettirme", "Ön kolunuzu masaya koyun, eliniz masanın kenarından taşsın. Bileğinizi yapabildiğiniz kadar aşağı bırakın, sonra yukarı kaldırın. Ağrı izin verdikçe diğer elinizle hafifçe yardım edebilirsiniz.", "10 tekrar, günde 3–4 kez")
_ex2("wb_ext", "wflex", "Bileği geriye esnetme", "Kolunuzu önünüze uzatın, dirseğiniz düz, avucunuz yukarı baksın. Diğer elinizle parmaklarınızı nazikçe aşağı ve geriye doğru çekin; bileğinizin ve ön kolunuzun iç yüzünde gerilme hissedin. Ağrı izin verdiği kadar zorlayın.", "10 tekrar ya da 15–20 saniye, günde 3–4 kez")
_ex2("wb_rot", "ge_rot", "Ön kolu çevirme", "Dirseğiniz bükülü ve gövdenize yakın olsun. Avucunuzu yukarı, sonra aşağı bakacak şekilde çevirin. Dirseğinizi gövdenizden ayırmamaya çalışın.", "10 tekrar, günde 3–4 kez")
_ex2("wb_fist", "tglide", "Yumruk yapıp açma", "Elinizi sıkıca yumruk yapın, sonra parmaklarınızı olabildiğince geniş açın.", "10 tekrar, günde 3–4 kez")
_ex2("wb_thumb", "thumb", "Başparmak hareketi", "Başparmağınızı serçe parmağınızın köküne doğru götürün, sonra olabildiğince dışarı açın. Hareketi ağrı izin verdikçe genişletin.", "10 tekrar, günde 3–4 kez")
_ex2("wb_grip", "grip", "Top sıkma", "Elinize yumuşak bir top alın ve sıkın, birkaç saniye tutup bırakın. Rahatladıkça daha güçlü sıkın ya da daha sert bir top kullanın.", "10 tekrar, günde 3–4 kez")

WB_FAQ = [
 ("Alçı çıktı ama bileğim hâlâ çok tutuk, normal mi?", "Evet. Alçıda geçen haftalardan sonra bilek ve parmakların tutuk, kasların zayıf olması beklenir. Bir miktar ağrı ve şişlik de normaldir, özellikle elinizi yeniden kullanmaya başladığınızda. Bunlar zamanla ve kullanımla giderek azalır. En büyük ilerleme genellikle ilk 1–2 ayda olur, ama bir miktar şişlik ve tutukluk birkaç ay sürebilir."),
 ("Fizyoterapiye gitmem şart mı?", "Herkes için şart değil. 26 çalışmayı inceleyen bir Cochrane derlemesinde, bir terapistin öğrettiği ev egzersiz programı ile buna ek olarak düzenli fizyoterapi alanlar arasında belirgin bir fark bulunmadı; ama kanıtların kalitesi düşük. Tutukluk ya da ağrı beklenenden yavaş düzeliyorsa bir fizyoterapistten destek almak yararlı olabilir."),
 ("Kompleks bölgesel ağrı sendromu nedir?", "Kırıktan sonra nadiren gelişebilen, yaralanmayla orantısız, genellikle yanıcı bir ağrıdır. Ciltte aşırı hassasiyet, şişlik, renk ve ısı değişikliği, terleme ve tutukluk eşlik edebilir. Elinizi olabildiğince normal kullanmak ve önerilen egzersizleri yapmak riskini azaltmaya yardım edebilir. Bu belirtileri fark ederseniz erkenden hekiminize ya da fizyoterapistinize başvurabilirsiniz."),
 ("Ne zaman araba kullanabilir, ağır kaldırabilirim?", "Hekiminiz güvenli olduğunu söyleyene kadar araba kullanmamanız ve ağır kaldırmamanız önerilir. Elinizi günlük işlerde kademeli olarak, rahatladıkça daha çok kullanabilirsiniz; ama bir seferde çok fazla egzersiz yapmak ağrıyı artırabilir."),
]

WB_SRC = [
 "NHS. " + ext("https://www.nhs.uk/conditions/broken-arm-or-wrist/", "Broken arm or wrist") + ". Page last reviewed 2 October 2026.",
 "United Lincolnshire Teaching Hospitals NHS Trust. " + ext("https://www.ulh.nhs.uk/wp-content/uploads/2026/06/Fractured-Wrist-Advice-and-Exercise-following-Cast-Removal.pdf", "Fractured wrist: advice and exercise following cast removal") + ". January 2026.",
 "Handoll HHG, Elliott J. " + ext("https://cochranelibrary.com/cdsr/doi/10.1002/14651858.CD003324.pub3/pdf/CDSR/CD003324/CD003324_abstract.pdf", "Rehabilitation for distal radial fractures in adults") + ". Cochrane Database of Systematic Reviews. 2015;(9):CD003324.",
 "East Kent Hospitals University NHS Foundation Trust. " + ext("https://leaflets.ekhuft.nhs.uk/s3/leaflets/complex-regional-pain-syndrome-crps/0cf1693d-1425-44fd-a801-e39314b88c3a.p1710924222.pdf", "Complex regional pain syndrome (CRPS)") + ". Last reviewed March 2024.",
 "Royal Osteoporosis Society. " + ext("https://theros.org.uk/information-and-support/osteoporosis/living-with-osteoporosis/recovering-from-a-broken-bone/broken-wrist/", "Broken hips, wrists and other bones") + ". Last reviewed 1 April 2026.",
]

WB_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>El bileği kırığı sonrası</h1>
    <p class="lede">Alçınız çıktı, ama bileğiniz tutuk, eliniz zayıf ve biraz şiş mi? Bu çok normal. El bileği kırığı genellikle 6–12 haftada kaynar; alçı çıktıktan sonra da hareket ve güç, düzenli egzersiz ve elinizi günlük işlerde kademeli kullanmakla geri gelir. Çekinseniz bile elinizi kullanmaya başlamak, iyileşmenin en önemli adımıdır.</p>
    <p class="meta">Son güncelleme: 27 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>6–12 hafta</b><span>El bileği kırığının genellikle iyileşme süresi; ciddi kırıklarda daha uzun</span></div>
        <div class="stat"><b>İlk 1–2 ay</b><span>Alçı çıktıktan sonra elin işlevinin en çok ilerlediği dönem</span></div>
        <div class="stat"><b>Günde 3–4 kez</b><span>Kısa egzersiz seansları; her hareketten yaklaşık 10 tekrarla başlayın</span></div>
        <div class="stat"><b>50 yaş üstü</b><span>Kırık sonrası kemik sağlığınızı hekiminizle konuşmanız önerilir</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Alçı çıkınca neler beklenir?</h2>
        <ul class="dots">
          <li>Bilek ve parmaklarda tutukluk, kaslarda zayıflık.</li>
          <li>Bir miktar ağrı ve şişlik, özellikle elinizi yeniden kullanmaya başladığınızda.</li>
          <li>Kuru cilt: Kolunuzu ılık suda bekletip nemlendirici sürebilirsiniz.</li>
          <li>Tutukluk ve zayıflık birkaç ay sürebilir; zamanla ve kullanımla giderek azalır.</li>
        </ul>
      </div>
      <div>
        <h2>İyileşmeyi hızlandırmak için</h2>
        <ul class="dots">
          <li>Çekinseniz bile elinizi kullanmaya başlayın ve kullanımı kademeli artırın.</li>
          <li>Egzersizleri bir seferde uzun uzun değil, gün içine yayılmış kısa seanslarla yapın.</li>
          <li>Ağrı kontrol altındayken egzersizleri yapmak kolaylaşır; ağrı kesici için hekiminize danışın.</li>
          <li>Size atel verildiyse, önerilen en kısa süre kullanın; atel hareketi kısıtlar.</li>
          <li>Hekiminiz söyleyene kadar araba kullanmayın ve ağır kaldırmayın.</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Bileği açan altı egzersiz</h2>
      <p class="soft">Her hareketten yaklaşık 10 tekrarla başlayın, günde 3–4 kez kısa seanslar yapın. Kolaylaştıkça tekrar sayısını ve hareket açıklığını artırın. Hafif ağrı normaldir; ağrı şiddetli ya da sürekli hale gelirse hekiminize başvurun.</p>
      {ex_grid(["wb_wrist", "wb_ext", "wb_rot", "wb_fist", "wb_thumb", "wb_grip"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(WB_FAQ)}
      <p class="soft" style="margin-top:18px">Düşme sonrası kırıklar kemik sağlığıyla ilgili olabilir: <a href="kemik-erimesi.html">kemik erimesi</a> ve <a href="dusme-onleme.html">düşmeleri önleme</a> rehberlerine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Ağrı şiddetli ya da sürekli hale geldiyse</li>
        <li>Yaralanmayla orantısız, yanıcı bir ağrı, ciltte aşırı hassasiyet, renk ya da ısı değişikliği ve belirgin şişlik varsa</li>
        <li>Alçıdayken: ağrı artıyor, alçı çok sıkı ya da gevşek geliyor, parmaklarınız uyuşuyor, şişiyor, morarıyor ya da beyazlaşıyorsa</li>
        <li>Alçıdayken: alçının altından kötü koku ya da akıntı geliyorsa, ateşiniz varsa</li>
      </ul>
      {CTA_CARD("El bileğiniz", "el bileği kırığı sonrası")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(WB_SRC)}
    </div>
  </section>
</main>'''

page("el-bilegi-kirigi.html", "El Bileği Kırığı Sonrası",
     "Alçı çıktı ama bileğiniz tutuk ve zayıf mı? El bileği kırığından sonra neler beklenir, ne zaman normale döner, fizyoterapi şart mı? Uyarı işaretleri ve evde altı egzersiz.",
     "el-bilegi-kirigi.html", NECK_CSS, WB_BODY, "",
     seo_title="El Bileği Kırığı Sonrası: Alçı Çıktıktan Sonra Egzersizler ve İyileşme | İhsan Eren",
     condition="El bileği kırığı (distal radius kırığı) sonrası rehabilitasyon", faq_items=WB_FAQ)
