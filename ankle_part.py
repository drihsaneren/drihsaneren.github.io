# -*- coding: utf-8 -*-
# Ayak bileği burkulması sayfası. osteo_part.py'den sonra exec edilir.

# Lastik bantla ayağı dışa çevirme (yukarıdan görünüm)
SV["evert"] = fig(
    '<path class="fig" d="M60 6 L60 66"/>'
    f'<g>{anim_t("0 60 70;-28 60 70;0 60 70", typ="rotate")}'
    '<rect x="52" y="64" width="16" height="42" rx="8" fill="#2A6F6B"/><circle cx="60" cy="104" r="3" fill="#C8963E"/></g>'
    f'<path class="band" d="M20 112 L60 104">{anim_d("M20 112 L60 104;M20 112 L80 100;M20 112 L60 104")}</path>'
    '<circle cx="18" cy="112" r="4" fill="#8FA8A2"/>'
    '<path d="M90 90 A30 30 0 0 0 96 70" fill="none" stroke="#C8963E" stroke-width="2.5" stroke-dasharray="3 4" stroke-linecap="round"/>',
    "Bantla ayağı dışa çevirme")

SV["apump2"] = SV["apump"]
SV["towelst2"] = SV["towelst"]
SV["heel4"] = SV["heel"]
SV["sls3"] = SV["sls"]
SV["tandem2"] = SV["tandem"]

EXT.update({
 "apump2": ("Ayak bileği pompası ve daireler", "Oturun ya da uzanın, bacağınız düz olsun. Ayak ucunuzu kendinize doğru çekin ve aşağı itin; sonra ayak bileğinizle iki yöne daireler çizin. İlk günlerden itibaren şişliği azaltmaya ve hareketi korumaya yardım eder.", "Her yöne 10 tekrar, günde 3–4 kez"),
 "towelst2": ("Havluyla baldır germe", "Bacaklarınız düz oturun, havluyu ayağınızın ön kısmına dolayıp uçlarından tutun. Dizinizi düz tutarak havluyu kendinize doğru çekin; baldırınızda gerilme hissedin. Ağrısız aralıkta kalın.", "30 saniye, 3 tekrar"),
 "evert": ("Bantla ayağı dışa çevirme", "Oturun, lastik bandı ayağınızın ön kısmına dolayıp diğer ucunu karşı tarafta sabitleyin. Topuğunuz yerde kalacak şekilde ayağınızı dışa doğru çevirin, yavaşça geri getirin. Ayak bileğinin dış yanındaki kasları güçlendirir.", "10–15 tekrar, 2–3 set"),
 "heel4": ("Topuk yükseltme", "Tezgâha tutunarak iki ayağınızla parmak uçlarınızda yükselin, yavaşça inin. Kolaylaştıkça yalnızca burkulan ayağınızla yapın.", "10–15 tekrar, 2–3 set"),
 "sls3": ("Tek ayak üzerinde durma", "Tezgâha yakın durup burkulan ayağınızın üzerinde dengede kalın. Kolaylaştıkça desteği bırakın, gözlerinizi kapatın ya da yastık gibi yumuşak bir zeminde deneyin. Yeni burkulmaları önlemenin temel egzersizidir.", "30 saniye, 3–5 tekrar"),
 "tandem2": ("Topuk-parmak yürüyüşü", "Tezgâh ya da duvar boyunca, öndeki ayağınızın topuğunu arkadaki ayağınızın parmak uçlarının hemen önüne koyarak düz bir çizgide yürüyün.", "10–15 adım, 2–3 tur"),
})

BILEK_FAQ = [
 ("Burkulan ayağıma basmalı mıyım?", "Evet, ağrının izin verdiği ölçüde. Amerikan Fizyoterapi Derneği'nin kılavuzu, yeni burkulmada ayak bileğini bant ya da bileklik gibi bir destekle korumayı ve ayağa kademeli olarak yük vermeyi öneriyor. Uzun süre hiç basmamak iyileşmeyi geciktirebilir."),
 ("Röntgen çektirmem gerekir mi?", "Çoğu burkulmada gerekmez. Ottawa kurallarına göre, yaralanmadan hemen sonra ve muayenede 4 adım atamıyorsanız ya da ayak bileğinin iç veya dış kemik çıkıntısının arka kenarında, alttaki 6 santimlik bölümde kemik üzerinde hassasiyet varsa röntgen gerekir. Bu kurallar kırıkların neredeyse tamamını yakalıyor."),
 ("Buz mu uygulamalıyım?", "Egzersiz programıyla birlikte, aralıklı ve tekrarlayan buz uygulaması kılavuzda ağrı ve şişliği azaltmak için kullanılabilecek yöntemler arasında yer alıyor. Buzu doğrudan cilde koymayın, arada ince bir bez bulundurun."),
 ("Bileklik kullanmalı mıyım?", "Yeni burkulmada destek kullanmak önerilir. Burkulma geçirmiş kişilerde yeni burkulmaları önlemek için de spor sırasında bileklik kullanmak ve denge egzersizleri yapmak öneriliyor."),
 ("Neden sürekli aynı ayağımı burkuyorum?", "Burkulma sonrasında denge, kas gücü ve ayak bileğinin konum algısı tam olarak toparlanmadıysa bilek yeniden burkulmaya yatkın hale gelir. Ağrı geçse de denge ve güçlendirme egzersizlerine devam etmek ve spora kademeli dönmek bu döngüyü kırmanın yoludur."),
]

