# -*- coding: utf-8 -*-
# Yeni rehber (25): atlet dizi (patellar tendinopati). cond24_part.py'den sonra exec edilir. Video yok.
# Havluya bastırma, oturarak diz düzeltme, köprü ve duvarda yarım çömelme mevcut anahtarlar (çevirileri hazır).

_ex2("pt_iso", "wall", "Duvarda bekleme", "Sırtınızı duvara yaslayın ve dizleriniz yaklaşık dik açı yapacak kadar kayarak inin; zorlanıyorsanız daha yukarıda kalın. Kımıldamadan bekleyin. Ağrı 10 üzerinden 3’ü geçmesin. Kolaylaştıkça ağırlığınızı ağrılı bacağa daha çok verebilirsiniz.", "45 saniye, 5 kez, her gün")
_ex2("pt_sls", "sls", "Tek bacak çömelme", "Duvarda yarım çömelme ağrısız hâle gelince başlayın. Tezgâha hafifçe tutunarak ağrılı bacağınızın üzerinde durun, dizinizi rahat ettiğiniz kadar bükün; diziniz içe kaçmasın. Sonra iterek doğrulun.", "10 tekrar, 3 set")

JK_FAQ = [
 ("Dinlenirsem geçer mi?", "Kiriş iyileşmek için yüke ihtiyaç duyar, ancak fazla yük ağrıyı artırır. Tamamen dinlenmek yerine ağrıyı artıran koşu, sıçrama ve uzun yürüyüşleri azaltıp kademeli egzersize başlayabilirsiniz."),
 ("Ne kadar sürer?", "Çoğu zaman aylar sürebilir. Büyük kısmının belirtileri yaklaşık iki yıldır süren sporcularla yapılan bir çalışmada, 24 haftanın sonunda katılımcıların yarısından azı eski spor düzeyine dönebilmişti. Düzenli ve sabırlı egzersiz önemlidir."),
 ("Spora devam edebilir miyim?", "Yükü azaltarak, ağrının izin verdiği ölçüde devam edebilirsiniz. Çalışmada sporcular, tek bacak çömelmede ağrı 10 üzerinden 3 ya da altına inince bir sonraki aşamaya geçti ve spora kademeli olarak döndü. Belirtiler alevlendiğinde ise etkinliği en az 4 hafta bırakmaları ya da belirgin azaltmaları önerildi."),
 ("Diz önü ağrısından farkı ne?", "Atlet dizinde ağrı diz kapağının hemen altında, kirişin üzerindedir. Diz önü ağrısında ise ağrı daha çok diz kapağının çevresinde ve arkasında hissedilir. Ayrıntılar için diz önü ağrısı rehberimize bakabilirsiniz."),
]

JK_SRC = [
 "Lian ØB, Engebretsen L, Bahr R. Prevalence of jumper’s knee among elite athletes from different sports: a cross-sectional study. Am J Sports Med. 2005;33(4):561–567. " + ext("https://lida.sport-iat.de/twm/Record/4009854?lng=en", "Özet") + ".",
 "Breda SJ, Oei EHG, Zwerver J, et al. Effectiveness of progressive tendon-loading exercise therapy in patients with patellar tendinopathy: a randomised clinical trial. Br J Sports Med. 2021;55(9):501–509. " + ext("https://pure.eur.nl/en/publications/effectiveness-of-progressive-tendon-loading-exercise-therapy-in-p/", "Özet") + "; program ayrıntıları: " + ext("https://www.physiotutors.com/research/progressive-tendon-loading-vs-eccentric-exercise", "Physiotutors") + ".",
 "Challoumas D, Pedret C, Biddle M, et al. " + ext("https://bmjopensem.bmj.com/content/7/4/e001110", "Management of patellar tendinopathy: a systematic review and network meta-analysis of randomised studies") + ". BMJ Open Sport Exerc Med. 2021;7(4):e001110",
 "NHS Borders. " + ext("https://rightdecisions.scot.nhs.uk/patient-information-leaflets/primary-community-services/physiotherapy/patellar-tendinopathy-a-guide-for-patients", "Patellar tendinopathy – a guide for patients") + ". Last reviewed 1 November 2024.",
 "NHS. " + ext("https://www.nhs.uk/conditions/knee-pain/", "Knee pain") + ". Page last reviewed 21 December 2023.",
]

