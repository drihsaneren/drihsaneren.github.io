# İÇERİK DENETİMİ — kayıt ve yöntem

Kullanıcı isteği (28 Ekim 2026): "bundan böyle düzenli denetleme çalışmaları istiyorum, lütfen çok dikkat et, sağlık sayfasıyız ve insanları yanıltıyorsun".

## Yöntem (her sayfa için)
1. Sayfa metni düz metne çıkarılır (scratchpad audit/<sayfa>.txt; SVG yerine [ÇİZİM]).
2. Sayfayı YAZMAMIŞ bağımsız bir denetçi (ayrı ajan) her sayı, yıl, isim, oran ve kılavuz önerisini kaynağından kontrol eder; ifade gücü, terim, hasta gözüyle anlaşılırlık, site kuralları ve iç tutarlılığa bakar. Uzun sayfalar ikiye bölünür.
3. Her bulgu kaynağına bakılarak ayrıca doğrulanır (denetçi de yanılabilir); yalnızca doğrulanan bulgular düzeltilir.
4. Düzeltmeler TR+EN birlikte; testler (make_en eksik 0, check.py, t_ls 0, taşma) ve yayın.
5. Bu dosyadaki tabloya: tarih, bulgu sayısı (yüksek/orta/düşük), düzeltilenler, açık kalanlar.
6. Klinik deneyim kutuları kullanıcının gözlemidir: kaynak istenmez, ama araştırma gibi sunulmuşsa ya da araştırmayla çeliştiği söylenmiyorsa işaretlenir.
Kontrol listesi: DEVAM.md › İÇERİK KALİTE KONTROLÜ.

