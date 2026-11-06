f="cond7_part.py"; s=open(f,encoding="utf-8").read()
K=("ACL_BODY = f'''",'page("on-capraz')
k=s.index(K[0]); e=s.index(K[1],k); b=s[k:e]
while "\n\n" in b.rstrip(): b=b.rstrip().replace("\n\n","\n")+"\n\n"
s=s[:k]+b+s[e:]
def R(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
def RB(a,b):
    global s
    k=s.index(K[0]); e=s.index(K[1],k); t=s[k:e]
    assert t.count(a)==1,(a[:90],t.count(a)); s=s[:k]+t.replace(a,b)+s[e:]
def SID(h2,sid):
    global s
    a=s.index(K[0]); key=f"<h2>{h2}</h2>"; i=s.index(key,a); j=s.rfind("<section",0,i); e=s.index(">",j)
    assert s[j:e+1]=="<section>",(h2,s[j:e+1]); s=s[:j]+f'<section id="{sid}">'+s[e+1:]

R('''ACL_BODY = f\'\'\'<header class="page">''','''ACL_TL = [
 ("1850", "Stark, ön çapraz bağ yırtığı olan iki hastayı anlatan bir yazı yayımladı; iki hasta da ameliyatsız tedavi edilmişti."),
 ("1895", "Mayo Robson, yırtık bağı uyluk kemiğine dikerek ilk başarılı onarımı yaptı (1903'te yayımlandı)."),
 ("1917", "Hey-Groves, bağın yerine uyluğun dış yanındaki zar dokusundan (fasya lata) alınan bir parçayla yeniden yapım tarif etti."),
 ("1963", "Jones, diz kapağı kirişinin orta üçte birini kemik parçasıyla birlikte kullanan yöntemi tarif etti; bugünkü kemik-kiriş-kemik greftlerinin öncüsü oldu."),
 ("1980'ler", "Artroskopinin yaygınlaşmasıyla ameliyat küçük kesilerle yapılmaya başlandı."),
 ("2006", "28 çalışmayı birleştiren bir meta-analiz (JOSPT): Lachman testi ön çapraz bağ yırtığını göstermede en geçerli muayene testi olarak öne çıktı."),
 ("2013", "121 genç ve aktif yetişkinle yapılan çalışmanın 5 yıllık sonuçları (BMJ): erken ameliyat ile önce rehabilitasyon, gerekirse sonradan ameliyat arasında fark yoktu; rehabilitasyonla başlayanların %51'i ameliyat olmuştu."),
 ("2014", "69 çalışmayı (7.556 kişi) birleştiren derleme (BJSM): ameliyat olanların %81'i bir spora, %65'i yaralanma öncesi düzeyine, %55'i yarışma düzeyinde spora döndü."),
 ("2016", "Delaware-Oslo izlem çalışması (BJSM): spora dönüş ölçütlerini geçemeden dönenlerin %38'i dizini yeniden yaraladı, geçenlerde bu oran %5,6 idi; dönüşün her ay ertelenmesi ilk 9 ayda yeniden yaralanmayı %51 azalttı."),
 ("2018", "Sekiz meta-analizin ortak sonucu (J Orthop Res): ısınmaya eklenen önleme egzersizleri ön çapraz bağ yaralanmalarını yaklaşık yarı yarıya azaltıyor."),
 ("2021", "167 hastalık COMPARE çalışması (BMJ): erken ameliyat 2. yılda diz puanını biraz daha yükseltti, ama fark klinik açıdan önemli bulunmadı; rehabilitasyonla başlayanların yarısı ameliyat olmadı."),
 ("2022", "Yaralanmanın üzerinden zaman geçmiş ve dizi boşalan 316 hastayla yapılan ACL SNNAP çalışması (Lancet): ameliyat 18. ayda rehabilitasyondan daha iyi sonuç verdi."),
]

ACL_BODY = f\'\'\'<header class="page">''')
RB('''<p class="meta">Son güncelleme: 7 Ekim 2026</p>''','''<p class="meta">Son güncelleme: 6 Kasım 2026</p>''')
RB('''<div class="stat"><b>%50</b><span>Isınmaya eklenen önleme egzersizleriyle ön çapraz bağ yaralanmalarındaki azalma</span></div>
      </div>''','''<div class="stat"><b>%50</b><span>Isınmaya eklenen önleme egzersizleriyle ön çapraz bağ yaralanmalarındaki azalma</span></div>
      </div>
      {g_toc([("nedir", "Nedir?"), ("tani", "Nasıl tanınır?"), ("ameliyat", "Ameliyat mı, rehabilitasyon mu?"), ("tarihce", "Geçmişten bugüne"), ("tedavi", "Tedavi"), ("egzersizler", "Egzersizler"), ("videolar", "Videolar"), ("sss", "Sık sorulan sorular"), ("uyari", "Uyarı işaretleri")])}''')
RB('''  <section>
    <div class="wrap">
      <h2>Ameliyat mı, rehabilitasyon mu?</h2>''','''  <section id="tani">
    <div class="wrap">
      <h2>Nasıl tanınır?</h2>
      <p class="soft">Tanı öykü ve muayeneyle konur. 28 çalışmayı birleştiren bir meta-analiz (JOSPT, 2006), muayene testlerinin doğruluğunu karşılaştırdı. Bu testler hekim ya da fizyoterapist tarafından yapılır.</p>
      <div class="kinds">
        <div class="kind"><h3>Lachman testi</h3><p>Diz hafif bükülüyken kaval kemiği öne doğru çekilir. Yırtıkların yaklaşık %85'ini yakalıyor (duyarlılık), sağlam bağda büyük olasılıkla olumsuz çıkıyor (özgüllük %94); yazarlar bu testi en geçerli test olarak öneriyor.</p></div>
        <div class="kind"><h3>Pivot shift testi</h3><p>Olumlu çıktığında yırtığı güçlü şekilde destekliyor (özgüllük %98), ama yırtıkların ancak dörtte birini yakalıyor (duyarlılık %24); olumsuz çıkması yırtığı dışlamaz.</p></div>
        <div class="kind"><h3>Ön çekmece testi ve MR</h3><p>Ön çekmece testi eski yaralanmalarda iyi sonuç veriyor (duyarlılık %92, özgüllük %91), yeni yaralanmalarda ise zayıf kalıyor. MR, menisküs ve diğer bağlar gibi eşlik eden yaralanmaları gösterir.</p></div>
      </div>
    </div>
  </section>
  <section id="ameliyat">
    <div class="wrap">
      <h2>Ameliyat mı, rehabilitasyon mu?</h2>''')
RB('''  <section>
    <div class="wrap">
      <h2>Tedavi</h2>''','''  <section id="tarihce">
    <div class="wrap">
      <p class="eyebrow">Geçmişten bugüne</p>
      <h2>Dikişten yeniden yapıma, ameliyattan kişiye özel karara</h2>
      <p class="soft">Ön çapraz bağ cerrahisi yüz yılı aşkın sürede dikişten kiriş parçasıyla yeniden yapıma ve artroskopiye uzandı. Son on beş yılın çalışmaları ise her yırtığın ameliyat gerektirmediğini ve spora dönüşte ölçümün önemini gösterdi.</p>
      {g_tl(ACL_TL)}
      <h3 class="g-h3">Çalışmalar yan yana</h3>
      <p class="soft">Bu sayfada sözü edilen çalışmaların temel bulguları. Sonuçlar yaralanmanın ne kadar yeni olduğuna, dizin boşalıp boşalmadığına ve kişinin hedeflerine göre değişiyor; karar kişiye özeldir.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Yeni yaralanma, genç ve aktif yetişkin</h3><dl><dt>KANON (BMJ, 2013)</dt><dd>121 kişi, 5 yıl: erken ameliyat ile önce rehabilitasyon arasında diz şikâyetleri ve işlevi açısından fark yok; rehabilitasyonla başlayanların %51'i ameliyat oldu.</dd><dt>COMPARE (BMJ, 2021)</dt><dd>167 hasta, 2 yıl: erken ameliyatta diz puanı biraz daha yüksek (84,7'ye karşı 79,4), fark klinik açıdan önemli değil; rehabilitasyonla başlayanların yarısı ameliyat olmadı.</dd></dl></div>
        <div class="kind"><h3>Eski yaralanma, dizi boşalan hasta</h3><dl><dt>ACL SNNAP (Lancet, 2022)</dt><dd>316 hasta, 18 ay: ameliyat rehabilitasyondan daha iyi (diz puanı 73,0'a karşı 64,6); rehabilitasyon grubunun %41'i sonradan ameliyat oldu.</dd></dl></div>
        <div class="kind"><h3>Spora dönüş</h3><dl><dt>Delaware-Oslo (BJSM, 2016)</dt><dd>Ölçütleri geçmeden dönenlerde yeniden yaralanma %38, geçenlerde %5,6; ilk 9 ayda dönüşün her ay ertelenmesi riski %51 azalttı.</dd><dt>Derleme (BJSM, 2014)</dt><dd>%81 bir spora, %65 eski düzeyine, %55 yarışma düzeyinde spora döndü.</dd></dl></div>
        <div class="kind"><h3>Önleme</h3><dl><dt>J Orthop Res (2018)</dt><dd>Sekiz meta-analiz: ısınmaya eklenen denge, güç ve yere inme egzersizleri yaralanmaları yaklaşık yarı yarıya azaltıyor; verilerin çoğu kadın sporculardan.</dd></dl></div>
      </div>
    </div>
  </section>
  <section id="tedavi">
    <div class="wrap">
      <h2>Tedavi</h2>''')
SID("Nedir?","nedir"); SID("Sık sorulan sorular","sss"); SID("Ne zaman hemen başvurmalı?","uyari")
RB('''      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Yaralanmadan sonra dizin üzerine hiç basamama</li>
        <li>Dizde belirgin şekil bozukluğu</li>
        <li>Dizin kilitlenip açılmaması</li>
        <li>Ayakta ya da bacakta uyuşma, soğukluk ya da renk değişikliği (acil)</li>
        <li>Baldırda şişlik, ağrı ve kızarıklık</li>
        <li>Ameliyattan sonra ateş, yarada akıntı ya da artan kızarıklık</li>
      </ul>''','''      <p class="soft">Şu durumlarda beklemeden başvurun.</p>
      <p class="soft"><strong>Hemen 112'yi arayın ya da acil servise gidin:</strong></p>
      <ul class="dots redflags">
        <li>Ayakta ya da bacakta uyuşma, soğukluk ya da renk değişikliği</li>
        <li>Dizde belirgin şekil bozukluğu</li>
        <li>Baldırda şişlik, ağrı ve kızarıklıkla birlikte nefes darlığı ya da göğüs ağrısı (akciğere pıhtı atmış olabilir)</li>
      </ul>
      <p class="soft"><strong>Aynı gün:</strong></p>
      <ul class="dots redflags">
        <li>Yaralanmadan sonra dizin üzerine hiç basamama</li>
        <li>Dizin kilitlenip açılmaması</li>
        <li>Baldırda şişlik, ağrı ve kızarıklık (pıhtı olabilir)</li>
        <li>Ameliyattan sonra ateş, yarada akıntı ya da artan kızarıklık</li>
      </ul>
      <p class="soft"><strong>Birkaç gün içinde bir hekime:</strong></p>
      <ul class="dots redflags">
        <li>Yaralanmadan sonra hızla gelişen şişlik ve dizde güvensizlik hissi (bağ yırtığı açısından değerlendirilmesi gerekir)</li>
        <li>Rehabilitasyona rağmen dizin tekrar tekrar boşalması</li>
      </ul>''')
R('''ACL_SRC = [
''','''ACL_SRC = [
 "Benjaminse A, Gokeler A, van der Schans CP. " + ext("https://research.hanze.nl/en/publications/clinical-diagnosis-of-an-anterior-cruciate-ligament-rupture-a-met/", "Clinical diagnosis of an anterior cruciate ligament rupture: a meta-analysis") + ". J Orthop Sports Phys Ther. 2006;36(5):267-288.",
 "D'Ambrosi R, Meena A, Arora ES, Attri M, Schäfer L, Migliorini F. " + ext("https://atm.amegroups.org/article/view/114816/html", "Reconstruction of the anterior cruciate ligament: a historical view") + ". Ann Transl Med. 2023;11(10).",
''')
open(f,"w",encoding="utf-8").write(s); print("acl ok")
