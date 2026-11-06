f="cond3_part.py"; s=open(f,encoding="utf-8").read()
K=("HA_BODY = f'''",'page("bas-agrisi')
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

R('''HA_BODY = f\'\'\'<header class="page">''','''HA_TL = [
 ("2002", "Boyun kaynaklı baş ağrısı olan 200 kişiyle yapılan çalışmada (Spine) 6 haftalık manuel terapi de, boyun ve kürek kemiği kaslarına yönelik özel egzersizler de baş ağrısının sıklığını ve şiddetini azalttı; etki 12 ay sonra da sürüyordu."),
 ("2012", "İngiltere'nin ulusal sağlık kılavuzu kurumu NICE baş ağrısı kılavuzunu yayımladı: gerilim tipi baş ağrısında opioid önerilmedi; ayda 15 gün ve üzeri süren gerilim tipi baş ağrısında 10 seansa kadar bir akupunktur kürü önerilebileceği belirtildi."),
 ("2017", "Amerikan Fizyoterapi Derneği'nin (APTA) ortopedi biriminin boyun ağrısı kılavuzu (JOSPT): baş ağrısıyla birlikte boyun ağrısında egzersizlerin ve manuel terapinin yeri tanımlandı."),
 ("2018", "Uluslararası Baş Ağrısı Derneği'nin sınıflamasının 3. baskısı (ICHD-3) yayımlandı; gerilim tipi ve boyun kaynaklı baş ağrısının tanı ölçütleri bugün bu sınıflamaya dayanıyor."),
 ("2022", "Egzersiz türlerini karşılaştıran bir meta-analiz (J Pain): migren ve gerilim tipi baş ağrısında egzersizin etkisi incelendi; gerilim tipi baş ağrısında kanıtın kesinliği düşük kaldı."),
]

HA_BODY = f\'\'\'<header class="page">''')
RB('''<p class="meta">Son güncelleme: 30 Eylül 2026</p>''','''<p class="meta">Son güncelleme: 6 Kasım 2026</p>''')
RB('''<div class="stat"><b>15 gün</b><span>Ayda bu kadar ve daha fazla gün süren baş ağrısı kronik kabul edilir</span></div>
      </div>''','''<div class="stat"><b>15 gün</b><span>Ayda bu kadar ve daha fazla gün süren baş ağrısı kronik kabul edilir</span></div>
      </div>
      {g_toc([("turler", "Baş ağrınız hangi türde?"), ("tani", "Tanı ölçütleri"), ("fizyoterapi", "Egzersiz ve fizyoterapi"), ("tarihce", "Geçmişten bugüne"), ("egzersizler", "Egzersizler"), ("videolar", "Videolar"), ("sss", "Sık sorulan sorular"), ("uyari", "Uyarı işaretleri")])}''')
RB('''  <section>
    <div class="wrap">
      <h2>Egzersiz ve fizyoterapi ne sağlar?</h2>''','''  <section id="tani">
    <div class="wrap">
      <h2>Tanı ölçütleri (ICHD-3)</h2>
      <p class="soft">Baş ağrısının türü, Uluslararası Baş Ağrısı Derneği'nin sınıflamasına (ICHD-3) göre belirlenir. Tanıyı hekim koyar; aşağıdaki ölçütler türler arasındaki farkı anlamanıza yardımcı olmak içindir.</p>
      <div class="kinds">
        <div class="kind"><h3>Sık tekrarlayan gerilim tipi</h3><p>3 aydan uzun süredir ayda ortalama 1–14 gün, en az 10 atak; her atak 30 dakika ile 7 gün arası sürer. Şu dört özellikten en az ikisi: iki taraflı, sıkıştırıcı ya da baskı şeklinde (zonklamayan), hafif ya da orta şiddette, yürüme ya da merdiven çıkma gibi günlük hareketlerle artmayan. Bulantı ya da kusma olmaz; ışığa ya da sese hassasiyetten en fazla biri bulunur.</p></div>
        <div class="kind"><h3>Boyun kaynaklı</h3><p>Boyunda bir sorunun muayene ya da görüntülemeyle gösterilmesi ve şunlardan en az ikisi: ağrının boyun sorunuyla birlikte başlaması; boyun sorunu düzeldikçe ağrının da düzelmesi; boyun hareketlerinin kısıtlı olması ve zorlayıcı hareketlerle ağrının belirgin artması; boyundaki bir yapıya yapılan tanısal iğneyle ağrının geçmesi.</p></div>
        <div class="kind"><h3>Ayırt etmeye yardımcı ipuçları</h3><p>Tek taraflı ağrı, boyun kaslarına bastırınca ya da baş hareketleriyle tanıdık ağrının ortaya çıkması ve ağrının başın arkasından öne doğru yayılması boyun kaynaklı baş ağrısını düşündürür; ancak bu özellikler tek başına tanı koydurmaz.</p></div>
      </div>
    </div>
  </section>
  <section id="fizyoterapi">
    <div class="wrap">
      <h2>Egzersiz ve fizyoterapi ne sağlar?</h2>''')
