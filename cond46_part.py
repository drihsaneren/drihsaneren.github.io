# -*- coding: utf-8 -*-
# Yeni rehber (46): Diz kapağı çıkığı (patella çıkığı). cond45_part.py'den sonra exec edilir. Video yok.
# Egzersizler Sherwood Forest Hospitals (Temmuz 2026) ve Royal United Hospitals Bath (2020) NHS broşürlerine göre, hazır çizimlerle.

_ex2("dk_quad", "quad", "Uyluğu sıkıp topuğu kaldırma", "Bacaklarınız düz olacak şekilde oturun ya da uzanın, dizinizin altına rulo yapılmış bir havlu koyun. Uyluğunuzu sıkarak dizinizin arkasını havluya bastırın ve topuğunuzu kaldırın. 3 saniye tutun, yavaşça indirin.", "10 tekrar")
_ex2("dk_slr", "slr", "Düz bacak kaldırma", "Sırtüstü uzanın ya da bacaklarınız düz oturun. Ayak ucunuzu kendinize çekin, uyluğunuzu sıkın ve dizinizi düz tutarak bacağınızı yaklaşık 15 cm kaldırın. 3 saniye tutun, yavaşça indirin.", "10 tekrar")
_ex2("dk_bend", "hslide", "Diz bükme", "Sırtüstü uzanın ya da oturun. Topuğunuzu kaydırarak dizinizi rahat ettiğiniz kadar bükün, kısa bir süre tutun ve düzeltin. Dizlik kullanıyorsanız hekiminizin ya da fizyoterapistinizin belirlediği sınırı aşmayın.", "5 dakika boyunca")
_ex2("dk_bridge", "bridge", "Köprü", "Sırtüstü uzanın, ayaklarınız yerde, dizleriniz bükülü olsun; dizlik kullanıyorsanız izin verilen sınıra kadar bükün. Kalçanızı ve belinizi yerden kaldırın, sonra yavaşça indirin.", "Her seferde 5–10 saniye tutun")

PD_FAQ = [
 ("Diz kapağım yeniden çıkar mı?", "Olabilir. 519 kişiyi kapsayan 10 araştırmayı inceleyen bir Cochrane derlemesine göre ilk çıkıktan sonra ameliyatsız izlenenlerin yaklaşık üçte birinde, 2–9 yıl içinde diz kapağı yeniden çıktı. Ameliyat olanlarda bu oran yaklaşık beşte birdi; ancak kanıtın kesinliği çok düşük ve ameliyatın günlük işlevi belirgin şekilde iyileştirip iyileştirmediği belli değil. Çocuk ve gençlerde oran daha yüksek olabilir: 16 yaşından küçük, diz kapağı ilk kez çıkmış 64 dizle yapılan ve ortalama 14 yıl izlenen bir çalışmada diz kapağı ameliyatsız izlenenlerin %71’inde, iç bağları onarılanların %67’sinde yeniden çıktı; ameliyat uzun dönem sonucu iyileştirmedi ve tekrarı öngören tek etken ailede diz kapağı çıkığı olmasıydı. Ameliyatsız tedaviyi inceleyen 25 çalışmayı (920 hasta) kapsayan bir sistematik derlemede de yeniden çıkma oranı %31 bulundu; hiçbir ameliyatsız yöntemin diğerinden üstün olduğu gösterilemedi."),
 ("Ameliyat gerekir mi?", "Çoğu zaman gerekmez. Diz içinde başka yapılar da hasar gördüyse ya da diz kapağı tekrar tekrar çıkıyorsa ameliyat düşünülebilir. Karar, muayene ve görüntüleme sonrası hekiminizle birlikte verilir."),
 ("Dizlik ne kadar takılır?", "İlk çıkıktan sonra dizlik verilebilir. Ne kadar süre takacağınıza ve dizinizi ne kadar bükebileceğinize ekibiniz karar verir. Bir NHS broşürüne göre dizlik iki haftaya kadar kullanılabilir ve gece, kişisel bakım ve egzersiz sırasında çıkarılabilir. Dizlik çıkınca bir süre tutukluk olması normaldir."),
 ("Spora ne zaman dönebilirim?", "Dizinizin hareketi ve uyluk, arka uyluk ve baldır kaslarınızın gücü sağlam tarafla aynı düzeye gelince; koşma, yön değiştirme ve sıçrama gibi sporunuzun gerektirdiği hareketleri güvenle yapabildiğinizde. Kaynaklarda bu süre 6–8 haftadan 12–24 haftaya kadar değişiyor. Günlük işlere dönüş genellikle 6–12 hafta sürer."),
 ("Ne zaman araba kullanabilirim?", "Koltuk değneği olmadan yürüyebildiğinizde ve ani frene güvenle basabildiğinizde."),
]