BILEK_SRC = [
 "Martin RL, et al. " + ext("https://www.jospt.org/doi/10.2519/jospt.2021.0302", "Ankle stability and movement coordination impairments: lateral ankle ligament sprains revision 2021. Clinical practice guidelines linked to the International Classification of Functioning, Disability and Health") + ". J Orthop Sports Phys Ther. 2021;51(4).",
 "Physiopedia. " + ext("https://www.physio-pedia.com/Ottawa_Ankle_Rules", "Ottawa Ankle Rules") + ".",
]

BILEK_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Ayak bileği burkulması</h1>
    <p class="lede">Ayak bileği çoğunlukla içe doğru burkulur ve dış yandaki bağlar zorlanır ya da yırtılır. Çoğu burkulma ameliyatsız iyileşir. Erken ve kademeli yük verme, egzersiz ve denge çalışmaları hem iyileşmeyi destekler hem de aynı bileğin yeniden burkulmasını önler.</p>
    <p class="meta">Son güncelleme: {UPDATED}</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>Erken yük</b><span>Destekle, kademeli olarak ayağa basmak önerilir</span></div>
        <div class="stat"><b>4 adım</b><span>Atılamıyorsa röntgen gerekebilir (Ottawa kuralları)</span></div>
        <div class="stat"><b>%97,6</b><span>Ottawa kurallarının kırığı atlamama başarısı (27 çalışma)</span></div>
        <div class="stat"><b>Denge</b><span>Yeni burkulmaları önlemenin temeli</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Ayak bileği içe doğru ani ve zorlu bir şekilde döndüğünde, dış kemik çıkıntısının önündeki ve altındaki bağlar gerilir ya da yırtılır. Ağrı, şişlik ve morarma olur; basmak zorlaşır.</p>
        <p class="soft">Burkulmadan sonra rehabilitasyon yarım kalırsa bilek yeniden burkulmaya yatkın hale gelebilir ve bazı kişilerde bilekte sık sık boşalma hissi (kronik instabilite) gelişebilir.</p>
      </div>
      <div>
        <h2>İlk günlerde</h2>
        <ul class="dots">
          <li>Bileği bant ya da bileklikle destekleyin, ağrının izin verdiği ölçüde basın.</li>
          <li>Gerekirse ilk günler koltuk değneği kullanın, ama kademeli olarak ayağa yük verin.</li>
          <li>Aralıklı buz uygulaması ve bacağı yükseltmek şişliği azaltmaya yardım eder.</li>
          <li>Ayak bileği pompasıyla hareketi erkenden koruyun.</li>
          <li>Ağrı kesici gerekiyorsa hekiminize danışın.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Röntgen gerekir mi?</h2>
      <p class="soft">Çoğu burkulmada kırık yoktur ve röntgen gerekmez. Ottawa ayak bileği kuralları, röntgen gereken hastaları ayırmak için geliştirildi ve 27 çalışmanın birleştirildiği bir derlemede kırıkların %97,6'sını yakaladı.</p>
      <div class="callout">
        <p>Ayak bileği bölgesinde ağrıyla birlikte şunlardan biri varsa röntgen gerekir: iç ya da dış kemik çıkıntısının arka kenarında, alttaki 6 santimlik bölümde ya da ucunda kemik üzerinde hassasiyet; yaralanmadan hemen sonra ve muayenede 4 adım atamamak.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <p class="soft">Amerikan Fizyoterapi Derneği'nin 2021 kılavuzu burkulma sonrası tedaviyi şu başlıklarda topluyor.</p>
      <ul class="tx">
        <li><b>Koruma ve kademeli yük</b><span>Bant ya da bileklik gibi dış destekle ayak bileğini korumak ve ayağa kademeli olarak yük vermek önerilir.</span></li>
        <li><b>Egzersiz</b><span>Hareket açıklığı, germe, kas-sinir kontrolü, duruş ve denge egzersizlerini içeren yapılandırılmış bir program önerilir.</span></li>
        <li><b>Manuel terapi</b><span>Lenf drenajı, yumuşak doku ve eklem mobilizasyonları ağrısız aralıkta uygulanır.</span></li>
        <li><b>Buz ve ilaç</b><span>Egzersizle birlikte aralıklı buz uygulaması ve hekim önerisiyle iltihap giderici ağrı kesiciler kullanılabilir.</span></li>
        <li><b>İşe ve spora dönüş</b><span>Rehabilitasyonun erken döneminden itibaren işe ve spora özgü çalışmalar planlanır; dönüşte bileklik kullanılabilir.</span></li>
        <li><b>Yeni burkulmaları önlemek</b><span>Burkulma geçirmiş kişilerde bileklik kullanmak ve denge odaklı egzersiz programı yapmak önerilir.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Ayak bileği için altı egzersiz</h2>
      <p class="soft">İlk iki egzersizle erken dönemde başlayabilirsiniz. Ağrı ve şişlik azaldıkça güçlendirme ve denge egzersizlerine geçin. Ayakta yapılan hareketlerde sağlam bir yere tutunun; keskin ağrı olursa durun.</p>
      {ex_grid(["apump2", "towelst2", "evert", "heel4", "sls3", "tandem2"])}
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Spora ve günlük hayata dönüş</h2>
        <p class="soft">Ağrının geçmesi, bileğin tamamen toparlandığı anlamına gelmez. Dönüşü kademeli yapmak yeni burkulmaları önler.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Önce düz zeminde yürüyün, sonra hafif koşuya, en son yön değiştirme ve zıplamalara geçin.</li>
        <li>Burkulan ayağınızın üzerinde rahatça dengede durabilmeden koşuya başlamayın.</li>
        <li>Spora dönüşte bir süre bileklik ya da bantla destek kullanın.</li>
        <li>Ağrı geçtikten sonra da denge egzersizlerine haftada birkaç kez devam edin.</li>
        <li>Engebeli zeminde ve karanlıkta dikkatli olun; topuğu destekleyen ayakkabılar giyin.</li>
      </ul>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Ayak bileği burkulması için videolar</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("JlImzKN7w-E", "Ayak bileği rehabilitasyon videosunu oynat", "REBUILD Your Ankles-Stop Pain &amp; Return To Action!")}
          <h3>Ayak bileğini yeniden güçlendirmek</h3>
          <p>Burkulma sonrası hareket ve güçlendirme çalışmaları.</p>
        </div>
        <div class="vid">
          {vbox("Zk1vdqlCFUI", "Ayak bileği güçlendirme videosunu oynat", "The 8 Best At-Home Ankle Strengthening Exercises")}
          <h3>Evde ayak bileği güçlendirme</h3>
          <p>Hareket açıklığı kazanıldıktan sonra yapılacak güçlendirme egzersizleri.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(BILEK_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Yaralanmadan hemen sonra ve sonrasında 4 adım atamamak, kemik üzerinde belirgin hassasiyet (kırık olabilir)</li>
        <li>Ayak bileğinde şekil bozukluğu</li>
        <li>Topuğun arkasında "pat" sesiyle başlayan ağrı ve parmak ucunda yükselememe (aşil tendonu yırtığı olabilir)</li>
        <li>Ayakta uyuşma, soğukluk ya da renk değişikliği</li>
        <li>Baldırda şişlik, ağrı ve kızarıklık (pıhtı olabilir); ateş ve giderek artan kızarıklık</li>
      </ul>
      {CTA_CARD("Ayak bileği burkulmanız", "ayak bileği burkulması")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(BILEK_SRC)}
    </div>
  </section>
</main>'''

page("ayak-bilegi-burkulmasi.html", "Ayak Bileği Burkulması",
     "Ayak bileği burkulması: burkulan ayağa basılır mı, röntgen gerekir mi, buz uygulanmalı mı, neden tekrarlar? Evde altı egzersiz, spora dönüş önerileri, videolar ve uyarı işaretleri.",
     "ayak-bilegi-burkulmasi.html", NECK_CSS, BILEK_BODY, YT_JS,
     seo_title="Ayak Bileği Burkulması: İlk Günler, Egzersizler ve Spora Dönüş | İhsan Eren",
     condition="Ayak bileği burkulması", about=cond("Ayak bileği burkulması"),
     faq_items=pick(BILEK_FAQ, 0, 1, 3, 4))
