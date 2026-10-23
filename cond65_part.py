# -*- coding: utf-8 -*-
# Yeni rehber (65): Dupuytren kontraktürü (avuç içinde kordon, parmağın bükülmesi). cond64_part.py'den sonra exec edilir. Video yok.
# Kaynaklar (22 Ekim 2026'da okundu): NHS genel + tedavi + iyileşme (18 Haziran 2024), HSE (4 Ekim 2023), BSSH hasta broşürü (2016),
# İskoçya ulusal Dupuytren broşürü, NHS GGC MSK Index (Right Decisions, 9 Mayıs 2024; ameliyat sonrası öneriler ve egzersizler),
# Jerosch-Herold 2011 (UEA deposu özeti), Dias 2024 DISC (HTA özeti).

_ex2("dp_fist", "mf_fist", "Yumruk yapma", "Parmaklarınızı avucunuzdaki alt çizgiye (avuç çizgisine) doğru bükerek yumruk yapın, sonra açın. Zorlamadan, ağrısız aralıkta çalışın.", "10 tekrar, günde 4–6 kez")
_ex2("dp_open", "mf_spread", "Parmakları düzeltip açma", "Parmaklarınızı ağrısız olarak gidebildiği kadar düzeltin ve birbirinden ayırın, sonra birleştirin. İşlemle kazanılan düzlüğü korumak için önemlidir.", "10 tekrar, günde 4–6 kez")
_ex2("dp_hook", "mf_hook", "Kanca yumruk", "Parmak diplerinizdeki eklemleri düz tutarak yalnızca orta ve uç eklemlerinizi bükün, sonra parmaklarınızı düzeltin.", "10 tekrar, günde 4 kez")
_ex2("dp_glide", "tglide", "Tendon kaydırma", "Parmaklar düz başlayın; sırayla kanca yumruk, tam yumruk ve düz yumruk (parmak dipleri bükülü, parmaklar düz) pozisyonlarına geçin, her birinde birkaç saniye bekleyin.", "Sırayı 10 kez, günde 4 kez")
_ex2("dp_thumb", "thumb", "Başparmak hareketleri", "Başparmağınızı avucunuzdan olabildiğince uzaklaştırın, sonra yeniden yaklaştırın. Hareketi zorlamadan, ağrısız aralıkta yapın.", "10 tekrar, günde 4 kez")
_ex2("dp_wrist", "dq_wrist", "Bileği aşağı yukarı hareket ettirme", "Ön kolunuzu masaya koyun, eliniz masanın kenarından taşsın. Bileğinizi rahatça yapabildiğiniz kadar yukarı kaldırın, sonra aşağı indirin.", "10 tekrar, günde 4 kez")