PD_SRC = [
 "NHS. " + ext("https://www.nhs.uk/conditions/dislocated-kneecap/", "Dislocated kneecap") + ". Page last reviewed: 10 March 2026.",
 "Sherwood Forest Hospitals NHS Foundation Trust. " + ext("https://sfh-tr.nhs.uk/media/41qdash0/pil202607-03-pd-patella-dislocation.pdf", "Patella (kneecap) dislocation") + ". PIL202607-03-PD, July 2026.",
 "Royal United Hospitals Bath NHS Foundation Trust. " + ext("https://www.ruh.nhs.uk/patients/patient_information/PHY035_Patella_dislocation.pdf", "Dislocated knee cap (patella)") + ". RUH PHY/035, August 2020.",
 "Smith TO, Gaukroger A, Metcalfe A, Hing CB. " + ext("https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD008106.pub4/full", "Surgical versus non-surgical interventions for treating patellar dislocation") + ". Cochrane Database Syst Rev. 2023;(1):CD008106.",
 "Palmu S, Kallio PE, Donell ST, Helenius I, Nietosvaara Y. " + ext("https://ueaeprints.uea.ac.uk/13408", "Acute patellar dislocation in children and adolescents: a randomized clinical trial") + ". J Bone Joint Surg Am. 2008;90(3):463–470.",
 "Moiz M, Smith N, Smith TO, Chawla A, Thompson P, Metcalfe A. " + ext("https://ora.ox.ac.uk/objects/uuid:81381995-a360-4d23-8b66-21c3b13e1eb7", "Clinical outcomes following nonoperative management of lateral patellar dislocation: a systematic review") + ". Orthop J Sports Med. 2018;6(6):2325967118766275.",
]

