# drihsaneren.com — kaynak dosyaları (bu dal siteyi ETKİLEMEZ)

Site `main` dalından yayınlanır (GitHub Pages, drihsaneren.com). Bu `kaynak` dalı,
`main`'deki hazır sayfaları üreten araçları saklar. Yeni bir oturumda buradan devam edilir.

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