DP_FAQ = [
 ("Egzersiz ya da atel hastalığın ilerlemesini durdurur mu?", "Hayır. Dupuytren’in bilinen bir tedavisi yok ve egzersizin ya da atelin hastalığın ilerlemesini durdurduğu gösterilmedi. İskoçya’daki bir NHS kas-iskelet rehberi, atel ve ultrasonun yararına dair kanıtın sınırlı olduğunu belirtiyor. Egzersizler asıl olarak işlemden sonra parmak hareketini geri kazanmak ve korumak içindir."),
 ("Ne zaman tedavi gerekir?", "Parmaklarınızı tam düzeltebiliyorsanız ameliyat gerekmez. Elinizi masaya düz koyamadığınızda ya da günlük işlerinizde zorlandığınızda bir el cerrahıyla konuşmanın zamanı gelmiştir. İskoçya’nın ulusal hasta broşürüne göre ameliyat genellikle parmakta en az 30 derecelik bükülme olduğunda yapılır."),
 ("İğneyle gevşetme mi, ameliyat mı?", "İğneyle gevşetme (iğne fasiyotomi) lokal anestezide yapılır, aynı gün eve dönülür ve iyileşme 2 haftaya kadar sürer; ancak hastalığın geri gelme olasılığı daha yüksektir. Ameliyatla hastalıklı dokunun çıkarılmasında (fasiyektomi) iyileşme 4–12 hafta sürer, geri gelme riski en düşüktür. Deri yamasıyla yapılan ameliyat (dermofasiyektomi) geri gelme riskini daha da azaltır ama iyileşmesi daha uzundur. Karar; parmağınızın durumu, işiniz ve beklentileriniz konuşularak cerrahınızla birlikte verilebilir."),
 ("Kollajenaz iğnesi işe yarıyor mu?", "İngiltere’de 672 kişiyle yapılan DISC çalışmasında kollajenaz enzimi iğnesi, sınırlı ameliyatla karşılaştırıldı. Birinci yılda iğne biraz daha az etkili ama daha ucuzdu; ikinci yılda aradaki fark büyüdü. İğne grubunda toplam yan etki daha fazlaydı, orta-ağır yan etkiler ise ameliyat grubunda daha sıktı. Bu ilacın Avrupa Birliği’ndeki ruhsatı, üretici firmanın isteğiyle ve ticari nedenlerle 2020’de geri çekildi; bu nedenle her ülkede bulunmayabilir."),
 ("Ameliyattan sonra gece ateli takmalı mıyım?", "Herkes için gerekmeyebilir. İngiltere’de ameliyat olan 154 kişiyle yapılan bir çalışmada, el terapisine gece ateli eklemek 12. ayda el işlevini ve parmak düzlüğünü değiştirmedi. Araştırmacılar ateli yalnızca parmak yeniden bükülmeye başlarsa kullanmayı öneriyor. Cerrahınızın ve el terapistinizin önerisine uyun."),
 ("Hastalık geri gelir mi?", "Gelebilir. Her tedaviden sonra, ameliyat edilen parmakta ya da elin başka bir bölgesinde birkaç yıl içinde yeniden bükülme olabilir. Yine de ameliyat gereken hastaların çoğu ömürleri boyunca tek bir ameliyat olur."),
]

DP_SRC = [
 "NHS. " + ext("https://www.nhs.uk/conditions/dupuytrens-contracture/", "Dupuytren’s contracture") + ", " + ext("https://www.nhs.uk/conditions/dupuytrens-contracture/treatment/", "Treatment") + " ve " + ext("https://www.nhs.uk/conditions/dupuytrens-contracture/recovery/", "Recovery") + ". Page last reviewed 18 June 2024.",
 "Health Service Executive (HSE). " + ext("https://www.hse.ie/conditions/dupuytrens-contracture/", "Dupuytren’s contracture") + ". Last reviewed 4 October 2023.",
 "British Society for Surgery of the Hand. " + ext("https://www.BSSH.ac.uk/_userfiles/pages/files/Patients/Conditions/Elective/dupuytrens_disease_leaflet_2016.pdf", "Dupuytren’s disease: patient information") + ". 2016.",
 "NHS Scotland. " + ext("https://rightdecisions.scot.nhs.uk/media/jooewmsf/national-dupuytrens-disease-patient-information-leaflet.pdf", "National Dupuytren’s disease patient information leaflet") + ".",
 "NHS Greater Glasgow and Clyde, Right Decisions. " + ext("https://www.rightdecisions.scot.nhs.uk/ggc-msk-index/hand/dupuytrens", "MSK Index: Dupuytren’s") + ". Last reviewed 9 May 2024.",
 "Jerosch-Herold C, Shepstone L, Chojnowski AJ, et al. " + ext("https://doi.org/10.1186/1471-2474-12-136", "Night-time splinting after fasciectomy or dermo-fasciectomy for Dupuytren’s contracture: a pragmatic, multi-centre, randomised controlled trial") + ". BMC Musculoskelet Disord. 2011;12:136.",
 "European Medicines Agency. " + ext("https://www.ema.europa.eu/en/medicines/human/EPAR/xiapex", "Xiapex: withdrawal of the marketing authorisation in the European Union") + ". Withdrawn 1 March 2020.",
 "Dias J, et al. " + ext("https://doi.org/10.3310/kgxd8528", "Collagenase injection versus limited fasciectomy surgery to treat Dupuytren’s contracture in adult patients in the UK: DISC, a non-inferiority RCT and economic evaluation") + ". Health Technol Assess. 2024;28(78):1–262.",
]

