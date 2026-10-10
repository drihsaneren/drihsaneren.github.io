# -*- coding: utf-8 -*-
# Yeni rehber (21): huzursuz bacak sendromu. cond20_part.py'den sonra exec edilir. Video yok.

_ex2("rl_walk", "walk", "Gün içinde yürüyüş", "Rahat ya da orta tempoda yürüyün; konuşabileceğiniz ama biraz zorlandığınız bir hız yeterli. Ağır egzersizi gece geç saatlere bırakmayın.", "Günde 20–30 dakika")
_ex2("rl_sts", "sts", "Sandalyeden kalkıp oturma", "Sağlam bir sandalyenin ön kısmına oturun. Hafifçe öne eğilip kollarınızı kullanmadan ayağa kalkın, sonra yavaşça oturun.", "10 tekrar, 2 set, haftada 3 gün")
_ex2("rl_heel", "heel2", "Topuk yükseltme", "Bir sandalyenin arkalığına tutunun. İki topuğunuzu yavaşça yerden kaldırın, kısa bir an bekleyip yavaşça indirin.", "12–15 tekrar, 2 set")
_ex2("rl_bridge", "bridge", "Köprü", "Sırtüstü yatın, dizleriniz bükülü. Kalçanızı sıkarak kaldırın, 3 saniye tutup yavaşça indirin.", "10–12 tekrar, 2 set")
_ex2("rl_calf", "calf", "Baldır esnetme", "Duvara dönük durun, bir bacağınızı geriye alın; arka topuğunuz yerde, dizi düz kalsın. Öndeki dizinizi bükerek baldırınızda gerginlik hissedene kadar öne eğilin.", "Her bacakla 30 saniye, 2 kez; akşam ve belirtiler başladığında")
_ex2("rl_soleus", "soleus", "Alt baldır esnetme", "Baldır esnetmesindeki gibi durun, bu kez arkadaki dizinizi de hafifçe bükün; gerginliği aşil tendonunun üstünde hissedersiniz.", "Her bacakla 30 saniye, 2 kez")

RL_FAQ = [
 ("Gebelikte huzursuz bacak olur mu?", "Evet, gebelikte sık görülür ve genellikle doğumdan sonra geçer. Demir eksikliği eşlik edebileceği için hekiminize söyleyin; gebelikte ilaç ve takviyeleri hekime danışmadan kullanmayın."),
 ("Demir hapını kendim başlayabilir miyim?", "Önce kan değerlerinize bakılması gerekir. Amerikan Uyku Tıbbı Akademisi'nin 2024 kılavuzu, huzursuz bacak sendromu olan herkesin demir değerlerinin ölçülmesini ve takviyenin bu değerlere göre verilmesini öneriyor. Gereksiz demir kullanımı zararlı olabilir."),
 ("Kahve ve alkol etkiler mi?", "Belirtileri artırabilirler. İngiltere Ulusal Sağlık Sistemi (NHS), öğleden sonra kafeinden ve yatmadan önceki 2 saat içinde alkolden kaçınmayı, sigarayı bırakmayı öneriyor."),
 ("Kramptan farkı nedir?", "Kramp, kasın ağrılı ve istem dışı kasılmasıdır ve genellikle kısa sürer. Huzursuz bacakta ise bacakları hareket ettirme dürtüsü ve rahatsız edici bir his vardır; dinlenirken başlar ve hareketle hafifler. Sinir hasarı (nöropati) da benzer belirtiler verebilir; ayırımı hekim yapar."),
]

RL_SRC = [
 "NHS. " + ext("https://www.nhs.uk/conditions/restless-legs-syndrome/", "Restless legs syndrome") + ". Page last reviewed 22 September 2025.",
 "Winkelman JW, Berkowski JA, DelRosso LM, et al. Treatment of restless legs syndrome and periodic limb movement disorder: an American Academy of Sleep Medicine clinical practice guideline. J Clin Sleep Med. 2024. doi:10.5664/jcsm.11390. Özet: " + ext("https://aasm.org/summary-of-new-clinical-practice-guideline-for-rls-and-plmd/", "AASM, Summary of new clinical practice guideline for RLS and PLMD") + ", 13 November 2024.",
 "HCPLive. " + ext("https://www.hcplive.com/view/aasm-updates-clinical-guidelines-restless-legs-syndrome", "AASM updates clinical guidelines for restless legs syndrome") + ". 22 November 2024.",
 "Aukerman MM, Aukerman D, Bayard M, Tudiver F, Thorp L, Bailey B. " + ext("https://www.jabfm.org/content/19/5/487.short", "Exercise and restless legs syndrome: a randomized controlled trial") + ". J Am Board Fam Med. 2006;19(5):487–493.",
]

