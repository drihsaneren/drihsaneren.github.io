# drihsaneren.com — kaynak dosyaları (bu dal siteyi ETKİLEMEZ)

Site `main` dalından yayınlanır (GitHub Pages, drihsaneren.com). Bu `kaynak` dalı,
`main`'deki hazır sayfaları üreten araçları saklar. Yeni bir oturumda buradan devam edilir.

## İÇERİK KALİTE KONTROLÜ (her yeni metin için ZORUNLU — kullanıcı isteği, 28 Ekim 2026)
Kullanıcı skolyoz sayfasında art arda hata buldu (belirsiz "büyümenin önemi" girişi, "eklem esnekliği" terimi, kurum adının yanlış çevrilmesi, "tek taraflı alışkanlık"ın yalnızca çantaya daraltılması, çizimde açı hatası) ve "diğer çalışmalarda ve bilgilerde de böyle titizlik ve dikkat istiyorum" dedi. Yayından önce şu adımlar atlanmaz:
1. **Her sayı, yıl, isim, oran** bir kaynakta (tercihen birincil: makale özeti, kılavuz metni) açıkça görülerek yazılır. Kaynakta görülmeyen ayrıntı (ilk ad, milliyet, cilt/sayı, yüzde) hafızadan EKLENMEZ; doğrulanamıyorsa çıkarılır ya da daha genel yazılır. İkincil kaynaktan gelen bilgi mümkünse birincilden kontrol edilir.
2. **Sonuç ifadesinin gücü** çalışma tasarımına uyar: kesitsel/vaka-kontrol → "ilişkili bulundu", neden-sonuç yok; ters yön olasılığı varsa yazılır; beyana dayalı ölçüm, röntgensiz tanı gibi sınırlılıklar belirtilir.
3. **Kurum, terim ve kavram adları** Türkçe tıbbi kullanıma göre kontrol edilir (ör. "Skolyoz Araştırma Derneği (SRS)", "bağ dokusu esnekliği"); kelime kelime çeviri yapılmaz.
4. **Kullanıcının söylediği** daraltılmadan ve genişletilmeden uygulanır; ifade iki anlama gelebiliyorsa yazmadan önce sorulur. Klinik deneyim kutusu kullanıcının kendi gözlemini yansıtır, araştırmadan ayrı ve etiketli kalır.
5. **Hasta gözüyle okuma**: giriş paragrafı, başlıklar, içindekiler, kart metni ve sayfa açıklaması ayrıca okunur; tek başına okunduğunda yanlış ya da belirsiz anlam veren cümle kalmaz.
6. **Sayfa içi tutarlılık**: yeni eklenen bilgi sayfanın geri kalanıyla (istatistik kutuları, giriş, SSS) çelişmez; çelişki varsa eski metin düzeltilir ve kullanıcıya söylenir.
7. **Görseller/çizimler** ekran görüntüsüyle bakılarak anatomik doğruluk açısından kontrol edilir.
8. Raporda neyin birincil kaynaktan, neyin ikincil kaynaktan doğrulandığı ve neyin çıkarıldığı açıkça yazılır.

## Kurulum (yeni oturum)

```bash
# main: sitenin kendisi (ör. /home/claude/drihsaneren.github.io)
git -C <main-dizini> fetch origin kaynak
git -C <main-dizini> worktree add <çalışma-dizini> kaynak     # araçlar buraya açılır
export REPO=<main-dizini>                                       # betikler çıktıyı buraya yazar
cd <çalışma-dizini> && mkdir -p up40 shots6
```

## Üretim hattı (hepsi çalışma dizininden)

```bash
python3 build_pages.py github up40      # konu sayfaları + bilgi.html + yenilikler.html (up40/)
bash rebuild_home.sh                    # ana sayfa kaynağı: site/index.bak_fb.html + fb_*.py zinciri -> site/index.html
bash publish.sh up40 bilgi.html         # ana sayfayı ve up40/*.html'i $REPO'ya yazar, /en/ üretir, site haritası
python3 fb_recete.py                    # recete.orig.html -> $REPO/recete.html (koyu tema)
python3 make_en.py $REPO $REPO          # İngilizce sayfalar; "toplam eksik: 0" olmalı
python3 search_index.py $REPO           # ara-tr.json / ara-en.json
```
Bu sırayla çalıştırınca `main` ile birebir aynı çıktı gelir (yalnızca sitemap.xml tarihi değişir).
Dikkat: `publish.sh` her zaman `build_pages.py`'den sonra çalıştırılmalı (`up40/_home_section.txt` ve `_home_css.txt` yoksa hata verip durur).
Sonra `$REPO` içinde commit + push (main). Araçlarda değişiklik yaptıysan bu dalı da commit + push et.

## Ne nerede

- **Ana sayfa**: `site/index.bak_fb.html` (taban) üzerine sırayla `fb_hero.py` (giriş, üst çubuk),
  `fb_misc.py` (iletişim, galeri, hızlı test), `fb_report.py` (analiz raporu slaytları),
  `fb_book.py` (ücretsiz ön görüşme; Google takvim gelince `data-embed`), `fb_day.py` (Günlük Hareket
  Skalası), `fb_lx.py` (Longevity başı), `fb_trim.py` (kısaltmalar), `fb_qr.py` (nöron karekod),
  `fb_reg.py` (®). Sıra `rebuild_home.sh` içinde. `to_github.py` + `splice_home.py` yayın biçimine çevirir.