DP_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Dupuytren kontraktürü</h1>
    <p class="lede">Avucunuzda sert bir kabarcık ya da kordon var ve yüzük ya da serçe parmağınız avucunuza doğru bükülüp tam düzelmiyor mu? Dupuytren kontraktüründe avuç içindeki bağ dokusu kalınlaşıp kısalır. Genellikle ağrısızdır ve aylar ya da yıllar içinde yavaş ilerler. Kesin bir tedavisi yoktur; parmak bükülüp elinizi kullanmanızı kısıtladığında iğneyle gevşetme ya da ameliyat düşünülür. El egzersizleri özellikle işlemden sonra parmak hareketini geri kazanmak için önemlidir.</p>
    <p class="meta">Son güncelleme: 23 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>3’te 1</b><span>Avuçtaki kabarcıklar yaklaşık her üç kişiden birinde parmağı büken bir kordona dönüşür</span></div>
        <div class="stat"><b>30 derece</b><span>Ameliyatın genellikle düşünüldüğü en az parmak bükülmesi</span></div>
        <div class="stat"><b>2 hafta</b><span>İğneyle gevşetmeden sonra iyileşme süresi; ameliyattan sonra 4–12 hafta</span></div>
        <div class="stat"><b>154 kişi</b><span>Ameliyat sonrası gece atelinin el işlevine ek yarar sağlamadığı çalışma</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Avuç içinde sert kabarcık, çukurlaşma ya da sırt şeklinde kalınlaşma; çoğu zaman yüzük parmağının hizasında.</li>
          <li>Avuçtan parmağa uzanan, deri altında hissedilen bir kordon.</li>
          <li>Yüzük ve serçe parmağın avuca doğru bükülmesi ve tam düzelmemesi; sıklıkla iki elde birden.</li>
          <li>Bazen parmak eklemlerinin üstünde yastıkçıklar ya da ayak tabanında kabarcıklar.</li>
        </ul>
        <p class="soft">Genellikle ağrısızdır. Yeni oluşan kabarcıklar bastırınca hassas olabilir; bu rahatsızlık zamanla neredeyse her zaman geçer.</p>
      </div>
      <div>
        <h2>Kimlerde daha sık?</h2>
        <ul class="dots">
          <li>Orta yaş ve üstünde, erkeklerde kadınlardan daha sık.</li>
          <li>Kuzey Avrupa kökenlilerde daha yaygın; ailede görülme sık.</li>
          <li>Sigara, çok alkol, diyabet ve epilepsiyle ilişkili; ancak bunların hiçbiri olmayan pek çok kişide de görülür.</li>
          <li>El ile ağır çalışmanın bir nedeni olduğu düşünülmüyor.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Masa testi</h2>
      <div class="callout">
        <p>Avucunuzu ve parmaklarınızı bir masanın üzerine düz koyun. Elinizi tamamen düz koyamıyorsanız ya da günlük işlerinizde zorlanıyorsanız hekiminize başvurabilirsiniz. Erken dönemde, parmaklar düzelebiliyorken genellikle tedavi gerekmez.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi seçenekleri</h2>
      <ul class="tx">
        <li><b>İzlemek</b><span>Parmaklar tam düzelebiliyorsa tedavi gerekmez; masa testini ara ara tekrarlayabilirsiniz.</span></li>
        <li><b>İğneyle gevşetme</b><span>Lokal anestezide bir iğneyle kordon gevşetilip parmak düzeltilir. Aynı gün eve dönülür, iyileşme 2 haftaya kadar sürer; hastalığın geri gelme olasılığı ameliyattan daha yüksektir.</span></li>
        <li><b>Fasiyektomi</b><span>Hastalıklı doku ameliyatla çıkarılır. Genellikle aynı gün eve dönülür, iyileşme 4–12 hafta sürer; geri gelme riski en düşük seçenektir.</span></li>
        <li><b>Dermofasiyektomi</b><span>Hastalıklı doku üzerindeki deriyle birlikte çıkarılır ve yerine deri yaması konur. Geri gelme riski daha düşüktür ama iyileşme daha uzun sürer; genellikle tekrarlayan ya da yaygın hastalıkta kullanılır.</span></li>
        <li><b>Kollajenaz iğnesi</b><span>Kordonu yumuşatan bir enzim iğnesi ve birkaç gün sonra parmağın düzeltilmesi. Bazı hastalarda işe yarar; Avrupa Birliği’nde ruhsatı 2020’de üretici firmanın isteğiyle geri çekildiği için her ülkede bulunmaz.</span></li>
      </ul>
      <p class="soft" style="margin-top:14px">Hiçbir tedaviden sonra parmak tamamen düz ya da eskisi kadar güçlü olmayabilir ve hastalık yıllar içinde geri gelebilir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>İşlemden sonra</h2>
      <ul class="dots">
        <li>Dikişler alınıp yara iyileşene kadar sargıyı temiz ve kuru tutun; duşta elinizi bir poşetle koruyabilirsiniz.</li>
        <li>Otururken ve uyurken ön kolunuzu yastıkların üzerinde yüksekte tutun; bileğinizi, dirseğinizi ve omzunuzu hareket ettirmeyi sürdürün.</li>
        <li>İlk birkaç hafta ağır kaldırma ve çekmeden kaçının; ağır işlerde bu süre en az 6 haftadır.</li>
        <li>Yara iyileştikten sonra izi kokusuz bir nemlendiriciyle ovarak masaj yapabilirsiniz.</li>
        <li>Ağrınız izin verdiğinde ve aracı tam kontrol edebildiğinizi hissettiğinizde araç kullanabilirsiniz; önce sigortanıza danışın.</li>
        <li>Kötü koku, akıntı, kızarıklık, ateş ya da artan ağrı gibi enfeksiyon işaretlerini hemen bildirin.</li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>El hareketini korumak için altı egzersiz</h2>
      <p class="soft">Bu egzersizler, İskoçya’da bir NHS kas-iskelet rehberinin işlem sonrası önerilerinden alındı; şişlik ve iltihaba göre günde 4–6 kez yapılır. İşlemden sonra el terapistinizin size verdiği program önceliklidir. İşlem öncesinde de eli hareketli tutmaya yardım ederler, ancak hastalığın ilerlemesini durdurmazlar.</p>
      {ex_grid(["dp_fist", "dp_open", "dp_hook", "dp_glide", "dp_thumb", "dp_wrist"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(DP_FAQ)}
      <p class="soft" style="margin-top:18px">Parmağın takılıp birden açıldığı durum için <a href="tetik-parmak.html">tetik parmak</a>, el ve parmak eklemlerinde ağrı ve tutukluk için <a href="el-kireclenmesi.html">el ve parmak kireçlenmesi</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Elinizi masaya düz koyamıyorsanız</li>
        <li>Bükülme hızla ilerliyorsa ya da günlük işlerinizi zorlaştırıyorsa</li>
        <li>İşlemden sonra enfeksiyon işaretleri ya da artan ağrı ve uyuşma varsa</li>
        <li>İşlemden sonra parmak yeniden bükülmeye başlıyorsa: atel gerekip gerekmediğini konuşabilirsiniz</li>
      </ul>
      {CTA_CARD("Dupuytren işlemi sonrası el rehabilitasyonunuz", "Dupuytren kontraktürü sonrası el rehabilitasyonu")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(DP_SRC)}
    </div>
  </section>
</main>'''

page("dupuytren-kontrakturu.html", "Dupuytren Kontraktürü",
     "Avuçta sert kabarcık ve kordon, avuca bükülen yüzük ve serçe parmak: Dupuytren kontraktürü, masa testi, iğneyle gevşetme ve ameliyat seçenekleri, işlem sonrası bakım ve el egzersizleri.",
     "dupuytren-kontrakturu.html", NECK_CSS, DP_BODY, "",
     seo_title="Dupuytren Kontraktürü: Belirtiler, Tedavi Seçenekleri ve El Egzersizleri | İhsan Eren",
     condition="Dupuytren kontraktürü", faq_items=DP_FAQ)