PD_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Diz kapağı çıkığı (patella çıkığı)</h1>
    <p class="lede">Ani bir dönüşte ya da dizinize aldığınız bir darbede diz kapağınızın yerinden kaydığını mı hissettiniz? Diz kapağı, uyluk kemiğindeki oluğundan çoğu zaman dışa doğru çıkar ve sıklıkla kendiliğinden yerine döner. Yerine dönmüş olsa bile bir hekimin muayenesi gerekir. İyileşmenin anahtarı, uyluk ve kalça kaslarınızı yeniden güçlendirmektir.</p>
    <p class="meta">Son güncelleme: 24 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>6–12 hafta</b><span>Günlük işlere dönüş için gereken yaklaşık süre</span></div>
        <div class="stat"><b>12–24 hafta</b><span>Spora tam dönüşün sürebileceği süre</span></div>
        <div class="stat"><b>Üçte bir</b><span>İlk çıkıktan sonra ameliyatsız izlenenlerde 2–9 yılda yeniden çıkma oranı</span></div>
        <div class="stat"><b>Beşte bir</b><span>Ameliyat olanlarda aynı oran; kanıtın kesinliği çok düşük</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Diz kapağının yerinden çıkmış ya da garip bir açıda durması.</li>
          <li>Dizde “pat” diye bir his, dizi düzeltememe.</li>
          <li>Ağrı, şişlik ve bacağa basamama.</li>
          <li>Diz kapağı kendiliğinden yerine dönmüş olabilir; şişlik ve ağrı yine de sürer.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Ayak yerdeyken yapılan ani bir dönüş ya da dize doğrudan bir darbe.</li>
          <li>Zayıf bacak kasları ve eklemlerin olağandan gevşek olması riski artırır.</li>
          <li>Diz kapağının şekli de rol oynar: küçük ya da yüksekte duran bir diz kapağı daha kolay çıkabilir.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>İlk anda ne yapmalı?</h2>
      <ul class="dots">
        <li>Dizinizi hareket ettirmeyin; otururken ya da uzanırken rulo yapılmış havlu, giysi ya da yastıkla destekleyin.</li>
        <li>Bacağınıza basmayın ve üzerinde yürümeyin.</li>
        <li>Diz kapağını kendiniz yerine itmeye çalışmayın.</li>
        <li>Diz kapağı yerine dönmüş olsa bile en kısa sürede bir hekime görünün; genellikle röntgen gerekir.</li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>İyileşme döneminde neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Buz ve yükseltme</h3><p>Havluya sarılı buzu 10–15 dakika, günde en az 3 kez uygulayabilirsiniz. Dinlenirken bacağınızı yüksekte ve destekli tutun.</p></div>
        <div class="kind"><span class="n">2</span><h3>Ağrıyı kontrol edin</h3><p>Hekiminize danışarak ağrı kesici kullanabilirsiniz. Ağrının azalması egzersizleri kolaylaştırır.</p></div>
        <div class="kind"><span class="n">3</span><h3>Hareketli kalın</h3><p>Tutukluğu önlemek için diz egzersizlerini gün boyunca yapın. Dizliği ekibinizin söylediği süre ve hareket sınırıyla kullanın.</p></div>
        <div class="kind"><span class="n">4</span><h3>Dizinizi burkmayın</h3><p>Dizinizi döndürme ve burkma hareketlerinden kaçının. Diz eski gücüne kavuşmadan spora dönmeyin.</p></div>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Dizi güçlendiren dört egzersiz</h2>
      <p class="soft">Bu egzersizler ilk dönem içindir; dizlik kullanıyorsanız hekiminizin ya da fizyoterapistinizin izin verdiği sınırlar içinde yapın. Uyluk kasınız yorulduğunda dinlenin. Güçlendikçe fizyoterapistiniz sizi basamak çıkma gibi ayakta yapılan egzersizlere geçirir.</p>
      {ex_grid(["dk_quad", "dk_slr", "dk_bend", "dk_bridge"], "ex four")}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(PD_FAQ)}
      <p class="soft" style="margin-top:18px">Dizde boşalma hissi için <a href="on-capraz-bag.html">ön çapraz bağ</a>, merdivende ve çömelince artan ağrı için <a href="diz-onu-agrisi.html">diz önü ağrısı</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman acile ya da hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Dizinizin şekli değiştiyse, dizinizde “pat” diye bir his olduysa ya da diz hızla şiştiyse</li>
        <li>Kemik görünüyorsa ya da çok kanama varsa</li>
        <li>Bacağınıza basamıyorsanız ya da basınca keskin ağrı oluyorsa</li>
        <li>Yürürken zonklayan ağrı, baldırda şişlik, kızarıklık ya da sıcaklık varsa</li>
        <li>Diz ağrınız ateşle birlikte aniden ve şiddetle arttıysa</li>
        <li>Uykunuzu ciddi şekilde bölen, sürekli ve şiddetli gece ağrısı varsa</li>
      </ul>
      <p class="soft">İlk iki durumda acil servise gidin; ağrı nedeniyle bacağınızı hareket ettiremiyorsanız 112’yi arayın. Kendiniz araç kullanmayın. Hareketiniz ve gücünüz tam döndüğü halde ağrı, boşalma hissi ya da işlerinize dönmekte güçlük sürüyorsa da bir uzmana görünebilirsiniz.</p>
      {CTA_CARD("Diz kapağı çıkığı sonrası iyileşmeniz", "diz kapağı çıkığı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(PD_SRC)}
    </div>
  </section>
</main>'''

page("diz-kapagi-cikigi.html", "Diz Kapağı Çıkığı (Patella Çıkığı)",
     "Diz kapağınız yerinden mi çıktı? İlk anda ne yapmalı, dizlik ne kadar takılır, yeniden çıkar mı, spora ne zaman dönülür? Uyarı işaretleri ve evde dört egzersiz.",
     "diz-kapagi-cikigi.html", NECK_CSS, PD_BODY, "",
     seo_title="Diz Kapağı Çıkığı (Patella Çıkığı): İlk Yardım, İyileşme ve Egzersizler | İhsan Eren",
     condition="Patella çıkığı", faq_items=PD_FAQ)