RL_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Huzursuz bacak sendromu</h1>
    <p class="lede">Huzursuz bacak sendromu, bacakları hareket ettirmeye yönelik güçlü bir dürtüdür; çoğu zaman karıncalanma, zonklama ya da ağrı gibi rahatsız edici bir hisle birlikte gelir. Akşamları ve dinlenirken artar, hareket edince hafifler ve uykuyu bozabilir. Demir eksikliğinin düzeltilmesi, yaşam alışkanlıkları ve düzenli egzersiz tedavinin önemli parçalarıdır.</p>
    <p class="meta">Son güncelleme: 11 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>2024</b><span>Amerikan Uyku Tıbbı Akademisi'nin güncellenen tedavi kılavuzu: önce demir değerlendirmesi</span></div>
        <div class="stat"><b>Yılda %7–10</b><span>Dopamin ilaçlarıyla belirtilerin giderek ağırlaşması (augmentasyon) görülme sıklığı</span></div>
        <div class="stat"><b>%35–50</b><span>Aynı ilaçlarla 5 yılda augmentasyon gelişebilen hasta oranı</span></div>
        <div class="stat"><b>12 hafta</b><span>Haftada 3 gün egzersizin belirtileri azalttığı randomize çalışmanın süresi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Bacakları hareket ettirme dürtüsü</li>
          <li>Karıncalanma, zonklama, kaşıntı ya da ağrı gibi rahatsız edici his</li>
          <li>Dinlenirken, özellikle akşam ve gece artma</li>
          <li>Yürüyünce ya da esneyince hafifleme</li>
          <li>Uykuya dalmakta güçlük ve gece uyanmaları</li>
          <li>Bazen kollarda da benzer his</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <p class="soft">Çoğu zaman belirgin bir neden yoktur; beyindeki demir ve dopamin düzeyiyle ilişkili olduğu düşünülür. Ailede görülmesi riski artırır.</p>
        <ul class="tx">
          <li><b>Demir eksikliği</b><span>Düzeltilebilir bir neden; demir eksikliği anemisiyle ilişkilidir.</span></li>
          <li><b>Gebelik</b><span>Sık görülür, genellikle doğumdan sonra geçer.</span></li>
          <li><b>Böbrek hastalığı</b><span>Özellikle ileri böbrek yetmezliğinde.</span></li>
          <li><b>Bazı ilaçlar</b><span>Belirtileri başlatabilir ya da artırabilir; hekiminiz ilaçlarınızı gözden geçirebilir.</span></li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Kendiniz neler yapabilirsiniz?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Gün içinde hareket</h3><p>Gündüz düzenli egzersiz yapın. Ağır egzersizi ve büyük öğünleri gece geç saatlere bırakmayın.</p></div>
        <div class="kind"><span class="n">2</span><h3>Belirtiler başlayınca</h3><p>Yürüyün, bacaklarınızı esnetin ya da ovun. Okumak ya da bulmaca çözmek gibi dikkatinizi dağıtan bir şey yapın.</p></div>
        <div class="kind"><span class="n">3</span><h3>Uyku düzeni</h3><p>Her gün aynı saatte yatıp kalkın, gündüz uykusundan kaçının. Yatmadan önce ılık bir banyo ya da bacaklara sıcak uygulama deneyin.</p></div>
        <div class="kind"><span class="n">4</span><h3>Kafein, alkol, sigara</h3><p>Öğleden sonra kafeinli içecek almayın, yatmadan önceki 2 saat içinde alkolden kaçının ve sigarayı bırakın.</p></div>
      </div>
      <p class="soft" style="margin-top:18px">Uykunuzu düzenlemek için <a href="uyku.html">İyi uyku için</a>, akşam gevşemek için <a href="kas-gevsetme.html">Kas gevşetme</a> sayfasına bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi: 2024 kılavuzu ne diyor?</h2>
      <p class="soft">Amerikan Uyku Tıbbı Akademisi'nin 2024 kılavuzu tedavide önemli bir değişikliğe gitti: Uzun yıllar ilk seçenek olan dopamin ilaçları artık çoğu hastada rutin kullanım için önerilmiyor.</p>
      <ul class="tx">
        <li><b>Demir değerlendirmesi</b><span>Herkesin demir değerleri ölçülmeli ve takviye bu değerlere göre verilmeli. Damardan demir (ferrik karboksimaltoz) güçlü, ağızdan demir koşullu olarak öneriliyor.</span></li>
        <li><b>Gabapentin ve pregabalin</b><span>Güçlü öneri alan ilaçlar.</span></li>
        <li><b>Dopamin ilaçları</b><span>Pramipeksol, ropinirol, rotigotin ve levodopa çoğu hastada rutin kullanım için önerilmiyor. Bu ilaçlarla belirtiler zamanla daha erken başlayıp vücudun başka bölgelerine yayılabiliyor (augmentasyon); yılda %7–10 kişide görülüyor.</span></li>
        <li><b>Diğer seçenekler</b><span>Dikkatli opioid kullanımı ve her iki bacakta peroneal sinirin yüksek frekanslı uyarılması da koşullu olarak öneriliyor.</span></li>
      </ul>
      <div class="callout">
        <p>Kullandığınız ilacı kendi başınıza bırakmayın ya da dozunu değiştirmeyin; değişikliği hekiminizle planlayın. Belirtiler ilaca rağmen artıyorsa doz artırmak yerine hekiminize augmentasyonu sorun.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Egzersiz işe yarar mı?</h2>
        <p class="soft">ABD'de yapılan randomize bir çalışmada huzursuz bacak sendromu olan kişiler 12 hafta boyunca haftada 3 gün aerobik egzersiz ve bacak güçlendirme çalışması yaptı. Egzersiz grubunda belirtilerin şiddeti, egzersiz yapmayan gruba göre belirgin biçimde azaldı.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Çalışmaya 41 kişi alındı, 23'ü çalışmayı tamamladı; küçük bir çalışma.</li>
        <li>Egzersiz uyku ve genel sağlık için de yararlıdır.</li>
        <li>NHS de gün içinde düzenli egzersizi ve belirtiler başlayınca yürümeyi, esnemeyi ve masajı öneriyor.</li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Huzursuz bacaklar için altı hareket</h2>
      <p class="soft">Yürüyüş ve bacak güçlendirme hareketlerini gün içinde, haftada en az 3 gün yapın. Esneme hareketlerini akşam ve belirtiler başladığında kullanın. Ağır egzersizi yatmadan hemen önceye bırakmayın.</p>
      {ex_grid(["rl_walk", "rl_sts", "rl_heel", "rl_bridge", "rl_calf", "rl_soleus"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(RL_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Belirtiler uyumanızı engelliyorsa</li>
        <li>Ruh hâlinizi ya da gündüz yaşamınızı etkiliyorsa</li>
        <li>Kendi kendine uygulanan önlemlerle düzelmiyorsa</li>
        <li>Kullandığınız ilaca rağmen belirtiler daha erken başlıyor ya da yayılıyorsa</li>
        <li>Bacaklarda kalıcı uyuşma, güçsüzlük ya da tek taraflı şişlik ve ağrı varsa</li>
      </ul>
      {CTA_CARD("Huzursuz bacaklarınız için düzenli bir egzersiz programı", "huzursuz bacak sendromu")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(RL_SRC)}
    </div>
  </section>
</main>'''

page("huzursuz-bacak.html", "Huzursuz Bacak Sendromu",
     "Huzursuz bacak sendromu nedir, neden olur? Belirtiler, demir eksikliğinin rolü, 2024 tedavi kılavuzundaki değişiklikler, kendi yapabilecekleriniz ve altı egzersiz.",
     "huzursuz-bacak.html", NECK_CSS, RL_BODY, "",
     seo_title="Huzursuz Bacak Sendromu: Belirtiler, Demir, Tedavi ve Egzersiz | İhsan Eren",
     condition="Huzursuz bacak sendromu", faq_items=RL_FAQ)