JK_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Atlet dizi (patellar tendinopati)</h1>
    <p class="lede">Atlet dizi, diz kapağının hemen altındaki kirişte (patellar tendon) aşırı yüklenmeyle ortaya çıkan ağrıdır. Voleybol ve basketbol gibi sıçrama gerektiren sporlarda sık görülür, ama sporcu olmayanlarda da olabilir. Tek başına dinlenmek çoğu zaman yetmez; tedavinin temeli, kirişi aşama aşama yeniden yüke alıştıran egzersizlerdir.</p>
    <p class="meta">Son güncelleme: 11 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%45</b><span>Norveç’te elit voleybolcularda atlet dizi sıklığı; basketbolda %32</span></div>
        <div class="stat"><b>613 sporcu</b><span>Dokuz spor dalında incelendi; genel sıklık %14, bisiklette ve oryantiringde hiç görülmedi</span></div>
        <div class="stat"><b>28 / 18 puan</b><span>24 haftada iyileşme: aşamalı yüklenme ve yalnızca eksantrik egzersiz grupları (100 puanlık ölçek)</span></div>
        <div class="stat"><b>10 üzerinden 3</b><span>Bir sonraki egzersiz aşamasına geçmek için tek bacak çömelmede kabul edilen en yüksek ağrı</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Diz kapağının hemen altında ağrı.</li>
          <li>Diz kapağının altında ya da üstünde şişlik.</li>
          <li>Çömelirken, yokuş ya da merdiven inerken ağrı.</li>
        </ul>
        <p class="soft">Tanı genellikle şikâyetler ve muayeneyle konur; çoğu zaman görüntüleme gerekmez.</p>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Kirişe gelen aşırı yük: çok yürümek, yokuş aşağı koşmak.</li>
          <li>Tekrarlayan çömelme ve sıçrama.</li>
          <li>Uyluğun ön kasında, bazen de kalça kaslarında güçsüzlük.</li>
          <li>En sık gençlik ile otuzlu yaşlar arasında görülür, ama her yaşta olabilir.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Aşamalı yüklenme</h2>
        <p class="soft">Hollanda’da 76 hastayla yapılan bir çalışmada, katılımcıların çoğunun ağrısı yaklaşık iki yıldır sürüyordu. Yarısı dört aşamalı bir programa, yarısı yalnızca eğimli zeminde yavaş inişli (eksantrik) çömelmeye ayrıldı. 24 hafta sonra aşamalı programdaki grup daha fazla iyileşti; spora dönüş oranı %43’e karşı %27 idi, ancak bu fark istatistiksel olarak anlamlı değildi.</p>
      </div>
      <div>
        <h2>Programın dört aşaması</h2>
        <ul class="dots">
          <li>Kası hareket ettirmeden kasma: duvarda bekleme gibi, 45 saniye, 5 kez.</li>
          <li>Yavaş kuvvet egzersizleri: hamle, basamak çıkma ya da makinede bacak itme.</li>
          <li>Sıçrama, koşu ve yön değiştirme.</li>
          <li>Spora özgü antrenman.</li>
        </ul>
        <p class="soft">Bir sonraki aşamaya, tek bacak çömelmede ağrı 10 üzerinden 3 ya da altındaysa ve mevcut aşama en az bir hafta yapıldıysa geçildi.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Yükü ayarlayın</h3><p>Koşu, sıçrama, uzun ve yokuşlu yürüyüş gibi ağrıyı artıran etkinlikleri azaltabilirsiniz. Kiriş iyileşmek için yüke ihtiyaç duyar, fazlası ise ağrıyı artırır.</p></div>
        <div class="kind"><span class="n">2</span><h3>Ağrıyı izleyin</h3><p>Egzersiz sırasında ağrının 10 üzerinden 3’ü geçmemesine dikkat edebilirsiniz. Bir egzersiz ağrısız hâle gelince bir sonrakine geçin.</p></div>
        <div class="kind"><span class="n">3</span><h3>Buz</h3><p>Havluya sardığınız buzu 10–15 dakika, günde 2–3 kez uygulayabilirsiniz.</p></div>
        <div class="kind"><span class="n">4</span><h3>Bant ve ağrı kesici</h3><p>Diz kapağının altına takılan atlet dizi bandı kirişin yükünü azaltabilir. Uygun ağrı kesiciyi eczacınıza sorabilirsiniz.</p></div>
      </div>
      <p class="soft" style="margin-top:18px">Diz kapağının çevresindeki ağrı için <a href="diz-onu-agrisi.html">diz önü ağrısı</a>, topuğun üstündeki kiriş ağrısı için <a href="asil-tendinopatisi.html">Aşil tendinopatisi</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Kirişi güçlendiren altı egzersiz</h2>
      <p class="soft">Sırayla ilerleyin: bir egzersiz ağrısız hâle gelmeden bir sonrakine geçmeyin. Egzersiz sırasında ağrı 10 üzerinden 3’ü geçmemeli.</p>
      {ex_grid(["pt_iso", "quad", "kext", "bridge", "pf_wall", "pt_sls"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(JK_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Ağrı birkaç haftada düzelmiyorsa</li>
        <li>Diz çok ağrılıysa, dizinizi hareket ettiremiyor ya da üzerine basamıyorsanız</li>
        <li>Diz çok şiştiyse ya da şekli değiştiyse</li>
        <li>Diz kilitleniyor, boşalıyor ya da ağrılı biçimde tıklıyorsa</li>
        <li>Yüksek ateş, titreme ya da dizde kızarıklık ve sıcaklık varsa</li>
      </ul>
      {CTA_CARD("Diz ağrınız", "atlet dizi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(JK_SRC)}
    </div>
  </section>
</main>'''

page("atlet-dizi.html", "Atlet Dizi (Patellar Tendinopati)",
     "Diz kapağının altında, sıçrarken ve merdiven inerken artan ağrı: atlet dizi neden olur, aşamalı yüklenme programı nasıl uygulanır? Belirtiler, öneriler ve evde altı egzersiz.",
     "atlet-dizi.html", NECK_CSS, JK_BODY, "",
     seo_title="Atlet Dizi (Patellar Tendinopati): Egzersiz ve Tedavi | İhsan Eren",
     condition="Patellar tendinopati (atlet dizi)", faq_items=JK_FAQ)