RB('''  <section id="egzersizler">''','''  <section id="tarihce">
    <div class="wrap">
      <p class="eyebrow">Geçmişten bugüne</p>
      <h2>Ölçütler ve kılavuzlar</h2>
      <p class="soft">Baş ağrısı türlerinin tanımı uluslararası sınıflamayla netleşti; boyun kaynaklı baş ağrısında egzersiz ve manuel terapinin yeri de son yirmi yılın çalışmalarıyla şekillendi.</p>
      {g_tl(HA_TL)}
      <h3 class="g-h3">Tedavi seçenekleri: kılavuzlar ne diyor?</h3>
      <p class="soft">İngiltere'nin NICE baş ağrısı kılavuzu (2012) ile Amerikan Fizyoterapi Derneği'nin boyun ağrısı kılavuzu (JOSPT, 2017) yan yana. NICE gerilim tipi baş ağrısını, JOSPT boyun kaynaklı baş ağrısını ele alıyor; tedavi kişiye göre seçilir.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Gerilim tipi baş ağrısında ilaç</h3><dl><dt>NICE</dt><dd>Hekim bir ağrı kesici önerebilir; opioidler önerilmiyor. 16 yaşın altındakilere aspirin verilmemeli.</dd><dt>Not</dt><dd>Hangisinin uygun olduğunu hekiminize sorun.</dd></dl></div>
        <div class="kind"><h3>Sık gerilim tipi baş ağrısını önleme</h3><dl><dt>NICE</dt><dd>Ayda 15 gün ve üzeri gerilim tipi baş ağrısında 10 seansa kadar bir akupunktur kürü önerilebilir.</dd><dt>Not</dt><dd>Türkiye'de akupunkturu yalnızca yetkili hekimler uygulayabilir.</dd></dl></div>
        <div class="kind"><h3>Boyun kaynaklı baş ağrısı</h3><dl><dt>JOSPT</dt><dd>Yeni başlayan ağrıda gözetimli aktif hareket egzersizleri ve üst boyun için kendi kendine yapılan hareketlendirme (C1–C2 SNAG); uzun süren ağrıda boyun ya da boyun-sırt manipülasyonu veya mobilizasyonu, omuz kuşağı ve boyun kaslarına germe, güçlendirme ve dayanıklılık egzersizleriyle birlikte.</dd></dl></div>
      </div>
    </div>
  </section>
  <section id="egzersizler">''')
SID("Baş ağrınız hangi türde?","turler"); SID("Sık sorulan sorular","sss"); SID("Ne zaman hemen başvurmalı?","uyari")
RB('''        <li>Öksürme, ıkınma ya da eğilmeyle belirgin artan, sabahları kusmayla uyandıran baş ağrısı</li>
      </ul>''','''        <li>Öksürme, ıkınma ya da eğilmeyle belirgin artan, sabahları kusmayla uyandıran baş ağrısı</li>
      </ul>
      <p class="soft"><strong>Birkaç gün içinde bir hekime:</strong></p>
      <ul class="dots redflags">
        <li>Baş ağrınızın özellikleri ya da sıklığı belirgin şekilde değiştiyse</li>
        <li>Ağrı kesicilere ayda 10–15 günden fazla ihtiyaç duyuyorsanız</li>
        <li>Ayda 15 gün ve üzeri baş ağrısı yaşıyorsanız</li>
      </ul>''')
R('''HA_SRC = [
''','''HA_SRC = [
 "Headache Classification Committee of the International Headache Society. " + ext("https://ichd-3.org/2-tension-type-headache/2-2-frequent-episodic-tension-type-headache/", "ICHD-3: 2.2 Frequent episodic tension-type headache") + "; " + ext("https://ichd-3.org/11-headache-or-facial-pain-attributed-to-disorder-of-the-cranium-neck-eyes-ears-nose-sinuses-teeth-mouth-or-other-facial-or-cervical-structure/11-2-headache-attributed-to-disorder-of-the-neck/11-2-1-cervicogenic-headache", "11.2.1 Cervicogenic headache") + ".",
 "NICE. " + ext("https://www.nice.org.uk/guidance/CG150/ifp/chapter/Treatments-for-tensiontype-headache", "Treatments for tension-type headache (CG150, information for the public)") + ".",
''')
open(f,"w",encoding="utf-8").write(s); print("ha ok")