- **Konu sayfaları**: `build_pages.py` + `*_part.py` (page(), KC kartları, NEWS listesi, CTA_CARD, bar()).
- **Bilgi köşesi (bilgi.html)**: `AGR` (bölge etiketli hastalıklar), `REHAB`, `SELF` listeleri tek kaynak; yayın sayacı (`pulse()`: sayılar + dönen başlıklar),
  yapışkan kategori çubuğu (`#tabs`), liste/kart görünümü (`#hub[data-view]`, varsayılan liste, seçim `localStorage` `bk-view`) ve ana sayfadaki
  gruplanmış haplar (`pill_group`, kısa adlar `PILL` sözlüğünde) bu listelerden üretilir. Yeni sayfa eklerken `PILL`'e kısa ad yazmak yeterli;
  sayılar kendiliğinden güncellenir. Haber bölümünün adı **Bilim gündemi** ("magazin" dedikodu çağrışımı yaptığı için kullanılmadı; EN: Science news);
  `NEWS` listesinden `headlines()` ile başlık listesi (bilgi.html bölümü, ana sayfa grubu, yenilikler.html'de açılır dizin) üretilir, her haberin `news_id()` çapası var.
  Ana sayfa girişindeki üç kapı (`.trio`: Hastalık rehberleri, Kendine iyi bak, Bilim gündemi) ve altındaki açılır hastalık listesi (`details.hx`, `hx_groups()`: bölgeye göre kısa adlar) ile "Kendine iyi bak ne işe yarar?" kutusu (`hx_self()`, gruplar `SELF_GROUPS`) `_home_trio.txt` ile `splice_home.py` tarafından eklenir. Telefonda yana kayan menü yok: giriş bölümündeki kısayollar iki sütun (`fb_hero.py`), kategori çubuğu 2×2 (≤1040 px). Ana sayfanın bilgi köşesi stilleri de `HOME_CSS`'ten gelir (`splice_home.py` bölümü ve stili birlikte değiştirir).
- **Yeni hastalık ekleme** (örnekler: `cond5_part.py` dar kanal, `cond6_part.py` MS): yeni `condN_part.py` (çizimler `SV`/`EXT`, `_ex2`, FAQ, kaynaklar,
  gövde, `page(...)`) yazılır ve `build_pages.py`'deki exec listesine eklenir. `build_pages.py`'de ayrıca `KOSE_PAGES`, `TOPICS`,
  `RELATED`, kart görseli `TH_*` + `C_* = KC(...)`, `AGR` (bölge etiketi) ya da `REHAB`/`SELF` listesi ve `PILL` kısa adı; `i18n_map.py`'de `EN` adresi.
  Çeviri: `python3 export_todo.py $REPO <sayfa>.html` -> `i18n/todo/<sayfa>.json`, karşılığı `i18n/done/<sayfa>.json`;
  diğer sayfalara düşen metinler (kart, hap) `fb1.json`'a. Yayın: `bash publish.sh up40 <sayfa>.html`.
- **Örnek reçete**: `recete.orig.html` + `fb_recete.py`.
- **Galeri kareleri**: yalnızca `main`'de duran `p01, p02, p03, p07, p10, p13, p21` (`.jpg` tam: 1100 px genişlik, dikeyde 880×1100; `_t.jpg` küçük: 700 px, dikeyde 416×520). Sıra ve alt metinler `site/index.bak_fb.html` içindeki `picks` dizisinde. 4 Ekim 2026'da yedisi de aynı adlarla yenilendi.
- **İngilizce**: `make_en.py`, `i18n_map.py` (adresler), `i18n/todo|done/*.json` (TR -> EN bellek).
  Yeni/değişen metinler `i18n/todo/fb1.json` + `i18n/done/fb1.json`'a yeni kimlikle eklenir
  (`python3 i18n/check.py fb1` ile doğrula). Betik içi metinler `i18n/js.json`. Var olan todo dosyalarını yeniden dışa aktarma.
- **Arama**: `ara.js`, `search_ui.py`, `search_index.py`.
- **Sınama**: `./srv.sh python3 t_xxx.py` (yerel sunucu + Playwright). Örn. `t_fb.py`, `t_gh.py`,
  `t_bk2.py`, `t_nq3.py` (karekod her karede okunuyor mu), `t_st2.py` (karekod dayanıklılık), `t_rec.py`,
  `t_ls.py <dizin> <tr.html> <en.html> <video-sayısı> [ilgili-tr ilgili-en]` (yeni konu sayfası: taşma 390/1366/1440, kart, süzgeç, hap, ilgili bağlantı, TR + EN).

## Değişmez kurallar

- "randevu" kelimesi yok ("Seans planla" / "Book a session"). Okul adı yok. "Biruni" yok.
- Telefon numarası görünmez, `tel:` bağlantısı yok (yalnızca WhatsApp ve e-posta). Şemada adres/telefon yok.
- Dijital kartvizit bağlantısı yalnızca iletişim bölümünde. "YouTube'da izle / Spotify'da aç" yönlendirmesi yok.
- Altın-yeşil tasarım korunur. Galeri fotoğrafları tıklanınca açılmaz; yapay zekâ görselleri gerçek fotoğraf diye sunulmaz.
- İğneleme (akupunktur, kuru iğneleme) hekim yetkisindedir; hizmet olarak sunulmaz, yalnızca logo bölümünde "hekimlik" çerçevesinde geçer.
  Ayrı konu: **"Kişisel klinik gözlemim" kutusu** (`OBS()`, neck_part.py). Kullanıcı 7 Ekim 2026'da akupunktur için kendi klinik gözlemini yazmamı istedi; kutu yüz felci, inme, fibromiyalji ve titreme sayfalarında var. Her zaman araştırma özetinin YANINDA, "gözlem, araştırma sonucu değil" cümlesiyle (`OBS_TAIL`) ve mevzuat notuyla (`ACU_LAW`) birlikte durur; hizmet olarak sunulmaz. Üşüme sayfasına konmaz.
- Sağlık iddiaları kaynaklı ve ölçülü yazılır; skala "tanı koymaz" notunu taşır.
- Her değişiklik TR + EN birlikte; telefon (390) ve bilgisayar (1366/1440) genişliğinde taşma sınaması.
- Kullanıcıya yanıtlar Türkçe.

## Bekleyen işler

- MS sayfası (4 Ekim 2026) videosuz: YouTube sayfaları okunamadığı için kanal doğrulanamadı. Uygun, kanalı doğrulanmış MS egzersiz videosu bulunursa `cond6_part.py`'ye `#videolar` bölümü eklenebilir.
- Dar kanal sayfası (2 Ekim 2026): Delitto 2015 çalışmasında fizyoterapi grubundan ameliyata geçenlerin tam oranı kaynaktan doğrulanamadı; sayfada rakamsız ("önemli bir bölümü") yazıldı. Doğrulanınca rakam eklenebilir.
- Google Takvim "Appointment schedule" yerleştirme kodu gelince `fb_book.py` içindeki `data-embed=""` doldurulacak (30 dk).
- Armut.com yorumları (profil bağlantısı bekleniyor). Gerçek fotoğraflar (özellikle iğneleme karesi yerine).
- LinkedIn için 1200×627 paylaşım görseli önerildi.
- Arkadaşının "PC'de düzgün açılmıyor" bildirimi tekrarlanamadı (tarayıcı bilgisi bekleniyor).

## Almanca (durduruldu)
Kullanıcı Almancadan vazgeçti (6 Ekim 2026). Site yalnızca TR + EN. Yarım kalan altyapı ve çeviriler
(`make_lang.py`, `de_tool.py`, `i18n/BRIEF_DE.md`, `i18n/done_de/`, 51 dosyadan ~20'si çevrili) `almanca` dalında
duruyor; `kaynak` dalı Almanca öncesi hâline döndürüldü. Kullanıcı açıkça istemedikçe devam etme.

## Giriş (hero) düzeni
6 Ekim 2026: kullanıcı isteğiyle bilgisayarda da telefondaki giriş kullanılıyor: kabartmalı canlı logo üstte, "İhsan Eren" üst çubukta
solda, büyük isim başlığı yok (h1 yalnızca ekran okuyucular için). Eski "logo arkada gravür" masaüstü düzeni kaldırıldı (`fb_hero.py`).

## Karekod (fb_qr.py)
6 Ekim 2026: kullanıcının gönderdiği tasarıma uyarlandı: koyu yeşil zemin, kum rengi (#c9c990) kabartma kareler, ortada 9×7 modüllük
logo alanı, hata düzeltme Q (29×29). Hedef yine WhatsApp (kullanıcının görseli drihsaneren.com'a gidiyordu; sitede anlamsız olurdu).
Açılış: halkalar iris gibi dönerek oturur, gözler sırayla düşer; döngü: altın dalga (yalnızca renk); imleçle eğilir, ışık imleci izler.
Okunurluk iki çözücüyle (zxing-cpp, OpenCV) her karede sınandı. Dikkat: göz köşeleri fazla yuvarlanırsa OpenCV okuyamıyor (dış yarıçap ≤ ~0,6 modül);
`.nq` üzerinde overflow:hidden ya da bitmiş dönüşüm animasyonu kalırsa eğilirken bulanıklaşıyor.

## Portre (fb_face.py)
6 Ekim 2026: kullanıcının gönderdiği kameraya bakan portre eklendi (`portre2.jpg` 720px, `portre2_s.jpg` 192px; yalnızca main dalında).
"Ben kimim": ana daire yeni portre, sağ alt köşesinde küçük dairede eski beyaz önlüklü kare (`portre.jpg`). İletişim: yazının altında,
düğmelerin üstünde küçük yüz + ad + unvan ("imza"). Giriş: birkaç deneme sonrası (unvan yanında küçük yüz, logo + portre çifti beğenilmedi) kullanıcının önerisiyle portre "Ücretsiz ön görüşme" düğmesinin altında, ortada bir kimlik kartı (`.hero-me`: yüz + "Ben kimim" + ad, dokununca bölüme iner); logo yine tek başına.
Kaynak görsel `site/` aşamasında `img/portre2.jpg` diye geçer; `to_github.py` "img/" önekini atar.
Portre aynı gün ikinci bir fotoğrafla değiştirildi (kafeterya arka planı). Kırpma (120,70,1000,950): arkadaki hastane tabelasının yazısı
dairenin dışında kalacak biçimde seçildi (kural: yazarla ilgili kurum adı görünmez); yeniden kırparken buna dikkat et.
"Ben kimim"deki köşe karesi (beyaz önlüklü, başka yöne bakan `portre.jpg`) kullanıcı isteğiyle kaldırıldı; bölümde yalnızca yeni portre var.
Giriş kartından ad kaldırıldı (kullanıcı: "sol üstte yazıyor zaten"); kartta yalnızca yüz + "Ben kimim" var, fotoğraf 84 px (≥700 px: 94 px).
Aşağıdaki "Ben kimim" bölümünün "İhsan Eren" başlığı kullanıcıya soruldu, yerinde kaldı. Yapısal verideki portre adresi artık `schema_home.json`'da `portre2.jpg` (önceden yalnızca main'de elle düzeltilmişti).
Yeni oturumda `pip install qrcode` gerekir (`fb_qr.py`); yoksa `rebuild_home.sh` yarıda kalır.

## DOST molası (self3_part.py)
6 Ekim 2026: Kendine iyi bak'a 11. rehber: `dost-molasi.html` / `en/self-kindness-break.html`. Dört adım (Dur ve adını koy, Omuzlarını bırak,
Seslen, Teşekkür et) + sonunda kişinin seçimlerinden oluşan "kendine not" (hiçbir şey kaydedilmez; `#ds`, metinler `.ds-strings` içinde, JS'te metin yok).
Kaynaklar (hepsi okundu): Lieberman 2007 (30 kişi, duyguya ad koyma), Dreisoerner 2021 (159 kişi, 20 sn dokunuş: kortizol düşük, kalp hızı ve
hissedilen stres farksız), Kross 2014 (7 çalışma, 585 kişi), Shapira & Mongrain 2010 (üniversite duyurusundan: 3 ayda daha az çökkün, 6 ayda daha mutlu),
Alleva 2015 (81 kadın), Ferrari 2019 (27 RKÇ). Sayfada açıkça yazıyor: adımlar ayrı ayrı araştırıldı, birleşim bütün olarak sınanmadı.
İngilizcede adım adları Türkçe bırakıldı ("Dur: stop and name it"); bu yüzden `i18n/check.py` ALLOW_TR'ye "Omuzlarını bırak", "Teşekkür et" eklendi.
Sayfa açıkken telefondaki yüzen WhatsApp düğmesi araç görünürken gizlenir (`body.ds-on #fab`).
Girişteki kısayollardan "Ben kimim" çıkarıldı (kimlik kartı aynı yere gidiyor); üst çubukta duruyor.
Dikkat: aynı gün başka bir oturum da bu depoya gönderim yaptı; göndermeden önce `git fetch` ile iki dalı da denetle.

Galeri: 6 Ekim 2026'da `p07` (omurga maketi) el görünümü yüzünden yeniden değiştirildi; yeni kare dikey (880×1100, küçük 416×520),
kutuda yüz + maket + kalem tutan el görünsün diye `fb_misc.py`'de `object-position:50% 38%`.

## Ön çapraz bağ (cond7_part.py)
7 Ekim 2026: 27. hastalık rehberi `on-capraz-bag.html` / `en/acl-injury.html` (bölge: diz; menisküs sayfasının ilgili bağlantısı buna çevrildi).
Kaynaklar (hepsinin özeti okundu): Frobell 2013 BMJ (121 kişi, 5 yıl, fark yok, %51 sonradan ameliyat), Reijman 2021 BMJ COMPARE (167; 84,7'ye 79,4,
klinik açıdan önemsiz; %50), Beard 2022 Lancet ACL SNNAP (316; 73,0'a 64,6; %41), Grindem 2016 (106 sporcu; ayda %51; %38,2'ye %5,6),
Ardern 2014 (69 çalışma, 7.556 kişi; %81/%65/%55), Webster & Hewett 2018 (8 meta-analiz; %50). Çalışmaların ülkeleri özetlerde geçmediği için yazılmadı.
Video yok: YouTube araması robots.txt nedeniyle okunamadı, Bob & Brad video kimlikleri doğrulanamadı (MS sayfasıyla aynı durum).
Egzersizlerin beşi menisküs sayfasındaki metinlerle aynı (`mn_*`), yalnızca `acl_hslide` yeni.

## KOAH (cond8_part.py) ve video kuralı
7 Ekim 2026: 8. rehabilitasyon rehberi `koah.html` / `en/copd-pulmonary-rehabilitation.html`. Yeni çizimler: `plb` (büzük dudak nefesi), `fwdlean` (öne eğilerek toparlanma).
Kaynaklar (özetleri okundu): McCarthy 2015 Cochrane (65 RKÇ, 3.822 hasta, 6 dk yürüme +43,93 m), Puhan 2016 Cochrane (20 çalışma, 1.477 hasta, +62 m,
yeniden yatış OR 0,44, orta kanıt), Holland 2017 Thorax (166 hasta, ev programı kısa vadede eşdeğer; 12. ayda eşdeğerlik gösterilemedi), Holland Cochrane
nefes egzersizleri (16 çalışma, 1.233 hasta, +35–50 m; Cochrane sayfası atıfı "2022, Issue 3" diye veriyor, öyle yazıldı), DSÖ bilgi notu (10 Haziran 2026: 3. sıra, 2023'te 3,4 milyon ölüm, yüksek gelirli ülkelerde >%70 tütün).
**Video kuralı (kullanıcı, 7 Ekim 2026):** Bob & Brad dışında, düzenli yayın yapan güvenilir ve tescilli kişi/kurum kanalları da kullanılabilir.
KOAH'ta American Lung Association (`7kpJ0QlRss4`) ve NHS inform (`oSclbDihp2Y`); ön çapraz bağa Bob & Brad (`_gF6llBpol0`, `m-G-r_MgL_4`) eklendi.
**Video kimliği doğrulama yöntemi:** WebSearch'ü `allowed_domains: ["youtube.com"]` ile yap (kimlikler sonuçlarda gelir), sonra
`https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=<kimlik>&format=json` adresini WebFetch ile okuyup başlık + kanal adını doğrula.
Videolar izlenemedi; açıklamalar yalnızca başlığa dayanır, bu yüzden kısa ve iddiasız tutuldu. MS sayfasına da bu yöntemle video eklendi: MS Society UK (`0DTnlCCxS7s`) ve Cleveland Clinic (`X8nkMFcBIvA`).

## Kalp rehabilitasyonu (cond9_part.py)
7 Ekim 2026: 9. rehabilitasyon rehberi `kalp-rehabilitasyonu.html` / `en/cardiac-rehabilitation.html`. Yeni çizim yok; egzersizler var olan şekillerle
(`cr_walk`, `copd_sts`, `mn_kext`, `copd_heel`, `pf_sabd`, `cr_wall`). Videolar British Heart Foundation (`ESYDPnY5_1A`, `-JsuNKbAAkU`).
Kaynaklar (Cochrane özet sayfaları ve DSÖ bilgi notu okundu): Dibben ve ark., Cochrane 2026;(9):CD001800 (18 Eylül 2026 güncellemesi; 85 çalışma, 23.430 kişi;
6–12 ayda kalp krizi RR 0,72, yatış RR 0,58 [NNT 12], tüm nedenli ölüm RR 0,87 [0,73–1,04], katılımcıların %17'si kadın), McDonagh 2023 Cochrane
(24 çalışma, 3.046 kişi; ev = merkez), DSÖ (31 Temmuz 2025: 2022'de 19,8 milyon ölüm, %32). Sayfa her yerde "kardiyoloğunuzun onayıyla" vurgusunu taşır;
hedef nabız için sayı verilmedi (ilaçlar etkiler), konuşma testi önerildi.

## Romatoid artrit (cond10_part.py)
7 Ekim 2026: 28. hastalık rehberi `romatoid-artrit.html` / `en/rheumatoid-arthritis.html` (bölge: genel). Egzersizler var olan el şekilleriyle
(`ra_tglide`, `ra_grip`, `ra_wflex`, `ra_eccwe`) + `copd_sts`, `cr_walk`. Videolar: North Bristol NHS Trust (`mIxCSJNbfhU`), Hospital for Special Surgery (`oQvMzkBxqbQ`).
Kaynaklar (özet sayfaları okundu): Hurkmans ve ark. Cochrane CD006853 (8 çalışma; toplam hasta sayısı özet sayfasında yoktu, yazılmadı; Cochrane sayfası atıfı
"2022, Issue 3" diye veriyor), Lamb 2015 Lancet SARAH (490 hasta; MHQ 7,9'a karşı 3,6, fark 4,3; PEDro özeti ondalık noktaları düşürmüş, "79/36/43" görünüyor),
EULAR 2018 fiziksel aktivite önerileri, DSÖ bilgi notu (28 Haziran 2023: 18 milyon, %70 kadın, %55'i 55 yaş üstü).

## Sürekli üşüme (cond11_part.py) ve tamamlayıcı tıp çerçevesi
7 Ekim 2026: kullanıcının isteğiyle (bir arkadaşının nedeni bulunamayan üşümesi) belirti rehberi `surekli-usume.html` / `en/always-feeling-cold.html` (bölge: genel).
Sıra: olası nedenler ve testler -> günlük önlemler -> "Tamamlayıcı yaklaşımlar: kanıt ne diyor?" -> ısınmak için altı hareket. Video yok.
Bu sayfada bilerek `CTA_CARD` (seans planla) yok: ilk adım hekim muayenesi.
**Akupunktur bu sayfada GEÇMEZ** (kullanıcı 7 Ekim 2026: "üşüme kısmında akupunkturu çıkart, titremede koy"); akupunktur kanıt özeti ve GETAT notu yalnızca titreme sayfasında. Geri ekleme.
Kaynaklar (okundu): MedlinePlus "Cold intolerance" (27 Şubat 2026), NHS Raynaud's (20 Temmuz 2023), NHS hipotiroidi belirtileri (28 Nisan 2025),
Malenfant 2009 (özet qxmd üzerinden: 20 RKÇ; biyogeribildirim işe yaramıyor, eldiven tek çalışma, lazer belirsiz, akupunktur 2 çalışma yetersiz; cilt/sayfa hafızadan: 48(7):791-795),
Yamazaki 2023 (16 kadın, 2 hafta yürüyüş/koşu: üşüme hissi azaldı, cilt sıcaklığı değişmedi). Okunamayan: el-ayak üşümesinde bitkisel ürünler derlemesi (PMC captcha) -> sayfada kullanılmadı.
**Titreme (tremor) için bekleyen fikir:** kullanıcı "akupunktur etkili" dedi. Okunan: Shen ve ark., Healthcare 2026 ağ meta-analizi (esansiyel tremor; 20 RKÇ, 1.067 kişi,
hepsi Çin'de; küçük örneklem, körleme yok, gizleme yetersiz) -> "umut verici ama kanıt kesinliği düşük" diye yazıldı. Rehber kullanıcı onayıyla yayımlandı (aşağıda).

## Titreme (cond12_part.py)
7 Ekim 2026: 30. hastalık rehberi `titreme.html` / `en/tremor.html` (bölge: genel). Sıra üşüme sayfasıyla aynı: türler ve araştırma -> tedavi -> günlük hayat
önerileri -> tamamlayıcı yaklaşımlar için kanıt -> altı egzersiz -> videolar. `CTA_CARD` var ("titremeye bağlı günlük yaşam güçlükleri"; NINDS fizyoterapi/iş-uğraşı terapisini sayıyor).
Kaynaklar (okundu): NINDS Tremor (23 Temmuz 2026: 7 tür, ET'de %50–70 kalıtsal, tedaviler), NHS (14 Kasım 2023: neler artırır, ne zaman başvurmalı),
Kavanagh 2016 (10 ET + 9 kontrol, 6 hafta), Sequeira 2012 (6 kişi, kontrolsüz), Shen 2026 (20 RKÇ, 1.067 kişi, hepsi Çin'de). Videolar: IETF (`z-nBScb735E`), VCU Health (`WwIsROk3QA8`).
Üşüme sayfasına videolar eklendi: Johns Hopkins Rheumatology (`Jv0kEFCYF5M`), Avera Health (`yjG_BmcfpNo`).
Günlük hayat önerileri (kapaklı bardak, dirseği dayama, kalın saplı kaşık vb.) yaygın iş-uğraşı terapisi önerileridir; ayrı bir kaynağa dayandırılmadı, iddia içermez.

## Nobel 2026 özel sayfası (nobel_part.py)
7 Ekim 2026: kullanıcının isteğiyle Bilim gündemi'ne özel sayfa: `nobel-2026.html` / `en/nobel-prizes-2026.html` ("Işık, ayna ve buz").
Üç ödül (tıp: optogenetik; kimya: Kagan ve Soai; fizik: Halzen/IceCube), her birinde resmî gerekçe, "tek cümleyle", sade anlatım,
canlandırma, "Dün – Bugün – Yarın" kartları ve "İnsanlık için değeri". Sonda "Üçünün ortak yanı", 4 SSS, kaynaklar. Şema (ld+json) bilerek yok (MedicalWebPage uymuyor).
Canlandırmalar: `#og` (ışık kapısı; düğme "Işığı yak", sayaç), `#mt` (eldivenler üst üste oturmuyor; yalnızca CSS), `#kg` (Kagan çubuğu 56/6/38),
`#so` (Soai nokta ızgarası 50 -> 79 -> 99; sekmeler), `#ic` (IceCube; düğme "Bir nötrino gönder", 4 hazır iz). Görünürken kendi kendine oynar, dokununca durur (`auto()`),
`prefers-reduced-motion`'da otomatik oynatma yok. **SVG içinde yazı yok** (çeviri SVG'leri maskeler); bütün yazılar HTML'de.
Kayıt: `NEWS_PAGES` (üst çubukta "Bilim gündemi" vurgusu), `TOPICS`, `RELATED`, `i18n_map`, `search_index.py` (tür "n"), `NEWS` başına öne çıkan kart (`IL_NOBEL`, `rel` ile sayfaya gider).
`KOSE_PAGES`'te değil: Bilgi köşesi kartı yok, girişi haber kartından. Sınama betikleri: `scratchpad/nb.py`, `nb2.py`.
Kaynak durumu: nobelprize.org 403 verdi (okunamadı; yalnızca bağlantı). Gerekçe cümleleri ve kimyadaki sayılar (%0,00005 -> %57 -> %99; 56/6/38) kullanıcının
gönderdiği resmî Nobel Instagram görsellerinden. Okunan: STAT (tıp), Forbes (kimya; Linke alıntısı), icecube.wisc.edu (2013, 2023 Samanyolu, 450 kişi/14 ülke, Gen2 8 kat, Halzen alıntısı).
CNN ve NPR okunamadı (robots). Hafızadan (doğrulanmadı): kanalrodopsin 2002–2003, Pasteur 1848, Kagan 1986, Soai 1995, Pauli 1930, ilk nötrino 1956,
Halzen'in önerisi 1980'lerin sonu, IceCube 2011, karvon (nane/Frenk kimyonu), Sahel 2021 Nature Medicine künyesi. Portre çizimleri (Nobel'in görselleri) kullanılmadı.
Çeviri: `i18n/done/nobel-2026.json` (87 birim) + fb392–fb397 (haber kartı, "Ekim 2026").

## Yüz felci (cond13_part.py) ve klinik gözlem kutuları
7 Ekim 2026: 31. hastalık rehberi `yuz-felci.html` / `en/bells-palsy.html` (bölge: genel). Ana ileti: ilk 72 saatte kortizon + göz koruma; yüzü zorlamak iyileşmeyi hızlandırmaz.
Bu yüzden "altı egzersiz" değil "altı güvenli uygulama": ilk üçü ilk haftalar için (`fp_eye`, `fp_massage`, `fp_breath`), son üçü hareket geri gelirken (`fp_smile`, `fp_brow`, `fp_lips`).
Yeni yüz çizimleri `_face()` ile üretilir. Videolar Queen Victoria Hospital (`xmnpEpmmiTQ` göz bantlama, `u0pEAFvnUSg` masaj; oEmbed ile doğrulandı, izlenemedi).
Yedekte doğrulanmış videolar: Cleveland Clinic "What Is Bell's Palsy?" (`stS7WAp4n8U`), University Hospital Southampton "Facial exercise programme" (`og33hoO-8AQ`).
Kaynaklar (okundu): NHS (4 Temmuz 2023), NINDS (19 Mayıs 2026), Cochrane kortizon (7 çalışma, 895 kişi, %17'ye karşı %28), Cochrane fizik tedavi (12 çalışma, 872 kişi),
Cochrane akupunktur (6 çalışma, 537 kişi: sonuca varılamadı), Facial Palsy UK (ilk dönem önerileri), Oxford University Hospitals broşürü (Ekim 2025), Berkshire Healthcare broşürü.
Kaynağa dayanmayan, genel bilgiyle yazılanlar: son üç uygulamanın tekrar sayıları (5 tekrar, günde 2–3 kez), "kulak çevresinde ağrılı kabarcıklar" uyarısı, gevşeme nefesinin ayrıntıları.
**Dikkat:** cochrane.org her derlemeyi "2022, Issue 3" diye gösteriyor; yıl oradan ALINMAZ. Bu yüzden Hurkmans (2009;(4)) ve Holland (2012;(10)) künyeleri düzeltildi;
Chen 2010;(8), Deare 2013;(5), Yang 2016;(8), Madhok 2016;(7), Teixeira 2011;(12) yıl/sayıları hafızadan yazıldı (doğrulanmadı).
Aynı gün inme ve fibromiyalji sayfalarına "Akupunktur: araştırmalar ve klinik gözlemim" bölümü eklendi (Cochrane: inme 31 çalışma/2.257 kişi, kanıt düşük–çok düşük;
fibromiyalji 9 çalışma/395 kişi, standart tedaviye eklenince ağrıda ~30 puan, etki 1 ay, 6. ayda yok). Titreme sayfasındaki mevcut bölüme gözlem kutusu kondu.
Parkinson ve MS sayfalarına eklenmedi (kanıt okunmadı; kullanıcı isterse eklenir). Çeviri: `i18n/done/yuz-felci.json` (97 birim) + fb398–fb408.
t_ls kullanımı: İngilizce sayfa adları `en/` ÖNEKSİZ verilir (`t_ls.py <dizin> yuz-felci.html bells-palsy.html 2 cene-eklemi.html jaw-joint-tmd.html`).

## Site Core v2 ve sağlık asistanı (başka oturumdan; üretim hattına işlendi)
7 Ekim 2026'da başka bir oturum `main`e DOĞRUDAN beş commit gönderdi (919acbf … 6263dec): `assets/site-core.css|js`, `assets/health-assistant.*`,
`scripts/site_audit.py`, `.github/workflows/site-audit.yml`, `cloudflare-worker/`, `wrangler.jsonc`, `404.html`, `SITE_CORE_V2.md`; ayrıca bütün sayfalara
site-core bağlantısı, Twitter/X kart üst verileri eklendi ve sayfa içi `@font-face` kaldırıldı. Bu dosyalar `kaynak`ta yok; üretim hattı onlara dokunmaz.
Aynı çıktıyı üretmek için: `build_pages.py` (`CORE_CSS`, `CORE_JS`, twitter üst verileri, `FONTFACE` boş), `to_github.py`, `fb_recete.py` güncellendi;
kalp rehabilitasyonu istatistik cümlesi de onların düzeltmesiyle eşlendi. Denetim: `main`i `origin/main`e eşitleyip hattı çalıştırınca ilgisiz sayfalarda fark çıkmamalı.
Onların betiğindeki bir hata burada düzeltildi: açıklamada kesme işareti olan sayfalarda `twitter:description` yarıda kesiliyordu (ana sayfa, Bilim gündemi, Nobel).
**Her gönderimden önce** `git fetch origin main` ve `git log origin/main` ile yeni doğrudan değişiklik var mı bak; varsa önce üretim hattına işle, sonra gönder.

## Kalça yan ağrısı ve lenfödem (cond14_part.py)
7 Ekim 2026: iki rehber birden. `kalca-yan-agrisi.html` / `en/lateral-hip-pain.html` (Hastalık rehberi, bölge: diz) ve `lenfodem.html` / `en/lymphoedema.html` (Rehabilitasyon rehberi).
Kalça yan ağrısı: LEAP çalışması (Mellor, BMJ 2018; 204 kişi; 8. hafta %77/%58/%29, 52. hafta %79/%58/%52; okundu) + NHS Fife broşürü (Şubat 2025; alışkanlıklar ve beş egzersiz; okundu).
Altıncı hareket (`gt_sls`, leğen düz tek ayak) ve dozu kaynakta yok; LEAP'in "işlev sırasında kalça kontrolü" ilkesine dayanarak yazıldı. Uyarı işaretleri genel bilgi.
Videolar: Somerset NHS Foundation Trust (`z9w5axHITms`), UC San Diego Health (`xqPew4-Pq54`). Yeni çizim: `gt_belt`.
Lenfödem: NHS (genel, tedavi, önleme; 29 Mart 2023), Cancer Research UK egzersiz sayfası (20 Mayıs 2026; hareketler ve tekrar sayıları buradan), Cochrane Stuiver (10 çalışma, 1.205 kişi;
dirençli egzersiz 2 çalışma/358 kişi; yıl/sayı 2015;(2) hafızadan), NCI PDQ (18 Aralık 2024: %19,9'a karşı %5,6; ACSM görüşü). Hepsi okundu. "Tek bacakta ani şişlik" ve "nefes darlığı" uyarıları genel bilgi.
Bu sayfada bilerek `CTA_CARD` yok (lenfödem bakımı özel eğitim ister; kullanıcı isterse eklenir); yerine lenfödem terapisti notu var. Videolar: Cancer Research UK (`Rku5PGz48c8`, `zcQB6pZmdN0`).
Yeni çizimler: `ly_shrug`, `ly_arm`. Yedekte doğrulanmış: Macmillan "Lymphoedema explained" (`68NgrFiQkeU`). Çeviri: kalca-yan-agrisi (75), lenfodem (87) + fb411–fb413.
Not: bu kabuktan youtube.com'a curl ile erişilemiyor; oEmbed doğrulaması WebFetch ile yapılır.

## De Quervain ve diyabetik nöropati (cond15_part.py)
8 Ekim 2026: `de-quervain.html` / `en/de-quervains-tenosynovitis.html` (bölge: omuz) ve `diyabetik-noropati.html` / `en/diabetic-neuropathy.html` (bölge: ayak).
De Quervain: beş NHS hastane broşürü okundu (Gloucestershire Tem 2024: 3 kat, 30–55 yaş; Plymouth Ara 2023: atel 3–8 hafta, aşamalı egzersizler; Dorset Nis 2025: 6 hafta + 2–4 hafta bırakma;
Leicestershire Tem 2021: dört egzersiz ve dozları; Sherwood Forest Oca 2026: 20 dk soğuk x3) + Cochrane kortizon iğnesi (1 çalışma, 18 kişi, 9/9'a karşı 0/9; çok düşük kesinlik; yıl/sayı 2009;(3) hafızadan).
Kaynakta olmayan: "bebeği kucağa alırken bilekleri düz tutun, yükü ön kollara yayın" (broşürlerdeki "bileği yana büken hareketlerden kaçının" önerisinin uygulaması) ve uyarı işaretleri.
Yeni çizimler: `dq_hammer`, `dq_band`, `dq_wrist`. Videolar: Mayo Clinic (`o0KSfDuy3i0`), Doctor O'Donovan (`RdtJdUSIaVQ`; İngiltere'de hekim, kişisel kanal).
Diyabetik nöropati: NIDDK periferik nöropati (Şubat 2018) ve ayak sorunları (Ocak 2017) sayfaları, Lima 2021 (8 RKÇ, 457 kişi; denge ve düşme korkusu biraz iyileşti, düşme riski değişmedi; SciELO'dan okundu),
Wang 2025 (21 RKÇ; PEDro kaydından özet okundu). Egzersizler düşme önleme sayfasındakilerin uyarlaması. "Açık yara varken üzerine basarak egzersiz yapmayın" genel bilgi.
Videolar: Diabetes UK (`jC9hXPURsQA`), Mayo Clinic (`SulNOSMMNLY`). Bu sayfaya akupunktur/klinik gözlem kutusu konmadı (kanıt okunmadı). Çeviri: de-quervain (80), diyabetik-noropati (81) + fb414–fb417.

## Düztabanlık ve omurilik yaralanması (cond16_part.py)
8 Ekim 2026: `duztabanlik.html` / `en/flat-feet.html` (Hastalık rehberi, bölge: ayak) ve `omurilik-yaralanmasi.html` / `en/spinal-cord-injury.html` (Rehabilitasyon rehberi).
Düztabanlık: NHS (24 Haziran 2025: çoğu zaman tedavi gerekmez, beş başvuru durumu, 3–10 yaş), Cochrane Evans 2022 (16 RKÇ, 1.058 çocuk; ağrısız düztabanlıkta özel tabanlık 67/100'e karşı ayakkabı 79/100),
NHS Borders PTTD broşürü (altı egzersizin beşi ve dozları buradan; "tek ayakla topuk yükseltme" aynı broşürdeki ilerletme). Hepsi okundu. Yeni çizimler: `ff_short`, `ff_press`.
Videolar kurum değil kişi kanalı: Doctor O'Donovan (`B5KbzQf5HdU`), Rehab Science / Dr. Tom Walters (`vcx_NNR7b1k`); kurum kanalı bulunamadı.
Omurilik yaralanması: DSÖ bilgi notu (16 Nisan 2024), NINDS (13 Mart 2026), Martin Ginis 2018 egzersiz kılavuzu (211 çalışma; 20 dk x2 + güçlendirme x2; 30 dk x3), MSKTC/UW bası yarası ve
basınç azaltma sayfaları (2009: günde 2 kontrol, 15–30 dk'da bir 30–90 sn, yatakta 2–6 saatte bir dönme, itme hareketi omuz için riskli), RNOH otonom disrefleksi. Hepsi okundu.
Kaynakta olmayan: egzersiz seçenekleri cümlesi (kol ergometresi vb.), "omuzlar bacaklarıdır" benzetmesi, kürek çekme/kürek sıkıştırma/nefes/öne uzanma hareketlerinin seçimi ve tekrar sayıları, uyarı listesinin bir kısmı.
Yeni çizimler (oturarak): `sc_sidelean`, `sc_row`, `sc_scap`. Videolar: Shepherd Center (`ibrZzDZb-PU`, `-Ew-N5Ux0Ns`). Akupunktur/klinik gözlem kutusu konmadı (kanıt okunmadı).
İnme sayfasının ilgili bağlantıları üçe çıktı (omurilik eklendi). Çeviri: duztabanlik (79), omurilik-yaralanmasi (90) + fb418–fb419.

## Halluks valgus ve tetik parmak (cond17_part.py)
8 Ekim 2026: `halluks-valgus.html` / `en/bunions.html` (bölge: ayak) ve `tetik-parmak.html` / `en/trigger-finger.html` (bölge: omuz).
Halluks valgus: NHS (12 Haziran 2023: kendi başına geçmez; ayakkabı, ped, buz 5 dk; ameliyat sonrası süreler), Cochrane Dias 2024 (25 RKÇ, 1.597 yetişkin; ameliyat-izlem ağrı 21'e karşı 39; kesinlik düşük),
ABUHB Eylül 2026 (kadınlarda 3 kat, parmak arası silikon, tabanlık, kilo), Gateshead Ekim 2020 (egzersizin ilerlemeyi önlediğine kanıt yok; başparmak germe 10–15 sn; gece ateli kanıtı zayıf),
Livewell Eylül 2025 (ayakkabı, baldır germe 30 sn günde 5–10), NHS Borders Mart 2016 (6–12 hafta; ameliyat için en az 3 ay). Hepsi okundu.
Sayfa egzersizin çıkıntıyı düzeltmediğini açıkça söyler; altı hareketin ilk ikisi broşürlerden, diğer dördü genel ayak güçlendirme (kaynaksız, sayfada böyle yazıyor). Yeni çizim: `hv_toe`.
Videolar: Manipal Hospitals (`YCmqXvTmfFI`), Human 2.0 Fitness / ortopedi cerrahı Dr. Chris Raynor (`RSefS_rHugY`; kişi kanalı).
Tetik parmak: NHS (17 Kasım 2025), NHS Scotland ulusal broşürü (iğne %70–80; ameliyat ayrıntıları), North Tees (iki hareket, günde 4–5; 12 hafta), Torbay Eylül 2025 (ılık su, buz masajı, üç hareket, gece ateli),
St George's Nisan 2020 (%2–3, kadın, 40 yaş üstü), Cochrane iğne (2 RKÇ, 63 kişi; 37/100'e karşı 17/100; yıl/sayı 2009;(1) hafızadan). Hepsi okundu; altı uygulamanın hepsi broşürlerden.
Kaynakta olmayan: enfeksiyon ve yaralanma uyarıları. Yeni çizimler: `tf_warm`, `tf_ice`, `tf_table`, `tf_passive`, `tf_splint`. Videolar: Mayo Clinic (`58xQr9tOx24`), Doctor O'Donovan (`89ACJJ-jsfA`).
Çeviri: halluks-valgus (76), tetik-parmak (69) + fb420–fb421.

## Golfçü dirseği ve Guillain-Barré (cond18_part.py)
8 Ekim 2026: `golfcu-dirsegi.html` / `en/golfers-elbow.html` (bölge: omuz) ve `guillain-barre.html` / `en/guillain-barre-syndrome.html` (Rehabilitasyon rehberi).
Golfçü dirseği: NHS Fife (Şubat 2025: yedi egzersiz ve dozları, buz 10 dk x3–4, bant, iğne az kişide kısa vadeli; spor yapmayanlarda daha sık, kadın=erkek) ve Plymouth broşürü
(Eylül 2019: 30–50 yaş, belirtiler, golf tekniği, eksantrik 3x10). Altı egzersizin hepsi Fife broşüründen. Kaynakta olmayan: uyarı işaretleri. Araştırma kanıtı (RKÇ/derleme) okunmadı; sayfa da iddia etmiyor.
Yeni çizimler: `ge_rot`, `ge_con`. Videolar: CommonSpirit Houston (`m8YtVpSR1Bk`), Rehab Science (`yTPQEW1aTTI`). Sayfada tenisçi dirseği rehberine iç bağlantı var.
Guillain-Barré: NHS (12 Ağustos 2024), DSÖ (24 Ekim 2025: 3'te 1 solunum), NINDS (13 Mart 2026: %90'ı 3. haftada en zayıf; pasif hareket, hedefli güçlendirme), Cochrane IVIG (Hughes 2014: IVIG = plazma değişimi),
Kiper 2025 kapsam derlemesi (16 çalışma; PEDro kaydından özet: güç, yorgunluk, bağımsızlık "olabilir"; güvenlik verisi kayıtta yok, bu yüzden "zarar göstermiyor" denmedi). Hepsi okundu.
Kaynakta olmayan: altı egzersizin seçimi ve tekrar sayıları, "ertesi gün yorgunluk artarsa azaltın" kuralı, uyarı listesinin bir kısmı.
Tek video: Mayo Clinic Radio (`HtkWhtG-MCM`); Mayo'nun diğer videosu (`qtKXD411CeA`) gömmeye kapalı (oEmbed 401). t_ls bu sayfada video sayısı 1 ile çalıştırılır.
Çeviri: golfcu-dirsegi (74), guillain-barre (68) + fb422–fb424.

## Sarkopeni ve demansta egzersiz (cond19_part.py)
8 Ekim 2026: `sarkopeni.html` / `en/sarcopenia.html` (Hastalık rehberi, bölge: genel) ve `demans-egzersiz.html` / `en/dementia-and-exercise.html` (Rehabilitasyon rehberi).
Sarkopeni: Cochrane Liu & Latham 2009 (121 RKÇ, 6.700 kişi; haftada 2–3, orta-yüksek şiddet; güç, sandalyeden kalkma, yürüme hızı +0,08 m/sn, kireçlenmede ağrı; ciddi yan etki nadir),
EWGSOP2 özeti (Cruz-Jentoft 2019: önce kas gücü; kütle düşükse doğrulanır; performans düşükse ağır), Cleveland Clinic (2 Nisan 2026: 30'lu–40'lı yaşlarda başlar, 65–80 hızlanır, on yılda %8'e kadar;
belirtiler, risk etkenleri, SARC-F beş başlık 0–2 puan, 4 ve üzeri ileri inceleme; öğün başına 20–35 g protein; onaylı ilaç yok), Harvard Health (14 Ağustos 2024: 80 üstünün yaklaşık yarısı;
protein tek başına yetmez; böbrek uyarısı; güne yayma), NHS Strength exercises (28 Şubat 2024: altı egzersizin hepsi ve tekrar sayıları buradan). Hepsi okundu.
Hafızadan / kaynaksız: SARC-F sorularının ayrıntılı ifadesi ve puan seçenekleri (Malmstrom 2013'ten hafızadan; Cleveland yalnızca başlıkları veriyor), tanı testlerinin tek cümlelik açıklamaları,
"yürüyüş yeterli mi" yanıtındaki yürüyüş cümlesi, uyarı işaretleri listesi. Sayfa derlemenin yalnızca sarkopeni tanılı kişileri kapsamadığını açıkça söylüyor.
Yeni çizimler: `sk_push` (duvar şınavı), `sk_curl` (ağırlıkla kol bükme). Videolar: Mayo Clinic (`ymcFS1tQrsk`), National Institute on Aging (`TOKxtgKrGCQ`); izlenmedi.
Demans: Cochrane Forbes 2015 (17 RKÇ, 1.067 kişi; günlük işler iyileşebilir, kanıt çok düşük; biliş, davranış, depresyonda belirgin yarar yok; tek çalışmada bakım yükü azaldı; zarar bulgusu yok),
DSÖ (3 Temmuz 2026: 57 milyon, %60–70 Alzheimer, erken belirtiler, ilaç dışı yaklaşımlar, bakım verenler günde ortalama 5 saat), Alzheimer's Society üç sayfa (ilerlemeyi yavaşlattığı gösterilmedi;
etkinlik türleri, oturarak egzersiz listesi, konuşma testi, ısınma, 150 dk/hafta hedefi, kime danışılmalı, ne zaman durmalı, yalnız yürüyüş güvenliği, takvim ve adımları yazma). Hepsi okundu.
Kaynaksız: altı hareketin tekrar sayıları, "hareketi önce siz gösterin" önerisi, uyarı işaretleri listesi (ani şaşkınlık vb.). Sayfa egzersizin demansı durdurmadığını açıkça söyler; iğneleme/akupunktur yok.
Yeni çizimler: `dm_march`, `dm_toe`, `dm_arm`. Videolar: NHS Greater Glasgow and Clyde (`VhnkOhAWf-Q`, `YA5xvvoaVa8`); izlenmedi.
İlgili bağlantılar: kemik-erimesi → sarkopeni, parkinson → demans-egzersiz. Çeviri: sarkopeni (109), demans-egzersiz (110) + fb425–fb426.
Not: `publish.sh` her çağrıda `up40/_home_*.txt` dosyalarını siler; aynı derlemeden ikinci sayfayı yayımlamadan önce `build_pages.py` + `rebuild_home.sh` yeniden çalıştırılmalı (yoksa ikinci sayfa site haritasına eklenmez).

## Galeri başlığı (9 Ekim 2026)
Ana sayfadaki "Evde bir seansın hikâyesi" başlığı kullanıcı isteğiyle "Bir seansın hikâyesi" oldu (fb_misc.py); EN: "The story of a session" (fb32, fb_tr_en.py).

## Dizin 12 Sırrı (knee12_part.py) — 10 Ekim 2026
`dizin-12-sirri.html` / `en/knee-12-secrets.html` (Kendine iyi bak; SELF listesinin başında, "Zamanlayıcıyla birlikte yapın" grubunda). Diz kireçlenmesi rehberinden ve RELATED'dan bağlantı var.
Kullanıcı isteği: egzersiz uyumunu artıran, merak uyandıran, benzersiz bir egzersiz deneyimi. Yapı: söz kartı (gün/saat/"neyin ardından"/yalnızca egzersizde dinlenecek şey),
30 sn sandalyeden kalkma ölçümü (başta, 6. ve 12. seansta), sesli sayan seans oynatıcı (tempo, tutma, sağ/sol, dinlenmede "sırrın kilidi %"), ağrı trafik ışığı (5/10 ve 24 saat kuralı),
seans sonunda kilit açılma animasyonu ve sır kartı + bir sonraki sorunun ön gösterimi, harita (3 bölüm × 4 kilit), haftalık 2 seans halkası, .ics takvim, WhatsApp'la bir yakına söyleme (numarasız wa.me).
Veriler yalnızca localStorage'da (anahtar drihsaneren.diz12.v1). Arayüz metinlerinin hepsi gizli `.d12-s [data-k]` kaplarında; betikte görünen metin yok (EN hattı için).
Okunan kaynaklar: Cochrane 2024 (139 RKÇ, 12.468 kişi; ağrı ~13, işlev ~12,5 puan), Jack 2010 özeti (engeller), Bedson 2008 (%15–76 / %15–81), Øiestad 2022 (OR 1,85 / 1,43; kanıt düşük),
ELHT NHS diz ağrısı sayfası (<5/10, bir günde geçmeli; >5 ya da >24 saat → azalt), UCL haberi (Lally: 66 gün, tek kaçırma etkilemedi), Messier 2005 (1'e 4), Wharton haberi (Milkman: %51),
ikincil kaynak (Gollwitzer & Sheeran: 94 test, d=0,65), CDC STEADI 30 sn testi (2017). NICE NG226 bilgisi diz rehberinde daha önce okunmuştu.
Hafızadan: Lawford ilk yazar (Cochrane 2024), Jack 2010 yazar listesi, Lally/Gollwitzer/Milkman cilt-sayfa bilgileri. Kaynaksız/genel: "başlamadan önce danışın" listesi, ısınma adımı, tempo süreleri, tekrar artış kuralı.
Program hareketleri ve anlatımları diz rehberindekilerle aynı (EXT yeniden kullanıldı, d12_ kopyaları programa özgü dozlarla). Çeviri: dizin-12-sirri (217) + fb427–fb428.

## Ruh sağlığı turu (mind_part.py) — 10 Ekim 2026
Kullanıcı isteği: "Kendine iyi bak" bölümüne psikoloji için içerik. Seçtiği dört iş: egzersizle ruh sağlığı rehberi, ruh hâli ölçümü (WHO-5 + PHQ-4), zamanlayıcılı kas gevşetme, küçük adım planlayıcı (davranışsal aktivasyon).
Ana sayfadaki "Kendine iyi bak ne işe yarar?" kutusuna yeni grup: **Ruh sağlığı için** (fb430 "For mental health"); DOST molası ve Stres bu gruba taşındı. Kayıt betiği: scratchpad/mind/reg_mind.py.
1) `ruh-sagligi-egzersiz.html` / `en/exercise-for-mental-health.html`. Okunan kaynaklar: Noetel 2024 BMJ (218 çalışma, 14.170 kişi; g: dans −0,96 [5 çalışma], yürüyüş/koşu −0,62, yoga −0,55, güç −0,49, karma aerobik −0,43, tai chi −0,42;
CBT ile benzer; şiddet arttıkça etki; yoga/güç daha az bırakma; cinsiyet/yaş alt grupları; CINeMA güven düşük/çok düşük), Singh 2023 BJSM (97 derleme, 1.039 RKÇ, 128.119 kişi; depresyon −0,43, kaygı −0,42; yüksek şiddet ve ≤12 hafta daha etkili),
Pearce 2022 JAMA Psychiatry (15 çalışma, 191.130 kişi; 8,8 mMET-sa/hafta ≈ 2,5 sa tempolu yürüyüş %25, yarısı %18), Göteborg Üniversitesi haberi (Henriksson: 286 kişi, 12 hafta, 3×60 dk fizyoterapist eşliğinde devre; 3,62 / 4,88 kat),
NICE NG222 öneriler sayfası (grup egzersizi: haftada 1'den fazla, 10 hafta, ~8 kişi), DSÖ fiziksel aktivite (26 Haziran 2024), NHS Exercise for depression (16 Nisan 2026), NHS Depression overview (5 Temmuz 2023). Hepsi okundu.
Hafızadan: Singh bitiş sayfası 1209, Henriksson cilt-sayfa (2022;297:26–34) ve yazar listesi, NICE NG222 yayın yılı 2022, etki büyüklüğü eşikleri (0,2/0,5/0,8, Cohen), "konuşabilir ama şarkı söyleyemezsiniz" tempo tarifi (NHS orta şiddet tanımı).
Kaynaksız/genel: altı hareketin dozları, "gün ve saati baştan belirleyin" önerisi, uyarı işaretleri listesinin ifadesi (112 Türkiye acil). Hareket çizimleri mevcut (walk, sidestep, sts, sk_push, cat, childp). Çeviri: ruh-sagligi-egzersiz (93) + fb429–fb430. stres.html'in ilgili bağlantılarına eklendi.
2) `ruh-hali-olcumu.html` / `en/mood-check.html` (Ruh sağlığı için grubu). WHO-5 (5 soru) + PHQ-4 (4 soru), soru soru ilerleyen araç; sonuç: iki gösterge, alt puanlar, dört düzeyli öneri (g/m/y/r), her zaman 112 kutusu,
isteğe bağlı kayıt (localStorage `drihsaneren.ruhhali.v1`, en çok 26 kayıt, WHO-5 değişimi ≥10 "anlamlı"), iki hafta sonrası için .ics, tümünü sil. Düzey kuralı: r = WHO-5 ≤28 ya da PHQ-4 ≥9; y = WHO-5 ≤50 ya da PHQ-4 ≥6 ya da alt puan ≥3; m = PHQ-4 3–5 ya da bir WHO-5 maddesi 0/1; g = diğer.
WHO-5 Türkçe metni resmî PDF'ten birebir (psykiatri-regionh.dk WHO5_Turkish.pdf: başlık, yönerge, 5 madde, 6 seçenek, puanlama: ham <13 ya da bir madde 0/1 → ayrıntılı değerlendirme, %10 değişim). İngilizce metin INSPQ sayfasından birebir doğrulandı.
PHQ-4 İngilizce metni ve "izin gerekmez" notu SRA Lab PDF'inden; puan aralıkları (0–2/3–5/6–8/9–12, alt puan ≥3) Oregon Pain Guidance PDF'inden. PHQ-4'ün resmî Türkçesi okunamadı (phqscreeners erişilemedi): Türkçe ifadeler bu sayfa için çevrildi ve sayfada böyle yazıyor.
Topp 2015 (213 makale; ≤50 duyarlılık 0,86 özgüllük 0,81 [18 çalışma]; ≤28 majör depresyon düzeyi; Danimarka ortalaması ~70; 10 puan) ve Eser 2019 (1.752 kişi; α 0,81/0,86) okundu. Kroenke 2009 özeti (2.149 hasta, 15 klinik) okundu; dergi cilt-sayfa (Psychosomatics 2009;50(6):613–621) hafızadan.
Çeviri belleği notu: "Her zaman" ve "Bazen" başka sayfalarda "Always"/"Sometimes" diye çevrili olduğundan WHO-5 seçeneklerinde sonlarına görünmez U+2060 (&#8288;) eklendi; böylece EN'de resmî "All of the time"/"Some of the time" çıkıyor.
t_ls bu sayfada "egzersiz=0" diye 6 sorun sayar; sayfada egzersiz ızgarası olmadığı için beklenen durum. Çeviri: ruh-hali-olcumu (126) + fb431. check.py'nin Eser/Kroenke kaynakça satırlarındaki "Türkçe karakter" uyarısı yazar adlarından (Çevik, Löwe).
3) `kas-gevsetme.html` / `en/progressive-muscle-relaxation.html` (Ruh sağlığı için grubu). Sesli zamanlayıcı: giriş 10 sn, her bölge 4 sn hazırlık + 5 sn sık + 10/20 sn bırak, kapanış 20 sn; tam 18 bölge (~6:12), kısa 7 bölge (~2:43).
Önden insan çizimi (`.rg[data-g]`): hazırlıkta altın çerçeve, sıkarken titreşen altın, bırakınca yeşil, bitenler soluk yeşil. speechSynthesis (tr-TR/en-GB) + kısa sesler; "Sesli yönlendirme" kutusu ikisini birden açıp kapatır. Adım metinleri sayfadaki iki listeden (#pm-full, #pm-short) okunur (EN hattı için).
Okunan kaynaklar: Muhammad Khir 2024 PRBM (46 çalışma, 3.402 kişi, 16 ülke; 24 stres/21 kaygı/11 depresyon destekliyor; seans 5–28 dk; süre ve sıklık sonucu belirgin değiştirmedi; birleşik yöntem daha belirgin; meta-analiz yok), Manzoni 2008 BMC Psychiatry (27 çalışma; d .57 / .51; uzun ve evde pratik daha etkili),
CCI Batı Avustralya PMR sayfası (≈5 sn sık, ≈10 sn bırak; 18 adımın sırası ve tarifleri; uyarılar: yaralanma/kas ağrısında önce hekim, ağrıtmadan, boyunda dikkat, baldırda kramp, ağır yemek/alkol sonrası değil), UCLH Relaxation techniques (29 Mayıs 2024), Anxiety Canada/HeretoHelp,
AJMC haberi (AASM 2021: gevşeme tedavisi koşullu öneri, BDT-U güçlü). Hafızadan: Edinger 2021 cilt-sayfa (17(2):255–262), Khir yazar listesi (dergideki ilk ad "Muhammad Khir"), Jacobson'ın "1930'lar" (Khir'de 1938 kaynak). Kaynaksız/uyarlama: kısa sürümün bölge birleştirmeleri, 4 sn hazırlık, 20 sn seçeneği, giriş/kapanış metinleri.
Çeviri: kas-gevsetme (116) + fb432–fb434. ic-cekis'in ilgili bağlantılarına eklendi. t_ls yine yalnızca "egzersiz=0" sayar.
4) `kucuk-adimlar.html` / `en/small-steps-planner.html` (Ruh sağlığı için grubu; dost-molasi'nin ilgili bağlantılarına eklendi). Davranışsal aktivasyon planlayıcısı: tür (Gündelik/Gerekli/Keyif veren, ELFT NHS sınıflaması) + öneri çipleri ya da serbest metin,
gün(ler) + Sabah/Öğle/Akşam, haftalık plan (bugün vurgulu), "Yaptım" → öncesi/sonrası 0–10 ruh hâli puanı, özet (bu hafta yapılan, ortalama değişim, en çok iyi gelen, son 8 kayıt), haftalık tekrarlı .ics (RRULE; 09/13/19), tümünü sil. localStorage `drihsaneren.adimlar.v1` (en çok 12 adım, 200 kayıt).
Okunan kaynaklar: Ekers 2014 PLoS One (26 RKÇ, 1.524 kişi; kontrole göre SMD −0,74; ilaca göre −0,42 [4 çalışma]; kalite düşük, izlem kısa), NIHR Evidence COBRA özeti (440 yetişkin; 5 gün eğitimli çalışanlar; PHQ-9 17,7→8,4 / 17,4→8,4; ~%21 ucuz), NICE NG222 öneriler (bireysel BA seçeneklerde),
ELFT NHS BA broşürü (kısır döngü; rutin/gerekli/keyifli; kolaydan zora; ne-ne zaman-nerede-kimle; önce/sonra ruh hâli %0–100; motivasyonu beklemeden), Healthy WA (keyif ve başarı; küçült; süre hedefi; "action is the first step"). Hafızadan: COBRA Lancet cilt-sayfa (388(10047):871–880).
Kaynaksız/uyarlama: öneri çiplerinin seçimi, 0–10 ölçek (ELFT 0–100 kullanıyor), saat eşlemesi, "haftaya 3–5 adım" önerisi. Çeviri: kucuk-adimlar (99) + fb435–fb437 (fb437: ana sayfadaki "Kendine iyi bak ne işe yarar?" özetine "ruh sağlığı" eklendi; fb348'in yerini aldı).
- (11 Ekim 2026) Kullanıcı isteği, SONRA yapılacak: ruh sağlığı sayfalarına da "Dizin 12 Sırrı"ndaki gibi merak uyandıran, oyunlaştırılmış, sürdürmeyi destekleyen deneyimler.

## Bilim gündemi: 4 haber (11 Ekim 2026)
Kullanıcı seçti: (1) Uyku evreleri ve 83 hastalık — PLOS Medicine 17 Eylül 2026 (Luo J … Chen R; UK Biobank 95.559 kişi, 7 gün bilek ölçümü, ortanca 8,9 yıl; REM IQR 47,6 dk: kalp yetmezliği HR 0,74, demans 0,54; derin uyku 7 hastalık; <5 sa 37 hastalık; 6–8 sa en düşük) + Science Media Centre uzman görüşleri (ölçüm doğruluğu, ters nedensellik) okundu, PLOS sayfası okunamadı (ScienceDaily + SMC'den).
(2) Sinir-kas kavşağı ve sarkopeni — JCI 1 Eylül 2026 (Arnold WD … Clark BC) özeti + ScienceDaily/Missouri (ignaseclant CMT denemesi). (3) Ultra işlenmiş gıda ve uyluk kası yağlanması — RSNA 14 Nisan 2026 (Radiology, Akkaya; 615 kişi, OAI, %41 UİG, Goutallier). (4) Lakozamid ve kıkırdak — Yale 2 Haziran 2026 + ScienceDaily (Bioactive Materials 2026;61:640; hayvan/hücre).
Not: ScienceDaily'de Ekim 2026'da görünen Stanford 15-PGDH kıkırdak çalışması aslında Kasım 2025'te yayımlanmış (Science); eklenmedi. Haberler tarih sırasına göre NEWS listesine yerleştirildi (uyku ve kas: Eylül; lakozamid: Haziran; UİG: Nisan).
Çizimler: IL_SLEEPST, IL_NMJ, IL_UPF, IL_LACO. Çeviri: i18n/todo|done/yen4.json (y4-1…y4-19). Eksik birimleri tam metinle dökmek için scratchpad/mind/dump_miss.py yazıldı.

## Bel kayması (cond20_part.py) — 11 Ekim 2026
`bel-kaymasi.html` / `en/spondylolisthesis.html` (Hastalık rehberi, bölge: bel; dar-kanal ↔ bel-kaymasi ilgili bağlantı). Kullanıcı: kullanım %91, rehberler "birer birer" eklenecek.
Okunan kaynaklar: Cleveland Clinic (15 Ağustos 2024: türler, risk etkenleri, belirtiler, röntgen/BT/MR, ameliyatsız tedavi, 10 gün ağrı kesici uyarısı, korse kırıkta, ameliyat ölçütleri, acil belirtiler), MSD Manual (Kasım 2024: 5 tip, L5–S1 en sık, dejeneratif kadınlarda 6 kat, derece I–IV %25'lik, eğilme filmleri, stabilizasyon egzersizi, genellikle kararlı),
The Bottom Line özeti (Försth 2016 NEJM: 247 hasta, füzyon eklemek 2 yılda fark yok, yatış 4,1→7,4 gün, maliyet +6.800 $). Hafızadan: Försth yazar listesi ve cilt-sayı (374(15)). Kaynaksız: altı egzersizin tarif ve dozları, "kasık/makat uyuşması" acil belirtisi (genel kauda ekina bilgisi). Video yok.
Çeviri: bel-kaymasi (81) + fb438–fb439. check.py'deki tek uyarı yazar adı (Försth).

## Huzursuz bacak sendromu (cond21_part.py) — 11 Ekim 2026
`huzursuz-bacak.html` / `en/restless-legs-syndrome.html` (Hastalık rehberi, bölge: genel; uyku.html ilgili bağlantılarının başına eklendi). Okunan kaynaklar: NHS (22 Eylül 2025: belirtiler, nedenler, kendi kendine önlemler, ilaçlar, ne zaman GP),
AASM özet sayfası (13 Kasım 2024: demir değerlendirmesi herkese; IV ferrik karboksimaltoz güçlü, oral demir koşullu; gabapentinoidler güçlü; dopamin agonistleri çoğu kişide koşullu karşı, kabergolin güçlü karşı; opioid ve iki taraflı yüksek frekanslı peroneal uyarım koşullu),
HCPLive (Winkelman yazar listesi, augmentasyon yılda %7–10, 5 yılda %35–50; ferritin >100 ve TSAT >20 hedefi — sayfada kullanılmadı), Aukerman 2006 özeti (41 randomize, 23 tamamlayan; 12 hafta, haftada 3 gün aerobik + alt ekstremite direnç; anlamlı düzelme).
Kaynaksız/genel: egzersiz dozları, kramp tarifi, "tek taraflı şişlik ve ağrı" uyarısı (DVT), "ileri böbrek yetmezliği" vurgusu (AASM'de ESRD özel grubu). Çeviri: huzursuz-bacak (83) + fb440–fb441.

## 11 Ekim 2026 akşam: e-posta, yumuşak dil, karekod
- Sitedeki e-posta `ihsan@drihsaneren.com` oldu (ImprovMX ile ihsneren@gmail.com'a yönleniyor): fb_misc.py, fb_book.py, schema_home.json, site/index.bak_fb.html, i18n index + manual_index. Sitede Gmail adresi kalmadı.
- Kullanıcı isteği: "Kararı hekiminizle birlikte verin" gibi keskin emir cümleleri yerine "-ebilirsiniz". Dört yerde değişti (omuz sıkışması, ön çapraz bağ, halluks valgus, uyku); EN karşılıkları "You can …" yapıldı. Yeni yazılarda karar/tercih cümlelerinde bu üslup kullanılmalı (egzersiz tarifleri emir kipinde kalabilir).
- Karekod (fb_qr.py, iletişim bölümü, bilgisayarda sağ altta): ilk denemede çok şey kaldırıldı, kullanıcı beğenmedi ("eskisi çok iyiydi"). SON HÂL: eski tasarım aynen geri alındı; yalnızca minik yıldız parıltıları (nq-sp) ve çapraz cam parıltısı (nq-shine) kaldırıldı. Dönen kenar ışığı, ışık dalgası (nq-lt), imleç parlaması ve 14° eğilme duruyor.
  t_nq3: 43/44 karede okundu (0. kare açılış animasyonu).
- LinkedIn (11 Ekim 2026): kullanıcı sitede LinkedIn bağlantısı İSTEMİYOR (eklenip aynı gün geri alındı). Profil: https://www.linkedin.com/in/ihsaneren/ (yalnızca bilgi).

## Kuyruk sokumu ağrısı (cond22_part.py) — 11 Ekim 2026
`kuyruk-sokumu-agrisi.html` / `en/tailbone-pain.html` (Hastalık rehberi, bölge: bel; bel-agrisi'nin ilgili bağlantılarının başına eklendi). Okunan kaynaklar: NHS Tailbone (coccyx) pain (20 Kasım 2025: belirtiler, nedenler, ev önlemleri, fizyoterapi/iğne/ameliyat, ne zaman GP),
Mazzoleni 2025 Ann Joint sistematik derleme (16 çalışma, 858 hasta, %77 kadın; ESWT, enjeksiyon, ganglion impar, RF, koksijektomi %70,4 MCID; ~%90 ameliyatsız düzelme önceki literatürden), Patel 2008 Curr Rev Musculoskelet Med derlemesi (kullanıcı PDF olarak yükledi: kadınlarda 5 kat, başlangıç 40 yaş, obezite 3 kat, dinamik röntgende %70'e kadar bozukluk, normal 5–25°, Fogel protokolü <2 ay 8 hafta, Wray iğne %59 / iğne+manipülasyon %85, koksijektomi %60–91, yara enfeksiyonu %22'ye kadar).
Not: Springer sayfası WebFetch'te 429 verdi; proxy "bu sayfayı yeniden çekme" dedi. Kullanıcı PDF'i yükleyince okundu. Kaynaksız: minder biçimi önerisi genel tutuldu, egzersiz dozları. Üslup: karar cümleleri "-ebilirsiniz".
Çeviri: kuyruk-sokumu-agrisi (62) + fb443–fb456.

## Boyun düzleşmesi rehberi (11 Ekim 2026, 5 yeni rehberin 1.si)
- boyun-duzlesmesi.html → en/straight-neck.html (cond23_part.py). Egzersizler mevcut boyun anahtarları (chin, rot, side, scap, thor, wallpost).
- Okunan kaynaklar: Grob 2007 ve McAviney 2005 (ikisi de PainScience özetinden; makalelerin tam metni okunamadı), NHS Neck pain (27 Nisan 2023).
- Kaynaksız / genel bilgi: ekranı göz hizasına yaklaştırma önerisi, baş dönmesi SSS'sindeki ifade, kırmızı bayraklardaki ateş/kilo kaybı/kaza maddesi.
- Kartlarda yeni metin: fb457. Sıradaki: kalça sıkışması (FAI), atlet dizi, omuz çıkığı, piriformis.

## Kalça sıkışması (FAI) rehberi (11 Ekim 2026, 5'in 2.si)
- kalca-sikismasi.html → en/hip-impingement.html (cond24_part.py). Egzersizler: ptilt, fai_hslide (yeni metin, hslide çizimi), bridge, abd, sideplank, sls.
- Okunan kaynaklar: Warwick Agreement 2016 (BJSM tam metin), NIHR Evidence UK FASHIoN özeti (2 Ekim 2018; Lancet makalesi okunmadı), MPFT NHS kalça sıkışması sayfası (tarihsiz), George Eliot NHS broşürü (20 Ağustos 2025).
- Kaynaksız / genel bilgi: köprü, yan köprü, yan yatarak bacak kaldırma, tek ayak denge seçimi (genel kalça güçlendirme; NHS sayfası pelvik eğme ve topuk kaydırmayı veriyor), "kasıkta sıkışma hissetmeden önce durun", çorap/araba önerisi.
- Kayıt artık scratchpad/reg_cond.py + cNN.py ile yapılıyor. Kartlarda: fb458, fb459.

## Atlet dizi rehberi (11 Ekim 2026, 5'in 3.sü)
- atlet-dizi.html → en/jumpers-knee.html (cond25_part.py). Egzersizler: pt_iso (yeni, "wall" çizimi; wallsit çizimi self2'de sonradan tanımlandığı için kullanılamadı), quad, kext, bridge, pf_wall, pt_sls (yeni).
- Okunan kaynaklar: Lian 2005 özeti (lida.sport-iat.de; yazar baş harfleri hafızadan), Breda 2021 özeti (pure.eur.nl) + Physiotutors program özeti, NHS Borders broşürü (1 Kasım 2024), NHS Knee pain (21 Aralık 2023).
- Kaynaksız / genel bilgi: "diz önü ağrısından farkı" SSS'si, "aylar sürebilir" ifadesi.
- Kartlarda: fb460, fb461.

## Omuz çıkığı rehberi (11 Ekim 2026, 5'in 4.sü)
- omuz-cikigi.html → en/shoulder-dislocation.html (cond26_part.py). Egzersizler: scap2, isoer, di_wall (yeni, wslide çizimi), scaption, row, sler.
- Okunan kaynaklar: NHS Dislocated shoulder (16 Eylül 2026), Olds 2015 BJSM özeti (canterbury deposu; sayfa aralığı 913–922 hafızadan), NLG broşürü (Aralık 2025), Worcestershire broşürü, Leicester broşürü (Aralık 2024).
- Kaynaksız / genel bilgi: koldaki uyuşma/karıncalanma kırmızı bayrağı, 112 (NHS 999 diyor; Türkiye'ye uyarlandı), "en sık öne doğru çıkar" ifadesi.
- Kartlarda: fb462, fb463.

## Piriformis sendromu rehberi (11 Ekim 2026, 5'in 5.si — 5 rehberlik tur tamam)
- piriformis-sendromu.html → en/piriformis-syndrome.html (cond27_part.py). Egzersizler: pi_str (yeni, k2c çizimi), slump, bridge, abd, sideplank, hext.
- Okunan kaynaklar: Hopayian 2010 (UEA deposu + tam rapor PDF: 55 çalışma, ≤%1 tahmini), Hopayian & Danielyan 2018 özeti, NHS Lothian broşürü (Ocak 2025; egzersizler görselde olduğu için okunamadı, yalnızca "30 saniye tut" ve tenis topu masajı), NHS Sciatica (3 Aralık 2024).
- Kaynaksız / genel bilgi: egzersiz seçimi (piriformis germe, köprü, yan köprü vb.), "sık kalkıp hareket etme" ve "daha yumuşak yüzeyde oturma" önerisi.
- Kartlarda: fb464.

## Kambur duruş (kifoz) rehberi (12 Ekim 2026)
- kambur-durus.html → en/kyphosis.html (cond28_part.py). Egzersizler: pchest, thor, wallpost, row, scap, cat (hepsi mevcut).
- Okunan kaynaklar: NHS Kyphosis (30 Aralık 2025), SHEAF (Katzman 2017; escholarship özeti), Oliveira-Costa 2025 gençlerde egzersiz derlemesi (SciELO tam metin), Christensen & Hartvigsen 2008 (PainScience özeti).
- Kaynaksız / genel bilgi: "duruşa bağlı kamburluk esnektir, dikleşince düzelir", "kemik erimesi olan birinde ani sırt ağrısı" uyarısı, pozisyon değiştirme önerisi.
- reg_cond.py AGR eşleşmesi satır sonu virgülüne göre düzeltildi. Kartlarda: fb465, fb466. masa-basi ilgili listesine de eklendi.

## Üç Kapı: beden, nefes, zihin (12 Ekim 2026)
- uc-kapi.html → en/three-doors.html (kapi_part.py, mind_part.py'den sonra exec). Kendine iyi bak, "Ruh sağlığı için" grubunun başında; kayıt: scratchpad/reg_kapi.py. Kartlarda fb467, fb468.
- İçerik: kanca giriş + canlandırmalı Venn; sesli seans (giriş ölçümü → beden 90 sn yerinde yürüyüş/oturarak → döngüsel iç çekiş 120 sn → zihin: beden haritası + duygu kelimeleri + "ustaların soruları" (Jung, Gendlin, Slavinski, Frankl) + 3 nefes yanında kalma → çıkış ölçümü, önce/sonra çubukları, geçmiş ve kapı sayaçları, localStorage drihsaneren.ucKapi.v1). Test için ?x=40 hızlandırır (ses kapalı).
- Kanıt pusulası: 1895–2024 zaman çizelgesi, 5 etiket (Güçlü kanıt / Umut verici / Tartışmalı / Yeterli kanıt yok / Tarihsel fikir), süzgeçli. "Ustalardan öğrendiklerimiz": Jung, Gendlin, Levine, Slavinski, Nelson, Jacobson, Shapiro, Frankl.
- İhsan'ın isteği: anlaşılır, empatik dil + "Harvard'dan bir hoca baksa sallamış demesin" düzeyinde doğruluk. Seansın bütün olarak sınanmadığı açıkça yazılı.
- Okunan kaynaklar: Balban 2023 (Stanford haberi + özet), Nummenmaa 2014 (Aalto haberi, özet), Lieberman 2007 (ScienceDaily), Reed & Ones 2006 (UMN özeti), Frattaroli 2006 (özet), EMDR Institute tarihçesi, Brom 2017 (özet), Grossman 2023 (yalnız başlık/kayıt), Giroux 2023 (tam metin), Worcestershire FND broşürü, Peterson & Jung 1907 (kayıt) + Jung'un metni (sidis.net), Carvalho 2016 (Medical News Today), Steffen 2017 (PubMed özeti), Elezović 2016 ve Pinal Villanueva 2024 (kayıtlar), Emotion Code anlatımı (All Within), Schwartz 2014 (SkepDoc özeti), Gendlin/Levine için GoodTherapy sayfaları.
- Hafızadan: bazı yazar listeleri ve sayfa numaraları (Nummenmaa, Lieberman, Carvalho, Steffen, Schwartz), Porges 1995 künyesi, Breuer-Freud 1895 / Jacobson 1929 / Reich 1933 kitap künyeleri, ustaların doğum-ölüm yılları, Levine'in kurucu olduğu, "deri iletkenliği bugün de kullanılıyor", "bu tablonun bir bölümü bugün FND" ifadesi.
- Kas gevşetme sayfasındaki "1930'larda" → "1920'lerde" düzeltildi (Jacobson'ın kitabı 1929).
- Ana sayfa galerisinden omurga maketli kare (p07) kaldırıldı (İhsan istedi); lastik bant karesi (p21) iki sütun kaplıyor, boşluk yok. i18n/js.json'dan ilgili altyazı silindi.
- Sırada: İhsan'ın kendi klinik gözlemleri için "Klinikten notlar" kutusu (o yazarsa); Üç Kapı için kısa tanıtım videosu.

## Ana sayfa sekmeleri (12 Ekim 2026)
- Bir arkadaşın yorumu: "sekmeler olsun, çok aşağı iniyoruz, o düğmeler dikkat çekmiyor, bir test daha üstte olsun".
- fb_tabs.py (publish.sh'te splice_home.py'den sonra çalışır): hero'daki 5 küçük düğme kalktı; hero'nun hemen altında "Keşfedin · Neyi merak ediyorsunuz?" başlıklı 6 büyük sekme var: Hizmetler · Hızlı test (2 dk rozeti) · Longevity analizi · Kişiye özel egzersiz · Uygulama kareleri · Logonun anlamı. Yalnızca seçili bölüm görünür; hızlı test kendi bölümüne (#test) taşındı.
- Aşağı inince başlığın altına ince bir sekme çubuğu yapışır. Üst menü bağlantıları ve #analiz gibi adresler ilgili sekmeyi açar. JavaScript yoksa bütün bölümler alt alta görünür.
- Bilgi köşesindeki konu listeleri mobilde "Tüm konuları göster (109 başlık)" ile katlanır; masaüstünde açık.
- Mobil sayfa boyu 15.377 px → 7.079 px; masaüstü 10.105 → 6.073. Yeni çeviriler fb469–fb474.
- (12 Ekim, devam) İhsan: geniş kare (p21, lastik bant) yarım görünüyordu → galeriden kaldırıldı; galeri 1 büyük + 4 kare, masaüstünde 4 sütun (mobil 2), ızgara tam dolu. Konu listesi artık masaüstünde de katlı başlıyor ("Tüm konuları göster").
- Üç Kapı tanıtım videosu: scratchpad/vid4 (film.py sahneler, music.py özgün müzik, 54 sn, 1080x1920). Tek video yeterli dedi; 4:5 sürüm yapılmadı.

## Baker kisti rehberi (14 Ekim 2026)
- baker-kisti.html → en/bakers-cyst.html (cond29_part.py). Egzersizler: bk_hslide (yeni, hslide çizimi), quad, kext, slr, dn_heel, sts.
- Okunan kaynaklar: NHS 111 Wales Baker's cyst (6 Kasım 2025), Royal Berkshire NHS broşürü (Şubat 2025; patlama 20'de 1–2), ORS 2025 kongre özeti (diz MR kistleri; yüzde verilmiyor).
- Kaynaksız / genel bilgi: egzersiz seçimi ve "gerginliği artıran hareketleri azaltın" önerisi; 112 (NHS 999 diyor).
- Kartlarda: fb475, fb476.

## Kürek kemiği arası ağrı rehberi (14 Ekim 2026)
- kurek-kemigi-arasi-agri.html → en/pain-between-shoulder-blades.html (cond30_part.py). Egzersizler: cat, ub_trot (yeni çizim: oturarak gövde döndürme), thor, ub_sbend (yeni çizim: duvarda yana eğilme), scap, row.
- Okunan kaynaklar: Berkshire Healthcare NHS mid-back pain (Şubat 2026; belirtiler, egzersizler 10–20 tekrar günde 2–3, uyarı işaretleri), Briggs ve ark. 2009 BMC MSD sistematik derleme (yaşam boyu %15,6–19,5 — sayfada nüfus belirtilmeden "araştırmalarda bildirilen" diye yazıldı; gençlerde ve kızlarda daha sık; ilişkili etkenler), Carmichael ve ark. 2025 NASSJ kapsam derlemesi (boyun kökü sıkışmasında kürek kemiği ağrısı; kol ağrısından haftalar önce başlayabilir), NHS kalp krizi belirtileri (31 Mart 2026; sırttan söz etmiyor, kol/boyun/çene diyor), HSE aort diseksiyonu belirtileri.
- Kaynaksız / klinik bilgi: "hareketle ve pozisyonla değişen ağrı daha çok kas-eklem kaynaklı" cümlesi (tek başına kalbi dışlamaz diye yumuşatıldı); "duvarda yana eğilme" tarifinin ayrıntısı (Berkshire yalnızca adını veriyor); "stres sırt kaslarını gerebilir"; çocuk sorusundaki uyku ve hareket alışkanlıkları; 112 (NHS 999 diyor).
- Kartlarda: fb477, fb478.
- Ders: çevrilmiş bir sayfada TR metni değişince i18n/todo ve done/<sayfa>.json silinip tam export/import yapılmalı (tek satırlık import done'ı ezer).

## Gece bacak krampları rehberi (14 Ekim 2026)
- gece-bacak-kramplari.html → en/night-leg-cramps.html (cond31_part.py). Egzersizler: lc_relief (towelst2 çizimi), lc_calf, lc_soleus, lc_ham (yeni çizim: sandalyede arka uyluk germe), lc_towel, lc_walk. Bölge "genel", huzursuz bacaktan sonra. reg_cond.py artık satır sonundaki ")]" ile biten AGR öğesini de buluyor.
- Okunan kaynaklar: HSE Leg cramps (1 Temmuz 2024; süre, nedenler, statin/diüretik, germe 5 dk günde 3 kez, hekim ölçütleri), Allen & Kirby 2012 AFP (%50–60, ortalama 9 dk, huzursuz bacak/klodikasyon/nöropati ayrımı, kinin FDA uyarısı), Hallegraeff 2012 J Physiother RKÇ (80 kişi >55 yaş, 6 hafta, gecede 1,2 kramp ve 1,3 cm VAS fark), Garrison 2020 Cochrane (magnezyum: yaşlılarda anlamlı fayda yok; gebelikte belirsiz), NHS DVT (30 Nisan 2026).
- Kaynaksız / genel bilgi: "topuğa basarak birkaç adım atmak" önerisi; soleus, arka uyluk ve havlu germede 20–30 saniye süreleri (Hallegraeff kaydında süre yok); "ilacı kendiniz bırakmayın" uyarısı; "tek bacakta pıhtı belirtisinde aynı gün" (NHS "acil GP / 111" diyor); 112 (NHS 999 diyor).
- Kartlarda: fb479.

## Ganglion kisti rehberi (14 Ekim 2026)
- ganglion-kisti.html → en/ganglion-cyst.html (cond32_part.py). Egzersizler: gg_wrist (dq_wrist çizimi), gg_rot (ge_rot çizimi), tglide, wflex, wext_st, grip. Bölge "omuz" (kol ve el), tetik parmaktan sonra.
- Okunan kaynaklar: NHS Ganglion cyst (16 Temmuz 2025), AoMRC Evidence-Based Interventions: Ganglion excision (Eylül 2024; boşaltma %30 kalıcı, ameliyat sonrası 4–6 hafta kısıtlılık), BSSH hasta broşürü 2016 (ameliyat sonrası tekrarlama: bilek sırtı ~%10, iç yüzü ~%30, parmak ucu ~%10).
- Kaynaksız: egzersizlerin kendisi (sayfada "kisti küçülttüğüne dair kanıt yok" diye açıkça yazıldı); "kitapla vurma" sorusu halk pratiğinden; uyuşma/güçsüzlükte hekime başvurma maddesi (AoMRC'deki "uyuşma varsa tedavi" ölçütünden türetildi); "aynı gün" (NHS 111 diyor).
- Kartlarda: fb480.

## Boyun tutulması rehberi (14 Ekim 2026)
- boyun-tutulmasi.html → en/wry-neck.html (cond33_part.py). Egzersizler: bt_rot (rot çizimi), bt_side (side), bt_nod (yeni çizim: başı öne-arkaya eğme), bt_shrug (ly_shrug), chin, scap. Bölge "boyun", boyun ağrısından sonra.
- Okunan kaynaklar: Royal Berkshire NHS acil servis broşürü Acute torticollis (Haziran 2024; belirtiler, nedenler, hekime başvuru ölçütleri), Dorset County Hospital NHS broşürü (Nisan 2014, eski; spazm 24–48 saat, tam iyileşme bir hafta, birkaç saatte bir her yöne hareket, tek sağlam yastık, "hareket boyna zarar vermez"), nidirect Meningitis (23 Temmuz 2026).
- Kaynaksız / genel bilgi: egzersiz tekrar sayıları (5–10); "boyunluk genellikle gerekmez" (kaynaklar boyunluktan söz etmiyor, hareket öneriyor); sıcak torbayı havluya sarma uyarısı; "kola yayılan ağrı ya da uyuşma olursa egzersizi bırakın"; 112 (kaynak 999 diyor).
- Kartlarda: fb481, fb482.

## Kaval kemiği ağrısı rehberi (14 Ekim 2026)
- kaval-kemigi-agrisi.html → en/shin-splints.html (cond34_part.py). Egzersizler: ss_calf, ss_soleus, ss_toe (dm_toe çizimi), ss_heel, ss_arch (ff_short), ss_sls. Bölge "ayak", aşilden sonra.
- Okunan kaynaklar: NHS Shin splints (9 Şubat 2023; buz 20 dk 2–3 saatte bir, birkaç haftada düzelir), nidirect Shin splints (10 Ocak 2025; 2–3 hafta ara, 5 cm kuralı, stres kırığı/kompartman ayrımı, risk etkenleri), Newman ve ark. 2013 OAJSM meta-analiz (%5–35; kadın, yüksek VKİ, navikular düşme, önceki MTSS, tabanlık kullanımı, az koşu deneyimi).
- Kaynaksız / yorum: tüm egzersiz doz ve süreleri; tek ayakla topuk yükseltmeye geçiş ve göz kapalı denge; tabanlık sorusundaki "risk taşıyanlar kullanıyor olabilir" yorumu (makale nedensellik kurmuyor); "aynı gün" (NHS 111 diyor).
- Kartlarda: fb483, fb484.

## Arka uyluk zorlanması rehberi (14 Ekim 2026)
- arka-uyluk-zorlanmasi.html → en/hamstring-injury.html (cond35_part.py). Egzersizler kolaydan zora: hs_slide (hslide), hs_bridge, hs_stretch (lc_ham), hs_walk, hs_hinge, hs_nordic (yeni çizim: Nordic hamstring). Bölge "diz", atlet dizinden sonra.
- Okunan kaynaklar: nidirect Hamstring injury (19 Aralık 2024; 3 derece, PRICE 48–72 saat, buz 15–20 dk 2–3 saatte bir, ilk 72 saatte HARM'dan kaçınma, ibuprofen 48 saat sonra, birkaç gün sonra hafif germe, spora dönüş ölçütü), van Dyk ve ark. 2019 BJSM meta-analiz (8459 sporcu, Nordic içeren programlar RR 0,49).
- Kaynaksız: tüm egzersiz doz ve süreleri; Nordic için "haftada 1–2 kez, 2–3 set × 3–6 tekrar" (bellekten, yaygın protokoller); "ağrı ertesi gün artarsa bir önceki seviyeye dönün" kuralı; "pat sesi / bacağı kullanamama / geniş morarma" maddesi nidirect'in 3. derece tanımından türetildi (sayfa bunu ayrıca acil saymıyor).
- Kartlarda: fb485, fb486.

## Sakroiliak eklem ağrısı rehberi (14 Ekim 2026)
- sakroiliak-eklem-agrisi.html → en/sacroiliac-joint-pain.html (cond36_part.py). Egzersizler: ptilt, bridge, birddog, si_abd (abd çizimi), k2c, si_walk. Bölge "bel", piriformisten sonra.
- Okunan kaynaklar: Barros, McGrath, Gelfenbeyn 2019 Federal Practitioner (%15–30, ağrı alanı 3×10 cm PSIS altı, L5 üstüne çıkmaz, risk etkenleri, test kümeleri, tanısal iğne, RF ~2/3'te 6–12 ay, füzyon ölçütleri), HCA Healthcare UK hasta sayfası (otur-kalk ağrısı, bacak boşalması, pelvik stabilizasyon, buz/ağrı kesici; tarih/yazar yok, özel hastane), NICE NG59 (hareketli kalma; sitede zaten kaynak).
- Kaynak zayıflığı: NHS'te SİE için ayrı sayfa bulamadım; healthdirect sayfası okunamadı. Uyarı işaretleri bel ağrısı ve ankilozan spondilit sayfalarındaki listelerden alındı (bu sayfaya özel kaynak yok). Egzersiz seçimi ve dozları kaynaksız (HCA yalnızca "pelvik stabilizasyon" diyor).
- Kartlarda: fb487.

## Osgood-Schlatter rehberi (14 Ekim 2026)
- osgood-schlatter.html → en/osgood-schlatter.html (cond37_part.py). Egzersizler: os_qstr (yeni çizim: ayakta ön uyluk germe), os_ham (lc_ham), os_wall, os_slr, os_abd, os_bridge. Bölge "diz", diz önü ağrısından sonra.
- Okunan kaynaklar: NHS Fife çocuk ortopedi sayfası (Ocak 2022; 10–14 yaş, 12–24 ay, aktivite azaltma), Bradford Teaching Hospitals NHS broşürü (Şubat 2025; 10–16 yaş, erkeklerde daha sık, buz 10 dk, 20–30 sn germeler, 6 haftada düzelmezse hekim), Rathleff ve ark. 2020 OJSM (51 genç, 12 hafta aktivite merdiveni + güçlendirme, %80 başarı, 12 ayda %69 spora dönüş; kontrol grubu yok).
- Kaynaksız: güçlendirme egzersizlerinin seçimi ve dozları (Rathleff özetinde egzersiz ayrıntısı yok), duvar çömelmesinin "sabit tutma" biçimi; gece ağrısı, ateş/sıcak kızarık diz, topallama/kilitlenme uyarıları (genel çocuk diz ağrısı bilgisi, iki broşür de bunları listelemiyor).
- Kartlarda: fb488, fb489.

## Morton nöroması rehberi (14 Ekim 2026)
- morton-noromasi.html → en/mortons-neuroma.html (cond38_part.py). Bilinçli olarak 4 egzersiz ("ex four"): mn_calf, mn_soleus, mn_arch (ff_short), mn_toe (dm_toe). t_ls 6 egzersiz beklediği için "sorun: 6" verir; bu sayfada beklenen durum (taşma/hata/kırık bağlantı yok).
- Okunan kaynaklar: NHS Morton's neuroma (12 Haziran 2025; belirtiler, nedenler, ayakkabı/ped/kilo önerileri, 2 hafta kuralı, hekime başvuru ölçütleri), Matthews ve ark. 2019 J Foot Ankle Res (25 çalışma; kortizon iğnesi ve mobilizasyon en güçlü kanıt, altın standart yok, ESWT anlamsız).
- Kaynaksız: egzersizlerin seçimi ve dozları (sayfada "nöromayı geçirdiğine dair kanıt yok" yazıyor); "dar ayakkabılar ayak önündeki baskıyı artırdığı için" gerekçesi.
- Kartlarda: fb490.

## El bileği kırığı sonrası rehberi (14 Ekim 2026)
- el-bilegi-kirigi.html → en/wrist-fracture.html (cond39_part.py). Egzersizler (ULH broşüründeki hareketler, hazır çizimler): wb_wrist (dq_wrist), wb_ext (wflex), wb_rot (ge_rot), wb_fist (tglide), wb_thumb (thumb), wb_grip (grip). Bölge "omuz" (kol-el), ganglion kistinden sonra.
- Okunan kaynaklar: NHS Broken arm or wrist (2 Ekim 2026; 6–12 hafta, alçı uyarı işaretleri, 50 yaş üstü kemik sağlığı), United Lincolnshire NHS broşürü (Ocak 2026; ilk 1–2 ay, günde 3–4 kez ~10 tekrar, atel en kısa süre), Handoll & Elliott 2015 Cochrane (26 çalışma; ev programı ≈ ek fizyoterapi, kanıt düşük), East Kent NHS CRPS broşürü (belirtiler), Royal Osteoporosis Society (egzersizin CRPS riskini azaltmaya yardım edebileceği).
- Kaynaksız: "wb_ext" broşürdeki "avuç masada, dirseği kaldırma" yerine ön kol germe çizimiyle anlatıldı (aynı hareket yönü); 15–20 saniye seçeneği; Türkiye'de "kırık irtibat hizmeti" olmadığı için "kemik sağlığınızı hekiminizle konuşun" diye uyarlandı.
- Kartlarda: fb491.

## Eklem hipermobilitesi rehberi (14 Ekim 2026)
- eklem-hipermobilitesi.html → en/joint-hypermobility.html (cond40_part.py). Egzersizler: jh_sls, jh_bridge, jh_birddog, jh_wall, jh_scap, jh_walk (hepsi "eklemi kilitlemeden, orta açıklıkta" vurgusuyla). Bölge "genel", gece bacak kramplarından sonra.
- Okunan kaynaklar: NHS Joint hypermobility syndrome (30 Ağustos 2023; belirtiler, nedenler, Beighton, düşük darbeli egzersiz, aşırı germe ve tekrardan kaçınma, molalar, ılık banyo), Engelbert ve ark. (fizyoterapi gerekçesi; ayaktan fizyoterapi hastalarında %30–55, Beighton ≥4/≥5, kanıt sınırlı).
- Bellekten / kaynaksız: Beighton'un 9 puanlık maddeleri (standart bilgi, bu oturumda okunan sayfada sayılmıyor); Engelbert makalesinin dergi ve yılı (Am J Med Genet C 2017; okunan PDF'te yayın bilgisi yoktu); "ayağa kalkınca baş dönmesi, çarpıntı" uyarısı (hEDS–POTS ilişkisi, NHS sayfasında yok); egzersiz dozları.
- Kartlarda: fb492, fb493.

## El ve parmak kireçlenmesi rehberi (14 Ekim 2026)
- el-kireclenmesi.html → en/hand-osteoarthritis.html (cond41_part.py). Egzersizler: ho_fist (tglide), ho_opp (thumb), ho_web (thumb), ho_grip (grip), ho_wrist (dq_wrist), ho_rot (ge_rot). Bölge "omuz" (kol-el), el bileği kırığından sonra.
- Okunan kaynaklar: NHS Dumfries & Galloway Right Decisions (12 Aralık 2025; 50 yaş üstü, ≥45 yaş + ≤30 dk sabah tutukluğu ile klinik tanı, ısı/soğuk, mola, yumruk ve başparmakla parmaklara dokunma, sıcak-kabarık şişlikte romatoloji), St George's NHS başparmak OA broşürü (Mayıs 2025; 5 dk ısıtma, 30 sn başparmak arası esnetme, top sıkma), Østerås 2017 Cochrane (ağrıda 0,5 puan, kanıt düşük, yan etki az).
- Kaynaksız: egzersiz tekrar sayıları; "örgü, bilgisayar, bahçe işi" örnekleri; "sabah tutukluğu 30 dakikadan uzunsa hekime" maddesi (tanı ölçütünden türetildi). Versus Arthritis broşürü bağlantısı 404 verdi.
- Kartlarda: fb494.

## Bilgi köşesi tanıtım videosu (14 Ekim 2026)
- scratchpad/vid5: film.py (8 sahne, 50 sn, 1080x1920), music.py (özgün sentez müzik), shot.py (gece-bacak-kramplari mobil tam sayfa görüntüsü + başlık konumları), ex.json (sitedeki 4 egzersiz çizimi). Çıktı: out/bilgi-kosesi-video.mp4 (9,2 MB, ortalama -16,1 dB).
- Sahneler: "Nereniz ağrıyor?" beden haritası → 6 gerçek soru baloncuğu → 61 hastalık rehberi sayacı + bölge sayıları → telefonda gece bacak krampları rehberinin içi → 4 egzersiz çizimi → "Abartı yok" (sitedeki 3 gerçek cümle) + uyarı işaretleri → TR/EN kart çevirme → kapanış (drihsaneren.com/bilgi).
- Sayılar sitedeki filtrelerden: Tümü 61, bel 12, boyun 7, omuz-kol-el 12, kalça-diz 11, ayak 8, tüm vücut 10, kadın 2; toplam 122 başlık.

## Kendine iyi bak: 10 saniye denge testi (14 Ekim 2026)
- denge-testi.html → en/balance-test.html (self4_part.py; SELF4_CSS = SELF2_CSS + denge stilleri). Kayıt aracı: scratchpad/reg_self.py (config: s_bal.py). "Kendinizi ölçün" grubunda otur-kalk testinden sonra; C_BAL (C_BT boyun tutulmasında kullanılıyor).
- Araç: göz açık/kapalı, yaş grubu, 5 sn hazırlık + bip, 45 sn üst sınır, 10 sn işareti, ekrana dokunma / boşluk tuşu ile durdurma, 3 deneme + en iyisi, Springer normlarıyla karşılaştırma; mobilde sıra: seçimler → süreölçer → sonuç. Hiçbir şey kaydedilmez.
- Okunan kaynaklar: Araujo ve ark. 2022 BJSM (1702 kişi, 51–75 yaş, %20,4 yapamadı, 7 yıl, %17,5 / %4,6, HR 1,84), Springer ve ark. 2007 JGPT (549 kişi, yaş gruplarına göre en iyi 3 deneme, uygulama ve durdurma ölçütleri), Sherrington 2019 Cochrane (%24, düşme önleme sayfasıyla aynı).
- Kaynaksız / yorum: "ortalamanın %85'i ve üzeri = ortalamaya yakın" eşiği; göz kapalıyken dengenin neden zorlaştığı açıklaması (genel fizyoloji); güvenlik önerileri. Araujo makalesinin bitiş sayfası yazılmadı (okunan özette yoktu). t_ls 4 egzersiz nedeniyle "sorun: 6" verir (beklenen).
- Kartlarda: fb495, fb496.

## Kendine iyi bak: Hareket atıştırmalıkları (14 Ekim 2026)
- hareket-atistirmaliklari.html → en/exercise-snacks.html (self4_part.py, 2. sayfa). "Zamanlayıcıyla birlikte yapın" grubunun sonunda; C_SNACK. Yeni çizim: sn_stair (merdiven). Atıştırmalıklar: sn_stair, sn_walk, sn_sts, sn_push (sk_push), sn_march (dm_march), sn_heel (heel2).
- Araç: 6 kartlı seçici (svg'ler .an sınıfıyla), "Benim için seç", 3 sn hazırlık + 60 sn halka, günlük 0/3 sayacı (localStorage drihsaneren.atistirmalik.v1, try/catch), 30 dakikada bir mola hatırlatıcı (sayfa açıkken, bip + titreşim).
- Okunan kaynaklar: Stamatakis ve ark. 2022 Nature Medicine (UK Biobank sayfası; 25.241 egzersiz yapmayan, 6,9 yıl, günde ortanca 3 nöbet → %38–40 / KVH %48–49; 4,4 dk/gün → %26–30; gözlemsel), Jenkins ve ark. 2019 APNM (merdiven atıştırmalıkları, 60 basamak, günde 3, haftada 3, 6 hafta; VO2peak arttı, küçük), Duran ve ark. 2023 MSSE (11 kişi; 30 dk'da 5 dk yürüyüş glukozu düşürdü; tüm molalar sistolik tansiyonu düşürdü).
- Kaynaksız / yorum: "merdiveni koşar adım çıkmak, otobüse yetişmek" örnekleri (çalışmanın basın açıklamalarındaki örnekler; okunan özette yok); "konuşmakta zorlanma" tempo tarifi; atıştırmalık seçimi ve süreleri; Stamatakis makalesinin cilt/sayfası yazılmadı.
- Kartlarda: fb497.

## Kendine iyi bak: Ağrıyı anlamak + Egzersizde ağrı trafik ışığı (14 Ekim 2026)
- Yeni grup "Ağrıyla yaşamak" (SELF_GROUPS, "Günlük hayat için"in önünde; fb501). Sayfalar self4_part.py'de 3. ve 4. sayfa; C_PAINU, C_PAINX.
- agriyi-anlamak.html → en/understanding-pain.html: IASP 2020 tanımı ve 6 not (IASP duyurusu, 16 Temmuz 2020; resmî İngilizce ifadeler EN'de birebir), "alarm sistemi" etkileşimi (5 hassaslaştıran + 5 yatıştıran etken; katsayılar 1 + 0,22·h − 0,11·y, 0,45–2,2 arası — tamamen temsilî, sayfada "öğretici benzetme, ağrınızı ölçmez" yazıyor), Brinjikji 2015 AJNR (33 çalışma, 3.110 ağrısız kişi; 20/80 yaş: dejenerasyon %37/%96, taşma %30/%84, protrüzyon %29/%43, anüler fissür %19/%29), Watson 2019 J Pain (12 RKÇ, 755 kişi; ağrı ve özürlülükte küçük etki, hareket korkusunda kısa vadede anlamlı azalma; hikâyesini anlatabilmek).
- egzersizde-agri.html → en/pain-during-exercise.html: 3 soru (ağrı 0–10, ertesi sabah, haftalık gidiş) → yeşil/sarı/kırmızı. Silbernagel 2007 AJSM (38 kişi; egzersiz sırasında ağrı 5'e ulaşmamalı, sonrasında 5'e çıkabilen ağrı ertesi sabah geçmeli, haftadan haftaya artmamalı; kurallar fizyoterapi blogundan, makalenin tam metninden değil), Smith 2017 BJSM (7 çalışma, 385 kişi; ağrıya izin veren egzersiz kısa vadede SMD −0,27; orta-uzun vadede fark yok).
- Kaynaksız / yorum: yeşil 0–2 / sarı 3–4 bölge sınırları (klinikte yaygın uyarlama; kaynaktaki tek eşik 5), "yükü azaltın ama bırakmayın" önerisinin ayrıntıları, alarm etkenlerinin listesi (IASP'nin biyopsikososyal notuna dayanıyor, tek tek kaynaklanmadı), "tüm ağrılar beyinde oluşur" cümlesi, hemen durun listesi.
- t_ls iki sayfada da egzersiz=0 nedeniyle "sorun: 6" verir (beklenen). Kartlarda: fb498–fb501.

## Bilim gündemi: 3 yeni haber (14 Ekim 2026)
- build_pages.py NEWS listesine Nobel'den hemen sonra (ana sayfadaki ilk 4 başlığa girer): Parkinson'da fiziksel aktivite (Neurology, 7 Ekim 2026; 294 kişi, 7 yıl, >8 sa/hafta vs <4; gözlemsel, anket), kireçlenme 2050 (The Lancet yol haritası, Curtin Üniv.; 2023'te ~600 milyon, 2050'de ~1 milyar, engellilik yükü 1990–2023 %65 arttı, Avustralya 2009–10 %43), lakozamid ve kıkırdak (Yale, Bioactive Materials 2026;61:640; yalnızca hücre/hayvan). Yeni çizimler: IL_PDACT, IL_OA2050, IL_LACO.
- Çeviri: haber metinleri ayrı parti dosyasında: i18n/todo/yen5.json + i18n/done/yen5.json (y5-0…12; kaynak satırları ham HTML, bağlantılar birebir). DİKKAT: export_todo yenilikler.html'i çalıştırınca todo/yenilikler.json yeniden yazılır ve eski done eşleşmesi bozulur; bu sefer eski dosyalar geri yüklendi. Yeni haberlerde aynı yolu izleyin (yeni yenN partisi).
- Okunan kaynaklar: EurekAlert AAN basın bülteni (7 Ekim 2026), Knowridge (14 Ekim 2026), ScienceDaily/Yale (8 Ekim 2026). Okunamayan: Washington Post, Medscape, Medical Xpress (bağlantı olarak verildi, içerik Knowridge'den), Lancet sayfası (robots).
- Kaynaksız / yorum: "kanıtı en güçlü yaklaşımlar egzersiz, kilo kontrolü ve hastalığı tanımak" cümlesi (genel kılavuz bilgisi, bu haberin kaynağında yok); OA çizimindeki 1990 sütunu temsilî.

## Logo paneli 4 genişletildi (15 Ekim 2026)
- "İki Y ve renk geçişi" paneli tek cümleden 4 paragrafa çıktı (Yin–Yang → Doğu/Batı tıbbı → bütüncül tedavi yaklaşımı → pusula bilim). Düzenleme site/index.bak_fb.html'de (rebuild_home.sh index.html'i oradan kopyalıyor; doğrudan site/index.html'e yazılanlar kaybolur).
- EN çevirisi ayrı parti: i18n/todo/logo4.json + done/logo4.json (lg-0..3). export_todo index.html'de yalnız yeni dizeleri ind0.. kimlikleriyle yazıp eski todo'yu ezdi; eski todo/done geri yüklendi, yeni dizeler ayrı partiye kondu (yen5 ile aynı yöntem).
- Panel metninde sağlık iddiası yok; "kanıtın desteklediği ölçüde" ilkesi dile getiriliyor.

## 30 saniye sandalye testi, kameralı sayaç (15 Ekim 2026)
- Sayfa: sandalye-testi.html → en/chair-stand-test.html (self5_part.py, C_CST, "Kendinizi ölçün" grubunda denge testinden sonra). reg_self.py EXEC'i kapi_part.py'den sonra ekliyor; self5 SELF4_CSS'e ihtiyaç duyduğu için exec sırası elle "self4_part.py", "self5_part.py" yapıldı.
- Kamera: MediaPipe Tasks Vision 0.10.35 (npm, Apache-2.0) main'de assets/mp/ altında (vision_bundle.js = .mjs'nin adı değişmiş hali, wasm 11 MB). Model (pose_landmarker_lite.task, ~5,8 MB) çalışma anında storage.googleapis.com'dan iniyor; görüntü cihazda işleniyor. Önce GPU, ilk 3 karede ortalama >150 ms ise otomatik CPU'ya geçiş.
- Sayma: her bacak için (diz.y − kalça.y) / baldır uzunluğu; görünürlüğe göre ağırlıklı ortalama, EMA; histerezis 0,78 (kalktı) / 0,42 (oturdu), 300 ms kilit. Yandan ve önden çalışır. Süre biterken yarıdan fazla doğrulmuşsa +1 (STEADI kuralı).
- Test: sahte kamera (Chromium --use-file-for-fake-video-capture) ile çizilmiş manken videosu; 30 sn penceredeki 10 kalkışın 10'u sayıldı (TR ve EN). Gerçek bir insanla, gerçek telefonda test EDİLMEDİ; kullanıcıya söylendi. Sandbox'ta model storage.googleapis.com'dan inemiyor, testte route ile yerel kopya verildi (npm pose-landmarker-react-native paketinden; yalnızca test için).
- Kaynaklar (okunan): CDC STEADI 30-Second Chair Stand (protokol, yarı kuralı, yaş/cinsiyet eşikleri; NJ kopyasından okundu), Shirley Ryan AbilityLab sayfası (Rikli & Jones 1999 %25–75 aralıkları, McKay 2017 20–59 ort.±SS, Wright 2011 MCID 2,0–2,6). Rikli-Jones aralıklarının alt sınırları STEADI eşikleriyle birebir aynı. McKay ve Rikli & Jones makalelerinin kendisi açılmadı; değerler SRA derlemesinden.
- Kamerasız mod: dokunarak sayım ya da sonucu elle girme; sonuç localStorage drihsaneren.sandalye.v1 (son 10). WhatsApp düğmesi sonucu hazır mesajla gönderiyor.
- Tanıtım videosu (15 Ekim 2026): scratchpad/vid6 (film.py 7 sahne 44 sn 1080x1920, music.py özgün sentez + sitedeki bip sesleri, timing.json sayım zamanları). Kamera sahnesindeki kişi ve iskelet çizim (gerçek görüntü değil). Çıktı: out/sandalye-testi-video.mp4 (7,2 MB, ortalama -18 dB). Örnek sonuç "kadın, 72 yaş, 13 tekrar" Rikli & Jones 70–74 kadın aralığıyla (10–15) tutarlı.
- Düzeltme (15 Ekim 2026, kullanıcı testi): (1) "9'da bitiyor": büyük ihtimalle iPhone'un 30 sn otomatik kilidi; ekran kilitlenince sayaç durup geri dönünce süre doldu sayılıyordu. Artık kamera açıkken ekran uyanık tutuluyor (Wake Lock; yoksa ya da reddedilirse assets/mp/awake.mp4 sessiz döngü video yedeği), ekran kapanır ya da sekme değişirse test iptal edilip "Test yarıda kaldı" yazıyor, sonuç kaydedilmiyor. WAKE_JS'e (self2_part.py) 'release' dinleyicisi eklendi; kilit bırakılınca yeniden alınabiliyor (tüm zamanlayıcılı sayfalar). (2) "×2 sayıyor": eski sayaç EMA + 300 ms kilitti; takılmalarda iki kez sayıyordu. Yeni mkCounter: 5 örneklik medyan + yumuşatma, eşik 0,75/0,40, eşiğin ötesinde 120/150 ms bekleme, 200 ms'den kısa "oturma" ve son sayımdan 500 ms içindeki kalkış sayılmıyor. Ölçüm: diz–kalça ve bilek–kalça oranlarının ortalaması, en görünür taraf. 13 sentetik senaryoda (gürültü, sıçrama, takılma, 0,7–3,2 sn tempo, yarım kalkış) doğru; eski sayaç 3'ünde iki kat saydı. Manken videosunda 10/10. Gerçek telefonda yeniden denenmesi gerekiyor.

## 4 yeni rehber (16 Ekim 2026): cond42–45
- boyun-incinmesi.html → en/whiplash.html (WH, boyun). Okunan: NHS Whiplash (19 Ağu 2026: 2–3 ay, belirtiler saatler sonra, boyunluk yardım etmez, aciller), Berkshire Healthcare NHS broşürü (Şubat 2026: 5 egzersiz 10–20 tekrar günde 2–3, araç kullanma ölçütü, ısı uyarısı, acil işaretler), NHS Fife broşürü (2016, eski: 1–2 saatte bir 10 tekrar, 5–10 sn tutma, buz/ısı 10 dk, boyunluk iyileşmeyi geciktirir, 6 hafta, uyku), Lamb 2013 Lancet MINT (PEDro özeti: 599 kişi, 4. ayda küçük yarar, 8–12. ayda fark yok).
- omuzda-kirec-birikmesi.html → en/calcific-tendinopathy.html (CF, omuz). Okunan: NHS Lothian (2020: 30–60 yaş, çoğu kendiliğinden kaybolur, birkaç haftada yatışır, 9 ay+), DBTH (2017: 1–6 haftada kendiliğinden düzelme, askı kısa, yastıkla uyku, evreli egzersizler ve dozlar), Whittington (2025: kadınlarda biraz daha sık, tedavi seçenekleri), Lafrance 2019 BMJ OSEM (lavaj; düşük kalite; asemptomatik %7,8), NHS Shoulder pain (aciller). Sarkaç ve sopa çizimleri donuk omuz EX listesinden alındı (cf_pendf, cf_stickf).
- karin-kasi-ayrilmasi.html → en/diastasis-recti.html (DR, kadin). Okunan: Sperstad 2016 BJSM özeti (300 ilk doğum: %33,1 / %60 / %45,4 / %32,6; bel-leğen ağrısı farksız), Gluppe 2021 (PEDro: 7 RKÇ, 381 anne, çok düşük kalite), OUH (Haziran 2022: 6–8 hafta, egzersizler, kaçınılacaklar, başvuru), Royal Devon (Ekim 2020: parmak testi, 2 parmak, karın düzleştirme dozu).
- sever-hastaligi.html → en/severs-disease.html (SV, ayak). Okunan: CUH (Eylül 2024), NHS Lothian öz yönetim (Mayıs 2022: kız 8–10, erkek 10–14, 6 hafta, esneme dozları), AFP 2017 Uvelli (James 2016 n=124, Wiegerinck 2016 n=101), NHS Heel pain (24 Eki 2025, aciller). Uyarı işaretleri NHS topuk ağrısı sayfasından çocuğa uyarlandı. 3 egzersiz (kaynaklarda bu kadar).
- check.py karin-kasi-ayrilmasi'nde kar54 için "Türkçe karakter" uyarısı verir: kaynakçadaki İsveççe ad (Ellström); doğru, düzeltilmedi.

## Kendine iyi bak, 6. tur (16 Ekim 2026): self6_part.py
- yurume-hizi-testi.html → en/gait-speed-test.html (C_YH, "Kendinizi ölçün", sandalye testinden sonra). 3/4/5 m seçimi, iki deneme (hızlı olanı), m/sn ve km/sa, Bohannon & Andrews 2011 ortalamaları (utoronto PDF'inden okundu), 65+ için Studenski 2011 eşikleri (ACP özeti: 34.485 kişi, 9 kohort, HR 0,88/0,1 m/sn, 0,8 ≈ ortanca yaşam beklentisi, ≥1,0 beklenenden uzun). Protokol Harvard eFrailty SPPB sayfasından. Studenski cilt/sayfa mitofit kaydından (305:50–58). localStorage drihsaneren.yuruyus.v1.
- agri-gunlugu.html → en/pain-diary.html (C_AG, "Ağrıyla yaşamak"). Günlük kayıt (0–10, yer, uyku, hareket, not), son 30 gün SVG grafik, 7 günlük ortalama ve önceki haftaya fark, uyku/hareket gözlemleri (≥5 kayıt ve her grupta ≥3 gün), WhatsApp özeti, CSV indirme, silme. localStorage drihsaneren.agri.v1. Farrar 2001 (chiro.org özeti: 2.724 kişi, ~2 puan / ~%30).
- reg_self.py EXEC'i kapi_part.py'den sonra ekliyor; sıra elle "self4", "self5", "self6" yapıldı.

## Bilim gündemi, 3 haber daha (16 Ekim 2026)
- Egzersiz ve ağrı (IL_EXPAIN): Adelaide Üniversitesi şemsiye derlemesi, PAIN Reports Ağustos 2026 (DOI 10.1097/PR9.0000000000001455); SciTechDaily 6 Ekim 2026'dan okundu (157 derleme, 2.736 RKÇ, 221.279 kişi, ortalama 1,1 puan, ~%60 ilaçlardan büyük ama dolaylı karşılaştırma).
- 47 yıllık İsveç SPAF (IL_SPAF): ScienceDaily 14 Ekim 2026 (Karolinska; 427 kişi, 16–63 yaş, zirve 26–36, 63'te %30–48 düşük, %5–10 artış). Asıl makale J Cachexia Sarcopenia Muscle 2025;16(6) — DOI'si okunmadı, yalnızca ScienceDaily bağlantısı var.
- Tai chi 20 yıl (IL_TAICHI): Mark & Wang, Curr Rheumatol Rep 2026;28:30, çevrimiçi 9 Ekim 2026 (Springer sayfası okundu: 19 RKÇ/2.031 kişi + 34 derleme, diz-kalça OA en güçlü, RA yetersiz, anlatısal derleme).
- GAE haberi (Radiology, Charité 194 hasta) Ekim'de yeniden basına çıktı ama Haziran 2026'da zaten eklenmişti; tekrar eklenmedi.
- Çeviri: i18n/todo/yen6.json + done/yen6.json (y6-0…14), yen5 ile aynı yöntem (export_todo yenilikler.html çalıştırılmadı).

## Bilgi köşesi, 3 rehber daha (16 Ekim 2026): cond46–48
- Siyatik istenmişti ama "Bel fıtığı ve siyatik" (bel-fitigi.html) zaten var; yerine diz kapağı çıkığı eklendi (kullanıcıya söylendi).
- cond46 diz-kapagi-cikigi.html → en/dislocated-kneecap.html (PD, diz, C_ACL'den sonra). NHS Dislocated kneecap (10 Mart 2026), Sherwood Forest PIL202607-03-PD (Temmuz 2026), RUH Bath PHY/035 (2020), Cochrane Smith 2023 (CD008106.pub4: 10 çalışma/519 kişi, ameliyatsız 348/1000 yeniden çıkma, ameliyat 157/1000 daha az, çok düşük kesinlik). Egzersiz: dk_quad, dk_slr, dk_bend(hslide), dk_bridge.
- cond47 kubital-tunel-sendromu.html → en/cubital-tunnel-syndrome.html (CU, omuz, C_CTS'den sonra). EKHUFT Web 597 (Mart 2025), Royal Berkshire (Ocak 2024), Right Decision Service (NHS Scotland; kurum/tarih yazmıyor), Cochrane Caliandro 2016 (51 kişi bilgilendirme; 55 kişi kortizon %28/%30; gevşetme ~%70 / taşıma ~%75, enfeksiyon ~%4/%12). Yeni çizim SV["uglide"] (ulnar sinir kaydırma, dirsek bükülüp el başa). Egzersiz: cu_glide, cu_roll(ly_shrug).
- cond48 asil-tendonu-kopmasi.html → en/achilles-tendon-rupture.html (AR, ayak, C_ACHILLES'ten sonra). Royal Berkshire (Ekim 2025), Sherwood Forest PIL202606-03-ATR (Haziran 2026; bot dönemi egzersizleri 10×3 sn), NHS Fife (Şubat 2024; spora dönüş süreleri), Myhrvold NEJM 2022 (554 kişi; yeniden kopma %6,2/%0,6; sinir hasarı %0,6/%2,8/%5,2). Egzersiz: ar_quad, ar_slr, ar_kext, ar_hext, ar_sabd.
- "Norveç'te" bilgisi (Myhrvold) bellekten; NEJM sayfası okunmadı.
- fb516–521 (kart açıklamaları, haplar).

## Kendine iyi bak, 7. tur (16 Ekim 2026): self7_part.py
- Adım hedefi ve oturma–hareket dengesi düşünülmüştü; hareket.html (Ding 2025 adım), masa-basi.html (Ekelund 2016) ve hareket-atistirmaliklari (Duran 2023) zaten kapsıyor. Yerine nabız ölçer ve bel–boy oranı yapıldı.
- nabiz-olcer.html → en/pulse-check.html (C_PULSE, "Kendinizi ölçün" 5. sıra). 30/60 sn geri sayım (WAKE_JS, bip, titreşim, sekme gizlenince iptal), atım sayısı → atım/dk, dinlenme/egzersiz, ritim (düzenli/düzensiz/emin değilim), 220−yaş ve %50–70 / %70–85 (AHA 12 Ağu 2024), 60–100 ve düşük/yüksek/düzensiz mesajları (BHF 18 Eki 2024), acil listesi NHS Heart palpitations (17 Mart 2026; 999 → 112). localStorage drihsaneren.nabiz.v1, WhatsApp.
- bel-boy-orani.html → en/waist-to-height-ratio.html (C_WHTR, 6. sıra). NICE NG246 sınırları 0,4–0,49 / 0,5–0,59 / ≥0,6, ölçüm yöntemi, BKİ<35, 5 yaş+ çocuklar, etnik köken notu; CG189 "Other information". Gösterge çubuğu 0,35–0,75, hedef bel = boy/2, kaydet → localStorage drihsaneren.belboy.v1 (+ .h boy hatırlanır), WhatsApp.
- reg_self EXEC'i kapi_part'tan sonra ekledi; sıra elle self4, self5, self6, self7 yapıldı. fb522–524.

## Bilim gündemi, 3 haber (16 Ekim 2026, ikinci tur)
- IL_DEMPA (beyin, Ağustos 2026): Feter ve ark., The Lancet Public Health 2026, "Domain-specific physical activity levels and risk of dementia" (74 çalışma, 4,2 milyon kişi; boş zaman −%24, iş +%20, ev işi −%15, işe aktif ulaşım +%10). PsyPost 8 Eylül 2026'dan okundu. DOI (10.1016/S2468-2667(26)00142-8) The Conversation'daki PII'den türetildi, açılıp doğrulanmadı.
- IL_REACT (kalp, Ağustos 2026): Bundgaard ve ark., NEJM 2026 (DOI 10.1056/NEJMoa2609059), ESC 2026 Hot Line 29 Ağustos; 16.808 kişi, %57,1 plak, 18–29 yaşta 1/13. News-Medical ve ScienceDaily'den okundu.
- IL_CAVD (hareket, Mayıs 2026): The BMJ 2026, DOI 10.1136/bmj-2025-088050 (69 RKÇ, 153.902 kişi); BMJ basın bülteni 20 Mayıs 2026'dan okundu.
- Çeviri: i18n/todo/yen7.json + done/yen7.json (y7-0…15).
- Ekim'deki ScienceDaily haberlerinin çoğu eski çalışmaların yeniden yayımıydı (ör. yürüyüş değiştirme Lancet Rheum 2025 — Ekim 2025'te zaten eklenmişti); eklenmedi.

## Bilgi köşesi, 3 rehber (16 Ekim 2026, ikinci tur): cond49–51
- cond49 omuz-kireclenmesi.html → en/shoulder-osteoarthritis.html (SO, omuz, C_SHOULDER'dan sonra). Northern Devon leaflet 527, RUH PHY/024 (2020), NHS Lothian (Mayıs 2024), ELHT PHYSIO-001. Egzersiz: so_pend(cf_pendf), so_stick(cf_stickf), so_table(towel), so_back (EX "Havlu ile germe" çizimi → SV["so_backf"]).
- cond50 baldir-kasi-zorlanmasi.html → en/calf-strain.html (CZ, ayak, C_SS'ten sonra). HEY231/2025, Plymouth (Şubat 2025), Royal Free RFL1181 (Haziran 2026), NHS DVT (30 Nisan 2026). Egzersiz: cz_pump, cz_towel, cz_calf, cz_sol, cz_heel, cz_sls.
- cond51 ayak-bilegi-kirigi.html → en/ankle-fracture.html (AK, ayak, C_ANKLE'dan sonra). WWL Musc 080 v3 (Temmuz 2026), NHS Lothian v2.1 (Haziran 2025), RUH (2017), ULHT (Haziran 2025), Kortekangas BMJ 2019;364:k5432 (yalnızca özet bloğundan; n okunmadı), NHS DVT. Egzersiz: ak_pump, ak_towel, ak_calf, ak_heel, ak_sts, ak_sls.

## Kendine iyi bak, 8. tur (16 Ekim 2026): self8_part.py
- kalk-yuru-testi.html → en/timed-up-and-go.html (C_TUG, "Kendinizi ölçün" yürüme hızından sonra). CDC STEADI TUG (2017; ≥12 sn risk, gözlem listesi), Bohannon 2006 (8,1/9,2/11,3 sn ve GA üst sınırları). Gözlem kutuları sonucu "Değerlendirme önerilir"e çevirir. localStorage drihsaneren.tug.v1.
- mola-zamanlayicisi.html → en/desk-break-timer.html (C_MOLA, "Zamanlayıcıyla birlikte yapın" sonu). 20 dk göz (20 sn) + 30/60 dk hareket (5 dk) molası, Date.now tabanlı, ses/titreşim/sekme başlığı/isteğe bağlı Notification, günlük sayaç drihsaneren.mola.v1. Test kancası window.__mz (set/st/end). Kaynak: AAO computer usage, Duran 2023, WHO 2020.
- reg_self sırası elle self4…self8. fb525–531. bel-boy-orani EN "movement snacks" → "activity snacks" düzeltildi.
- Kendine iyi bak tanıtım videosu (16 Ekim 2026): scratchpad /tmp/claude-0/-home-claude/b0063e9c-5c48-589d-b9ce-8371b9238425/scratchpad/vid7 (film.py 7 sahne 44 sn 1080x1920, music.py özgün sentez, timing.json). Örnek ekranlar: sandalye 13, denge 10 sn, yürüme 1,12 m/sn, TUG 9,4 sn, nabız 72, bel–boy 0,47 ("Örnek ekranlar" yazılı). Çıktı: out/kendine-iyi-bak-video.mp4 (6,8 MB, ortalama -17,5 dB).
- Karekod (fb_qr.py, 16 Ekim 2026): imleç üstündeyken eğme/büyütme (rotateX/Y, scale), imleci izleyen ışık (nq-gl) ve mouseenter'da dalgayı yeniden başlatma kaldırıldı; kullanıcı bulanık göründüğünü söyledi. Hover'da yalnızca çerçeve/ışıltı güçleniyor.

## 18 Ekim 2026 turu (3 rehber, 2 araç, 3 haber)
- Rehberler: cond52 köprücük kemiği kırığı (KL, en/broken-collarbone), cond53 büyüme ağrıları (GRP, en/growing-pains), cond54 bel fıtığı ameliyatı sonrası (BFA, en/after-lumbar-disc-surgery). İT bant sendromu kaynak zayıf olduğu için yapılmadı.
- self9_part.py: dusme-riski-testi (C_FR, CDC STEADI Stay Independent 12 madde, ≥4 puan) ve dort-asamali-denge-testi (C_B4, CDC 4-Stage; süre ileri sayar, test hook window.__b4). SVG'lerde gizleme toggleAttribute ile (svg.hidden özelliği yok).
- Haberler (yen8, y8-0…14): gençlerde inme (Neurology), yalnızlık (Nature Communications), İngiltere'de tansiyon (BMJ Public Health). fb532–536 kart açıklamaları.
- Sonraki yen batch: yen9. Son fb: fb536.
- Öne çıkan yıldız: PREM = {"dizin-12-sirri.html", "uc-kapi.html"} (build_pages.py). KC kartında "kc prem" (sağ üst köşede altın yıldız rozeti, ::before; liste görünümünde küçük resmin köşesinde), hap linklerinde "pill prem" (yazının yanında küçük yıldız, ::after). Yıldız CSS'te data-URI SVG, çeviriye etkisi yok.
- Bilgi köşesi her açılışta liste görünümüyle başlar; kart görünümü yalnızca o ziyarette geçerli (eski bk-view kaydı siliniyor).
- 19 Ekim: yıldız artık satır içi SVG (STAR sabiti, .prem-s); data-URI arka plan kaldırıldı. Kartlarda <span class="kc-star">, haplarda yazının yanında, haber başlık listesinde (hl-c) ve haber kartı etiketinde Nobel için (_nprem: cat "Nobel" ile başlıyorsa). PREM'e nobel-2026.html eklendi.

## 19 Ekim 2026 turu (3 rehber, 2 araç, 3 haber)
- Rehberler: cond55 kaburga kırığı (KB, en/broken-ribs; kb_breath, kb_cough yeni çizim), cond56 kasık zorlanması (KS, en/groin-strain; ks_ball, ks_bridge, ks_low, ks_band yeni çizim), cond57 çekiç parmak (MF, en/mallet-finger; mf_pip, mf_spread, mf_hook, mf_fist yeni çizim).
- self10_part.py: pelvik-taban-zamanlayicisi (C_PFT, drihsaneren.pelvik.v1, test hook __pf) ve tempolu-yuruyus (C_TEMPO, Web Audio metronom, drihsaneren.tempo.v1, __tp). Grup: "Zamanlayıcıyla birlikte yapın".
- Haberler (yen9, y9-0…13): genikülat arter embolizasyonu (Radiology), robotik protez (The BMJ), haftada 1 duvar oturuşu (BMJ OSEM). fb537–542.
- Dikkat: publish.sh'den önce her zaman rebuild_home.sh çalıştırılmalı (yoksa splice_home END işaretini bulamaz).
- Sonraki yen batch: yen10. Son fb: fb542.

## 19 Ekim 2026 akşam turu (3 rehber, 2 araç, 3 haber)
- Rehberler: cond58 omuz ucu (AC eklem) yaralanması (ACJ, en/ac-joint-injury; ac_assist yeni çizim), cond59 5. metatars kırığı (MT5, en/fifth-metatarsal-fracture; mt_circle, mt_toes, mt_inout yeni), cond60 bebeklerde tortikolis (TOR, en/torticollis-in-babies; tor_side, tor_rot, tor_carry, tor_tummy yeni; bölge boyun).
- self11_part.py: dustukten-sonra-kalkma (C_GETUP, "Günlük hayat için" grubunun başında; soru → yardım/8 adım/bitti akışı, __gu) ve oturma-suresi (C_SIT, Ekelund 2016 Lancet Tablo 2 ve 3; hücre metinleri JS ile dile göre yazılır).
- Haberler (yen10, y10-0…12): VITAL anestezi (JAMA), DBS depresyon yolları (Am J Psychiatry), kanserde yapılandırılmış egzersiz (BJSM). fb543–551.
- DÜZELTME: Önceki turda eklenen Ekim 2026 GAE haberi, Haziran 2026'daki aynı Charité çalışmasının tekrarıydı; kaldırıldı ve ikinci IL_GAE tanımı silindi (Haziran haberi kendi çizimine döndü). Yeni haber eklerken NEWS listesinde aynı çalışma var mı diye başlık/kurum/örneklem ile kontrol et.
- Sonraki yen batch: yen11. Son fb: fb551.

## 19 Ekim 23:00 — AZ KAYNAKLI SAYFALARA KAYNAK EKLEME (yarım kaldı, kullanım hakkı sıfırlanınca devam)
Hedef: ≤2 kaynaklı 21 sayfa: agri-gunlugu(1, self6), arka-uyluk-zorlanmasi(2, cond35), ayak-bilegi-burkulmasi(2, ankle_part), bebeklerde-tortikolis(2, cond60), bel-boy-orani(2, self7), cene-eklemi(2, cond4), dort-asamali-denge-testi(1, self9), dusme-riski-testi(2, self9), egzersizde-agri(2, self4), eklem-hipermobilitesi(2, cond40), golfcu-dirsegi(2, cond18), ic-cekis(2, self2), kaburga-kirigi(2, cond55), kalca-yan-agrisi(2, cond14), kalk-yuru-testi(2, self8), morton-noromasi(2, cond38), otur-kalk-testi(2, self2), oturma-suresi(2, self11), pelvik-taban-zamanlayicisi(2, self10), sabah-rutini(1, self_part).
Her sayfaya en az 1 kılavuz/derleme; kaynağı okuyup içerikle bağla (gerekirse 1–2 TR cümle).
Çeviri yöntemi (TR metni değişirse): i18n/todo|done/<ad>.json → <ad>__v1.json olarak yeniden adlandır (mem'de kalır), sayfayı derle, export_todo yalnızca yeni cümleleri çıkarır, en_tool ile çevir. Yalnız İngilizce kaynak satırı eklemek çeviri gerektirmez (english_ref → identity).
Okunmuş kaynaklar:
- NICE NG210 (2021) pelvik taban: 1.3.9 tüm kadınlara PFMT; 1.6.14 stres/karışık kaçırmada en az 3 ay denetimli program; fizyoterapist denetimi; erkekler kapsamda değil. URL https://www.nice.org.uk/guidance/NG210/chapter/Recommendations
- NICE NG249 (29 Nisan 2025) düşmeler: 1.1.1 "düşme riski tahmin araçlarını kullanmayın"; TUG gibi testler yürüme/denge sorununu gözlemek için, riski tahmin etmez; son bir yılda düşmeyi sorun; kapsamlı değerlendirme kriterleri (kırılganlık, tıbbi tedavi gerektiren yaralanma, bilinç kaybı, yardımsız kalkamama, ≥2 düşme); egzersiz programları ilerleyici, denge-koordinasyon-kuvvet; 1.5.1 düşme sonrası ne yapılacağı ve nasıl kalkılacağı anlatılmalı. URL https://www.nice.org.uk/guidance/ng249/resources/falls-assessment-and-prevention-in-older-people-and-in-people-50-and-over-at-higher-risk-pdf-66143964997573
- World Falls Guidelines: Montero-Odasso M, et al. Age Ageing. 2022;51(9):afac205. doi:10.1093/ageing/afac205 (fırsatçı tarama; yüksek riskte çok faktörlü değerlendirme; tekrarlayan düşme = 12 ayda ≥2).
- CMT kılavuzu: Kaplan SL, Coulter C, Sargent B. Pediatr Phys Ther. 2018;30(4):240–290. doi:10.1097/PEP.0000000000000544; güncel: Sargent B, et al. Pediatr Phys Ther. 2024;36(4):370–421 (taburculuk: pasif boyun hareketi sağlam tarafla 5° içinde, görünür eğiklik yok, yaşa uygun motor gelişim, simetrik hareket, bakım veren egzersizleri biliyor). İçerik (eylem maddeleri) henüz okunamadı.
Önemli: düşme riski testi, 4 aşamalı denge ve TUG sayfalarına NICE NG249'un "bu testler riski tek başına tahmin etmez" notu eklenmeli.
- 19 Ekim gece: TAMAMLANDI. 21 sayfanın hepsi ≥3 kaynak, her birinde en az 1 kılavuz/derleme. Yeni TR cümleler (SSS) 16 sayfada; __v1 yöntemiyle çevrildi. Kaynaklar: NICE NG249 + Dünya Düşme Kılavuzu (düşme/denge/TUG/kalkma), Browne&Nair 2019 (TUG), NICE NG210 (pelvik), Battle 2012/2023 (kaburga), APTA CMT 2018 (tortikolis), Ekelund 2020 BJSM + WHO 2020 (oturma, otur-kalk), Fincham 2023 (iç çekiş), IMMPACT 2008 + Redelmeier 1996 (ağrı günlüğü), Geneen 2017 Cochrane özet (egzersizde ağrı), Ashwell 2012 (bel-boy), Paton 2023 (arka uyluk), See 2026 (golfçü), Cordeiro 2024 + NHS Ayrshire (kalça yan), Vuurberg 2018 + NHS (ayak bileği), NHS TMD (çene), Castori 2017 (hipermobilite), NHS Tayside (Morton), Brooke-Wavell 2022 + NHS düşük tansiyon (sabah rutini).
- DİKKAT: export_todo'yu __v1 yapmadan çalıştırma; mevcut todo'yu yalnız yeni cümlelerle ezer (git checkout ile düzeltildi).

## 20 Ekim — KAYNAK TURU 2 (sayfalar tamam, haberler sırada)
- 54 sayfaya kaynak eklendi; artık hiçbir sayfa 4'ten az kaynaklı değil (67 sayfa 4, kalanlar 5+). 13 sayfaya kısa TR SSS/cümle (__v1). Beighton eşiği 2017 ölçütlerine göre düzeltildi (çocuk 6, ≤50 yaş 5, >50 4).
- Yalnız İngilizce kaynak satırı eklenen sayfalarda make_en "eksik" verirse: i18n'i __vN yap, export_todo çalıştır (identity'ye otomatik ekler), boş kalanları geri adlandır; kalanları "==" ile çevir.
- SIRADA: Bilim gündemi — tek kaynaklı / dergi kaynağı olmayan 26 habere birincil yayın + bağımsız kaynak.
- 20 Ekim: Bilim gündemi tamam. 21 habere birincil yayın (DOI) ya da bağımsız kaynak eklendi; artık tüm haberlerde en az 2 kaynak var. Çeviriler yenilikler__v1/__v2 yöntemiyle.
- DİKKAT: yenilikler.html için export_todo'dan ÖNCE yenilikler.json'u __vN yap; yoksa done id'leri kayar.

## 20 Ekim akşam — BİLİMSEL DENETİM (kullanıcının yüklediği rapor, "yalnızca uygunsa uygula")
- Kullanıcı `drihsaneren_uc_bolum_bilimsel_denetim_CLAUDE_ICIN_KONTROLLU_SURUM.md` yükledi: 52 bulgu (Bilgi köşesi hastalık 16, rehabilitasyon 9, Kendine iyi bak 16, Bilim gündemi 11). Raporun kendisi "salt okunur" diyordu; kullanıcı ardından "kontrol et, yalnızca uygunsa uygula" dedi. Her bulgu sitedeki tam cümle + asıl kaynakla karşılaştırıldı; doğrulama raporu Claude Docs belgesinde: https://claude.ai/code/artifact/62a90583-1519-46ed-b3c2-c67cf2205b19
- Sonuç: 6 gerçek hata düzeltildi (fibromiyalji tanısı "dışlama" → 2016 ölçütleri birlikte bulunabilir; De Quervain kanıtı Challoumas 2023 JAMA Netw Open NMA ile güncellendi; topuk dikeni "10'da 1" plantar fasiite ait; iç çekiş "hepsi nefes verişini uzatır" kutu nefesi için yanlış; Ekim lakozamid haberi Haziran'daki aynı Yale çalışmasının kopyasıydı, silindi → 47 haber; yenilikler tarihi 20 Ekim). 29 maddede ifade/bağlam yumuşatıldı (gözlemsel → "ilişkili", göreli/mutlak risk, hasta grubu, broşür atfı). 17 maddede değişiklik gerekmedi.
- Eklenen kaynaklar: Wolfe 2016 (fibromiyalji), StatPearls Margetis 2025 (bel kayması; kart artık "L4–L5", istmikte L5–S1), Challoumas 2023 (De Quervain), Roadley 2026 Spine RCT (mikrodiskektomi kısıtlamaları; yeni SSS), NHS SIDS (tortikolis: uykuda sırtüstü; karın üstü günde ≥3, APTA), Martin 2015 (derin gluteal sendrom), MSKTC otonom disrefleksi, NICE QS2 (inme 3 saate katılamayanlar), St George's PHP_PFR_04 (pelvik taban aşırı gerginlik uyarısı).
- DOKUNULMADI / kullanıcı kararı: inme sayfasındaki akupunktur "klinik gözlemim" kutusu (rapor kaldırmayı önerdi; kutu kullanıcının 7 Ekim isteği, karar kullanıcıda). Enlisitid onay tarihi sitede 17 Temmuz, Merck bülteni 16 Temmuz (FDA sayfası açılamadı). Rapordaki De Quervain 2024 derlemesi (PMID 38642740, 16 çalışma/1.206) açılamadı; kullanılmadı. Nakashima %87,6 bu oturumda açılamadı. Anestezi (VITAL) başlığı değiştirilmedi (anchor index.html'de kullanılıyor; gövde grubu zaten veriyor).
- İngilizce: rapor "EN için ayrı onay" diyordu ama sitenin kuralı TR+EN birlikte; EN de güncellendi.
- Hafızadan künyeler: 21'i kaynağından açılıp doğrulandı (hepsi doğru, düzeltme yok); 17'si açılamadı (liste Docs raporunun E bölümünde).
- Çeviri: i18n/todo|done/den1.json (71 birim), den2.json (2). Yeni araç `collect_todo.py`: değişen sayfaların bellekte olmayan birimlerini tek yeni dosyaya toplar; __vN yeniden adlandırmaya gerek kalmaz. Sonraki batch: den3.
- Haber başlığı değişince anchor (news_id) da değişir; index.html/bilgi.html bağlantıları kendiliğinden güncellenir, dış bağlantılar kırılabilir.
- Web erişimi notu: kullanıcı yokken yeni alan adlarına WebFetch onay bekleyip düşüyor; WebSearch sonuçlarındaki adresler açılabiliyor. pubmed.ncbi.nlm.nih.gov boş döner, PMC bazen captcha verir; Europe PMC 429 verdi.

## 22 Ekim 2026 turu (3 rehber, 2 araç, 3 haber) — bol kaynaklı
Kullanıcı: "bilgi köşesi, kendine iyi bak, bilim gündemi, bol kaynaklı eklemeye devam". Akupunktur kutusu sorusuna "tercih yok" dedi → inme sayfasındaki kutu AYNEN kaldı.
- **Kayıt artık depoda:** `reg_tur.py` (sayfa + kart + hap + RELATED + i18n_map + haber + IL çizimi; tekrar çalıştırılınca eklenenleri atlar). Sonraki turda CONDS/SELFS/NEWS_ADD listelerini değiştirip kullanın. Scratchpad'deki eski reg_cond.py/reg_self.py yok.
- **Exec sırası:** cond61–63 artık `self12_part.py`'den SONRA exec ediliyor (cond61 `sn_stair` çizimini kullanıyor; o self4'te tanımlı).
- cond61 periferik-arter-hastaligi.html → en/peripheral-arterial-disease.html (C_PAD, REHAB, C_CARDIAC'tan sonra). 10 kaynak: NICE CG147, Lane 2017 Cochrane (+NIHR özeti), Gornik 2024 ACC/AHA (ACC özeti), Mazzolai 2024 ESC uzlaşı (Vasa 53(2):87–108; kabul edilmiş metin okundu), McDermott 2021 LITE JAMA, Song 2019 Lancet Glob Health, NHS PAD+tedavi (10 Nis 2026), NHS D&G Right Decisions (29 Nis 2026), NCEPOD 2025 broşürü. Kaynaksız/genel: güç egzersizlerinin seçimi ve dozları (sayfada böyle yazıyor), "yürürken göğüs ağrısı" maddesi.
- cond62 beyin-sarsintisi.html → en/concussion.html (C_CONC, boyun, C_VERTIGO'dan sonra). 7 kaynak: Patricios 2023 BJSM Amsterdam uzlaşısı (BMJ bülteni okundu; cilt/sayı 57(11) hafızadan), UK grassroots kılavuzu (Kasım 2024; 6 aşama, 21. gün), NHS 111 Wales (19 Kas 2024), Leddy 2019, Thomas 2015, Schneider 2014, SCHN denge notu (Ağu 2026; egzersizler buradan). Kaynaksız/genel: belirti listesinin bir kısmı (ışık/ses hassasiyeti, sisli hissetme), "yukarı-aşağı bakma" dozu. APTA 2020 kılavuzu (Quatman-Yates) okunamadı, kullanılmadı.
- cond63 pelvik-organ-sarkmasi.html → en/pelvic-organ-prolapse.html (C_POP, kadin, C_UI'dan sonra). 8 kaynak: NICE NG123, Hagen 2014 POPPY (tam metin: 5 seans/16 hafta; ev: 10×10 sn + 50 hızlı, günde 3), Hagen & Stark Cochrane (yıl 2011;(12) — cochrane.org "2021 Issue 6" gösteriyordu, ALINMADI), Kearney 2024 TOPSY, NHS tedavi (3 Tem 2025), NHS 111 Wales (8 Nis 2025), CUH broşürü (v5 Tem 2024), MFT SMPIL-24-036. Kaynaksız/genel: pesserde kanama/akıntı uyarısı, menopoz sonrası kanama notu, kaldırma tekniği ayrıntısı. Li 2016 meta-analizi özeti okunamadı, kullanılmadı.
- self12_part.py: guc-devresi.html → en/home-strength-circuit.html (C_GD, "Zamanlayıcıyla birlikte yapın", hareket atıştırmalıklarından sonra; 4/6 hareket, 30+30 ya da 40+20 sn, 1–3 tur; sesli ad okuma isteğe bağlı; haftalık gün sayacı drihsaneren.guc.v1; test kancası window.__gd). iki-dakika-adim-testi.html → en/two-minute-step-test.html (C_AD, "Kendinizi ölçün", yürüme hızından sonra; dokunarak sayaç ya da elle giriş; Rikli & Jones 1999b yüzdelikleri + 2013 bağımsızlık eşikleri (SRA sayfasından); drihsaneren.adim2.v1; __ad). Kaynaklar: DSÖ, Bull 2020, Momma 2022 (bitiş sayfası 763 hafızadan), Currier 2023, Sciamanna 2026 FAST-2 (makale başlığı okunamadı; DOI + Penn State haberi), NHS strength exercises; SRA 2MST, Rikli & Jones 1999a/b, 2013, Human Kinetics alıntısı.
- Haberler (yen11, IL_ACLX/IL_HIPOA/IL_FAST4, tarih sırasına göre): SUPER-Knee (Ann Intern Med 29 Eyl 2026; birincil DOI + News-Medical + Medical Dialogues — Annals sayfası açılamadı, sayılar iki ikincil kaynakta tutarlı), Cochrane kalça OA 2026 (23 Tem 2026; Cochrane sade özet + Sidney Üniv.), FAST-2 (PLOS One 2026; Penn State + PSH haberleri). Elenen: ANA 2026 adım sayısı–nörolojik hastalık bildirisi (düzeltilmiş sonuç anlamsız, hakemli değil), 3.000 adım–Alzheimer (Kasım 2025 Nature Medicine'in yeniden yayımı), DEAF1 (Haziran 2026, mekanizma), 4 dk günde uyku (2025).
- Çeviri: i18n/todo|done/tur12.json (422 birim), collect_todo.py ile. Sonraki batch adı serbest (ör. tur13).
- DÜZELTME (yan bulgu): `table.nt` tabloları (kalk-yuru-testi, sandalye-testi, yurume-hizi-testi, iki-dakika) self2'deki `.nt{display:grid}` yüzünden bozuk görünüyordu; self5_part.py'ye `table.nt{display:table}` eklendi (SELF5+ CSS kullanan sayfalarda yalnızca bu satır değişti).
- t_ls notu: 6 SSS'li sayfalarda "sss=6" uyarısı (betik 4 bekliyor) beklenen durum; araç sayfalarında egzersiz=0 da beklenen.

## 23 Ekim 2026 turu (2. tur: 3 rehber, 2 araç, 3 haber) — bol kaynaklı
Kullanıcı: "devam edelim eklemeye". Kayıt yine `reg_tur.py` ile; CONDS/SELFS/RELATED/IL_NEW/NEWS_ADD listeleri bu turun sayfalarıyla DEĞİŞTİRİLDİ (1. turun listeleri git geçmişinde, fcf2047). Exec zinciri: … cond63 → self13 → cond64 → cond65 → cond66 → nobel. Betik idempotent (iki kez çalıştırıldı, fark yok).
- cond64 kalp-yetmezligi.html → en/heart-failure.html (C_HF, REHAB, C_PAD'den sonra). 8 kaynak: Molloy 2023 Cochrane (EJHF doi:10.1002/ejhf.3046; 60 RKÇ, 8.728 kişi, yatış %31↓, NNT 13), McDonagh 2021 ESC (Hadjiphilippou & Lane BJC 2022 özeti), NICE NG106 halk bilgisi, NHS belirtiler+tedavi (26 Haz 2026), BHF Heart Matters (27 Oca 2026), UHB "Top tips" PI25/3263/04 (Haz 2025; 2 litre sıvı, 3–4 günde 2 kg), Queensland HF egzersiz föyleri (2010; Borg 9–13), Liu 2024 ESC Heart Fail 11(5):3264–3278 (56 milyon). Kaynaksız/genel: kırmızı bayraklardaki "dinlenmekle geçmeyen göğüs ağrısı", egzersiz seçimi ve dozları (sayfada genel öneri olduğu yazıyor).
- cond65 dupuytren-kontrakturu.html → en/dupuytrens-contracture.html (C_DUP, omuz bölgesi, C_TF'den sonra). 7 kaynak: NHS genel/tedavi/iyileşme (18 Haz 2024), HSE (4 Eki 2023), BSSH broşürü 2016, NHS Scotland ulusal broşür (30°), NHS GGC Right Decisions MSK (9 May 2024; egzersizler ve günde 4–6 kez buradan), Jerosch-Herold 2011 BMC MSD 12:136 (154 kişi, gece ateli ek yarar yok), Dias 2024 DISC HTA 28(78) (672 kişi). Kaynaksız/genel: "kollajenaz her merkezde bulunmaz" ifadesi.
- cond66 omurga-kirigi.html → en/vertebral-fracture.html (C_VF, bel, C_KY'den sonra). 7 kaynak: Brooke-Wavell 2022 BJSM 56(15):837–846 (İngiltere uzlaşısı), Gibbs 2019 Cochrane CD008618 (9 çalışma, 749 kişi, TUG −1,1 sn; 3 çalışmada 4 yan olay), Barker 2019 PROVE HTA 23(44) (615 kişi), Bristol Vertebral Fractures Study tanı rehberi (25 Kas 2022), Leyland/BackCare 2021 (güncelleme 5 Haz 2024; korse gerekmez), Leeds Community Healthcare (12 Mar 2026), ROS egzersiz sayfası (Şub 2019; 3–5 sn tutma, günde en az 1). Kaynaksız/genel: nörolojik belirti ve ateş/kilo kaybı/kanser kırmızı bayrakları.
- self13_part.py (SELF13_CSS = SELF12_CSS + …): yemek-sonrasi-yuruyus.html → en/walk-after-meals.html (C_YY, "Zamanlayıcıyla birlikte yapın", tempolu yürüyüşten sonra; öğün seçimi saate göre varsayılan, 3/10/15 dk, dakikada bip, yarı yolda uyarı, bugün 3 öğün işareti + 7 gün; drihsaneren.yemekyuruyus.v1; kanca window.__yy {st, ff}). Kaynaklar: Reynolds 2016 Diabetologia (41 kişi, %12/%22; HCPLive), Buffey 2022 Sports Med (7 çalışma, 2–5 dk, 60–90 dk zirve; MDedge), Colberg 2016 ADA (30 dakikada bir mola, hipoglisemi; AJMC), Bull 2020 DSÖ. Bu turda WebFetch günlük sınıra takıldı; bu üç haber sayfası 2. kez okunamadı, sayılar 1. turdaki okumaya dayanıyor.
  denge-antrenmani.html → en/balance-training.html (C_DB, aynı grup, yemek sonrası yürüyüşten sonra; Otago'dan 6 hareket: topuk-burun duruş, tek ayak, topuk-burun yürüyüş 20, yana yürüme 10+10, parmak ucunda 10, sandalyeden kalkma; 3 destek seviyesi (iki el / tek el / tutunmadan — sayfada "basitleştirilmiş uyarlama" diye yazıyor); duruşlarda 3 sn hazırlan → 10 sn birinci ayak → 3 sn ayak değiştir → 10 sn ikinci ayak; yürüyüşlerde İleri; haftalık seans + hedefe ulaşılan hafta (≥3/hafta) sayacı; drihsaneren.denge.v1; kanca window.__db {st, skip}). Kaynaklar: Sherrington 2019 Cochrane (cochrane.org özeti + MDedge okundu), Thomas 2010 Age Ageing (özet okundu: 7 çalışma, 1.503 kişi, 81,6 yaş, IRR 0,68), Montero-Odasso 2022 Dünya Düşme Kılavuzu (RoSPA sunumu), ROH Otago sayfası (okundu; dozlar ve "sandalyeye değil tezgâha tutun" buradan). Kaynaksız/genel: "mümkünse yakınınızda biri olsun", kaymayan zemin/düz ayakkabı.
- Haberler (IL_ESTEPS/IL_BELT/IL_PACBACK, tarih sırasına göre): eSTEPS (JAMA Netw Open 16 Eki 2026, doi 10.1001/jamanetworkopen.2026.39240; Medical Daily + UTMB + 2 Minute Medicine okundu; 19,3 vs 21,2 /100 hasta-yılı, %22 reçete), LOMBACT bel korsesi (JAMA Netw Open 19 Ağu 2026, doi …2026.29793; ScienceAlert + Harvard Health okundu; üretici finansmanı ve DSÖ 2023 notu), PACBACK (JAMA Intern Med Haziran 2026, doi 10.1001/jamainternmed.2026.1893; ReachMD + News-Medical okundu; −1,7 puan, %64 vs %55, aracılık %76).
- Çeviri: i18n/todo|done/tur13.json (352 birim). İngilizce sayaç metinleri çoğul sorunu yüzünden "Meals walked after today: {n}" / "Sessions this week: {n}" biçiminde yazıldı. Sonraki batch: tur14.
- Testler: t_ls "sorun: 0"; 360/390/1366/1440'ta yeni sayfalarda taşma yok (index'teki gün şeridi kendi içinde kayıyor, sayfa taşması değil); iki araç TR+EN'de baştan sona çalıştırıldı, sayfa hatası yok. Yerel test betikleri scratchpad'de: t_tools13.py, sw.py (sayfa düzeyi taşma), rb.sh (derle+yayımla).

## 23 Ekim 2026 akşam — KAYNAK TURU 3 (4 kaynaklı sayfalar → en az 5)
Kullanıcı: "Devam kaynakları da artıralım". Önce 2. turun açıkları kapatıldı, sonra 4 kaynaklı 63 sayfaya kaynak eklendi; artık hiçbir sayfa 5'ten az kaynaklı değil (95 sayfa 5, kalanlar 6+). Her yeni kaynak okunup içerikle bağlandı (çoğunlukla ilgili SSS cevabının sonuna 1–2 cümle).
- Yardımcı: srcedit.py (faq_tail, after, replace, src_after, bump; 24 Ekim itibarıyla depoda, pinfo.py ile birlikte): faq_tail ("soru", "cevap" demetinin sonuna ekler), src_after (çapa URL'sinin satırından sonra aynı girintiyle kaynak satırı ekler).
- 2. tur açıkları: kalp yetmezliği acil maddesi Berkshire Healthcare NHS FT sayfasına göre yeniden yazıldı (göğüs ağrısı, soluk soluğa kalma → 999/112); Dupuytren kollajenaz: EMA, Xiapex AB ruhsatı 1 Mart 2020'de üreticinin isteğiyle (ticari) geri çekildi; omurga kırığı kırmızı bayrakları HSE Back pain (14 Tem 2026) + Henschke 2013 Cochrane (kanser öyküsü en anlamlı işaret); yemek sonrası yürüyüş: Reynolds/Buffey/ADA haber sayfaları yeniden okundu (sayılar doğru), hipoglisemi için Know Diabetes + NHS 111 Wales; denge antrenmanına NICE NG249.
- Eklenen başlıca kaynaklar: Askling 2013 (hamstring 28/51 gün), Chimenti 2024 JOSPT (Aşil), Doherty 2017 BJSM (ayak bileği), Frush & Noyes 2015 (Baker), Choi 2021 JBJS (5. metatars), Palmu 2008 JBJS (patella), Neal 2024 BJSM (patellofemoral), Kulig 2009 (PTTD), NICE NG226 (kalça OA), Kemp 2020 BJSM (FAI), Grimaldi & Fearon 2015 + Royal Berkshire Kas 2024 (GTPS), Winters 2018 (MTSS), Thomson 2013 (Morton), Guldhammer 2019 (Osgood), NICE QS16 (kalça kırığı); Blanpied 2017 JOSPT (boyun ×2 + baş ağrısı), Varangot-Reille 2022 (baş ağrısı), BSSH çekiç parmak 2016, NIDCR TMD (Eyl 2026), NHS Orthotic Managers Group ayak bakımı (May 2025), Higo 2024 (hipermobilite), Kloppenburg 2019 EULAR (el OA), Dias 2007 (ganglion), Davenport 2019 BJSM (gebelik), LPT golfçü dirseği (May 2026), Harrison 2019 (huzursuz bacak), EAU kadın LUTS, Mukherjee 2022 EAST (kaburga), NACR 2023 (kalp rehab), Bansal 2014 (kifoz), Abdullah 2025 + Benjamin 2014 (diastaz), Gregson 2022 NOGG, Svernlöv 2009 (kübital; Cochrane'deki 51 kişilik çalışmayla aynı, cümle buna göre), Blanco-Diaz 2025 (koksidini), COTS 2015 (AC eklem), CSP RA el egzersizi (NICE), Ramírez 2023 (SİE), Negrini 2015 Cochrane korse, Karanasios 2021 BJSM (tenisçi); Royal Wolverhampton pacing, Moseley & Butler 2015, Ashwell & Gibson 2016, NG249 (denge testi, otur-kalk, düşme önleme), Thomas 2010 (4 aşamalı, düşme önleme), Sherrington 2019 (düşme riski), Fleming & Brayne 2008 BMJ, Hansford 2021, Hayden 2021 Cochrane, Bull 2020, Paluch 2022, NHS nefes (Haz 2026), Podsiadlo 1991, Sheppard 2018, Tanaka 2001, Patterson 2018, Gardner 2012, Tudor-Locke 2018, Fritz & Lusardi 2009.
- Hafızadan künye ayrıntıları (sayfa/cilt doğrulanamadı): Moseley & Butler 16(9):807–813, Grimaldi 45(11):910–922 (PDF'de doğrulandı), COTS J Orthop Trauma 29(11):479–487, Ashwell BMJ Open 6(3):e010159, Podsiadlo 39(2):142–148, Karanasios 55(9):477–485, Hayden yazar listesi. Varangot-Reille için cilt/sayfa yazılmadı.
- Çeviri: i18n/todo|done/tur14.json (79 birim; değişen SSS'lerde eski İngilizce korunup yeni cümle eklendi). check.py'deki tek uyarı yazar adı (Svernlöv). Sonraki batch: tur15.
- Düzeltme: oturma-suresi aracındaki tablo 360 px'te 6 px taşıyordu (önceden de vardı); self11_part.py'ye ≤380 px için küçük yazı/boşluk eklendi.
- Testler: t_ls sorun 0; değişen 66 TR + 66 EN sayfada 360/390/1366/1440'ta sayfa taşması yok.
- Sırada (öneri): 41 haberde 2 kaynak var, 3'e çıkarılabilir; sonra yeni ekleme turu.

## 23 Ekim 2026 gece — 3. tur (3 rehber, 2 araç, 3 haber + 1 haber güncellemesi) — bol kaynaklı
Kullanıcı: "Devam kaynakları da artıralım" (eklemeye devam + kaynak artırma). Kayıt `reg_tur.py` ile; listeler bu turun sayfalarıyla DEĞİŞTİRİLDİ (önceki turlar git geçmişinde). Exec zinciri: … cond66 → cond67 → cond68 → cond69 → self14 → nobel. Betik idempotent (iki kez çalıştırıldı).
- cond67 diyabette-egzersiz.html → en/exercise-and-diabetes.html (C_DIA, REHAB, C_HF'den sonra). 10 kaynak: Kanaley 2022 ACSM uzlaşısı MSSE 54(2):353–368, ADA Standards of Care 2026 Diabetes Care 49(Suppl 1):S89–S131, Umpierre 2011 JAMA 305(17):1790–1799 (47 RKÇ, −0,67; >150 dk −0,89), Colberg 2016, Reynolds 2016, IDF Atlas 11. baskı (589 milyon), UHCW HIC/LFT/2055 (Nis 2025), Know Diabetes, NHS 111 Wales hipoglisemi, NHS Orthotic Managers ayak broşürü. Kaynaksız/genel: egzersiz seçimi ve dozları (sayfada genel öneri yazıyor), Umpierre yazar listesi hafızadan.
- cond68 yogun-bakim-sonrasi.html → en/recovery-after-intensive-care.html (C_ICU, REHAB, C_DIA'dan sonra). 9 kaynak: NICE CG83, NICE QS158 madde 4 (2–3 ay), Connolly 2016 JCSM 7(5):520–526 (Cochrane özeti; 6 çalışma, 483 kişi), Hatch 2018 Crit Care 22 (4.943 kişi; %46/%40/%22 — makale numarası yazılmadı), Herridge 2011 NEJM 364(14):1293–1304 (109 kişi, %76, işe dönüş %77 — yazar/sayı hafızadan), Fan 2014 AJRCCM 190(12):1437–1446 (ATS; dörtte bir), UHS 2684 v5 (Kas 2024), UHL 1248 (Şub 2025), ICUsteps (13 May 2020). Kaynaksız/genel: kırmızı bayraklar, egzersiz dozları.
- cond69 yuksek-tansiyon.html → en/high-blood-pressure.html (C_HT, REHAB, C_ICU'dan sonra). 11 kaynak: McEvoy 2024 ESC (PCR + ACC özetleri; cilt/sayı 45(38) hafızadan), DSÖ 2025 küresel raporu (HIFA; 1,4 milyar), Cornelissen 2013 JAHA (93 RKÇ), Edwards 2023 BJSM, Hansford 2021, Naci 2019 BJSM (391 çalışma), NICE NG136 (GPnotebook), NHS 111 Wales (4 Ara 2024), nidirect (26 Şub 2026), UHB PI25/3366/06 (Eki 2025), Blood Pressure UK.
- self14_part.py (SELF14_CSS = SELF13_CSS + tg-/aw- sınıfları):
  tansiyon-gunlugu.html → en/blood-pressure-diary.html (C_TG, "Kendinizi ölçün", nabız ölçerden sonra). 5 dk dinlenme → 1. ölçüm → 1 dk → 2. ölçüm; sabah/akşam (saate göre varsayılan); doğrulama (büyük 60–260, küçük 30–160, büyük>küçük, nabız 30–220 ya da boş); ≥180/110 ve ≤90/60 uyarıları (112 belirtileriyle); son 7 gün, ≥4 gün olunca ilk gün hariç ortalama, 135/85 (80+ için 145/85) rozeti; son 14 ölçüm listesi, son ölçümü sil, CSV indir (BOM'lu, ; ayraçlı), iki adımlı "Tümünü sil" (confirm yok). drihsaneren.tansiyon.v1; kanca window.__tg {st, ff}. Kaynaklar: NICE NG136/GPnotebook, NHS 111 Wales, UHB 2025, Blood Pressure UK, ESC 2024, nidirect.
  alti-dakika-yurume-testi.html → en/six-minute-walk-test.html (C_AW, "Kendinizi ölçün", 2 dk adım testinden sonra). Parkur (varsayılan 10 m), yaş/cinsiyet/boy/kilo; 3 sn hazırlık → 6:00, her dakika ATS/ERS standart cesaretlendirme cümlesi + bip; büyük düğme ya da boşluk tuşu = +1 parkur; bitişte 2,5 sn yanlış dokunuş koruması; toplam mesafe elle düzeltilip kaydedilir. Beklenen değer (Enright & Sherrill 1998) yalnızca parkur ≥30 m ve yaş 40–80 iken; önceki testle fark, ≥30 m ise "anlamlı" notu, parkur farklıysa karşılaştırma yok uyarısı; son 10 sonuç. drihsaneren.yurume6.v1; kanca window.__aw {st, ff}. Kaynaklar: Holland 2014 ERS/ATS (tam metin PDF), Enright 1998, ATS hasta bilgisi 2021, CUH (Şub 2025), Polkey 2013 (RBHT özeti).
- Haberler: IL_ESPRESSO (Mart 2026, İnme; Brain Communications fcag057 + Neuroscience News + Auckland Üniv.), IL_OAEX (Şubat 2026, Kireçlenme; RMD Open şemsiye derleme Schleimer/Belavy + BMJ Group + Medical Republic + ScienceDaily + karşı görüş olarak Yan 2025 BMJ ağ meta-analizi), IL_DEPEX (Ocak 2026, Depresyon; Cochrane CD004366.pub7 + ScienceDaily + Science Media Centre uzman görüşleri + HCPLive + Medicine Today). Var olan IL_PDACT (Parkinson, Ekim 2026) aynı çalışma olduğu için yeni haber yazılmadı; sayılar (0,478/0,007; +0,143/−0,783), sınırlılıklar, SPARX3 ve Healio + ScienceDaily kaynakları eklendi (5 kaynak).
- ruh-sagligi-egzersiz (mind_part.py): Cochrane 2026 (Clegg) kaynağı + SSS'ye bir cümle; tarih 23 Ekim 2026.
- Çeviri: tur15 (359 birim) + tur16 (1 birim: nabız alanı notu). İngilizce sayaç metinleri çoğul sorunu yüzünden "Last 7 days · days: {n} · readings: {m}" biçiminde. Sonraki batch: tur17.
- Testler: t_ls sorun 0; yeni ve değişen sayfalar TR+EN 360/390/1366/1440'ta sayfa taşması yok, 360'ta öğe taşması yok; t_tools14.py (scratchpad) iki aracı TR+EN baştan sona çalıştırdı (Enright değerleri elle doğrulandı: kadın 62/168/74 → 494 m, erkek → 521 m), sayfa hatası yok.

## 23 Ekim 2026 gece — KAYNAK TURU 4 (haberler: 2 kaynaklı 41 haber → en az 3)
Kullanıcı yine: "Devam kaynakları da artıralım". Bilim gündemindeki 2 kaynaklı 41 haberin her birine okunmuş üçüncü bir kaynak eklendi (artık 56 haberin 52'si 3, 1'i 4, 3'ü 5 kaynaklı). Eklenenler çoğunlukla üniversite/kurum bülteni ya da bağımsız tıp haberciliği: Critical Care Reviews (VITAL), Mount Sinai (DBS), Neuroscience News (yalnızlık), Oxford (tansiyon), Adelaide (egzersiz-ağrı), Karolinska (SPAF), NCCIH (tai chi), News-Medical (izometrik), Cincinnati Üniv. (genç inme), ecancer (kanser-egzersiz, Galleri, CHALLENGE), Healio (uyku evreleri), Nautilus (sinir-kas kavşağı), HealthDay (domuz böbreği), NeurologyLive (AMT-130 başvurusu, tavapadon, oveporekston, PrevenTRON), USC (demans), CNIC (REACT), ASCO Post (daraksonrasib, INTerpath-001), Cambridge Kök Hücre Enst. (STEM-PD), TCTMD (enlisitid), NIHR UCLH BRC (CAR-T lupus), ScienceAlert (lakozamid), AuntMinnie (GAE), Hospital Healthcare Europe (kalsiyum-D), Drug Topics (baksdrostat), Radiology Business (ultra işlenmiş gıda), Patient Care (orforglipron), Medical Republic (OPTIMIZE), Live Science (OTOF), Nature Asia (BrainGate), SpinalCure (eWALK), Lund Üniv. (MASAI), News-Medical (yürüyüş eğitimi), MedCity News (zimislecel), Penn Medicine (KJ), EMA (Casgevy).
- Okurken bulunan ve DÜZELTİLEN hatalar: GAE haberinde "%80'inde anlamlı iyileşme" yanlıştı (KOOS alanlarına göre %55–80 eşik aşımı; %7 hafif yan etki eklendi). Casgevy sayıları (17'de 16, 27'de 25) doğrulanamadı → EMA'nın değerlendirdiği sayılarla değiştirildi (29'da 28; 42'de 39), hem haberde hem SSS'de. Trontinemab %92 → "yaklaşık %91–92" (NeurologyLive 49/54 veriyor) + PrevenTRON tasarımı (~1.600 kişi, 55–80 yaş, p-tau217), hem haberde hem SSS'de. Kalsiyum-D: birlikte kullanımda RR 0,91 istatistiksel olarak anlamlı ama mutlak fark %1 → "klinik açıdan anlamlı değil" diye netleştirildi. Domuz böbreği: "işlevini yitirdi" → "işlevini yitirmeye başladı" (HealthDay: pıhtı hasarı, yetmezliğe gidiyordu).
- Tutarsızlık notları (değiştirilmedi): VITAL JAMA'da 12 Ağustos'ta çevrim içi, 13 Ekim sayısında; NHS-Galleri katılımcı sayısı ASCO bülteninde 142.942, ecancer'da 142.924; kalsiyum-D derlemesinde D vitamini grubu BMJ bülteninde 92.045, Hospital Healthcare'de 92.415 kişi (bülten esas alındı). Oxford başlığı "üçte iki" diyor, çalışmadaki tanımlı oran %59 (sayfada %59 yazıyor).
- Betik: scratchpad'de r3/news_src.py (ADD sözlüğü il→(etiket, url) + TEXT düzeltmeleri; idempotent). Çeviri tur17 (48 birim): kaynak satırlarının eski İngilizcesi TR→EN eşlemesinden alınıp yeni bağlantı eklendi; değişen 7 metin elle çevrildi. Sonraki batch: tur18.
- Testler: t_ls sorun 0; yenilikler/index TR+EN 360/390/1366/1440 taşma yok.
- Sırada (öneri): 3 kaynaklı haberlerin bazılarına birincil makale bağlantısı (DOI) eksik olanlar (ör. FDA onay haberleri) için hakemli makale eklenebilir; ya da yeni ekleme turu.

## 24 Ekim 2026 — 4. tur (3 rehber, 2 araç, 3 haber) + KAYNAK TURU 5 (29 sayfa güçlendirildi)
Kullanıcı: "Bilgi köşesi, Bilim gündemi, Kendine iyi bak, ekleme yapmaya devam edelim, kaynakları güçlü ve fazla olsun, öncekilerinde de kaynak az varsa onları güçlendirip kaynak ekleyelim." Kayıt `reg_tur.py` ile (listeler bu turla DEĞİŞTİRİLDİ; sayfa listesi scratchpad r3/cfg_pages4.txt, haberler r3/cfg_news4.txt). Exec zinciri: … cond69 → self14 → cond70 → cond71 → cond72 → self15 → nobel.
- cond70 kosucu-dizi.html → en/iliotibial-band-syndrome.html (it_abd, it_side, it_bridge, it_sls, it_wall, it_walk). 8 kaynak: van der Worp 2012, Aderem 2015, Fairclough 2006, Fredericson 2000, Sanchez-Alvarado 2024, Gunter 2004 BJSM 38(3):269–272 (son sayfa hafızadan), Nielsen 2014, Bupa.
- cond71 uzun-covid.html → en/long-covid.html (lc_breath, lc_plb, lc_lean, lc_sts, lc_push, lc_walk). 7 kaynak: DSÖ post-COVID, NICE NG188 (25 Oca 2024), World Physiotherapy BP9 (efor sonrası kötüleşme), Berry 2025 JAMA Netw Open 8(11):e2534304 (2025, yorgunluğa etkisi yok), Glasgow bülteni, REGAIN BMJ 2024;384:e076506, DSÖ Avrupa broşürü.
- cond72 zayiflama-ilaci-ve-kas.html → en/weight-loss-medication-and-muscle.html (gl_sts, gl_push, gl_row, gl_bridge, gl_heel, gl_walk). 10 kaynak: DSÖ GLP-1 kılavuzu (1 Ara 2025), Mozaffarian 2025 AJCN 122:344–367, Wilding STEP 1 DXA alt çalışması (bildiri özeti, Newswise — makale başlığı uydurulmasın diye betimleyici etiket), Wilding 2022 DOM 24(8):1553–1564, Lundgren 2021 NEJM 384(18):1719–1730, D'Souza 2022 BJSM 56(13):771, Villareal 2017 NEJM 376(20):1943–1955 (26 hafta), LEAN-PREP BMJ Open 2026;16:e116911, Bull 2020, Patient Care orforglipron.
- self15_part.py (SELF15_CSS = SELF14_CSS + is-/ah- sınıfları; yeni çizimler SV["plank"], SV["squat"]):
  sakatlanmayi-onleyen-isinma.html → en/injury-prevention-warm-up.html (FIFA 11+ temelli 15 hareket is_run…is_cut; IS_PLAN segment motoru; tam 1.250 sn, maç modu 600 sn = 1. ve 3. bölüm; haftalık hedef ≥2; drihsaneren.isinma.v1; kanca window.__is {st, skip, total}). Kaynaklar: Thorborg 2017 BJSM 51(7):562–571, Soligard 2008 BMJ 337:a2469 (PEDro), van Dyk 2019 BJSM 53(21):1362–1370, WakeMed PDF, Physiopedia, FIFA 11+ Referee PDF.
  adim-hedefi.html → en/step-goal-planner.html (metin girişi — type=number "4.250"yi reddediyordu; yaş <60/60+; haftada +1.000 ile 7.000'e, sonra 8.000 (<60) ya da 6.000 (60+); koruma hedefi Math.round(a/100)*100; son 8 hafta çubukları, ≥7.000 "hit"; drihsaneren.adimhedefi.v1; kanca window.__ah {st}). Kaynaklar: Ding 2025 (Epocrates), Paluch 2022 Lancet PH 7(3):e219–e228 (cilt/sayfa hafızadan), Banach 2023 EJPC zwad229 (yazarlar hafızadan), Ekelund 2026 Lancet 407(10526):339–349, Bull 2020.
- Haberler: IL_LBPG (AAPM akut bel ağrısı kılavuzu, 5 Eki 2026; Pain Med doi 10.1093/pm/pnag131 + Managed Healthcare Executive + MSSNY), IL_RRAD (JAMA Neurol 2026, 513 kişi; PBRC + EMJ), IL_SMALL (Ekelund Lancet; doi 10.1016/S0140-6736(25)02219-6 + EurekAlert + KI + SMC İspanya).
- KAYNAK TURU 5: 5 kaynaklı 96 sayfadan 29'una okunmuş birer güçlü kaynak (çoğu RKÇ, Cochrane ya da kılavuz) + ilgili SSS'ye bir cümle + "Son güncelleme: 24 Ekim 2026". Betikler scratchpad kt/batch_a.py (15 sayfa) ve kt/batch_b.py (14 sayfa); srcedit.py'ye bump(part, sayfa.html) eklendi (yayımlanmış h1'i part dosyasında bulup tarihi günceller).
  batch A: demans (rrAD Zhang 2026 + Feter 2026/USC), sarkopeni (SPAF/KI), hareket ve masa başı (Ekelund 2026), uyku (Luo PLOS Med 2026/Healio), tempolu yürüyüş (Ding 2025), duvar oturuşu (BMJ OSEM 2026 izometrik sıklık), düşme riski testi (eSTEPS/UTMB), ayak bileği (Thorborg 2017, %32), kalça kireçlenmesi (Schleimer RMD Open 2026), menisküs (TeMPO, Katz NEJM 2025/MGB), Parkinson (Ryu Neurology 2026/Healio), kanser-egzersiz (BJSM 2026 meta-analiz/BMJ Group), kemik erimesi (Massé BMJ 2026;393:e088050), bel fıtığı (AAPM 2026).
  batch B: kalp rehabilitasyonu (Krishnamurthi 2023 JAHA, ev temelli, gözlemsel), KOAH (Cox 2021 Cochrane telerehabilitasyon), kalça kırığı (Magaziner 2019 CAP JAMA 322(10):946–956), protez sonrası (Buhagiar 2017 HIHO JAMA 317(10):1037–1046), rotator manşet (Karjalainen 2019 Cochrane CD013502), idrar kaçırma (Dumoulin 2020 JAMA Intern Med 180(10):1284–1293), diyabetik nöropati (IWGDF 2023, Bus SA, DMRR 2024;40(3):e3651), omuz çıkığı (Kavaja 2018 BJSM 52(23):1498 — son sayfa yazılmadı), köprücük (Ahrens 2017 JBJS 99(16):1345–1354), Aşil kopması (UKSTAR Lancet 2020;395(10222):441–448), omuzda kireç (de Witte 2013 AJSM 41(7):1665–1673), bel fıtığı ameliyatı sonrası (Carragee 1999 Spine 24(22):2346–2351, karşılaştırmasız), Aşil tendinopatisi (Silbernagel 2007 AJSM 35(6):897–906), tenisçi dirseği (Bisset 2006 BMJ 333(7575):939).
  Dikkat: ilk seçilen bazı kaynaklar (Dumoulin 2018 Cochrane, Bhattacharyya 2017, EULAR 2018 RA, ASAS-EULAR 2022, Delitto 2015, SOSORT 2016, AASM RLS, Coombes 2013, Beyer 2015) sayfalarda ZATEN vardı; o sayfalara bu turda dokunulmadı. Yeni kaynak eklemeden önce pinfo.py ile mevcut URL'lere bakın.
  Hafızadan/doğrulanamayan künye ayrıntıları: Gunter son sayfa, Paluch cilt/sayfa, Banach yazar listesi, Feter makale başlığı (Türkçe betimleme olarak yazıldı), Bus SA dışındaki IWGDF yazarları yazılmadı.
- Çeviri: tur18 (372 birim, 4. tur sayfaları), tur19 (43 birim: Wilding etiketi + 29 sayfanın değişen SSS/kaynak satırları; eski İngilizce TR→EN eşlemesinden alınıp yeni cümle eklendi). check.py 0 sorun, make_en toplam eksik 0. Sonraki batch: tur20.
- Testler: t_ls sorun 0; 4. tur sayfaları ve değişen 29 sayfa TR+EN (60 sayfa) 360/390/1366/1440'ta taşma yok; iki araç TR+EN baştan sona çalıştırıldı (t_tools15.py, t_ah.py), sayfa hatası yok.
- Sırada (öneri): 5 kaynaklı kalan 67 sayfa (çoğu NHS broşürü ağırlıklı: el bileği kırığı, boyun incinmesi, baş dönmesi, skolyoz, huzursuz bacak vb.) aynı yöntemle güçlendirilebilir; ya da yeni ekleme turu.

## 24 Ekim 2026 öğleden sonra — KAYNAK TURU 6 (11 sayfa) + 3 haber
Kullanıcı: "Haftalık limite göre bir şeyler daha ekleyebilirsin." Hasta broşürü (NHS) ağırlıklı 5 kaynaklı sayfalara okunmuş birer güçlü kaynak + SSS'ye bir cümle + tarih (scratchpad kt/batch_c.py): kasık zorlanması (Harøy 2019 BJSM 53(3):150–157, Kopenhag addüksiyon, %41), baldır (Bayer 2017 NEJM 377(13):1300–1301 mektup; erken yüklenme ~3 hafta daha erken ağrısız — katılımcı sayısı ve yazar listesi yazılmadı), Sever (Wiegerinck 2016 J Pediatr Orthop 36(2):152–157; çalışma sayfada zaten anlatılıyordu, birincil kaynak + 6. hafta memnuniyeti eklendi), boyun incinmesi (Michaleff 2014 PROMISE Lancet 384(9938):133–141), omuz kireçlenmesi (Craig 2020 Cochrane CD012879), kalça sıkışması (Palmer 2019 UK FAIT BMJ 364:l185), huzursuz bacak (Allen 2018 IRLSSG Sleep Med 41:27–44; ferritin ≤75 / <300), bel kayması (Austevoll 2021 NORDSTEN-DS NEJM 385(6):526–538; 262 hasta mITT), kalk-yürü testi (Barry 2014 BMC Geriatr 14:14; duyarlılık %31), çekiç parmak (O'Brien 2011 Arch Phys Med Rehabil 92(2):191–198), diz kapağı çıkığı (Moiz 2018 OJSM 6(6); %31).
- Bu turda bakılıp dokunulmayanlar: kübital tünel (Caliandro Cochrane bulgusu sayfada zaten var), boyun incinmesinde MINT (PEDro 35109 zaten MINT), el bileği kırığı (C vitamini kanıtı çelişkili; Ekrol RKÇ'nin dergi künyesi doğrulanamadı).
- Haberler (scratchpad r5/news5.py; IL_COGENG/IL_CADENCE/IL_PREHAB çizimleri): Egzersiz + sosyal-zihinsel katılım ve bilişsel bozulmasız yıllar (Alzheimer's & Dementia 2026, doi 10.1002/alz.71854; ayrıntılar yalnızca Çince eBiotrade özetinden, Medscape ve Wiley sayfaları açılamadı — sayılar HR 0,80/0,79/0,70; 17,5 vs 24,7 yıl), adım temposu (Wei, BJSM Eylül 2026, doi 10.1136/bjsports-2025-111173; News-Medical 103.684, ScienceAlert "64 binden fazla" diyor → sayfada sayı yazılmadı), PREPARE (McIsaac, JAMA Surg 2026;161(2):113–123, 3 Ara 2025 çevrim içi; OHRI + HealthDay — HealthDay başlığı keşif amaçlı analize dayanıyor, haberde açıklandı). NEWS_FAQ'a "Günde 10.000 adım atmak şart mı?" eklendi.
- Çeviri tur20 (27 birim), check 0 sorun, make_en eksik 0. Sonraki batch: tur21.
- Testler: t_ls sorun 0; değişen 11 sayfa + yenilikler/index/bilgi TR+EN 360/390/1366/1440'ta taşma yok. Yerel sunucu konteyner yeniden başlayınca kapanıyor: `cd /home/claude/main && python3 -m http.server 8765 --bind 127.0.0.1`.
- Sırada: 5 kaynaklı kalan ~57 sayfa (kübital tünel, golfçü dirseği, kürek kemiği arası, boyun tutulması, omuz ucu, 5. metatars, bebeklerde tortikolis, büyüme ağrıları, el bileği kırığı…).

## 25 Ekim 2026 — HİZMET YERİ GEÇİCİ OLARAK KÜTAHYA MERKEZ
Kullanıcı şu an Kütahya'da (belki Mayıs–Haziran 2027'ye kadar). İsteği: İstanbul etiketini kaldırıp hem sitede hem Google İşletme Profili'nde Kütahya yapmak. Seçimleri: hizmet alanı yalnızca "Kütahya merkez", sitede İstanbul hiç geçmesin (dönüşte geri çevrilecek).
- Değişen kaynaklar: site/index.bak_fb.html (title, description, hero "where", intro, iletişim cümlesi), fb_misc.py, fb_trim.py, to_github.py (og/twitter), schema_home.json (description, PostalAddress Kütahya, areaServed City @id #kutahya, geo 39.4167/29.9833). Çeviri tur21 (8 birim; check.py'nin "Türkçe karakter" uyarıları yalnızca "Kütahya" adından). Sonraki batch: tur22.
- İstanbul'a dönüşte geri almak için: bu dosyalarda "Kütahya merkezde" → "İstanbul içinde", "Kütahya merkezde evde fizyoterapi:" → "İstanbul'da evde fizyoterapi:", title/hero "Kütahya" → "İstanbul", schema'yı git geçmişinden (24 Ekim sürümü) geri yükleyin; EN eşleri bellekte duruyor.
- Dokunulmadı: doga-recetesi.html'deki "İstanbul'dan öneriler / İstanbul'da doğa" bölümü (içerik sayfası; istenirse Kütahya önerileri eklenebilir) ve bilgi.html'deki kart cümlesi.
- Google İşletme Profili kullanıcıda; erişimimiz yok. Önerilen yol: mevcut (aktif olmayan) İstanbul profilini düzenleyip adres gizli hizmet bölgesi işletmesi olarak Kütahya adresine ve "Kütahya" hizmet alanına çevirmek (yeniden doğrulama, çoğunlukla video ile, beklenir); ikinci bir profil açmamak.

## 26 Ekim 2026 — ANA SAYFADA ŞEHİR ADI YOK
Kullanıcı: "Kütahya evde fizyoterapi hizmeti yazma", ardından seçim: "Evde fizyoterapi, konumsuz". Ana sayfada (TR+EN) hiçbir şehir adı geçmiyor: başlık "İhsan Eren · Evde Fizyoterapi", hero "Evde fizyoterapi hizmeti", intro "Evinize geliyorum; …", iletişim "… Evde fizyoterapi hizmeti.", og/twitter "Evde fizyoterapi: …". Şemada (schema_home.json) areaServed kaldırıldı, adres yalnızca addressCountry TR, occupationLocation Country "Türkiye". Çeviri tur22 (7 birim). Sonraki batch: tur23.
- Kural: kullanıcı açıkça istemedikçe ana sayfaya şehir adı (İstanbul/Kütahya) yazılmaz. Doğa reçetesi sayfasındaki İstanbul önerileri içerik olarak duruyor.
- Bir önceki bölümdeki "geri alma" notu artık geçersiz; şehir eklenecekse yukarıdaki dosyalar düzenlenir.

## 27 Ekim 2026 — İLAÇ ÖNERİSİ CÜMLELERİ KALDIRILDI (16 sayfa)
Kullanıcı piriformis sayfasındaki "Parasetamol ya da ibuprofen gibi bir ilacı prospektüse uygun şekilde kullanabilirsiniz" cümlesinin etik olup olmadığını sordu (sakroiliak sanmıştı; cümle piriformis-sendromu'ndaydı). İlaç önermek fizyoterapistin görev alanı dışında ve 2025 yönetmeliği yalnızca hekimin tedavi planındaki işlemlere izin veriyor; ayrıca bazı cümleler kanıta da uymuyordu (ör. parasetamol şişliği azaltmaz).
- KURAL: Sitede okura belirli bir ilacı (parasetamol, ibuprofen vb.) kullanmasını söyleyen ya da doz/prospektüs yönlendiren cümle yazılmaz. Kalıp: "Ağrı kesici kullanmanız gerekiyorsa hangisinin size uygun olduğunu hekiminize sorun." (27 Ekim öğlen: eczacı ifadesi de kaldırıldı, aşağıya bakın) Kılavuzların ne dediğini aktarmak (ör. "kılavuz opioidle başlanmamasını öneriyor") serbest; kararın hekimde olduğu belirtilir.
- Değişen sayfalar (tarih 27 Ekim 2026): arka uyluk, Baker kisti, 5. metatars, beyin sarsıntısı (HSE kaynağı eklendi: baş yaralanmasından sonra ibuprofen/aspirin yerine parasetamol; NHS 111 Wales ikisini de sayıyor), boyun tutulması (2 yer), büyüme ağrıları (çocuk dozu → hekim/eczacı; 16 yaş altı aspirin uyarısı kaldı), el bileği kırığı, ganglion, gece krampları, kalça sıkışması, kambur duruş, kaval kemiği, Morton, omuz çıkığı, omuz ucu, piriformis. Betik: scratchpad kt/batch_ilac.py. Çeviri tur23 (18 birim). Sonraki batch: tur24.
- Kalan ilaç adları yalnızca bilgilendirme: agriyi-anlamak (NICE: kronik birincil ağrıda parasetamol/NSAİİ/opioidle başlanmaması), beyin-sarsintisi (HSE uyarısı), yenilikler (haberler).

## 27 Ekim 2026 öğlen — "ECZACINIZA" İFADESİ KALDIRILDI
Kullanıcı: "DOKTORUNUZA olmalı, eczacıya danışılır mı". Sitedeki tüm "hekiminize ya da eczacınıza", "eczacınıza danışın", "hekiminizle ya da eczacınızla" vb. ifadeler yalnızca "hekiminize/hekiminizle" yapıldı (36 sayfa, 35 part dosyası; ilaç dışı bağlamlar da dahil: KOAH inhaler tekniği, düşme riski ilaç gözden geçirme, sürekli üşüme bitkisel ürün, kuyruk sokumu kabızlık). Sitede "eczac" ve İngilizcede "pharmacist" kalmadı.
- KURAL: Okuru eczacıya yönlendiren ifade yazılmaz; yalnızca "hekiminize" (sitede "doktor" yerine "hekim" kullanılıyor: ~175 kez "hekiminize"). Kullanıcı "doktor" kelimesini isterse ayrıca sorulmalı.
- Betik: tools_eczaci_hekim.py (TR kalıpları + EN "doctor or pharmacist" → "doctor"; TR→EN eşlemesini bellekten üretip tur24'e yazdı). Çeviri tur24 (39 birim). Sonraki batch: tur25.

## 28 Ekim 2026 — SKOLYOZ REHBERİ BAŞTAN GENİŞLETİLDİ
Kullanıcı skolyoz sayfasını yetersiz buldu; istedikleri: C/S eğrilik, röntgen ve Cobb açısı (kısa anlatım + "ayrıntılı bilgi" bağlantıları), büyüme dönemi (12–18 yaş civarı), tek taraflı çanta/eşya, duruş bozukluğu ve benign eklem hipermobilitesinin etkisi (araştırma ile klinik deneyim AYRI gösterilerek), geçmişten bugüne tedaviler ve karşılaştırma, yüksek dereceli ama kompanse eğrilikte ameliyatın önerilmeyebilmesi, çizimler, egzersizlerin kişiye özel olması ve iki tarafı eşit çalıştıran egzersizlerin ağrı yoksa güvenli olabileceğinin açıkça yazılması.
- cond3_part.py: SC_FAQ (9 soru), SC_SRC (21 kaynak), SC_CSS (= NECK_CSS + sk-*), SK_CLIN() kutusu ("Klinik deneyimden" + "araştırma sonucu değil" notu), Python ile üretilen SVG çizimler: SK_SPINE("N"/"C"/"S"), SK_COBB() (uç omurlar, kesişen çizgiler, açı yayı), SK_ADAMS(), SK_RISSER(), SK_BALANCE(True/False) (çekül çizgisi). Çizimlerde yazı yok (yalnızca Risser'de 1–4 rakamları); açıklamalar figcaption'da. Sayfada "gerçek röntgen değildir" notu var. sc_side metni "iki tarafa eşit" olarak güncellendi. Bilgi köşesi kart metni (C_SCOLIOSIS) yenilendi.
- Bölümler: içindekiler, nedir/duruş farkı, C ve S, Cobb + ölçüm payı + SRS derece eşikleri, öne eğilme testi ve Risser, türler, büyüme (Lonstein&Carlson 727 çocuk %23; Risser 0–1 %68 / 2–4 %23 — Haines/Virginia Spine ikincil kaynağı; Little 2000 %83/%4, 3,6 yıl), çanta/alışkanlık/esneklik (SRS, Minghelli 2016, Czaprowski 2011 %51,4/%19, Tanchev 2000 %12/%1,1 "tehlikeli üçlü" + klinik deneyim kutusu + çanta önerileri AAP %10–15), tarihçe (SRS zaman çizelgesi; Hipokrat ve Schroth 1921 Moramarco 2017; elektrik uyarımı NSF 1993 raporu; VBT 2019), yöntem kartları (izlem, PSSE, gece korsesi, tam gün korse, füzyon, VBT), PSSE (7 okul Berdishevsky 2016; Kuru 2016; Cochrane 2024; CONTRAIS 2024) + klinik kutu, korse, ameliyat/denge (radiopaedia eşikleri; Weinstein 2003; Dragsted 2025) + klinik kutu + denge çizimi, egzersizler (kişiye özel uyarısı; iki taraflı genel egzersizler ağrı yoksa genellikle güvenli), yetişkin, spor, SSS, kırmızı bayraklar.
- Hafızadan künye: Lonstein & Carlson 66(7):1061–1071; Little DG ve ark. 82(5):685–693; Tanchev yazar listesi; Czaprowski yazar listesi; Weinstein 2003 yazar listesi (AAFP özetinde 289:559-67).
- Çeviri tur25 (159 birim; check'in tek uyarısı "Türkiye") + tur26 (kart metni). Sonraki batch: tur27.
- Testler: TR+EN 360/390/1366/1440 taşma yok, 360'ta öğe taşması yok, t_ls sorun 0, JSON-LD geçerli; çizimler ekran görüntüsüyle kontrol edildi (scratchpad sk/shot.py).

## 28 Ekim 2026 — "eklem esnekliği" → "bağ dokusu esnekliği"
Kullanıcı: "eklem esnekliği ifadesi Türkçede ne kadar doğru, bağ doku esnekliği demek daha doğru değil mi". Kural: altta yatan özellik için "bağ dokusu esnekliği / gevşekliği", tıbbi bulgu için "eklem hipermobilitesi", ölçülen şey için "eklem hareketliliği" yazılır; "eklem esnekliği" kullanılmaz (TDK yazımı "bağ dokusu"). Değişenler: skolyoz (başlık, açıklama, SSS, Czaprowski cümlesi, öneri maddesi), bilgi köşesi skolyoz kartı, eklem hipermobilitesi (Beighton cümlesi), büyüme ağrıları SSS. Çalışmaların kendi terimi olan "eklem gevşekliği" (Tanchev "generalized joint laxity") yerinde bırakıldı. Çeviri tur27 (8 birim; EN "connective tissue flexibility/laxity", "joint mobility"). Sonraki batch: tur28.

## 28 Ekim 2026 sabah — skolyoz giriş metni düzeltildi
Kullanıcı: "ilk skolyoz açılınca büyümenin önemi yazıyor, nasıl böyle bir hata yapabilirsin". Giriş paragrafındaki belirsiz "büyümenin önemini" ifadesi, sayfa açıklaması ve bilgi köşesi kartındaki "büyüme döneminin önemi" kaldırıldı; yerine "eğrilik en çok ergenlikteki hızlı boy uzaması döneminde ilerlediği için…", "boy uzaması döneminde ilerleme riski" yazıldı. Bölüm başlığı "Eğrilik ne zaman ilerler?", içindekiler bağlantısı "İlerleme riski". Kullanıcının kastettiği hata farklıysa sorulacak. Çeviri tur28 (5 birim). Sonraki batch: tur29.

## 28 Ekim 2026 — "BU SAYFADA" + "GEÇMİŞTEN BUGÜNE" (1. parti: bel fıtığı, diz kireçlenmesi, donuk omuz)
Kullanıcı: "o tarihi çizelgeleri çok seviyorum hastanın anlaması açısından, bir de 'bu sayfada' yazarak altında keywordlerin olduğu yeri, bu iki yeri tüm hastalıklara ekleyelim, 3-5 hastalık olarak başlayıp". Yavaş yavaş, partiler halinde devam edilecek.
- Ortak yapı (build_pages.py, pick()'in altında): G_CSS (.g-toc yuvarlak bağlantılar, .g-tl zaman çizelgesi, section[id] scroll-margin), g_toc([(id, etiket), ...]) ve g_tl([(yıl, metin), ...]). page() gövdede g-toc/g-tl görürse G_CSS'i kendisi ekler. Skolyoz kendi sk-toc/sk-tl sınıflarıyla duruyor (aynı görünüm).
- Yerleşim: g_toc istatistik kutularının hemen altına (ilk .stats kapanışından sonra); tarihçe bölümü (id="tarihce", eyebrow "Geçmişten bugüne", h2 "... kısa tarihi") tedavi bölümünden hemen önce. Bölümlere id: nedir, tani/rontgen/evreler/sinirler, tarihce, tedavi, egzersizler, videolar, sss, uyari. Sabit çubuk altında başlık örtülmüyor (test edildi).
- Her tarihçe satırı kaynaklı; yeni kaynaklar sayfa kaynak listesine eklendi:
  - Bel fıtığı: Cotugno 1764, Lasègue 1864, Mixter&Barr 1934, Yaşargil&Caspar 1977 (Gusmão 2016 Springer bölümü), Weber 1983 (PEDro 2195), Deyo 1986 (203 kişi, 2 gün = 7 gün, %45 daha az iş günü kaybı), Peul 2007, Chiu+Brinjikji 2015, AAPM 2026.
  - Diz: 1890'lar fildişi menteşe ve 1974 total kondiler (Patel 2019 Bone Joint 360), Moseley 2002 (180, sahte ameliyat), Kirkley 2008 (178), GLA:D 2013 (Skou&Roos 2017: 3 eğitim + 12 egzersiz, 9.825 kişi, 3. ayda −12,4/100, kontrol grubu yok), Skou 2015 NEJM (100 hasta; ciddi yan etki 24/6; ameliyatsız grubun %26'sı 1 yılda protez), NICE NG226 2022.
  - Donuk omuz: Duplay 1872, Codman 1934, Neviaser 1945 (D'Orsi 2012), Reeves 1975 (41 hasta), Bunker&Anthony 1995 (Dupuytren benzeri; dupuytren-kontrakturu.html bağlantısı), Wong 2017 (7 çalışma; tam kendiliğinden düzelme kanıtı yok), UK FROST 2020 (503 kişi).
- Düzeltmeler: diz sayfasındaki "artroskopik yıkama… (kilitlenme gibi özel durumlar dışında)" — NICE NG226 1.7.1'de istisna yok, parantez kaldırıldı. Donuk omuz girişi "Çoğu zaman zamanla düzelir… bazı kişilerde bir miktar kısıtlılık kalabilir" (Wong 2017 ile uyumlu).
- Betikler: scratchpad g1/gx.py (sec_id, insert_before_section, toc_after_stats), g1/g1.py, g1/tr29.py, g1/shots.py. Çeviri tur29 (37 birim). Sonraki batch: tur30.
- Sıradaki aday parti: boyun fıtığı, bel ağrısı, omuz sıkışması, kalça kireçlenmesi, karpal tünel (kullanıcıya önerildi).

## 28 Ekim 2026 — skolyoz: "tek taraflı alışkanlıklar" netleştirildi
Kullanıcı: "tek taraflı çanta takmak, tek taraflı alışkanlıklar anlamında demiştim; mesela okul çağında bir yere dayanarak oturmak". Bölüm (id="risk") başlığı "Tek taraflı alışkanlıklar ve bağ dokusu esnekliği" oldu; girişte okul çağı örnekleri listesi (sırada aynı yana/duvara/dirseğe dayanmak, hep aynı kalçaya yüklenmek, yazarken omzu düşürmek, sınıfta hep aynı yerde oturup tahtaya aynı yöne dönmek, ayakta tek bacağa yüklenmek, çanta/çalgı tek tarafta). Araştırmalara iki Çin okul taraması çalışması eklendi: Yang 2022 J Orthop Surg Res 17:472 (2.538 öğrenci vaka-kontrol; dik oturma aOR 0,69, sınıfta yer değiştirme 0,72, okul sırası çok alçak 1,40; yana yaslanma anlamlı değil; beyan + röntgensiz) ve Xu 2025 Front Pediatr 13:1524073 (90.635 tarama, röntgenli 1.458; tek tarafa yaslanma aOR 2,13, sıraya kapanma 1,52; çanta ilişkisiz; kesitsel, ters yön mümkün) + "Özetle" cümlesi. Klinik deneyim kutusu ve SSS (soru: "Tek taraflı alışkanlıklar, ağır çanta ya da kötü duruş skolyoza yol açar mı?") oturma örnekleriyle güncellendi; önerilere oturma, sıra-sandalye yüksekliği, sınıfta yer değiştirme eklendi. İçindekiler: "Tek taraflı alışkanlıklar"; sayfa açıklaması ve bilgi köşesi kartı güncellendi. Betik: scratchpad g1/sk_habit.py. Çeviri tur30 (20 birim). Sonraki batch: tur31.

## 28 Ekim 2026 — kalite kontrol kuralı + donuk omuz tarihçesinde iki düzeltme
Kullanıcı daha fazla titizlik istedi; başa "İÇERİK KALİTE KONTROLÜ" listesi eklendi. Bu kurala göre bugünkü tarihçeler yeniden gözden geçirildi: "Julius Neviaser" adındaki ilk ad kaynakta doğrulanamadığı için "Neviaser" yapıldı; Reeves 1975 satırı ikincil kaynak (IASP) yerine dergi özetinden (Scand J Rheumatol 4(4):193–196: 49 hasta, 41'i 5–10 yıl izlendi, ağrı-katılaşma-düzelme evreleri, ortalama 30,1 ay, en iyi düzelmeden sonra yarıdan fazlasında hafif kısıtlılık, 3'ünde işlevsel kayıp) yeniden yazıldı. Duplay (Fransız cerrah, 1836–1924; 1872 makalesi) doğrulandı. Çeviri tur31 (2 birim). Sonraki batch: tur32.

## 28 Ekim 2026 öğle — skolyoz denetimi düzeltmeleri (tur32, tur33), stres sayfasında "doktorunuza" → "hekiminize" (tur34)
Ayrıntılar DENETIM.md'de. Günlük zamanlanmış denetim kuruldu (her gün 06:39 İstanbul, 3 sayfa). Sonraki batch: tur35.

## 28 Ekim 2026 — stres: nefes çemberine dokunmak da başlatır
Kullanıcı: "şu yuvarlağın ortasına tıklayınca da başlasın". #orb tıklaması yalnızca dururken Başlat ile aynı işi yapar (çalışırken dokunmak bir şey yapmaz; durdurma yine "Durdur" düğmesiyle). Bekleme yazısı "Başlat'a basın" → "Başlamak için dokunun" (EN "Tap to begin"; i18n/manual_stres.py ve i18n/js.json güncellendi), boşta imleç el. Çeviri tur35. Sonraki batch: tur36.

## 29 Ekim 2026 — günlük denetim (bel fıtığı, bel ağrısı, boyun fıtığı)
Ayrıntılar DENETIM.md'de. Önemli: NICE NG59 29 Temmuz 2026'da BDT/psikolojik terapi önerilerini (1.2.13, 1.2.14) kaldırdı; sitede NICE'a dayanarak BDT öneren başka cümle varsa (ör. fibromiyalji dışı bel/siyatik sayfaları) ilgili denetimde düzeltilmeli. SRC_NICE59 künyesi "2016, güncelleme 2020 ve 2026". Çeviri tur36. Sonraki batch: tur37.

## 30 Ekim 2026 — günlük denetim (diz kireçlenmesi, donuk omuz, inme rehabilitasyonu)
Ayrıntılar DENETIM.md'de. İnme sayfasının tarihi artık sabit metin ("30 Ekim 2026"; önceden build_pages.UPDATED). Yeni oturumda `pip install qrcode --break-system-packages` gerekiyor (yoksa rb.sh sessizce yayımlamıyor: publish.sh "hero nav bulunamadı"). Çeviri tur37. Sonraki batch: tur38.

## 30–31 Ekim 2026 — rehber genişletme başladı (bel ağrısı, boyun ağrısı)
Kullanıcı seçimi: en sık şikâyetlerden başla; klinik deneyim kutusu yok (yalnızca araştırma); oturum başına 2–3 sayfa; her genişletilmiş sayfa YAYINDAN ÖNCE bağımsız denetimden geçer. Yeni ortak CSS: G_CSS'e .g-cmp (karşılaştırma kartları, dl/dt/dd), .g-facts (numaralı bilgi kartları), .g-h3. Ayrıntılar ve açık kalanlar DENETIM.md'de. Önerilen sıradaki parti: omuz sıkışması, kalça kireçlenmesi, karpal tünel sendromu. Çeviri tur38. Sonraki batch: tur39.

## 31 Ekim 2026 — günlük denetim (beyin sarsıntısı, kalp rehabilitasyonu, kalp yetmezliği)
Ayrıntılar DENETIM.md'de. Önemli: cochrane.org/evidence/<CD> sayfalarında sade özet güncellenmiş olsa da "Abstract" bölümü eski sürüm kalabiliyor (CD001800'de 2021 metni duruyordu) — güncel sayıları yayıncı/depo kopyasından (ör. eprints.gla.ac.uk) doğrulayın. Çeviri tur39 + tur40. Sonraki batch: tur41.

31 Ekim 2026 (öğleden önce): genişletme partisi 2 — omuz sıkışması, kalça kireçlenmesi, karpal tünel sendromu (içindekiler, tanı bölümleri, tarihçe, iki kılavuz karşılaştırma kartları, yeni SSS); her sayfa yayından önce ayrı bağımsız denetçiden geçti, bulgular kaynağından doğrulanıp düzeltildi. Ortak EXT değişti: scaption (kürek kemiği düzlemi tarifi), isoer (el sırtı), row (bant kapı arasına), mglide (kaydırıcı: baş aynı tarafa; çizim de) — rotator manşet, omuz çıkığı, ganglion vb. sayfalar da etkilendi. Ayrıntılar DENETIM.md'de. Önerilen sıradaki parti: tenisçi dirseği, topuk dikeni (plantar fasiit), ayak bileği burkulması. Çeviri tur41. Sonraki batch: tur42.