## Günlük zamanlanmış denetim (kullanıcı seçimi, 28 Ekim 2026)
Her gün 06:39 (İstanbul) yeni bir oturum açılır ve tablodaki öncelik sırasıyla "denetlenmedi" durumundaki ilk 3 sayfayı denetler. Kullanıcının seçimi: **kesin hatalar hemen düzeltilip yayımlanır, yorum gerektirenler kullanıcıya sorulur.**
1. Kurulum: `bash /home/claude/drihsaneren.github.io/denetim/kurulum.sh` (yoksa: repoyu klonla, `denetim/kurulum.sh`'i çalıştır). Sonra DEVAM.md (özellikle İÇERİK KALİTE KONTROLÜ ve kurallar) ve bu dosya okunur. Yerel sunucu: `cd /home/claude/main && python3 -m http.server 8765 --bind 127.0.0.1` (arka planda).
2. Her sayfa: `python3 denetim/sayfa_metni.py <sayfa>.html <scratchpad>/<sayfa>.txt` → her sayı/yıl/isim/oran/kılavuz önerisi kaynağından (WebFetch/WebSearch; PubMed engelliyse PMC, yayıncı, PEDro, kurum siteleri) kontrol edilir; ifade gücü, Türkçe terim, hasta gözüyle anlaşılırlık, site kuralları, iç tutarlılık, kaynak künyeleri ve bağlantılar, İngilizce sürümün anlam uyumu (göz atarak).
3. **Hemen düzeltilecek kesin hatalar:** kaynakla çelişen ya da kaynakta bulunmayan sayı/yıl/isim/oran; yanlış kuruma/çalışmaya atıf; gözlemsel çalışmanın nedensel anlatılması; çizimde anatomik hata; kırık ya da yanlış kaynak bağlantısı/künye; site kuralı ihlali (randevu, eczacı, doktor→hekim, ilaç/doz önerisi, telefon, akupunktur hizmeti vb.). Düzeltme TR+EN birlikte (collect_todo → i18n/done/turNN.json → check.py → make_en "toplam eksik: 0" → search_index → t_ls "sorun: 0" → denetim/sw.py taşma yok) ve iki dal push (önce `git fetch`).
4. **Kullanıcıya sorulacaklar (değiştirilmez):** klinik deneyim kutuları ve kullanıcının kendi terimleri/ifadeleri; içerik çıkarma ya da büyük ekleme; tartışmalı yorumlar; tasarım. Bunlar bu dosyaya "soruldu" diye yazılır.
5. Bu dosyaya: tablo satırı (durum, tarih, bulgu Y/O/D, not) + sayfa başına kısa bulgu/düzeltme özeti. Çeviri tur numarası DEVAM.md'deki "Sonraki batch" ile ilerletilir.
6. Bitişte kullanıcıya kısa Türkçe rapor (yumuşak "-ebilirsiniz" üslubu): denetlenen sayfalar, düzeltilen kesin hatalar (önce → sonra, kaynak), soruları, açık kalanlar. Kota sınırlıysa 3 yerine 2 sayfa yapılabilir; bu raporda söylenir.
Değişiklik/iptal: kullanıcı isterse zamanlanmış görev ayarlarından.

## Site geneli otomatik taramalar (her denetim turunda tekrarlanır)
randevu/appointment, eczacı/pharmacist, tel: bağlantısı, "eklem esnekliği", Biruni, YouTube'da izle/Spotify'da aç, LinkedIn, belirli ilaç adı + "kullanabilirsiniz", ana sayfada şehir adı.
- 28 Ekim 2026: temiz. Not: stres.html'deki iki "doktorunuza danışın" 28 Ekim'de "hekiminize danışın" yapıldı (tur34). Ayrıca: omuzda-kirec-birikmesi "Hekiminize danışarak ağrı kesici ya da iltihap giderici ilaç kullanabilirsiniz" → kural kalıbına çevrilecek (o sayfanın denetiminde). index.html'deki "randevu" yalnızca kod yorumu; 5. metatars EN'deki "appointment" kaynak URL'si.

## Sayfa durumu (öncelik sırasıyla; 1 = yüksek risk / çok okunan / çocuk / ilaç geçen)
| Öncelik | Sayfa | Başlık | Tür | Durum | Tarih | Bulgu (Y/O/D) | Not |
|---|---|---|---|---|---|---|---|
| 1 | skolyoz.html | Skolyoz | Hastalık rehberi | tamamlandı | 28 Ekim 2026 | A: 2/6/12, B: 1/9/14 | tümü düzeltildi (tur32–33); 2 madde açık, aşağıda |
| 1 | bel-fitigi.html | Bel fıtığı ve siyatik | Hastalık rehberi | denetlenmedi | | | |
| 1 | bel-agrisi.html | Bel ağrısı | Hastalık rehberi | denetlenmedi | | | |
| 1 | boyun-fitigi.html | Boyun fıtığı ve sinir sıkışması | Hastalık rehberi | denetlenmedi | | | |
| 1 | diz-kireclenmesi.html | Diz kireçlenmesi (osteoartrit) | Hastalık rehberi | denetlenmedi | | | |
| 1 | donuk-omuz.html | Donuk omuz (adeziv kapsülit) | Hastalık rehberi | denetlenmedi | | | |
| 1 | inme-rehabilitasyonu.html | İnme (felç) sonrası rehabilitasyon | Rehabilitasyon rehberi | denetlenmedi | | | |
| 1 | beyin-sarsintisi.html | Beyin sarsıntısı: iyileşme ve harekete kademeli dönüş | Hastalık rehberi | denetlenmedi | | | |
| 1 | kalp-rehabilitasyonu.html | Kalp rehabilitasyonu | Rehabilitasyon rehberi | denetlenmedi | | | |
| 1 | kalp-yetmezligi.html | Kalp yetmezliğinde egzersiz | Rehabilitasyon rehberi | denetlenmedi | | | |
| 1 | koah.html | KOAH'ta akciğer rehabilitasyonu | Rehabilitasyon rehberi | denetlenmedi | | | |
| 1 | buyume-agrilari.html | Çocuklarda büyüme ağrıları | Hastalık rehberi | denetlenmedi | | | |
| 1 | bebeklerde-tortikolis.html | Bebeklerde tortikolis | Hastalık rehberi | denetlenmedi | | | |
| 1 | sever-hastaligi.html | Çocuklarda topuk ağrısı (Sever hastalığı) | Hastalık rehberi | denetlenmedi | | | |
| 1 | osgood-schlatter.html | Osgood-Schlatter (büyüme çağında diz altı ağrısı) | Hastalık rehberi | denetlenmedi | | | |
| 1 | eklem-hipermobilitesi.html | Eklem hipermobilitesi (eklem gevşekliği) | Hastalık rehberi | denetlenmedi | | | |
| 1 | diyabetik-noropati.html | Diyabetik nöropati: ayaklarda uyuşma ve yanma | Hastalık rehberi | denetlenmedi | | | |
| 1 | huzursuz-bacak.html | Huzursuz bacak sendromu | Hastalık rehberi | denetlenmedi | | | |
| 1 | omuzda-kirec-birikmesi.html | Omuzda kireç birikmesi (kalsifik tendinit) | Hastalık rehberi | denetlenmedi | | | |
| 1 | fibromiyalji.html | Fibromiyalji | Hastalık rehberi | denetlenmedi | | | |
| 1 | titreme.html | Titreme (tremor) | Hastalık rehberi | denetlenmedi | | | |
| 1 | yuz-felci.html | Yüz felci (Bell felci) | Hastalık rehberi | denetlenmedi | | | |
| 1 | kemik-erimesi.html | Kemik erimesi (osteoporoz) | Hastalık rehberi | denetlenmedi | | | |
| 1 | dusme-onleme.html | Düşmeleri önleme ve denge | Rehabilitasyon rehberi | denetlenmedi | | | |
| 1 | kalca-kirigi.html | Kalça kırığı sonrası evde rehabilitasyon | Rehabilitasyon rehberi | denetlenmedi | | | |
| 1 | dar-kanal.html | Dar kanal (lomber spinal stenoz) | Hastalık rehberi | denetlenmedi | | | |
| 1 | gebelikte-bel-agrisi.html | Gebelikte bel ve leğen kemiği ağrısı | Hastalık rehberi | denetlenmedi | | | |
| 1 | idrar-kacirma.html | İdrar kaçırma ve pelvik taban egzersizleri | Hastalık rehberi | denetlenmedi | | | |
| 2 | adim-hedefi.html | Adım hedefi planlayıcısı | Kendine iyi bak | denetlenmedi | | | |
| 2 | agri-gunlugu.html | Ağrı günlüğü | Kendine iyi bak | denetlenmedi | | | |
| 2 | agriyi-anlamak.html | Ağrıyı anlamak | Kendine iyi bak | denetlenmedi | | | |
| 2 | alti-dakika-yurume-testi.html | 6 dakika yürüme testi | Kendine iyi bak | denetlenmedi | | | |
| 2 | ankilozan-spondilit.html | Ankilozan spondilit | Hastalık rehberi | denetlenmedi | | | |
| 2 | arka-uyluk-zorlanmasi.html | Arka uyluk zorlanması (hamstring sakatlığı) | Hastalık rehberi | denetlenmedi | | | |
| 2 | asil-tendinopatisi.html | Aşil tendinopatisi | Hastalık rehberi | denetlenmedi | | | |
| 2 | asil-tendonu-kopmasi.html | Aşil tendonu kopması | Hastalık rehberi | denetlenmedi | | | |
| 2 | atlet-dizi.html | Atlet dizi (patellar tendinopati) | Hastalık rehberi | denetlenmedi | | | |
| 2 | ayak-bilegi-burkulmasi.html | Ayak bileği burkulması | Hastalık rehberi | denetlenmedi | | | |
| 2 | ayak-bilegi-kirigi.html | Ayak bileği kırığı sonrası | Hastalık rehberi | denetlenmedi | | | |
| 2 | bag-kurmak.html | Sosyal bağ: unutulan sağlık önerisi | Kendine iyi bak | denetlenmedi | | | |
| 2 | baker-kisti.html | Baker kisti (diz arkası kisti) | Hastalık rehberi | denetlenmedi | | | |
| 2 | baldir-kasi-zorlanmasi.html | Baldır kası zorlanması | Hastalık rehberi | denetlenmedi | | | |
| 2 | bas-agrisi.html | Baş ağrısı: gerilim tipi ve boyun kaynaklı | Hastalık rehberi | denetlenmedi | | | |
| 2 | bas-donmesi.html | Pozisyonel baş dönmesi (BPPV) | Hastalık rehberi | denetlenmedi | | | |
| 2 | bel-boy-orani.html | Bel–boy oranı | Kendine iyi bak | denetlenmedi | | | |
| 2 | bel-fitigi-ameliyati-sonrasi.html | Bel fıtığı ameliyatı sonrası | Hastalık rehberi | denetlenmedi | | | |
| 2 | bel-kaymasi.html | Bel kayması (spondilolistezis) | Hastalık rehberi | denetlenmedi | | | |
| 2 | besinci-metatars-kirigi.html | Ayak dış kenarı (5. tarak kemiği) kırığı | Hastalık rehberi | denetlenmedi | | | |
| 2 | boyun-agrisi.html | Boyun ağrısı | Hastalık rehberi | denetlenmedi | | | |
| 2 | boyun-duzlesmesi.html | Boyun düzleşmesi | Hastalık rehberi | denetlenmedi | | | |
| 2 | boyun-incinmesi.html | Boyun incinmesi (whiplash) | Hastalık rehberi | denetlenmedi | | | |
| 2 | boyun-tutulmasi.html | Boyun tutulması (akut tortikolis) | Hastalık rehberi | denetlenmedi | | | |
| 2 | cekic-parmak.html | Çekiç parmak (mallet finger) | Hastalık rehberi | denetlenmedi | | | |
| 2 | cene-eklemi.html | Çene eklemi rahatsızlıkları | Hastalık rehberi | denetlenmedi | | | |
| 2 | de-quervain.html | De Quervain: başparmak tarafında bilek ağrısı | Hastalık rehberi | denetlenmedi | | | |
| 2 | demans-egzersiz.html | Demansta egzersiz | Rehabilitasyon rehberi | denetlenmedi | | | |
| 2 | denge-antrenmani.html | Denge antrenmanı | Kendine iyi bak | denetlenmedi | | | |
| 2 | denge-testi.html | 10 saniye denge testi | Kendine iyi bak | denetlenmedi | | | |
| 2 | diyabette-egzersiz.html | Diyabette egzersiz | Rehabilitasyon rehberi | denetlenmedi | | | |
| 2 | diz-kapagi-cikigi.html | Diz kapağı çıkığı (patella çıkığı) | Hastalık rehberi | denetlenmedi | | | |
| 2 | diz-onu-agrisi.html | Diz önü ağrısı (patellofemoral ağrı) | Hastalık rehberi | denetlenmedi | | | |
| 2 | dizin-12-sirri.html | Dizin 12 Sırrı | Kendine iyi bak · Diz kireçlenmesi | denetlenmedi | | | |
| 2 | doga-recetesi.html | Doğa reçetesi: haftada 120 dakika | Kendine iyi bak | denetlenmedi | | | |
| 2 | dort-asamali-denge-testi.html | 4 aşamalı denge testi | Kendine iyi bak | denetlenmedi | | | |
| 2 | dost-molasi.html | DOST molası: kendinize dost olmanın beş dakikası | Kendine iyi bak | denetlenmedi | | | |
| 2 | dupuytren-kontrakturu.html | Dupuytren kontraktürü | Hastalık rehberi | denetlenmedi | | | |
| 2 | dusme-riski-testi.html | Düşme riskinizi değerlendirin | Kendine iyi bak | denetlenmedi | | | |
| 2 | dustukten-sonra-kalkma.html | Düştükten sonra yerden kalkma | Kendine iyi bak | denetlenmedi | | | |
| 2 | duvar-oturusu.html | Tansiyon için duvar oturuşu | Kendine iyi bak | denetlenmedi | | | |
| 2 | duztabanlik.html | Düztabanlık | Hastalık rehberi | denetlenmedi | | | |
| 2 | egzersizde-agri.html | Egzersizde ağrı trafik ışığı | Kendine iyi bak | denetlenmedi | | | |
| 2 | el-bilegi-kirigi.html | El bileği kırığı sonrası | Hastalık rehberi | denetlenmedi | | | |
| 2 | el-kireclenmesi.html | El ve parmak kireçlenmesi | Hastalık rehberi | denetlenmedi | | | |
| 2 | ganglion-kisti.html | Ganglion kisti (el bileği kisti) | Hastalık rehberi | denetlenmedi | | | |
| 2 | gece-bacak-kramplari.html | Gece bacak krampları | Hastalık rehberi | denetlenmedi | | | |
| 2 | golfcu-dirsegi.html | Golfçü dirseği | Hastalık rehberi | denetlenmedi | | | |
| 2 | guc-devresi.html | Evde güç devresi | Kendine iyi bak | denetlenmedi | | | |
| 2 | guillain-barre.html | Guillain-Barré sendromu | Rehabilitasyon rehberi | denetlenmedi | | | |
| 2 | halluks-valgus.html | Halluks valgus: ayak başparmağı çıkıntısı | Hastalık rehberi | denetlenmedi | | | |
| 2 | hareket-atistirmaliklari.html | Hareket atıştırmalıkları | Kendine iyi bak | denetlenmedi | | | |
| 2 | hareket.html | Ne kadar hareket yeterli? | Kendine iyi bak | denetlenmedi | | | |
| 2 | ic-cekis.html | 5 dakikalık iç çekiş nefesi | Kendine iyi bak | denetlenmedi | | | |
| 2 | iki-dakika-adim-testi.html | 2 dakika adım testi | Kendine iyi bak | denetlenmedi | | | |
| 2 | kaburga-kirigi.html | Kaburga kırığı ve morarması | Hastalık rehberi | denetlenmedi | | | |
| 2 | kalca-kireclenmesi.html | Kalça kireçlenmesi (koksartroz) | Hastalık rehberi | denetlenmedi | | | |
| 2 | kalca-sikismasi.html | Kalça sıkışması (FAI) | Hastalık rehberi | denetlenmedi | | | |
| 2 | kalca-yan-agrisi.html | Kalça yan ağrısı (trokanterik bursit) | Hastalık rehberi | denetlenmedi | | | |
| 2 | kalk-yuru-testi.html | Kalk ve yürü testi | Kendine iyi bak | denetlenmedi | | | |
| 2 | kambur-durus.html | Kambur duruş (kifoz) | Hastalık rehberi | denetlenmedi | | | |
| 2 | kanser-egzersiz.html | Kanser tedavisi sırasında ve sonrasında egzersiz | Rehabilitasyon rehberi | denetlenmedi | | | |
| 2 | karin-kasi-ayrilmasi.html | Doğum sonrası karın kası ayrılması (diastazis rekti) | Hastalık rehberi | denetlenmedi | | | |
| 2 | karpal-tunel-sendromu.html | Karpal tünel sendromu | Hastalık rehberi | denetlenmedi | | | |
| 2 | kas-gevsetme.html | Kas gevşetme: sesli rehberle | Kendine iyi bak | denetlenmedi | | | |
| 2 | kasik-zorlanmasi.html | Kasık zorlanması | Hastalık rehberi | denetlenmedi | | | |
| 2 | kaval-kemigi-agrisi.html | Kaval kemiği ağrısı (shin splints) | Hastalık rehberi | denetlenmedi | | | |
| 2 | koprucuk-kemigi-kirigi.html | Köprücük kemiği kırığı | Hastalık rehberi | denetlenmedi | | | |
| 2 | kosucu-dizi.html | Koşucu dizi (iliotibial bant sendromu) | Hastalık rehberi | denetlenmedi | | | |
| 2 | kubital-tunel-sendromu.html | Kübital tünel sendromu (dirsekte sinir sıkışması) | Hastalık rehberi | denetlenmedi | | | |
| 2 | kucuk-adimlar.html | Küçük adımlar planlayıcısı | Kendine iyi bak | denetlenmedi | | | |
| 2 | kurek-kemigi-arasi-agri.html | Kürek kemiği arası ağrı (sırt ağrısı) | Hastalık rehberi | denetlenmedi | | | |
| 2 | kuyruk-sokumu-agrisi.html | Kuyruk sokumu ağrısı (koksidini) | Hastalık rehberi | denetlenmedi | | | |
| 2 | lenfodem.html | Lenfödem | Rehabilitasyon rehberi | denetlenmedi | | | |
| 2 | masa-basi.html | Masa başında çalışanlar için | Kendine iyi bak | denetlenmedi | | | |
| 2 | menisku-yirtigi.html | Menisküs yırtığı | Hastalık rehberi | denetlenmedi | | | |
| 2 | mola-zamanlayicisi.html | Masa başı mola zamanlayıcısı | Kendine iyi bak | denetlenmedi | | | |
| 2 | morton-noromasi.html | Morton nöroması | Hastalık rehberi | denetlenmedi | | | |
| 2 | multipl-skleroz.html | Multipl sklerozda (MS) egzersiz ve evde rehabilitasyon | Rehabilitasyon rehberi | denetlenmedi | | | |
| 2 | nabiz-olcer.html | Nabız ölçer ve hedef nabız | Kendine iyi bak | denetlenmedi | | | |
| 2 | nobel-2026.html | Işık, ayna ve buz | Nobel 2026 | denetlenmedi | | | |
| 2 | omurga-kirigi.html | Kemik erimesine bağlı omurga kırığı | Hastalık rehberi | denetlenmedi | | | |
| 2 | omurilik-yaralanmasi.html | Omurilik yaralanması sonrası rehabilitasyon | Rehabilitasyon rehberi | denetlenmedi | | | |
| 2 | omuz-cikigi.html | Omuz çıkığı (omuz instabilitesi) | Hastalık rehberi | denetlenmedi | | | |
| 2 | omuz-kireclenmesi.html | Omuz kireçlenmesi | Hastalık rehberi | denetlenmedi | | | |
| 2 | omuz-sikismasi.html | Omuz sıkışması (subakromiyal ağrı) | Hastalık rehberi | denetlenmedi | | | |
| 2 | omuz-ucu-yaralanmasi.html | Omuz ucu (AC eklem) yaralanması | Hastalık rehberi | denetlenmedi | | | |
| 2 | on-capraz-bag.html | Ön çapraz bağ yaralanması | Hastalık rehberi | denetlenmedi | | | |
| 2 | otur-kalk-testi.html | Yere oturup kalkabiliyor musunuz? | Kendine iyi bak | denetlenmedi | | | |
| 2 | oturma-suresi.html | Günlük oturma süresi hesaplayıcısı | Kendine iyi bak | denetlenmedi | | | |
| 2 | parkinson.html | Parkinson hastalığında egzersiz ve evde rehabilitasyon | Rehabilitasyon rehberi | denetlenmedi | | | |
| 2 | pelvik-organ-sarkmasi.html | Pelvik organ sarkması (rahim, mesane ya da bağırsak sarkması) | Hastalık rehberi | denetlenmedi | | | |
| 2 | pelvik-taban-zamanlayicisi.html | Pelvik taban egzersiz zamanlayıcısı | Kendine iyi bak | denetlenmedi | | | |
| 2 | periferik-arter-hastaligi.html | Periferik arter hastalığı: yürürken bacak ağrısı ve egzersiz | Rehabilitasyon rehberi | denetlenmedi | | | |
| 2 | piriformis-sendromu.html | Piriformis sendromu | Hastalık rehberi | denetlenmedi | | | |
| 2 | protez-sonrasi.html | Diz ve kalça protezi sonrası evde rehabilitasyon | Rehabilitasyon rehberi | denetlenmedi | | | |
| 2 | romatoid-artrit.html | Romatoid artrit ve egzersiz | Hastalık rehberi | denetlenmedi | | | |
| 2 | rotator-manset-yirtigi.html | Rotator manşet yırtığı | Hastalık rehberi | denetlenmedi | | | |
| 2 | ruh-hali-olcumu.html | Ruh hâlinizi ölçün | Kendine iyi bak | denetlenmedi | | | |
| 2 | ruh-sagligi-egzersiz.html | Ruh sağlığı için egzersiz | Kendine iyi bak | denetlenmedi | | | |
| 2 | sabah-rutini.html | Güne 5 dakikayla başlayın | Kendine iyi bak | denetlenmedi | | | |
| 2 | sakatlanmayi-onleyen-isinma.html | Sakatlanmayı önleyen ısınma | Kendine iyi bak | denetlenmedi | | | |
| 2 | sakroiliak-eklem-agrisi.html | Sakroiliak eklem ağrısı | Hastalık rehberi | denetlenmedi | | | |
| 2 | sandalye-testi.html | 30 saniye sandalye testi | Kendine iyi bak | denetlenmedi | | | |
| 2 | sarkopeni.html | Sarkopeni: yaşa bağlı kas kaybı | Hastalık rehberi | denetlenmedi | | | |
| 2 | stres.html | Stresli anlarda ne yapabilirsiniz? | Kendine iyi bak | denetlenmedi | | | |
| 2 | surekli-usume.html | Sürekli üşüme (soğuğa duyarlılık) | Hastalık rehberi | denetlenmedi | | | |
| 2 | tansiyon-gunlugu.html | Ev tansiyon günlüğü | Kendine iyi bak | denetlenmedi | | | |
| 2 | tempolu-yuruyus.html | Tempolu yürüyüş metronomu | Kendine iyi bak | denetlenmedi | | | |
| 2 | tenisci-dirsegi.html | Tenisçi dirseği (lateral epikondilit) | Hastalık rehberi | denetlenmedi | | | |
| 2 | tetik-parmak.html | Tetik parmak | Hastalık rehberi | denetlenmedi | | | |
| 2 | topuk-dikeni.html | Topuk dikeni (plantar fasiit) | Hastalık rehberi | denetlenmedi | | | |
| 2 | uc-kapi.html | Üç Kapı | Kendine iyi bak · Yeni bir yaklaşım | denetlenmedi | | | |
| 2 | uyku.html | İyi uyku için | Kendine iyi bak | denetlenmedi | | | |
| 2 | uzun-covid.html | Uzun COVID'de hareket ve nefes | Rehabilitasyon rehberi | denetlenmedi | | | |
| 2 | yemek-sonrasi-yuruyus.html | Yemek sonrası yürüyüş | Kendine iyi bak | denetlenmedi | | | |
| 2 | yenilikler.html | Geleceğin tıbbı, bugün | Bilim gündemi | denetlenmedi | | | |
| 2 | yogun-bakim-sonrasi.html | Yoğun bakım sonrası iyileşme | Rehabilitasyon rehberi | denetlenmedi | | | |
| 2 | yuksek-tansiyon.html | Yüksek tansiyonda egzersiz | Rehabilitasyon rehberi | denetlenmedi | | | |
| 2 | yurume-hizi-testi.html | Yürüme hızı testi | Kendine iyi bak | denetlenmedi | | | |
| 2 | zayiflama-ilaci-ve-kas.html | Zayıflama ilacı kullanırken kaslarınızı koruyun | Rehabilitasyon rehberi | denetlenmedi | | | |

## Skolyoz denetimi — 28 Ekim 2026 (iki bağımsız denetçi: A = başlangıç–#risk, B = #tarihce–son)
Düzeltildi (TR+EN, çeviri tur32): ameliyat %0,1–0,3 (payda belirsiz) kutudan çıkarıldı; %72/%48 kutusu BrAIST tanımıyla yazıldı; Cobb tablosunda egzersiz önerisi SRS'ye değil SOSORT'a atfedildi (SRS: seyri değiştirdiği gösterilen tedaviler korse ve ameliyat); uç omur yüzeyi tarifi; Risser çiziminde numaralar tersti (kemikleşme dış uçtan başlar) + açıklama; büyüme atağı yaşı 10–18 → SRS 10–15; Dragsted (25° altında da >10° artış olabilir) ve "50° üstü yetişkinlikte ilerler, düzenli röntgen" eklendi; nefes darlığı eşiği JAMA özetine göre (80° üstü göğüs eğriliği); "tek başına" ifadesi çıkarıldı, ters yön olasılığı eklendi; tarihçe girişi (ameliyatlar gözlemsel), Risser işareti 1958, CD 1983 "ilk kez uygulandı", BrAIST "50 dereceye ulaşmayı azalttı" (ameliyatı değil), SOSORT "güncellendi", tethering HDE ("insani kullanım" yanlış terimdi) + uzun dönem bilinmiyor; gece korsesi %76 ile BrAIST %72 karşılaştırılamaz notu; korse 18 saat verildi / 13 saat ve üzeri %90–93; füzyon ve tam gün korse riskleri eklendi; egzersiz kartı "orta eğrilikte korsenin yanında"; Kuru 2016 (≈2,5°, ölçüm payının altında; ev grubu kontrolle benzer); Cochrane "muhtemelen" = orta güvenilirlik; spor uyarısı (SOSORT: korse döneminde temaslı/çok hareketli sporlar dikkatle); acil uyarı ayrı madde; "uzman" → "hekim"; SSS'deki klinik gözlemlere "araştırma sonucu değil" notu; Radiopaedia bağlantısı makaleye.
Açık kalanlar (düşük önem, 10.50 sonrası): Czaprowski "vaka-kontrol, neden göstermez" notu; "benign eklem hipermobilite sendromu (bugün hipermobilite spektrum bozukluğu)" notu — kullanıcının terimi, silinmeyecek; meta açıklama nötrleştirme; fonksiyonel eğrilik cümlesi (bacak boyu farkında öne eğilince değil, otururken düzelir) ve "büyük bacak boyu farkı"; tip yaş bantları (0–3 / 4–9 / 10–büyüme bitimi); Little 2000 paydaları (60 kızın 50'si, 28 kızın 1'i); Minghelli "röntgenle doğrulanmadı" notu; öne eğilme altyazısı "dönme olabilir; tanı röntgenle"; denge altyazısı "ortadan bir yana kayar"; yetişkin "en sık iki tip"; ev egzersizlerine "ameliyat olduysanız / bacağa yayılan ağrı varsa önce hekiminize"; BrAIST ITT %75/%42 notu; Hipokrat kaynağı (Vasiliadis 2009); kaynak künyeleri (Berdishevsky 2016;11:20, SOSORT tam adı, Moramarco 1452–1465, Lonstein blog yerine makale tablosu); JSON-LD tarihi kontrolü; "psikolojik destek" ifadesinin kaynağı.
Bilinçli bırakılan: Tanchev için "eklem gevşekliği" (çalışmanın kendi terimi, DEVAM kararı).

Skolyoz düşük önemli düzeltmeler (28 Ekim 2026 öğle, çeviri tur33): Little 2000 paydaları (60'ın 50'si, 28'in 1'i; qxmd özetiyle doğrulandı), Minghelli "röntgenle doğrulanmadı", Czaprowski "vaka-kontrol, neden göstermez", "Benign eklem hipermobilite sendromu (bugünkü adıyla hipermobilite spektrum bozukluğu)", tip yaş bantları, fonksiyonel eğrilik "otururken" + "büyük bir fark", öne eğilme ve denge altyazıları, "en sık iki tip", ev egzersizine ameliyat/bacağa yayılan ağrı uyarısı, "psikolojik destek" (kaynakta yok) → "hasta eğitimi", meta açıklama, BrAIST randomize grup %75/%42, Berdishevsky 2016;11:20, Moramarco 1452–1465, Hipokrat kaynağı Vasiliadis 2009.
Skolyozda açık: SOSORT'un resmî adı ("Scientific" geçiyor mu) doğrulanamadı; Lonstein %68/%23 için ikincil kaynak (blog) yerine makale tablosu bulunamadı — sayılar bilinen tabloyla uyumlu, kaynak değiştirilmedi.
