p="site/index.html"; s=open(p,encoding="utf-8").read()
def rep(old,new,cnt=1):
    global s
    assert s.count(old)==cnt,(old[:70],s.count(old)); s=s.replace(old,new)
# hızlı test: başlık + yaş 18
rep('<h3>Bedeniniz kaç yaşında gösteriyor?</h3>','<h3>Gerçek yaşınız kaç?</h3>')
rep('<div class="qt-val"><span id="qt-age-v">45</span><small>yaş</small></div>\n            <input type="range" id="qt-age" min="18" max="90" step="1" value="45" aria-label="Yaşınız">',
    '<div class="qt-val"><span id="qt-age-v">18</span><small>yaş</small></div>\n            <input type="range" id="qt-age" min="18" max="90" step="1" value="18" aria-label="Yaşınız">')
rep('<form id="qt-form" novalidate>','<form id="qt-form" novalidate autocomplete="off">')
rep("  age.oninput = function(){ $('qt-age-v').textContent = age.value; };",
    "  age.oninput = function(){ $('qt-age-v').textContent = age.value; }; age.oninput();")
# galeri: kare başına "Temsili görsel" yok; tek, dürüst giriş cümlesi
rep('<p class="eyebrow">Temsili görseller</p>\n        <h2>Uygulamalardan kareler</h2>\n        <p class="intro">Değerlendirme, tedavi ve egzersiz süreçlerinden temsili görseller.</p>',
    '<p class="eyebrow">Kareler</p>\n        <h2>Evde bir seansın hikâyesi</h2>\n        <p class="intro">Değerlendirmeden tedaviye, egzersizden takibe: evde bir sürecin nasıl ilerlediğini anlatmak için hazırlanmış görseller.</p>')
for a,b in [("'Temsili görsel: “İntörn Doktor · Fizyoterapist” isimlikli çalışma masası'","'“İntörn Doktor · Fizyoterapist” isimlikli çalışma masası'"),
            ("'Temsili görsel: sırtta kuru iğneleme'","'Sırtta kuru iğneleme'"),
            ("'Temsili görsel: dizde manuel terapi'","'Dizde manuel terapi'"),
            ("'Temsili görsel: bacağa elektroterapi'","'Bacağa elektroterapi'"),
            ("'Temsili görsel: omurga maketiyle anlatım'","'Omurga maketiyle anlatım'"),
            ("'Temsili görsel: lastik bantla egzersiz'","'Lastik bantla egzersiz'"),
            ("'Temsili görsel: kavrama gücü ölçümü'","'Kavrama gücü ölçümü'")]:
    rep(a,b)
rep('<p>Logo tescillidir. Galerideki görseller temsilidir.</p>','<p>Logo tescillidir.</p>')
# iletişim: numara yok, sıcak bir başlık
rep('''          <p class="eyebrow">Bilgi ve iletişim</p>
          <a class="phone" href="tel:+905538815568">0553 881 55 68</a>
          <p class="sub">Arayın ya da WhatsApp'tan yazın. İstanbul içinde evde fizyoterapi hizmeti.</p>''',
'''          <p class="eyebrow">Bilgi ve iletişim</p>
          <h2 class="hello">Hikâyenizi dinleyerek başlayalım.</h2>
          <p class="sub">Ne yaşadığınızı, neyi yeniden yapabilmek istediğinizi bir mesajla anlatın; size en kısa sürede dönüş yapayım. İstanbul içinde evde fizyoterapi hizmeti.</p>''')
rep(".phone{font-family:var(--display);font-size:clamp(34px,8vw,52px);line-height:1.05;color:var(--foil);text-decoration:none;display:inline-block;margin:6px 0 8px;font-variant-numeric:tabular-nums}",
    ".hello{font-size:clamp(30px,6vw,46px);line-height:1.12;color:var(--foil);margin:8px 0 12px;max-width:18ch}")
rep('<a class="cta ghost" href="mailto:ihsneren@gmail.com">ihsneren@gmail.com</a>',
    '<a class="cta ghost" href="mailto:ihsneren@gmail.com">E-posta gönderin</a>')
# FAB: arama düğmesi yok
i=s.index('  <a class="call" href="tel:+905538815568"'); j=s.index('</a>\n',i)+5; s=s[:i]+s[j:]
for l in ['  .fab .call{width:44px;background:var(--foil);color:var(--ground)}\n','  .fab .call:active{background:var(--gold)}\n','  .fab .call svg{width:20px;height:20px}\n']:
    rep(l,'')
assert 'tel:' not in s and '0553 881' not in s
# kaldırılan "Uyguladığım yöntemler" bölümünün artık kullanılmayan stilleri
i=s.index("  .methods{margin-top:40px}"); j=s.index("  .m .tag:hover{text-decoration:underline}\n",i)+len("  .m .tag:hover{text-decoration:underline}\n")
s=s[:i]+s[j:]
# galeri: dikey kare (kavrama gücü ölçümü) yatay kutuda kırpılırken yüz görünsün
rep("  .tile.big{grid-row:span 2;grid-column:span 2}",
    "  .tile.big{grid-row:span 2;grid-column:span 2}\n  .tile img[src*=\"p03\"]{object-position:50% 18%}")
open(p,"w",encoding="utf-8").write(s)
print("ok")
