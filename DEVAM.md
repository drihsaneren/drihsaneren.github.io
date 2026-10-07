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
