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
Sonra `$REPO` içinde commit + push (main). Araçlarda değişiklik yaptıysan bu dalı da commit + push et.

## Ne nerede

- **Ana sayfa**: `site/index.bak_fb.html` (taban) üzerine sırayla `fb_hero.py` (giriş, üst çubuk),
  `fb_misc.py` (iletişim, galeri, hızlı test), `fb_report.py` (analiz raporu slaytları),
  `fb_book.py` (ücretsiz ön görüşme; Google takvim gelince `data-embed`), `fb_day.py` (Günlük Hareket
  Skalası), `fb_lx.py` (Longevity başı), `fb_trim.py` (kısaltmalar), `fb_qr.py` (nöron karekod),
  `fb_reg.py` (®). Sıra `rebuild_home.sh` içinde. `to_github.py` + `splice_home.py` yayın biçimine çevirir.
- **Konu sayfaları**: `build_pages.py` + `*_part.py` (page(), KC kartları, NEWS listesi, CTA_CARD, bar()).
- **Örnek reçete**: `recete.orig.html` + `fb_recete.py`.
- **İngilizce**: `make_en.py`, `i18n_map.py` (adresler), `i18n/todo|done/*.json` (TR -> EN bellek).
  Yeni/değişen metinler `i18n/todo/fb1.json` + `i18n/done/fb1.json`'a yeni kimlikle eklenir
  (`python3 i18n/check.py fb1` ile doğrula). Betik içi metinler `i18n/js.json`. Var olan todo dosyalarını yeniden dışa aktarma.
- **Arama**: `ara.js`, `search_ui.py`, `search_index.py`.
- **Sınama**: `./srv.sh python3 t_xxx.py` (yerel sunucu + Playwright). Örn. `t_fb.py`, `t_gh.py`,
  `t_bk2.py`, `t_nq3.py` (karekod her karede okunuyor mu), `t_st2.py` (karekod dayanıklılık), `t_rec.py`.

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

- Google Takvim "Appointment schedule" yerleştirme kodu gelince `fb_book.py` içindeki `data-embed=""` doldurulacak (30 dk).
- Armut.com yorumları (profil bağlantısı bekleniyor). Gerçek fotoğraflar (özellikle iğneleme karesi yerine).
- LinkedIn için 1200×627 paylaşım görseli önerildi.
- Arkadaşının "PC'de düzgün açılmıyor" bildirimi tekrarlanamadı (tarayıcı bilgisi bekleniyor).
