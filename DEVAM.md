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
  Ana sayfa girişindeki üç kapı (`.trio`: Bilgi köşesi, Kendine iyi bak, Bilim gündemi) `_home_trio.txt` ile `splice_home.py` tarafından eklenir. Telefonda yana kayan menü yok: giriş bölümündeki kısayollar iki sütun (`fb_hero.py`), kategori çubuğu 2×2 (≤1040 px). Ana sayfanın bilgi köşesi stilleri de `HOME_CSS`'ten gelir (`splice_home.py` bölümü ve stili birlikte değiştirir).
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
