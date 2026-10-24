# -*- coding: utf-8 -*-
"""Builds the Bilgi köşesi pages in two flavours:
   mode="artifact": Google Fonts, images under img/
   mode="github":   self-hosted fonts, images at repo root
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fab_part import FAB_CSS, fab_html
from urllib.parse import quote
from i18n_map import LANG_CSS, switcher, hreflang
from search_ui import SEARCH_BTN, SEARCH_CSS, SEARCH_TAG, search_field

MODE = sys.argv[1]
OUT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)
IMG = "img/" if MODE == "artifact" else ""
WA = "https://wa.me/905538815568?text=" + quote("Merhaba, evde fizyoterapi için seans planlamak istiyorum.")
UPDATED = "28 Eylül 2026"

# ------------------------------------------------------------------ SSS + yapısal veri
import json as _json, re as _re, html as _html
FAQ_CSS = """
  .faq{max-width:820px;border-top:1px solid var(--line);margin-top:8px}
  .faq details{border-bottom:1px solid var(--line)}
  .faq summary{cursor:pointer;list-style:none;padding:16px 40px 16px 0;position:relative;font-family:var(--display);font-size:20px;line-height:1.3}
  .faq summary::-webkit-details-marker{display:none}
  .faq summary::after{content:"+";position:absolute;right:6px;top:12px;font-family:var(--body);font-size:26px;line-height:1;color:var(--foil);transition:transform .2s}
  .faq details[open] summary::after{transform:rotate(45deg)}
  .faq summary:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
  .faq details p{margin:0 0 16px;color:var(--ink-soft)}
"""
def faq(items):
    return '<div class="faq">\n' + "\n".join(
        f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + '\n      </div>'
def pick(items, *idx):
    return [items[i] for i in idx]
def _plain(s):
    return _re.sub(r"\s+", " ", _html.unescape(_re.sub(r"<[^>]+>", "", s))).strip()
HOME = "https://drihsaneren.com/"
AUTHOR_ID = HOME + "#ihsan-eren"
AUTHOR = {"@type": "Person", "@id": AUTHOR_ID, "name": "İhsan Eren", "url": HOME,
          "jobTitle": ["Fizyoterapist", "İntörn Tıp Doktoru"]}
def cond(name, home_id=None):
    d = {"@type": "MedicalCondition", "name": name}
    if home_id: d["@id"] = HOME + "#" + home_id
    return d
def ld(obj):
    return ('<script type="application/ld+json">\n'
            + _json.dumps(obj, ensure_ascii=False, indent=2).replace("</", "<\\/")
            + '\n</script>\n')
def schema(fname, full_title, desc, about, faq_items):
    url = HOME + fname
    out = ld({"@context": "https://schema.org", "@type": "MedicalWebPage", "@id": url + "#sayfa",
              "name": full_title, "description": desc, "url": url, "inLanguage": "tr",
              "about": about, "lastReviewed": "2026-09-28",
              "author": AUTHOR, "reviewedBy": {"@id": AUTHOR_ID}})
    if faq_items:
        out += ld({"@context": "https://schema.org", "@type": "FAQPage", "@id": url + "#sss",
                   "url": url, "inLanguage": "tr",
                   "mainEntity": [{"@type": "Question", "name": _plain(q),
                                   "acceptedAnswer": {"@type": "Answer", "text": _plain(a)}}
                                  for q, a in faq_items]})
    return out

if MODE == "artifact":
    FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
             '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
             '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Marcellus&family=Figtree:wght@400;500;600&display=swap">')
    FONTFACE = ""
else:
    # Site Core v2 (7 Ekim 2026, başka oturumda eklendi): yazı tipleri ve ortak yardımcılar /assets/site-core.css|js içinde;
    # her sayfa bu iki dosyayı kök-göreli yolla yükler. Sayfa içinde @font-face YOK.
    FONTS = ""
    FONTFACE = ""
CORE_CSS = '<link rel="stylesheet" href="/assets/site-core.css">\n' if MODE == "github" else ""
CORE_JS = '<script src="/assets/site-core.js" defer></script>\n' if MODE == "github" else ""

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg>'
BACK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 6-6 6 6 6"/></svg>'

CHAT_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 21l2.1-5.4A8.4 8.4 0 1 1 21 11.5z"/><path transform="translate(7.9 6.8) scale(.4)" d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z" fill="currentColor" stroke-width="2.5"/></svg>'
def CTA_CARD(topic, msg_topic):
    """Yazının sonunda konuya özel hızlı iletişim kartı."""
    wa = "https://wa.me/905538815568?text=" + quote(f"Merhaba, {msg_topic} için evde değerlendirme ve seans planlamak istiyorum.")
    return f"""<aside class="ctacard" aria-label="Hızlı iletişim">
        <span class="ic">{CHAT_SVG}</span>
        <div>
          <p class="k">Hızlı iletişim</p>
          <h3>Evde değerlendirme ister misiniz?</h3>
          <p>{topic} için ev ortamında kapsamlı fonksiyonel değerlendirme ve kişiye özel rehabilitasyon seansı planlamak isterseniz WhatsApp'tan iletişime geçebilirsiniz.</p>
          <div class="acts"><a class="cta" href="{wa}" target="_blank" rel="noopener">WhatsApp'tan yazın {ARROW}</a><a class="cta ghost" href="index.html#tanisma">Ücretsiz ön görüşme planla</a></div>
        </div>
      </aside>"""

CSS = """
  :root{
    color-scheme: dark;
    --ground:#1c2819; --ground-2:#223020; --panel:#263723;
    --ink:#ece5cf; --ink-soft:#c9c6ad; --muted:#9fab90; --sage:#8fa476;
    --gold:#e2ab47; --foil:#d8b25e;
    --line:rgba(236,229,207,.14); --line-strong:rgba(216,178,94,.55);
    --paper:#efe9d6; --paper-ink:#2b3325;
    --display:"Marcellus","Cormorant Garamond",Georgia,"Times New Roman",serif;
    --body:"Figtree","Segoe UI",system-ui,-apple-system,sans-serif;
    --gut:clamp(16px,5vw,40px);
  }
  *{box-sizing:border-box}
  html{scroll-behavior:smooth;background:#1c2819}
  body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--body);font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased}
  a{color:var(--foil);text-underline-offset:3px}
  a:focus-visible,button:focus-visible{outline:2px solid var(--gold);outline-offset:3px;border-radius:4px}
  h1,h2,h3{font-family:var(--display);font-weight:400;text-wrap:balance;margin:0}
  .wrap{max-width:1120px;margin:0 auto;padding-inline:var(--gut)}
  .col{max-width:760px}
  .eyebrow{font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);font-weight:600;margin:0}

  .bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:40;background:rgba(28,40,25,.9);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
  .bar .wrap{display:flex;align-items:center;gap:18px;padding-block:10px}
  .brand{display:flex;align-items:center;flex:none;text-decoration:none;border-radius:8px}
  .brand img{height:36px;width:auto;display:block;transition:transform .3s ease}
  .brand:hover img{transform:scale(1.06)}
  .brand{position:relative}
  .brand .reg{position:absolute;top:-3px;right:-9px;font:600 9px/1 var(--body);color:var(--foil);letter-spacing:0}
  .links{display:flex;gap:20px;margin-left:auto}
  .links a{color:var(--ink-soft);text-decoration:none;font-size:14px}
  .links a:hover,.links a[aria-current],.links a.on{color:var(--foil)}
  .cta{display:inline-flex;align-items:center;gap:8px;padding:11px 18px;border-radius:999px;background:var(--foil);color:var(--ground);font-weight:600;font-size:15px;text-decoration:none;border:1px solid var(--foil);max-width:100%}
  .cta:hover{background:var(--gold);border-color:var(--gold)}
  .cta.ghost{background:transparent;color:var(--ink);border-color:var(--line-strong)}
  .cta.ghost:hover{color:var(--foil);border-color:var(--foil);background:transparent}
  .cta svg{width:16px;height:16px;flex:none}
  .bar .cta{margin-left:auto;padding:8px 14px;font-size:14px}
  .links + .cta{margin-left:0}
  @media (max-width:900px){.links{display:none}}

  .back{display:inline-flex;align-items:center;gap:6px;color:var(--muted);text-decoration:none;font-size:14px}
  .back svg{width:16px;height:16px}
  .back:hover{color:var(--foil)}

  header.page{padding-block:clamp(28px,6vw,56px) clamp(24px,5vw,40px);border-bottom:1px solid var(--line);
    background:radial-gradient(120% 80% at 0% 0%, rgba(143,164,118,.14), transparent 60%),var(--ground)}
  header.page .eyebrow{margin-top:22px;color:var(--foil)}
  header.page h1{font-size:clamp(34px,7vw,54px);line-height:1.08;margin:10px 0 14px}
  header.page .lede{margin:0;color:var(--ink-soft);font-size:clamp(17px,2.2vw,19px);max-width:60ch}
  .meta{margin:16px 0 0;font-size:13px;color:var(--muted)}

  main section{padding-block:clamp(36px,7vw,60px)}
  main section + section{border-top:1px solid var(--line)}
  h2{font-size:clamp(26px,5vw,34px);line-height:1.15;margin:0 0 14px}
  h3{font-size:21px;line-height:1.25;margin:0 0 6px}
  p{margin:0 0 14px;max-width:65ch}
  .soft{color:var(--ink-soft)}
  ul.dots{margin:0 0 14px;padding:0;list-style:none;display:grid;gap:8px;max-width:65ch}
  ul.dots li{position:relative;padding-left:18px}
  ul.dots li::before{content:"";position:absolute;left:2px;top:.72em;width:6px;height:6px;border-radius:50%;background:var(--gold)}

  .note{border:1px solid var(--line-strong);border-radius:10px;padding:14px 16px;background:var(--ground-2);font-size:15px;color:var(--ink-soft);max-width:760px}
  .note strong{color:var(--ink)}
  .warn{border-color:rgba(226,171,71,.8)}

  .sources{font-size:14px;color:var(--muted)}
  .sources ol{margin:8px 0 0;padding-left:20px;display:grid;gap:6px}
  .sources a{color:var(--ink-soft)}

  .more{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px}
  .more a{display:grid;gap:4px;padding:16px;border:1px solid var(--line);border-radius:10px;background:var(--ground-2);text-decoration:none;color:var(--ink)}
  .more a:hover{border-color:var(--line-strong)}
  .more .k{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--foil);font-weight:600}
  .more .t{font-family:var(--display);font-size:20px;line-height:1.2}

  .ctacard{margin-top:28px;display:grid;grid-template-columns:auto minmax(0,1fr);gap:18px;align-items:start;padding:22px;border:1px solid var(--line-strong);border-radius:16px;
    background:radial-gradient(120% 120% at 0% 0%, rgba(226,171,71,.12), transparent 60%),var(--ground-2);max-width:820px}
  .ctacard .ic{width:52px;height:52px;border-radius:50%;background:var(--foil);color:var(--ground);display:grid;place-items:center;box-shadow:0 6px 16px rgba(0,0,0,.3)}
  .ctacard .ic svg{width:26px;height:26px}
  .ctacard .k{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--foil);font-weight:600;margin:0}
  .ctacard h3{font-size:22px;margin:4px 0 6px}
  .ctacard p{margin:0 0 14px;color:var(--ink-soft);max-width:62ch}
  .ctacard .acts{display:flex;flex-wrap:wrap;gap:10px}
  @media (max-width:560px){.ctacard{grid-template-columns:1fr;padding:18px}.ctacard .ic{width:44px;height:44px}}
  footer{border-top:1px solid var(--line);padding-block:26px 34px;color:var(--muted);font-size:13px;text-align:center}
  footer p{margin:0 auto;max-width:none}
  footer p + p{margin-top:6px}

  @media (prefers-reduced-motion:reduce){html{scroll-behavior:auto} *{animation:none!important;transition:none!important}}
"""

KOSE_PAGES = {"zayiflama-ilaci-ve-kas.html", "uzun-covid.html", "kosucu-dizi.html", "yuksek-tansiyon.html", "yogun-bakim-sonrasi.html", "diyabette-egzersiz.html", "omurga-kirigi.html", "dupuytren-kontrakturu.html", "kalp-yetmezligi.html", "pelvik-organ-sarkmasi.html", "beyin-sarsintisi.html", "periferik-arter-hastaligi.html", "bilgi.html", "bebeklerde-tortikolis.html", "besinci-metatars-kirigi.html", "omuz-ucu-yaralanmasi.html", "cekic-parmak.html", "kasik-zorlanmasi.html", "kaburga-kirigi.html", "bel-fitigi-ameliyati-sonrasi.html", "buyume-agrilari.html", "koprucuk-kemigi-kirigi.html", "ayak-bilegi-kirigi.html", "baldir-kasi-zorlanmasi.html", "omuz-kireclenmesi.html", "asil-tendonu-kopmasi.html", "kubital-tunel-sendromu.html", "diz-kapagi-cikigi.html", "sever-hastaligi.html", "karin-kasi-ayrilmasi.html", "omuzda-kirec-birikmesi.html", "boyun-incinmesi.html", "el-kireclenmesi.html", "eklem-hipermobilitesi.html", "el-bilegi-kirigi.html", "morton-noromasi.html", "osgood-schlatter.html", "sakroiliak-eklem-agrisi.html", "arka-uyluk-zorlanmasi.html", "kaval-kemigi-agrisi.html", "boyun-tutulmasi.html", "ganglion-kisti.html", "gece-bacak-kramplari.html", "kurek-kemigi-arasi-agri.html", "baker-kisti.html", "kambur-durus.html", "piriformis-sendromu.html", "omuz-cikigi.html", "atlet-dizi.html", "kalca-sikismasi.html", "boyun-duzlesmesi.html", "kuyruk-sokumu-agrisi.html", "huzursuz-bacak.html", "bel-kaymasi.html", "sarkopeni.html", "demans-egzersiz.html", "golfcu-dirsegi.html", "guillain-barre.html", "halluks-valgus.html", "tetik-parmak.html", "duztabanlik.html", "omurilik-yaralanmasi.html", "de-quervain.html", "diyabetik-noropati.html", "kalca-yan-agrisi.html", "lenfodem.html", "yuz-felci.html", "titreme.html", "surekli-usume.html", "romatoid-artrit.html", "kalp-rehabilitasyonu.html", "koah.html", "on-capraz-bag.html", "dost-molasi.html", "stres.html", "donuk-omuz.html", "boyun-agrisi.html", "boyun-fitigi.html", "bel-agrisi.html", "bel-fitigi.html", "diz-kireclenmesi.html", "inme-rehabilitasyonu.html", "topuk-dikeni.html", "omuz-sikismasi.html", "karpal-tunel-sendromu.html", "dusme-onleme.html", "protez-sonrasi.html", "masa-basi.html", "kalca-kireclenmesi.html", "tenisci-dirsegi.html", "kemik-erimesi.html", "ayak-bilegi-burkulmasi.html", "sabah-rutini.html", "hareket.html", "uyku.html", "parkinson.html", "kalca-kirigi.html", "kanser-egzersiz.html", "menisku-yirtigi.html", "fibromiyalji.html", "bas-donmesi.html", "ankilozan-spondilit.html", "diz-onu-agrisi.html", "asil-tendinopatisi.html", "bas-agrisi.html", "skolyoz.html", "rotator-manset-yirtigi.html", "cene-eklemi.html", "idrar-kacirma.html", "gebelikte-bel-agrisi.html", "dar-kanal.html", "multipl-skleroz.html", "otur-kalk-testi.html", "duvar-oturusu.html", "ic-cekis.html", "doga-recetesi.html", "bag-kurmak.html"}
NEWS_PAGES = {"nobel-2026.html"}   # Bilim gündemi'nin özel sayfaları
SELF_PAGES = {"adim-hedefi.html", "sakatlanmayi-onleyen-isinma.html", "alti-dakika-yurume-testi.html", "tansiyon-gunlugu.html", "denge-antrenmani.html", "yemek-sonrasi-yuruyus.html", "iki-dakika-adim-testi.html", "guc-devresi.html", "dizin-12-sirri.html", "oturma-suresi.html", "dustukten-sonra-kalkma.html", "tempolu-yuruyus.html", "pelvik-taban-zamanlayicisi.html", "dusme-riski-testi.html", "dort-asamali-denge-testi.html", "mola-zamanlayicisi.html", "kalk-yuru-testi.html", "bel-boy-orani.html", "nabiz-olcer.html", "agri-gunlugu.html", "yurume-hizi-testi.html", "sandalye-testi.html", "egzersizde-agri.html", "agriyi-anlamak.html", "hareket-atistirmaliklari.html", "denge-testi.html", "uc-kapi.html", "kucuk-adimlar.html", "kas-gevsetme.html", "ruh-hali-olcumu.html", "ruh-sagligi-egzersiz.html", "dost-molasi.html", "stres.html", "masa-basi.html", "sabah-rutini.html", "hareket.html", "uyku.html", "otur-kalk-testi.html", "duvar-oturusu.html", "ic-cekis.html", "doga-recetesi.html", "bag-kurmak.html"}
def bar(current):
    items = [("bilgi.html", "Bilgi köşesi"), ("bilgi.html#kendine-iyi-bak", "Kendine iyi bak"), ("yenilikler.html", "Bilim gündemi")]
    def attr(h):
        if h == current: return ' aria-current="page"'
        if h == "yenilikler.html" and current in NEWS_PAGES: return ' class="on"'
        if h == "bilgi.html#kendine-iyi-bak" and current in SELF_PAGES: return ' class="on"'
        if h == "bilgi.html" and current in KOSE_PAGES and current not in SELF_PAGES: return ' class="on"'
        return ""
    links = "\n      ".join(f'<a href="{h}"{attr(h)}>{t}</a>' for h, t in items)
    return f'''<header class="bar">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="{IMG}logo-mark.svg" alt="İhsan Eren" width="44" height="36"><sup class="reg">®</sup></a>
    <nav class="links" aria-label="Bilgi köşesi">
      <a href="index.html">Ana sayfa</a>
      {links}
    </nav>
    {SEARCH_BTN}
    {switcher(current) if MODE == "github" else ""}
    <a class="cta" href="{WA}" target="_blank" rel="noopener">Seans planla</a>
  </div>
</header>'''

TOPICS = {
    "adim-hedefi.html": ("Kendine iyi bak", "Adım hedefi planlayıcısı"),
    "sakatlanmayi-onleyen-isinma.html": ("Kendine iyi bak", "Sakatlanmayı önleyen ısınma"),
    "zayiflama-ilaci-ve-kas.html": ("Rehabilitasyon rehberi", "Zayıflama ilacı kullanırken kaslarınızı koruyun"),
    "uzun-covid.html": ("Rehabilitasyon rehberi", "Uzun COVID'de hareket ve nefes"),
    "kosucu-dizi.html": ("Hastalık rehberi", "Koşucu dizi (iliotibial bant sendromu)"),
    "alti-dakika-yurume-testi.html": ("Kendine iyi bak", "6 dakika yürüme testi"),
    "tansiyon-gunlugu.html": ("Kendine iyi bak", "Ev tansiyon günlüğü"),
    "yuksek-tansiyon.html": ("Rehabilitasyon rehberi", "Yüksek tansiyonda egzersiz"),
    "yogun-bakim-sonrasi.html": ("Rehabilitasyon rehberi", "Yoğun bakımdan sonra iyileşme"),
    "diyabette-egzersiz.html": ("Rehabilitasyon rehberi", "Tip 2 diyabette egzersiz"),
    "denge-antrenmani.html": ("Kendine iyi bak", "Denge antrenmanı"),
    "yemek-sonrasi-yuruyus.html": ("Kendine iyi bak", "Yemek sonrası yürüyüş"),
    "omurga-kirigi.html": ("Hastalık rehberi", "Kemik erimesine bağlı omurga kırığı"),
    "dupuytren-kontrakturu.html": ("Hastalık rehberi", "Dupuytren kontraktürü"),
    "kalp-yetmezligi.html": ("Rehabilitasyon rehberi", "Kalp yetmezliğinde egzersiz"),
    "iki-dakika-adim-testi.html": ("Kendine iyi bak", "2 dakika adım testi"),
    "guc-devresi.html": ("Kendine iyi bak", "Evde güç devresi"),
    "pelvik-organ-sarkmasi.html": ("Hastalık rehberi", "Pelvik organ sarkması (rahim sarkması)"),
    "beyin-sarsintisi.html": ("Hastalık rehberi", "Beyin sarsıntısı (konküzyon)"),
    "periferik-arter-hastaligi.html": ("Rehabilitasyon rehberi", "Periferik arter hastalığı ve yürüyüş egzersizi"),
    "bel-agrisi.html": ("Hastalık rehberi", "Bel ağrısı"),
    "bel-fitigi.html": ("Hastalık rehberi", "Bel fıtığı ve siyatik"),
    "diz-kireclenmesi.html": ("Hastalık rehberi", "Diz kireçlenmesi"),
    "kalca-kireclenmesi.html": ("Hastalık rehberi", "Kalça kireçlenmesi"),
    "boyun-agrisi.html": ("Hastalık rehberi", "Boyun ağrısı"),
    "boyun-fitigi.html": ("Hastalık rehberi", "Boyun fıtığı ve sinir sıkışması"),
    "donuk-omuz.html": ("Hastalık rehberi", "Donuk omuz (adeziv kapsülit)"),
    "inme-rehabilitasyonu.html": ("Rehabilitasyon rehberi", "İnme (felç) sonrası rehabilitasyon"),
    "dusme-onleme.html": ("Rehabilitasyon rehberi", "Düşmeleri önleme ve denge"),
    "protez-sonrasi.html": ("Rehabilitasyon rehberi", "Diz ve kalça protezi sonrası"),
    "kalca-kirigi.html": ("Rehabilitasyon rehberi", "Kalça kırığı sonrası rehabilitasyon"),
    "parkinson.html": ("Rehabilitasyon rehberi", "Parkinson hastalığında egzersiz"),
    "multipl-skleroz.html": ("Rehabilitasyon rehberi", "Multipl sklerozda (MS) egzersiz"),
    "kanser-egzersiz.html": ("Rehabilitasyon rehberi", "Kanser tedavisi sırasında ve sonrasında egzersiz"),
    "koah.html": ("Rehabilitasyon rehberi", "KOAH'ta akciğer rehabilitasyonu"),
    "kalp-rehabilitasyonu.html": ("Rehabilitasyon rehberi", "Kalp rehabilitasyonu"),
    "topuk-dikeni.html": ("Hastalık rehberi", "Topuk dikeni (plantar fasiit)"),
    "omuz-sikismasi.html": ("Hastalık rehberi", "Omuz sıkışması (subakromiyal ağrı)"),
    "karpal-tunel-sendromu.html": ("Hastalık rehberi", "Karpal tünel sendromu"),
    "tenisci-dirsegi.html": ("Hastalık rehberi", "Tenisçi dirseği"),
    "kemik-erimesi.html": ("Hastalık rehberi", "Kemik erimesi (osteoporoz)"),
    "ayak-bilegi-burkulmasi.html": ("Hastalık rehberi", "Ayak bileği burkulması"),
    "menisku-yirtigi.html": ("Hastalık rehberi", "Menisküs yırtığı"),
    "fibromiyalji.html": ("Hastalık rehberi", "Fibromiyalji"),
    "bas-donmesi.html": ("Hastalık rehberi", "Baş dönmesi (BPPV)"),
    "ankilozan-spondilit.html": ("Hastalık rehberi", "Ankilozan spondilit"),
    "diz-onu-agrisi.html": ("Hastalık rehberi", "Diz önü ağrısı"),
    "asil-tendinopatisi.html": ("Hastalık rehberi", "Aşil tendinopatisi"),
    "bas-agrisi.html": ("Hastalık rehberi", "Baş ağrısı"),
    "skolyoz.html": ("Hastalık rehberi", "Skolyoz"),
    "rotator-manset-yirtigi.html": ("Hastalık rehberi", "Rotator manşet yırtığı"),
    "cene-eklemi.html": ("Hastalık rehberi", "Çene eklemi rahatsızlıkları"),
    "idrar-kacirma.html": ("Hastalık rehberi", "İdrar kaçırma ve pelvik taban egzersizleri"),
    "gebelikte-bel-agrisi.html": ("Hastalık rehberi", "Gebelikte bel ve leğen kemiği ağrısı"),
    "dar-kanal.html": ("Hastalık rehberi", "Dar kanal (lomber spinal stenoz)"),
    "bel-kaymasi.html": ("Hastalık rehberi", "Bel kayması (spondilolistezis)"),
    "huzursuz-bacak.html": ("Hastalık rehberi", "Huzursuz bacak sendromu"),
    "kuyruk-sokumu-agrisi.html": ("Hastalık rehberi", "Kuyruk sokumu ağrısı"),
    "bebeklerde-tortikolis.html": ("Hastalık rehberi", "Bebeklerde tortikolis"),
    "besinci-metatars-kirigi.html": ("Hastalık rehberi", "Ayak dış kenarı (5. tarak kemiği) kırığı"),
    "omuz-ucu-yaralanmasi.html": ("Hastalık rehberi", "Omuz ucu (AC eklem) yaralanması"),
    "cekic-parmak.html": ("Hastalık rehberi", "Çekiç parmak (mallet finger)"),
    "kasik-zorlanmasi.html": ("Hastalık rehberi", "Kasık zorlanması"),
    "kaburga-kirigi.html": ("Hastalık rehberi", "Kaburga kırığı ve morarması"),
    "bel-fitigi-ameliyati-sonrasi.html": ("Hastalık rehberi", "Bel fıtığı ameliyatı sonrası"),
    "buyume-agrilari.html": ("Hastalık rehberi", "Çocuklarda büyüme ağrıları"),
    "koprucuk-kemigi-kirigi.html": ("Hastalık rehberi", "Köprücük kemiği kırığı"),
    "ayak-bilegi-kirigi.html": ("Hastalık rehberi", "Ayak bileği kırığı sonrası"),
    "baldir-kasi-zorlanmasi.html": ("Hastalık rehberi", "Baldır kası zorlanması"),
    "omuz-kireclenmesi.html": ("Hastalık rehberi", "Omuz kireçlenmesi"),
    "asil-tendonu-kopmasi.html": ("Hastalık rehberi", "Aşil tendonu kopması"),
    "kubital-tunel-sendromu.html": ("Hastalık rehberi", "Kübital tünel sendromu"),
    "diz-kapagi-cikigi.html": ("Hastalık rehberi", "Diz kapağı çıkığı"),
    "sever-hastaligi.html": ("Hastalık rehberi", "Çocuklarda topuk ağrısı (Sever)"),
    "karin-kasi-ayrilmasi.html": ("Hastalık rehberi", "Doğum sonrası karın kası ayrılması"),
    "omuzda-kirec-birikmesi.html": ("Hastalık rehberi", "Omuzda kireç birikmesi"),
    "boyun-incinmesi.html": ("Hastalık rehberi", "Boyun incinmesi (whiplash)"),
    "el-kireclenmesi.html": ("Hastalık rehberi", "El ve parmak kireçlenmesi"),
    "eklem-hipermobilitesi.html": ("Hastalık rehberi", "Eklem hipermobilitesi"),
    "el-bilegi-kirigi.html": ("Hastalık rehberi", "El bileği kırığı sonrası"),
    "morton-noromasi.html": ("Hastalık rehberi", "Morton nöroması"),
    "osgood-schlatter.html": ("Hastalık rehberi", "Osgood-Schlatter"),
    "sakroiliak-eklem-agrisi.html": ("Hastalık rehberi", "Sakroiliak eklem ağrısı"),
    "arka-uyluk-zorlanmasi.html": ("Hastalık rehberi", "Arka uyluk zorlanması"),
    "kaval-kemigi-agrisi.html": ("Hastalık rehberi", "Kaval kemiği ağrısı"),
    "boyun-tutulmasi.html": ("Hastalık rehberi", "Boyun tutulması"),
    "ganglion-kisti.html": ("Hastalık rehberi", "Ganglion kisti"),
    "gece-bacak-kramplari.html": ("Hastalık rehberi", "Gece bacak krampları"),
    "kurek-kemigi-arasi-agri.html": ("Hastalık rehberi", "Kürek kemiği arası ağrı"),
    "baker-kisti.html": ("Hastalık rehberi", "Baker kisti"),
    "kambur-durus.html": ("Hastalık rehberi", "Kambur duruş (kifoz)"),
    "piriformis-sendromu.html": ("Hastalık rehberi", "Piriformis sendromu"),
    "omuz-cikigi.html": ("Hastalık rehberi", "Omuz çıkığı"),
    "atlet-dizi.html": ("Hastalık rehberi", "Atlet dizi (patellar tendinopati)"),
    "kalca-sikismasi.html": ("Hastalık rehberi", "Kalça sıkışması (FAI)"),
    "boyun-duzlesmesi.html": ("Hastalık rehberi", "Boyun düzleşmesi"),
    "on-capraz-bag.html": ("Hastalık rehberi", "Ön çapraz bağ yaralanması"),
    "romatoid-artrit.html": ("Hastalık rehberi", "Romatoid artrit ve egzersiz"),
    "surekli-usume.html": ("Hastalık rehberi", "Sürekli üşüme (soğuğa duyarlılık)"),
    "titreme.html": ("Hastalık rehberi", "Titreme (tremor)"),
    "yuz-felci.html": ("Hastalık rehberi", "Yüz felci (Bell felci)"),
    "kalca-yan-agrisi.html": ("Hastalık rehberi", "Kalça yan ağrısı"),
    "lenfodem.html": ("Rehabilitasyon rehberi", "Lenfödem"),
    "de-quervain.html": ("Hastalık rehberi", "De Quervain (bilek ağrısı)"),
    "diyabetik-noropati.html": ("Hastalık rehberi", "Diyabetik nöropati"),
    "duztabanlik.html": ("Hastalık rehberi", "Düztabanlık"),
    "omurilik-yaralanmasi.html": ("Rehabilitasyon rehberi", "Omurilik yaralanması"),
    "halluks-valgus.html": ("Hastalık rehberi", "Halluks valgus"),
    "tetik-parmak.html": ("Hastalık rehberi", "Tetik parmak"),
    "golfcu-dirsegi.html": ("Hastalık rehberi", "Golfçü dirseği"),
    "guillain-barre.html": ("Rehabilitasyon rehberi", "Guillain-Barré sendromu"),
    "sarkopeni.html": ("Hastalık rehberi", "Sarkopeni"),
    "demans-egzersiz.html": ("Rehabilitasyon rehberi", "Demansta egzersiz"),
    "stres.html": ("Kendine iyi bak", "Stresli anlarda ne yapabilirsiniz?"),
    "masa-basi.html": ("Kendine iyi bak", "Masa başında çalışanlar için"),
    "sabah-rutini.html": ("Kendine iyi bak", "Güne 5 dakikayla başlayın"),
    "hareket.html": ("Kendine iyi bak", "Ne kadar hareket yeterli?"),
    "uyku.html": ("Kendine iyi bak", "İyi uyku için"),
    "otur-kalk-testi.html": ("Kendine iyi bak", "Yere oturup kalkabiliyor musunuz?"),
    "dizin-12-sirri.html": ("Kendine iyi bak", "Dizin 12 Sırrı"),
    "duvar-oturusu.html": ("Kendine iyi bak", "Tansiyon için duvar oturuşu"),
    "ic-cekis.html": ("Kendine iyi bak", "5 dakikalık iç çekiş nefesi"),
    "doga-recetesi.html": ("Kendine iyi bak", "Doğa reçetesi"),
    "bag-kurmak.html": ("Kendine iyi bak", "Sosyal bağ ve sağlık"),
    "uc-kapi.html": ("Kendine iyi bak", "Üç Kapı: beden, nefes, zihin"),
    "oturma-suresi.html": ("Kendine iyi bak", "Günlük oturma süresi hesaplayıcısı"),
    "dustukten-sonra-kalkma.html": ("Kendine iyi bak", "Düştükten sonra yerden kalkma"),
    "tempolu-yuruyus.html": ("Kendine iyi bak", "Tempolu yürüyüş metronomu"),
    "pelvik-taban-zamanlayicisi.html": ("Kendine iyi bak", "Pelvik taban egzersiz zamanlayıcısı"),
    "dusme-riski-testi.html": ("Kendine iyi bak", "Düşme riski testi"),
    "dort-asamali-denge-testi.html": ("Kendine iyi bak", "4 aşamalı denge testi"),
    "mola-zamanlayicisi.html": ("Kendine iyi bak", "Mola zamanlayıcısı"),
    "kalk-yuru-testi.html": ("Kendine iyi bak", "Kalk ve yürü testi"),
    "bel-boy-orani.html": ("Kendine iyi bak", "Bel–boy oranı"),
    "nabiz-olcer.html": ("Kendine iyi bak", "Nabız ölçer"),
    "agri-gunlugu.html": ("Kendine iyi bak", "Ağrı günlüğü"),
    "yurume-hizi-testi.html": ("Kendine iyi bak", "Yürüme hızı testi"),
    "sandalye-testi.html": ("Kendine iyi bak", "30 saniye sandalye testi"),
    "egzersizde-agri.html": ("Kendine iyi bak", "Egzersizde ağrı trafik ışığı"),
    "agriyi-anlamak.html": ("Kendine iyi bak", "Ağrıyı anlamak"),
    "hareket-atistirmaliklari.html": ("Kendine iyi bak", "Hareket atıştırmalıkları"),
    "denge-testi.html": ("Kendine iyi bak", "10 saniye denge testi"),
    "kucuk-adimlar.html": ("Kendine iyi bak", "Küçük adımlar planlayıcısı"),
    "kas-gevsetme.html": ("Kendine iyi bak", "Kas gevşetme: sesli rehber"),
    "ruh-hali-olcumu.html": ("Kendine iyi bak", "Ruh hâlinizi ölçün"),
    "ruh-sagligi-egzersiz.html": ("Kendine iyi bak", "Ruh sağlığı için egzersiz"),
    "dost-molasi.html": ("Kendine iyi bak", "DOST molası"),
    "yenilikler.html": ("Bilim gündemi", "Geleceğin tıbbı, bugün"),
    "nobel-2026.html": ("Bilim gündemi", "2026 Nobel ödülleri"),
}
RELATED = {
    "adim-hedefi.html": ["hareket.html", "tempolu-yuruyus.html", "yemek-sonrasi-yuruyus.html"],
    "sakatlanmayi-onleyen-isinma.html": ["on-capraz-bag.html", "arka-uyluk-zorlanmasi.html", "ayak-bilegi-burkulmasi.html"],
    "zayiflama-ilaci-ve-kas.html": ["sarkopeni.html", "guc-devresi.html", "diyabette-egzersiz.html"],
    "uzun-covid.html": ["yogun-bakim-sonrasi.html", "ic-cekis.html", "koah.html"],
    "kosucu-dizi.html": ["diz-onu-agrisi.html", "kalca-yan-agrisi.html", "sakatlanmayi-onleyen-isinma.html"],
    "alti-dakika-yurume-testi.html": ["iki-dakika-adim-testi.html", "kalp-yetmezligi.html", "koah.html"],
    "tansiyon-gunlugu.html": ["yuksek-tansiyon.html", "duvar-oturusu.html", "nabiz-olcer.html"],
    "yuksek-tansiyon.html": ["duvar-oturusu.html", "tansiyon-gunlugu.html", "tempolu-yuruyus.html"],
    "yogun-bakim-sonrasi.html": ["sarkopeni.html", "ic-cekis.html", "alti-dakika-yurume-testi.html", "uzun-covid.html"],
    "diyabette-egzersiz.html": ["yemek-sonrasi-yuruyus.html", "diyabetik-noropati.html", "guc-devresi.html", "zayiflama-ilaci-ve-kas.html"],
    "denge-antrenmani.html": ["dort-asamali-denge-testi.html", "dusme-onleme.html", "guc-devresi.html"],
    "yemek-sonrasi-yuruyus.html": ["tempolu-yuruyus.html", "oturma-suresi.html", "guc-devresi.html", "diyabette-egzersiz.html"],
    "omurga-kirigi.html": ["kemik-erimesi.html", "kambur-durus.html", "dusme-onleme.html"],
    "dupuytren-kontrakturu.html": ["tetik-parmak.html", "el-kireclenmesi.html", "karpal-tunel-sendromu.html"],
    "kalp-yetmezligi.html": ["kalp-rehabilitasyonu.html", "tempolu-yuruyus.html", "koah.html", "alti-dakika-yurume-testi.html"],
    "iki-dakika-adim-testi.html": ["sandalye-testi.html", "yurume-hizi-testi.html", "tempolu-yuruyus.html"],
    "guc-devresi.html": ["sandalye-testi.html", "hareket-atistirmaliklari.html", "sarkopeni.html"],
    "pelvik-organ-sarkmasi.html": ["idrar-kacirma.html", "pelvik-taban-zamanlayicisi.html", "karin-kasi-ayrilmasi.html"],
    "beyin-sarsintisi.html": ["boyun-incinmesi.html", "bas-agrisi.html", "bas-donmesi.html"],
    "periferik-arter-hastaligi.html": ["kalp-rehabilitasyonu.html", "dar-kanal.html", "tempolu-yuruyus.html"],
    "bel-agrisi.html": ["kuyruk-sokumu-agrisi.html", "bel-fitigi.html", "ankilozan-spondilit.html"],
    "bel-fitigi.html": ["bel-fitigi-ameliyati-sonrasi.html", "piriformis-sendromu.html", "bel-agrisi.html", "dar-kanal.html"],
    "diz-kireclenmesi.html": ["menisku-yirtigi.html", "kalca-kireclenmesi.html", "dizin-12-sirri.html"],
    "boyun-agrisi.html": ["boyun-tutulmasi.html", "boyun-duzlesmesi.html", "boyun-fitigi.html", "bas-agrisi.html"],
    "boyun-fitigi.html": ["boyun-agrisi.html", "bel-fitigi.html"],
    "donuk-omuz.html": ["omuz-kireclenmesi.html", "boyun-agrisi.html", "diz-kireclenmesi.html"],
    "stres.html": ["uyku.html", "sabah-rutini.html", "ruh-sagligi-egzersiz.html"],
    "sabah-rutini.html": ["hareket.html", "bel-agrisi.html"],
    "hareket.html": ["sabah-rutini.html", "dusme-onleme.html", "nabiz-olcer.html", "oturma-suresi.html", "adim-hedefi.html"],
    "uyku.html": ["huzursuz-bacak.html", "stres.html", "sabah-rutini.html"],
    "inme-rehabilitasyonu.html": ["dusme-onleme.html", "parkinson.html", "omurilik-yaralanmasi.html"],
    "parkinson.html": ["dusme-onleme.html", "multipl-skleroz.html", "demans-egzersiz.html"],
    "multipl-skleroz.html": ["dusme-onleme.html", "parkinson.html"],
    "kalca-kirigi.html": ["kemik-erimesi.html", "dusme-onleme.html"],
    "kanser-egzersiz.html": ["lenfodem.html", "hareket.html"],
    "koah.html": ["kalp-rehabilitasyonu.html", "ic-cekis.html", "kalp-yetmezligi.html", "alti-dakika-yurume-testi.html"],
    "kalp-rehabilitasyonu.html": ["koah.html", "duvar-oturusu.html", "periferik-arter-hastaligi.html", "kalp-yetmezligi.html"],
    "dusme-onleme.html": ["bas-donmesi.html", "diyabetik-noropati.html", "kalk-yuru-testi.html", "dusme-riski-testi.html", "dustukten-sonra-kalkma.html", "denge-antrenmani.html"],
    "protez-sonrasi.html": ["diz-kireclenmesi.html", "dusme-onleme.html"],
    "masa-basi.html": ["boyun-agrisi.html", "bel-agrisi.html", "hareket-atistirmaliklari.html", "mola-zamanlayicisi.html"],
    "kalca-kireclenmesi.html": ["kalca-sikismasi.html", "kalca-yan-agrisi.html", "protez-sonrasi.html"],
    "tenisci-dirsegi.html": ["golfcu-dirsegi.html", "karpal-tunel-sendromu.html"],
    "kemik-erimesi.html": ["el-bilegi-kirigi.html", "dusme-onleme.html", "kalca-kirigi.html", "sarkopeni.html", "omurga-kirigi.html"],
    "ayak-bilegi-burkulmasi.html": ["besinci-metatars-kirigi.html", "ayak-bilegi-kirigi.html", "topuk-dikeni.html", "dusme-onleme.html"],
    "topuk-dikeni.html": ["duztabanlik.html", "asil-tendinopatisi.html"],
    "omuz-sikismasi.html": ["omuzda-kirec-birikmesi.html", "rotator-manset-yirtigi.html", "donuk-omuz.html"],
    "karpal-tunel-sendromu.html": ["kubital-tunel-sendromu.html", "de-quervain.html", "boyun-fitigi.html"],
    "yenilikler.html": ["stres.html", "diz-kireclenmesi.html"],
    "nobel-2026.html": ["yenilikler.html", "parkinson.html"],
    "menisku-yirtigi.html": ["baker-kisti.html", "diz-kireclenmesi.html", "on-capraz-bag.html"],
    "on-capraz-bag.html": ["menisku-yirtigi.html", "diz-onu-agrisi.html", "sakatlanmayi-onleyen-isinma.html"],
    "romatoid-artrit.html": ["ankilozan-spondilit.html", "karpal-tunel-sendromu.html"],
    "surekli-usume.html": ["titreme.html", "uyku.html"],
    "titreme.html": ["parkinson.html", "surekli-usume.html"],
    "yuz-felci.html": ["inme-rehabilitasyonu.html", "cene-eklemi.html"],
    "kalca-yan-agrisi.html": ["kalca-kireclenmesi.html", "bel-agrisi.html", "kosucu-dizi.html"],
    "lenfodem.html": ["kanser-egzersiz.html", "hareket.html"],
    "de-quervain.html": ["el-kireclenmesi.html", "tetik-parmak.html", "karpal-tunel-sendromu.html"],
    "diyabetik-noropati.html": ["dusme-onleme.html", "surekli-usume.html", "diyabette-egzersiz.html"],
    "duztabanlik.html": ["halluks-valgus.html", "topuk-dikeni.html"],
    "omurilik-yaralanmasi.html": ["inme-rehabilitasyonu.html", "multipl-skleroz.html", "guillain-barre.html"],
    "halluks-valgus.html": ["morton-noromasi.html", "duztabanlik.html", "topuk-dikeni.html"],
    "tetik-parmak.html": ["cekic-parmak.html", "ganglion-kisti.html", "de-quervain.html", "karpal-tunel-sendromu.html", "dupuytren-kontrakturu.html"],
    "golfcu-dirsegi.html": ["tenisci-dirsegi.html", "de-quervain.html"],
    "guillain-barre.html": ["omurilik-yaralanmasi.html", "dusme-onleme.html"],
    "sarkopeni.html": ["dusme-onleme.html", "kemik-erimesi.html", "yogun-bakim-sonrasi.html", "zayiflama-ilaci-ve-kas.html"],
    "demans-egzersiz.html": ["dusme-onleme.html", "parkinson.html"],
    "fibromiyalji.html": ["uyku.html", "stres.html", "agriyi-anlamak.html"],
    "bas-donmesi.html": ["dusme-onleme.html", "boyun-agrisi.html"],
    "ankilozan-spondilit.html": ["bel-agrisi.html", "boyun-agrisi.html"],
    "diz-onu-agrisi.html": ["diz-kapagi-cikigi.html", "osgood-schlatter.html", "atlet-dizi.html", "diz-kireclenmesi.html", "menisku-yirtigi.html", "kosucu-dizi.html"],
    "asil-tendinopatisi.html": ["asil-tendonu-kopmasi.html", "kaval-kemigi-agrisi.html", "topuk-dikeni.html", "ayak-bilegi-burkulmasi.html", "egzersizde-agri.html"],
    "bas-agrisi.html": ["boyun-agrisi.html", "cene-eklemi.html"],
    "skolyoz.html": ["kambur-durus.html", "bel-agrisi.html", "masa-basi.html"],
    "rotator-manset-yirtigi.html": ["omuz-cikigi.html", "omuz-sikismasi.html", "donuk-omuz.html"],
    "cene-eklemi.html": ["bas-agrisi.html", "yuz-felci.html"],
    "idrar-kacirma.html": ["gebelikte-bel-agrisi.html", "hareket.html", "pelvik-taban-zamanlayicisi.html", "pelvik-organ-sarkmasi.html"],
    "gebelikte-bel-agrisi.html": ["karin-kasi-ayrilmasi.html", "idrar-kacirma.html", "bel-agrisi.html"],
    "dar-kanal.html": ["bel-fitigi.html", "bel-agrisi.html", "bel-kaymasi.html"],
    "bel-kaymasi.html": ["dar-kanal.html", "bel-agrisi.html"],
    "huzursuz-bacak.html": ["gece-bacak-kramplari.html", "uyku.html", "diyabetik-noropati.html"],
    "kuyruk-sokumu-agrisi.html": ["bel-agrisi.html", "idrar-kacirma.html"],
    "boyun-duzlesmesi.html": ["boyun-agrisi.html", "masa-basi.html"],
    "kalca-sikismasi.html": ["kalca-kireclenmesi.html", "kalca-yan-agrisi.html"],
    "atlet-dizi.html": ["arka-uyluk-zorlanmasi.html", "diz-onu-agrisi.html", "asil-tendinopatisi.html"],
    "omuz-cikigi.html": ["koprucuk-kemigi-kirigi.html", "eklem-hipermobilitesi.html", "rotator-manset-yirtigi.html", "donuk-omuz.html"],
    "piriformis-sendromu.html": ["sakroiliak-eklem-agrisi.html", "bel-fitigi.html", "kalca-yan-agrisi.html"],
    "kambur-durus.html": ["kurek-kemigi-arasi-agri.html", "skolyoz.html", "masa-basi.html", "omurga-kirigi.html"],
    "baker-kisti.html": ["menisku-yirtigi.html", "diz-kireclenmesi.html"],
    "kurek-kemigi-arasi-agri.html": ["kaburga-kirigi.html", "kambur-durus.html", "boyun-fitigi.html"],
    "gece-bacak-kramplari.html": ["huzursuz-bacak.html", "uyku.html", "periferik-arter-hastaligi.html"],
    "ganglion-kisti.html": ["de-quervain.html", "tetik-parmak.html"],
    "boyun-tutulmasi.html": ["bebeklerde-tortikolis.html", "boyun-incinmesi.html", "boyun-agrisi.html", "masa-basi.html"],
    "kaval-kemigi-agrisi.html": ["baldir-kasi-zorlanmasi.html", "asil-tendinopatisi.html", "duztabanlik.html"],
    "arka-uyluk-zorlanmasi.html": ["kasik-zorlanmasi.html", "kalca-sikismasi.html", "atlet-dizi.html", "sakatlanmayi-onleyen-isinma.html"],
    "sakroiliak-eklem-agrisi.html": ["bel-agrisi.html", "piriformis-sendromu.html"],
    "osgood-schlatter.html": ["buyume-agrilari.html", "sever-hastaligi.html", "diz-onu-agrisi.html", "atlet-dizi.html"],
    "morton-noromasi.html": ["halluks-valgus.html", "duztabanlik.html"],
    "el-bilegi-kirigi.html": ["kemik-erimesi.html", "dusme-onleme.html"],
    "eklem-hipermobilitesi.html": ["omuz-cikigi.html", "fibromiyalji.html"],
    "el-kireclenmesi.html": ["de-quervain.html", "romatoid-artrit.html"],
    "boyun-incinmesi.html": ["boyun-tutulmasi.html", "boyun-agrisi.html", "beyin-sarsintisi.html"],
    "omuzda-kirec-birikmesi.html": ["omuz-sikismasi.html", "donuk-omuz.html"],
    "karin-kasi-ayrilmasi.html": ["idrar-kacirma.html", "gebelikte-bel-agrisi.html"],
    "sever-hastaligi.html": ["osgood-schlatter.html", "topuk-dikeni.html"],
    "diz-kapagi-cikigi.html": ["on-capraz-bag.html", "diz-onu-agrisi.html"],
    "kubital-tunel-sendromu.html": ["karpal-tunel-sendromu.html", "golfcu-dirsegi.html"],
    "asil-tendonu-kopmasi.html": ["asil-tendinopatisi.html", "ayak-bilegi-burkulmasi.html"],
    "omuz-kireclenmesi.html": ["donuk-omuz.html", "omuz-sikismasi.html"],
    "baldir-kasi-zorlanmasi.html": ["asil-tendonu-kopmasi.html", "kaval-kemigi-agrisi.html"],
    "ayak-bilegi-kirigi.html": ["ayak-bilegi-burkulmasi.html", "el-bilegi-kirigi.html"],
    "koprucuk-kemigi-kirigi.html": ["omuz-ucu-yaralanmasi.html", "omuz-cikigi.html", "el-bilegi-kirigi.html"],
    "buyume-agrilari.html": ["osgood-schlatter.html", "sever-hastaligi.html", "eklem-hipermobilitesi.html"],
    "bel-fitigi-ameliyati-sonrasi.html": ["bel-fitigi.html", "bel-agrisi.html"],
    "kaburga-kirigi.html": ["kurek-kemigi-arasi-agri.html", "kemik-erimesi.html"],
    "kasik-zorlanmasi.html": ["arka-uyluk-zorlanmasi.html", "kalca-sikismasi.html"],
    "cekic-parmak.html": ["tetik-parmak.html", "el-kireclenmesi.html"],
    "omuz-ucu-yaralanmasi.html": ["koprucuk-kemigi-kirigi.html", "omuz-cikigi.html"],
    "besinci-metatars-kirigi.html": ["ayak-bilegi-burkulmasi.html", "ayak-bilegi-kirigi.html"],
    "bebeklerde-tortikolis.html": ["boyun-tutulmasi.html", "buyume-agrilari.html"],
    "otur-kalk-testi.html": ["dusme-onleme.html", "hareket.html", "denge-testi.html", "sandalye-testi.html"],
    "dizin-12-sirri.html": ["diz-kireclenmesi.html", "otur-kalk-testi.html"],
    "duvar-oturusu.html": ["hareket.html", "otur-kalk-testi.html", "yuksek-tansiyon.html"],
    "ic-cekis.html": ["stres.html", "uyku.html", "kas-gevsetme.html"],
    "doga-recetesi.html": ["bag-kurmak.html", "stres.html"],
    "bag-kurmak.html": ["doga-recetesi.html", "stres.html"],
    "dost-molasi.html": ["ic-cekis.html", "bag-kurmak.html", "kucuk-adimlar.html"],
    "kucuk-adimlar.html": ["uc-kapi.html", "ruh-hali-olcumu.html", "ruh-sagligi-egzersiz.html"],
    "uc-kapi.html": ["kas-gevsetme.html", "ic-cekis.html", "ruh-sagligi-egzersiz.html"],
    "oturma-suresi.html": ["hareket.html", "mola-zamanlayicisi.html", "tempolu-yuruyus.html"],
    "dustukten-sonra-kalkma.html": ["dusme-onleme.html", "dusme-riski-testi.html", "otur-kalk-testi.html"],
    "tempolu-yuruyus.html": ["yurume-hizi-testi.html", "hareket.html", "hareket-atistirmaliklari.html", "yemek-sonrasi-yuruyus.html", "adim-hedefi.html"],
    "pelvik-taban-zamanlayicisi.html": ["idrar-kacirma.html", "karin-kasi-ayrilmasi.html", "pelvik-organ-sarkmasi.html"],
    "dusme-riski-testi.html": ["dusme-onleme.html", "dort-asamali-denge-testi.html", "kalk-yuru-testi.html"],
    "dort-asamali-denge-testi.html": ["denge-testi.html", "dusme-riski-testi.html", "dusme-onleme.html", "denge-antrenmani.html"],
    "mola-zamanlayicisi.html": ["masa-basi.html", "hareket-atistirmaliklari.html"],
    "kalk-yuru-testi.html": ["dusme-onleme.html", "yurume-hizi-testi.html", "sandalye-testi.html"],
    "bel-boy-orani.html": ["hareket.html", "hareket-atistirmaliklari.html"],
    "nabiz-olcer.html": ["hareket.html", "yurume-hizi-testi.html", "tansiyon-gunlugu.html"],
    "agri-gunlugu.html": ["agriyi-anlamak.html", "egzersizde-agri.html"],
    "yurume-hizi-testi.html": ["sandalye-testi.html", "denge-testi.html", "dusme-onleme.html", "tempolu-yuruyus.html", "iki-dakika-adim-testi.html"],
    "sandalye-testi.html": ["denge-testi.html", "otur-kalk-testi.html", "dusme-onleme.html", "yurume-hizi-testi.html", "guc-devresi.html"],
    "egzersizde-agri.html": ["agriyi-anlamak.html", "asil-tendinopatisi.html", "diz-kireclenmesi.html", "agri-gunlugu.html"],
    "agriyi-anlamak.html": ["egzersizde-agri.html", "bel-agrisi.html", "fibromiyalji.html"],
    "hareket-atistirmaliklari.html": ["hareket.html", "masa-basi.html", "bel-boy-orani.html"],
    "denge-testi.html": ["dusme-onleme.html", "otur-kalk-testi.html", "sandalye-testi.html", "dort-asamali-denge-testi.html"],
    "kas-gevsetme.html": ["ic-cekis.html", "uyku.html"],
    "ruh-hali-olcumu.html": ["ruh-sagligi-egzersiz.html", "ic-cekis.html"],
    "ruh-sagligi-egzersiz.html": ["stres.html", "ic-cekis.html", "ruh-hali-olcumu.html"],
    "bilgi.html": [],
}
def more(current):
    if current == "bilgi.html":
        return ""
    rel = RELATED.get(current, [])
    cards = "\n".join(f'<a href="{h}"><span class="k">{TOPICS[h][0]}</span><span class="t">{TOPICS[h][1]}</span></a>'
                      for h in rel)
    if current != "bilgi.html":
        cards += '\n<a href="bilgi.html"><span class="k">Bilgi köşesi</span><span class="t">Tüm konular</span></a>'
    return f'''<section>
    <div class="wrap">
      <p class="eyebrow" style="margin-bottom:14px">Bilgi köşesinden</p>
      <div class="more">
{cards}
<a href="index.html"><span class="k">Ana sayfa</span><span class="t">Evde fizyoterapi hizmeti</span></a>
      </div>
    </div>
  </section>'''

SITE = "https://drihsaneren.com/"
def page(fname, title, desc, current, head_extra_css, body, script="", seo_title=None, condition=None, about=None, faq_items=None):
    full_title = seo_title or f"{title} | İhsan Eren"
    ldj = ""
    if MODE == "github" and (condition or about):
        ldj = schema(fname, full_title, desc, about if about is not None else cond(condition), faq_items)
    faq_css = FAQ_CSS if '<div class="faq">' in body else ""
    seo = ""
    if MODE == "github":
        seo = (f'<link rel="canonical" href="{SITE}{fname}">\n'
               f'<meta property="og:type" content="article">\n'
               f'<meta property="og:title" content="{full_title}">\n'
               f'<meta property="og:description" content="{desc}">\n'
               f'<meta property="og:image" content="{SITE}logo.png">\n'
               f'<meta property="og:locale" content="tr_TR">\n'
               f'<meta property="og:url" content="{SITE}{fname}">\n'
               f'<meta name="twitter:card" content="summary_large_image">\n'
               f'<meta name="twitter:title" content="{full_title}">\n'
               f'<meta name="twitter:description" content="{desc}">\n'
               f'<meta name="twitter:image" content="{SITE}logo.png">\n'
               + hreflang(fname))
    html = f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="color-scheme" content="dark">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" href="{IMG}logo.png">
{CORE_CSS}{seo}{FONTS}
<meta name="theme-color" content="#1c2819">
<style>
{("  " + FONTFACE + CSS) if FONTFACE else CSS.lstrip(chr(10))}{LANG_CSS}{SEARCH_CSS}{FAB_CSS}{faq_css}{head_extra_css}
</style>
{ldj}</head>
<body>
{bar(current)}
{body}
{more(current)}
<footer>
  <div class="wrap">
    <p>© 2026 İhsan Eren · drihsaneren.com</p>
    <p>Bu sayfa bilgilendirme amaçlıdır; muayene ve tedavinin yerini tutmaz.</p>
  </div>
</footer>
{fab_html(WA)}{script}
{SEARCH_TAG}{CORE_JS}</body>
</html>
'''
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)

# ------------------------------------------------------------------ STRES

SP_ID = "37i9dQZF1E8LKe7RHlcpxG"
SP_URL = "https://open.spotify.com/playlist/" + SP_ID
SP_NOTE = '<svg viewBox="0 0 24 24" fill="none" stroke="#1c2819" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>'
if MODE == "artifact":
    SP_BOX = f'<a class="spx" href="{SP_URL}" target="_blank" rel="noopener"><span class="play">{SP_NOTE}</span><span class="vt"><b>Nuvole Bianche Radio</b><br>Spotify’da aç</span></a>'
else:
    SP_BOX = f'<button type="button" class="spx" data-sp="{SP_ID}" aria-label="Spotify çalma listesini yükle"><span class="play">{SP_NOTE}</span><span class="vt"><b>Nuvole Bianche Radio</b><br>Çalma listesini yükle</span></button>'

STRES_CSS = """
  .breath{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);column-gap:32px;align-content:start;
    grid-template-areas:"intro orb" "modes orb" "ctl orb" "note orb";grid-template-rows:auto auto auto 1fr}
  .b-intro{grid-area:intro} .b-modes{grid-area:modes} .b-ctl{grid-area:ctl} .b-note{grid-area:note;margin-top:14px}
  .breath .orb{grid-area:orb;align-self:center}
  @media (max-width:720px){
    .breath{grid-template-columns:1fr;grid-template-areas:"intro" "modes" "orb" "ctl" "note";grid-template-rows:none}
    .breath .orb{width:min(260px,72vw);margin:14px auto 18px}
  }
  [hidden]{display:none!important}
  .orb{position:relative;width:min(320px,80vw);aspect-ratio:1/1;max-width:100%;margin:0 auto;display:grid;place-items:center}
  .orb .ring{position:absolute;inset:0;border-radius:50%;border:1px solid var(--line-strong);transition:border-color .4s,box-shadow .4s}
  .orb.hold .ring{border-color:var(--gold);box-shadow:0 0 0 6px rgba(226,171,71,.12)}
  .orb .ball{width:100%;height:100%;border-radius:50%;
    background:radial-gradient(circle at 40% 35%, rgba(226,171,71,.55), rgba(143,164,118,.35) 55%, rgba(143,164,118,.08) 75%);
    transform:scale(.5);transition:transform 1s ease-in-out;will-change:transform}
  .modes{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0 6px}
  .modes button{all:unset;cursor:pointer;padding:8px 14px;border-radius:999px;border:1px solid var(--line-strong);font-size:14px;color:var(--ink-soft);font-variant-numeric:tabular-nums}
  .modes button:hover{border-color:var(--foil);color:var(--ink)}
  .modes button[aria-pressed="true"]{background:var(--foil);border-color:var(--foil);color:var(--ground);font-weight:600}
  .modes button:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
  .steps-mini{font-size:14px;color:var(--muted);margin:0 0 14px}
  .orb .say{position:absolute;inset:0;display:grid;place-content:center;text-align:center;pointer-events:none}
  .orb .say b{font-family:var(--display);font-weight:400;font-size:clamp(24px,4vw,30px);color:var(--ink)}
  .orb .say span{font-size:14px;color:var(--ink-soft);font-variant-numeric:tabular-nums}
  .controls{display:flex;flex-wrap:wrap;gap:10px;margin-top:6px}
  button.cta{font:inherit;font-weight:600;font-size:15px;cursor:pointer}
  .count{font-size:14px;color:var(--muted);margin-top:10px;font-variant-numeric:tabular-nums}


  .music{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:32px;align-items:center}
  @media (max-width:760px){.music{grid-template-columns:1fr;gap:18px}}
  .sp{position:relative;height:152px;max-width:100%;border-radius:12px;overflow:hidden;border:1px solid var(--line);
    background:radial-gradient(120% 90% at 70% 20%, rgba(226,171,71,.18), transparent 60%),#152012}
  .spx{all:unset;cursor:pointer;position:absolute;inset:0;display:grid;grid-auto-flow:column;place-content:center;align-items:center;gap:16px;text-align:left;padding:16px}
  .spx .play{width:64px;height:64px;border-radius:50%;background:var(--foil);display:grid;place-items:center;transition:transform .2s}
  .spx .play svg{width:26px;height:26px}
  .spx:hover .play{transform:scale(1.06)}
  .spx:focus-visible{outline:2px solid var(--gold);outline-offset:-4px}
  .spx .vt{font-size:14px;color:var(--ink-soft)}
  .spx .vt b{font-family:var(--display);font-weight:400;font-size:20px;color:var(--ink)}
  .sp iframe{position:absolute;inset:0;display:block;width:100%;height:152px;border:0;border-radius:12px;background:transparent;color-scheme:normal}
  .sp.on{border:0;background:transparent;color-scheme:normal}
  .ext{font-size:13px;color:var(--muted)}
  .ext:hover{color:var(--foil)}
  .skills{list-style:none;margin:0;padding:0;display:grid;gap:0;counter-reset:s}
  .skills > li{display:grid;grid-template-columns:44px minmax(0,1fr);gap:16px;padding-block:24px;border-top:1px solid var(--line)}
  .skills > li:last-child{border-bottom:1px solid var(--line)}
  .num{width:34px;height:34px;border-radius:50%;border:1px solid var(--foil);color:var(--foil);display:grid;place-items:center;font-family:var(--display);font-size:17px;line-height:1;margin-top:2px}
  .skills p{color:var(--ink-soft)}
  .steps{margin:10px 0 0;padding:0;list-style:none;display:grid;gap:10px;max-width:65ch}
  .steps li{display:grid;grid-template-columns:auto minmax(0,1fr);gap:10px;align-items:baseline}
  .steps .k{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--foil);font-weight:600;white-space:nowrap}
  .say-it{font-family:var(--display);color:var(--ink);font-size:19px}

  .res{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px;max-width:900px}
  .res a{display:grid;grid-template-columns:auto minmax(0,1fr);gap:14px;align-items:center;padding:18px;border:1px solid var(--line);border-radius:12px;background:var(--ground-2);text-decoration:none;color:var(--ink)}
  .res a:hover{border-color:var(--line-strong)}
  .res .ic{width:46px;height:46px;border-radius:12px;background:rgba(216,178,94,.14);display:grid;place-items:center;color:var(--foil)}
  .res .ic svg{width:24px;height:24px}
  .res b{display:block;font-weight:600}
  .res small{color:var(--muted);font-size:14px}
"""

STRES_HELP = ("Ne zaman destek almalı?", "Stres, kaygı ya da çökkünlük haftalardır uykunuzu, işinizi veya ilişkilerinizi etkiliyorsa bir hekime ya da ruh sağlığı uzmanına başvurun. Kendinize zarar verme düşünceleriniz varsa hemen <strong>112</strong>'yi arayın.")
STRES_FAQ = [
 ("Stres anında nefes egzersizi nasıl yapılır?", "Rahat bir yere oturun ve omuzlarınızı bırakın. Burnunuzdan 4 saniye nefes alın, 6 saniyede yavaşça verin. Bir tur 10 saniye sürer; 6 tur yaklaşık 1 dakikadır. Nefesi yavaşlatmak bedenin sakinleşmesine yardım eder."),
 ("Kutu nefesi ve 4-7-8 nefesi nasıl yapılır?", "Kutu nefesinde 4 saniye nefes alın, 4 saniye tutun, 4 saniye verin ve 4 saniye tutun. 4-7-8 tekniğinde burnunuzdan 4 saniye alın, 7 saniye tutun ve dudaklarınız hafif aralık, 8 saniyede verin. Tutma aşamalarını zorlamadan yapın; ciddi kalp ya da akciğer hastalığınız varsa tutmalı teknikleri doktorunuza danışın."),
 ("Nefes egzersizlerinin yararı kanıtlandı mı?", "785 yetişkini kapsayan randomize çalışmaların 2023 tarihli bir meta-analizinde nefes çalışmaları, stres, kaygı ve depresif belirtilerde küçük ile orta düzeyde azalma sağladı. Çalışmaların yanlılık riski orta düzeydeydi; daha iyi tasarlanmış araştırmalara ihtiyaç var."),
 ("Dünya Sağlık Örgütü'nün stres rehberindeki beş beceri nedir?", "Ayağınızı yere basmak, zor düşüncelerden sıyrılmak, değerlerinize göre davranmak, kendinize nazik olmak ve duygulara yer açmaktır. Amaç stresi tamamen yok etmek değil, zor duygular varken de sizin için önemli olana dönebilmektir."),
]
STRES_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Stresli anlarda ne yapabilirsiniz?</h1>
    <p class="lede">Dünya Sağlık Örgütü'nün herkes için hazırladığı resimli rehberden uyarlanmış, günde birkaç dakikanızı alan beş beceri ve bir nefes egzersizi.</p>
    <p class="meta">Son güncelleme: {UPDATED}</p>
  </div>
</header>

<main>
  <section id="nefes">
    <div class="wrap">
      <div class="breath">
        <div class="b-intro">
          <p class="eyebrow">Hemen deneyin</p>
          <h2>Nefes egzersizi</h2>
          <p class="soft">Nefesi yavaşlatmak bedenin sakinleşmesine yardım eder. Rahat bir yere oturun, omuzlarınızı bırakın. Çember büyürken burnunuzdan nefes alın, küçülürken yavaşça verin. Çemberin kenarı altın rengine döndüğünde nefesinizi tutun.</p>
        </div>
        <div class="b-modes">
          <div class="modes" role="group" aria-label="Nefes temposu">
            <button type="button" data-m="46" aria-pressed="true">Sakin · 4-6</button>
            <button type="button" data-m="kutu" aria-pressed="false">Kutu · 4-4-4-4</button>
            <button type="button" data-m="478" aria-pressed="false">4-7-8</button>
          </div>
          <p class="steps-mini" id="b-desc">4 saniye alın, 6 saniye verin. Tutma yok. İstediğiniz kadar sürdürebilirsiniz.</p>
        </div>
        <div class="b-ctl">
          <div class="controls">
            <button type="button" class="cta" id="b-start">Başlat</button>
            <button type="button" class="cta ghost" id="b-stop" hidden>Durdur</button>
          </div>
          <p class="count" id="b-count" aria-live="polite">Bir tur 10 saniye. 6 tur yaklaşık 1 dakika sürer.</p>
        </div>
        <p class="count b-note">Tutma aşamalarını zorlamadan yapın. Başınız döner ya da nefesiniz daralırsa Sakin tempoya ya da normal nefesinize dönün. Ciddi kalp ya da akciğer hastalığınız varsa tutmalı teknikleri doktorunuza danışın.</p>
        <div class="orb" id="orb" aria-hidden="true">
          <div class="ring"></div>
          <div class="ball"></div>
          <div class="say"><b id="b-word">Hazır</b><span id="b-sec">Başlat'a basın</span></div>
        </div>
      </div>
    </div>
  </section>

  <section id="muzik">
    <div class="wrap music">
      <div>
        <p class="eyebrow">Müzik</p>
        <h2>Haftaya sakin, klasik bir başlangıç</h2>
        <p class="soft">Kahve eşliğinde kendinize yönelmek için: Ludovico Einaudi’nin <em>Nuvole Bianche</em>’si ve benzeri sakin piyano eserlerinden oluşan bir Spotify listesi. Nefes egzersizinden önce ya da sonra arka planda açabilirsiniz.</p>
        <p class="meta">Liste Spotify’dan yüklenir. Spotify’a giriş yapmamış dinleyiciler parçaların kısa önizlemelerini duyabilir.</p>
      </div>
      <div class="sp">{SP_BOX}</div>
    </div>
  </section>

  <section id="beceriler">
    <div class="wrap col">
      <p class="eyebrow">Beş beceri</p>
      <h2>Zor anlar için küçük araçlar</h2>
      <p class="soft">Bu becerilerin amacı stresi tamamen yok etmek değil. Amaç, zor duygular varken de ayağınızı yere basmanız ve sizin için önemli olana dönebilmeniz.</p>
      <ol class="skills">
        <li>
          <span class="num">1</span>
          <div>
            <h3>Ayağınızı yere basın</h3>
            <p>Duygular fırtına gibi geldiğinde, fırtına dinene kadar gemiyi demirlemek gibidir.</p>
            <ul class="steps">
              <li><span class="k">Fark edin</span><span>Şu an ne düşündüğünüzü ve ne hissettiğinizi sessizce fark edin.</span></li>
              <li><span class="k">Bedene dönün</span><span>Ayaklarınızı yere bastırın, sırtınızı dikleştirin, yavaşça nefes verin, omuzlarınızı esnetin.</span></li>
              <li><span class="k">Çevreye dönün</span><span>Etrafınızda gördüğünüz, duyduğunuz, dokunduğunuz şeyleri tek tek fark edin. Sonra yaptığınız işe geri dönün.</span></li>
            </ul>
          </div>
        </li>
        <li>
          <span class="num">2</span>
          <div>
            <h3>Zor düşüncelerden sıyrılın</h3>
            <p>Zor düşünceler bizi bir olta gibi yakalayıp o anki hayatımızdan uzaklaştırır.</p>
            <ul class="steps">
              <li><span class="k">Fark edin</span><span>Bir düşüncenin sizi yakaladığını fark edin.</span></li>
              <li><span class="k">Adını koyun</span><span>İçinizden söyleyin: <span class="say-it">“Şu an zor bir düşünce fark ediyorum.”</span></span></li>
              <li><span class="k">Geri dönün</span><span>Dikkatinizi yaptığınız işe ve yanınızdaki insanlara yeniden verin.</span></li>
            </ul>
          </div>
        </li>
        <li>
          <span class="num">3</span>
          <div>
            <h3>Değerlerinize göre davranın</h3>
            <p>Koşulları her zaman değiştiremeyiz ama nasıl biri olmak istediğimizi seçebiliriz. Sizin için önemli olan ne: sabırlı, nazik, yardımsever olmak mı?</p>
            <ul class="steps">
              <li><span class="k">Bu hafta</span><span>Bu değeri gösteren küçük ve yapılabilir bir adım seçin. Bir arkadaşı aramak ya da bir komşuya yardım etmek gibi.</span></li>
            </ul>
          </div>
        </li>
        <li>
          <span class="num">4</span>
          <div>
            <h3>Kendinize nazik olun</h3>
            <p>Zor bir dönemden geçen bir arkadaşınıza nasıl davranırsanız kendinize de öyle davranın.</p>
            <ul class="steps">
              <li><span class="k">Dokunun</span><span>Bir elinizi nazikçe göğsünüze koyun, sıcaklığını hissedin.</span></li>
              <li><span class="k">Söyleyin</span><span><span class="say-it">“Bu gerçekten zor. Böyle hissetmekte yalnız değilim.”</span></span></li>
            </ul>
          </div>
        </li>
        <li>
          <span class="num">5</span>
          <div>
            <h3>Duygulara yer açın</h3>
            <p>Zor bir duyguyla savaşmak onu çoğu zaman büyütür. Onu bir süre yanınızda taşımayı deneyin.</p>
            <ul class="steps">
              <li><span class="k">Merak edin</span><span>Duyguyu bedeninizin neresinde hissediyorsunuz? Bir nesne olsaydı şekli, rengi, sıcaklığı nasıl olurdu?</span></li>
              <li><span class="k">Nefes verin</span><span>O bölgenin çevresine yavaşça nefes verin ve ona yer açın. Duygular gelip geçer.</span></li>
            </ul>
          </div>
        </li>
      </ol>
    </div>
  </section>

  <section id="sss">
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(STRES_FAQ)}
    </div>
  </section>

  <section id="kaynaklar">
    <div class="wrap">
      <p class="eyebrow">Ücretsiz Türkçe kaynaklar</p>
      <h2>Kitapçık ve sesli egzersizler</h2>
      <p class="soft">Rehberin tamamını ve sesli uygulamaları Dünya Sağlık Örgütü'nün sitesinden ücretsiz edinebilirsiniz. Ses kayıtları Türkçe dahil 20'den fazla dilde var.</p>
      <div class="res">
        <a href="https://apps.who.int/iris/handle/10665/333917" target="_blank" rel="noopener">
          <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5a2 2 0 0 1 2-2h10l4 4v12a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2z"/><path d="M15 3v5h5M8 13h8M8 17h5"/></svg></span>
          <span><b>Stresli Anlarda Ne Yapmalı?</b><small>Türkçe resimli kitapçık (PDF) · DSÖ, 2020</small></span>
        </a>
        <a href="https://who.canto.global/b/S7VEH" target="_blank" rel="noopener">
          <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="14" width="4" height="7" rx="1.5"/><rect x="17" y="14" width="4" height="7" rx="1.5"/></svg></span>
          <span><b>Türkçe sesli egzersizler</b><small>Rehberdeki uygulamaların ses kayıtları · DSÖ</small></span>
        </a>
        <a href="https://www.who.int/publications/i/item/9789240003927" target="_blank" rel="noopener">
          <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/></svg></span>
          <span><b>Diğer diller</b><small>Rehberin tüm dil seçenekleri · who.int</small></span>
        </a>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap col">
      <div class="note warn"><strong>{STRES_HELP[0]}</strong> {STRES_HELP[1]}</div>
      <div class="sources" style="margin-top:24px">
        <p class="eyebrow">Kaynaklar</p>
        <ol>
          <li>Cleveland Clinic. <a href="https://health.clevelandclinic.org/4-7-8-breathing" target="_blank" rel="noopener">How To Do the 4-7-8 Breathing Exercise</a>. Health Essentials.</li>
          <li>Cleveland Clinic. <a href="https://health.clevelandclinic.org/box-breathing-benefits" target="_blank" rel="noopener">How Box Breathing Can Help You Destress</a>. Health Essentials.</li>
          <li>Fincham GW, Strauss C, Montero-Marin J, Cavanagh K. <a href="https://www.nature.com/articles/s41598-022-27247-y" target="_blank" rel="noopener">Effect of breathwork on stress and mental health: a meta-analysis of randomised-controlled trials</a>. Sci Rep. 2023;13:432.</li>
          <li>World Health Organization. <a href="https://www.who.int/publications/i/item/9789240003927" target="_blank" rel="noopener">Doing What Matters in Times of Stress: An Illustrated Guide</a>. Geneva: WHO; 2020. Türkçesi: <a href="https://apps.who.int/iris/handle/10665/333917" target="_blank" rel="noopener">Stresli Anlarda Ne Yapmalı?: Resimli Rehber</a>. Lisans: CC BY-NC-SA 3.0 IGO.</li>
        </ol>
        <p style="margin-top:12px">Bu sayfa rehberdeki becerilerin kendi cümlelerimizle yazılmış kısa bir özetidir. Dünya Sağlık Örgütü bu sayfayı hazırlamamış ve onaylamamıştır. Nefes egzersizleri rehberin parçası değildir, genel gevşeme teknikleridir.</p>
      </div>
    </div>
  </section>
</main>'''

STRES_JS = '''<script>
(function(){
  var orb=document.getElementById('orb'), w=document.getElementById('b-word'), s=document.getElementById('b-sec'),
      start=document.getElementById('b-start'), stop=document.getElementById('b-stop'), cnt=document.getElementById('b-count');
  var ball=orb.querySelector('.ball'), desc=document.getElementById('b-desc');
  // [söz, saniye, çember: 1 büyü, 0 küçül, -1 tut]
  var MODES={
    '46':{ph:[['Nefes al',4,1],['Nefes ver',6,0]],max:0,
      d:'4 saniye alın, 6 saniye verin. Tutma yok. İstediğiniz kadar sürdürebilirsiniz.',
      c:'Bir tur 10 saniye. 6 tur yaklaşık 1 dakika sürer.'},
    'kutu':{ph:[['Nefes al',4,1],['Tut',4,-1],['Nefes ver',4,0],['Tut',4,-1]],max:0,
      d:'4 saniye alın, 4 tutun, 4 verin, 4 tutun. Hafifçe, zorlamadan. Günde 1–2 kez, 3–4 tur yeterli.',
      c:'Bir tur 16 saniye. 4 tur yaklaşık 1 dakika sürer.'},
    '478':{ph:[['Nefes al',4,1],['Tut',7,-1],['Nefes ver',8,0]],max:4,
      d:'Burnunuzdan 4 saniye alın, 7 saniye tutun, dudaklarınız hafif aralık, “fuuu” sesiyle 8 saniyede verin. Dilinizin ucu üst ön dişlerinizin arkasında dursun. Başlangıçta günde 2 kez, 3–4 tur.',
      c:'Bir tur 19 saniye. 4 turdan sonra kendiliğinden durur.'}
  };
  var mode='46', t=null, t0=0, rounds=0, cur=-1;
  function total(){return MODES[mode].ph.reduce(function(a,p){return a+p[1];},0);}
  function setBall(scale,sec){ball.style.transition='transform '+sec+'s ease-in-out'; ball.style.transform='scale('+scale+')';}
  function halt(msg){
    clearInterval(t); t=null; cur=-1; orb.classList.remove('hold'); setBall(.5,1);
    w.textContent='Hazır'; s.textContent="Başlat'a basın";
    if(msg){cnt.textContent=msg;}
    stop.hidden=true; start.hidden=false;
  }
  function tick(){
    var m=MODES[mode], T=total(), el=(Date.now()-t0)/1000, r=Math.floor(el/T), c=el-r*T;
    if(r!==rounds){rounds=r; cnt.textContent=rounds+' tur tamamlandı';}
    if(m.max && rounds>=m.max){halt(m.max+' tur tamamlandı. Normal nefesinize dönün.'); start.focus(); return;}
    var i=0, acc=0; while(i<m.ph.length-1 && c>=acc+m.ph[i][1]){acc+=m.ph[i][1]; i++;}
    var p=m.ph[i], key=r*10+i;
    if(key!==cur){
      cur=key; w.textContent=p[0];
      if(p[2]===1){orb.classList.remove('hold'); setBall(1,p[1]);}
      else if(p[2]===0){orb.classList.remove('hold'); setBall(.5,p[1]);}
      else{orb.classList.add('hold');}
    }
    s.textContent=Math.max(1,Math.ceil(acc+p[1]-c))+' sn';
  }
  start.addEventListener('click',function(){
    ball.style.transition='none'; ball.style.transform='scale(.5)'; void ball.offsetWidth;
    t0=Date.now(); rounds=0; cur=-1; cnt.textContent='Başladı'; tick(); clearInterval(t); t=setInterval(tick,100);
    start.hidden=true; stop.hidden=false; stop.focus();
  });
  Array.prototype.forEach.call(document.querySelectorAll('.modes button'),function(b){
    b.addEventListener('click',function(){
      var running=!!t; if(running){halt();}
      mode=b.dataset.m;
      Array.prototype.forEach.call(document.querySelectorAll('.modes button'),function(x){x.setAttribute('aria-pressed',x===b?'true':'false');});
      desc.textContent=MODES[mode].d; cnt.textContent=MODES[mode].c;
      if(running){start.click();}
    });
  });
  var spb=document.querySelector('button.spx');
  if(spb){spb.addEventListener('click',function(){
    var f=document.createElement('iframe');
    f.src='https://open.spotify.com/embed/playlist/'+spb.dataset.sp+'?utm_source=generator&theme=0';
    f.title='Spotify çalma listesi: Nuvole Bianche Radio';
    f.allow='autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture';
    f.height='152'; f.style.colorScheme='normal'; spb.parentNode.classList.add('on'); spb.replaceWith(f);
  });}
  stop.addEventListener('click',function(){ halt(); start.focus(); });
})();
</script>'''

page("stres.html", "Stresli Anlarda", "Dünya Sağlık Örgütü rehberinden uyarlanmış beş beceri, nefes egzersizleri (4-6, kutu, 4-7-8) ve ücretsiz Türkçe kitapçık ve ses kayıtları.",
     "stres.html", STRES_CSS, STRES_BODY, STRES_JS, about=cond("Stres"), faq_items=STRES_FAQ + [STRES_HELP],
     seo_title="Stresli Anlarda Ne Yapmalı? Nefes Egzersizleri | İhsan Eren")

# ------------------------------------------------------------------ DONUK OMUZ

PLAYSVG = '<svg viewBox="0 0 24 24" fill="#1c2819"><path d="M7 4.5v15l13-7.5z"/></svg>'
def vbox(vid, label, title):
    url = "https://www.youtube.com/watch?v=" + vid
    if MODE == "artifact":
        inner = f'<a class="vlink" href="{url}" target="_blank" rel="noopener" aria-label="{label} (YouTube)"><span class="play">{PLAYSVG}</span><span class="vt">{title}</span></a>'
    else:
        inner = (f'<button type="button" data-yt="{vid}" aria-label="{label}">'
                 f'<img class="thumb" src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy">'
                 f'<span class="play">{PLAYSVG}</span></button>')
    return f'<div class="vbox">{inner}</div>'
VBOX_uKzCZcvi_m0 = vbox("uKzCZcvi-m0", "Donma evresi videosunu oynat", "Frozen Shoulder? Step-by-Step Exercise &amp; Pain Relief (Freezing Phase)")
VBOX_A8DWUzW3rbM = vbox("A8DWUzW3rbM", "Donmuş evre videosunu oynat", "Frozen Shoulder? Step-by-Step Exercise &amp; Pain Relief (Frozen Phase)")

def fig(inner, caption, h=120):
    return f'<figure class="an"><svg viewBox="0 0 120 {h}" aria-hidden="true">{inner}</svg><figcaption>{caption}</figcaption></figure>'

A = 'dur="3.2s" repeatCount="indefinite" calcMode="spline" keyTimes="0;0.5;1" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"'
EX = [
 ("Önce ısıtın", "Egzersizden önce omzunuza 10–15 dakika ılık bir havlu ya da sıcak su torbası koyun. Kaslar gevşer, hareketler daha rahat yapılır. Cildinizi korumak için arada ince bir bez bulundurun.", "Günde 1–2 kez, en fazla 20 dakika",
  fig('<line class="grd" x1="6" y1="112" x2="114" y2="112"/><circle class="hd" cx="60" cy="20" r="8"/>'
      '<path class="fig" d="M44 36 H76 M60 36 V78 M60 78 L52 112 M60 78 L68 112 M76 36 L80 60 L78 76"/>'
      '<path class="fig hl" d="M44 36 L40 60 L42 76"/>'
      '<rect x="34" y="28" width="20" height="14" rx="4" fill="#C8963E"/>'
      '<g fill="none" stroke="#C8963E" stroke-width="2.5" stroke-linecap="round"><path d="M36 22c-3-4 3-6 0-10"><animate attributeName="opacity" values="0;1;0" dur="2.4s" repeatCount="indefinite"/></path>'
      '<path d="M44 22c-3-4 3-6 0-10"><animate attributeName="opacity" values="0;1;0" dur="2.4s" begin="0.8s" repeatCount="indefinite"/></path>'
      '<path d="M52 22c-3-4 3-6 0-10"><animate attributeName="opacity" values="0;1;0" dur="2.4s" begin="1.6s" repeatCount="indefinite"/></path></g>', "Isıtma")),
 ("Sarkaç", "Sağlam elinizle bir masaya dayanın, öne eğilin. Ağrılı kolunuzu gevşekçe sarkıtın ve küçük daireler çizdirin. Kolu kasla değil, gövdenizin hafif sallanmasıyla hareket ettirin.", "10 tur saat yönünde, 10 tur tersine",
  fig('<line class="grd" x1="6" y1="112" x2="114" y2="112"/><path class="obj" d="M84 64 H114 M110 64 V112"/>'
      '<path class="fig" d="M50 72 L44 112 M50 72 L58 112"/><path class="fig" d="M50 72 L80 54"/><path class="fig" d="M80 54 L90 64"/>'
      '<circle class="hd" cx="90" cy="46" r="8"/>'
      f'<path class="fig hl" d="M78 56 L76 96"><animate attributeName="d" values="M78 56 L70 95;M78 56 L86 95;M78 56 L70 95" {A}/></path>', "Sarkaç")),
 ("Duvarda parmak yürüyüşü", "Duvara bir kol boyu uzaklıkta, yüzünüz duvara dönük durun. Parmaklarınızla duvarda örümcek gibi yukarı yürüyün, gerginlik hissettiğiniz yerde birkaç saniye bekleyin, yavaşça inin.", "10 tekrar, günde 1–2 kez",
  fig('<line class="grd" x1="6" y1="112" x2="114" y2="112"/><line class="obj" x1="98" y1="6" x2="98" y2="112" stroke-width="5"/>'
      '<path class="fig" d="M60 74 L56 112 M60 74 L66 112"/><path class="fig" d="M60 74 L62 42"/><circle class="hd" cx="64" cy="30" r="8"/>'
      f'<path class="fig hl" d="M62 44 L94 58"><animate attributeName="d" values="M62 44 L94 60;M62 44 L90 14;M62 44 L94 60" {A}/></path>', "Parmak yürüyüşü")),
 ("Havlu ile germe", "Bir havluyu sırtınızın arkasında iki elinizle tutun: sağlam kolunuz yukarıda, ağrılı kolunuz aşağıda. Sağlam kolunuzla havluyu yavaşça yukarı çekin, ağrılı kol sırt boyunca yukarı kaysın.", "10–20 saniye tutun, 5 tekrar",
  fig('<line class="grd" x1="6" y1="112" x2="114" y2="112"/><circle class="hd" cx="60" cy="22" r="8"/>'
      '<path class="fig" d="M44 38 H76 M60 38 V78 M60 78 L52 112 M60 78 L68 112"/>'
      '<path class="fig" d="M76 38 L84 20 L72 16"/>'
      f'<path class="band" d="M72 16 L48 74"><animate attributeName="d" values="M72 16 L48 76;M72 12 L50 62;M72 16 L48 76" {A}/></path>'
      f'<path class="fig hl" d="M44 38 L38 60 L48 74"><animate attributeName="d" values="M44 38 L38 62 L48 76;M44 38 L38 54 L50 62;M44 38 L38 62 L48 76" {A}/></path>', "Havlu ile germe")),
 ("Göğüs önünden çapraz germe", "Ağrılı kolunuzu göğsünüzün önünden karşı omza doğru uzatın. Diğer elinizle dirseğinizin üstünden hafifçe bastırarak kolu kendinize doğru çekin.", "15–20 saniye tutun, 5 tekrar",
  fig('<line class="grd" x1="6" y1="112" x2="114" y2="112"/><circle class="hd" cx="60" cy="20" r="8"/>'
      '<path class="fig" d="M44 36 H76 M60 36 V78 M60 78 L52 112 M60 78 L68 112"/>'
      f'<path class="fig hl" d="M44 36 L80 46"><animate attributeName="d" values="M44 36 L78 46;M44 36 L88 42;M44 36 L78 46" {A}/></path>'
      f'<path class="fig" d="M76 36 L82 58 L66 44"><animate attributeName="d" values="M76 36 L82 58 L64 44;M76 36 L84 56 L70 42;M76 36 L82 58 L64 44" {A}/></path>', "Çapraz germe")),
 ("Sopa ile dışa döndürme", "Sırtüstü yatın ya da ayakta durun. Ağrılı kolunuzun dirseği gövdenize yapışık ve 90 derece bükülü olsun. Bir sopayı iki elinizle tutun; sağlam kolunuzla sopayı iterek ağrılı kolun ön kolunu dışarı doğru çevirin.", "15–20 saniye tutun, 5 tekrar",
  fig('<line class="grd" x1="6" y1="112" x2="114" y2="112"/><circle class="hd" cx="60" cy="20" r="8"/>'
      '<path class="fig" d="M44 36 H76 M60 36 V78 M60 78 L52 112 M60 78 L68 112"/>'
      '<path class="fig hl" d="M44 36 L42 62"/>'
      f'<path class="fig hl" d="M42 62 L58 66"><animate attributeName="d" values="M42 62 L58 66;M42 62 L24 58;M42 62 L58 66" {A}/></path>'
      '<path class="fig" d="M76 36 L80 60 L72 68"/>'
      f'<path class="obj" d="M58 66 L72 68"><animate attributeName="d" values="M58 66 L72 68;M24 58 L72 68;M58 66 L72 68" {A}/></path>', "Dışa döndürme")),
]

OMUZ_CSS = """
  .stats{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin-top:4px}
  @media (max-width:760px){.stats{grid-template-columns:repeat(2,minmax(0,1fr))}}
  .stat{border:1px solid var(--line);border-radius:12px;padding:16px;background:var(--ground-2)}
  .stat b{display:block;font-family:var(--display);font-weight:400;font-size:clamp(26px,4vw,34px);color:var(--foil);line-height:1.1;font-variant-numeric:tabular-nums}
  .stat span{font-size:14px;color:var(--ink-soft)}
  .two{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:40px}
  @media (max-width:820px){.two{grid-template-columns:1fr;gap:10px}}

  .phases{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0;border:1px solid var(--line);border-radius:12px;overflow:hidden;margin-top:8px}
  @media (max-width:760px){.phases{grid-template-columns:1fr}}
  .ph{padding:18px;border-right:1px solid var(--line);display:grid;gap:8px;align-content:start}
  .ph:last-child{border-right:0}
  @media (max-width:760px){.ph{border-right:0;border-bottom:1px solid var(--line)}.ph:last-child{border-bottom:0}}
  .ph .bar2{height:6px;border-radius:3px}
  .ph:nth-child(1) .bar2{background:linear-gradient(90deg,#c96b5a,#e2ab47)}
  .ph:nth-child(2) .bar2{background:linear-gradient(90deg,#e2ab47,#b9b37a)}
  .ph:nth-child(3) .bar2{background:linear-gradient(90deg,#b9b37a,#8fa476)}
  .ph .k{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--foil);font-weight:600}
  .ph h3{margin:0}
  .ph .dur{font-variant-numeric:tabular-nums;color:var(--ink);font-weight:600;font-size:15px}
  .ph p{margin:0;color:var(--ink-soft);font-size:15px}

  .tx{list-style:none;margin:0;padding:0;display:grid;gap:0;max-width:820px}
  .tx li{display:grid;grid-template-columns:200px minmax(0,1fr);gap:18px;padding-block:14px;border-top:1px solid var(--line)}
  .tx li:last-child{border-bottom:1px solid var(--line)}
  @media (max-width:640px){.tx li{grid-template-columns:1fr;gap:2px}}
  .tx b{font-weight:600}
  .tx span{color:var(--ink-soft)}

  .ex{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px}
  .exc{display:grid;grid-template-rows:auto 1fr;border:1px solid var(--line);border-radius:12px;background:var(--ground-2);overflow:hidden}
  .exc .body{padding:14px 16px 16px;display:grid;gap:6px;align-content:start}
  .exc h3{font-size:19px;margin:0}
  .exc p{margin:0;font-size:15px;color:var(--ink-soft)}
  .exc .dose{font-size:13px;color:var(--foil);font-weight:600;letter-spacing:.02em}
  .an{margin:0;background:var(--paper);display:grid;justify-items:center;padding:10px 8px 8px;gap:2px}
  .an svg{width:100%;max-width:170px;height:auto;display:block}
  .an figcaption{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
  .an .fig{fill:none;stroke:#2A6F6B;stroke-width:5;stroke-linecap:round;stroke-linejoin:round}
  .an .fig.hl{stroke:#C8963E;stroke-width:6}
  .an .hd{fill:#2A6F6B}
  .an .grd{stroke:#B9CBC6;stroke-width:3;stroke-linecap:round}
  .an .obj{stroke:#8FA8A2;stroke-width:4;fill:none;stroke-linecap:round}
  .an .band{fill:none;stroke:#C8963E;stroke-width:3.5;stroke-linecap:round;stroke-dasharray:5 4}
  .vids{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
  @media (max-width:760px){.vids{grid-template-columns:1fr}}
  .vid{display:grid;gap:10px;align-content:start}
  .vbox{position:relative;aspect-ratio:16/9;max-width:100%;border-radius:12px;overflow:hidden;border:1px solid var(--line);
    background:radial-gradient(120% 90% at 30% 20%, rgba(143,164,118,.25), transparent 60%),#152012}
  .vbox button,.vbox .vlink{all:unset;cursor:pointer;position:absolute;inset:0;display:grid;place-content:center;justify-items:center;gap:10px;text-align:center;padding:16px}
  .vbox .play{width:64px;height:64px;border-radius:50%;background:var(--foil);display:grid;place-items:center;transition:transform .2s}
  .vbox .play svg{width:26px;height:26px;margin-left:4px}
  .vbox button:hover .play,.vbox .vlink:hover .play{transform:scale(1.06)}
  .ext{font-size:13px;color:var(--muted);justify-self:start}
  .ext:hover{color:var(--foil)}
  .vbox button:focus-visible,.vbox .vlink:focus-visible{outline:2px solid var(--gold);outline-offset:-4px}
  .vbox .vt{font-size:14px;color:var(--ink-soft);max-width:34ch}
  .vbox .thumb{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:brightness(.8);transition:filter .2s}
  .vbox button:hover .thumb{filter:brightness(.95)}
  .vbox .play{position:relative;z-index:1;box-shadow:0 6px 20px rgba(0,0,0,.35)}
  .vbox iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
  .vid h3{font-size:19px;margin:0}
  .vid p{margin:0;font-size:15px;color:var(--ink-soft)}
  .sources details{margin-top:6px}
  .sources summary{cursor:pointer;color:var(--ink-soft)}
  .sources ol ol{margin-top:8px;font-size:13px}
  .redflags{columns:2;column-gap:32px;max-width:820px}
  @media (max-width:640px){.redflags{columns:1}}
  .redflags li{break-inside:avoid}
"""

ex_cards = "\n".join(f'''<article class="exc">{svg}<div class="body"><h3>{t}</h3><p>{d}</p><span class="dose">{dose}</span></div></article>'''
                     for t, d, dose, svg in EX)

OMUZ_FAQ = [
 ("Donuk omuz kendiliğinden geçer mi?", "Çoğu zaman kendi seyrinde düzelir ama bu aylar, hatta yıllar sürebilir; hastalığın tipik süresi 1–3 yıldır. Bazı kişilerde hafif kısıtlılık uzun süre kalabilir. Doğru egzersiz ve tedaviyle bu süreci daha rahat geçirmek mümkündür."),
 ("Ağrılı omzumu hareket ettirmeli miyim?", "Evet, ama zorlamadan. Ağrılı evrede ağrısız aralıkta nazik hareketler, katılaşma evresinde germe ve eklem mobilizasyonu öne çıkar. Egzersizler hafif bir gerginlik hissi verecek kadar yapılır, keskin ağrıya kadar zorlanmaz."),
 ("Donuk omuz için MR gerekir mi?", "Tanı çoğunlukla muayeneyle konur: omuz hem sizin kaldırdığınızda hem de başkası kaldırdığında aynı şekilde kısıtlıdır. Röntgen, ultrason veya MR tanı için şart değildir ama kireçlenme ya da yırtık gibi başka nedenleri dışlamak için istenebilir."),
 ("Kortizon iğnesi işe yarar mı?", "Eklem içi kortizon iğnesi özellikle erken, ağrılı evrede ağrıyı birkaç hafta içinde belirgin azaltabilir. Etkisi daha çok kısa vadelidir ve hekim kararıyla yapılır. Tedavinin temeli ise fizyoterapi ve düzenli egzersizdir."),
]
OMUZ_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Donuk omuz (adeziv kapsülit)</h1>
    <p class="lede">Omzun önce ağrıdığı, sonra giderek kilitlendiği bir durum. Çoğu zaman kendi seyrinde düzelir ama bu aylar, hatta yıllar sürebilir. Doğru egzersiz ve tedaviyle bu süreci daha rahat geçirmek mümkün.</p>
    <p class="meta">Son güncelleme: {UPDATED}</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%2–5</b><span>Genel toplumda görülme sıklığı</span></div>
        <div class="stat"><b>40–60</b><span>En sık görüldüğü yaş aralığı</span></div>
        <div class="stat"><b>3–10 kat</b><span>Diyabetlilerde daha sık görülür</span></div>
        <div class="stat"><b>1–3 yıl</b><span>Hastalığın tipik süresi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Omuz eklemini saran kapsül adı verilen bağ dokusu kalınlaşır, iltihaplanır ve büzüşür. Eklem içindeki hareket alanı daralır. Sonuç: hem ağrı hem de kolu kaldırmada, arkaya götürmede ve dışa çevirmede belirgin kısıtlılık.</p>
        <p class="soft">En çok kolu dışa çevirme hareketi kısıtlanır. Saç taramak, ceket giymek, arkadan kopça ya da kemer bağlamak zorlaşır. Ağrı çoğunlukla geceleri artar ve o tarafa yatmak zorlaşır.</p>
      </div>
      <div>
        <h2>Kimlerde görülür?</h2>
        <ul class="dots">
          <li>40–60 yaş arası, kadınlarda daha sık</li>
          <li>Diyabeti olanlarda belirgin olarak daha sık ve daha uzun sürer</li>
          <li>Tiroid hastalıkları (az ya da çok çalışan tiroid)</li>
          <li>Ameliyat, kırık ya da yaralanma sonrası kolun uzun süre hareketsiz kalması</li>
          <li>İnme, Parkinson ve kalp hastalıkları</li>
        </ul>
        <p class="soft">Bir omuzda geçirenlerin bir kısmında yıllar içinde diğer omuzda da görülebilir.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Üç evre</h2>
      <p class="soft">Süreler kişiden kişiye değişir; diyabetlilerde genellikle daha uzundur.</p>
      <div class="phases">
        <div class="ph"><span class="bar2"></span><span class="k">1 · Donma</span><h3>Ağrılı evre</h3><span class="dur">Yaklaşık 2–9 ay</span><p>Ağrı giderek artar, özellikle geceleri. Hareket açıklığı azalmaya başlar.</p></div>
        <div class="ph"><span class="bar2"></span><span class="k">2 · Donmuş</span><h3>Katılaşma evresi</h3><span class="dur">Yaklaşık 4–12 ay</span><p>Ağrı azalabilir ama omuz belirgin şekilde katılaşır. Günlük işler en çok bu evrede zorlaşır.</p></div>
        <div class="ph"><span class="bar2"></span><span class="k">3 · Çözülme</span><h3>İyileşme evresi</h3><span class="dur">Yaklaşık 5–24 ay</span><p>Hareket yavaş yavaş geri gelir. Bazı kişilerde hafif kısıtlılık uzun süre kalabilir.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tanı ve tedavi</h2>
      <p class="soft">Tanı çoğunlukla muayeneyle konur: omuz hem sizin kaldırdığınızda hem de başkası kaldırdığında aynı şekilde kısıtlıdır. Röntgen, ultrason veya MR tanı için şart değildir ama kireçlenme ya da yırtık gibi başka nedenleri dışlamak için istenebilir.</p>
      <ul class="tx">
        <li><b>Fizyoterapi ve egzersiz</b><span>Tedavinin temelidir. Ağrılı evrede ağrısız aralıkta nazik hareketler, katılaşma evresinde germe ve eklem mobilizasyonu öne çıkar. Evde düzenli egzersiz çok önemlidir.</span></li>
        <li><b>Ağrı kontrolü</b><span>Sıcak uygulama ve hekiminizin önerdiği ağrı kesiciler, egzersizi yapılabilir kılar.</span></li>
        <li><b>Eklem içi kortizon iğnesi</b><span>Özellikle erken, ağrılı evrede ağrıyı birkaç hafta içinde belirgin azaltabilir. Etkisi daha çok kısa vadelidir; hekim kararıyla yapılır.</span></li>
        <li><b>Hidrodilatasyon</b><span>Eklem içine sıvı verilerek büzüşmüş kapsülün genişletilmesidir.</span></li>
        <li><b>Cerrahi seçenekler</b><span>Aylarca süren tedaviye yanıt alınamazsa narkoz altında manipülasyon ya da kapalı (artroskopik) kapsül gevşetme düşünülebilir.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Isınma ve sık kullanılan beş egzersiz</h2>
      <p class="soft">Bu egzersizler hafif bir gerginlik hissi verecek kadar yapılır, keskin ağrıya kadar zorlanmaz. Ağrılı evrede dozu düşük tutun. Hangi egzersizin sizin evrenize uygun olduğunu fizyoterapistinizle belirleyin.</p>
      <div class="ex">
{ex_cards}
      </div>
    </div>
  </section>


  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Evreye göre egzersiz videoları</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından, donuk omzun evrelerine göre adım adım egzersiz programları. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {VBOX_uKzCZcvi_m0}
          <h3>1. evre: Donma (ağrılı dönem)</h3>
          <p>Ağrıyı artırmadan hareketi korumaya yönelik nazik egzersizler.</p>
        </div>
        <div class="vid">
          {VBOX_A8DWUzW3rbM}
          <h3>2. evre: Donmuş (katılaşma dönemi)</h3>
          <p>Hareket açıklığını artırmaya yönelik germe ve mobilizasyon egzersizleri.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(OMUZ_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Omuz ağrısı her zaman donuk omuz değildir. Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Ağrı bir düşme ya da darbeden sonra başladıysa</li>
        <li>Kolda ani güç kaybı, uyuşma ya da karıncalanma varsa</li>
        <li>Omuzda kızarıklık, şişlik ve ateş varsa</li>
        <li>Nedensiz kilo kaybı ya da dinlenmekle geçmeyen şiddetli gece ağrısı varsa</li>
        <li>Özellikle sol omuz ağrısına göğüs ağrısı, nefes darlığı ya da terleme eşlik ediyorsa (kalp kaynaklı olabilir, <strong>112</strong>'yi arayın)</li>
      </ul>
      {CTA_CARD("Donuk omzunuz", "donuk omuz")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      <ol>
        <li>American Academy of Orthopaedic Surgeons. <a href="https://www.orthoinfo.org/diseases--conditions/frozen-shoulder" target="_blank" rel="noopener">Frozen Shoulder</a>. OrthoInfo.</li>
        <li>Bal A, Eksioglu E, Gulec B, Aydog E, Gurcay E, Cakci A. Effectiveness of corticosteroid injection in adhesive capsulitis. Clin Rehabil. 2008;22:503-512.</li>
        <li>Boyles RE, Flynn TW, Whitman JM. Manipulation following regional interscalene anesthetic block for shoulder adhesive capsulitis: a case series. Man Ther. 2005;10:164-171.</li>
        <li>Chen M-H, Chen W-S. <a href="https://www.mdpi.com/2077-0383/13/19/5696" target="_blank" rel="noopener">A narrative review of adhesive capsulitis with diabetes</a>. J Clin Med. 2024;13(19):5696.</li>
        <li>Cleland J, Durall CJ. Physical therapy for adhesive capsulitis: systematic review. Physiotherapy. 2002;88:450-457.</li>
        <li>Dias R, Cutts S, Massoud S. Frozen shoulder. BMJ. 2005;331:1453-1456.</li>
        <li>Gaspar PD, Willis FB. Adhesive capsulitis and dynamic splinting: a controlled, cohort study. BMC Musculoskelet Disord. 2009;10:111.</li>
        <li>Hakim AJ, Cherkas LF, Spector TD, MacGregor AJ. Genetic associations between frozen shoulder and tennis elbow: a female twin study. Rheumatology (Oxford). 2003;42:739-742.</li>
        <li>Kelley MJ, McClure PW, Leggin BG. Frozen shoulder: evidence and a proposed model guiding rehabilitation. J Orthop Sports Phys Ther. 2009;39:135-148.</li>
        <li>NHS. <a href="https://www.nhs.uk/conditions/frozen-shoulder/" target="_blank" rel="noopener">Frozen shoulder</a>.</li>
        <li>Physiopedia. <a href="https://www.physio-pedia.com/Adhesive_Capsulitis" target="_blank" rel="noopener">Frozen Shoulder</a>.</li>
        <li>Vermeulen HM, Rozing PM, Obermann WR, le Cessie S, Vliet Vlieland TP. Comparison of high-grade and low-grade mobilization techniques in the management of adhesive capsulitis of the shoulder: randomized controlled trial. Phys Ther. 2006;86:355-368.</li>
        <li>Walmsley S, Rivett DA, Osmotherly PG. Adhesive capsulitis: establishing consensus on clinical identifiers for stage 1 using the Delphi technique. Phys Ther. 2009;89:906-917.</li>
      </ol>
    </div>
  </section>
</main>'''

YT_JS = """<script>
document.querySelectorAll('.vbox button[data-yt]').forEach(function(b){
  b.addEventListener('click', function(){
    var f = document.createElement('iframe');
    var L = document.documentElement.lang === 'en' ? 'en' : 'tr';
    f.src = 'https://www.youtube-nocookie.com/embed/' + b.dataset.yt + '?autoplay=1&rel=0&hl=' + L + '&cc_lang_pref=' + L;
    f.title = b.getAttribute('aria-label').replace(/ oynat$/, '').replace(/^Play (the )?/, '');
    f.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
    f.allowFullscreen = true; f.loading = 'lazy'; f.referrerPolicy = 'strict-origin-when-cross-origin';
    b.replaceWith(f);
  });
});
</script>"""
page("donuk-omuz.html", "Donuk Omuz", "Donuk omuz (adeziv kapsülit) nedir, kimlerde görülür, evreleri, tedavi seçenekleri, evde yapılabilecek egzersizler ve videolar.",
     "donuk-omuz.html", OMUZ_CSS, OMUZ_BODY, YT_JS,
     seo_title="Donuk Omuz: Belirtiler, Evreler ve Egzersizler | İhsan Eren", condition="Donuk omuz (adeziv kapsülit)", about=cond("Donuk omuz (adeziv kapsülit)", "frozen-shoulder"),
     faq_items=OMUZ_FAQ)

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "neck_part.py"), encoding="utf-8").read())
for _p in ("lowback_part.py", "knee_part.py", "stroke_part.py", "heel_part.py", "shoulder_part.py", "cts_part.py", "falls_part.py", "protez_part.py", "desk_part.py", "hip_part.py", "elbow_part.py", "osteo_part.py", "ankle_part.py", "self_part.py", "rehab_part.py", "cond2_part.py", "cond3_part.py", "cond4_part.py", "cond5_part.py", "cond6_part.py", "cond7_part.py", "cond8_part.py", "cond9_part.py", "cond10_part.py", "cond11_part.py", "cond12_part.py", "cond13_part.py", "cond14_part.py", "cond15_part.py", "cond16_part.py", "cond17_part.py", "cond18_part.py", "cond19_part.py", "cond20_part.py", "cond21_part.py", "cond22_part.py", "cond23_part.py", "cond24_part.py", "cond25_part.py", "cond26_part.py", "cond27_part.py", "cond28_part.py", "cond29_part.py", "cond30_part.py", "cond31_part.py", "cond32_part.py", "cond33_part.py", "cond34_part.py", "cond35_part.py", "cond36_part.py", "cond37_part.py", "cond38_part.py", "cond39_part.py", "cond40_part.py", "cond41_part.py", "cond42_part.py", "cond43_part.py", "cond44_part.py", "cond45_part.py", "cond46_part.py", "cond47_part.py", "cond48_part.py", "cond49_part.py", "cond50_part.py", "cond51_part.py", "cond52_part.py", "cond53_part.py", "cond54_part.py", "cond55_part.py", "cond56_part.py", "cond57_part.py", "cond58_part.py", "cond59_part.py", "cond60_part.py", "self2_part.py", "self3_part.py", "knee12_part.py", "mind_part.py", "kapi_part.py", "self4_part.py", "self5_part.py", "self6_part.py", "self7_part.py", "self8_part.py", "self9_part.py", "self10_part.py", "self11_part.py", "self12_part.py", "cond61_part.py", "cond62_part.py", "cond63_part.py", "self13_part.py", "cond64_part.py", "cond65_part.py", "cond66_part.py", "cond67_part.py", "cond68_part.py", "cond69_part.py", "self14_part.py", "cond70_part.py", "cond71_part.py", "cond72_part.py", "self15_part.py", "nobel_part.py"):
    exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), _p), encoding="utf-8").read())

# ------------------------------------------------------------------ YENİLİKLER
IL_BLOOD = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<circle cx="236" cy="86" r="62" fill="rgba(143,164,118,.12)"/>
<path d="M206 70c0-22 16-38 36-38 10 0 18 4 24 10 10 2 18 11 18 22 0 6-2 11-6 15 3 5 4 10 2 16-3 9-12 15-22 14-5 7-13 11-22 10-12-1-22-10-24-22-4-6-6-11-6-17z" fill="none" stroke="#8fa476" stroke-width="3"/>
<path d="M232 44c-4 10 2 16 10 18m10-18c6 8 2 18-6 22m-30 6c10-2 16 4 16 12m20 4c8-4 18-2 22 6m-50 8c6 2 10 8 8 16" fill="none" stroke="#8fa476" stroke-width="2.5" stroke-linecap="round"/>
<g transform="rotate(-24 96 96)"><rect x="80" y="28" width="32" height="118" rx="16" fill="rgba(236,229,207,.08)" stroke="#ece5cf" stroke-width="3"/>
<rect x="80" y="86" width="32" height="60" rx="16" fill="#b5483a"/><rect x="80" y="86" width="32" height="14" fill="#b5483a"/>
<rect x="74" y="22" width="44" height="12" rx="4" fill="#d8b25e"/></g>
<path d="M150 136c0-10 12-24 12-24s12 14 12 24a12 12 0 0 1-24 0z" fill="#b5483a"/>
<path d="M146 90h40" stroke="#d8b25e" stroke-width="3" stroke-dasharray="4 6" stroke-linecap="round"/></svg>'''

IL_SHUTTLE = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M150 0 C130 60 170 120 150 180" fill="none" stroke="#d8b25e" stroke-width="4" stroke-dasharray="10 8"/>
<text x="46" y="30" fill="#9fab90" font-family="Figtree,sans-serif" font-size="12" letter-spacing="1.5">KAN</text>
<text x="222" y="30" fill="#9fab90" font-family="Figtree,sans-serif" font-size="12" letter-spacing="1.5">BEYİN</text>
<g fill="none" stroke="#ece5cf" stroke-width="3"><path d="M44 96h56"/><path d="M84 84l16 12-16 12"/></g>
<rect x="30" y="80" width="30" height="32" rx="8" fill="#d8b25e"/>
<g fill="#8fa476" opacity=".9"><circle cx="220" cy="70" r="10"/><circle cx="244" cy="98" r="13"/><circle cx="212" cy="118" r="9"/><circle cx="270" cy="68" r="8"/><circle cx="276" cy="126" r="11"/></g>
<g fill="none" stroke="#d8b25e" stroke-width="3"><path d="M180 96h26"/><path d="M196 88l10 8-10 8"/></g>
<rect x="160" y="84" width="22" height="24" rx="6" fill="#d8b25e"/></svg>'''

IL_DNA = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<g fill="none" stroke-width="4" stroke-linecap="round"><path d="M40 60 C80 20 120 20 160 60 S240 100 280 60" stroke="#8fa476"/><path d="M40 60 C80 100 120 100 160 60 S240 20 280 60" stroke="#ece5cf" opacity=".85"/></g>
<g stroke-width="3" stroke-linecap="round"><path d="M64 44v32M96 34v52M128 38v44M192 44v32M224 34v52M256 38v44" stroke="rgba(236,229,207,.35)"/><path d="M160 46v28" stroke="#e2ab47" stroke-width="5"/></g>
<circle cx="160" cy="60" r="18" fill="none" stroke="#e2ab47" stroke-width="2" stroke-dasharray="4 4"/>
<g transform="translate(160 132)"><circle r="26" fill="rgba(216,178,94,.14)"/><circle cy="-6" r="8" fill="#d8b25e"/><path d="M-12 14c2-10 22-10 24 0" fill="none" stroke="#d8b25e" stroke-width="4" stroke-linecap="round"/></g></svg>'''

IL_CRISPR = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<g fill="none" stroke-width="4" stroke-linecap="round"><path d="M20 70 C60 30 100 30 140 70 S220 110 260 70 S300 50 320 60" stroke="#8fa476"/><path d="M20 70 C60 110 100 110 140 70 S220 30 260 70 S300 90 320 80" stroke="#ece5cf" opacity=".85"/></g>
<g stroke="rgba(236,229,207,.35)" stroke-width="3" stroke-linecap="round"><path d="M44 54v32M76 44v52M108 48v44M172 54v32M204 44v52M236 48v44"/></g>
<g transform="translate(140 70) rotate(-30)"><circle cx="-22" cy="-10" r="9" fill="none" stroke="#e2ab47" stroke-width="4"/><circle cx="-22" cy="10" r="9" fill="none" stroke="#e2ab47" stroke-width="4"/><path d="M-14 -6 L22 8 M-14 6 L22 -8" stroke="#e2ab47" stroke-width="4" stroke-linecap="round"/></g>
<g transform="translate(96 142)"><ellipse rx="22" ry="14" fill="#b5483a"/><ellipse rx="9" ry="5" fill="#8f3328"/></g>
<g transform="translate(160 142)"><path d="M-24 6c10-22 38-22 48 0-12-8-36-8-48 0z" fill="#b5483a" opacity=".65"/></g>
<g transform="translate(224 142)"><ellipse rx="22" ry="14" fill="#b5483a"/><ellipse rx="9" ry="5" fill="#8f3328"/></g>
<path d="M186 142h14" stroke="#ece5cf" stroke-width="3" stroke-linecap="round"/><path d="M194 136l6 6-6 6" fill="none" stroke="#ece5cf" stroke-width="3" stroke-linecap="round"/></svg>'''

IL_PARK = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<circle cx="182" cy="96" r="64" fill="rgba(143,164,118,.12)"/>
<g transform="translate(-60 10)"><path d="M206 70c0-22 16-38 36-38 10 0 18 4 24 10 10 2 18 11 18 22 0 6-2 11-6 15 3 5 4 10 2 16-3 9-12 15-22 14-5 7-13 11-22 10-12-1-22-10-24-22-4-6-6-11-6-17z" fill="none" stroke="#8fa476" stroke-width="3"/>
<path d="M232 44c-4 10 2 16 10 18m10-18c6 8 2 18-6 22m-30 6c10-2 16 4 16 12m20 4c8-4 18-2 22 6m-50 8c6 2 10 8 8 16" fill="none" stroke="#8fa476" stroke-width="2.5" stroke-linecap="round"/></g>
<path d="M64 26 L174 94" stroke="#ece5cf" stroke-width="3" stroke-linecap="round"/>
<rect x="44" y="12" width="30" height="16" rx="4" transform="rotate(32 59 20)" fill="#d8b25e"/>
<g fill="#e2ab47"><circle cx="178" cy="97" r="5"/><circle cx="188" cy="92" r="4"/><circle cx="186" cy="103" r="4.5"/><circle cx="176" cy="107" r="3.5"/><circle cx="194" cy="100" r="3"/></g>
<circle cx="184" cy="99" r="20" fill="none" stroke="#e2ab47" stroke-width="2" stroke-dasharray="4 4"/>
<g fill="#8fa476"><circle cx="216" cy="78" r="3"/><circle cx="222" cy="112" r="2.5"/><circle cx="152" cy="126" r="3"/><circle cx="206" cy="136" r="2.5"/></g></svg>'''

IL_SPINE = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<g fill="#8fa476"><rect x="96" y="14" width="36" height="12" rx="4"/><rect x="96" y="30" width="36" height="12" rx="4"/><rect x="96" y="46" width="36" height="12" rx="4"/><rect x="96" y="62" width="36" height="12" rx="4"/><rect x="96" y="102" width="36" height="12" rx="4"/><rect x="96" y="118" width="36" height="12" rx="4"/><rect x="96" y="134" width="36" height="12" rx="4"/><rect x="96" y="150" width="36" height="12" rx="4"/></g>
<path d="M92 84l8 8 8-8 8 8 8-8 8 8 8-8" fill="none" stroke="#b5483a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<g fill="#d8b25e"><rect x="140" y="38" width="14" height="30" rx="3"/><rect x="140" y="112" width="14" height="30" rx="3"/></g>
<g fill="#223020"><circle cx="147" cy="46" r="2"/><circle cx="147" cy="53" r="2"/><circle cx="147" cy="60" r="2"/><circle cx="147" cy="120" r="2"/><circle cx="147" cy="127" r="2"/><circle cx="147" cy="134" r="2"/></g>
<path d="M158 127h12l6-10 8 20 8-20 6 10h16" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M158 53c24 0 40-10 58-22" fill="none" stroke="#ece5cf" stroke-width="2.5" stroke-dasharray="5 5" stroke-linecap="round" opacity=".8"/>
<path d="M252 60 L262 104 L250 146 L270 146" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="262" cy="104" r="12" fill="none" stroke="#e2ab47" stroke-width="2" stroke-dasharray="4 4"/>
<path d="M210 156h90" stroke="rgba(236,229,207,.35)" stroke-width="3" stroke-linecap="round"/></svg>'''

IL_GAIT = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M160 12v156" stroke="rgba(236,229,207,.3)" stroke-width="2" stroke-dasharray="6 6"/>
<g transform="translate(112 100)" fill="#8fa476"><ellipse cy="-10" rx="13" ry="21"/><ellipse cy="28" rx="10" ry="11"/><circle cx="7" cy="-39" r="5"/><circle cx="-2" cy="-41" r="4"/><circle cx="-9" cy="-38" r="3.5"/><circle cx="-14" cy="-33" r="3"/></g>
<g transform="translate(208 100) rotate(-16 0 28)"><g fill="none" stroke="#e2ab47" stroke-width="3"><ellipse cy="-10" rx="13" ry="21"/><ellipse cy="28" rx="10" ry="11"/></g><g fill="#e2ab47"><circle cx="-7" cy="-39" r="5"/><circle cx="2" cy="-41" r="4"/><circle cx="9" cy="-38" r="3.5"/><circle cx="14" cy="-33" r="3"/></g></g>
<path d="M246 64 A58 58 0 0 0 214 38" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round"/>
<path d="M222 32 L213 38 L223 43" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'''

IL_FORK = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<g fill="none" stroke="#8fa476" stroke-width="4" stroke-linecap="round"><path d="M48 90C92 90 100 50 138 50"/><path d="M48 90C92 90 100 130 138 130"/></g>
<g fill="none" stroke="#ece5cf" stroke-width="3" stroke-linecap="round" stroke-dasharray="6 6" opacity=".7"><path d="M184 50C224 50 230 90 266 90"/><path d="M184 130C224 130 230 90 266 90"/></g>
<circle cx="40" cy="90" r="8" fill="#d8b25e"/>
<g stroke="#e2ab47" stroke-linecap="round"><path d="M148 50h28" stroke-width="4"/><path d="M146 40v20M178 40v20" stroke-width="7"/></g>
<path d="M178 128a16 13 0 0 1-23 11l-9 4 3-8a16 13 0 1 1 29-7z" fill="none" stroke="#e2ab47" stroke-width="3.5" stroke-linejoin="round"/>
<circle cx="278" cy="90" r="14" fill="rgba(216,178,94,.18)" stroke="#d8b25e" stroke-width="3"/><path d="M271 90l5 5 9-10" fill="none" stroke="#d8b25e" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'''

IL_MAMMO = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<rect x="34" y="24" width="140" height="132" rx="10" fill="#152012" stroke="#8fa476" stroke-width="3"/>
<path d="M58 144C58 92 90 52 152 44V144Z" fill="rgba(236,229,207,.10)" stroke="rgba(236,229,207,.45)" stroke-width="2"/>
<circle cx="112" cy="98" r="7" fill="rgba(236,229,207,.6)"/>
<rect x="95" y="81" width="34" height="34" rx="3" fill="none" stroke="#e2ab47" stroke-width="3" stroke-dasharray="6 4"/>
<g stroke="rgba(143,164,118,.55)" stroke-width="1.5"><path d="M222 58L256 76M222 58L256 122M222 98L256 76M222 98L256 122M222 138L256 76M222 138L256 122M256 76L290 98M256 122L290 98"/></g>
<g fill="#8fa476"><circle cx="222" cy="58" r="6"/><circle cx="222" cy="98" r="6"/><circle cx="222" cy="138" r="6"/><circle cx="256" cy="76" r="6"/><circle cx="256" cy="122" r="6"/></g>
<circle cx="290" cy="98" r="8" fill="#e2ab47"/>
<path d="M212 98H134" stroke="#e2ab47" stroke-width="2.5" stroke-dasharray="4 5" stroke-linecap="round"/></svg>'''

IL_EAR = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<circle cx="150" cy="92" r="66" fill="rgba(143,164,118,.10)"/>
<path d="M156 36c-32 0-54 24-54 54 0 18 8 30 17 38 9 8 9 20 19 27 13 9 30 2 32-13 1-11-6-17-6-27 0-11 13-15 17-30 7-26-9-49-25-49z" fill="none" stroke="#8fa476" stroke-width="6" stroke-linejoin="round"/>
<path d="M136 90c0-15 11-26 24-24 11 2 15 13 11 22-4 9-15 9-15 20" fill="none" stroke="#8fa476" stroke-width="5" stroke-linecap="round"/>
<g fill="none" stroke="#e2ab47" stroke-width="4" stroke-linecap="round"><path d="M214 68a30 30 0 0 1 0 48"/><path d="M234 56a48 48 0 0 1 0 72" opacity=".75"/><path d="M254 44a66 66 0 0 1 0 96" opacity=".5"/></g>
<g fill="none" stroke-width="3" stroke-linecap="round"><path d="M34 150c10-14 20-14 30 0s20 14 30 0" stroke="#d8b25e"/><path d="M34 150c10 14 20 14 30 0s20-14 30 0" stroke="rgba(236,229,207,.6)"/></g></svg>'''

IL_KIDNEY = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M92 50c-28 0-42 22-42 48s14 48 42 48c16 0 24-10 20-22-3-9-12-13-12-26s9-17 12-26c4-12-4-22-20-22z" fill="rgba(226,171,71,.18)" stroke="#e2ab47" stroke-width="3.5"/>
<g transform="translate(320 0) scale(-1 1)"><path d="M92 50c-28 0-42 22-42 48s14 48 42 48c16 0 24-10 20-22-3-9-12-13-12-26s9-17 12-26c4-12-4-22-20-22z" fill="rgba(143,164,118,.25)" stroke="#8fa476" stroke-width="3.5"/></g>
<path d="M118 52C146 14 174 14 202 52" fill="none" stroke="#ece5cf" stroke-width="3" stroke-dasharray="6 6" stroke-linecap="round"/>
<path d="M192 46l10 6-2 11" fill="none" stroke="#ece5cf" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="52" cy="40" r="15" fill="#d8b25e"/><ellipse cx="52" cy="42" rx="8" ry="6" fill="#223020"/><circle cx="49" cy="42" r="1.8" fill="#d8b25e"/><circle cx="55" cy="42" r="1.8" fill="#d8b25e"/></svg>'''

IL_CART = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<g stroke="#e2ab47" stroke-width="3" stroke-linecap="round" fill="none"><path d="M110 50V36M110 130V144M70 90H56M150 90H164M82 62L72 52M138 62L148 52M82 118L72 128M138 118L148 128"/><path d="M104 32L110 36L116 32M104 148L110 144L116 148M52 84L56 90L52 96M168 84L164 90L168 96"/></g>
<circle cx="110" cy="90" r="36" fill="rgba(226,171,71,.2)" stroke="#e2ab47" stroke-width="3.5"/>
<circle cx="110" cy="90" r="13" fill="#e2ab47"/>
<g fill="rgba(143,164,118,.35)" stroke="#8fa476" stroke-width="3"><circle cx="232" cy="58" r="18"/><circle cx="252" cy="120" r="21"/><circle cx="206" cy="132" r="14"/></g>
<path d="M150 80L212 64" stroke="#e2ab47" stroke-width="2.5" stroke-dasharray="4 5" stroke-linecap="round"/>
<circle cx="232" cy="58" r="27" fill="none" stroke="#e2ab47" stroke-width="2" stroke-dasharray="4 4"/></svg>'''

IL_GAE = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<rect x="132" y="-14" width="62" height="92" rx="24" fill="rgba(236,229,207,.10)" stroke="#8fa476" stroke-width="3"/>
<rect x="136" y="96" width="54" height="96" rx="16" fill="rgba(236,229,207,.10)" stroke="#8fa476" stroke-width="3"/>
<g fill="none" stroke="#b5483a" stroke-width="3" stroke-linecap="round"><path d="M96 20C112 44 104 66 126 82S176 88 206 104"/><path d="M126 82C132 70 150 66 160 74"/><path d="M206 104C220 96 232 100 244 92"/></g>
<path d="M40 176C70 150 96 118 122 86" fill="none" stroke="#ece5cf" stroke-width="3" stroke-linecap="round" opacity=".85"/><circle cx="122" cy="86" r="4" fill="#ece5cf"/>
<g fill="#e2ab47"><circle cx="156" cy="72" r="3.5"/><circle cx="163" cy="76" r="3"/><circle cx="150" cy="68" r="2.5"/><circle cx="160" cy="68" r="2.5"/></g>
<circle cx="157" cy="72" r="15" fill="none" stroke="#e2ab47" stroke-width="2" stroke-dasharray="4 4"/></svg>'''

IL_VACCINE = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<g transform="rotate(-30 110 96)"><rect x="60" y="84" width="96" height="24" rx="5" fill="rgba(236,229,207,.12)" stroke="#ece5cf" stroke-width="3"/><rect x="62" y="86" width="52" height="20" rx="3" fill="rgba(226,171,71,.45)"/><path d="M156 96H186" stroke="#ece5cf" stroke-width="3" stroke-linecap="round"/><path d="M40 96H60M40 84V108" stroke="#d8b25e" stroke-width="5" stroke-linecap="round"/></g>
<path d="M52 150c10-12 20-12 30 0s20 12 30 0 20-12 30 0" fill="none" stroke="#8fa476" stroke-width="4" stroke-linecap="round"/>
<g fill="#8fa476"><circle cx="67" cy="150" r="3"/><circle cx="97" cy="150" r="3"/><circle cx="127" cy="150" r="3"/></g>
<path d="M236 54c22 0 40 16 40 38 0 24-20 42-42 40-24-2-40-18-38-42 2-20 18-36 40-36z" fill="rgba(181,72,58,.35)" stroke="#b5483a" stroke-width="3"/>
<circle cx="236" cy="92" r="46" fill="none" stroke="#e2ab47" stroke-width="2.5" stroke-dasharray="5 5"/>
<path d="M236 38v-12M236 158v-12M182 92h-12M302 92h-12" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>'''

IL_RUN = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M40 156H280" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/>
<circle cx="160" cy="34" r="12" fill="#8fa476"/>
<path d="M156 50L146 96M150 60L128 76L114 70M150 60L172 70L184 58M146 96L166 118L160 152M146 96L126 120L106 124" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M90 60h-26M96 84h-36M88 108h-22" stroke="rgba(236,229,207,.35)" stroke-width="3" stroke-linecap="round"/>
<path d="M238 64c-10-14-30-6-26 10 3 12 26 26 26 26s23-14 26-26c4-16-16-24-26-10z" fill="#e2ab47"/>
<path d="M214 118h48" stroke="#d8b25e" stroke-width="3" stroke-dasharray="4 5" stroke-linecap="round"/></svg>'''

IL_BCI = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M60 150V124c-14-8-22-24-22-44 0-32 26-54 56-54 28 0 50 20 50 48 0 8-2 14 2 20l10 14c2 4 0 8-4 8h-8v14c0 8-6 12-14 12h-16v22" fill="none" stroke="#8fa476" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
<rect x="82" y="36" width="24" height="16" rx="3" fill="#e2ab47"/><g fill="#223020"><circle cx="89" cy="44" r="1.8"/><circle cx="94" cy="44" r="1.8"/><circle cx="99" cy="44" r="1.8"/></g>
<path d="M106 44C150 30 176 48 196 72" fill="none" stroke="#e2ab47" stroke-width="2.5" stroke-dasharray="5 5" stroke-linecap="round"/>
<g fill="rgba(236,229,207,.14)" stroke="rgba(236,229,207,.45)" stroke-width="1.5"><rect x="196" y="84" width="18" height="16" rx="3"/><rect x="218" y="84" width="18" height="16" rx="3"/><rect x="262" y="84" width="18" height="16" rx="3"/><rect x="200" y="104" width="18" height="16" rx="3"/><rect x="222" y="104" width="18" height="16" rx="3"/><rect x="244" y="104" width="18" height="16" rx="3"/><rect x="266" y="104" width="18" height="16" rx="3"/><rect x="208" y="124" width="68" height="14" rx="3"/></g>
<rect x="240" y="84" width="18" height="16" rx="3" fill="#e2ab47"/>
<path d="M204 62h54" stroke="#ece5cf" stroke-width="3" stroke-linecap="round" opacity=".7"/><path d="M262 54v16" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>'''

IL_ISLET = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M50 104c0-26 30-38 60-36 26 2 44-14 72-14 34 0 58 18 58 40 0 24-26 34-52 30-22-4-40 14-72 12-36-2-66-8-66-32z" fill="rgba(143,164,118,.16)" stroke="#8fa476" stroke-width="3.5"/>
<g fill="#e2ab47"><circle cx="150" cy="90" r="7"/><circle cx="164" cy="84" r="6"/><circle cx="166" cy="98" r="6.5"/><circle cx="152" cy="104" r="5.5"/><circle cx="140" cy="96" r="5"/></g>
<circle cx="154" cy="94" r="24" fill="none" stroke="#e2ab47" stroke-width="2" stroke-dasharray="4 4"/>
<path d="M266 46c0 0 16 18 16 30a16 16 0 0 1-32 0c0-12 16-30 16-30z" fill="#b5483a"/>
<path d="M258 78l6 6 10-12" fill="none" stroke="#ece5cf" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'''

IL_HD = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<circle cx="232" cy="84" r="70" fill="rgba(143,164,118,.10)"/>
<g transform="translate(-110 -30) scale(1.4)"><path d="M206 70c0-22 16-38 36-38 10 0 18 4 24 10 10 2 18 11 18 22 0 6-2 11-6 15 3 5 4 10 2 16-3 9-12 15-22 14-5 7-13 11-22 10-12-1-22-10-24-22-4-6-6-11-6-17z" fill="none" stroke="#8fa476" stroke-width="2.2"/><path d="M232 44c-4 10 2 16 10 18m10-18c6 8 2 18-6 22m-30 6c10-2 16 4 16 12m20 4c8-4 18-2 22 6m-50 8c6 2 10 8 8 16" fill="none" stroke="#8fa476" stroke-width="1.8" stroke-linecap="round"/></g>
<path d="M64 22 L224 82" stroke="#ece5cf" stroke-width="3" stroke-linecap="round"/>
<rect x="44" y="10" width="30" height="16" rx="4" transform="rotate(20 59 18)" fill="#d8b25e"/>
<g fill="#e2ab47"><circle cx="230" cy="86" r="4.5"/><circle cx="238" cy="80" r="3.5"/><circle cx="238" cy="92" r="4"/><circle cx="224" cy="94" r="3"/></g>
<circle cx="232" cy="87" r="17" fill="none" stroke="#e2ab47" stroke-width="2" stroke-dasharray="4 4"/>
<polygon points="93.8,122.5 86.0,127.0 78.2,122.5 78.2,113.5 86.0,109.0 93.8,113.5" fill="rgba(143,164,118,.25)" stroke="#8fa476" stroke-width="2.5"/><polygon points="115.8,134.5 108.0,139.0 100.2,134.5 100.2,125.5 108.0,121.0 115.8,125.5" fill="rgba(143,164,118,.25)" stroke="#8fa476" stroke-width="2.5"/><polygon points="91.8,148.5 84.0,153.0 76.2,148.5 76.2,139.5 84.0,135.0 91.8,139.5" fill="rgba(143,164,118,.25)" stroke="#8fa476" stroke-width="2.5"/><polygon points="136.1,121.5 130.0,125.0 123.9,121.5 123.9,114.5 130.0,111.0 136.1,114.5" fill="rgba(143,164,118,.25)" stroke="#8fa476" stroke-width="2.5"/></svg>'''
IL_SLEEPST = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M44 26a16 16 0 1 0 14 24a13 13 0 1 1 -14 -24z" fill="#e2ab47"/>
<g fill="#ece5cf" opacity=".55"><circle cx="86" cy="22" r="1.8"/><circle cx="112" cy="40" r="1.4"/><circle cx="276" cy="24" r="1.8"/></g>
<g stroke="rgba(236,229,207,.12)" stroke-width="1"><path d="M70 52H290M70 76H290M70 104H290M70 132H290"/></g>
<path d="M70 52H86V104H104V132H130V104H146V76H164V104H182V132H196V104H214V76H240V104H256V76H284V52H290" fill="none" stroke="#8fa476" stroke-width="3" stroke-linejoin="round"/>
<g stroke="#e2ab47" stroke-width="6" stroke-linecap="round"><path d="M148 76H162M216 76H238M258 76H282"/></g>
<rect x="22" y="128" width="40" height="30" rx="9" fill="rgba(236,229,207,.10)" stroke="#ece5cf" stroke-width="2.5"/><path d="M30 128v-8h24v8M30 158v8h24v-8" fill="none" stroke="#8fa476" stroke-width="2.5"/>
<path d="M30 145h6l3-7 4 13 3-6h8" fill="none" stroke="#e2ab47" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'''
IL_NMJ = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<rect x="34" y="104" width="252" height="50" rx="25" fill="rgba(143,164,118,.22)" stroke="#8fa476" stroke-width="3"/>
<g stroke="rgba(143,164,118,.55)" stroke-width="2"><path d="M62 108v42M86 106v46M110 106v46M210 106v46M234 106v46M258 108v42"/></g>
<path d="M150 14C150 40 160 52 160 70" fill="none" stroke="#ece5cf" stroke-width="5" stroke-linecap="round"/>
<path d="M160 70C150 78 136 82 128 92M160 70C160 80 160 86 160 92M160 70C170 78 184 82 192 92" fill="none" stroke="#ece5cf" stroke-width="3.5" stroke-linecap="round"/>
<g fill="#ece5cf"><ellipse cx="128" cy="96" rx="7" ry="5"/><ellipse cx="160" cy="96" rx="7" ry="5"/><ellipse cx="192" cy="96" rx="7" ry="5"/></g>
<g fill="#e2ab47"><circle cx="128" cy="104" r="2.6"/><circle cx="160" cy="104" r="2.6"/><circle cx="154" cy="102" r="2"/><circle cx="166" cy="102" r="2"/></g>
<g fill="none" stroke="#e2ab47" stroke-width="2.5" stroke-linecap="round"><path d="M120 116l-8 10M136 116l8 10M152 116l-8 10M168 116l8 10"/></g>
<g fill="none" stroke="rgba(236,229,207,.35)" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="3 4"><path d="M192 108v14"/></g>
<path d="M200 118l10 10m0-10l-10 10" stroke="#c96b5a" stroke-width="3" stroke-linecap="round"/></svg>'''
IL_UPF = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<ellipse cx="190" cy="92" rx="88" ry="70" fill="rgba(236,229,207,.06)" stroke="rgba(236,229,207,.4)" stroke-width="2.5"/>
<path d="M126 96c0-30 20-54 44-58c18 10 24 34 12 56c-14 14-38 18-56 2z" fill="rgba(143,164,118,.45)" stroke="#8fa476" stroke-width="2.5"/>
<path d="M188 40c30 2 60 22 66 52c-14 10-40 10-58-4c-10-14-14-32-8-48z" fill="rgba(143,164,118,.45)" stroke="#8fa476" stroke-width="2.5"/>
<path d="M136 120c22 14 60 18 92 6c10 14 4 28-14 34c-30 8-62 2-82-14c-4-10-2-20 4-26z" fill="rgba(143,164,118,.45)" stroke="#8fa476" stroke-width="2.5"/>
<circle cx="190" cy="100" r="13" fill="#ece5cf"/>
<g stroke="#e2ab47" stroke-width="3" stroke-linecap="round"><path d="M142 78l14 6M150 64l12 4M206 60l14 10M224 76l12 4M160 136l18 2M196 142l16-2"/></g>
<rect x="30" y="56" width="46" height="62" rx="5" fill="rgba(236,229,207,.10)" stroke="#d8b25e" stroke-width="2.5"/><path d="M30 72h46M38 86h30M38 96h22M38 106h26" stroke="#d8b25e" stroke-width="2" stroke-linecap="round"/></svg>'''
IL_LACO = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M126 -6V54C126 74 140 84 160 84C180 84 194 74 194 54V-6" fill="rgba(236,229,207,.10)" stroke="#8fa476" stroke-width="3"/>
<path d="M126 186V124C126 108 140 100 160 100C180 100 194 108 194 124V186" fill="rgba(236,229,207,.10)" stroke="#8fa476" stroke-width="3"/>
<path d="M132 70C140 80 150 84 160 84C170 84 180 80 188 70" fill="none" stroke="#e2ab47" stroke-width="5" stroke-linecap="round"/>
<path d="M132 112C140 104 150 100 160 100C170 100 180 104 188 112" fill="none" stroke="#e2ab47" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="160" cy="92" rx="26" ry="6" fill="rgba(216,178,94,.35)"/>
<g fill="#e2ab47"><circle cx="146" cy="92" r="2"/><circle cx="160" cy="91" r="2"/><circle cx="174" cy="92" r="2"/></g>
<g transform="rotate(-24 262 70)"><rect x="236" y="62" width="62" height="16" rx="3" fill="rgba(236,229,207,.12)" stroke="#ece5cf" stroke-width="2.5"/><rect x="242" y="65" width="30" height="10" fill="rgba(216,178,94,.6)"/><path d="M298 70h12M310 62v16M236 70h-30" stroke="#ece5cf" stroke-width="2.5" stroke-linecap="round"/></g>
<g fill="none" stroke="#e2ab47" stroke-width="2" stroke-dasharray="3 4"><circle cx="160" cy="92" r="40"/></g></svg>'''
IL_TAVA = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M112 14C112 58 132 76 160 76C188 76 208 58 208 14" fill="rgba(143,164,118,.16)" stroke="#8fa476" stroke-width="3.5"/>
<path d="M86 152Q160 116 234 152" fill="none" stroke="#8fa476" stroke-width="4" stroke-linecap="round"/>
<g fill="none" stroke-width="3.5" stroke-linecap="round"><path d="M126 124v7a6 6 0 0 0 12 0v-7" stroke="#e2ab47"/><path d="M154 122v7a6 6 0 0 0 12 0v-7" stroke="rgba(236,229,207,.45)"/><path d="M182 124v7a6 6 0 0 0 12 0v-7" stroke="#e2ab47"/></g>
<g fill="#e2ab47"><circle cx="150" cy="96" r="4"/><circle cx="166" cy="102" r="3.5"/><circle cx="158" cy="110" r="3"/><circle cx="176" cy="92" r="3"/><circle cx="142" cy="108" r="3.5"/></g>
<g transform="rotate(-28 66.0 61.0)"><rect x="40" y="50" width="52" height="22" rx="11.0" fill="rgba(236,229,207,.10)" stroke="#ece5cf" stroke-width="2.5"/><path d="M66.0 50 H51.0 A11.0 11.0 0 0 0 51.0 72 H66.0 Z" fill="#d8b25e"/></g>
<path d="M96 78Q112 116 128 118" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5" stroke-linecap="round"/>
<circle cx="132" cy="128" r="16" fill="none" stroke="#e2ab47" stroke-width="2" stroke-dasharray="4 4"/><circle cx="188" cy="128" r="16" fill="none" stroke="#e2ab47" stroke-width="2" stroke-dasharray="4 4"/></svg>'''
IL_OREX = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M110 50a38 38 0 1 0 26 66a30 30 0 1 1 -26 -66z" fill="rgba(143,164,118,.35)" stroke="#8fa476" stroke-width="3"/>
<g fill="#ece5cf" opacity=".6"><circle cx="58" cy="44" r="2"/><circle cx="70" cy="132" r="2.5"/><circle cx="46" cy="96" r="1.8"/></g>
<circle cx="232" cy="84" r="22" fill="#e2ab47"/>
<g stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round"><path d="M232 48v-12M232 120v12M196 84h-12M268 84h12M207 59l-8-8M257 59l8-8M207 109l-8 8M257 109l8 8"/></g>
<path d="M130 40Q170 6 204 44" fill="none" stroke="#ece5cf" stroke-width="3" stroke-dasharray="6 6" stroke-linecap="round"/><path d="M194 40l10 5-2 11" fill="none" stroke="#ece5cf" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<g transform="rotate(0 164.0 144.0)"><rect x="136" y="132" width="56" height="24" rx="12.0" fill="rgba(236,229,207,.10)" stroke="#ece5cf" stroke-width="2.5"/><path d="M164.0 132 H148.0 A12.0 12.0 0 0 0 148.0 156 H164.0 Z" fill="#d8b25e"/></g></svg>'''
IL_RAS = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<g transform="translate(-14 22) scale(.86)"><path d="M50 104c0-26 30-38 60-36 26 2 44-14 72-14 34 0 58 18 58 40 0 24-26 34-52 30-22-4-40 14-72 12-36-2-66-8-66-32z" fill="rgba(143,164,118,.16)" stroke="#8fa476" stroke-width="3.5"/></g>
<circle cx="66" cy="112" r="13" fill="#b5483a"/><circle cx="66" cy="112" r="22" fill="none" stroke="#e2ab47" stroke-width="2" stroke-dasharray="4 4"/>
<rect x="222" y="52" width="66" height="32" rx="16" fill="rgba(236,229,207,.08)" stroke="#ece5cf" stroke-width="3"/><circle cx="239" cy="68" r="11" fill="#d8b25e"/>
<path d="M280 40H246" stroke="#ece5cf" stroke-width="3" stroke-linecap="round"/><path d="M254 34l-8 6 8 6" fill="none" stroke="#ece5cf" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<g transform="rotate(-18 254.0 123.0)"><rect x="226" y="112" width="56" height="22" rx="11.0" fill="rgba(236,229,207,.10)" stroke="#ece5cf" stroke-width="2.5"/><path d="M254.0 112 H237.0 A11.0 11.0 0 0 0 237.0 134 H254.0 Z" fill="#d8b25e"/></g>
<path d="M218 96C170 124 120 124 90 116" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5" stroke-linecap="round"/></svg>'''
IL_MCED = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<g transform="rotate(-18 86 96)"><rect x="70" y="30" width="32" height="118" rx="16" fill="rgba(236,229,207,.08)" stroke="#ece5cf" stroke-width="3"/><rect x="70" y="88" width="32" height="60" rx="16" fill="#b5483a"/><rect x="70" y="88" width="32" height="14" fill="#b5483a"/><rect x="64" y="24" width="44" height="12" rx="4" fill="#d8b25e"/></g>
<circle cx="232" cy="36" r="14" fill="none" stroke="#8fa476" stroke-width="3.5"/>
<rect x="202" y="56" width="60" height="100" rx="26" fill="rgba(143,164,118,.14)" stroke="#8fa476" stroke-width="3.5"/>
<g fill="#e2ab47"><circle cx="222" cy="82" r="5"/><circle cx="244" cy="88" r="5"/><circle cx="232" cy="110" r="5.5"/><circle cx="220" cy="128" r="4.5"/><circle cx="246" cy="132" r="4.5"/></g>
<circle cx="232" cy="110" r="14" fill="none" stroke="#e2ab47" stroke-width="2" stroke-dasharray="4 4"/>
<path d="M122 92H190" stroke="#d8b25e" stroke-width="3" stroke-dasharray="4 6" stroke-linecap="round"/><path d="M182 86l8 6-8 6" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'''
IL_LDL = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<g fill="none" stroke="#8fa476" stroke-width="4" stroke-linecap="round"><path d="M16 50C80 44 140 56 200 50S280 46 304 52"/><path d="M16 126C80 132 140 120 200 126S280 130 304 124"/></g>
<path d="M50 50Q76 82 104 49Z" fill="rgba(226,171,71,.55)" stroke="#e2ab47" stroke-width="2"/><path d="M60 128Q80 104 100 127Z" fill="rgba(226,171,71,.55)" stroke="#e2ab47" stroke-width="2"/>
<path d="M214 50Q226 60 238 50Z" fill="rgba(226,171,71,.45)" stroke="#e2ab47" stroke-width="2"/>
<g fill="#e2ab47"><circle cx="40" cy="92" r="5"/><circle cx="70" cy="100" r="5"/><circle cx="118" cy="84" r="5"/><circle cx="96" cy="110" r="4.5"/><circle cx="140" cy="100" r="4.5"/><circle cx="252" cy="90" r="4.5"/><circle cx="280" cy="104" r="4"/></g>
<path d="M160 88H224" stroke="#ece5cf" stroke-width="3" stroke-dasharray="5 6" stroke-linecap="round" opacity=".8"/><path d="M216 82l8 6-8 6" fill="none" stroke="#ece5cf" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" opacity=".8"/>
<g transform="rotate(0 158.0 158.0)"><rect x="128" y="146" width="60" height="24" rx="12.0" fill="rgba(236,229,207,.10)" stroke="#ece5cf" stroke-width="2.5"/><path d="M158.0 146 H140.0 A12.0 12.0 0 0 0 140.0 170 H158.0 Z" fill="#d8b25e"/></g></svg>'''
IL_BAX = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M84 64c-26 0-40 22-40 46s14 46 40 46c16 0 22-10 18-21-3-8-11-12-11-24s8-16 11-25c4-12-2-22-18-22z" fill="rgba(143,164,118,.25)" stroke="#8fa476" stroke-width="3.5"/>
<path d="M62 64L84 34L106 62Z" fill="rgba(226,171,71,.35)" stroke="#e2ab47" stroke-width="3" stroke-linejoin="round"/>
<circle cx="86" cy="50" r="24" fill="none" stroke="#ece5cf" stroke-width="3"/><path d="M69 67L103 33" stroke="#ece5cf" stroke-width="3" stroke-linecap="round"/>
<g fill="none" stroke-width="10"><path d="M172 124A60 60 0 0 1 202 72" stroke="#8fa476"/><path d="M202 72A60 60 0 0 1 262 72" stroke="#d8b25e"/><path d="M262 72A60 60 0 0 1 292 124" stroke="#b5483a"/></g>
<path d="M232 124L196 94" stroke="#ece5cf" stroke-width="4.5" stroke-linecap="round"/><circle cx="232" cy="124" r="8" fill="#ece5cf"/>
<path d="M258 56Q226 42 204 64" fill="none" stroke="#ece5cf" stroke-width="2.5" stroke-dasharray="4 5" stroke-linecap="round" opacity=".7"/>
<g transform="rotate(-20 151.0 139.0)"><rect x="126" y="128" width="50" height="22" rx="11.0" fill="rgba(236,229,207,.10)" stroke="#ece5cf" stroke-width="2.5"/><path d="M151.0 128 H137.0 A11.0 11.0 0 0 0 137.0 150 H151.0 Z" fill="#d8b25e"/></g></svg>'''
IL_ORFO = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<g transform="rotate(-18 95.0 95.0)"><rect x="40" y="74" width="110" height="42" rx="21.0" fill="rgba(236,229,207,.10)" stroke="#ece5cf" stroke-width="2.5"/><path d="M95.0 74 H61.0 A21.0 21.0 0 0 0 61.0 116 H95.0 Z" fill="#d8b25e"/></g>
<circle cx="160" cy="46" r="18" fill="none" stroke="#8fa476" stroke-width="3.5"/><path d="M160 36v10l8 5" fill="none" stroke="#8fa476" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M204 34V144H296" fill="none" stroke="rgba(236,229,207,.35)" stroke-width="3" stroke-linecap="round"/>
<path d="M214 52L234 66L254 88L274 104L292 110" fill="none" stroke="#e2ab47" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<g fill="#e2ab47"><circle cx="214" cy="52" r="5"/><circle cx="234" cy="66" r="4.5"/><circle cx="254" cy="88" r="4.5"/><circle cx="274" cy="104" r="4.5"/><circle cx="292" cy="110" r="5"/></g>
<path d="M214 136H292" stroke="#8fa476" stroke-width="2.5" stroke-dasharray="4 6" stroke-linecap="round"/></svg>'''
IL_RETA = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M104 10L138 90L118 170" fill="none" stroke="#8fa476" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="138" cy="90" r="10" fill="#d8b25e"/>
<g fill="none" stroke="#b5483a" stroke-width="3" stroke-linecap="round"><path d="M160 72a26 26 0 0 1 0 36" opacity=".8"/><path d="M172 62a40 40 0 0 1 0 56" opacity=".45"/><path d="M184 52a54 54 0 0 1 0 76" opacity=".2"/></g>
<rect x="212" y="112" width="84" height="40" rx="10" fill="rgba(236,229,207,.08)" stroke="#ece5cf" stroke-width="3"/>
<path d="M238 128a16 16 0 0 1 32 0" fill="none" stroke="#ece5cf" stroke-width="2.5"/><path d="M254 128L246 120" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/>
<path d="M254 28V88" stroke="#e2ab47" stroke-width="5" stroke-linecap="round"/><path d="M240 76l14 14 14-14" fill="none" stroke="#e2ab47" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'''

IL_PDACT = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 150 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<circle cx="96" cy="44" r="12" fill="#8fa476"/>
<path d="M96 58 L92 98 M94 66 L78 84 L82 98 M94 66 L112 80 L118 92 M92 98 L76 124 L64 148 M92 98 L108 124 L124 146" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M60 60 h-16 M58 76 h-22 M62 92 h-14" stroke="rgba(143,164,118,.6)" stroke-width="3" stroke-linecap="round"/>
<g fill="none" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="M170 70 L200 82 L230 96 L260 112 L286 126" stroke="rgba(181,72,58,.75)"/><path d="M170 70 L200 72 L230 75 L260 79 L286 82" stroke="#e2ab47"/></g>
<g fill="#e2ab47"><circle cx="170" cy="70" r="4"/><circle cx="286" cy="82" r="5"/></g><circle cx="286" cy="126" r="4" fill="rgba(181,72,58,.85)"/>
<path d="M166 40 v100 h124" fill="none" stroke="rgba(236,229,207,.3)" stroke-width="2"/></svg>'''
IL_OA2050 = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M58 14 C64 50 66 70 74 86 M106 14 C100 50 98 70 90 86" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/>
<path d="M70 98 C66 120 64 146 60 168 M94 98 C98 120 100 146 104 168" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/>
<path d="M68 90 Q82 82 96 90 M68 96 Q82 104 96 96" fill="none" stroke="#d8b25e" stroke-width="3"/>
<circle cx="82" cy="93" r="22" fill="none" stroke="#e2ab47" stroke-width="2" stroke-dasharray="4 4"/>
<g fill="#8fa476"><rect x="150" y="122" width="26" height="36" rx="3" opacity=".55"/><rect x="190" y="104" width="26" height="54" rx="3" opacity=".7"/><rect x="230" y="78" width="26" height="80" rx="3" fill="#e2ab47"/></g>
<path d="M140 158 H272" stroke="rgba(236,229,207,.35)" stroke-width="2"/>
<g font-family="Georgia,serif" font-size="13" fill="#ece5cf" text-anchor="middle"><text x="163" y="174">1990</text><text x="203" y="174">2023</text><text x="243" y="174">2050</text></g>
<path d="M243 40 V66 M233 56 L243 66 L253 56" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" transform="rotate(180 243 53)"/></svg>'''
IL_LACO = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M120 10 C126 50 128 70 136 86 M168 10 C162 50 160 70 152 86" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/>
<path d="M132 100 C128 124 126 148 122 172 M156 100 C160 124 162 148 166 172" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/>
<ellipse cx="144" cy="93" rx="26" ry="9" fill="rgba(143,179,196,.35)" stroke="#8fb3c4" stroke-width="2.5"/>
<g fill="#8fb3c4"><circle cx="132" cy="92" r="2.5"/><circle cx="146" cy="95" r="2"/><circle cx="156" cy="91" r="2.5"/></g>
<path d="M262 26 L190 80" stroke="#ece5cf" stroke-width="3" stroke-linecap="round"/>
<rect x="246" y="12" width="40" height="16" rx="4" transform="rotate(-37 266 20)" fill="#d8b25e"/>
<path d="M190 80 L180 88" stroke="#e2ab47" stroke-width="2" stroke-linecap="round"/>
<g fill="none" stroke="#e2ab47" stroke-width="2" stroke-linecap="round"><path d="M210 120 h40"/><path d="M210 132 h28"/><path d="M210 144 h36"/></g></svg>'''

IL_EXPAIN = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 156 H170" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<circle cx="92" cy="40" r="12" fill="#8fa476"/>
<path d="M92 54 L88 96 M90 62 L70 50 M90 62 L112 76 M88 96 L70 124 L60 154 M88 96 L108 120 L128 150" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<g font-family="Georgia,serif" font-size="12" fill="#ece5cf" text-anchor="end"><text x="214" y="38">10</text><text x="214" y="158">0</text></g>
<rect x="222" y="26" width="18" height="132" rx="9" fill="rgba(236,229,207,.08)" stroke="rgba(236,229,207,.25)"/>
<rect x="222" y="68" width="18" height="90" rx="9" fill="#e2ab47" opacity=".85"/>
<rect x="250" y="88" width="18" height="70" rx="9" fill="#8fa476"/>
<path d="M231 60 C246 52 256 66 259 80 M259 80 l-7 -3 M259 80 l3 -7" fill="none" stroke="#ece5cf" stroke-width="2.5" stroke-linecap="round"/>
<g fill="none" stroke="rgba(226,171,71,.55)" stroke-width="2.5" stroke-linecap="round"><path d="M44 70 q8 -8 0 -16"/><path d="M36 76 q14 -14 0 -28"/></g></svg>'''
IL_SPAF = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M40 24 V146 H292" fill="none" stroke="rgba(236,229,207,.3)" stroke-width="2"/>
<path d="M48 120 C80 70 104 48 128 46 C156 44 176 60 206 82 C236 104 260 118 284 130" fill="none" stroke="rgba(181,72,58,.75)" stroke-width="4" stroke-linecap="round"/>
<path d="M48 120 C80 70 104 48 128 46 C156 44 176 54 206 66 C236 78 260 88 284 96" fill="none" stroke="#e2ab47" stroke-width="4" stroke-linecap="round"/>
<circle cx="128" cy="46" r="6" fill="#ece5cf"/>
<g font-family="Georgia,serif" font-size="13" fill="#ece5cf" text-anchor="middle"><text x="48" y="164">16</text><text x="128" y="164">~35</text><text x="284" y="164">63</text></g>
<circle cx="284" cy="96" r="5" fill="#e2ab47"/><circle cx="284" cy="130" r="5" fill="rgba(181,72,58,.85)"/></svg>'''
IL_TAICHI = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M60 156 H260" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<path d="M92 92 C120 40 200 40 228 92" fill="none" stroke="rgba(226,171,71,.45)" stroke-width="3" stroke-dasharray="2 7" stroke-linecap="round"/>
<circle cx="160" cy="46" r="12" fill="#8fa476"/>
<path d="M160 60 V100 M160 70 C140 70 122 76 108 66 M160 70 C182 74 196 88 212 82 M160 100 L136 124 L124 154 M160 100 L184 122 L206 152" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="108" cy="64" r="5" fill="#d8b25e"/><circle cx="212" cy="82" r="5" fill="#d8b25e"/></svg>'''
IL_DEMPA = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M126 112 C98 112 86 92 94 74 C86 56 102 38 122 42 C128 28 152 24 164 36 C178 26 202 32 204 50 C222 54 228 76 216 90 C220 108 202 120 184 114 C174 126 146 126 138 114 Z" fill="rgba(143,164,118,.12)" stroke="rgba(236,229,207,.5)" stroke-width="3" stroke-linejoin="round"/>
<path d="M160 38 C154 58 166 72 158 94 C154 104 158 110 156 118 M118 66 C132 70 136 82 128 92 M196 62 C184 70 182 82 192 92" fill="none" stroke="rgba(236,229,207,.3)" stroke-width="2" stroke-linecap="round"/>
<circle cx="62" cy="146" r="11" fill="none" stroke="#8fa476" stroke-width="3"/><path d="M53 141 Q62 146 71 141 M53 151 Q62 146 71 151" fill="none" stroke="#8fa476" stroke-width="2"/>
<path d="M92 132 V162 M83 153 L92 163 L101 153" fill="none" stroke="#8fa476" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="222" y="138" width="24" height="20" rx="2" fill="none" stroke="rgba(181,72,58,.85)" stroke-width="3"/><path d="M222 146 H246" stroke="rgba(181,72,58,.85)" stroke-width="2"/>
<path d="M266 162 V132 M257 141 L266 131 L275 141" fill="none" stroke="rgba(181,72,58,.85)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''
IL_REACT = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<rect x="30" y="86" width="260" height="50" fill="rgba(181,72,58,.16)"/>
<path d="M30 84 H290 M30 138 H290" stroke="rgba(236,229,207,.4)" stroke-width="4"/>
<path d="M104 136 Q138 106 172 136 Z" fill="#e2ab47"/><path d="M214 86 Q232 102 250 86 Z" fill="#d8b25e" opacity=".85"/><path d="M58 136 Q66 128 74 136 Z" fill="#d8b25e" opacity=".6"/>
<path d="M146 22 H174 L169 48 H151 Z" fill="none" stroke="#8fa476" stroke-width="3" stroke-linejoin="round"/>
<path d="M150 58 Q160 64 170 58 M144 67 Q160 76 176 67" fill="none" stroke="#8fa476" stroke-width="2.5" stroke-linecap="round" opacity=".8"/>
</svg>'''
IL_CAVD = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<g fill="#223020" stroke="rgba(236,229,207,.55)" stroke-width="4"><circle cx="86" cy="58" r="14"/><circle cx="86" cy="86" r="14"/><circle cx="234" cy="58" r="14"/><circle cx="234" cy="86" r="14"/></g>
<rect x="86" y="60" width="148" height="24" fill="#223020"/><path d="M86 60 H234 M86 84 H234" stroke="rgba(236,229,207,.55)" stroke-width="4"/>
<rect x="104" y="122" width="52" height="22" rx="11" fill="none" stroke="#e2ab47" stroke-width="3"/><path d="M130 122 V144" stroke="#e2ab47" stroke-width="2"/>
<circle cx="198" cy="133" r="12" fill="none" stroke="#d8b25e" stroke-width="3"/><path d="M190 133 H206" stroke="#d8b25e" stroke-width="2"/>
<path d="M164 128 H180 M164 138 H180" stroke="rgba(236,229,207,.35)" stroke-width="3" stroke-linecap="round"/>
</svg>'''
IL_YSTROKE = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M150 118 C122 118 110 98 118 80 C110 62 126 44 146 48 C152 34 176 30 188 42 C202 32 226 38 228 56 C246 60 252 82 240 96 C244 114 226 126 208 120 C198 132 170 132 162 120 Z" fill="rgba(143,164,118,.12)" stroke="rgba(236,229,207,.5)" stroke-width="3" stroke-linejoin="round"/>
<path d="M200 60 L190 80 L204 82 L192 104" fill="none" stroke="#e2ab47" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
<g fill="#8fa476"><rect x="40" y="128" width="16" height="22" rx="3"/><rect x="62" y="114" width="16" height="36" rx="3"/></g>
<path d="M44 108 C60 98 72 92 86 84" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round"/><path d="M78 82 L88 83 L84 92" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''
IL_LONELY = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<g fill="rgba(236,229,207,.28)"><circle cx="60" cy="70" r="11"/><circle cx="92" cy="64" r="11"/><circle cx="124" cy="70" r="11"/></g>
<path d="M46 118 Q60 88 74 118 M78 112 Q92 82 106 112 M110 118 Q124 88 138 118" fill="none" stroke="rgba(236,229,207,.28)" stroke-width="8" stroke-linecap="round"/>
<circle cx="232" cy="66" r="12" fill="#8fa476"/><path d="M216 120 Q232 86 248 120" fill="none" stroke="#8fa476" stroke-width="9" stroke-linecap="round"/>
<path d="M30 148 H290" stroke="rgba(236,229,207,.2)" stroke-width="3" stroke-linecap="round"/>
<path d="M160 148 H290" stroke="#d8b25e" stroke-width="3" stroke-linecap="round"/><path d="M226 140 V156 M290 140 V156" stroke="#d8b25e" stroke-width="3" stroke-linecap="round"/>
<path d="M150 78 C160 78 168 92 178 92" fill="none" stroke="rgba(236,229,207,.25)" stroke-width="2" stroke-dasharray="4 5"/>
</svg>'''
IL_HTN = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<circle cx="110" cy="92" r="52" fill="none" stroke="rgba(236,229,207,.45)" stroke-width="4"/>
<path d="M76 118 A40 40 0 1 1 144 118" fill="none" stroke="rgba(236,229,207,.2)" stroke-width="8" stroke-linecap="round"/>
<path d="M110 92 L138 66" stroke="#e2ab47" stroke-width="5" stroke-linecap="round"/><circle cx="110" cy="92" r="7" fill="#e2ab47"/>
<path d="M160 120 C176 120 180 140 196 140 H214" fill="none" stroke="rgba(236,229,207,.45)" stroke-width="4" stroke-linecap="round"/>
<rect x="212" y="122" width="40" height="34" rx="12" fill="none" stroke="#8fa476" stroke-width="4"/>
<g fill="#d8b25e"><circle cx="232" cy="48" r="7"/><circle cx="254" cy="48" r="7"/><circle cx="276" cy="48" r="7"/></g>
<g fill="rgba(236,229,207,.22)"><circle cx="232" cy="72" r="7"/><circle cx="254" cy="72" r="7"/><circle cx="276" cy="72" r="7"/><circle cx="232" cy="96" r="7"/><circle cx="254" cy="96" r="7"/><circle cx="276" cy="96" r="7"/></g>
</svg>'''
IL_ROBOT = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M128 18 L140 82 L130 160 M176 18 L166 82 L176 160" fill="none" stroke="rgba(236,229,207,.45)" stroke-width="6" stroke-linecap="round"/>
<rect x="132" y="74" width="42" height="18" rx="6" fill="#d8b25e"/>
<path d="M290 160 V120 L248 96 L206 92" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="290" cy="120" r="6" fill="#8fa476"/><circle cx="248" cy="96" r="6" fill="#8fa476"/>
<path d="M206 92 h-14" stroke="#e2ab47" stroke-width="4" stroke-linecap="round"/>
<path d="M40 60 h44 M40 76 h44" stroke="rgba(236,229,207,.35)" stroke-width="4" stroke-linecap="round"/><text x="62" y="112" text-anchor="middle" font-family="Georgia,serif" font-size="26" fill="#ece5cf">=</text>
</svg>'''
IL_ISOWEEK = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M60 20 V160" stroke="rgba(236,229,207,.45)" stroke-width="6"/>
<circle cx="80" cy="56" r="11" fill="#8fa476"/><path d="M76 70 L74 112 H112 V150" fill="none" stroke="#8fa476" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M76 80 L98 94" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/>
<g fill="none" stroke="rgba(236,229,207,.35)" stroke-width="2"><rect x="170" y="36" width="120" height="96" rx="8"/></g>
<g fill="rgba(236,229,207,.12)"><rect x="180" y="62" width="22" height="22" rx="4"/><rect x="208" y="62" width="22" height="22" rx="4"/><rect x="236" y="62" width="22" height="22" rx="4"/><rect x="264" y="62" width="18" height="22" rx="4"/><rect x="180" y="92" width="22" height="22" rx="4"/><rect x="236" y="92" width="22" height="22" rx="4"/><rect x="264" y="92" width="18" height="22" rx="4"/></g>
<rect x="208" y="92" width="22" height="22" rx="4" fill="#d8b25e"/>
<path d="M176 48 H284" stroke="#e2ab47" stroke-width="4" stroke-linecap="round"/>
</svg>'''
IL_VITAL = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<rect x="54" y="40" width="44" height="64" rx="8" fill="none" stroke="#8fa476" stroke-width="4"/><path d="M76 104 V132 Q76 146 96 146 H130" fill="none" stroke="#8fa476" stroke-width="3"/>
<path d="M60 70 H92" stroke="rgba(143,164,118,.5)" stroke-width="20"/>
<path d="M222 40 C206 40 198 52 198 66 V104 H246 V66 C246 52 238 40 222 40 Z" fill="none" stroke="#d8b25e" stroke-width="4"/>
<path d="M222 104 V132 Q222 146 202 146 H170" fill="none" stroke="#d8b25e" stroke-width="3"/>
<g fill="#d8b25e" opacity=".7"><circle cx="214" cy="80" r="4"/><circle cx="228" cy="72" r="3"/><circle cx="224" cy="90" r="3.5"/></g>
<text x="150" y="100" text-anchor="middle" font-family="Georgia,serif" font-size="34" fill="#ece5cf">=</text>
</svg>'''
IL_ONCOEX = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M40 150 H280" stroke="rgba(236,229,207,.25)" stroke-width="3" stroke-linecap="round"/>
<circle cx="98" cy="46" r="11" fill="#8fa476"/><path d="M96 58 L90 96 L72 120 L66 148 M90 96 L106 118 L118 146 M94 68 L76 86 M94 68 L114 80" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M170 132 C196 128 214 100 232 92 C248 84 262 70 276 52" fill="none" stroke="#d8b25e" stroke-width="4" stroke-linecap="round"/>
<path d="M266 50 h12 v12" fill="none" stroke="#d8b25e" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M226 36 c-8 -10 -22 -4 -18 8 c3 9 18 16 18 16 s15 -7 18 -16 c4 -12 -10 -18 -18 -8 z" fill="none" stroke="#e2ab47" stroke-width="3"/>
</svg>'''
IL_DBS = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M130 132 C96 132 82 108 92 86 C82 64 100 40 124 44 C130 26 160 22 172 36 C188 24 216 32 218 54 C240 58 246 84 232 100 C238 120 216 134 196 126 C184 142 150 142 142 128 Z" fill="rgba(143,164,118,.1)" stroke="rgba(236,229,207,.45)" stroke-width="3" stroke-linejoin="round"/>
<path d="M160 10 L162 82" stroke="#ece5cf" stroke-width="3" stroke-linecap="round"/><circle cx="162" cy="84" r="5" fill="#e2ab47"/>
<g fill="none" stroke-width="3.5" stroke-linecap="round"><path d="M162 84 C140 80 122 70 112 58" stroke="#d8b25e"/><path d="M162 84 C182 76 200 64 210 50" stroke="#d8b25e" opacity=".8"/><path d="M162 84 C166 100 178 112 196 116" stroke="#8fa476"/></g>
</svg>'''
IL_ACLX = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M40 156 H280" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<path d="M118 22 C112 54 116 74 130 90 M130 90 C146 108 146 128 136 156" fill="none" stroke="#8fa476" stroke-width="16" stroke-linecap="round"/>
<ellipse cx="134" cy="92" rx="15" ry="11" fill="#d8b25e"/>
<path d="M120 84 L148 102" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" stroke-dasharray="3 4"/>
<rect x="196" y="58" width="16" height="64" rx="6" fill="rgba(236,229,207,.25)"/><rect x="220" y="40" width="16" height="82" rx="6" fill="#8fa476"/>
<path d="M188 122 H246" stroke="rgba(236,229,207,.35)" stroke-width="2"/></svg>'''
IL_HIPOA = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M58 40 C82 30 118 34 132 54" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/>
<circle cx="120" cy="74" r="20" fill="#d8b25e"/>
<path d="M120 94 L104 156" stroke="#8fa476" stroke-width="16" stroke-linecap="round"/>
<path d="M40 156 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<path d="M190 40 V150 H290" fill="none" stroke="rgba(236,229,207,.3)" stroke-width="2"/>
<rect x="208" y="118" width="24" height="32" rx="5" fill="#e2ab47"/>
<path d="M196 94 H286" stroke="rgba(236,229,207,.6)" stroke-width="2" stroke-dasharray="5 5"/>
<g font-family="Georgia,serif" font-size="12" fill="#ece5cf" text-anchor="middle"><text x="220" y="112">7</text><text x="268" y="88">12</text></g></svg>'''
IL_FAST4 = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 156 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<g fill="none" stroke="#8fa476" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">
<circle cx="56" cy="74" r="8" fill="#8fa476" stroke="none"/><path d="M56 84 L54 112 L46 138 M54 112 L64 138 M56 92 L74 98"/>
<circle cx="124" cy="62" r="8" fill="#8fa476" stroke="none"/><path d="M122 72 L116 100 L130 116 L128 138 M116 100 L104 110 M120 80 L138 90"/>
<circle cx="188" cy="64" r="8" fill="#8fa476" stroke="none"/><path d="M188 74 V108 L184 138 M188 108 L194 138 M188 84 L172 92 M188 84 L204 92"/>
<circle cx="252" cy="62" r="8" fill="#8fa476" stroke="none"/><path d="M252 72 L250 106 L262 118 L262 138 M250 106 L240 138 M250 82 L236 98 M250 82 L266 94"/></g>
<path d="M232 138 H276 V124 H262" fill="none" stroke="#d8b25e" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M76 98 C90 96 100 90 104 84" fill="none" stroke="#e2ab47" stroke-width="2.5" stroke-dasharray="3 4"/>
<circle cx="160" cy="28" r="14" fill="none" stroke="#e2ab47" stroke-width="3"/><path d="M160 28 V20 M160 28 L166 32" stroke="#ece5cf" stroke-width="2.5" stroke-linecap="round"/></svg>'''
IL_ESTEPS = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 156 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<rect x="44" y="34" width="112" height="78" rx="8" fill="none" stroke="rgba(236,229,207,.4)" stroke-width="3"/>
<path d="M84 112 L78 132 H122 L116 112" fill="none" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linejoin="round"/>
<g stroke-linecap="round" stroke-linejoin="round" fill="none"><path d="M60 56 l5 5 l9 -10" stroke="#8fa476" stroke-width="3.5"/><path d="M82 56 H140" stroke="rgba(236,229,207,.35)" stroke-width="3"/>
<path d="M60 76 l5 5 l9 -10" stroke="#8fa476" stroke-width="3.5"/><path d="M82 76 H130" stroke="rgba(236,229,207,.35)" stroke-width="3"/>
<path d="M60 96 l5 5 l9 -10" stroke="#e2ab47" stroke-width="3.5"/><path d="M82 96 H124" stroke="rgba(236,229,207,.35)" stroke-width="3"/></g>
<path d="M192 92 H284 M204 92 V156 M276 92 V156" stroke="#8a6a44" stroke-width="5" stroke-linecap="round" fill="none"/>
<circle cx="236" cy="44" r="9" fill="#8fa476"/>
<path d="M236 56 V104 M236 104 L232 156 M236 104 L242 128 L240 156 M236 66 L262 86 L274 90 M236 66 L218 80" fill="none" stroke="#8fa476" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>'''
IL_BELT = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M124 22 C116 52 112 76 114 100 C116 124 112 146 108 164 M196 22 C204 52 208 76 206 100 C204 124 208 146 212 164" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/>
<path d="M110 86 C140 96 180 96 210 86 L212 124 C180 134 140 134 108 124 Z" fill="#d8b25e" opacity=".85"/>
<path d="M150 92 V130 M170 92 V130" stroke="#223020" stroke-width="2.5" stroke-dasharray="4 4"/>
<path d="M240 60 C256 72 256 92 240 104 M254 52 C276 70 276 98 254 116" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" opacity=".7"/>
<path d="M40 164 H280" stroke="rgba(236,229,207,.18)" stroke-width="2"/></svg>'''
IL_PACBACK = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 156 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<circle cx="96" cy="40" r="10" fill="#8fa476"/>
<path d="M96 54 L94 104 L82 130 L80 156 M94 104 L108 130 L112 156 M96 64 L78 86 M96 64 L118 80" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="94" cy="98" r="11" fill="none" stroke="#e2ab47" stroke-width="3"/>
<rect x="170" y="36" width="96" height="104" rx="10" fill="none" stroke="rgba(236,229,207,.4)" stroke-width="3"/>
<g stroke-linecap="round"><path d="M186 62 H250" stroke="#d8b25e" stroke-width="4"/><path d="M186 84 H240" stroke="rgba(236,229,207,.35)" stroke-width="4"/><path d="M186 106 H232" stroke="rgba(236,229,207,.35)" stroke-width="4"/></g>
<path d="M190 124 C204 114 218 132 232 120 C240 114 248 118 252 122" fill="none" stroke="#8fa476" stroke-width="3.5" stroke-linecap="round"/></svg>'''
IL_ESPRESSO = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 160 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<rect x="160" y="30" width="130" height="86" rx="8" fill="none" stroke="rgba(236,229,207,.4)" stroke-width="3"/>
<path d="M172 94 C192 78 212 98 232 84 C248 74 264 84 278 76" fill="none" stroke="rgba(143,164,118,.5)" stroke-width="3" stroke-linecap="round"/>
<path d="M196 70 C206 56 230 52 246 62 C252 66 256 66 262 62 C260 70 254 74 246 74 C232 82 212 82 196 70 Z" fill="#d8b25e"/>
<path d="M222 58 L226 48 L232 58" fill="#d8b25e"/>
<path d="M206 136 V116 M244 136 V116" stroke="rgba(236,229,207,.3)" stroke-width="3"/>
<path d="M44 110 H112 M56 110 V160 M104 110 V160" stroke="#8a6a44" stroke-width="5" stroke-linecap="round" fill="none"/>
<circle cx="84" cy="44" r="10" fill="#8fa476"/>
<path d="M84 58 L86 104 L120 106 L122 158 M84 70 L118 78 L148 72" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="148" cy="72" r="5" fill="#e2ab47"/></svg>'''
IL_OAEX = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 156 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<g fill="none" stroke-linecap="round" stroke-linejoin="round"><rect x="40" y="40" width="96" height="110" rx="8" stroke="rgba(236,229,207,.25)" stroke-width="3"/><rect x="50" y="30" width="96" height="110" rx="8" stroke="rgba(236,229,207,.35)" stroke-width="3" fill="#223020"/><rect x="60" y="20" width="96" height="110" rx="8" stroke="rgba(236,229,207,.5)" stroke-width="3" fill="#223020"/>
<path d="M76 44 H140 M76 60 H132 M76 76 H136" stroke="rgba(236,229,207,.35)" stroke-width="3"/></g>
<path d="M76 116 V108 M92 116 V102 M108 116 V110 M124 116 V106" stroke="#e2ab47" stroke-width="7" stroke-linecap="round"/>
<path d="M198 24 C194 50 194 70 202 86 M246 24 C252 50 252 70 244 86" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/>
<path d="M202 96 C196 116 196 136 200 158 M244 96 C250 116 250 136 246 158" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/>
<path d="M200 88 C214 96 232 96 246 88 M200 94 C214 102 232 102 246 94" fill="none" stroke="#d8b25e" stroke-width="3.5" stroke-linecap="round"/>
<circle cx="276" cy="56" r="8" fill="none" stroke="#e2ab47" stroke-width="3"/><path d="M282 62 L292 72" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>'''
IL_DEPEX = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 156 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<path d="M58 70 C50 70 44 64 44 57 C44 49 51 43 59 44 C62 36 70 31 79 32 C89 33 96 41 96 50 C103 50 108 55 108 62 C108 66 104 70 99 70 Z" fill="rgba(236,229,207,.22)"/>
<path d="M56 82 L52 92 M72 82 L68 92 M88 82 L84 92" stroke="rgba(236,229,207,.25)" stroke-width="3" stroke-linecap="round"/>
<circle cx="250" cy="48" r="18" fill="#d8b25e"/>
<path d="M250 18 V24 M250 72 V78 M220 48 H226 M274 48 H280 M229 27 L233 31 M267 65 L271 69 M271 27 L267 31 M229 69 L233 65" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/>
<circle cx="164" cy="54" r="10" fill="#8fa476"/>
<path d="M164 68 L160 108 L146 130 L142 156 M160 108 L176 128 L182 154 M162 78 L146 98 M162 78 L182 90" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M120 116 C128 104 134 104 140 110" fill="none" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round" stroke-dasharray="3 5"/></svg>'''
IL_LBPG = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 160 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<rect x="40" y="26" width="104" height="128" rx="8" fill="none" stroke="rgba(236,229,207,.45)" stroke-width="3"/>
<g fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M56 50 l5 5 l9 -10" stroke="#8fa476" stroke-width="3.5"/><path d="M78 50 H128" stroke="rgba(236,229,207,.35)" stroke-width="3"/>
<path d="M56 78 l5 5 l9 -10" stroke="#8fa476" stroke-width="3.5"/><path d="M78 78 H122" stroke="rgba(236,229,207,.35)" stroke-width="3"/>
<path d="M58 100 l10 10 M68 100 l-10 10" stroke="#e2ab47" stroke-width="3.5"/><path d="M78 106 H118" stroke="rgba(236,229,207,.35)" stroke-width="3"/>
<path d="M58 124 l10 10 M68 124 l-10 10" stroke="#e2ab47" stroke-width="3.5"/><path d="M78 130 H114" stroke="rgba(236,229,207,.35)" stroke-width="3"/></g>
<circle cx="228" cy="40" r="10" fill="#8fa476"/>
<path d="M228 54 C226 74 230 90 226 104 M226 104 L216 132 L214 158 M226 104 L240 130 L244 158 M228 64 L210 84 M228 64 L248 80" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="227" cy="96" r="12" fill="none" stroke="#e2ab47" stroke-width="3"/></svg>'''
IL_RRAD = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 160 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<circle cx="82" cy="46" r="10" fill="#8fa476"/>
<path d="M82 60 L78 102 L64 126 L60 156 M78 102 L94 124 L100 154 M80 70 L64 90 M80 70 L100 84" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M160 70 C150 56 154 36 172 32 C178 22 196 20 204 30 C216 24 232 32 232 46 C244 50 246 68 236 76 C238 92 222 100 210 94 C202 104 184 104 178 94 C164 98 152 86 160 70 Z" fill="none" stroke="#d8b25e" stroke-width="4" stroke-linejoin="round"/>
<path d="M176 52 C186 58 196 50 206 58 M184 74 C194 68 204 78 214 70" fill="none" stroke="rgba(236,229,207,.4)" stroke-width="3" stroke-linecap="round"/>
<path d="M190 120 H210 M200 110 V130" stroke="rgba(236,229,207,.35)" stroke-width="4" stroke-linecap="round"/>
<path d="M150 142 H170 L176 132 L184 152 L190 142 H250" fill="none" stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'''
IL_SMALL = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 156 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<circle cx="96" cy="78" r="44" fill="none" stroke="#d8b25e" stroke-width="5"/>
<path d="M96 78 V46 M96 78 L118 90" stroke="#ece5cf" stroke-width="4" stroke-linecap="round"/>
<path d="M96 34 A44 44 0 0 1 118 40" fill="none" stroke="#e2ab47" stroke-width="9" stroke-linecap="round"/>
<circle cx="96" cy="78" r="5" fill="#ece5cf"/>
<circle cx="222" cy="42" r="10" fill="#8fa476"/>
<path d="M222 56 L218 96 L204 118 L200 152 M218 96 L234 116 L240 150 M220 66 L204 86 M220 66 L240 80" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M256 96 H284 M262 110 H284" stroke="rgba(236,229,207,.35)" stroke-width="3" stroke-linecap="round"/></svg>'''
IL_CADENCE = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 156 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<circle cx="86" cy="40" r="10" fill="#8fa476"/>
<path d="M86 54 L80 96 L62 120 L56 154 M80 96 L100 118 L112 150 M84 64 L66 86 M84 64 L106 80" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<g fill="#d8b25e" opacity=".85"><ellipse cx="150" cy="146" rx="5" ry="8"/><ellipse cx="170" cy="134" rx="5" ry="8"/><ellipse cx="190" cy="146" rx="5" ry="8"/><ellipse cx="210" cy="134" rx="5" ry="8"/></g>
<path d="M226 104 A40 40 0 0 1 290 104" fill="none" stroke="rgba(236,229,207,.4)" stroke-width="4" stroke-linecap="round"/>
<path d="M276 76 A40 40 0 0 1 290 104" fill="none" stroke="#e2ab47" stroke-width="7" stroke-linecap="round"/>
<path d="M258 104 L280 82" stroke="#ece5cf" stroke-width="4" stroke-linecap="round"/><circle cx="258" cy="104" r="5" fill="#ece5cf"/></svg>'''
IL_PREHAB = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 156 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<rect x="34" y="30" width="96" height="82" rx="8" fill="none" stroke="rgba(236,229,207,.45)" stroke-width="3"/>
<path d="M34 50 H130" stroke="rgba(236,229,207,.45)" stroke-width="3"/>
<g fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="3.5"><path d="M48 66 l4 4 l8 -9" stroke="#8fa476"/><path d="M74 66 l4 4 l8 -9" stroke="#8fa476"/><path d="M100 66 l4 4 l8 -9" stroke="#8fa476"/><path d="M48 90 l4 4 l8 -9" stroke="#8fa476"/><path d="M76 86 l8 8 M84 86 l-8 8" stroke="#e2ab47"/></g>
<circle cx="196" cy="46" r="10" fill="#8fa476"/>
<path d="M196 60 L194 102 L182 128 L180 154 M194 102 L208 128 L212 154 M195 70 L176 86 M195 70 L216 86" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M176 86 C190 112 204 112 216 86" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/>
<path d="M238 128 H292 M244 128 V150 M286 128 V150 M244 116 H262" stroke="rgba(236,229,207,.4)" stroke-width="4" stroke-linecap="round"/></svg>'''
IL_COGENG = '''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M30 156 H290" stroke="rgba(236,229,207,.18)" stroke-width="2"/>
<path d="M118 66 C108 52 112 32 130 28 C136 18 154 16 162 26 C174 20 190 28 190 42 C202 46 204 64 194 72 C196 88 180 96 168 90 C160 100 142 100 136 90 C122 94 110 82 118 66 Z" fill="none" stroke="#d8b25e" stroke-width="4" stroke-linejoin="round"/>
<path d="M134 48 C144 54 154 46 164 54 M142 70 C152 64 162 74 172 66" fill="none" stroke="rgba(236,229,207,.4)" stroke-width="3" stroke-linecap="round"/>
<g fill="none" stroke="#8fa476" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"><circle cx="82" cy="108" r="8" fill="#8fa476" stroke="none"/><path d="M82 120 V146 M82 128 L70 140 M82 128 L94 138"/>
<circle cx="236" cy="108" r="8" fill="#8fa476" stroke="none"/><path d="M236 120 V146 M236 128 L224 138 M236 128 L248 140"/></g>
<circle cx="158" cy="122" r="8" fill="#e2ab47"/><path d="M158 134 V150 M158 140 L146 134 M158 140 L170 134" fill="none" stroke="#e2ab47" stroke-width="6" stroke-linecap="round"/>
<path d="M100 130 H138 M178 130 H216" stroke="rgba(236,229,207,.35)" stroke-width="3" stroke-linecap="round" stroke-dasharray="4 6"/></svg>'''
NEWS = [
 dict(il=IL_NOBEL, g="beyin", cat="Nobel 2026", feat=True, date="Ekim 2026",
      title="Işık, ayna ve buz: 2026 Nobel ödülleri",
      text="Tıp ödülü, beyin hücrelerini ışıkla çalıştırıp durdurmayı sağlayan optogenetiğin üç öncüsüne; kimya ödülü, ayna görüntüsü moleküllerden yalnızca birini üretmenin yolunu gösteren Henri Kagan ve Kenso Soai'ye; fizik ödülü ise Güney Kutbu'nun buzunda kozmik nötrinoları yakalayan Francis Halzen'e verildi.",
      point="Üçünün de çıkış noktası, o gün hiçbir işe yaramayacak gibi görünen bir meraktı: bir gölet yosunu, hesaba uymayan bir tepkime ve buzun dibinde çakan bir ışık. Üçünü de canlandırmalarla, sade bir dille anlattım.",
      src=[("STAT, 5 Ekim 2026", "https://www.statnews.com/2026/10/05/nobel-prize-medicine-2026-winner-deisseroth-hegemann-nagel/"), ("IceCube, 6 Ekim 2026", "https://icecube.wisc.edu/news/awards/2026/10/francis-halzen-icecube-principal-investigator-wins-2026-physics-nobel-prize/"), ("Forbes, 7 Ekim 2026", "https://www.forbes.com/sites/michaeltnietzel/2026/10/07/the-2026-nobel-prize-in-chemistry-is-awarded-to-henri-kagan-and-kenso-soai/"), ("Nobel Ödülü, Ekim 2026", "https://www.nobelprize.org/all-nobel-prizes-2026/")],
      rel=("Canlandırmalı anlatımı aç", "nobel-2026.html")),
 dict(il=IL_COGENG, g="beyin", cat="Demans", date="Ekim 2026",
      title="Egzersiz ile sosyal ve zihinsel etkinlik birlikte: bilişsel bozulma olmadan geçen yıllar artabilir",
      text="Dört büyük yaşlanma kohortunun verilerini birleştiren ve 2026'da Alzheimer's & Dementia dergisinde yayımlanan bir çalışmada, başlangıçta bilişsel bozukluğu olmayan 50 yaş ve üstü 54.217 kişi izlendi. Düzenli ve planlı egzersiz ile sosyal ve zihinsel etkinliklere katılım (topluluk etkinlikleri, hobiler, gönüllülük, oyunlar, yeni şeyler öğrenme) birlikte değerlendirildi. İkisi de düşük olanlara göre bilişsel bozukluk riski yalnızca egzersizi yüksek olanlarda %20, yalnızca sosyal-zihinsel katılımı yüksek olanlarda %21, ikisi de yüksek olanlarda %30 daha düşüktü. 50 yaşından itibaren bilişsel bozukluk olmadan geçirilmesi beklenen süre ikisi de düşük olanlarda 17,5 yıl, ikisi de yüksek olanlarda 24,7 yıl olarak hesaplandı; aradaki fark yaklaşık 7 yıldı.",
      point="Bu bir gözlem çalışmasıdır; bu etkinliklerin bilişsel bozukluğu önlediğini kanıtlamaz. Etkinlikler kişilerin kendi beyanına dayanıyor, “yüksek” ve “düşük” düzeyler kohortlar arasında uyumlaştırılmış ölçütler ve bir kılavuz eşiği değil. Yazarlar sonuçların nesnel ölçümlerle ve müdahale çalışmalarıyla doğrulanması gerektiğini belirtiyor. Yine de bulgu, egzersizin ve sosyal-zihinsel etkinliğin birbirinin yerine değil, birlikte düşünülmesini destekliyor.",
      src=[("Alzheimer's & Dementia, 2026", "https://doi.org/10.1002/alz.71854"), ("Medscape, 2026", "https://www.medscape.com/viewarticle/more-exercise-and-cognitive-social-engagement-tied-more-2026a10013j4"), ("eBiotrade (Çince), 15 Ekim 2026", "https://www.ebiotrade.com/newsf/2026-10/20261015085510850.htm")],
      rel=("Demansta egzersiz", "demans-egzersiz.html")),
 dict(il=IL_ESTEPS, g="hareket", cat="Düşme", date="Ekim 2026",
      title="Aile hekimliğinde elektronik kayıt üzerinden önerilen ev egzersizleri düşmeleri biraz azalttı",
      text="ABD'de Brigham and Women's Hastanesi ve Teksas Üniversitesi Tıp Fakültesi'nden (UTMB) araştırmacıların 16 Ekim 2026'da JAMA Network Open'da yayımladığı eSTEPS çalışmasında, tek bir sağlık sistemine bağlı 22 aile hekimliği muayenehanesi rastgele iki gruba ayrıldı. Düşme riski taramasında riskli çıkan 65 yaş üstü 11.945 kişi (yaş ortalaması 77, üçte ikisi kadın) 12–23 ay izlendi. Müdahale grubundaki muayenehanelerde elektronik hasta kaydına eklenen bir araç, hekimlere hastaya göre ayarlanmış ev egzersizleri önermeyi hatırlattı. Egzersizler Otago programından sadeleştirilmişti: dört zorluk seviyesi, yaklaşık 10 dakika süren ve ekipman gerektirmeyen bir program; hastalara el kitabı, web sitesi ve videolu bir uygulama da sunuldu. Kayıtlara geçen düşmeler müdahale grubunda 100 hasta-yılında 19,3, olağan bakım grubunda 21,2 oldu; yani %9 daha azdı. Düşmeye bağlı yaralanmalar 15,7'ye karşı 16,7 idi; ölümlerde fark görülmedi.",
      point="Etki küçük; üstelik müdahale grubundaki hastaların yalnızca yaklaşık %22'sine egzersiz reçetesi verildi ve hastaların egzersizleri yapıp yapmadığı izlenmedi. Düşmeler tanı kodlarından sayıldığı için bildirilmeyen düşmeler gözden kaçmış olabilir; çalışma tek bir sağlık sisteminde yapıldı ve gruplar başlangıçta bazı açılardan farklıydı. Yine de sonuç, kısa ve düzenli ev egzersizlerinin günlük muayene akışı içinde, çok sayıda kişiye önerilebileceğini gösteriyor. Benzer hareketleri Kendine iyi bak bölümündeki denge antrenmanıyla yapabilirsiniz.",
      src=[("JAMA Network Open, 16 Ekim 2026", "https://doi.org/10.1001/jamanetworkopen.2026.39240"), ("Medical Daily, 17 Ekim 2026", "https://www.medicaldaily.com/older-adults-falls-home-strength-balance-exercise-trial-480083"), ("UTMB, 19 Ekim 2026", "https://www.utmb.edu/scoa/news-and-events/archive/2026/10/19/study-finds-electronic-health-record-tool-can-help-reduce-falls-among-older-adults")],
      rel=("Denge antrenmanı", "denge-antrenmani.html")),
 dict(il=IL_VITAL, g="tani", cat="Ameliyat", date="Ekim 2026",
      title="Büyük ameliyatlarda damardan ya da gazla anestezi: iyileşmede fark yok",
      text="İngiltere'de Warwick Üniversitesi ve Royal Marsden Hastanesi'nin yürüttüğü ve JAMA'da yayımlanan VITAL çalışmasında, 49 NHS hastanesinde kalp dışı büyük ve planlı bir ameliyat geçiren, 50 yaş ve üzeri 2.507 hasta rastgele iki gruba ayrıldı: bir grupta anestezi damar yoluyla sürekli propofol verilerek (total intravenöz anestezi), diğerinde sevofluran gibi solunan gazlarla yapıldı. Ameliyattan sonraki 30 günde hayatta ve hastane dışında geçirilen gün sayısında anlamlı bir fark bulunmadı. Büyük komplikasyonlar, deliryum ve ölüm 30 gün, 90 gün ve 6 ay sonra da benzerdi. Damar yoluyla anestezi alanlar ameliyattan sonraki gün daha az susuzluk, ses kısıklığı, bulantı ve kusma bildirdi; altı aylık maliyet ve yaşam kalitesi de benzerdi.",
      point="Çalışma körlenmemişti: hastalar hangi yöntemin uygulandığını biliyordu, bu da bulantı gibi hastanın kendi bildirdiği sonuçları etkilemiş olabilir. Tüm hastalar İngiltere'de tedavi edildi; sonuçlar başka sağlık sistemlerine doğrudan aktarılamayabilir. Uzun vadeli kanser sonuçları ve çevresel etki incelenmedi. İki yöntem arasında iyileşme açısından anlamlı bir fark görülmediğinden, seçim anestezi uzmanınızla birlikte yapılabilir.",
      src=[("Warwick Üniversitesi, Ekim 2026", "https://warwick.ac.uk/news/pressreleases/anaesthesia-choice-makes-no-difference-for-pateint-recovery-VITAL/"), ("JAMA, 13 Ekim 2026", "https://doi.org/10.1001/jama.2026.11065"), ("Critical Care Reviews, bağımsız değerlendirme", "https://criticalcarereviews.com/perioperative/vital-trial")]),
 dict(il=IL_DBS, g="beyin", cat="Depresyon", date="Ekim 2026",
      title="Derin beyin stimülasyonunda depresyonu düzelten üç beyin yolu",
      text="ABD'de Mount Sinai'den araştırmacıların American Journal of Psychiatry'de yayımladığı çalışmada, tedaviye dirençli ağır depresyon nedeniyle beynin subkallosal singulat bölgesine derin beyin stimülasyonu (DBS) elektrotları yerleştirilmiş hastaların birkaç ayrı gruptan toplanan verileri incelendi. Araştırmacılar elektrotların oluşturduğu elektrik alanını bilgisayarda modelleyip beyin bağlantı haritalarıyla birleştirdi. Kalıcı düzelme, uyarının üç beyaz cevher yoluna ulaşmasıyla tutarlı biçimde ilişkiliydi: singulum demeti, forseps minör ve medial unsinat fasikülüs ile ventral amigdalofugal yol. İki yıl sonunda yanıt vermeyen hastalarda uyarının sol singulum demetine ulaşmadığı görüldü.",
      point="Bu, var olan hasta gruplarının verilerinin birlikte incelendiği bir çalışma; elektrotları bu yollara göre yerleştirmenin sonuçları iyileştirip iyileştirmediği henüz denenmedi. Her hastanın kendi beyin görüntüsü yoktu; basın bülteninde hasta sayısı ve yanıt oranları verilmedi. Yazarlardan bazıları, yöntemin lisanslandığı cihaz şirketine danışmanlık yapıyor. DBS, yalnızca diğer tedavilere yanıt vermeyen ağır depresyonda kullanılan, ameliyat gerektiren bir yöntemdir.",
      src=[("ScienceDaily (Mount Sinai), 18 Ekim 2026", "https://www.sciencedaily.com/releases/2026/10/261017230021.htm"), ("American Journal of Psychiatry, 1 Ekim 2026", "https://doi.org/10.1176/appi.ajp.20250449"), ("Mount Sinai, 13 Ekim 2026", "https://www.mountsinai.org/about/newsroom/2026/study-identifies-brain-pathways-linked-to-sustained-improvement-in-those-receiving-deep-brain-stimulation-for-treatment-resistant-depression")]),
 dict(il=IL_ROBOT, g="hareket", cat="Protez", date="Ekim 2026",
      title="Robotik diz ve kalça protezi, erken dönemde klasik ameliyattan üstün çıkmadı",
      text="Queen Mary, Oxford ve Bristol üniversitelerinden araştırmacıların The BMJ'de yayımladığı iki çalışmada, İngiltere ve Galler Ulusal Eklem Kayıt Sistemi'nin 2018–2024 verileri incelendi: 666.283 kalça protezi (10.203'ü robot yardımlı) ve 697.145 diz protezi (22.111'i robot yardımlı). Ortalama 2,5 yıllık izlemde robot yardımlı ve klasik ameliyatlar arasında protezin ömrü ve yeniden ameliyat (revizyon) riski açısından fark bulunmadı. Kalçada robot yardımlı ameliyat, protezin yanlış konumlanmasıyla ilişkili olabilecek revizyonlarda daha düşük riskle ilişkiliydi, ancak bu genel revizyon riskini azaltmadı. Kalça protezinde hastaların hayatta kalma oranı da farklı değildi.",
      point="Bu bir gözlem çalışması: Randomize bir çalışmayı taklit eden bir yöntemle yapıldı, ama ölçülemeyen farklar sonuçları etkilemiş olabilir. İzlem kısa; uzun vadeli farklar ve ağrı, günlük işlev gibi hasta sonuçları henüz karşılaştırılmadı, bunları devam eden randomize çalışmalar gösterecek. Robot sistemlerinin kurulumu yaklaşık 1 milyon sterlin tutuyor ve her ameliyata 1.000–2.500 sterlin ek maliyet getiriyor.",
      src=[("BMJ Group, 30 Eylül 2026", "https://bmjgroup.com/robotic-surgery-offers-no-clear-benefit-over-conventional-joint-replacement-surgery/"), ("The BMJ, 2026 (diz)", "https://doi.org/10.1136/bmj-2026-100691"), ("The BMJ, 2026 (kalça)", "https://doi.org/10.1136/bmj-2026-100709")],
      rel=("Diz ve kalça protezi sonrası", "protez-sonrasi.html")),
 dict(il=IL_LONELY, g="beyin", cat="Yalnızlık", date="Ekim 2026",
      title="Yalnızlık ve sosyal izolasyon, hastalıksız geçen yılları kısaltabilir",
      text="ABD'deki Tulane Üniversitesi'nden araştırmacıların Nature Communications dergisinde yayımladığı çalışmada, başlangıçta diyabet, kalp hastalığı, akciğer hastalığı, demans, kanser, depresyon ve kaygı bozukluğu olmayan, 40–69 yaş arası 277.489 yetişkin izlendi. 50 yaşında hem yalnızlık hisseden hem de sosyal olarak yalıtılmış olanlar, ikisini de yaşamayanlara göre bedensel hastalıklardan uzak geçirecekleri yıllardan kadınlarda yaklaşık 2,4, erkeklerde 1,7 yıl; depresyon ve kaygıdan uzak geçirecekleri yıllardan kadınlarda yaklaşık 3,7, erkeklerde 5,8 yıl kaybediyordu. Sağlıklı beslenme, egzersiz, iyi uyku ve sigara içmeme gibi alışkanlıklar, sosyal izolasyonla ilişkili kaybı azalttı; yalnızlıkla ilişkili kaybı ise anlamlı ölçüde azaltmadı.",
      point="Bu bir gözlem çalışması: Yalnızlığın hastalıklara yol açtığını kanıtlamıyor. Araştırmacılar neden-sonuç ilişkisini sınamak için klinik çalışmalar planlıyor. Bulgu yine de, yalnızlık hissinin yalnızca sağlıklı alışkanlıklarla telafi edilemeyebileceğini; insan ilişkilerine ayrıca özen göstermek gerektiğini düşündürüyor.",
      src=[("ScienceDaily (Tulane Üniversitesi), 10 Ekim 2026", "https://www.sciencedaily.com/releases/2026/10/261006234514.htm"), ("Nature Communications, 2026", "https://doi.org/10.1038/s41467-026-74498-8"), ("Neuroscience News, 22 Eylül 2026", "https://neurosciencenews.com/loneliness-mental-health-longevity-31238/")],
      rel=("Sosyal bağ ve sağlık", "bag-kurmak.html")),
 dict(il=IL_LBPG, g="hareket", cat="Bel ağrısı", date="Ekim 2026",
      title="Yeni başlayan bel ağrısında yeni kılavuz: Önce bilgi ve hareket, rutin görüntüleme ve opioid yok",
      text="Amerikan Ağrı Tıbbı Akademisi (AAPM), 6 haftadan kısa süren ve bir yaralanmaya bağlı olmayan bel ağrısı için Ekim 2026'da yeni bir klinik kılavuz yayımladı. Kılavuz, 105 çalışmayı inceleyen ve Pain Medicine dergisinde yayımlanan bir sistematik derlemeye dayanıyor. Ciddi bir hastalığı düşündüren belirtisi olmayanlarda erken görüntülemenin (röntgen, MR) ağrıyı ve işlevi iyileştirmediği görüldü; kılavuz bu kişilerde rutin görüntülemeye karşı güçlü bir öneride bulunuyor. İlk adım olarak hasta eğitimi, hafif etkinliklerle aktif kalma ve kendi kendine bakım öneriliyor; güvenle kullanılabiliyorsa kısa süreli reçetesiz ağrı kesici (NSAİİ) ve sıcak uygulama da seçenekler arasında. Opioidler ilk tedavi olarak rutin kullanılmamalı: Plaseboya göre ağrıyı daha fazla azaltmadılar ama daha çok yan etkiye yol açtılar. Parasetamol plasebodan farklı bulunmadı. Ağrı 1–2 hafta içinde azalmaz ya da artarsa, kas gevşeticiler, fizik tedavi ya da akupunktur gibi en az bir ek tedavi önerilebilir.",
      point="Derlemede fizik tedaviye erken yönlendirme, manipülasyon ve mobilizasyon, kas gevşeticiler ve NSAİİ'lerin yararı orta güvenilirlikteydi; ancak yararlar genel olarak küçüktü ve ilk birkaç haftada ortaya çıkıyordu. Ağrının sürüp sürmeyeceğini en iyi psikososyal etkenler öngördü. Yeni başlayan bel ağrılarının %85'inden fazlasında belirli bir hastalık ya da omurga sorunu bulunmuyor ve çoğu kişi günler ya da haftalar içinde iyileşiyor. Kılavuzu hazırlayan proje ABD Gıda ve İlaç Dairesi (FDA) tarafından finanse edildi.",
      src=[("Amerikan Ağrı Tıbbı Akademisi, 5 Ekim 2026", "https://www.painmed.org/news/acute-low-backpain-guideline-systematic-review-available"), ("Pain Medicine, 2026 (sistematik derleme)", "https://doi.org/10.1093/pm/pnag131"), ("Managed Healthcare Executive, 8 Ekim 2026", "https://www.managedhealthcareexecutive.com/view/new-acute-low-back-pain-guideline-steers-clinicians-away-from-routine-imaging-and-opioids"), ("New York Eyaleti Tabipler Derneği, 9 Ekim 2026", "https://www.mssny.org/pulse-10-9-2026new-acute-low-back-pain-guideline-and-free-resources-for-physicians/")],
      rel=("Bel ağrısı rehberi", "bel-agrisi.html")),
 dict(il=IL_HTN, g="kalp", cat="Tansiyon", date="Ekim 2026",
      title="Yüksek tansiyonu olanların yarısından fazlası bunu bilmiyor olabilir",
      text="Oxford Üniversitesi'nden araştırmacıların BMJ Public Health dergisinde yayımladığı çalışmada, İngiltere'de Our Future Health programına 2022–2025 arasında katılan yaklaşık 1,4 milyon yetişkinin tansiyon ölçümleri incelendi. Katılımcıların %37'sinde yüksek tansiyon vardı: 18–39 yaşlarında %15, 80 yaş ve üzerinde %71. Yaş farkları düzeltildiğinde oran erkeklerde %42, kadınlarda %29'du. Yüksek tansiyonu olanların %59'u hiç tanı ya da tedavi almamıştı; tansiyon ilacı kullananların da yarısında tansiyon hâlâ 140/90 ve üzerindeydi.",
      point="Bu, tek bir zamandaki ölçümlere dayanan kesitsel bir çalışma ve İngiltere'deki gönüllülerden oluşuyor; tek bir ölçüm tanı için yeterli değil. Yüksek tansiyon çoğu zaman belirti vermez, bu yüzden tansiyonunuzu düzenli ölçtürmek önemli. İlaç kullanıyorsanız, hedef değerinize ulaşıp ulaşmadığınızı hekiminizle konuşabilirsiniz.",
      src=[("ScienceDaily (Oxford Üniversitesi), 2 Ekim 2026", "https://www.sciencedaily.com/releases/2026/09/260930225445.htm"), ("BMJ Public Health, 2026", "https://doi.org/10.1136/bmjph-2025-004815"), ("Oxford Üniversitesi, 23 Eylül 2026", "https://www.ox.ac.uk/news/2026-09-23-two-thirds-of-adults-with-high-blood-pressure-do-not-know-they-have-it")],
      rel=("Tansiyon için duvar oturuşu", "duvar-oturusu.html")),
 dict(il=IL_EXPAIN, g="hareket", cat="Ağrı", date="Ekim 2026",
      title="Egzersiz birçok ağrı türünü azaltıyor: 221 bin kişilik büyük derleme",
      text="Avustralya'daki Adelaide Üniversitesi'nden araştırmacılar, egzersizin ağrıya etkisini inceleyen 157 sistematik derlemeyi bir araya getirdi: toplam 2.736 randomize çalışma ve 221.279 katılımcı. PAIN Reports dergisinde yayımlanan analizde egzersiz; kireçlenme, migren, nörolojik ve romatizmal hastalıklar ile kansere bağlı ağrı dahil hem kısa süreli hem uzun süreli ağrıda azalmayla ilişkiliydi. Ağrı 0–10 ölçeğinde ortalama 1,1 puan azaldı. Aerobik egzersiz, direnç çalışması, yoga, pilates ve tai chi'nin hepsinde yarar görüldü; daha düşük yoğunluklu ve haftada toplam 2 saatten kısa programlar da anlamlı fayda sağladı.",
      point="Bu, var olan derlemelerin bir araya getirildiği bir analiz; hangi egzersizin kime en uygun olduğunu söylemiyor. Araştırmacılar bu azalmanın, yaygın ağrı ilaçlarıyla bildirilen ortalama etkiden yaklaşık %60 daha büyük olduğunu belirtiyor; ancak bu karşılaştırma farklı çalışmalardan yapıldı, doğrudan bir karşılaştırma değil. Mesaj yine de net: Ağrıda hareket, tedavinin temel parçalarından biri.",
      src=[("SciTechDaily (Adelaide Üniversitesi), 6 Ekim 2026", "https://scitechdaily.com/study-finds-exercise-may-be-a-surprisingly-powerful-treatment-for-pain/"), ("PAIN Reports, Ağustos 2026", "https://doi.org/10.1097/PR9.0000000000001455"), ("Adelaide Üniversitesi, 24 Eylül 2026", "https://adelaide.edu.au/about/news/2026/less-is-more--exercise-rivals-common-pain-meds/")],
      rel=("Ağrıyı anlamak", "agriyi-anlamak.html")),
 dict(il=IL_SPAF, g="hareket", cat="Kas gücü", date="Ekim 2026",
      title="Kondisyon 30'ların ortasında azalmaya başlıyor; hareket bu düşüşü yavaşlatıyor",
      text="İsveç'teki Karolinska Enstitüsü'nün yürüttüğü SPAF çalışmasında, 1958 doğumlu, rastgele seçilmiş 427 kişinin aerobik kondisyonu, kas dayanıklılığı ve patlayıcı kas gücü 16 yaşından 63 yaşına kadar, 47 yıl boyunca tekrar tekrar ölçüldü. Aerobik kondisyon ve kas dayanıklılığı 26–36 yaş arasında zirveye ulaştı ve 30'ların ortasında azalmaya başladı; patlayıcı güç daha da erken zirve yaptı. Düşüş önce yavaştı, yaş ilerledikçe hızlandı: 63 yaşında performans zirvenin ortalama %30–48 altındaydı. Düşüş kadınlarda ve erkeklerde benzerdi. Yetişkinlikte düzenli harekete başlayanların fiziksel kapasitesi yaklaşık %5–10 arttı.",
      point="Bunlar ortalamalar; herkes 35 yaşında birden güçsüzleşmiyor. Hareket düşüşü tamamen durduramasa da yavaşlatabiliyor ve başlamak için hiçbir yaş geç değil. Ergenlikte aktif olanlar yetişkinlikte de daha iyi kondisyonu korudu. Araştırmacılar katılımcıları 68 yaşında yeniden ölçmeyi planlıyor.",
      src=[("ScienceDaily (Karolinska Enstitüsü), 14 Ekim 2026", "https://www.sciencedaily.com/releases/2026/10/261014000912.htm"), ("Journal of Cachexia, Sarcopenia and Muscle, 2025", "https://doi.org/10.1002/jcsm.70134"), ("Karolinska Enstitüsü, 16 Aralık 2025", "https://news.ki.se/long-term-study-reveals-physical-ability-peaks-at-age-35")],
      rel=("Sarkopeni rehberi", "sarkopeni.html")),
 dict(il=IL_TAICHI, g="hareket", cat="Tai chi", date="Ekim 2026",
      title="Tai chi'nin 20 yılı: Kas-iskelet ağrısında en güçlü kanıt kireçlenmede",
      text="ABD'deki Tufts Medicine'den araştırmacılar, 9 Ekim 2026'da Current Rheumatology Reports'ta yayımlanan derlemede tai chi'nin kronik kas-iskelet ağrısındaki son 12 yıllık çalışmalarını inceledi: 2.031 katılımcılı 19 randomize çalışma ve 34 derleme. Kanıt en güçlü diz ve kalça kireçlenmesindeydi: 28 çalışmayı birleştiren bir analizde tai chi; ağrıda, hareketlilikte, işlevde ve tutuklukta egzersiz yapmayan gruplara göre iyileşme sağladı ve haftalık sıklık ve süre arttıkça ağrıdaki fayda büyüdü. Fibromiyalji ve kronik bel ağrısında sonuçlar umut verici ama çalışmalar arasında farklılık büyük; romatoid artritte kanıt yetersiz.",
      point="Tai chi genel olarak güvenli ve uygulanabilir bir seçenek; Doğu'nun hareket geleneğinin bilimsel yöntemle sınanmasının güzel bir örneği. Ancak bu sistematik değil, anlatısal bir derleme: Çalışmalarda tai chi'nin stili, dozu ve karşılaştırma grupları çok farklı, izlem süreleri çoğunlukla kısa. Faydanın büyüklüğünü kesinleştirmek için daha iyi çalışmalara ihtiyaç var.",
      src=[("Current Rheumatology Reports, 9 Ekim 2026", "https://link.springer.com/article/10.1007/s11926-026-01239-7"), ("Amerikan Romatoloji Koleji kireçlenme kılavuzu, 2020", "https://doi.org/10.1002/acr.24131"), ("NCCIH, Tai chi bilgi sayfası (Aralık 2023)", "https://nccih.nih.gov/health/taichi/introduction.htm")],
      rel=("Diz kireçlenmesi rehberi", "diz-kireclenmesi.html")),
 dict(il=IL_PDACT, g="hareket", cat="Parkinson", date="Ekim 2026",
      title="Parkinson'da daha çok hareket, daha yavaş ilerlemeyle ilişkili",
      text="ABD'de Cincinnati Üniversitesi'nden araştırmacıların 7 Ekim 2026'da Neurology dergisinde yayımladığı çalışmada, hafif ve orta evre Parkinson hastası 294 kişi 7 yıla kadar izlendi. Katılımcılar iş, ev işleri ve hobiler dahil haftada kaç saat orta ya da yüksek tempolu aktivite yaptıklarını bildirdi ve üç gruba ayrıldı: 4 saate kadar, 4–8 saat ve 8 saatten fazla. 30 puanlık düşünme testinde yıllık düşüş en az hareket edenlerde 0,478 puan, en çok hareket edenlerde yalnızca 0,007 puandı. Hareket belirtileri puanı (0–132; başlangıç ortalaması 23) en az hareket edenlerde yılda 0,143 puan kötüleşirken en çok hareket edenlerde yılda 0,783 puan hafifledi. Toplam süreye, yoğunlukla ağırlıklandırılmış miktara ve yalnızca yüksek tempolu aktiviteye bakıldığında da benzer ilişki görüldü.",
      point="Bu bir gözlem çalışması: Hareketin hastalığı yavaşlattığını kanıtlamıyor. Aktivite, kişilerin kendi beyanıyla anketle ölçüldü ve gruplar arasındaki farklar küçüktü; araştırmacılara göre bu küçük farklar yıllar içinde anlam kazanabilir. Katılımcıların düşünme becerileri başlangıçta iyiydi; %98'i beyaz ve üçte ikisi erkekti. Healio'nun aktardığına göre yoğunluk tek başına ele alındığında puanlardaki değişimle anlamlı ilişki göstermedi; araştırmacılar toplam sürenin yoğunluktan daha belirleyici olabileceğini düşünüyor. Yüksek tempolu egzersizin etkisini sınayan SPARX3 adlı randomize çalışma sürüyor. Yine de düzenli hareketin Parkinson'da ne kadar değerli olduğunu destekleyen bir veri daha.",
      src=[("Amerikan Nöroloji Akademisi (EurekAlert), 7 Ekim 2026", "https://www.eurekalert.org/news-releases/1146272"), ("U.S. News, 8 Ekim 2026", "https://www.usnews.com/news/health-news/articles/2026-10-08/exercise-can-slow-parkinsons-progression-study-says"), ("Neurology, 7 Ekim 2026", "https://doi.org/10.1212/WNL.0000000000218682"), ("Healio, 14 Ekim 2026", "https://www.healio.com/news/neurology/20261014/physical-activity-associated-with-slower-cognitive-motor-decline-in-parkinsons-disease"), ("ScienceDaily, 23 Ekim 2026", "https://www.sciencedaily.com/releases/2026/10/261022081306.htm")],
      rel=("Parkinson rehberi", "parkinson.html")),
 dict(il=IL_OA2050, g="hareket", cat="Kireçlenme", date="Ekim 2026",
      title="2050'de bir milyar kişide kireçlenme olabilir",
      text="The Lancet'te Ekim 2026'da yayımlanan ve Avustralya'daki Curtin Üniversitesi'nin öncülük ettiği küresel sağlık politikası yol haritasına göre 2023'te yaklaşık 600 milyon kişide osteoartrit (kireçlenme) vardı; bu sayı 2050'ye kadar bir milyara yaklaşabilir. Kireçlenmenin yol açtığı engellilik yükü 1990–2023 arasında %65 arttı. Yaşlanan nüfus, artan obezite ve eklem yaralanmaları artışın başlıca nedenleri olarak gösteriliyor.",
      point="Yazarlar kireçlenmenin yaşlanmanın kaçınılmaz bir parçası gibi görülmemesini; birinci basamak sağlık hizmetlerine ve rehabilitasyona dahil edilmesini, düşük değerli tedavilerin azaltılıp hareketi destekleyen yaklaşımların yaygınlaştırılmasını istiyor. Diz kireçlenmesinde fazla kilo ve eklem yaralanmaları değiştirilebilir risk etkenleri. Avustralya'da 2009–10 yıllarına ait bir çalışmada kireçlenme başvurularının yalnızca %43'ü en iyi uygulama standartlarını karşılıyordu.",
      src=[("Knowridge, 14 Ekim 2026", "https://knowridge.com/2026/10/a-common-form-of-arthritis-could-affect-nearly-a-billion-people-by-2050/"), ("Medical Xpress, Ekim 2026", "https://medicalxpress.com/news/2026-10-billion-people-osteoarthritis-international-experts.html"), ("Curtin Üniversitesi, 12 Ekim 2026", "https://www.curtin.edu.au/research/news/nearly-one-billion-people-could-live-with-osteoarthritis-by-2050-international-experts-warn?type=media")],
      rel=("Diz kireçlenmesi rehberi", "diz-kireclenmesi.html")),
 dict(il=IL_ACLX, g="hareket", cat="Diz", date="Eylül 2026",
      title="Ön çapraz bağ ameliyatından sonra süren diz yakınmalarında gözetimli egzersiz güvenli, yararı ılımlı",
      text="Avustralya'da La Trobe Üniversitesi'nin yürüttüğü ve 29 Eylül 2026'da Annals of Internal Medicine'de yayımlanan SUPER-Knee çalışmasına, ön çapraz bağ ameliyatından 9–36 ay sonra hâlâ diz yakınmaları olan 18–40 yaş arası 184 kişi katıldı. Yarısı 4 ay boyunca fizyoterapist gözetiminde ilerleyici egzersiz ve eğitim aldı; diğer yarısı tek bir eğitim seansı ve kendi başına egzersiz için kaynaklar. 4. ayda diz yakınma ve işlev puanı (KOOS4, 0–100) gözetimli grupta 14,1, diğer grupta 9,4 puan iyileşti; aradaki fark 4,8 puandı. Ağrıda anlamlı düzelme bildirenler %73'e karşı %40'tı ve uyluk kas gücü gözetimli grupta daha çok arttı. MR'da kıkırdak kalınlığı ve yapısında iki grup arasında 4. ve 12. ayda fark görülmedi.",
      point="Aradaki fark ılımlı ve 12. ayda, kontrol grubu da iyileşmeye devam ettiği için daraldı. Çalışma körlenmemişti; katılımcılar hangi grupta olduklarını biliyordu ve sonuçların çoğu kendi bildirimlerine dayanıyor. Ön çapraz bağ ameliyatı olan genç yetişkinler erken diz kireçlenmesi açısından risk altında; bu çalışmada yoğun egzersizin kıkırdağa zarar verdiğine dair bir işaret görülmedi.",
      src=[("Annals of Internal Medicine, 29 Eylül 2026", "https://doi.org/10.7326/ANNALS-26-02460"), ("News-Medical, 29 Eylül 2026", "https://news-medical.net/news/20260929/Exercise-therapy-reduces-knee-osteoarthritis-risk-after-ACL-surgery.aspx"), ("Medical Dialogues, 5 Ekim 2026", "https://medicaldialogues.in/orthopaedics/news/supervised-physical-therapy-provides-greater-pain-relief-after-acl-surgery-jama-180518")],
      rel=("Ön çapraz bağ rehberi", "on-capraz-bag.html")),
 dict(il=IL_ISOWEEK, g="kalp", cat="Tansiyon", date="Eylül 2026",
      title="Duvar oturuşunun tansiyona etkisi haftada bir seansla da sürebilir",
      text="BMJ Open Sport & Exercise Medicine dergisinde yayımlanan randomize kontrollü çalışmaya, büyük tansiyonu 120–140 mmHg arasında olan, düzenli egzersiz yapmayan ve yaş ortalaması 37 olan 100 yetişkin katıldı. Katılımcılar 4 hafta boyunca haftada 3 kez evde duvar oturuşu yaptı: her seansta 4 tekrar, aralarında 2 dakika oturarak dinlenme. Ardından 4 hafta boyunca haftada 3, 2 ya da 1 seansa devam ettiler ya da bıraktılar. 8. haftada büyük tansiyon başlangıca göre haftada 3 seansla 13,7, 2 seansla 7,0, 1 seansla 6,6 mmHg daha düşüktü; bırakanlarda ise tansiyon kontrol grubundan farksız düzeye döndü.",
      point="Katılımcıların hiçbirinde yüksek tansiyon yoktu ve bakım dönemi yalnızca 4 hafta sürdü; daha uzun çalışmalara ihtiyaç var. Haftada 1–2 seans kısa vadede düşüşü korumaya yetebilir, ama damar direnci ve kalp hızı değişkenliğindeki ek yararlar yalnızca haftada 3 seansla korundu. Tansiyonunuz yüksekse ya da tansiyon ilacı kullanıyorsanız başlamadan önce hekiminize danışın.",
      src=[("BMJ Group, 29 Eylül 2026", "https://bmjgroup.com/a-weekly-session-of-isometric-exercise-training-may-maintain-lower-blood-pressure/"), ("BMJ Open Sport & Exercise Medicine, 2026", "https://doi.org/10.1136/bmjsem-2025-003172"), ("News-Medical, 29 Eylül 2026", "https://www.news-medical.net/news/20260929/Weekly-isometric-exercise-may-maintain-short-term-blood-pressure-reductions.aspx")],
      rel=("Tansiyon için duvar oturuşu", "duvar-oturusu.html")),
 dict(il=IL_YSTROKE, g="beyin", cat="İnme", date="Eylül 2026",
      title="ABD'nin bir bölgesinde gençlerde inme 30 yılda neredeyse iki katına çıktı",
      text="ABD'de Cincinnati ve Kuzey Kentucky bölgesinde 1993–2020 arasında 20–54 yaş arası yetişkinlerde görülen 2.076 inmenin incelendiği ve 23 Eylül 2026'da Neurology dergisinde yayımlanan çalışmada, bu yaş grubunda inme sıklığı 100 binde 33,9'dan 62,2'ye, yaklaşık %83 arttı. Damar tıkanmasına bağlı (iskemik) inme 100 binde 23,8'den 47,3'e çıktı. İnme geçirenler arasında madde kullanımı bildirenlerin oranı %4,6'dan %40,2'ye yükseldi; bu artışın büyük kısmı esrardan kaynaklanıyordu. Aynı dönemde inmeden sonraki 30 gün içinde ölüm oranı %11,7'den %9,4'e geriledi.",
      point="Çalışma tek bir bölgeden ve gözleme dayalı; madde kullanımının ya da başka bir etkenin bu artışa yol açtığını kanıtlamıyor. Yine de inme yalnızca yaşlıların sorunu değil: Yüzde kayma, kolda güçsüzlük ya da konuşma bozukluğu gibi ani belirtilerde, yaşınız ne olursa olsun hemen 112'yi arayın.",
      src=[("ScienceDaily, 15 Ekim 2026", "https://www.sciencedaily.com/releases/2026/10/261014015459.htm"), ("Neurology, 23 Eylül 2026", "https://doi.org/10.1212/WNL.0000000000218622"), ("Cincinnati Üniversitesi, 23 Eylül 2026", "https://www.uc.edu/news/articles/2026/09/more-young-adult-strokes-uc-study.html")],
      rel=("İnme sonrası rehabilitasyon", "inme-rehabilitasyonu.html")),
 dict(il=IL_BLOOD, g="tani", cat="Alzheimer", feat=True, date="Eylül 2026",
      title="Alzheimer için kan testleri çoğalıyor",
      text="ABD'de Gıda ve İlaç Dairesi (FDA), Mayıs 2025'ten bu yana beyindeki amiloid ve tau değişikliklerini kandan ölçen dört testin kullanımına izin verdi. Son ikisi Ağustos 2026'da geldi. Bu testler beyin görüntülemesine ya da bel sıvısı alınmasına gerek kalmadan tanıyı kolaylaştırabilir.",
      point="Önemli: Testler yalnızca hafıza şikâyeti olan kişilerde, hekim değerlendirmesinin parçası olarak kullanılmak üzere izin aldı. Şikâyeti olmayan sağlıklı kişilerde tarama için uygun değiller.",
      src=[("TIME, 22 Eylül 2026", "https://time.com/article/2026/09/22/who-should-get-new-blood-tests-for-alzheimers-disease/"), ("Healio, 21 Ağustos 2026", "https://www.healio.com/news/neurology/20260821/fda-clears-precivityad2-alzheimers-disease-blood-test-as-early-as-age-40-years"), ("Pharmacy Times, 25 Ağustos 2026", "https://www.pharmacytimes.com/view/fda-clears-elecsys-phospho-tau-blood-test-for-alzheimer-disease")]),
 dict(il=IL_ONCOEX, g="hareket", cat="Kanser", date="Eylül 2026",
      title="Kanser tedavisinde yapılandırılmış egzersiz: daha uzun yaşam, daha az nüks",
      text="British Journal of Sports Medicine'da yayımlanan sistematik derleme ve meta-analizde, kanser hastalarında yapılandırılmış egzersiz programlarını inceleyen 21 randomize çalışma bir araya getirildi: 8.449 katılımcı (%88'i kadın, yaş ortalaması 54, ortalama izlem 64 ay); en sık meme, ardından bağırsak ve pankreas kanseri. Egzersiz programına katılanlarda genel sağkalım analizinde ölüm olasılığı %23, ölüm öncesi nüks olasılığı %17, kansere bağlı ölüm %26 daha düşüktü. Aerobik egzersiz tek başına ya da kuvvet egzersiziyle birlikte daha iyi sağkalımla ilişkiliydi; yalnızca kuvvet egzersizi için kanıt tek bir küçük çalışmaya dayanıyordu. Programın en az %70'ini tamamlayanlarda ilişki daha güçlüydü ve fayda en çok erken evre hastalıkta görüldü.",
      point="Kanserin ilerlemesinin geciktiğine dair net bir kanıt bulunmadı. Karşılaştırma gruplarındaki hastalar da daha sağlıklı alışkanlıklar edinmiş olabilir; egzersizin türü, süresi ve yoğunluğu çalışmalar arasında çok farklıydı ve kanıtın büyük kısmı meme kanserinden geliyor, ileri evre hastalık için veri az. Egzersize başlamadan önce tedavi ekibinizle konuşun.",
      src=[("BMJ Group, 15 Eylül 2026", "https://bmjgroup.com/structured-exercise-linked-to-longer-cancer-survival-and-time-free-of-disease/"), ("British Journal of Sports Medicine, 2026", "https://doi.org/10.1136/bjsports-2026-111664"), ("ecancer, 16 Eylül 2026", "https://ecancer.org/en/news/28911-structured-exercise-linked-to-longer-cancer-survival-and-time-free-of-disease")],
      rel=("Kanser tedavisinde egzersiz", "kanser-egzersiz.html")),
 dict(il=IL_SLEEPST, g="beyin", cat="Uyku", date="Eylül 2026",
      title="Uykunun süresi kadar evreleri de önemli olabilir",
      text="İngiltere'deki UK Biobank çalışmasına katılan yaklaşık 96 bin kişi bir hafta boyunca bileğinde hareket ölçer taşıdı; bir yapay zekâ algoritması bu verilerden uyku evrelerini tahmin etti. Yaklaşık 9 yıllık izlemde, gece REM uykusu daha uzun olanlarda 83 hastalığın riski daha düşüktü: REM uykusundaki yaklaşık 48 dakikalık fark, kalp yetmezliğinde %26, demansta %46 daha düşük riskle ilişkiliydi. Daha uzun derin uyku 7 hastalıkta (tip 2 diyabet ve majör depresyon dahil) daha düşük, düzensiz uyku ve gece uyanmaları ise kaygı gibi sorunlarda daha yüksek riskle ilişkiliydi. Gece 5 saatten az uyumak 37 hastalıkla ilişkiliydi; çoğu hastalıkta risk 6–8 saatte en düşüktü.",
      point="Bu bir gözlem çalışması: Uykunun bu hastalıklara yol açtığını göstermiyor; henüz tanı almamış hastalıklar da uykuyu bozmuş olabilir. Bilekten ölçülen hareket, uyku evrelerini ancak kabaca tahmin edebiliyor. Yine de düzenli ve yeterli uykunun önemini hatırlatan güçlü bir veri.",
      src=[('PLOS Medicine, 17 Eylül 2026', 'https://doi.org/10.1371/journal.pmed.1005213'), ('Science Media Centre, uzman görüşleri', 'https://www.sciencemediacentre.org/?p=58503'), ('Healio, 23 Eylül 2026', 'https://www.healio.com/news/primary-care/20260923/sleep-patterns-may-influence-over-150-diseases')],
      rel=('İyi uyku rehberi', 'uyku.html')),
 dict(il=IL_CADENCE, g="hareket", cat="Yürüyüş", date="Eylül 2026",
      title="Az adım atıyorsanız tempo önemli olabilir",
      text="Sidney Üniversitesi'nin yürüttüğü ve Eylül 2026'da British Journal of Sports Medicine'de yayımlanan çalışmada, UK Biobank'ta adımları bileğe takılan cihazla ölçülen orta yaşlı yetişkinler ortalama 8 yıl izlendi. Günlük adım sayısının yanında, günün en tempolu 30 dakikasındaki ortalama adım hızı (dakikada adım) da hesaplandı; bu dakikaların art arda olması gerekmiyordu. Günde 5.000'den az adım atan ama bu adımları daha tempolu atanlarda ölüm ve kalp-damar hastalığından ölüm riski belirgin olarak daha düşüktü ve günde 5.000–7.500 adımı yavaş tempoda atanlarla benzerdi. Tempodan bağımsız olarak en düşük risk günde 7.500–10.000 adım atanlarda görüldü; tüm adım gruplarında en düşük risk, dakikada yaklaşık 90–100 adımlık zirve tempo civarında toplanıyordu.",
      point="Bu bir gözlem çalışmasıdır; tempolu yürümenin ömrü uzattığını kanıtlamaz. Henüz fark edilmemiş hastalıklar hem adım sayısını hem de riski etkilemiş olabilir; bilekteki cihazlar adım dışı hareketleri de sayabilir ve adımlar çalışmanın yalnızca bir döneminde ölçüldü. Yazarlar bu ölçünün her gün kesintisiz 30 dakika o tempoda yürümek diye yorumlanmaması gerektiğini vurguluyor. Günde 10.000 adım hedefi ise kanıttan çok 1960'lardaki bir Japon adımsayar kampanyasından geliyor; bugünkü adım sayınızı kademeli artırmak ve bir kısmını tempolu yürümek iyi bir başlangıç.",
      src=[("British Journal of Sports Medicine, Eylül 2026", "https://doi.org/10.1136/bjsports-2025-111173"), ("News-Medical, 10 Eylül 2026", "https://www.news-medical.net/news/20260910/You-may-not-need-10000-steps-if-some-of-them-are-taken-at-a-faster-pace.aspx"), ("Scripps News, 9 Eylül 2026", "https://www.scrippsnews.com/health/faster-walking-pace-associated-with-longer-lifespan-in-new-study"), ("ScienceAlert, 13 Eylül 2026", "https://www.sciencealert.com/?p=218938")],
      rel=("Adım hedefi planlayıcısı", "adim-hedefi.html")),
 dict(il=IL_NMJ, g="hareket", cat="Sarkopeni", date="Eylül 2026",
      title="Yaşla gelen kas güçsüzlüğünde gözden kaçan halka",
      text="Sinirden gelen “kasıl” komutu kasa, sinir-kas kavşağı denen bağlantı noktasından geçer. Missouri Üniversitesi'nin öncülük ettiği çalışmada, güçsüz yaşlılarda bu geçişin aksadığı ve aksamanın güçsüzlüğün derecesiyle ilişkili olduğu görüldü. Yaşlı kemirgenlerde de aynı aksama vardı; kavşaktaki kas zarında NaV1.4 adlı sodyum kanalı azalmıştı. ClC-1 adlı klor kanalını kısmen engelleyen bir ilaç, yaşlı kemirgenlerde kasın sinir uyarısına yanıtını ve kas işlevini iyileştirdi.",
      point="İlacın etkisi şimdilik yalnızca hayvanlarda gösterildi. Aynı yoldan etki eden ignaseclant, kalıtsal bir sinir hastalığında (Charcot-Marie-Tooth) insanda denendi; yaşlılarda kas güçsüzlüğü için henüz denenmedi. Bugün sarkopenide en etkili tedavi, kasları dirence karşı çalıştıran egzersiz.",
      src=[('Journal of Clinical Investigation, 1 Eylül 2026', 'https://jci.org/articles/view/190646/pdf'), ('ScienceDaily (Missouri Üniversitesi), 24 Eylül 2026', 'https://www.sciencedaily.com/releases/2026/09/260923035924.htm'), ('Nautilus, 24 Eylül 2026', 'https://nautil.us/can-a-drug-reverse-age-related-muscle-weakness-1285260')],
      rel=('Sarkopeni rehberi', 'sarkopeni.html')),
 dict(il=IL_KIDNEY, g="gen", cat="Organ nakli", date="Eylül 2026",
      title="Domuz böbreği, insan böbreğine köprü oldu",
      text="ABD'de son dönem böbrek yetmezliği olan 66 yaşındaki Tim Andrews'a genetiği düzenlenmiş bir domuzdan böbrek nakledildi. Böbrek onu 271 gün diyalizden uzak tuttu; bu, yaşayan bir alıcıda belgelenen en uzun süre. Enfeksiyon nedeniyle bağışıklık baskılayıcı ilaçlar azaltılınca domuz böbreği hasar görmeye ve işlevini yitirmeye başladı; Andrews Ocak 2026'da bağışçıdan insan böbreği aldı ve yeni böbrek hemen çalışmaya başladı.",
      point="Organ bekleme listelerinin uzunluğu düşünüldüğünde umut verici bir adım. Ancak şimdilik az sayıda hastadan elde edilen deneyimler var; genetiği düzenlenmiş domuz böbreklerinin güvenliği ve kalıcılığı klinik çalışmalarda araştırılıyor.",
      src=[("The Lancet, 9 Eylül 2026", "https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(26)01295-X/abstract"), ("Mass General Brigham", "https://news.massgeneralbrigham.org/en/pig-kidney-xenotransplant-bridge-to-human-transplant"), ("HealthDay (MedicineNet), 9 Eylül 2026", "https://www.medicinenet.com/pig_kidney_kept_man_alive_while_waiting_donation/news.htm")]),
 dict(il=IL_HD, g="beyin", cat="Huntington", date="Eylül 2026",
      title="Huntington'da ilk gen tedavisi için onay başvurusu: 4. yıl verileri karışık",
      text="Huntington, kalıtsal ve ilerleyici bir beyin hastalığı; hareketi, düşünmeyi ve duygu durumunu etkiliyor ve gidişini yavaşlattığı kanıtlanmış bir tedavisi yok. uniQure'un geliştirdiği AMT-130, MR eşliğinde yapılan tek seferlik bir ameliyatla beynin derinindeki striatum bölgesine veriliyor ve hastalığa yol açan hatalı huntingtin proteininin üretimini azaltmayı hedefliyor. Yüksek dozu alan hastalarda 3. yılda hastalığın ilerlemesi, karşılaştırma grubuna göre %75 daha yavaştı; şirket Eylül 2026'da ABD ve İngiltere'de onay başvurusu yaptı.",
      point="Sonuçlar faz I/II çalışmalardaki az sayıda hastaya ve plasebo grubu yerine hastalık kayıtlarından seçilen benzer hastalarla karşılaştırmaya dayanıyor. 29 Eylül'de açıklanan 4. yıl verilerinde ana ölçekteki fark %44'e indi ve istatistiksel olarak anlamlı değildi; günlük işlev ölçeğinde %61'lik yavaşlama sürüyordu. Yüksek dozu alanların %17'sinde beyinde iltihapla ilişkili ciddi yan etki görüldü; bunların hepsi düzeldi.",
      src=[('uniQure, 29 Eylül 2026', 'https://www.globenewswire.com/news-release/2026/09/29/3370692/0/en/uniqure-announces-additional-data-from-ongoing-phase-i-ii-studies-of-ifezuntirgene-inilparvovec-amt-130-in-huntington-s-disease-showing-continued-slowing-of-disease-progression.html'), ('BioPharm International, 2 Eylül 2026', 'https://www.biopharminternational.com/view/uniqure-submits-bla-and-maa-for-amt-130-gene-therapy-in-huntington-s-disease'), ('NeurologyLive, 2 Eylül 2026', 'https://www.neurologylive.com/view/uniqure-submits-bla-gene-therapy-huntington-disease')]),
 dict(il=IL_TAVA, g="beyin", cat="Parkinson", date="Eylül 2026",
      title="Parkinson'da yeni etki biçimli ilaç: tavapadon",
      text="FDA, 28 Eylül 2026'da AbbVie'nin tavapadon (JUVMO) adlı ilacını onayladı. Günde bir kez alınan tablet, beyindeki dopamin reseptörlerinden D1 ve D5'i seçici olarak uyaran ilk ilaç; bugün kullanılan dopamin agonistleri ağırlıklı olarak D2 ve D3 reseptörlerine etki ediyor. Tek başına ya da levodopayla birlikte kullanılabiliyor. Levodopa alan hastalarda, rahatsız edici istemsiz hareketler olmadan iyi geçen “açık” süreyi günde 1,7 saat artırdı; plaseboda artış 0,6 saatti.",
      point='En sık yan etkiler bulantı, baş ağrısı, tat bozukluğu, yorgunluk ve baş dönmesi; ayağa kalkarken tansiyon düşmesi, halüsinasyon ve kumar gibi dürtü kontrol sorunları açısından dikkatli olunmalı. Yeni ilaçlar hareketi kolaylaştırsa da Parkinson hastalığında düzenli egzersiz tedavinin temel parçası olmaya devam ediyor.',
      src=[('AbbVie, 28 Eylül 2026', 'https://news.abbvie.com/2026-09-28-U-S-FDA-Approves-AbbVies-JUVMO-TM-tavapadon-for-Parkinsons-Disease'), ('Healio, 28 Eylül 2026', 'https://www.healio.com/news/neurology/20260928/fda-approves-juvmo-first-and-only-d1d5-receptor-agonist-for-parkinsons-disease'), ('NeurologyLive, 28 Eylül 2026', 'https://www.neurologylive.com/view/fda-approves-tavapadon-for-the-treatment-of-parkinson-disease')],
      rel=('Parkinson rehberi', 'parkinson.html')),
 dict(il=IL_BELT, g="hareket", cat="Bel ağrısı", date="Ağustos 2026",
      title="Bel ağrısında yumuşak bel korsesi: 12 haftada günlük işlevde ılımlı ek iyileşme",
      text="Fransa'da 17 merkezde yürütülen ve 19 Ağustos 2026'da JAMA Network Open'da yayımlanan LOMBACT çalışmasına, 1–6 aydır süren ve belirli bir nedene bağlanamayan bel ağrısı olan 168 yetişkin (yaş ortalaması 49) katıldı. Katılımcıların yarısı olağan bakımın yanında gün içinde 4–8 saat yumuşak, ayarlanabilir bir bel korsesi taktı; diğer yarısı yalnızca olağan bakım aldı. İki gruba da aktif kalmaları önerildi. 12 haftada günlük kısıtlılık puanı (Oswestry, 0–100) korse grubunda 10, diğer grupta 5,3 puan iyileşti; kısıtlılığı en az %30 azalanlar korse grubunda yaklaşık %61, diğer grupta %41 oldu. Korse grubunda ağrı, özellikle hareket sırasındaki ağrı, daha çok azaldı; ağrı kesici kullananların oranı da daha düşüktü (yaklaşık yarıya karşı üçte iki). Korsenin sensör verilerine göre katılımcılar onu taktıkları günlerde ortalama 4 saat kadar kullandı; altı kişide rahatsızlık ya da ciltte tahriş gibi hafif sorunlar görüldü.",
      point="Katılımcılar hangi grupta olduklarını biliyordu ve sahte bir korseyle karşılaştırma yapılmadı; beklentiler sonucu etkilemiş olabilir. İzlem yalnızca 12 hafta sürdü, korse bırakıldıktan sonraki durum incelenmedi ve çalışmayı korseyi üreten şirket finanse etti. Dünya Sağlık Örgütü 2023'te, kronik bel ağrısında korse ya da destek kemerlerinin rutin olarak önerilmemesini tavsiye etmişti. Araştırmacılar da korsenin aktif tedavinin yerine geçmemesi gerektiğini, hareket sırasındaki rahatsızlığı azaltarak bazı hastaların aktif kalmasına yardımcı olabileceğini vurguluyor.",
      src=[("JAMA Network Open, 19 Ağustos 2026", "https://doi.org/10.1001/jamanetworkopen.2026.29793"), ("ScienceAlert, 5 Eylül 2026", "https://www.sciencealert.com/?p=217137"), ("Harvard Health Publishing, 16 Ekim 2026", "https://www.health.harvard.edu/bones-and-joints/a-lumbar-belt-may-help-ease-low-back-pain")],
      rel=("Bel ağrısı rehberi", "bel-agrisi.html")),
 dict(il=IL_DEMPA, g="beyin", cat="Demans", date="Ağustos 2026",
      title="Boş zamanda hareket demans riskini azaltıyor; ağır bedensel iş ise artırabilir",
      text="ABD'de Güney Kaliforniya Üniversitesi'nden ve Brezilya'dan araştırmacıların The Lancet Public Health'te yayımladığı derlemede 30 ülkeden 74 çalışma ve 4,2 milyondan fazla kişinin verisi birleştirildi (ortanca izlem 10 yıl, 64 binden fazla demans vakası). Genel olarak en aktif olanlarda demans riski %20, Alzheimer riski %21, damarsal demans riski %29 daha düşüktü. Ama hareketin türü önemliydi: Boş zamanda yapılan spor, dans ve egzersizle risk %24 daha düşükken, bedensel olarak yorucu işlerde çalışanlarda %20 daha yüksekti ve iş ağırlaştıkça risk artıyordu. Ev işleriyle %15 daha düşük, yürüyerek ya da bisikletle işe gidip gelmekle %10 daha yüksek risk görüldü; bu ikisi çok az çalışmaya dayanıyor.",
      point="Bu, gözlem çalışmalarının derlemesi: Ağır işin demansa yol açtığını kanıtlamıyor ve kanıtın kesinliği düşük ile çok düşük arasında. Araştırmacılar bu ‘hareket paradoksunu’ ağır işlerdeki stres, yetersiz toparlanma, iş üzerinde az söz hakkı, gürültü ve hava kirliliği gibi etkenlerle açıklamaya çalışıyor. Pratik çıkarım: Gün boyu yorucu bir işte çalışmak, isteyerek ve dinlenerek yapılan hareketin yerini tutmayabilir.",
      src=[("PsyPost, 8 Eylül 2026", "https://www.psypost.org/massive-study-reveals-a-physical-activity-paradox-in-dementia-risk/"), ("The Lancet Public Health, 2026", "https://doi.org/10.1016/S2468-2667(26)00142-8"), ("Güney Kaliforniya Üniversitesi (USC), 18 Ağustos 2026", "https://today.usc.edu/why-you-move-not-just-how-often-could-affect-dementia-risk/")],
      rel=("Demansta egzersiz rehberi", "demans-egzersiz.html")),
 dict(il=IL_REACT, g="kalp", cat="Damar sağlığı", date="Ağustos 2026",
      title="Belirtisi olmayan yetişkinlerin yarısından fazlasında damar plağı",
      text="Danimarka ve İspanya'da 18–70 yaş arası, bilinen kalp-damar hastalığı olmayan 16.808 kişinin boyun, bacak ve kalp damarları ileri görüntüleme yöntemleriyle tarandı. 29 Ağustos 2026'da Avrupa Kardiyoloji Derneği kongresinde sunulan ve New England Journal of Medicine'de yayımlanan REACT çalışmasında katılımcıların %57,1'inde damar duvarında plak (ateroskleroz) bulundu. 18–29 yaş arasında her 13 kişiden birinde en az bir damarda plak vardı; 60–70 yaşta bu oran 10 kişide yaklaşık 9'du. Erkeklerde plak kadınlardan 5–10 yıl önce başlıyordu; kadınlarda en hızlı artış, menopoz dönemine denk gelen 40–60 yaş arasındaydı.",
      point="Kalp riskini tahmin etmek için kullanılan SCORE2 gibi standart hesaplamalar, plağı olan kişilerin yalnızca küçük bir kısmını yakaladı. Ancak bu bir yaygınlık çalışması: Herkesi taramanın ya da görüntülemeye göre koruyucu tedavi vermenin kalp krizlerini azalttığı henüz gösterilmedi; bunu sınayacak ikinci aşama planlanıyor. Bulgu, damar sağlığının gençlikte başladığını hatırlatıyor.",
      src=[("News-Medical (ESC Kongresi), 29 Ağustos 2026", "https://www.news-medical.net/news/20260829/New-study-detects-silent-atherosclerosis-in-healthy-young-adults.aspx"), ("New England Journal of Medicine, 2026", "https://doi.org/10.1056/NEJMoa2609059"), ("CNIC, 29 Ağustos 2026", "https://www.cnic.es/en/node/244034")],
      rel=("Ne kadar hareket yeterli?", "hareket.html")),
 dict(il=IL_OREX, g="beyin", cat="Uyku", date="Ağustos 2026",
      title='Tip 1 narkolepside eksik beyin sinyalinin yerini tutan ilk ilaç',
      text="Tip 1 narkolepside beyinde uyanıklığı düzenleyen oreksin (hipokretin) adlı maddeyi üreten hücreler kaybolur; kişi gün içinde karşı konulamaz uyku ataklarıyla boğuşur, güldüğünde ya da heyecanlandığında kasları aniden gevşeyebilir (katapleksi). FDA, 5 Ağustos 2026'da Takeda'nın oveporekston (Orzeyful) adlı ilacını, eksik oreksin sinyalinin yerini tutan ilk ilaç olarak onayladı. 273 hastalık iki çalışmada gündüz uyanıklığı arttı, uykululuk ve katapleksi atakları belirgin şekilde azaldı.",
      point="FDA'ya göre hastalığın altta yatan biyolojisini etkileyen ilk ilaç. Günde iki kez alınıyor; en sık yan etkiler uykusuzluk, sık idrara çıkma ve tükürük artışı. 18 yaş altında güvenliği ve etkinliği henüz bilinmiyor.",
      src=[('FDA, 5 Ağustos 2026', 'https://www.fda.gov/news-events/press-announcements/fda-approves-first-drug-treat-full-range-narcolepsy-type-1-symptoms'), ('Healio, 7 Ağustos 2026', 'https://www.healio.com/news/neurology/20260807/fda-approves-orzeyful-for-type-1-narcolepsy-in-adults'), ('NeurologyLive, 5 Ağustos 2026', 'https://www.neurologylive.com/view/fda-approves-orexin-agonist-oveporexton-narcolepsy-type-1')]),
 dict(il=IL_RAS, g="gen", cat="Kanser", feat=True, date="Ağustos 2026",
      title="Pankreas kanserinde RAS'ı hedefleyen ilk ilaç",
      text="Pankreas kanserlerinin %90'dan fazlasında tümörü büyüten RAS genlerinde (çoğunlukla KRAS) mutasyon bulunuyor. Uzun süre ilaçla hedeflenemez sanılan RAS'ın yalnızca tek bir mutasyonunu hedefleyen ilaçlar akciğer ve kalın bağırsak kanserlerinde kullanılıyordu; RAS'ın birçok biçimini birden engelleyen daraksonrasib (Rasonque) ise 26 Ağustos 2026'da FDA onayı aldı. Daha önce tedavi görmüş, yayılmış pankreas kanseri olan 500 hastalık RASolute 302 çalışmasında ortanca yaşam süresi kemoterapiyle 6,7 ay, daraksonrasiple 13,2 ay oldu.",
      point="Günde bir kez tablet olarak alınıyor. En sık yan etkiler döküntü, ishal, ağız yaraları ve bulantı. STAT'a konuşan bir onkolog onu pankreas kanserinde onlarca yılın en önemli gelişmesi olarak niteledi; ilacın ilk basamak tedavide kullanıldığı çalışmalar sürüyor.",
      src=[('FDA, 26 Ağustos 2026', 'https://www.fda.gov/news-events/press-announcements/fda-approves-first-class-targeted-therapy-metastatic-pancreatic-cancer'), ('STAT', 'https://www.statnews.com/2026/08/26/pancreatic-cancer-drug-rasonque-approved/'), ('The ASCO Post, Ağustos 2026', 'https://www.ascopost.com/news/august-2026/fda-approves-daraxonrasib-for-metastatic-pancreatic-adenocarcinoma/')]),
 dict(il=IL_VACCINE, g="gen", cat="Kanser", date="Ağustos 2026",
      title="Kişiye özel mRNA kanser aşısı melanomda ilk kez bir faz III çalışmasının hedefine ulaştı",
      text="Merck ve Moderna'nın geliştirdiği intismeran, her hastanın tümöründeki mutasyonlara göre ayrı ayrı üretilen bir mRNA aşısı. Ameliyatla tümörü tamamen çıkarılmış evre IIB–IV melanomlu 1.137 hastanın katıldığı INTerpath-001 çalışmasında aşı, bir bağışıklık ilacıyla (pembrolizumab) birlikte verildi ve tek başına ilaca göre hastalığın geri dönmesini ve uzak organlara yayılmasını geciktirdi.",
      point="Ayrıntılı sayılar henüz açıklanmadı; sonuçlar bir tıp kongresinde sunulacak. Önceki faz IIb çalışmasında nüks ya da ölüm riski %49 daha düşük bulunmuştu. Yeni bir güvenlik sorunu görülmedi. Yaşam süresine etkisi henüz bilinmiyor; çalışma bunu izlemeyi sürdürüyor. Aşı hâlâ deneysel, hiçbir ülkede onaylı değil ve sonuç yalnızca ameliyat edilmiş ileri evre melanom için geçerli.",
      src=[("Merck, 19 Ağustos 2026", "https://www.merck.com/news/merck-and-moderna-announce-phase-3-interpath-001-trial-of-intismeran-autogene-plus-keytruda-met-endpoints-of-recurrence-free-survival-rfs-and-distant-metastasis-free-survival-dmfs-in-patient/"), ("STAT", "https://www.statnews.com/2026/08/19/mrna-cancer-vaccine-trial-melanoma-merck-moderna/"), ("The ASCO Post, 21 Ağustos 2026", "https://ascopost.com/news/august-2026/interpath-001-trial-of-mrna-based-individualized-neoantigen-therapy-meets-primary-and-key-secondary-endpoints-in-patients-with-high-risk-resected-melanoma/")]),
 dict(il=IL_HIPOA, g="hareket", cat="Kireçlenme", date="Temmuz 2026",
      title="Kalça kireçlenmesinde egzersizin ortalama etkisi beklenenden küçük: Cochrane güncellemesi",
      text="Sidney ve Melbourne üniversitelerinden araştırmacıların 23 Temmuz 2026'da yayımladığı Cochrane derlemesi, kalça kireçlenmesi olan 1.368 kişiyle yapılmış 18 çalışmayı inceledi; programlar 2 ile 52 hafta sürdü ve güçlendirme, aerobik ve beden-zihin egzersizlerini kapsıyordu. Hiç tedavi almama, olağan bakım ya da yalnızca bilgilendirmeyle karşılaştırıldığında egzersiz ağrıyı 100 puanlık ölçekte ortalama 7,2, işlevi 8,8 puan iyileştirdi; oysa kişinin günlük hayatta fark etmesi için genellikle 12–13 puanlık bir iyileşme gerektiği kabul ediliyor. Sahte tedaviyle karşılaştırıldığında ağrıda etki çok az ya da hiç yoktu; başka bir tedaviye eklenen egzersiz de ağrı ve işlevi belirgin değiştirmedi. Yaşam kalitesinde de anlamlı bir iyileşme görülmedi.",
      point="Bu, egzersizin işe yaramadığı anlamına gelmiyor: Yazarlar egzersizin kalça kireçlenmesinde temel tedavi olarak önerilmeye devam etmesi gerektiğini, ucuz ve zararının az olduğunu vurguluyor. Ancak hastalara beklentilerin gerçekçi anlatılması ve kimin hangi egzersizden yarar gördüğünü gösterecek daha büyük çalışmalar gerektiğini söylüyorlar. Çalışmaların çoğu küçüktü, katılımcılar hangi grupta olduklarını biliyordu ve katılımcıların %63'ü kadın, yaşları 53 ile 74 arasındaydı.",
      src=[("Cochrane Library, 23 Temmuz 2026", "https://doi.org/10.1002/14651858.CD007912.pub3"), ("Cochrane sade dil özeti", "https://www.cochrane.org/evidence/CD007912_exercise-osteoarthritis-hip"), ("Sidney Üniversitesi, 23 Temmuz 2026", "https://www.sydney.edu.au/news-opinion/news/2026/07/23/exercise-benefit-for-hip-arthritis-pain-may-be-more-modest-than-expected.html")],
      rel=("Kalça kireçlenmesi rehberi", "kalca-kireclenmesi.html")),
 dict(il=IL_PARK, g="beyin", cat="Parkinson", date="Temmuz 2026",
      title="Parkinson'da kök hücreden beyin hücresi nakli",
      text="İsveç'teki Lund Üniversitesi ile İngiltere'deki Cambridge Üniversitesi'nin yürüttüğü STEM-PD çalışmasında, kök hücreden üretilen dopamin salgılayan hücreler orta evre Parkinson hastası 8 kişinin beynine nakledildi. Bir yıl sonra değerlendirilen 7 hastanın 6'sı ilaç dozunu belirgin şekilde azalttı; beyin görüntülemesi nakledilen hücrelerin yaşadığına işaret etti.",
      point="Hücrelere bağlı ciddi bir yan etki görülmedi. Küçük ve erken evre bir çalışma olduğu için etkinin kalıcılığını görmek üzere daha uzun takip ve daha büyük çalışmalar gerekiyor; tedavi henüz rutin kullanımda değil.",
      src=[("Nature Medicine, 9 Temmuz 2026", "https://www.nature.com/articles/s41591-026-04525-0"), ("Parkinson's UK", "https://www.parkinsons.org.uk/news/2026/landmark-european-stem-cell-trial-announces-positive-results"), ("Cambridge Kök Hücre Enstitüsü, 10 Temmuz 2026", "https://www.stemcells.cam.ac.uk/news/first-human-clinical-trial-shows-feasibility-new-parkinsons-cell-therapy")]),
 dict(il=IL_SHUTTLE, g="beyin", cat="Alzheimer", date="Temmuz 2026",
      title="Beyne “mekikle” taşınan ilaç: trontinemab",
      text="Roche'un geliştirdiği trontinemab, kan-beyin engelini bir taşıyıcı sayesinde daha kolay geçmek üzere tasarlandı. Temmuz 2026'daki Alzheimer kongresinde (AAIC) açıklanan erken faz verilerine göre yüksek dozu alan hastaların yaklaşık %91–92'sinde 28 haftada beyindeki amiloid birikimi eşik değerin altına indi. Kongrede ayrıca, belirtisi olmayan ama kanda p-tau217 düzeyi yüksek olan 55–80 yaş arası yaklaşık 1.600 kişide ilacın hastalığın başlamasını geciktirip geciktirmediğini sınayacak PrevenTRON çalışmasının tasarımı açıklandı.",
      point="İlaç henüz onaylı değil; büyük faz III çalışmaları sürüyor. Az sayıda hastada beyinde mikro kanama gibi yan etkiler izlendi.",
      src=[("Clinical Trials Arena, 16 Temmuz 2026", "https://www.clinicaltrialsarena.com/news/roche-alzheimers-trontinemab-aaic-26/"), ("Alzheimer Europe, 16 Temmuz 2026", "https://www.alzheimer-europe.org/news/long-term-phase-ib/iia-data-and-prevention-trial-design-trontinemab-presented-aaic"), ("NeurologyLive, 19 Temmuz 2026", "https://www.neurologylive.com/view/roche-unveils-preventron-phase-3-prevention-trial-trontinemab-cognitively-unimpaired-individuals-high-risk-alzheimers")]),
 dict(il=IL_LDL, g="kalp", cat="Kolesterol", date="Temmuz 2026",
      title='Kolesterol için ilk PCSK9 hapı',
      text="PCSK9 ilaçları kötü kolesterolü (LDL) güçlü şekilde düşürüyor, ama bugüne kadar yalnızca iğne olarak kullanılabiliyordu. FDA, 17 Temmuz 2026'da Merck'in enlisitid (Lipfendra) adlı ilacını günde bir kez alınan ilk PCSK9 hapı olarak onayladı. Zaten statin kullanan toplam 3.207 kişilik iki çalışmada LDL kolesterol 24. haftada plaseboya göre, kalp-damar hastalığı olan ya da riski yüksek kişilerde %56, ailesel yüksek kolesterolü olanlarda %59 daha fazla düştü.",
      point='Diyet ve egzersize ek olarak kullanılmak üzere onaylandı. Kalp krizi ve inmeyi azaltıp azaltmadığını gösterecek sonuç çalışması henüz tamamlanmadı.',
      src=[('FDA, 17 Temmuz 2026', 'https://www.fda.gov/news-events/press-announcements/fda-approves-first-oral-pcsk9-inhibitor-lower-ldl-cholesterol-adults-high-cholesterol'), ('NEJM, 4 Şubat 2026', 'https://doi.org/10.1056/NEJMoa2511002'), ('TCTMD, Temmuz 2026', 'https://www.tctmd.com/news/fda-approves-enlicitide-oral-pcsk9-inhibitor-ldl-lowering')]),
 dict(il=IL_PACBACK, g="hareket", cat="Bel ağrısı", date="Haziran 2026",
      title="Yeni başlayan bel ağrısında destekli kendi kendine yönetim, ağrının bir yıl sonraki etkisini biraz azalttı",
      text="ABD'de Minnesota ve Pittsburgh üniversitelerinde yürütülen ve Haziran 2026'da JAMA Internal Medicine'de yayımlanan PACBACK çalışmasına, yeni başlamış ya da birkaç haftadır süren bel ağrısı olan ve bir tarama testine göre ağrısı kronikleşme riski orta ya da yüksek bulunan 1.000 yetişkin katıldı. Katılımcılar 8 hafta boyunca dört yaklaşımdan birine ayrıldı: kılavuzlara dayalı tıbbi bakım (çoğunlukla ağrı kesici ve kas gevşetici ilaçlar), omurga manipülasyonu, klinisyen destekli kendi kendine yönetim (ağrı eğitimi, egzersiz, gevşeme, olumsuz düşünceleri yeniden çerçeveleme ve aktif kalma) ya da son ikisinin birlikte uygulanması. 10–12. aylarda ağrının günlük hayata etkisi (8–50 puanlık bir ölçekte) destekli kendi kendine yönetim grubunda tıbbi bakıma göre ortalama 1,7 puan daha düşüktü; ağrının etkisi en az yarı yarıya azalanlar %64'e karşı %55 oldu. Omurga manipülasyonu tek başına tıbbi bakımdan farklı değildi ve kendi kendine yönetime eklendiğinde ek yarar sağlamadı.",
      point="Araştırmacılar ortalama farkın küçük olduğunu belirtiyor. Kendi kendine yönetimin etkisinin yaklaşık %76'sı, katılımcıların 6. aya kadar hareket etmekten daha az korkması, ağrıyla başa çıkabileceğine daha çok güvenmesi ve ağrıyla ilgili olumsuz düşüncelerinin azalmasıyla açıklandı. Sonuçlar katılımcıların kendi bildirimlerine dayanıyor ve katılımcılar hangi yaklaşımı aldıklarını biliyordu. Bulgu, yeni başlayan bel ağrısında yalnızca ilaca değil, hareket etmeye ve ağrıyı anlamaya dayalı bir yaklaşıma da yer verilmesini destekliyor.",
      src=[("JAMA Internal Medicine, Haziran 2026", "https://doi.org/10.1001/jamainternmed.2026.1893"), ("ReachMD, 9 Haziran 2026", "https://reachmd.com/news/pacback-prevention-chronic-back-pain/2487393/"), ("News-Medical, 1 Temmuz 2026", "https://www.news-medical.net/news/20260701/Personalized-self-management-effectively-prevents-chronic-back-pain.aspx")],
      rel=("Bel ağrısı rehberi", "bel-agrisi.html")),
 dict(il=IL_FAST4, g="hareket", cat="Kas gücü", date="Haziran 2026",
      title="65 yaş üstünde günde 4 dakikalık güç egzersizi bacak gücünü ve dengeyi artırdı",
      text="ABD'de Penn State Tıp Fakültesi'nden araştırmacıların 2026'da PLOS One'da yayımladığı FAST-2 çalışmasında, haftada ortalama yalnızca 18 dakika egzersiz yapan, yaş ortalaması 74 olan 97 kişi rastgele iki gruba ayrıldı. Egzersiz grubu her gün yaklaşık 4 dakika süren bir program yaptı: şınav, sandalyeden kalkma, lastik bantla kürek çekme ve basamak çıkma; her hareket 30 saniye, ardından 30 saniye dinlenme. Katılımcılara lastik bantlar ve yüksekliği ayarlanabilen bir basamak verildi, hareketler güç arttıkça zorlaştırıldı. Egzersiz yapmayan gruba göre 30 saniyede sandalyeden kalkma sayısı 4,2 tekrar, tek ayak üstünde durma süresi 3,6 saniye arttı; oturup kalkma 2,3 saniye hızlandı. Katılımcılar programı günlerin %81'inde yaptı.",
      point="Haberlerde grupların başlangıç ve son değerleri ile güven aralıkları yer almıyor; bazı başlıklardaki “zindeliği dört katına çıkardı” ifadesi de verilen sayılarla desteklenmiyor. Yine de sonuç, kısa ama her gün yapılan güçlendirmenin yaşlılarda işe yarayabileceğini gösteren randomize bir kanıt. Benzer bir devreyi evde yapmak için Kendine iyi bak bölümündeki güç devresini kullanabilirsiniz.",
      src=[("PLOS One, 2026", "https://doi.org/10.1371/journal.pone.0336748"), ("Penn State, 9 Haziran 2026", "https://www.psu.edu/news/research/story/four-minute-daily-workout-improves-strength-balance-older-adults"), ("Penn State Health News, 12 Haziran 2026", "https://pennstatehealthnews.org/2026/06/four-minutes-of-daily-resistance-training-can-quadruple-fitness-in-older-adults/")],
      rel=("Evde güç devresi", "guc-devresi.html")),
 dict(il=IL_CART, g="gen", cat="Bağışıklık", date="Haziran 2026",
      title="Ağır lupusta CAR-T hücre tedavisi",
      text="Kanser tedavisinde kullanılan CAR-T yöntemi, bağışıklık sisteminin kendi dokularına saldırdığı hastalıklarda da deneniyor. University College London'ın (UCL) yürüttüğü CARLYSLE çalışmasında ağır lupus hastalarının bağışıklık hücreleri, hastalıktan sorumlu B hücrelerini hedefleyecek şekilde yeniden programlandı. Düşük doz grubundaki 6 hastanın 5'i standart ölçütlere göre remisyona girdi; böbrek tutulumu olanlarda idrarla protein kaybı azaldı.",
      point="Ağır sitokin salınım sendromu ya da sinir sistemi yan etkisi görülmedi; bir hastada gelişen karaciğer hasarı tamamen düzeldi. Sonuçlar 9 hastalık erken bir çalışmaya ait; İngiltere'de daha geniş bir faz II çalışması hasta almaya başladı.",
      src=[("UCL, 12 Haziran 2026", "https://www.ucl.ac.uk/news/2026/jun/car-t-cell-therapy-shows-early-promise-severe-lupus"), ("ACR Convergence 2025 bildirisi", "https://acrabstracts.org/?p=46111"), ("NIHR UCLH Biyomedikal Araştırma Merkezi, 12 Haziran 2026", "https://www.uclhospitals.brc.nihr.ac.uk/news/i-can-participate-life-now")]),
 dict(il=IL_LACO, g="hareket", cat="Kas-iskelet", date="Haziran 2026",
      title="Bir epilepsi ilacı kıkırdağı korumaya aday",
      text="Yale Tıp Fakültesi'nden araştırmacılar, kireçlenmiş eklemde aşırı çalışan Nav1.7 adlı sodyum kanalının hem ağrı sinyalini artırdığını hem de kıkırdak hücrelerini yıkıma ittiğini gösterdi. Bu kanalı engelleyen ve epilepside zaten kullanılan lakozamid, düşük dozda kıkırdak yapımını destekledi, yıkımı azalttı ve hayvanlarda eklem ağrısını hafifletti. İlaç, vücut ısısında jelleşen bir kolajen jelin içinde dize verildiğinde haftalarca eklemde kaldı; ayda bir yapılan enjeksiyon kıkırdak kaybını, her gün ağızdan verilen ilaçtan daha iyi önledi.",
      point="Sonuçlar hücre ve hayvan deneylerine dayanıyor; kireçlenmesi olan insanlarda henüz denenmedi. Etkili doz aralığı dar: Çok yüksek ya da çok düşük dozda yarar kayboldu. İlacın zaten onaylı olması klinik çalışmaları hızlandırabilir. O güne dek diz kireçlenmesinde tedavinin temeli egzersiz.",
      src=[('Yale School of Medicine, 2 Haziran 2026', 'https://medicine.yale.edu/news-article/hydrogel-relieves-pain-and-repairs-cartilage-in-osteoarthritis/'), ('Bioactive Materials, 2026', 'https://doi.org/10.1016/j.bioactmat.2026.02.045'), ('ScienceAlert, 14 Ekim 2026', 'https://www.sciencealert.com/?p=223859')],
      rel=('Dizin 12 Sırrı: ev programı', 'dizin-12-sirri.html')),
 dict(il=IL_GAE, g="hareket", cat="Kas-iskelet", date="Haziran 2026",
      title="Diz kireçlenmesi ağrısında damar tıkama (GAE)",
      text="Berlin'deki Charité Üniversite Hastanesi'nde, en az 3 aydır diğer tedavilerle geçmeyen kireçlenme ağrısı olan 194 hastaya genikülat arter embolizasyonu uygulandı: ince bir kateterle dizin çevresindeki küçük damarlara, birkaç saat içinde çözünen mikroküreler verildi. Ağrı 10 üzerinden ortanca 7'den 12. ayda 3'e indi; diz yakınmalarını ölçen ölçeğin (KOOS) alanlarına göre hastaların %55–80'i anlamlı kabul edilen iyileşme eşiğini aştı. İşlemlerin %7'sinde, çoğu bir gün içinde geçen ciltte renk değişikliği gibi hafif yan etkiler görüldü.",
      point="Orta ya da ağır yan etki görülmedi. Ancak kontrol grubu olmayan, tek merkezli bir çalışma ve 12. ayda hastaların %79'una ulaşılabildi. Egzersiz, diz kireçlenmesinde tedavinin temeli olmaya devam ediyor.",
      src=[("ScienceDaily (Charité), 16 Haziran 2026", "https://www.sciencedaily.com/releases/2026/06/260616102217.htm"), ("Radiology, 2026", "https://doi.org/10.1148/radiol.253312"), ("AuntMinnie, 16 Haziran 2026", "https://www.auntminnie.com/clinical-news/interventional/article/15827724/gae-effective-for-knee-pain-up-to-12-months")],
      rel=("Diz kireçlenmesi rehberi", "diz-kireclenmesi.html")),
 dict(il=IL_MCED, g="tani", cat="Kanser taraması", date="Haziran 2026",
      title='Tek kan testiyle birçok kanseri erken yakalamak: ilk büyük sonuçlar',
      text="İngiltere'de 50–77 yaş arası, şikâyeti olmayan 142.942 kişinin katıldığı NHS-Galleri çalışmasında katılımcıların yarısına 3 yıl boyunca yılda bir, kanda tümörlerin bıraktığı DNA parçalarını arayan Galleri testi yapıldı. Test grubunda taramayla yakalanan kanser sayısı yaklaşık 4 kat arttı; evre IV (yayılmış) kanser tanıları %14 azaldı ve daha erken evrede yakalanan kanserler arttı.",
      point='Çalışmanın ana hedefi olan evre III–IV kanserlerde anlamlı azalma sağlanamadı. Erken tanının yaşam süresini uzatıp uzatmadığı henüz bilinmiyor. Bu test meme, rahim ağzı ve kolon kanseri taramalarının yerine geçmiyor.',
      src=[('ASCO, Haziran 2026', 'https://www.asco.org/about-asco/press-center/galleri-early-detection-shift-timing-cancer-detection'), ('The ASCO Post', 'https://ascopost.com/news/june-2026/annual-galleri-screening-reduced-stage-iv-cancer-diagnoses-but-missed-primary-endpoint-in-first-randomized-mced-trial/'), ('ecancer, 30 Mayıs 2026', 'https://ecancer.org/en/news/28371-asco-2026-galleri-early-detection-test-may-shift-timing-of-cancer-detection-reducing-stage-iv-diagnoses')]),
 dict(il=IL_RETA, g="hareket", cat="Kas-iskelet", date="Haziran 2026",
      title='Kilo verdiren yeni ilaç diz kireçlenmesi ağrısını da azalttı',
      text="Eli Lilly'nin geliştirdiği retatrutid, iştah ve metabolizmayla ilgili üç hormon reseptörünü (GLP-1, GIP ve glukagon) birlikte uyaran, haftada bir yapılan bir iğne. Obezite ve diz kireçlenmesi olan 445 kişilik TRIUMPH-4 çalışmasında en yüksek dozu alanlar 68 haftada vücut ağırlıklarının ortalama %28,7'sini kaybetti; diz ağrısı iki dozda %74–76 azaldı, plasebo grubunda ise %40,3. Haziran 2026'da açıklanan 2.339 kişilik TRIUMPH-1 çalışmasında da diz kireçlenmesi olan katılımcılarda ağrı %73'e kadar azaldı; ancak TRIUMPH-4'te plasebo grubunda da ağrının %40 azaldığını unutmamak gerekir.",
      point="Retatrutid henüz onaylı değil, yalnızca klinik çalışmalarda kullanılıyor; internette satılan “retatrutid” ürünleri yasa dışı ve güvenilmez. Bulantı, ishal ve kusma sık görüldü; en yüksek dozda hastaların yaklaşık %18'i yan etki nedeniyle ilacı bıraktı. Diz kireçlenmesinde kilo vermeyi güçlendirme egzersizleriyle birleştirmek önemini koruyor.",
      src=[('Eli Lilly, 11 Aralık 2025', 'https://investor.lilly.com/news-releases/news-release-details/lillys-triple-agonist-retatrutide-delivered-weight-loss-average'), ('Eli Lilly, 6 Haziran 2026', 'https://investor.lilly.com/news-releases/news-release-details/lillys-triple-agonist-retatrutide-drove-substantial-improvements'), ('Healio, 20 Ocak 2026', 'https://www.healio.com/news/endocrinology/20260120/retatrutide-confers-up-to-287-weight-loss-reduction-in-knee-osteoarthritis-pain')],
      rel=('Diz kireçlenmesi rehberi', 'diz-kireclenmesi.html')),
 dict(il=IL_CAVD, g="hareket", cat="Kemik sağlığı", date="Mayıs 2026",
      title="Kalsiyum ve D vitamini takviyesi çoğu yaşlıda kırık ve düşmeleri azaltmadı",
      text="Kanadalı araştırmacıların The BMJ'de yayımladığı sistematik derlemede, kalsiyum, D vitamini ya da ikisinin birlikte kullanımını plasebo ya da tedavisizlikle karşılaştıran 69 randomize çalışma ve 153.902 yetişkinin verisi incelendi. Kalsiyum (11 çalışma, 9.067 kişi), D vitamini (36 çalışma, 92.045 kişi) ve ikisinin birlikte kullanımı (15 çalışma, 51.126 kişi) kırıkları, kalça kırığını ve düşmeleri klinik açıdan anlamlı ölçüde azaltmadı. Birlikte kullanımda herhangi bir kırık riski istatistiksel olarak biraz düşük çıktı (göreli risk 0,91), ama mutlak fark yalnızca %1 olduğu için yazarlar bunu klinik açıdan önemli bulmadı. Sonuçlar yaş, cinsiyet, önceki kırık ya da düşme ve beslenmeyle alınan kalsiyum miktarından bağımsız olarak benzerdi; kanıtın kesinliği çoğunlukla orta ile yüksek düzeydeydi.",
      point="Bu sonuçlar herkese rutin takviye önermeyi desteklemiyor. Ancak kemik hastalığı olanlar ve osteoporoz ilacı kullananlar için geçerli olmayabilir; hekiminizin önerdiği takviyeyi kendi başınıza bırakmayın. Araştırmacılar kaynakların, düşmeyi önlediği kanıtlanmış denge ve kuvvet egzersizlerine ve kişiye özel düşme önleme programlarına yönlendirilmesini öneriyor.",
      src=[("BMJ basın bülteni, 20 Mayıs 2026", "https://bmjgroup.com/calcium-and-vitamin-d-supplements-offer-little-to-no-meaningful-benefit-on-fracture-and-fall-prevention/"), ("The BMJ, 2026", "https://doi.org/10.1136/bmj-2025-088050"), ("Hospital Healthcare Europe, 30 Haziran 2026", "https://hospitalhealthcare.com/specialisms/rheumatology/clinical-benefit-of-vitamin-d-and-calcium-supplements-for-fracture-prevention-questioned/")],
      rel=("Düşmeleri önleme rehberi", "dusme-onleme.html")),
 dict(il=IL_BAX, g="kalp", cat="Tansiyon", date="Mayıs 2026",
      title='Zor kontrol edilen tansiyonda yeni ilaç sınıfı',
      text="Birden fazla ilaca rağmen tansiyonu yüksek kalan hastalarda, vücutta tuz ve su tutulmasına yol açan aldosteron hormonu önemli bir etken. AstraZeneca'nın baksdrostat (Baxfendy) adlı ilacı, aldosteronu üreten enzimi (aldosteron sentaz) seçici olarak engelleyen ilk ilaç olarak Mayıs 2026'da FDA onayı aldı. En az iki tansiyon ilacı kullanan 796 hastalık BaxHTN çalışmasında büyük tansiyon 12 haftada plaseboya göre 8,7–9,8 mmHg daha fazla düştü.",
      point="Başlıca dikkat edilmesi gereken yan etki kanda potasyum yükselmesi: potasyumun 6,0 mmol/L'nin üzerine çıkması yüksek dozda %3, plaseboda %0,4 oranında görüldü; bu yüzden potasyum düzeyi kan tahliliyle izlenir. Tansiyon ilacınızı hekiminize danışmadan değiştirmeyin. İlaçların yanında düzenli egzersizin, özellikle izometrik egzersizlerin de tansiyonu düşürdüğü gösterildi.",
      src=[('New England Journal of Medicine, 2025', 'https://www.nejm.org/doi/full/10.1056/NEJMoa2507109'), ('Pharmacy Times, Mayıs 2026', 'https://www.pharmacytimes.com/view/fda-approves-baxdrostat-as-first-in-class-aldosterone-synthase-inhibitor-for-hypertension'), ('Drug Topics, 18 Mayıs 2026', 'https://www.drugtopics.com/view/fda-approves-baxdrostat-as-first-aldosterone-synthase-inhibitor-for-hypertension')],
      rel=('Tansiyon için duvar oturuşu', 'duvar-oturusu.html')),
 dict(il=IL_UPF, g="hareket", cat="Beslenme", date="Nisan 2026",
      title="Ultra işlenmiş gıdalar uyluk kaslarındaki yağlanmayla ilişkili",
      text="ABD'deki Osteoarthritis Initiative çalışmasından, dizinde henüz kireçlenme olmayan ama risk taşıyan 615 kişinin uyluk MR'ları incelendi (ortalama yaş 60). Katılımcıların yediklerinin ortalama %41'i ultra işlenmiş gıdalardan oluşuyordu. Ultra işlenmiş gıda tüketimi arttıkça kas dokusunun içindeki yağlanma da arttı; bu ilişki toplam kalori ve yağ alımı, fiziksel aktivite ve sosyoekonomik etkenlerden bağımsızdı.",
      point="Bu bir gözlem çalışması: Ultra işlenmiş gıdanın kas yağlanmasına neden olduğunu kanıtlamıyor; beslenme bilgisi bir yıllık ankete dayanıyor. Kas içi yağlanma, dizi destekleyen kasları zayıflatarak kireçlenme riskini artırabilir. Kilo verirken yalnızca kaloriye değil, besin kalitesine de dikkat etmek akıllıca.",
      src=[('RSNA, 14 Nisan 2026', 'https://www.rsna.org/news/2026/april/thigh-muscle-fat-and-osteoarthritis'), ('Radiology, 2026', 'https://doi.org/10.1148/radiol.251129'), ('Radiology Business', 'https://radiologybusiness.com/topics/medical-imaging/magnetic-resonance-imaging-mri/ultraprocessed-foods-may-degrade-muscle-health-new-mri-findings-suggest')],
      rel=('Diz kireçlenmesi rehberi', 'diz-kireclenmesi.html')),
 dict(il=IL_ORFO, g="kalp", cat="Obezite", date="Nisan 2026",
      title='Yemek ve su kısıtlaması olmayan ilk GLP-1 zayıflama hapı',
      text="GLP-1 ilaçları şimdiye kadar çoğunlukla haftalık iğne olarak kullanılıyordu; Aralık 2025'te onaylanan ağızdan semaglutidin (Wegovy hap) ise aç karnına alınması gerekiyor. FDA, 1 Nisan 2026'da Eli Lilly'nin orforglipron (Foundayo) adlı hapını, günün herhangi bir saatinde yemek ve su kısıtlaması olmadan alınabilen ilk GLP-1 hapı olarak onayladı. 72 haftalık ATTAIN-1 çalışmasında en yüksek dozu alanlar vücut ağırlıklarının ortalama %12,4'ünü kaybetti; plaseboda kayıp %0,9'du.",
      point='Azaltılmış kalorili beslenme ve daha fazla hareketle birlikte kullanılmak üzere onaylandı. Bulantı, kabızlık ve ishal sık; tiroid tümörü riski, pankreatit ve safra kesesi sorunlarıyla ilgili uyarılar bu ilaç için de geçerli. Kilo verirken kas kaybını azaltmak için güçlendirme egzersizleri önemli.',
      src=[('Eli Lilly, 1 Nisan 2026', 'https://investor.lilly.com/news-releases/news-release-details/fda-approves-lillys-foundayotm-orforglipron-only-glp-1-pill'), ('Healio, 1 Nisan 2026', 'https://www.healio.com/news/endocrinology/20260401/fda-approves-orforglipron-an-oral-glp1-for-adults-with-obesity'), ('Patient Care, 1 Nisan 2026', 'https://www.patientcareonline.com/view/fda-approves-orforglipron-first-oral-glp-1-receptor-agonist-for-weight-loss-with-no-food-or-water-restrictions')],
      rel=('Ne kadar hareket yeterli?', 'hareket.html')),
 dict(il=IL_FORK, g="hareket", cat="Kas-iskelet", feat=True, date="Nisan 2026",
      title="Kronik bel ağrısında hangi tedaviyle başlamalı?",
      text="ABD'de 749 kronik bel ağrısı hastasıyla yapılan OPTIMIZE çalışmasında katılımcılar önce 8 hafta fizyoterapi ya da bilişsel davranışçı terapi aldı; yeterli fayda görmeyenler tedavi değiştirdi ya da farkındalık (mindfulness) programına geçti. 10. haftada fizyoterapiyle başlayanların günlük işlevi biraz daha iyiydi; ağrı düzeyi ise gruplar arasında benzerdi.",
      point="Kazanım mütevazı olsa da fizyoterapi makul bir ilk adım olarak öne çıktı. Bir yılın sonunda ikinci aşamadaki seçenekler arasında anlamlı fark çıkmadı; sonradan tedavi değiştirmek ya da eklemek uzun vadeli sonucu pek değiştirmedi.",
      src=[("Annals of Internal Medicine, 20 Nisan 2026", "https://doi.org/10.7326/annals-25-04645"), ("HealthDay", "https://www.healthday.com/healthpro-news/bone-and-joint/physical-therapy-may-be-beneficial-for-chronic-low-back-pain"), ("Medical Republic, 14 Mayıs 2026", "https://www.medicalrepublic.com.au/?p=125752")],
      rel=("Bel ağrısı rehberi", "bel-agrisi.html")),
 dict(il=IL_EAR, g="gen", cat="Genetik", date="Nisan 2026",
      title="Doğuştan işitme kaybında gen tedavisi kalıcı görünüyor",
      text="OTOF genindeki bir bozukluk nedeniyle işitme kaybı olan 9 aylık ile 32 yaş arasındaki 42 kişinin iç kulağına, sağlam bir gen kopyası taşıyan zararsız hale getirilmiş bir virüs verildi. Çin'deki sekiz merkezde yapılan çalışmada 2,5 yıllık izlemde katılımcıların %90'ının işitmesi düzeldi, yarısından fazlası normal işitme düzeyine ulaştı. Çocuklar seslere tepki vermekten kısa cümleler kurmaya, hatta şarkı söylemeye kadar ilerledi.",
      point="Ciddi yan etki görülmedi. Etki en çok 18 yaş ve altındakilerde belirgindi; katılımcıların %10'unda yanıt olmadı. Tedavi yalnızca OTOF kaynaklı işitme kaybı içindir ve onay süreci yeni başlıyor.",
      src=[("Harvard Gazette, Nisan 2026", "https://news.harvard.edu/gazette/story/2026/04/hearing-breakthrough-holds-up/"), ("Nature, 22 Nisan 2026", "https://doi.org/10.1038/s41586-026-10393-y"), ("Live Science, 22 Nisan 2026", "https://livescience.com/health/genetics/gene-therapy-improves-hearing-in-90-percent-of-patients-with-inherited-deafness-in-largest-trial-of-its-kind")]),
 dict(il=IL_ESPRESSO, g="beyin", cat="İnme", date="Mart 2026",
      title="İnmeden hemen sonra üç kat fazla kol terapisi, üç ayda ek yarar sağlamadı",
      text="Yeni Zelanda'da Auckland Üniversitesi'nden araştırmacıların Mart 2026'da Brain Communications'ta yayımladığı ESPRESSO çalışmasına, inmeden sonraki ilk iki hafta içindeki 64 hasta katıldı; katılımcılar kol ve elin toparlanma potansiyelini gösteren bir biyobelirteçle seçildi. Hastalar olağan bakımlarına ek olarak 3 hafta boyunca, hafta içi her gün 90 dakika daha terapi aldı: yarısı ekranda bir yunus gibi deniz canlısını kol hareketleriyle yönlendirdiği oyun tabanlı bir terapi, diğer yarısı aynı sürede klasik terapi. İki grup da terapi süresince belirgin iyileşti; 3. ayda kol ve el işlevini ölçen testte (ARAT) aralarında fark yoktu. Yaklaşık üç kat daha fazla terapi almalarına karşın, aynı merkezde daha önce yalnızca olağan bakım almış hastalardan da daha iyi değillerdi.",
      point="Araştırmacılara göre inmeden sonraki ilk haftalarda kol ve eldeki toparlanma büyük ölçüde beynin kendiliğinden onarım süreçlerine bağlı; bu dönemde terapinin miktarını artırmak sonucu belirgin değiştirmeyebilir. Çalışma küçük, tek merkezli ve keşif amaçlı (faz IIa); olağan bakım grubu aynı dönemde değil, daha önce izlenmiş hastalardan oluşuyordu. Bulgu erken dönemde terapinin gereksiz olduğu anlamına gelmiyor; hangi hastada, hangi zamanlamada ve ne kadar terapinin fark yarattığı daha büyük çalışmalarla netleşecek.",
      src=[("Brain Communications, Mart 2026", "https://academic.oup.com/braincomms/article/8/2/fcag057/8553076"), ("Neuroscience News (Auckland Üniversitesi), 26 Mart 2026", "https://neurosciencenews.com/stroke-rehab-early-intensity-recovery-30396"), ("Auckland Üniversitesi, 22 Nisan 2026", "https://www.auckland.ac.nz/en/news/2026/04/22/-more-therapy--earlier--didn-t-boost--stroke-recovery-.html")],
      rel=("İnme rehabilitasyonu", "inme-rehabilitasyonu.html")),
 dict(il=IL_RRAD, g="beyin", cat="Demans", date="Mart 2026",
      title="Egzersiz ve sıkı tansiyon-kolesterol tedavisi iki yılda düşünme becerilerini iyileştirmedi",
      text="ABD'de dört merkezde yürütülen ve 23 Mart 2026'da JAMA Neurology'de yayımlanan rrAD çalışmasına, demansı olmayan ama yüksek tansiyonu, ailesinde demans öyküsü ya da kendi fark ettiği hafıza yakınmaları olan 60–85 yaş arası 513 kişi katıldı. Katılımcılar dört gruba ayrıldı: haftada yaklaşık 160 dakika orta-yüksek tempolu aerobik egzersiz, büyük tansiyonu 130'un altına indirmeyi ve LDL kolesterolü düşürmeyi hedefleyen yoğun ilaç tedavisi, ikisi birlikte ya da olağan bakım. İki yıl sonunda düşünme ve hafıza testlerinden oluşan bileşik puan tüm gruplarda hafifçe arttı, ama gruplar arasında anlamlı fark yoktu. İlaç tedavisi tansiyonu ve LDL kolesterolü belirgin düşürdü.",
      point="Araştırmacıların ifadesiyle “bedeni iyileştirdik ama beyni değil”. İki yıl, bilişsel gerilemeyi önlemedeki etkiyi görmek için kısa olabilir; katılımcılar başlangıçta bilişsel olarak sağlıklıydı ve tüm gruplarda puanlar arttığı için fark görmek zorlaştı. Sonuç, egzersizin ve tansiyon kontrolünün değersiz olduğu anlamına gelmiyor: ikisi de kalp-damar sağlığı için önemli. Araştırmacılar demansı önlemek için birden fazla risk etkenini birlikte hedefleyen, daha uzun süreli yaklaşımların gerektiğini vurguluyor.",
      src=[("JAMA Neurology, Mart 2026", "https://jamanetwork.com/journals/jamaneurology/article-abstract/2846826"), ("Pennington Biyomedikal Araştırma Merkezi, 23 Mart 2026", "https://www.pbrc.edu/news/media/2026/jamaneurology.aspx"), ("EMJ", "https://www.emjreviews.com/?p=147867")],
      rel=("Demansta egzersiz", "demans-egzersiz.html")),
 dict(il=IL_BCI, g="beyin", cat="Nöroteknoloji", date="Mart 2026",
      title="Beyin-bilgisayar arayüzüyle evde hızlı yazı",
      text="ABD'deki BrainGate çalışmasında, biri ileri evre ALS, diğeri boyun hizasında omurilik yaralanması olan iki katılımcının beynin hareket bölgesine küçük elektrotlar yerleştirildi. Sistem, parmakları hareket ettirme girişimini klavyedeki harflere çevirdi. Katılımcılardan biri kendi evinde dakikada 22 kelime yazdı ve kelime hatası oranı %1,6'da kaldı; kurulum için yaklaşık 30 cümlelik bir ayar yeterli oldu.",
      point="Konuşamayan ve elini kullanamayan kişiler için iletişimde büyük bir adım. Cihaz henüz yalnızca araştırma amaçlı kullanılıyor ve beyin ameliyatı gerektiriyor.",
      src=[("Brown Üniversitesi, 16 Mart 2026", "https://www.brown.edu/news/2026-03-16/braingate-rapid-communication"), ("Nature Neuroscience, 16 Mart 2026", "https://doi.org/10.1038/s41593-026-02218-y"), ("Nature Asia basın bülteni, 17 Mart 2026", "https://www.natureasia.com/en/info/press-releases/detail/9273")]),
 dict(il=IL_SPINE, g="beyin", cat="Rehabilitasyon", date="2026",
      title="Omurilik yaralanmasında elektrik uyarımı: umut ve gerçek",
      text="ABD'deki Brown Üniversitesi'nin küçük bir çalışmasında tam omurilik yaralanması olan 3 kişiye yaralanmanın altına ve üstüne elektrot yerleştirildi. Alttaki uyarım bacak kaslarını çalıştırırken üstteki uyarım göğüs, kol ya da sırtta hissedilen sinyallerle diz açısı ve adım hakkında geri bildirim verdi; katılımcılar askı ve terapist desteğiyle koşu bandında yürüdü. 48 kişilik uluslararası eWALK çalışmasında ise deri üzerinden verilen uyarım, 12 haftalık yürüme eğitimine ek fayda sağlamadı.",
      point="eWALK'un asıl mesajı: yürüme eğitimi tek başına, uzun süredir omurilik yaralanması olan kişilerde bile yürümeyi belirgin şekilde iyileştirdi. Uyarım teknolojileri umut vadediyor ama henüz rehabilitasyonun yerini tutmuyor.",
      src=[("Brown Üniversitesi, 11 Mart 2026", "https://www.brown.edu/news/2026-03-11/spinal-cord-stimulation"), ("eClinicalMedicine, 2026", "https://www.thelancet.com/journals/eclinm/article/PIIS2589-5370(26)00049-0/fulltext"), ("SpinalCure Australia (eWALK)", "https://spinalcure.org.au/research/spinalcure-reflects-on-the-ewalk-trial-outcomes/")]),
 dict(il=IL_OAEX, g="hareket", cat="Kireçlenme", date="Şubat 2026",
      title="Kireçlenmede egzersizin ağrıya etkisi küçük ve kısa süreli olabilir: büyük bir derleme tartışma başlattı",
      text="Şubat 2026'da RMD Open'da yayımlanan bir şemsiye derlemede, kireçlenmede egzersiz tedavisini inceleyen 5 sistematik derleme (8.631 katılımcı) ve 28 randomize çalışma (4.360 katılımcı) bir araya getirildi; çalışmaların 23'ü diz ya da kalça, 3'ü el, 2'si ayak bileği kireçlenmesiyle ilgiliydi. Sahte tedaviye ya da tedavisizliğe göre egzersiz dizde ağrıyı az ve kısa süreli azalttı; kanıtın güvenilirliği çok düşüktü ve büyük, uzun çalışmalarda etki daha da küçüktü. Kalçada etki ihmal edilebilir düzeydeydi (orta güvenilirlik), elde küçüktü. Egzersiz; hasta eğitimi, manuel terapi, ağrı kesiciler, eklem içi kortizon ya da hyaluronik asit iğneleri ve artroskopik diz cerrahisiyle benzer sonuç verdi. Tek tek çalışmalarda, seçilmiş hastalarda uzun vadede diz osteotomisi ve protezden daha az etkiliydi.",
      point="Yazarlar sonuçlarının egzersizin genel sağlığa yararlarını ya da hastaların egzersizi tercih etmesini geçersiz kılmadığını, ancak egzersizin her hastada tek başına ilk basamak tedavi olarak öne çıkarılmasını sorguladığını belirtiyor ve ortak karar vermeyi öneriyor. Derleme bazı sistematik derlemeleri önceliklendirdi; doğrudan karşılaştırmalar azdı, hastaların belirti şiddeti çok farklıydı ve bazı çalışmalarda egzersizle birlikte başka tedaviler de uygulandı. 2025 sonunda The BMJ'de yayımlanan ve 217 çalışmayı kapsayan bir ağ meta-analizi ise diz kireçlenmesinde özellikle aerobik egzersizin ağrıyı ve işlevi orta güvenilirlikle iyileştirdiğini bildirmişti. Egzersiz ucuz ve güvenli; ama beklentiyi gerçekçi tutmak ve programı kişiye göre seçmek önemli.",
      src=[("RMD Open, Şubat 2026", "https://doi.org/10.1136/rmdopen-2025-006275"), ("BMJ Group, 17 Şubat 2026", "https://bmjgroup.com/effectiveness-of-exercise-to-ease-osteoarthritis-symptoms-likely-minimal-and-transient/"), ("Medical Republic, 19 Şubat 2026", "https://www.medicalrepublic.com.au/?p=123345"), ("ScienceDaily, 25 Şubat 2026", "https://www.sciencedaily.com/releases/2026/02/260225081208.htm"), ("The BMJ, 2025 (diz kireçlenmesinde egzersiz türleri)", "https://doi.org/10.1136/bmj-2025-085242")],
      rel=("Diz kireçlenmesi rehberi", "diz-kireclenmesi.html")),
 dict(il=IL_SMALL, g="hareket", cat="Hareket", date="Ocak 2026",
      title="Günde 5 dakika daha fazla hareket: küçük değişikliklerin büyük etkisi",
      text="Norveç, İsveç, ABD ve İngiltere'den 135 binden fazla yetişkinin hareketinin cihazlarla ölçüldüğü kohortları birleştiren ve 14 Ocak 2026'da The Lancet'te yayımlanan analizde, ortalama 8 yıllık izlem verileriyle küçük davranış değişikliklerinin kaç ölümü önleyebileceği hesaplandı. En hareketli %20 dışındaki herkes günde 5 dakika daha orta tempolu hareket etse (örneğin tempolu yürüyüş), ölümlerin yaklaşık %10'u önlenebilirdi; günde 10 dakika ek hareketle bu oran %15'e çıkıyordu. En hareketsiz %20'lik grupta 5 dakikalık artış ölümlerin yaklaşık %6'sını önleyebilirdi. Günde 30 dakika daha az oturmak ise ölümlerin yaklaşık %7'sini (en çok oturanlarda %3'ünü) önleyebilirdi.",
      point="Bunlar gözlem verilerine dayanan model tahminleridir; hareketin ölüm riskini doğrudan azalttığını kanıtlamaz. Hareket yalnızca başlangıçta bir kez ölçüldü, hareket kısıtlılığı gibi ölçülmeyen etkenler sonucu etkilemiş olabilir ve veriler yalnızca yüksek gelirli ülkelerden geliyor. Uzmanlar sonuçların kişisel bir egzersiz reçetesi olarak değil, toplum düzeyinde olası bir etki olarak okunması gerektiğini vurguluyor. Yine de mesaj net: Maraton koşmak gerekmiyor, her gün birkaç dakika daha tempolu yürümek bile fark yaratabilir.",
      src=[("The Lancet, 14 Ocak 2026", "https://doi.org/10.1016/S0140-6736(25)02219-6"), ("EurekAlert! (The Lancet), 13 Ocak 2026", "https://www.eurekalert.org/news-releases/1112291"), ("Karolinska Enstitüsü, 14 Ocak 2026", "https://news.ki.se/five-extra-minutes-of-movement-a-day-can-save-lives-study-in-the-lancet-finds"), ("Science Media Centre İspanya, uzman görüşleri", "https://sciencemediacentre.es/en/small-and-feasible-changes-physical-activity-are-associated-lower-mortality-risk")],
      rel=("Adım hedefi planlayıcısı", "adim-hedefi.html")),
 dict(il=IL_DEPEX, g="beyin", cat="Depresyon", date="Ocak 2026",
      title="Cochrane: Egzersiz depresyon belirtilerini azaltıyor, etkisi psikoterapiye yakın olabilir",
      text="Ocak 2026'da güncellenen Cochrane derlemesinde, depresyonu olan 4.985 kişiyle yapılmış 73 randomize çalışma incelendi. Hiç tedavi almama ya da kontrol koşullarıyla karşılaştırıldığında egzersiz depresyon belirtilerini orta düzeyde azalttı (standart ortalama fark −0,67; düşük güvenilirlik); yalnızca yöntemi en sağlam 7 çalışmaya bakıldığında etki küçüldü (−0,46) ama sürdü. Psikoterapiyle karşılaştırıldığında egzersiz benzer sonuç verdi (10 çalışma, 414 kişi; orta güvenilirlik); ilaç tedavisiyle karşılaştırıldığında da belirgin fark yoktu (5 çalışma, 330 kişi; düşük güvenilirlik). Orta yoğunlukta, toplam 13–36 seanslık programlar ve karma ya da direnç egzersizleri, yalnızca aerobik egzersize göre biraz daha yararlı görünüyordu.",
      point="Çalışmaların çoğu küçüktü ve yanlılık riski yüksekti; uzun vadeli veriler az. Bağımsız uzmanlar, egzersizin psikoterapi ve ilaçla benzer olduğu sonucunun az sayıda çalışmaya dayandığını, denetimli programların motivasyonu yüksek gönüllüleri çektiğini ve egzersizin en iyi var olan tedavilere ek olarak düşünülebileceğini vurguluyor. Egzersizin yan etkisi azdır; ama tedavinizi değiştirmeden ya da ilacınızı bırakmadan önce mutlaka hekiminizle konuşun.",
      src=[("Cochrane Library, Ocak 2026", "https://doi.org/10.1002/14651858.CD004366.pub7"), ("ScienceDaily, 8 Ocak 2026", "https://www.sciencedaily.com/releases/2026/01/260107225516.htm"), ("Science Media Centre uzman görüşleri, 8 Ocak 2026", "https://www.sciencemediacentre.org/expert-reaction-to-exercise-having-similar-results-as-therapy-for-treating-depression/"), ("HCPLive", "https://www.hcplive.com/view/exercise-may-be-effective-therapy-for-alleviating-depression-symptoms"), ("Medicine Today, Şubat 2026", "https://medicinetoday.com.au/mt/2026/february/in-brief/exercise-depression-similar-effects-other-active-treatments-finds-review")],
      rel=("Ruh sağlığı için egzersiz", "ruh-sagligi-egzersiz.html")),
 dict(il=IL_MAMMO, g="tani", cat="Yapay zekâ", date="Ocak 2026",
      title="Mamografide yapay zekâ desteği: ilk randomize çalışmanın sonuçları",
      text="İsveç'te 105 binden fazla kadının katıldığı MASAI çalışmasında mamografiler ya yapay zekâ desteğiyle ya da standart şekilde iki radyolog tarafından okundu. Yapay zekâ destekli grupta kanserlerin %81'i taramada yakalandı (standart grupta %74); iki tarama arasında ortaya çıkan kanserler %12, agresif alt tipteki kanserler %27 daha azdı. Yanlış alarm oranı iki grupta benzerdi.",
      point="Yapay zekâ radyoloğun yerini almıyor, ona destek oluyor; ara sonuçlarda radyologların okuma yükü %44 azalmıştı. Çalışma tek bir ülkede, tek bir cihaz ve tek bir yazılımla, deneyimli radyologlarla yapıldı.",
      src=[("The Lancet, 29 Ocak 2026", "https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)02464-X/abstract"), ("EurekAlert!", "https://www.eurekalert.org/news-releases/1114399"), ("Lund Üniversitesi, 30 Ocak 2026", "https://www.lunduniversity.lu.se/article/ai-support-breast-cancer-screening-fewer-missed-cancer-cases")]),
 dict(il=IL_PREHAB, g="hareket", cat="Ameliyat", date="Aralık 2025",
      title="Kırılgan yaşlılarda ameliyat öncesi ev egzersizi: genel sonuç olumsuz, programı tamamlayanlarda umut verici",
      text="Kanada'da 13 merkezde yürütülen ve 3 Aralık 2025'te JAMA Surgery'de yayımlanan PREPARE çalışmasına, planlı büyük bir ameliyat bekleyen ve kırılganlık ölçeğinde 4 ya da üzeri puanı olan 60 yaş ve üstü 847 kişi katıldı (yaş ortalaması 71,7; yaklaşık dörtte üçü kanser ameliyatı). Yarısı ameliyata kadar evde haftada üç kez birer saatlik kuvvet, aerobik ve esneklik egzersizi, kişiye özel beslenme önerisi ve en az haftada bir koç görüşmesinden oluşan bir hazırlık programı aldı; diğer yarısına yalnızca fiziksel aktivite ve sağlıklı beslenme önerilerini içeren basılı kılavuzlar verildi. Program ortanca 4 hafta sürdü. Ameliyattan 30 gün sonra engellilik puanı (WHODAS 2.0) iki grupta benzerdi; hastanedeki komplikasyon oranları da farklı değildi (%50,1'e karşı %47,7).",
      point="Keşif amaçlı bir ek analizde egzersizlerin %75'inden fazlasını tamamlayanlarda ameliyat sonrası engellilik daha düşüktü; bazı haber başlıkları programın engelliliği azalttığını bu analize dayanarak yazdı. Ancak bu tür bir analiz randomizasyonun koruyuculuğunu taşımaz: Programa iyi uyan kişiler zaten başka yönlerden farklı olabilir. Katılımcılar egzersizlerin ortanca %78'ini tamamladı; en önemli engeller başka öncelikler ve motivasyondu. Program grubunda kişilerin kendi sağlık algısı (EQ-VAS) biraz daha iyiydi. Araştırmacılar ameliyattan önce yeterli süre ve destek sağlanırsa hazırlık programlarının daha etkili olabileceğini düşünüyor ve çevrim içi bir programı yeni bir çalışmada (STRIVE) deniyor.",
      src=[("JAMA Surgery, 2026;161(2):113–123", "https://jamanetwork.com/journals/jamasurgery/fullarticle/2841757"), ("Ottawa Hastanesi Araştırma Enstitüsü, 3 Aralık 2025", "https://ohri.ca/en/newsroom/prehab-can-improve-recovery-after-surgery-barriers-remain"), ("HealthDay, 11 Aralık 2025", "https://www.healthday.com/healthpro-news/senior-health/prehabilitation-cuts-postsurgical-disability-in-older-adults-with-frailty")],
      rel=("Sarkopeni rehberi", "sarkopeni.html")),
 dict(il=IL_GAIT, g="hareket", cat="Kas-iskelet", date="Ekim 2025",
      title="Diz kireçlenmesinde yürüyüş şeklini değiştirmek",
      text="ABD'de Utah, New York ve Stanford üniversitelerinden araştırmacıların yürüttüğü, dizin iç kısmında kireçlenmesi olan 68 kişilik bir çalışmada her katılımcı için ayak ucunu 5 ya da 10 derece içe veya dışa çevirmekten hangisinin daha yararlı olacağı hareket analiziyle belirlendi ve 6 seanslık yürüyüş eğitimi verildi. Bir yılda ağrı 10 üzerinden ortalama 2,5 puan azaldı (sahte eğitim grubunda 1,3). MR'da kıkırdak yıkımının daha yavaş ilerlediğine işaret eden bulgular görüldü.",
      point="Bu, “ayak ucunuzu içe çevirin” gibi herkese uyan bir öneri değil; kişiye özel ölçüm ve uzman eşliği gerekiyor. Yöntemin yaygınlaşması için ölçümün basitleştirilmesi gerekiyor.",
      src=[("The Lancet Rheumatology, Ekim 2025", "https://www.thelancet.com/journals/lanrhe/article/PIIS2665-9913(25)00151-1/abstract"), ("Utah Üniversitesi, Ağustos 2025", "https://attheu.utah.edu/health-medicine/a-potential-way-to-relieve-arthritic-knees-without-drugs-or-surgery/"), ("News-Medical, 13 Ağustos 2025", "https://www.news-medical.net/news/20250813/New-research-explores-foot-positioning-to-treat-knee-osteoarthritis.aspx")],
      rel=("Diz kireçlenmesi rehberi", "diz-kireclenmesi.html")),
 dict(il=IL_RUN, g="hareket", cat="Egzersiz", date="Haziran 2025",
      title="Kolon kanseri sonrası egzersiz hayat kurtarıyor",
      text="6 ülkede, kemoterapisini tamamlamış 889 kolon kanseri hastasıyla yapılan CHALLENGE çalışmasında bir grup 3 yıllık, antrenör desteğiyle kişiye özel bir egzersiz programına katıldı (tempolu yürüyüşten grup derslerine kadar); diğer grup yalnızca sağlık eğitimi aldı. 5 yılda egzersiz grubunun %80'i, diğer grubun %74'ü kanserden arınmış kaldı; 8 yılda hayatta kalma %90'a karşı %83'tü.",
      point="Egzersiz grubunda kanserin geri dönme, yeni kanser ya da ölüm riski %28, ölüm riski %37 daha düşüktü. Egzersizin kanser tedavisinin bir parçası olabileceğini gösteren ilk büyük randomize çalışma.",
      src=[("New England Journal of Medicine, Haziran 2025", "https://www.nejm.org/doi/abs/10.1056/NEJMoa2502760"), ("Oncology Central", "https://www.oncology-central.com/world-first-trial-highlights-survival-benefits-of-exercise-for-colon-cancer/"), ("ecancer (ASCO 2025), 1 Haziran 2025", "https://ecancer.org/en/news/26554-asco-2025-exercise-programme-may-lower-risk-of-recurrence-and-death-for-some-colon-cancer-survivors")],
      rel=("Ne kadar hareket yeterli?", "hareket.html")),
 dict(il=IL_ISLET, g="gen", cat="Diyabet", date="Haziran 2025",
      title="Tip 1 diyabette kök hücreden üretilen insülin hücreleri",
      text="Vertex'in geliştirdiği zimislecel, kök hücreden laboratuvarda üretilen ve insülin salgılayan adacık hücrelerinden oluşuyor. Tam doz alan 12 hastanın 10'u bir yılın sonunda insülin iğnesine ihtiyaç duymadı; 12 hastanın tamamında HbA1c %7'nin altına indi ve ağır şeker düşmesi yaşanmadı.",
      point="Hücrelerin reddedilmemesi için bağışıklık baskılayıcı ilaç kullanmak gerekiyor. Çalışmada iki hasta hayatını kaybetti; biri bu ilaçlara bağlı bir enfeksiyon nedeniyle. Faz III çalışmaları sürüyor.",
      src=[("New England Journal of Medicine, Haziran 2025", "https://www.nejm.org/doi/abs/10.1056/NEJMoa2506549"), ("HCPLive", "https://www.hcplive.com/view/zimislecel-enables-insulin-independence-in-10-participants-with-type-1-diabetes"), ("MedCity News, 23 Haziran 2025", "https://medcitynews.com/2025/06/vertex-pharmaceuticals-type-1-diabetes-cell-therapy-zimislecel-insulin-vrtx/")]),
 dict(il=IL_DNA, g="gen", cat="Genetik", date="2025–2026",
      title="Tek bir bebek için tasarlanan gen tedavisi",
      text="ABD'de KJ adlı bir bebekte, vücutta amonyak birikmesine yol açan nadir bir genetik hastalık (CPS1 eksikliği) vardı. Araştırmacılar bebeğin kendi mutasyonunu düzelten kişiye özel bir gen düzenleme tedavisini yaklaşık altı ayda geliştirip uyguladı.",
      point="Çok nadir hastalıklar için “her hastaya özel” tedavi üretmenin mümkün olduğunu gösteren ilk örneklerden biri.",
      src=[("Innovative Genomics Institute, 2026", "https://innovativegenomics.org/news/crispr-clinical-trials-2026/"), ("NBC News, 15 Mayıs 2025", "https://www.nbcnews.com/health/health-news/pennsylvania-baby-first-receive-personalized-gene-therapy-rcna207100"), ("Penn Medicine, 15 Mayıs 2025", "https://pennmedicine.org/news/worlds-first-patient-treated-with-personalized-crispr-therapy")]),
 dict(il=IL_CRISPR, g="gen", cat="Genetik", feat=True, date="2026",
      title="CRISPR tedavileri klinikte",
      text="Onaylı ilk CRISPR tedavisi Casgevy, orak hücreli anemi ve beta talasemide kullanılıyor. Avrupa İlaç Ajansı'nın değerlendirdiği çalışmalarda orak hücre hastalarının 29'unun 28'i en az bir yıl ağrı krizi yaşamadı, talasemi hastalarının 42'sinin 39'u en az bir yıl kan nakline ihtiyaç duymadı. Vücut içinde doğrudan yapılan gen düzenlemesinde de umut verici sonuçlar var.",
      point="Talasemi ve orak hücreli anemi Türkiye'de özellikle Akdeniz bölgesinde sık görülüyor. Tedavi pahalı ve her merkezde uygulanamıyor.",
      src=[("Innovative Genomics Institute, 2026", "https://innovativegenomics.org/news/crispr-clinical-trials-2026/"), ("FDA, 8 Aralık 2023", "https://www.fda.gov/news-events/press-announcements/fda-approves-first-gene-therapies-treat-patients-sickle-cell-disease"), ("Avrupa İlaç Ajansı (EMA), 15 Aralık 2023", "https://www.ema.europa.eu/en/news/first-gene-editing-therapy-treat-beta-thalassemia-and-severe-sickle-cell-disease")]),
]

NEWS_CSS = """
  .grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}
  @media (max-width:760px){.grid{grid-template-columns:1fr}}
  .card{display:grid;grid-template-rows:auto 1fr;border:1px solid var(--line);border-radius:14px;overflow:hidden;background:var(--ground-2)}
  .card.feat{grid-column:1 / -1;grid-template-rows:none;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr)}
  @media (max-width:760px){.card.feat{grid-template-columns:1fr;grid-template-rows:auto 1fr}}
  .card .il{background:#223020;border-bottom:1px solid var(--line)}
  .card.feat .il{border-bottom:0;border-right:1px solid var(--line)}
  @media (max-width:760px){.card.feat .il{border-right:0;border-bottom:1px solid var(--line)}}
  .card .il svg{display:block;width:100%;height:auto}
  .card.feat .il svg{height:100%;object-fit:cover}
  .card .body{padding:18px 18px 16px;display:grid;gap:10px;align-content:start}
  .tags{display:flex;gap:10px;align-items:center;font-size:13px;color:var(--muted)}
  .chip{font-size:11px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;color:var(--ground);background:var(--foil);border-radius:999px;padding:3px 9px}
  .chip.g{background:var(--sage)}
  .card h2{font-size:clamp(22px,3vw,28px);margin:0}
  .card.feat h2{font-size:clamp(26px,3.6vw,34px)}
  .card p{margin:0;color:var(--ink-soft);font-size:16px}
  .card .point{font-size:15px;color:var(--ink);border-left:2px solid var(--foil);padding-left:12px}
  .card .src{font-size:13px;color:var(--muted)}
  .card .src a{color:var(--ink-soft)}
  .chip.o{background:transparent;color:var(--foil);box-shadow:inset 0 0 0 1px var(--line-strong)}
  .card .rel{margin:0;font-size:15px}
  .card .rel a{color:var(--foil);text-decoration:none;font-weight:600}
  .card .rel a:hover{text-decoration:underline}
  .filt{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 20px}
  .filt button{all:unset;cursor:pointer;padding:8px 14px;border-radius:999px;border:1px solid var(--line-strong);font-size:14px;color:var(--ink-soft)}
  .filt button:hover{border-color:var(--foil);color:var(--ink)}
  .filt button[aria-pressed="true"]{background:var(--foil);border-color:var(--foil);color:var(--ground);font-weight:600}
  .filt button:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
  .filt small{font-size:12px;opacity:.75;margin-left:4px}
  .grid.f .card.feat{grid-column:auto;grid-template-columns:1fr;grid-template-rows:auto 1fr}
  .grid.f .card.feat .il{border-right:0;border-bottom:1px solid var(--line)}
  [hidden]{display:none!important}
"""
GROUPS = [("tum", "Tümü"), ("beyin", "Beyin ve sinirler"), ("hareket", "Hareket ve ağrı"), ("kalp", "Kalp ve metabolizma"), ("gen", "Gen, hücre ve hedefli tedaviler"), ("tani", "Tanı ve teknoloji")]
def filt():
    cnt = {g: sum(1 for n in NEWS if n["g"] == g) for g, _ in GROUPS}
    cnt["tum"] = len(NEWS)
    return ('<div class="filt" role="group" aria-label="Konuya göre süz">' +
            "".join(f'<button type="button" data-f="{g}" aria-pressed="{"true" if g == "tum" else "false"}"><span>{t}</span><small>{cnt[g]}</small></button>' for g, t in GROUPS) +
            '</div>')
NEWS_JS = """<script>
(function(){
  var bar = document.querySelector('.filt'), grid = document.querySelector('.grid'); if (!bar || !grid) return;
  bar.addEventListener('click', function(e){
    var b = e.target.closest('button'); if (!b) return;
    var f = b.getAttribute('data-f');
    bar.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
    grid.classList.toggle('f', f !== 'tum');
    grid.querySelectorAll('.card').forEach(function(c){ c.hidden = f !== 'tum' && c.getAttribute('data-g') !== f; });
  });
  // başlık dizininden gidilen haber süzgeçle gizlenmiş olmasın
  var box = document.querySelector('.hl-box');
  if (box) box.addEventListener('click', function(e){
    if (!e.target.closest('a')) return;
    var all = bar.querySelector('[data-f="tum"]'); if (all && all.getAttribute('aria-pressed') !== 'true') all.click();
  });
})();
</script>
"""

def news_id(n):
    t = _html.unescape(_re.sub(r"<[^>]+>", "", n["title"])).replace("İ", "i").replace("I", "ı").lower()
    t = t.translate(str.maketrans("çğıöşüâîû", "cgiosuaiu"))
    return "h-" + _re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:48].rstrip("-")
assert len({news_id(n) for n in NEWS}) == len(NEWS)
STAR = '<svg class="prem-s" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 2.4l2.95 6.02 6.63.94-4.8 4.66 1.14 6.6L12 17.5l-5.92 3.12 1.14-6.6-4.8-4.66 6.63-.94z"/></svg>'
def _nprem(n):
    return n["cat"].startswith("Nobel")
def headlines(pre="", items=None):
    """Haber başlıkları: konu etiketi, başlık ve tarih; her satır haberin kendisine gider."""
    rows = "".join(f'<li><a href="{pre}#{news_id(n)}"><span class="hl-c">{n["cat"]}{STAR if _nprem(n) else ""}</span><span class="hl-t">{n["title"]}</span><small>{n["date"]}</small></a></li>'
                   for n in (items or NEWS))
    return f'<ul class="hl">{rows}</ul>'
HL_CSS = """
  /* haber başlıkları listesi */
  .hl{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 34px}
  @media (max-width:820px){.hl{grid-template-columns:minmax(0,1fr)}}
  .hl a{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:2px 12px;align-items:baseline;padding:11px 2px;border-bottom:1px solid var(--line);text-decoration:none;color:var(--ink)}
  .hl-c{grid-column:1/-1;font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;color:var(--foil)}
  .hl-t{font-family:var(--display);font-size:18px;line-height:1.3}
  .hl small{font-size:12.5px;color:var(--muted);white-space:nowrap}
  .hl a:hover .hl-t{color:var(--foil)}
  /* öne çıkan içerik yıldızı: Dizin 12 Sırrı, Üç Kapı, Nobel 2026 */
  .prem-s{display:inline-block;flex:none;width:1em;height:1em;vertical-align:-.12em;fill:#e8bd5f;filter:drop-shadow(0 0 3px rgba(232,189,95,.5))}
  .hl-c .prem-s{width:13px;height:13px;margin-left:6px;vertical-align:-2px}
  .chip .prem-s{width:12px;height:12px;margin-left:5px;vertical-align:-1px}
  .pill .prem-s{width:14px;height:14px;margin-left:7px}
  .pill.prem{border-color:rgba(216,178,94,.6);background:rgba(216,178,94,.09);color:var(--ink)}
  .kc.prem{position:relative;border-color:rgba(216,178,94,.42)}
  .kc.prem:hover{border-color:rgba(216,178,94,.8)}
  .kc .kc-star{position:absolute;top:10px;right:10px;z-index:1;width:34px;height:34px;border-radius:50%;display:grid;place-items:center;
    background:rgba(18,26,16,.82);border:1px solid rgba(216,178,94,.7);box-shadow:0 4px 14px rgba(0,0,0,.35);animation:premGlow 3.6s ease-in-out infinite}
  .kc .kc-star svg{display:block;width:18px;height:18px;background:none;border:0}
  @keyframes premGlow{0%,100%{box-shadow:0 4px 14px rgba(0,0,0,.35),0 0 0 0 rgba(216,178,94,0)}50%{box-shadow:0 4px 14px rgba(0,0,0,.35),0 0 0 5px rgba(216,178,94,.16)}}
  @media (prefers-reduced-motion:reduce){.kc .kc-star{animation:none}}
"""
def card(n):
    chip = {"Alzheimer": "chip", "Parkinson": "chip", "Huntington": "chip", "Uyku": "chip", "Nöroteknoloji": "chip", "Genetik": "chip g", "Kanser": "chip g", "Diyabet": "chip g"}.get(n["cat"], "chip o")
    srcs = " · ".join(f'<a href="{u}" target="_blank" rel="noopener">{t}</a>' for t, u in n["src"])
    rel = f'\n    <p class="rel"><a href="{n["rel"][1]}">{n["rel"][0]} →</a></p>' if n.get("rel") else ""
    return f'''<article class="card{' feat' if n.get('feat') else ''}" id="{news_id(n)}" data-g="{n["g"]}">
  <div class="il">{n["il"]}</div>
  <div class="body">
    <div class="tags"><span class="{chip}">{n["cat"]}{STAR if _nprem(n) else ""}</span><span>{n["date"]}</span></div>
    <h2>{n["title"]}</h2>
    <p>{n["text"]}</p>
    <p class="point">{n["point"]}</p>
    <p class="src">{"Kaynaklar" if len(n["src"]) > 1 else "Kaynak"}: {srcs}</p>{rel}
  </div>
</article>'''

NEWS_FAQ = [
 ("Günde 10.000 adım atmak şart mı?", "Hayır. 2026'da yayımlanan büyük bir gözlem çalışmasında en düşük risk günde 7.500–10.000 adım atanlarda görüldü; ama günde 5.000'den az adım atanlarda bile adımların bir kısmını tempolu atmak daha düşük riskle ilişkiliydi. 10.000 adım hedefi kanıttan çok 1960'lardaki bir Japon adımsayar kampanyasından geliyor. Bugünkü adım sayınızı kademeli artırmak ve bir kısmını tempolu yürümek iyi bir başlangıçtır."),
 ("Alzheimer kan testiyle anlaşılabilir mi?", "ABD'de FDA, Mayıs 2025'ten bu yana beyindeki amiloid ve tau değişikliklerini kandan ölçen dört testin kullanımına izin verdi. Ancak bu testler yalnızca hafıza şikâyeti olan kişilerde, hekim değerlendirmesinin parçası olarak kullanılmak üzere izin aldı; şikâyeti olmayan sağlıklı kişilerde tarama için uygun değildir."),
 ("Trontinemab onaylı bir Alzheimer ilacı mı?", "Hayır, henüz onaylı değildir; büyük faz III çalışmaları sürmektedir. Erken faz verilerine göre yüksek dozu alan hastaların yaklaşık %91–92'sinde 28 haftada beyindeki amiloid birikimi eşik değerin altına indi. Az sayıda hastada beyinde mikro kanama gibi yan etkiler izlendi."),
 ("Mamografiyi artık yapay zekâ mı okuyacak?", "Hayır. İsveç'teki MASAI çalışmasında yapay zekâ radyologların yerine değil, onlara destek olarak kullanıldı. Bu düzende kanserlerin daha fazlası taramada yakalandı, iki tarama arasında ortaya çıkan kanserler %12 azaldı ve yanlış alarm oranı artmadı."),
 ("Domuz organları insanlara nakledilebiliyor mu?", "Henüz deneysel. ABD'de bir hastaya nakledilen genetiği düzenlenmiş domuz böbreği onu 271 gün diyalizden uzak tuttu ve ardından insan böbreği nakline köprü oldu. Bu yöntemin güvenliği ve kalıcılığı klinik çalışmalarda araştırılıyor."),
 ("GLP-1 zayıflama ilaçları artık hap olarak da var mı?", "Evet. ABD'de Aralık 2025'te ağızdan semaglutid (Wegovy hap), Nisan 2026'da da yemek ve su kısıtlaması olmadan alınabilen orforglipron (Foundayo) onaylandı. 72 haftalık çalışmada orforglipronun en yüksek dozuyla ortalama kilo kaybı %12,4 oldu. Bu ilaçlar beslenme düzeni ve hareketle birlikte, hekim kontrolünde kullanılır."),
 ("Kanseri kandan erken yakalayan testler kullanıma hazır mı?", "Henüz değil. 142.942 kişilik NHS-Galleri çalışmasında test, taramayla yakalanan kanser sayısını yaklaşık 4 kat artırdı ve evre IV tanıları %14 azalttı; ancak evre III–IV kanserlerde hedeflenen azalma sağlanamadı ve yaşam süresine etkisi henüz bilinmiyor. Bu testler mevcut tarama programlarının yerine geçmez."),
 ("Parkinson hastalığında kök hücre tedavisi var mı?", "Henüz rutin bir tedavi değildir. STEM-PD adlı erken evre çalışmada kök hücreden üretilen dopamin hücreleri 8 hastaya nakledildi; bir yıl sonra değerlendirilen 7 hastanın 6'sı ilaç dozunu belirgin şekilde azalttı ve hücrelere bağlı ciddi yan etki görülmedi. Etkinin kalıcılığını görmek için daha uzun takip ve daha büyük çalışmalar gerekiyor."),
 ("Diz kireçlenmesinde yürüyüş şeklini değiştirmek ağrıyı azaltır mı?", "68 kişilik bir çalışmada kişiye özel belirlenen ayak açısıyla yapılan yürüyüş eğitimi, bir yılda ağrıyı 10 üzerinden ortalama 2,5 puan azalttı; sahte eğitim grubunda azalma 1,3 puandı. Bu herkese uyan bir öneri değildir; kişiye özel ölçüm ve uzman eşliği gerekir."),
 ("Egzersiz kanser tedavisinin bir parçası olabilir mi?", "Kolon kanseri tedavisini tamamlamış 889 hastayla yapılan CHALLENGE çalışmasında 3 yıllık, antrenör destekli egzersiz programına katılanlarda kanserin geri dönme, yeni kanser ya da ölüm riski %28, ölüm riski %37 daha düşüktü. Egzersiz programına başlamadan önce tedavi ekibinizle görüşün."),
 ("Talasemi ve orak hücreli anemi gen tedavisiyle tedavi edilebilir mi?", "Onaylı ilk CRISPR tedavisi Casgevy, orak hücreli anemi ve beta talasemide kullanılmaktadır. Avrupa İlaç Ajansı'nın değerlendirdiği çalışmalarda orak hücre hastalarının 29'unun 28'i en az bir yıl ağrı krizi yaşamadı, talasemi hastalarının 42'sinin 39'u en az bir yıl kan nakline ihtiyaç duymadı. Tedavi pahalıdır ve her merkezde uygulanamamaktadır."),
]
NEWS_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Bilim gündemi</p>
    <h1>Geleceğin tıbbı, bugün</h1>
    <p class="lede">Tıbbın öncü alanlarındaki önemli gelişmelerin kısa ve anlaşılır özetleri. Her haberin altında kaynağı var.</p>
    <p class="meta">Son güncelleme: 20 Ekim 2026</p>
  </div>
</header>
<main>
  <section>
    <div class="wrap">
      <details class="hl-box"><summary><span>Başlıklar</span><small>{len(NEWS)}</small></summary>{headlines()}</details>
      {filt()}
      <div class="grid">
{"".join(card(n) for n in NEWS)}
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(NEWS_FAQ)}
      <div class="note" style="margin-top:28px">Bu sayfa bilgilendirme amaçlıdır, tedavi önerisi değildir. Bahsedilen test ve tedavilerin bazıları Türkiye'de henüz kullanımda olmayabilir. Görseller temsili çizimlerdir.</div>
    </div>
  </section>
</main>'''

page("yenilikler.html", "Geleceğin Tıbbı", "Huntington gen tedavisi, pankreas kanserinde yeni ilaç, zayıflama hapları, Alzheimer kan testleri, Parkinson'da kök hücre nakli, mRNA kanser aşısı ve daha fazlası: kısa, kaynaklı özetler.",
     "yenilikler.html", NEWS_CSS + HL_CSS + """
  .card{scroll-margin-top:84px}
  .hl-box{margin:0 0 22px;border:1px solid var(--line);border-radius:14px;background:var(--ground-2)}
  .hl-box summary{cursor:pointer;list-style:none;display:flex;align-items:baseline;gap:8px;padding:13px 44px 13px 16px;position:relative;font-family:var(--display);font-size:19px}
  .hl-box summary::-webkit-details-marker{display:none}
  .hl-box summary small{font-family:var(--body);font-size:12.5px;color:var(--muted)}
  .hl-box summary::after{content:"+";position:absolute;right:16px;top:9px;font-family:var(--body);font-size:26px;line-height:1;color:var(--foil);transition:transform .2s}
  .hl-box[open] summary::after{transform:rotate(45deg)}
  .hl-box summary:focus-visible{outline:2px solid var(--gold);outline-offset:2px;border-radius:12px}
  .hl-box .hl{padding:0 16px 8px;border-top:1px solid var(--line)}
""", NEWS_BODY, NEWS_JS,
     seo_title="Geleceğin Tıbbı: Güncel Bilimsel Gelişmeler | İhsan Eren",
     about=[cond("Alzheimer hastalığı"), cond("Parkinson hastalığı"), cond("Omurilik yaralanması"), cond("Bel ağrısı", "low-back-pain"), cond("Diz kireçlenmesi", "knee-osteoarthritis"), cond("CPS1 eksikliği"), cond("Orak hücreli anemi"), cond("Beta talasemi"), cond("Meme kanseri"), cond("Kalıtsal işitme kaybı"), cond("Son dönem böbrek yetmezliği"), cond("Sistemik lupus eritematozus"), cond("Melanom"), cond("Kolon kanseri"), cond("Tip 1 diyabet"), cond("Amiyotrofik lateral skleroz (ALS)"), cond("Huntington hastalığı"), cond("Narkolepsi"), cond("Pankreas kanseri"), cond("Yüksek tansiyon (hipertansiyon)"), cond("Yüksek kolesterol"), cond("Obezite")],
     faq_items=NEWS_FAQ)

# ------------------------------------------------------------------ HOME SECTION (snippet written to file)
HOME_CSS = """
  /* bilgi köşesi */
  .kose{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
  @media (max-width:820px){.kose{grid-template-columns:1fr}}
  .kc{display:grid;grid-template-rows:auto 1fr;border:1px solid var(--line);border-radius:12px;overflow:hidden;background:var(--ground-2);text-decoration:none;color:var(--ink);transition:border-color .2s}
  .kc:hover{border-color:var(--line-strong)}
  .kc svg{display:block;width:100%;height:auto;background:#223020;border-bottom:1px solid var(--line)}
  .kc .b{padding:16px;display:grid;gap:6px;align-content:start}
  .kc .k{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--foil);font-weight:600}
  .kc h3{font-size:22px;margin:0}
  .kc p{margin:0;color:var(--muted);font-size:15px}
  .kc .go{color:var(--foil);font-size:14px;font-weight:600;margin-top:4px}
"""
TH_BREATH = '''<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="160" cy="75" r="58" fill="none" stroke="rgba(216,178,94,.35)"/><circle cx="160" cy="75" r="42" fill="rgba(226,171,71,.22)"/><circle cx="160" cy="75" r="26" fill="rgba(143,164,118,.45)"/><path d="M40 75c20-14 40-14 60 0M220 75c20 14 40 14 60 0" fill="none" stroke="#8fa476" stroke-width="3" stroke-linecap="round"/></svg>'''
TH_SHOULDER = '''<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="160" cy="40" r="14" fill="#8fa476"/><path d="M128 64h64M160 64v70" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/><path d="M128 64 L112 108" stroke="#d8b25e" stroke-width="8" stroke-linecap="round"/><path d="M192 64 L210 106" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/><path d="M100 50a44 44 0 0 1 20-26" fill="none" stroke="#d8b25e" stroke-width="3" stroke-dasharray="4 5" stroke-linecap="round"/><circle cx="128" cy="64" r="14" fill="none" stroke="#e2ab47" stroke-width="2.5"/></svg>'''
TH_DNA = '''<svg viewBox="0 0 320 150" aria-hidden="true"><g fill="none" stroke-width="4" stroke-linecap="round"><path d="M40 75 C80 35 120 35 160 75 S240 115 280 75" stroke="#8fa476"/><path d="M40 75 C80 115 120 115 160 75 S240 35 280 75" stroke="#ece5cf" opacity=".8"/></g><g stroke="rgba(236,229,207,.35)" stroke-width="3" stroke-linecap="round"><path d="M64 59v32M96 49v52M128 53v44M192 59v32M224 49v52M256 53v44"/></g><path d="M160 61v28" stroke="#e2ab47" stroke-width="5" stroke-linecap="round"/></svg>'''
TH_NECK = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="160" cy="32" r="14" fill="#8fa476"/><path d="M126 74h68M160 74v64M126 74 L114 126M194 74 L206 126" stroke="#8fa476" stroke-width="7" stroke-linecap="round" fill="none"/><g stroke-linecap="round" stroke-width="5"><path d="M154 52h12" stroke="#8fa476"/><path d="M153 59h14M153 66h14" stroke="#e2ab47"/></g><circle cx="160" cy="60" r="21" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M128 50l-12-6M126 61h-14M192 50l12-6M194 61h14" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
TH_NERVE = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="160" cy="32" r="14" fill="#8fa476"/><path d="M126 74h68M160 74v64M194 74 L206 126" stroke="#8fa476" stroke-width="7" stroke-linecap="round" fill="none"/><path d="M126 74 L112 126" stroke="#d8b25e" stroke-width="8" stroke-linecap="round"/><g stroke-linecap="round" stroke-width="5"><path d="M154 52h12M153 66h14" stroke="#8fa476"/><path d="M153 59h14" stroke="#e2ab47"/></g><path d="M150 60 L134 70 L128 84 L120 96 L116 110 L108 124" fill="none" stroke="#e2ab47" stroke-width="2.5" stroke-dasharray="5 5" stroke-linecap="round" stroke-linejoin="round"/><path d="M96 128l-10 2M98 138l-8 6M108 140l-2 9" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
TH_IDEA = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M136 44a24 24 0 1 1 48 0c0 12-9 17-12 28h-24c-3-11-12-16-12-28z" fill="none" stroke="#8fa476" stroke-width="5" stroke-linejoin="round"/><path d="M148 84h24M150 94h20" stroke="#8fa476" stroke-width="5" stroke-linecap="round"/><path d="M160 12v-6M120 44h-8M200 44h8M130 18l-5-5M190 18l5-5" stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round"/><path d="M110 118h100" stroke="rgba(236,229,207,.25)" stroke-width="3" stroke-linecap="round"/></svg>"""

HOME_CSS = HOME_CSS + """
  .pill{display:inline-flex;align-items:center;padding:8px 14px;border:1px solid var(--line-strong);border-radius:999px;color:var(--ink-soft);text-decoration:none;font-size:14px}
  .pill:hover{color:var(--foil);border-color:var(--foil)}
  /* konu dizini: kategoriye göre gruplanmış haplar */
  .kose-idx{display:grid;gap:14px;margin-top:22px}
  .kg{display:grid;grid-template-columns:215px minmax(0,1fr);gap:8px 18px;align-items:start;padding-top:14px;border-top:1px solid var(--line)}
  .kg .lbl{display:flex;align-items:baseline;gap:8px;padding-top:9px;white-space:nowrap;font-size:12px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;color:var(--foil);text-decoration:none}
  .kg .lbl small{font-size:12px;letter-spacing:0;color:var(--muted);font-weight:400}
  .kg .lbl:hover span{text-decoration:underline}
  .kg .pl{display:flex;flex-wrap:wrap;gap:8px}
  @media (max-width:700px){.kg{grid-template-columns:minmax(0,1fr)}.kg .lbl{padding-top:0}}
  .kose-idx .all{justify-self:end;color:var(--foil);font-weight:600;font-size:15px;text-decoration:none}
  .kose-idx .all:hover{text-decoration:underline}
  /* yayın sayacı: kaç rehber yayında + dönen başlık */
  .pulse{display:grid;gap:12px;margin:22px 0;padding:16px 18px 14px;border:1px solid var(--line);border-radius:16px;max-width:760px;
    background:radial-gradient(120% 120% at 0% 0%,rgba(226,171,71,.10),transparent 60%),var(--ground-2)}
  .pulse p{max-width:none}
  .pulse-live{margin:0;display:flex;align-items:center;gap:9px;font-size:12px;letter-spacing:.16em;text-transform:uppercase;font-weight:600;color:var(--foil)}
  .pulse-live::before{content:"";flex:none;width:8px;height:8px;border-radius:50%;background:var(--gold);animation:pulse-dot 2s ease-out infinite}
  @keyframes pulse-dot{from{box-shadow:0 0 0 0 rgba(226,171,71,.65)}to{box-shadow:0 0 0 11px rgba(226,171,71,0)}}
  .pulse-nums{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
  @media (max-width:560px){.pulse-nums{grid-template-columns:repeat(2,minmax(0,1fr));gap:14px 12px}}
  .pulse-nums a{display:grid;gap:3px;align-content:start;text-decoration:none;color:var(--ink-soft);font-size:14px;line-height:1.3}
  .pulse-nums a:hover span{color:var(--foil)}
  .pn{font-family:var(--display);font-weight:400;font-size:clamp(36px,7vw,48px);line-height:1;color:var(--gold);font-variant-numeric:tabular-nums;text-shadow:0 0 22px rgba(226,171,71,.4)}
  .pulse-rot{margin:0;display:flex;align-items:baseline;gap:8px;min-width:0;padding-top:11px;border-top:1px solid var(--line);font-size:15px;color:var(--muted)}
  .pulse-rot > span:first-child{flex:none}
  .rot{display:block;flex:1;min-width:0;overflow:hidden}
  .rot a{display:none;max-width:100%;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:var(--ink);text-decoration:none}
  .rot a.on{display:block;animation:rot-in .5s cubic-bezier(.2,.7,.2,1) both}
  .rot a::after{content:" →";color:var(--foil)}
  .rot a:hover{color:var(--foil)}
  @keyframes rot-in{from{opacity:0;transform:translateY(70%)}}
  .kg .hl{flex:1 1 100%}
  .kg .hl li:first-child a,.kg .hl li:nth-child(2) a{padding-top:4px}
  @media (max-width:820px){.kg .hl li:nth-child(2) a{padding-top:11px}}
  /* girişte üç kapı: Bilgi köşesi, Kendine iyi bak, Bilim gündemi */
  .trio{list-style:none;margin:24px auto 0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;max-width:600px}
  .trio a{height:100%;box-sizing:border-box;display:grid;grid-template-rows:1fr auto;gap:4px;justify-items:center;padding:11px 6px 10px;border:1px solid var(--line-strong);border-radius:14px;text-decoration:none;text-align:center;
    background:radial-gradient(120% 120% at 50% 0%,rgba(226,171,71,.13),transparent 70%),rgba(236,229,207,.03);transition:border-color .2s,transform .2s}
  .trio a:hover{border-color:var(--gold);transform:translateY(-2px)}
  .trio b{align-self:center;font-family:var(--display);font-weight:400;font-size:clamp(15px,4.1vw,20px);line-height:1.15;color:var(--foil);text-wrap:balance}
  .trio span{display:flex;gap:4px;align-items:baseline;font-size:12px;color:var(--muted)}
  .trio i,.trio em{font-style:normal}
  .trio i{color:var(--ink-soft);font-variant-numeric:tabular-nums}
  .trio-k{margin:22px 0 0;max-width:none;font-size:12px;letter-spacing:.16em;text-transform:uppercase;font-weight:600;color:var(--muted)}
  .trio-k + .trio{margin-top:10px}
  /* girişte açılır hastalık listesi: hangi hastalıklar var, tek dokunuşla */
  .hx{max-width:600px;margin:10px auto 0;border:1px solid var(--line);border-radius:14px;background:rgba(236,229,207,.03);text-align:left}
  .hx summary{cursor:pointer;list-style:none;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:2px 12px;align-items:center;padding:12px 16px}
  .hx summary::-webkit-details-marker{display:none}
  .hx summary b{font-weight:600;font-size:15px;line-height:1.3;color:var(--ink)}
  .hx summary span{grid-column:1;font-size:13px;line-height:1.45;color:var(--muted)}
  .hx summary em{grid-column:1;font-style:normal;font-size:13px;font-weight:600;color:var(--foil)}
  .hx[open] summary em{display:none}
  .hx summary::after{content:"";grid-column:2;grid-row:1/4;width:8px;height:8px;margin:0 4px 5px;border-right:2px solid var(--foil);border-bottom:2px solid var(--foil);transform:rotate(45deg);transition:transform .2s}
  .hx[open] summary::after{transform:rotate(-135deg);margin:5px 4px 0}
  .hx summary:focus-visible{outline:2px solid var(--gold);outline-offset:2px;border-radius:12px}
  .hx[open]{border-color:var(--line-strong)}
  .hx + .hx{margin-top:8px}
  .hx-list{display:grid;gap:14px;padding:14px 16px 16px;border-top:1px solid var(--line)}
  .hx-g{display:grid;gap:7px}
  .hx-g > span{font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;color:var(--foil)}
  .hx-g > div{display:flex;flex-wrap:wrap;gap:6px}
  .hx .pill{padding:6px 11px;font-size:13.5px}
  .hx-all{justify-self:end;font-weight:600;font-size:14px;color:var(--foil);text-decoration:none}
  .hx-all:hover{text-decoration:underline}
  .hero .trio-k,.hero .trio,.hero .hx{animation:rise calc(.85s*var(--k)) cubic-bezier(.2,.7,.2,1) both;animation-delay:calc(1.35s*var(--k))}
""" + HL_CSS

PREM = {"dizin-12-sirri.html", "uc-kapi.html", "nobel-2026.html"}
def _pc(h):
    return "pill prem" if h in PREM else "pill"

def KC(href, th, k, title, text, go="Oku →", ext_link=False):
    tgt = ' target="_blank" rel="noopener"' if ext_link else ""
    return f'<a class="{"kc prem" if href in PREM else "kc"}" href="{href}"{tgt}>{'<span class="kc-star" aria-hidden="true">' + STAR + '</span>' if href in PREM else ""}{th}<span class="b"><span class="k">{k}</span><h3>{title}</h3><p>{text}</p><span class="go">{go}</span></span></a>'

TH_BACK = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="156" cy="24" r="13" fill="#8fa476"/><path d="M156 40 Q146 72 156 104" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/><path d="M152 50 L170 80 M156 104 L146 146 M156 104 L168 146" stroke="#8fa476" stroke-width="7" stroke-linecap="round" fill="none"/><path d="M149 80 Q147 92 153 104" fill="none" stroke="#e2ab47" stroke-width="7" stroke-linecap="round"/><circle cx="151" cy="92" r="20" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M122 84h-12M124 98l-11 5M180 84h12M178 98l11 5" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
TH_SCIATICA = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="150" cy="22" r="13" fill="#8fa476"/><path d="M150 38 Q140 66 150 94" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/><path d="M146 48 L164 76 M150 94 L140 144" stroke="#8fa476" stroke-width="7" stroke-linecap="round" fill="none"/><path d="M150 94 L166 118 L162 144" stroke="#d8b25e" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M146 84 L158 100 L168 112 L170 126 L168 138" fill="none" stroke="#e2ab47" stroke-width="2.5" stroke-dasharray="5 5" stroke-linecap="round"/><path d="M178 140l10 2M176 130l10-4M170 148l8 2" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/><circle cx="147" cy="86" r="4" fill="#e2ab47"/></svg>"""
TH_KNEE = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M138 14 L152 74 L140 132 H176" fill="none" stroke="#8fa476" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/><circle cx="152" cy="74" r="9" fill="#d8b25e"/><circle cx="152" cy="74" r="22" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M118 66h-12M120 82l-11 5M186 66h12M184 82l11 5" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
TH_STROKE = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="152" cy="24" r="13" fill="#8fa476"/><circle cx="152" cy="24" r="22" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M152 40 L148 92 M154 50 L176 72 L182 78 M148 92 L164 144" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M152 50 L136 70 L142 86 M148 92 L136 144" stroke="#d8b25e" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M182 76 V146 M182 76 h8" stroke="#ece5cf" stroke-width="4" stroke-linecap="round" opacity=".7"/><path d="M118 20h-12M120 34l-11 5M186 20h12M184 34l11 5" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_STROKE = KC("inme-rehabilitasyonu.html", TH_STROKE, "Rehabilitasyon rehberi", "İnme (felç) sonrası rehabilitasyon", "Beyin nasıl toparlanır, rehabilitasyona ne zaman başlanmalı? Evde altı egzersiz ve güvenli ev önerileri.")
TH_HEEL = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M150 8 L156 74" stroke="#8fa476" stroke-width="9" stroke-linecap="round"/><path d="M144 72 L164 72 L172 88 L214 102 Q224 106 220 114 L150 116 Q132 116 132 102 Z" fill="#8fa476"/><path d="M146 124 Q180 127 214 121" fill="none" stroke="#e2ab47" stroke-width="3" stroke-dasharray="5 5" stroke-linecap="round"/><circle cx="146" cy="110" r="7" fill="#d8b25e"/><circle cx="146" cy="110" r="22" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M112 100h-12M114 114l-11 5M116 88l-10-6" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_HEEL = KC("topuk-dikeni.html", TH_HEEL, "Hastalık rehberi", "Topuk dikeni (plantar fasiit)", "Sabah ilk adımda topuk ağrısı, röntgendeki diken önemli mi? Evde altı egzersiz ve tabanlık önerileri.")
TH_IMPINGE = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="160" cy="24" r="13" fill="#8fa476"/><path d="M128 54 H192 M160 40 V108 M160 108 L148 146 M160 108 L172 146 M192 54 L200 96" stroke="#8fa476" stroke-width="7" stroke-linecap="round" fill="none"/><path d="M128 54 L96 32" stroke="#d8b25e" stroke-width="8" stroke-linecap="round"/><path d="M98.6 71 A34 34 0 0 1 98.6 37" fill="none" stroke="#e2ab47" stroke-width="3" stroke-dasharray="5 5" stroke-linecap="round"/><circle cx="128" cy="54" r="16" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M122 28l-4-10M136 28l4-10M110 44l-10-4" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_IMPINGE = KC("omuz-sikismasi.html", TH_IMPINGE, "Hastalık rehberi", "Omuz sıkışması", "Kolu kaldırınca omuz ağrısı, MR'daki yırtık önemli mi, ameliyat gerekir mi? Evde altı egzersiz.")
TH_CTS = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M160 150 V102" stroke="#8fa476" stroke-width="16" stroke-linecap="round"/><rect x="138" y="60" width="44" height="46" rx="12" fill="#8fa476"/><path d="M144 60 V30 M155 60 V20 M166 60 V22 M177 62 V36 M140 92 L122 74 L116 60" stroke="#8fa476" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M160 140 V104 L152 86 L146 64 M152 86 L156 60 M152 86 L166 62 M152 90 L128 76" fill="none" stroke="#e2ab47" stroke-width="2.5" stroke-dasharray="4 4" stroke-linecap="round"/><circle cx="160" cy="108" r="16" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M140 16l-4-8M156 10v-8M172 14l4-8M110 58l-9-4" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_CTS = KC("karpal-tunel-sendromu.html", TH_CTS, "Hastalık rehberi", "Karpal tünel sendromu", "Elde uyuşma neden geceleri artar, bilgisayar kullanmak neden olur mu? Gece ateli ve dört egzersiz.")
TH_FALLS = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M204 60 H250 M240 60 V146" stroke="#ece5cf" stroke-width="5" stroke-linecap="round" opacity=".55"/><circle cx="156" cy="22" r="13" fill="#8fa476"/><path d="M156 38 V92 M156 50 L182 60 L206 60 M156 92 V142" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M156 92 L162 116 L144 128" stroke="#d8b25e" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M110 146 H200" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M118 70 A40 40 0 0 1 118 30 M194 30 A40 40 0 0 1 194 44" fill="none" stroke="#e2ab47" stroke-width="3" stroke-dasharray="5 5" stroke-linecap="round"/><circle cx="156" cy="142" r="5" fill="#e2ab47"/></svg>"""
C_FALLS = KC("dusme-onleme.html", TH_FALLS, "Rehabilitasyon rehberi", "Düşmeleri önleme ve denge", "Yaşlılarda düşme neden olur, nasıl önlenir? Evde altı denge egzersizi ve ev güvenliği kontrol listesi.")
TH_PROSTH = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M146 8 L158 70 L144 138 H176" fill="none" stroke="#8fa476" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/><rect x="146" y="60" width="24" height="20" rx="6" fill="#d8b25e"/><path d="M150 70 H166" stroke="#1c2819" stroke-width="2.5" stroke-linecap="round"/><circle cx="158" cy="70" r="26" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M200 138 V92 M200 92 h10" stroke="#ece5cf" stroke-width="4" stroke-linecap="round" opacity=".7"/><path d="M116 62h-12M118 78l-11 5M198 50l10-6" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_PROSTH = KC("protez-sonrasi.html", TH_PROSTH, "Rehabilitasyon rehberi", "Diz ve kalça protezi sonrası", "İlk haftalarda ne beklenir, ne zaman yürünür ve araç kullanılır? Evde altı egzersiz ve güvenli ev önerileri.")
TH_DESK = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M178 70 H232 M204 70 V132 M188 132 H220" stroke="#ece5cf" stroke-width="5" stroke-linecap="round" opacity=".55"/><rect x="190" y="36" width="36" height="26" rx="3" fill="none" stroke="#8fa476" stroke-width="5"/><circle cx="140" cy="30" r="13" fill="#8fa476"/><path d="M142 46 L138 96 M140 58 L170 70 L186 66 M138 96 L166 96 L168 132 M122 96 V132" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M120 100 H150" stroke="#d8b25e" stroke-width="7" stroke-linecap="round"/><circle cx="98" cy="46" r="18" fill="none" stroke="#e2ab47" stroke-width="3"/><path d="M98 36 V46 L106 50" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>"""
C_DESK = KC("masa-basi.html", TH_DESK, "Kendine iyi bak", "Masa başında çalışanlar için", "Doğru duruş diye bir şey var mı, ne sıklıkla mola verilmeli? Mola için altı hareket ve rahat çalışma düzeni.")
TH_HIP = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="160" cy="18" r="12" fill="#8fa476"/><path d="M160 32 V78 M160 44 L140 66 M160 44 L180 66 M160 78 L146 142 M160 78 L176 140" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M138 70 Q160 88 182 70" fill="none" stroke="#ece5cf" stroke-width="5" stroke-linecap="round" opacity=".6"/><circle cx="149" cy="84" r="7" fill="#d8b25e"/><circle cx="149" cy="84" r="20" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M116 78h-12M118 94l-11 5M120 64l-10-6" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_HIP = KC("kalca-kireclenmesi.html", TH_HIP, "Hastalık rehberi", "Kalça kireçlenmesi", "Kasık ağrısı neden dize vurur, egzersiz ne kadar işe yarar, hangi iğneler önerilmez? Evde altı egzersiz.")
TH_ELBOW = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M110 40 L160 88 L222 70" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><rect x="220" y="56" width="22" height="26" rx="9" fill="#8fa476" transform="rotate(-16 231 69)"/><circle cx="160" cy="88" r="8" fill="#d8b25e"/><circle cx="160" cy="88" r="22" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M170 96 L196 86" stroke="#e2ab47" stroke-width="2.5" stroke-dasharray="4 4" stroke-linecap="round"/><path d="M146 122l-6 10M162 126v12M178 120l8 9" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_ELBOW = KC("tenisci-dirsegi.html", TH_ELBOW, "Hastalık rehberi", "Tenisçi dirseği", "Tenis oynamayanlarda neden olur, kortizon iğnesi yapılmalı mı? Evde altı egzersiz ve günlük hayat önerileri.")
TH_OSTEO = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M112 58 a12 12 0 1 1 18 -14 L190 44 a12 12 0 1 1 18 14 a12 12 0 1 1 -18 14 L130 72 a12 12 0 1 1 -18 -14z" fill="none" stroke="#8fa476" stroke-width="6" stroke-linejoin="round"/><g fill="#8fa476" opacity=".55"><circle cx="146" cy="58" r="3"/><circle cx="160" cy="52" r="2.5"/><circle cx="172" cy="62" r="3.5"/><circle cx="184" cy="54" r="2"/><circle cx="154" cy="66" r="2"/></g><path d="M162 44 L156 58 L166 60 L158 72" fill="none" stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M118 110 H202" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M130 110 V96 M150 110 V86 M170 110 V92 M190 110 V80" stroke="#d8b25e" stroke-width="6" stroke-linecap="round"/></svg>"""
C_OSTEO = KC("kemik-erimesi.html", TH_OSTEO, "Hastalık rehberi", "Kemik erimesi (osteoporoz)", "Egzersiz güvenli mi, hangi hareketlerden kaçınmalı? Güçlü, dengeli ve dik: evde altı egzersiz.")
TH_ANKLE = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M150 8 L154 78" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/><g transform="rotate(-18 154 84)"><path d="M144 78 L166 78 L174 92 L212 104 Q220 108 216 116 L150 118 Q134 118 134 104 Z" fill="#8fa476"/></g><circle cx="160" cy="92" r="7" fill="#d8b25e"/><circle cx="160" cy="92" r="22" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M196 70 A40 40 0 0 1 206 100" fill="none" stroke="#e2ab47" stroke-width="3" stroke-dasharray="5 5" stroke-linecap="round"/><path d="M122 86h-12M124 100l-11 5M126 72l-10-6" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_ANKLE = KC("ayak-bilegi-burkulmasi.html", TH_ANKLE, "Hastalık rehberi", "Ayak bileği burkulması", "Burkulan ayağa basılır mı, röntgen gerekir mi, neden tekrarlar? Evde altı egzersiz ve spora dönüş.")
TH_SUN = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M40 118h240" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M110 118a50 50 0 0 1 100 0" fill="rgba(226,171,71,.2)" stroke="#e2ab47" stroke-width="3"/><path d="M160 54v-14M118 70l-10-10M202 70l10-10M96 100H82M224 100h14" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/><circle cx="160" cy="62" r="9" fill="#8fa476"/><path d="M160 74v30M160 104l-9 14M160 104l9 14M160 80l-14-22M160 80l14-22" stroke="#8fa476" stroke-width="6" stroke-linecap="round" fill="none"/></svg>"""
TH_STEPS = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="160" cy="75" r="56" fill="none" stroke="rgba(236,229,207,.12)" stroke-width="9"/><path d="M160 19a56 56 0 1 1 -53.3 73.3" fill="none" stroke="#e2ab47" stroke-width="9" stroke-linecap="round"/><g fill="#8fa476"><ellipse cx="146" cy="84" rx="8" ry="13"/><ellipse cx="146" cy="104" rx="6" ry="7"/><ellipse cx="174" cy="56" rx="8" ry="13"/><ellipse cx="174" cy="76" rx="6" ry="7"/></g></svg>"""
TH_MOON = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M176 22a44 44 0 1 0 38 62 36 36 0 1 1 -38 -62z" fill="#e2ab47"/><g fill="#ece5cf" opacity=".7"><circle cx="112" cy="36" r="2.5"/><circle cx="96" cy="64" r="2"/><circle cx="238" cy="30" r="2"/><circle cx="252" cy="58" r="2.5"/></g><path d="M70 128h180M84 128v-18h52a10 10 0 0 1 10 10v8" stroke="#8fa476" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><rect x="92" y="98" width="30" height="12" rx="6" fill="#8fa476"/><text x="226" y="108" fill="#d8b25e" font-family="Marcellus,serif" font-size="22">z</text><text x="240" y="92" fill="#d8b25e" font-family="Marcellus,serif" font-size="16">z</text></svg>"""
C_MORNING = KC("sabah-rutini.html", TH_SUN, "Kendine iyi bak", "Güne 5 dakikayla başlayın", "Yatakta başlayıp ayakta biten dokuz hareket. Ekrandaki zamanlayıcıyla birlikte yapın.")
C_MOVE = KC("hareket.html", TH_STEPS, "Kendine iyi bak", "Ne kadar hareket yeterli?", "Haftalık hareketinizi ölçün; günlük adım sayısı ve kısa hareket molaları hakkında güncel bulgular.")
C_SLEEP = KC("uyku.html", TH_MOON, "Kendine iyi bak", "İyi uyku için", "Kaç saat uyumalı, kahve uykuyu nasıl etkiler, uyku ile ağrı ilişkisi ve yatma saati planlayıcı.")
TH_PARK = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 146 H260" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M96 146h14M136 146h14M176 146h14M216 146h14" stroke="#e2ab47" stroke-width="5" stroke-linecap="round"/><circle cx="150" cy="22" r="13" fill="#8fa476"/><path d="M150 38 L152 88 M151 50 L126 78 M151 50 L180 70 M152 88 L124 140" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M152 88 L190 138" stroke="#d8b25e" stroke-width="8" stroke-linecap="round"/><path d="M122 124 A62 62 0 0 1 196 122" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5" stroke-linecap="round"/><circle cx="222" cy="46" r="6" fill="#e2ab47"/><path d="M228 46 V20 l11 5" stroke="#e2ab47" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/><circle cx="250" cy="64" r="5" fill="#e2ab47" opacity=".75"/><path d="M255 64 V42 l9 4" stroke="#e2ab47" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity=".75"/></svg>"""
TH_HIPFX = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M70 146 H250" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M190 72 H234 M194 72 L188 144 M230 72 L236 144 M191 104 H233" stroke="#ece5cf" stroke-width="5" stroke-linecap="round" opacity=".6" fill="none"/><circle cx="150" cy="24" r="13" fill="#8fa476"/><path d="M151 40 L156 94 M153 52 L192 74 M156 94 L144 144" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M156 94 L172 142" stroke="#d8b25e" stroke-width="8" stroke-linecap="round"/><circle cx="159" cy="98" r="7" fill="#d8b25e"/><circle cx="159" cy="98" r="21" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M114 84 l9 6 -7 6 9 6" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M116 116h-12M120 128l-10 6" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
TH_ONCO = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M100 134 L122 92 C136 70 138 46 122 30 C106 46 108 70 122 92 L144 134" fill="none" stroke="#e2ab47" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M188 60 H236" stroke="#8fa476" stroke-width="6" stroke-linecap="round"/><rect x="178" y="44" width="12" height="32" rx="4" fill="#8fa476"/><rect x="234" y="44" width="12" height="32" rx="4" fill="#8fa476"/><path d="M166 112 H190 l8 -18 10 34 8 -16 H258" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
C_HIPFX = KC("kalca-kirigi.html", TH_HIPFX, "Rehabilitasyon rehberi", "Kalça kırığı sonrası", "Ameliyattan sonra ne zaman yürünür, evde egzersiz neden fark eder? Altı egzersiz ve güvenlik önerileri.")
C_PARK = KC("parkinson.html", TH_PARK, "Rehabilitasyon rehberi", "Parkinson hastalığında egzersiz", "Hangi egzersiz daha iyi, donmalarla nasıl başa çıkılır? Büyük ve ritimli altı egzersiz ve videolar.")
TH_MS = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M84 64 L62 44 M80 80 L54 86 M88 90 L72 116 M98 60 L96 34" stroke="#8fa476" stroke-width="5" stroke-linecap="round" fill="none"/><circle cx="98" cy="75" r="17" fill="#8fa476"/><circle cx="98" cy="75" r="6" fill="#223020" opacity=".55"/><path d="M115 75 H262 M262 75 L274 62 M262 75 L276 76 M262 75 L272 90" stroke="#ece5cf" stroke-width="3.5" stroke-linecap="round" fill="none" opacity=".7"/><g fill="#8fa476"><rect x="122" y="65" width="30" height="20" rx="10"/><rect x="157" y="65" width="30" height="20" rx="10"/><rect x="227" y="65" width="30" height="20" rx="10"/></g><path d="M193 67 q5 3 8 -1 M196 83 q6 -4 10 0 M209 68 q4 4 9 1" stroke="#e2ab47" stroke-width="4" stroke-linecap="round" fill="none"/><circle cx="207" cy="75" r="23" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M207 40 v-12 M228 46 l8 -9 M186 46 l-8 -9" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_MS = KC("multipl-skleroz.html", TH_MS, "Rehabilitasyon rehberi", "Multipl skleroz (MS) ve egzersiz", "Egzersiz güvenli mi, atak tetikler mi? Yorgunluk ve sıcağa duyarlılıkla başa çıkma, kılavuz önerileri ve evde altı egzersiz.")
C_ONCO = KC("kanser-egzersiz.html", TH_ONCO, "Rehabilitasyon rehberi", "Kanser ve egzersiz", "Tedavi sırasında egzersiz güvenli mi, yorgunluğa iyi gelir mi? Kılavuz önerileri ve evde altı egzersiz.")
TH_COPD = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M160 8 V44 M160 44 L142 62 M160 44 L178 62" stroke="#d8b25e" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M148 52 Q116 50 106 96 Q100 134 126 136 Q150 136 150 110 Z" fill="#8fa476"/><path d="M172 52 Q204 50 214 96 Q220 134 194 136 Q170 136 170 110 Z" fill="#8fa476" opacity=".8"/><path d="M236 70 q10 8 0 16 M250 62 q16 16 0 32 M84 70 q-10 8 0 16 M70 62 q-16 16 0 32" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" fill="none"/></svg>"""
C_COPD = KC("koah.html", TH_COPD, "Rehabilitasyon rehberi", "KOAH'ta akciğer rehabilitasyonu", "Nefes darlığı varken egzersiz yapılır mı? 65 çalışmanın gösterdiği yararlar, büzük dudak nefesi, evde altı egzersiz ve videolar.")
TH_CARDIAC = """<svg viewBox="0 0 320 150" aria-hidden="true"><path transform="translate(110 24) scale(1)" d="M50 86 C22 64 8 46 8 30 C8 16 19 7 31 7 C39 7 46 12 50 20 C54 12 61 7 69 7 C81 7 92 16 92 30 C92 46 78 64 50 86Z" fill="#8fa476"/><path d="M62 78 H126 L140 50 L156 104 L170 64 L178 78 H258" fill="none" stroke="#e2ab47" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
C_CARDIAC = KC("kalp-rehabilitasyonu.html", TH_CARDIAC, "Rehabilitasyon rehberi", "Kalp rehabilitasyonu", "Kalp krizi, stent ya da bypass sonrası egzersiz güvenli mi? 85 çalışmanın gösterdikleri, evde altı egzersiz ve videolar.")
TH_MENISCUS = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M150 6 L156 52" stroke="#8fa476" stroke-width="14" stroke-linecap="round"/><path d="M126 70 Q124 54 140 52 H170 Q186 54 184 70 Q182 80 170 80 H140 Q128 80 126 70Z" fill="#8fa476"/><path d="M124 97 H186 Q190 105 178 107 L166 109 V148 H146 V109 L134 107 Q120 105 124 97Z" fill="#8fa476" opacity=".8"/><path d="M125 91 Q138 83 151 89" fill="none" stroke="#d8b25e" stroke-width="7" stroke-linecap="round"/><path d="M159 89 Q172 83 185 91" fill="none" stroke="#d8b25e" stroke-width="7" stroke-linecap="round"/><path d="M136 82 L139 87 L135 91" fill="none" stroke="#1c2819" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="155" cy="88" r="40" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M100 80h-12M102 96l-11 5M210 80h12M208 96l11 5" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
TH_FIBRO = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="160" cy="22" r="13" fill="#8fa476"/><path d="M134 50 H186 M160 38 V96 M134 50 L126 94 M186 50 L194 94 M160 96 L148 146 M160 96 L172 146" stroke="#8fa476" stroke-width="7" stroke-linecap="round" fill="none"/><g fill="#e2ab47"><circle cx="151" cy="44" r="4.5"/><circle cx="169" cy="44" r="4.5"/><circle cx="137" cy="60" r="4.5"/><circle cx="183" cy="60" r="4.5"/><circle cx="152" cy="94" r="4.5"/><circle cx="168" cy="94" r="4.5"/><circle cx="154" cy="122" r="4.5"/><circle cx="166" cy="122" r="4.5"/></g><g fill="none" stroke="#d8b25e" stroke-width="2" opacity=".75"><circle cx="137" cy="60" r="11"/><circle cx="183" cy="60" r="11"/><circle cx="152" cy="94" r="11"/><circle cx="168" cy="94" r="11"/></g><path d="M86 64 q8-8 16 0 t16 0 M202 94 q8-8 16 0 t16 0" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
TH_VERTIGO = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M64 112 H262 M70 112 V142 M256 112 V142" stroke="#ece5cf" stroke-width="5" stroke-linecap="round" opacity=".55"/><rect x="100" y="99" width="42" height="13" rx="6" fill="#ece5cf" opacity=".3"/><path d="M122 98 L186 106 L250 106" stroke="#8fa476" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M130 100 L160 108" stroke="#8fa476" stroke-width="6" stroke-linecap="round"/><path d="M122 98 L104 103" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/><circle cx="92" cy="104" r="13" fill="#8fa476"/><path d="M92 58 m-3 0 a3 3 0 1 1 6 0 a7 7 0 1 1 -14 0 a11 11 0 1 1 22 0 a15 15 0 1 1 -30 0" fill="none" stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round"/><path d="M60 92 A34 34 0 0 1 124 88" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5" stroke-linecap="round"/><path d="M118 82 l6 6 -8 2" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
TH_AS = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M112 6 V146" stroke="#ece5cf" stroke-width="5" stroke-linecap="round" opacity=".55"/><path d="M100 146 H220" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><circle cx="131" cy="24" r="13" fill="#8fa476"/><path d="M126 96 L126 146 M126 96 L136 146 M128 46 L144 70 L146 92" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><g fill="#d8b25e"><rect x="118" y="40" width="12" height="6" rx="2"/><rect x="118" y="48.5" width="12" height="6" rx="2"/><rect x="118" y="57" width="12" height="6" rx="2"/><rect x="118" y="65.5" width="12" height="6" rx="2"/><rect x="118" y="74" width="12" height="6" rx="2"/><rect x="118" y="82.5" width="12" height="6" rx="2"/></g><path d="M117 92 H131 L124 104 Z" fill="#e2ab47"/><circle cx="124" cy="94" r="17" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M188 52 H160 M168 44 L160 52 L168 60" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M160 90h12M158 104l11 5M158 78l11-5" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_MENISCUS = KC("menisku-yirtigi.html", TH_MENISCUS, "Hastalık rehberi", "Menisküs yırtığı", "MR'daki yırtık ameliyat gerektirir mi? Egzersizin ameliyat kadar etkili bulunduğu çalışmalar ve evde altı egzersiz.")
TH_ACL = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M150 6 L156 46" stroke="#8fa476" stroke-width="14" stroke-linecap="round"/><path d="M126 62 Q124 46 140 44 H170 Q186 46 184 62 Q182 72 170 72 H140 Q128 72 126 62Z" fill="#8fa476"/><path d="M124 106 H186 Q190 114 178 116 L166 118 V148 H146 V118 L134 116 Q120 114 124 106Z" fill="#8fa476" opacity=".8"/><path d="M170 75 L142 103" stroke="#d8b25e" stroke-width="6" stroke-linecap="round" opacity=".4"/><path d="M141 75 L151 85" stroke="#d8b25e" stroke-width="8" stroke-linecap="round"/><path d="M160 94 L170 104" stroke="#d8b25e" stroke-width="8" stroke-linecap="round"/><path d="M198 82h12M196 97l11 5M112 82h-12M114 97l-11 5" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_ACL = KC("on-capraz-bag.html", TH_ACL, "Hastalık rehberi", "Ön çapraz bağ yaralanması", "Her yırtık ameliyat gerektirir mi? Rehabilitasyonla başlayanların yarısının ameliyat olmadığı çalışmalar, spora dönüş ölçütleri ve evde altı egzersiz.")
TH_RA = """<svg viewBox="0 0 320 150" aria-hidden="true"><g stroke="#8fa476" stroke-width="13" stroke-linecap="round" fill="none"><path d="M138 86 V36"/><path d="M156 82 V24"/><path d="M174 84 V30"/><path d="M191 90 V46"/><path d="M130 112 L108 88"/></g><rect x="128" y="82" width="72" height="56" rx="16" fill="#8fa476"/><g fill="#e2ab47"><circle cx="138" cy="60" r="5"/><circle cx="156" cy="52" r="5"/><circle cx="174" cy="56" r="5"/><circle cx="191" cy="67" r="5"/><circle cx="138" cy="86" r="5"/><circle cx="156" cy="82" r="5"/><circle cx="174" cy="84" r="5"/><circle cx="191" cy="90" r="5"/></g></svg>"""
C_RA = KC("romatoid-artrit.html", TH_RA, "Hastalık rehberi", "Romatoid artrit ve egzersiz", "Egzersiz iltihaplı eklemlere zarar verir mi? Araştırmaların gösterdikleri, alevlenmede ne yapmalı, el egzersizleri ve videolar.")
TH_COLD = """<svg viewBox="0 0 320 150" aria-hidden="true"><g stroke="#8fa476" stroke-width="7" stroke-linecap="round" fill="none"><path d="M160 22 V128"/><path d="M114 48 L206 102"/><path d="M114 102 L206 48"/><path d="M148 34 L160 46 L172 34"/><path d="M148 116 L160 104 L172 116"/><path d="M118 66 L134 60 L130 44"/><path d="M202 84 L186 90 L190 106"/><path d="M118 84 L134 90 L130 106"/><path d="M202 66 L186 60 L190 44"/></g><circle cx="160" cy="75" r="9" fill="#e2ab47"/></svg>"""
C_COLD = KC("surekli-usume.html", TH_COLD, "Hastalık rehberi", "Sürekli üşüme (soğuğa duyarlılık)", "Herkes rahatken siz neden üşüyorsunuz? Olası nedenler, istenen testler, günlük önlemler ve tamamlayıcı yöntemler için kanıt.")
TH_TREMOR = """<svg viewBox="0 0 320 150" aria-hidden="true"><g stroke="#8fa476" stroke-width="13" stroke-linecap="round" fill="none"><path d="M138 86 V36"/><path d="M156 82 V24"/><path d="M174 84 V30"/><path d="M191 90 V46"/><path d="M130 112 L108 88"/></g><rect x="128" y="82" width="72" height="56" rx="16" fill="#8fa476"/><g stroke="#e2ab47" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none"><path d="M222 40 l10 12 l-10 12 l10 12 l-10 12 l10 12"/><path d="M244 52 l8 10 l-8 10 l8 10 l-8 10"/><path d="M98 40 l-10 12 l10 12 l-10 12 l10 12"/><path d="M76 52 l-8 10 l8 10 l-8 10 l8 10"/></g></svg>"""
C_TREMOR = KC("titreme.html", TH_TREMOR, "Hastalık rehberi", "Titreme (tremor)", "Eller neden titrer? Titreme türleri, nedenin nasıl araştırıldığı, günlük hayat önerileri, egzersizler ve akupunktur için kanıt.")
TH_FACE = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="160" cy="75" r="56" fill="rgba(143,164,118,.16)" stroke="#8fa476" stroke-width="5"/><path d="M160 22V128" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 6" stroke-linecap="round"/><g fill="none" stroke="#8fa476" stroke-width="5" stroke-linecap="round"><path d="M128 54q11-7 22 0"/><path d="M134 100q14 6 26 4"/></g><circle cx="139" cy="70" r="5.5" fill="#8fa476"/><g fill="none" stroke="#e2ab47" stroke-width="5" stroke-linecap="round"><path d="M170 60q11-3 22 4"/><path d="M160 104q14 2 24 8"/><path d="M174 76h14"/></g><path d="M236 52l12 8-12 8M84 52l-12 8 12 8" fill="none" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
C_FACE = KC("yuz-felci.html", TH_FACE, "Hastalık rehberi", "Yüz felci (Bell felci)", "İlk 72 saatte ne yapılmalı, göz nasıl korunur, yüz neden zorlanmamalı? Egzersize ne zaman başlanır, akupunktur ve elektrik tedavisi için kanıt, altı güvenli uygulama.")
TH_GTPS = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="160" cy="26" r="13" fill="#8fa476"/><path d="M138 50h44M160 44v48M160 92l-14 50M160 92l14 50M138 50l-8 40M182 50l8 40" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><circle cx="174" cy="94" r="14" fill="rgba(226,171,71,.18)" stroke="#e2ab47" stroke-width="3"/><circle cx="174" cy="94" r="4.5" fill="#e2ab47"/><path d="M198 82l12-6M202 96h14M198 110l12 6" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_GTPS = KC("kalca-yan-agrisi.html", TH_GTPS, "Hastalık rehberi", "Kalça yan ağrısı", "Bursit denen ağrıda iğne mi, egzersiz mi? 204 kişilik çalışmanın sonucu, kalçayı rahatlatan alışkanlıklar, yatış pozisyonu ve evde altı egzersiz.")
TH_LYMPH = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M70 112Q150 104 244 54" fill="none" stroke="#8fa476" stroke-width="26" stroke-linecap="round"/><path d="M96 110Q150 102 214 70" fill="none" stroke="#e2ab47" stroke-width="26" stroke-dasharray="3 9" opacity=".8"/><circle cx="258" cy="46" r="15" fill="#8fa476"/><g fill="#ece5cf" opacity=".85"><circle cx="118" cy="72" r="4"/><circle cx="150" cy="60" r="4"/><circle cx="182" cy="44" r="4"/></g><path d="M206 30l14-8M212 34l8-12 2 14" fill="none" stroke="#ece5cf" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" opacity=".85"/></svg>"""
C_LYMPH = KC("lenfodem.html", TH_LYMPH, "Rehabilitasyon rehberi", "Lenfödem", "Kanser tedavisinden sonra kol ya da bacak şişliği: egzersiz şişliği artırır mı, cilt nasıl korunur, bası ve lenf drenajı ne işe yarar? Kol için altı hareket.")
TH_DQ = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M150 148V104" stroke="#8fa476" stroke-width="30" stroke-linecap="round"/><rect x="130" y="52" width="56" height="62" rx="16" fill="#8fa476"/><g stroke="#8fa476" stroke-width="12" stroke-linecap="round"><path d="M138 54V24M152 54V16M166 54V18M180 54V28"/></g><path d="M134 98L112 78L104 58" fill="none" stroke="#e2ab47" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/><circle cx="128" cy="106" r="15" fill="none" stroke="#e2ab47" stroke-width="3" stroke-dasharray="4 5"/><path d="M96 112l-10 4M100 124l-8 8M112 130l-2 10" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_DQ = KC("de-quervain.html", TH_DQ, "Hastalık rehberi", "De Quervain (bilek ağrısı)", "Başparmak tarafındaki bilek ağrısı yeni annelerde neden sık? Atel ne kadar takılır, kortizon iğnesi işe yarar mı? Aşamalı altı egzersiz.")
TH_DN = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M108 24v62q0 22 22 26l62 10q26 4 30-10 4-16-18-20l-40-10V24z" fill="rgba(143,164,118,.22)" stroke="#8fa476" stroke-width="5" stroke-linejoin="round"/><path d="M132 30v52q0 12 14 16l52 12" fill="none" stroke="#e2ab47" stroke-width="3" stroke-dasharray="5 6" stroke-linecap="round"/><g stroke="#e2ab47" stroke-width="3" stroke-linecap="round"><path d="M228 86l12-8M234 100h14M228 114l12 6"/></g><g fill="#e2ab47"><circle cx="150" cy="100" r="3.5"/><circle cx="176" cy="106" r="3.5"/><circle cx="200" cy="110" r="3.5"/></g></svg>"""
C_DN = KC("diyabetik-noropati.html", TH_DN, "Hastalık rehberi", "Diyabetik nöropati", "Diyabette ayaklar neden uyuşur ve yanar? Tedavinin üç hedefi, her gün ayak bakımı ve denge için altı egzersiz.")
TH_FLAT = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M40 120H280" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M84 30v62q0 16 16 20l88 6q22 0 22-8t-20-12l-58-18V30z" fill="rgba(143,164,118,.22)" stroke="#8fa476" stroke-width="5" stroke-linejoin="round"/><path d="M100 118Q140 96 186 118" fill="none" stroke="#e2ab47" stroke-width="4" stroke-dasharray="5 6" stroke-linecap="round"/><path d="M142 96V78M135 85l7-7 7 7" fill="none" stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
C_FLAT = KC("duztabanlik.html", TH_FLAT, "Hastalık rehberi", "Düztabanlık", "Tedavi gerekir mi, çocuklarda tabanlık işe yarar mı, kavis sonradan neden düşer? Ne zaman hekime görünmeli ve evde altı egzersiz.")
TH_SCI = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="150" cy="100" r="34" fill="none" stroke="#8fa476" stroke-width="5"/><circle cx="150" cy="100" r="4" fill="#8fa476"/><path d="M150 100l20-24M150 100l-28-14M150 100l8 32" stroke="rgba(143,164,118,.5)" stroke-width="2.5" stroke-linecap="round"/><circle cx="162" cy="26" r="12" fill="#8fa476"/><path d="M160 42v38h40l14 40" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M160 54l26 14" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/><path d="M146 44v34" stroke="#e2ab47" stroke-width="4" stroke-dasharray="3 6" stroke-linecap="round"/><circle cx="146" cy="62" r="6" fill="none" stroke="#e2ab47" stroke-width="3"/><path d="M206 124h20" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/></svg>"""
C_SCI = KC("omurilik-yaralanmasi.html", TH_SCI, "Rehabilitasyon rehberi", "Omurilik yaralanması", "Rehabilitasyon neleri kapsar? Bası yarasını önleme, basınç azaltma teknikleri, egzersiz kılavuzu, otonom disrefleksi ve altı uygulama.")
TH_HV = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M132 140V70q0-30 26-34l10-2q14 0 16 16l4 90z" fill="rgba(143,164,118,.22)" stroke="#8fa476" stroke-width="5" stroke-linejoin="round"/><path d="M132 78q-18-6-14-26 4-18 22-20" fill="none" stroke="#e2ab47" stroke-width="5" stroke-linecap="round"/><path d="M140 34q14-22 30-22" fill="none" stroke="#e2ab47" stroke-width="10" stroke-linecap="round"/><g stroke="#8fa476" stroke-width="8" stroke-linecap="round"><path d="M178 34V18M190 40V26M200 50V38"/></g><path d="M100 70l-14-4M98 56l-12-10" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_HV = KC("halluks-valgus.html", TH_HV, "Hastalık rehberi", "Halluks valgus", "Ayak başparmağı çıkıntısı egzersizle düzelir mi? Ayakkabı seçimi, ağrıyı azaltan önlemler, ameliyat için kanıt ve ayağı rahatlatan altı hareket.")
TH_TF = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M158 148V112" stroke="#8fa476" stroke-width="30" stroke-linecap="round"/><rect x="132" y="58" width="56" height="62" rx="16" fill="#8fa476"/><g stroke="#8fa476" stroke-width="12" stroke-linecap="round" fill="none"><path d="M140 60V30M168 60V24M182 60V34"/><path d="M136 104L114 84L108 64"/></g><path d="M154 60V44q0-12 12-10" fill="none" stroke="#e2ab47" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/><circle cx="154" cy="62" r="13" fill="none" stroke="#e2ab47" stroke-width="3" stroke-dasharray="4 5"/><path d="M206 40l12-8M210 54h14" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_TF = KC("tetik-parmak.html", TH_TF, "Hastalık rehberi", "Tetik parmak", "Parmak neden takılır, kendiliğinden geçer mi? Gece ateli, kortizon iğnesi için kanıt, ameliyat ve evde altı uygulama.")
TH_GOLF = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M70 40L156 78L246 44" fill="none" stroke="#8fa476" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/><circle cx="156" cy="92" r="15" fill="rgba(226,171,71,.18)" stroke="#e2ab47" stroke-width="3"/><circle cx="156" cy="92" r="5" fill="#e2ab47"/><path d="M130 118l-10 8M156 124v12M182 118l10 8" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/><circle cx="262" cy="36" r="13" fill="#8fa476"/></svg>"""
C_GOLF = KC("golfcu-dirsegi.html", TH_GOLF, "Hastalık rehberi", "Golfçü dirseği", "Dirseğin iç yanındaki ağrı: tenisçi dirseğinden farkı, yükü azaltma, dirsek bandı, iğne ve evde altı egzersiz.")
TH_GBS = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M40 75H112" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/><g fill="rgba(143,164,118,.3)" stroke="#8fa476" stroke-width="4"><rect x="112" y="60" width="34" height="30" rx="13"/><rect x="198" y="60" width="34" height="30" rx="13"/></g><rect x="155" y="60" width="34" height="30" rx="13" fill="none" stroke="#e2ab47" stroke-width="4" stroke-dasharray="5 6"/><path d="M232 75H280" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-dasharray="2 12"/><path d="M60 44l16 12-8 4 14 10" fill="none" stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M162 112q10 12 20 0" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_GBS = KC("guillain-barre.html", TH_GBS, "Rehabilitasyon rehberi", "Guillain-Barré sendromu", "Hastane tedavisi, iyileşme süresi, rehabilitasyonun bileşenleri, egzersiz için kanıt ve iyileşme dönemi için altı egzersiz.")
TH_SARC = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M110 82H210" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/><rect x="84" y="52" width="26" height="60" rx="8" fill="#8fa476"/><rect x="210" y="52" width="26" height="60" rx="8" fill="#8fa476"/><rect x="66" y="62" width="16" height="40" rx="6" fill="rgba(143,164,118,.5)"/><rect x="238" y="62" width="16" height="40" rx="6" fill="rgba(143,164,118,.5)"/><path d="M160 60V26M146 40l14-14 14 14" fill="none" stroke="#e2ab47" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><path d="M126 132h68" stroke="#e2ab47" stroke-width="3" stroke-dasharray="4 7" stroke-linecap="round"/></svg>"""
C_SARC = KC("sarkopeni.html", TH_SARC, "Hastalık rehberi", "Sarkopeni: yaşa bağlı kas kaybı", "Beş soruluk tarama, tanı testleri, dirençli egzersiz için kanıt, protein önerileri ve evde altı güçlendirme egzersizi.")
TH_DEM = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="132" cy="36" r="13" fill="#8fa476"/><path d="M132 52v46M132 98l-12 32M132 98l12 32M132 66l28 12" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><circle cx="190" cy="42" r="12" fill="rgba(143,164,118,.55)"/><path d="M190 57v42M190 99l-11 31M190 99l11 31M190 70l-30 8" fill="none" stroke="rgba(143,164,118,.55)" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><circle cx="160" cy="78" r="6" fill="#e2ab47"/><path d="M62 138h196" stroke="#e2ab47" stroke-width="3" stroke-dasharray="4 8" stroke-linecap="round"/></svg>"""
C_DEM = KC("demans-egzersiz.html", TH_DEM, "Rehabilitasyon rehberi", "Demansta egzersiz", "Egzersiz neye yarar, neye yaramaz? Uygun etkinlikler, bakım verenler için ipuçları, güvenlik ve birlikte yapılabilecek altı hareket.")
C_FIBRO = KC("fibromiyalji.html", TH_FIBRO, "Hastalık rehberi", "Fibromiyalji", "Yaygın ağrı ve yorgunluk neden olur? Güçlü öneri alan tek tedavi egzersiz: az ve yavaş başlayan altı hareket.")
C_VERTIGO = KC("bas-donmesi.html", TH_VERTIGO, "Hastalık rehberi", "Baş dönmesi (BPPV)", "Yatarken ve dönerken başlayan kısa süreli baş dönmesi: Epley manevrası adım adım ve acil uyarı işaretleri.")
C_AS = KC("ankilozan-spondilit.html", TH_AS, "Hastalık rehberi", "Ankilozan spondilit", "Dinlenmekle artan, hareketle azalan bel ağrısı: iltihaplı bel ağrısını tanıyın; evde altı duruş ve esneklik egzersizi.")
TH_PFP = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M116 14 L164 72 L148 136" stroke="#8fa476" stroke-width="12" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M148 138 H184" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/><ellipse cx="175" cy="66" rx="7" ry="12" fill="#d8b25e" transform="rotate(-28 175 66)"/><circle cx="170" cy="70" r="27" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M210 60h12M208 76l11 5M206 46l10-6" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
TH_ACHILLES = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M156 6 V96" stroke="#8fa476" stroke-width="12" stroke-linecap="round"/><path d="M148 18 Q128 48 142 84" stroke="#8fa476" stroke-width="11" fill="none" stroke-linecap="round"/><path d="M142 96 L204 108 Q214 112 208 120 L144 120 Q130 120 132 106 Z" fill="#8fa476"/><path d="M142 72 L136 106" stroke="#d8b25e" stroke-width="6" stroke-linecap="round"/><circle cx="138" cy="92" r="20" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M104 82h-12M106 98l-11 5M108 68l-10-6" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/><path d="M120 140 H220" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/></svg>"""
TH_HEADACHE = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="160" cy="56" r="32" fill="#8fa476"/><path d="M152 88 V108 M168 88 V108 M112 130 Q160 104 208 130" stroke="#8fa476" stroke-width="8" fill="none" stroke-linecap="round"/><path d="M127 50 Q160 36 193 50" stroke="#d8b25e" stroke-width="7" fill="none" stroke-linecap="round"/><circle cx="160" cy="100" r="15" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M116 36l-10-6M112 52h-12M116 68l-10 6M204 36l10-6M208 52h12M204 68l10 6" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
TH_SCOLIOSIS = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="161" cy="15" r="10" fill="#8fa476"/><path d="M161 25 V32" stroke="#8fa476" stroke-width="6" stroke-linecap="round"/><path d="M124 42 L198 32 Q204 60 191 84 Q185 100 189 116 H133 Q137 100 130 84 Q118 62 124 42 Z" fill="rgba(143,164,118,.22)" stroke="#8fa476" stroke-width="4" stroke-linejoin="round"/><path d="M124 42 L112 88 M198 32 L210 80 M148 116 L144 146 M176 116 L180 146" stroke="#8fa476" stroke-width="7" stroke-linecap="round" fill="none"/><path d="M161 34 V116" stroke="#ece5cf" stroke-width="2" stroke-dasharray="3 5" opacity=".45"/><g fill="#d8b25e"><circle cx="161" cy="42" r="4.5"/><circle cx="168" cy="52" r="4.5"/><circle cx="172" cy="62" r="4.5"/><circle cx="171" cy="72" r="4.5"/><circle cx="165" cy="82" r="4.5"/><circle cx="157" cy="92" r="4.5"/><circle cx="153" cy="102" r="4.5"/><circle cx="156" cy="112" r="4.5"/></g><path d="M224 30v-10M228 44h10M96 52h-10M100 38l-8-6" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_PFP = KC("diz-onu-agrisi.html", TH_PFP, "Hastalık rehberi", "Diz önü ağrısı", "Merdiven inerken ve çömelirken diz kapağı çevresinde ağrı: neden olur, hangi egzersizler işe yarar? Evde altı egzersiz ve videolar.")
C_ACHILLES = KC("asil-tendinopatisi.html", TH_ACHILLES, "Hastalık rehberi", "Aşil tendinopatisi", "Topuğun üstünde ağrı ve sabah tutukluğu: kirişi iyileştiren yüklenme egzersizleri ve basamaktan topuk indirme programı.")
C_HEADACHE = KC("bas-agrisi.html", TH_HEADACHE, "Hastalık rehberi", "Baş ağrısı", "Gerilim tipi ve boyun kaynaklı baş ağrısında egzersizin etkisi, ağrı kesici uyarıları ve acil başvuru gerektiren belirtiler.")
C_SCOLIOSIS = KC("skolyoz.html", TH_SCOLIOSIS, "Hastalık rehberi", "Skolyoz", "Evde nasıl fark edilir, ne zaman egzersiz, korse ya da ameliyat gerekir? Uluslararası kılavuz önerileri ve evde kontrol testi.")
C_BACK = KC("bel-agrisi.html", TH_BACK, "Hastalık rehberi", "Bel ağrısı", "MR'daki aşınma ne anlama gelir, yatak istirahati gerekir mi? Evde altı egzersiz ve günlük hayat önerileri.")
C_SCIATICA = KC("bel-fitigi.html", TH_SCIATICA, "Hastalık rehberi", "Bel fıtığı ve siyatik", "Bacağa vuran ağrı, fıtık kendiliğinden geçer mi, ameliyat ne zaman gerekir?")
C_KNEE = KC("diz-kireclenmesi.html", TH_KNEE, "Hastalık rehberi", "Diz kireçlenmesi", "Röntgen ne anlatır, kilo ve egzersiz neden önemli? Evde altı egzersiz ve merdiven, baston önerileri.")
C_NECK = KC("boyun-agrisi.html", TH_NECK, "Hastalık rehberi", "Boyun ağrısı", "Neden olur, boyun düzleşmesi önemli mi? Evde altı egzersiz ve masa başı önerileri.")
C_HERNIA = KC("boyun-fitigi.html", TH_NERVE, "Hastalık rehberi", "Boyun fıtığı ve sinir sıkışması", "Kola vuran ağrı, hangi sinir nereye vurur, MR ne anlatır, ne zaman ameliyat gerekir?")
C_SHOULDER = KC("donuk-omuz.html", TH_SHOULDER, "Hastalık rehberi", "Donuk omuz", "Nedir, evreleri nelerdir, nasıl tedavi edilir? Evde yapılabilecek egzersizler.")
C_STRES = KC("stres.html", TH_BREATH, "Kendine iyi bak", "Stresli anlarda ne yapabilirsiniz?", "Nefes egzersizleri, DSÖ rehberinden beş beceri, Türkçe kitapçık ve ses kayıtları.")
C_NEWS = KC("yenilikler.html", TH_DNA, "Bilim gündemi", "Geleceğin tıbbı, bugün", "Alzheimer'ı kandan tanıyan testler, domuz böbreği nakli, mamografide yapay zekâ, gen tedavileri ve rehabilitasyonda yeni bulgular.")
C_IDEA = KC("https://wa.me/905538815568?text=" + quote("Merhaba, Bilgi köşesi için bir konu önermek istiyorum."), TH_IDEA, "Sizden gelsin", "Hangi konuyu merak ediyorsunuz?", "Bilgi köşesinde okumak istediğiniz bir konu varsa önerinizi WhatsApp'tan iletebilirsiniz.", go="Konu öner →", ext_link=True)

TH_RC = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="160" cy="24" r="12" fill="#8fa476"/><path d="M130 54 H190 M160 36 V110 M160 110 L148 146 M160 110 L172 146 M190 54 L198 98" stroke="#8fa476" stroke-width="7" stroke-linecap="round" fill="none"/><path d="M130 54 L120 98" stroke="#d8b25e" stroke-width="8" stroke-linecap="round"/><path d="M112 50 A20 20 0 0 1 132 36" stroke="#e2ab47" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M140 38 A20 20 0 0 1 150 54" stroke="#e2ab47" stroke-width="5" fill="none" stroke-linecap="round"/><circle cx="130" cy="54" r="24" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M94 46h-12M96 62l-11 5M98 30l-10-6" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
TH_TMJ = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M136 94 Q112 68 126 42 Q142 18 172 22 Q198 28 200 54 L208 68 L199 71 L199 80" stroke="#8fa476" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M152 82 L158 104 Q164 112 188 106 L199 92" stroke="#d8b25e" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M142 110 L140 146 M168 114 L172 146" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/><circle cx="151" cy="76" r="5" fill="#e2ab47"/><circle cx="151" cy="76" r="18" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M122 70h-12M124 86l-11 5M126 56l-10-6" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
TH_UI = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M104 30 Q98 86 136 104 M216 30 Q222 86 184 104" stroke="#8fa476" stroke-width="8" fill="none" stroke-linecap="round"/><ellipse cx="160" cy="80" rx="18" ry="14" fill="#8fa476" opacity=".55"/><path d="M132 104 Q160 128 188 104" stroke="#d8b25e" stroke-width="6" fill="none" stroke-linecap="round"/><ellipse cx="160" cy="110" rx="44" ry="22" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M160 146 V130 M154 136 L160 130 L166 136" stroke="#e2ab47" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M234 70h12M232 86l11 5M86 70h-12M88 86l-11 5" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
TH_PREG = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="152" cy="20" r="12" fill="#8fa476"/><path d="M152 48 Q192 64 168 92 L150 88 Z" fill="#8fa476"/><path d="M152 34 Q146 60 150 88 L144 146 M150 88 L160 146" stroke="#8fa476" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M152 44 L136 60 L142 76" stroke="#8fa476" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M147 68 Q143 80 149 92" stroke="#e2ab47" stroke-width="6" fill="none" stroke-linecap="round"/><circle cx="146" cy="84" r="19" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M114 78h-12M116 94l-11 5M118 64l-10-6" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_RC = KC("rotator-manset-yirtigi.html", TH_RC, "Hastalık rehberi", "Rotator manşet yırtığı", "MR'daki omuz yırtığı ameliyat gerektirir mi? Fizyoterapinin etkisini gösteren çalışmalar ve evde altı omuz egzersizi.")
C_TMJ = KC("cene-eklemi.html", TH_TMJ, "Hastalık rehberi", "Çene eklemi rahatsızlıkları", "Çene ağrısı, klik sesi ve ağız açmada kısıtlılık: günlük öneriler ve evde altı çene ve boyun egzersizi.")
TH_LS = """<svg viewBox="0 0 320 150" aria-hidden="true"><g fill="#8fa476"><rect x="118" y="8" width="34" height="23" rx="5"/><rect x="118" y="36" width="34" height="23" rx="5"/><rect x="118" y="68" width="34" height="23" rx="5"/><rect x="118" y="96" width="34" height="23" rx="5"/><rect x="118" y="124" width="34" height="20" rx="5"/><rect x="178" y="12" width="22" height="15" rx="4"/><rect x="178" y="40" width="22" height="15" rx="4"/><rect x="178" y="72" width="22" height="15" rx="4"/><rect x="178" y="100" width="22" height="15" rx="4"/><rect x="178" y="127" width="22" height="14" rx="4"/></g><path d="M157 6 V46 Q157 54 162 60 V67 Q157 73 157 81 V146 H173 V81 Q173 73 168 67 V60 Q173 54 173 46 V6 Z" fill="#ece5cf" opacity=".5"/><ellipse cx="153" cy="63.5" rx="8" ry="5.5" fill="#e2ab47"/><ellipse cx="177" cy="63.5" rx="8" ry="7" fill="#d8b25e"/><circle cx="165" cy="63.5" r="24" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M84 63.5 H108 M100 56.5 L108 63.5 L100 70.5 M236 63.5 H212 M220 56.5 L212 63.5 L220 70.5" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
C_UI = KC("idrar-kacirma.html", TH_UI, "Hastalık rehberi", "İdrar kaçırma ve pelvik taban", "Öksürürken ya da gülerken idrar kaçırma: pelvik taban egzersizleri nasıl yapılır, ne kadar etkili?")
C_PREG = KC("gebelikte-bel-agrisi.html", TH_PREG, "Hastalık rehberi", "Gebelikte bel ve leğen ağrısı", "Gebelikte güvenli egzersizler, günlük hayat önerileri ve hemen başvurmanız gereken durumlar.")
C_LS = KC("dar-kanal.html", TH_LS, "Hastalık rehberi", "Dar kanal (spinal stenoz)", "Yürüyünce bacaklarda ağrı, oturunca rahatlama: MR'daki daralma ameliyat gerektirir mi? Evde altı egzersiz ve videolar.")
TH_SPL = """<svg viewBox="0 0 320 150" aria-hidden="true"><rect x="118" y="20" width="84" height="34" rx="9" fill="rgba(236,229,207,.10)" stroke="#8fa476" stroke-width="5"/><rect x="138" y="62" width="84" height="34" rx="9" fill="rgba(226,171,71,.18)" stroke="#e2ab47" stroke-width="5"/><rect x="118" y="104" width="84" height="34" rx="9" fill="rgba(236,229,207,.10)" stroke="#8fa476" stroke-width="5"/><path d="M234 79h22m-8-8 8 8-8 8" fill="none" stroke="#e2ab47" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
C_SPL = KC("bel-kaymasi.html", TH_SPL, "Hastalık rehberi", "Bel kayması (spondilolistezis)", "Omur neden kayar, dereceler ne anlatır, ameliyat ne zaman gerekir? Ameliyatsız tedavi ve beli destekleyen altı egzersiz.")
TH_RLS = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M248 30a20 20 0 1 0 16 30a16 16 0 1 1 -16 -30z" fill="#e2ab47"/><path d="M60 112 H150 L196 84 H230" fill="none" stroke="#8fa476" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/><path d="M60 128 H156 L200 118 H236" fill="none" stroke="#8fa476" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" opacity=".7"/><path d="M168 62q6-8 12 0t12 0M178 46q6-8 12 0t12 0" fill="none" stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round"/></svg>"""
C_RLS = KC("huzursuz-bacak.html", TH_RLS, "Hastalık rehberi", "Huzursuz bacak sendromu", "Akşamları bacakları hareket ettirme dürtüsü: demir neden önemli, 2024 kılavuzu neyi değiştirdi? Kendi yapabilecekleriniz ve altı egzersiz.")
TH_CX = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M160 10v24" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/><path d="M118 44c0 30 18 56 42 70c24-14 42-40 42-70" fill="rgba(236,229,207,.10)" stroke="#8fa476" stroke-width="5" stroke-linejoin="round"/><path d="M160 116v10m0 6v6" stroke="#e2ab47" stroke-width="7" stroke-linecap="round"/><circle cx="160" cy="132" r="16" fill="none" stroke="#e2ab47" stroke-width="2.5" stroke-dasharray="4 4"/><path d="M96 140h128" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/></svg>"""
C_CX = KC("kuyruk-sokumu-agrisi.html", TH_CX, "Hastalık rehberi", "Kuyruk sokumu ağrısı", "Oturunca artan ağrı neden olur, ne kadar sürer? Minder seçimi, fizyoterapi, şok dalga, iğne ve ameliyat için kanıt; evde altı hareket.")
TH_BD = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="150" cy="30" r="17" fill="none" stroke="#8fa476" stroke-width="5"/><path d="M152 50 C150 70 150 90 152 112" fill="none" stroke="rgba(236,229,207,.35)" stroke-width="5" stroke-dasharray="3 7" stroke-linecap="round"/><path d="M156 50 C168 70 168 92 156 112" fill="none" stroke="#e2ab47" stroke-width="5" stroke-linecap="round"/><g fill="#8fa476"><rect x="140" y="56" width="22" height="9" rx="3"/><rect x="140" y="72" width="22" height="9" rx="3"/><rect x="140" y="88" width="22" height="9" rx="3"/><rect x="140" y="104" width="22" height="9" rx="3"/></g><path d="M110 128h100" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/></svg>"""
C_BD = KC("boyun-duzlesmesi.html", TH_BD, "Hastalık rehberi", "Boyun düzleşmesi", "Röntgendeki düzleşme ağrının nedeni mi? Ağrısı olan ve olmayanları karşılaştıran çalışmalar, yastık ve boyunluk önerileri ve altı egzersiz.")
TH_FAI = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M116 64 A46 46 0 0 1 204 64" fill="none" stroke="#ece5cf" stroke-width="7" stroke-linecap="round" opacity=".55"/><circle cx="160" cy="74" r="30" fill="none" stroke="#8fa476" stroke-width="6"/><path d="M180 96 L206 124 V146 M152 104 L178 130 V146" fill="none" stroke="#8fa476" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="186" cy="92" r="7" fill="#d8b25e"/><path d="M200 50l12-9M206 64h14M194 40l5-13" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_FAI = KC("kalca-sikismasi.html", TH_FAI, "Hastalık rehberi", "Kalça sıkışması (FAI)", "Kasıkta hareketle artan ağrı neden olur? Fizyoterapi ile ameliyatı karşılaştıran 348 kişilik çalışma, zorlayan hareketler ve evde altı egzersiz.")
TH_JK = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M150 14 L156 70 L136 128 M136 128 h22" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><ellipse cx="166" cy="68" rx="9" ry="12" fill="none" stroke="#ece5cf" stroke-width="4" opacity=".7"/><path d="M164 82 L158 100" stroke="#d8b25e" stroke-width="6" stroke-linecap="round"/><circle cx="161" cy="91" r="17" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M196 40v-14M206 50l10-10M186 34l-4-12" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/><path d="M110 140h100" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/></svg>"""
C_JK = KC("atlet-dizi.html", TH_JK, "Hastalık rehberi", "Atlet dizi (patellar tendinopati)", "Diz kapağının altında, sıçrarken ve merdiven inerken artan ağrı. Kirişi aşama aşama yüke alıştıran program, ağrı sınırı ve evde altı egzersiz.")
TH_DI = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="150" cy="22" r="12" fill="#8fa476"/><path d="M150 36 V96 M150 96 L138 142 M150 96 L162 142 M150 46 H124 L116 86" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M174 42 A12 12 0 0 1 174 66" fill="none" stroke="#ece5cf" stroke-width="5" stroke-linecap="round" opacity=".6"/><circle cx="186" cy="62" r="8" fill="#d8b25e"/><path d="M186 70 L204 108" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/><path d="M200 44l10-8M206 58h13M196 32l3-12" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_DI = KC("omuz-cikigi.html", TH_DI, "Hastalık rehberi", "Omuz çıkığı", "Omuz çıktığında ne yapmalı, askı ne kadar takılır, omuz yeniden çıkar mı? Risk etkenleri, kaçınılacak pozisyon ve evde altı egzersiz.")
TH_PI = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M118 40 Q160 22 202 40 L196 78 Q160 92 124 78 Z" fill="none" stroke="#ece5cf" stroke-width="5" stroke-linejoin="round" opacity=".5"/><path d="M128 56 L190 66" stroke="#8fa476" stroke-width="12" stroke-linecap="round"/><path d="M160 44 C158 70 166 96 160 142" fill="none" stroke="#d8b25e" stroke-width="5" stroke-linecap="round"/><circle cx="161" cy="62" r="16" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M178 104l12 4M176 120l12 2M174 88l12 6" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_PI = KC("piriformis-sendromu.html", TH_PI, "Hastalık rehberi", "Piriformis sendromu", "Kalçada oturunca artan, bacağın arkasına yayılan ağrı. Tanı neden zor, siyatikten farkı ne? Öneriler ve evde altı egzersiz.")
TH_KY = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="128" cy="34" r="12" fill="none" stroke="rgba(236,229,207,.45)" stroke-width="4"/><path d="M134 48 Q150 70 140 100 L134 142" fill="none" stroke="rgba(236,229,207,.45)" stroke-width="5" stroke-linecap="round"/><path d="M178 66h22l-6-6M200 66l-6 6" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="232" cy="22" r="12" fill="#8fa476"/><path d="M232 38 C236 62 236 86 232 104 L230 142" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/><path d="M236 50 C244 64 244 80 236 94" fill="none" stroke="#d8b25e" stroke-width="3" stroke-dasharray="4 5"/></svg>"""
C_KY = KC("kambur-durus.html", TH_KY, "Hastalık rehberi", "Kambur duruş (kifoz)", "Kambur duruş ağrı yapar mı, egzersiz eğriliği değiştirir mi? Kifoz tipleri, çalışmaların sonuçları ve sırtı dikleştiren altı egzersiz.")
TH_BK = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M150 12 L156 70 L148 138" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M148 138 h20" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/><ellipse cx="140" cy="76" rx="13" ry="17" fill="rgba(216,178,94,.35)" stroke="#d8b25e" stroke-width="3"/><circle cx="140" cy="76" r="27" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M182 60l12-6M184 76h14M182 92l12 6" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_BK = KC("baker-kisti.html", TH_BK, "Hastalık rehberi", "Baker kisti", "Dizin arkasında şişlik neden olur, kendiliğinden geçer mi? Pıhtıyla karışan belirtiler, tedavi seçenekleri ve evde altı egzersiz.")
TH_UB = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M160 14 V138" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-dasharray="1 12"/><path d="M122 36 L146 40 L136 92 Z" fill="none" stroke="#8fa476" stroke-width="5" stroke-linejoin="round"/><path d="M198 36 L174 40 L184 92 Z" fill="none" stroke="#8fa476" stroke-width="5" stroke-linejoin="round"/><ellipse cx="160" cy="62" rx="11" ry="20" fill="rgba(216,178,94,.35)" stroke="#d8b25e" stroke-width="3"/><path d="M128 66l-10 0M192 66h10M160 32v-10" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_UB = KC("kurek-kemigi-arasi-agri.html", TH_UB, "Hastalık rehberi", "Kürek kemiği arası ağrı", "Kürek kemiklerinin arasında ağrı neden olur, ne zaman tehlikelidir? Uyarı işaretleri, iyi gelenler ve evde altı egzersiz.")
TH_LC = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M244 30a20 20 0 1 0 22 26 16 16 0 0 1-22-26z" fill="rgba(216,178,94,.35)" stroke="#d8b25e" stroke-width="3"/><path d="M130 14 C150 40 150 70 136 96 L132 132 H160" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M118 52 l14 8 -10 8 14 8 -10 8" fill="none" stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M166 50l10-6M168 66h12M166 82l10 6" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_LC = KC("gece-bacak-kramplari.html", TH_LC, "Hastalık rehberi", "Gece bacak krampları", "Gece baldırınızda kramp neden olur, nasıl önlenir? Kramp anında yapılacaklar, uyarı işaretleri ve evde altı hareket.")
TH_GG = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M70 92 H170 M70 112 H170" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/><path d="M170 92 C200 84 222 70 250 66 M170 112 C204 112 226 104 254 96 M250 66 L254 96" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><ellipse cx="176" cy="84" rx="15" ry="11" fill="rgba(216,178,94,.35)" stroke="#d8b25e" stroke-width="3"/><circle cx="176" cy="84" r="24" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M176 48v-12M152 58l-8-8M200 58l8-8" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_GG = KC("ganglion-kisti.html", TH_GG, "Hastalık rehberi", "Ganglion kisti", "El bileğinde şişlik neden olur, kendiliğinden geçer mi? Boşaltma ve ameliyat hakkında bilinenler, uyarı işaretleri ve altı egzersiz.")
TH_BT = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M110 138 C114 116 132 106 160 106 C188 106 206 116 210 138" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/><path d="M160 106 L166 78" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/><g transform="rotate(-18 166 78)"><circle cx="166" cy="52" r="24" fill="none" stroke="#8fa476" stroke-width="8"/></g><path d="M178 86 l8 6 -8 6 8 6" fill="none" stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><ellipse cx="176" cy="92" rx="14" ry="12" fill="rgba(216,178,94,.3)"/><path d="M214 40 Q230 52 222 70 M216 64 l6 6 6-6" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
C_BT = KC("boyun-tutulmasi.html", TH_BT, "Hastalık rehberi", "Boyun tutulması", "Sabah boynunuz tutulmuş, başınızı çeviremiyor musunuz? Ne kadar sürer, neler iyi gelir? Uyarı işaretleri ve evde altı egzersiz.")
TH_SS = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M150 12 L146 112 L170 136 H196" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M128 14 C118 50 122 90 136 112" fill="none" stroke="#8fa476" stroke-width="6" stroke-linecap="round" opacity=".6"/><path d="M150 40 L148 96" stroke="#d8b25e" stroke-width="5" stroke-linecap="round"/><path d="M152 40 l12 6 -10 8 12 6 -10 8 12 6 -10 8" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M206 60 h22 M206 76 h30 M206 92 h22" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" opacity=".7"/></svg>"""
C_SS = KC("kaval-kemigi-agrisi.html", TH_SS, "Hastalık rehberi", "Kaval kemiği ağrısı", "Koşarken bacağınızın önünde ağrı mı var? Ne kadar dinlenmeli, stres kırığından nasıl ayrılır? Koşuya dönüş ve evde altı egzersiz.")
TH_HS = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M112 34 L150 78 L130 126 H152" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M150 78 L196 52 L220 82 L246 82" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M118 46 C126 64 138 74 148 82" fill="none" stroke="#d8b25e" stroke-width="6" stroke-linecap="round"/><path d="M120 66 l-12 4 8 6 -12 4" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M70 60 h18 M64 76 h24 M70 92 h18" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" opacity=".7"/></svg>"""
C_HS = KC("arka-uyluk-zorlanmasi.html", TH_HS, "Hastalık rehberi", "Arka uyluk zorlanması", "Koşarken uyluğunuzun arkasında keskin ağrı mı oldu? İlk 72 saatte yapılacaklar, spora dönüş ve evde altı egzersiz.")
TH_SI = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M160 14 V60" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-dasharray="1 11"/><path d="M146 62 H174 L166 104 H154 Z" fill="none" stroke="#8fa476" stroke-width="5" stroke-linejoin="round"/><path d="M146 64 C120 50 96 58 92 82 C90 100 108 118 132 122 M174 64 C200 50 224 58 228 82 C230 100 212 118 188 122" fill="none" stroke="#8fa476" stroke-width="6" stroke-linecap="round"/><ellipse cx="144" cy="80" rx="8" ry="16" fill="rgba(216,178,94,.4)" stroke="#d8b25e" stroke-width="3"/><path d="M120 74l-12-4M120 88l-12 4" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_SI = KC("sakroiliak-eklem-agrisi.html", TH_SI, "Hastalık rehberi", "Sakroiliak eklem ağrısı", "Belin en altında, bir yanda saplanan ağrı bu eklemden mi geliyor? Belirtiler, tanının neden zor olduğu, tedavi seçenekleri ve evde altı egzersiz.")
TH_OS = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M150 12 L156 74 L150 138 H174" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><circle cx="164" cy="70" r="9" fill="none" stroke="#8fa476" stroke-width="4"/><path d="M162 80 L166 96" stroke="#8fa476" stroke-width="4" stroke-linecap="round"/><ellipse cx="166" cy="99" rx="8" ry="7" fill="rgba(216,178,94,.4)" stroke="#d8b25e" stroke-width="3"/><circle cx="166" cy="99" r="18" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M210 120 V40 M202 50 L210 40 L218 50" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
C_OS = KC("osgood-schlatter.html", TH_OS, "Hastalık rehberi", "Osgood-Schlatter", "Çocuğunuzun dizinin altındaki çıkıntı ağrıyor mu? Ne kadar sürer, spor bırakılmalı mı? Aktivite ayarı, kademeli dönüş ve evde altı egzersiz.")
TH_MN = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M70 110 C90 120 180 122 238 112 C258 108 262 92 246 86 C210 74 150 70 104 72 C80 74 64 96 70 110 Z" fill="none" stroke="#8fa476" stroke-width="7" stroke-linejoin="round"/><path d="M226 86 V62 M240 88 V66 M212 84 V60 M198 82 V62" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/><ellipse cx="205" cy="96" rx="9" ry="7" fill="rgba(216,178,94,.45)" stroke="#d8b25e" stroke-width="3"/><path d="M205 70 l-6 8 8 0 -6 8" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M190 108 l-10 6 M220 108 l10 6" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_MN = KC("morton-noromasi.html", TH_MN, "Hastalık rehberi", "Morton nöroması", "Ayak parmaklarınızın arasında yanma ya da ayakkabıda çakıl taşı hissi mi var? Hangi ayakkabılar iyi gelir, iğne ve ameliyat ne zaman gerekir?")
TH_WB = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 92 H160 M60 112 H160" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/><path d="M160 92 C190 84 214 72 244 70 M160 112 C196 114 220 104 250 98 M244 70 L250 98" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M146 84 l6 10 -6 10 6 10" fill="none" stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M196 46 a24 24 0 1 1 -8 30" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round"/><path d="M184 70 l4 8 8-3" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
C_WB = KC("el-bilegi-kirigi.html", TH_WB, "Hastalık rehberi", "El bileği kırığı sonrası", "Alçı çıktı ama bileğiniz tutuk ve zayıf mı? Neler beklenir, ne zaman normale döner? Uyarı işaretleri ve evde altı egzersiz.")
TH_JH = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M90 110 L150 74 L214 92" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><circle cx="150" cy="74" r="10" fill="rgba(216,178,94,.35)" stroke="#d8b25e" stroke-width="3"/><path d="M150 74 L214 50" stroke="#8fa476" stroke-width="5" stroke-linecap="round" stroke-dasharray="3 8" opacity=".7"/><path d="M196 46 Q216 66 206 92" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/><path d="M200 84 l6 8 7-7" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M96 56 c10-14 26-14 34 0 c8 14 24 14 34 0" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" opacity=".7"/></svg>"""
C_JH = KC("eklem-hipermobilitesi.html", TH_JH, "Hastalık rehberi", "Eklem hipermobilitesi", "Eklemleriniz çok esnek, ama sık ağrıyor ya da burkuluyor mu? Beighton puanı neyi gösterir, hangi egzersizler eklemleri korur?")
TH_HO = """<svg viewBox="0 0 320 150" aria-hidden="true"><rect x="122" y="80" width="72" height="56" rx="16" fill="none" stroke="#8fa476" stroke-width="7"/><path d="M134 80 V30 M152 80 V20 M170 80 V24 M188 82 V38 M124 112 L98 86" stroke="#8fa476" stroke-width="9" stroke-linecap="round"/><circle cx="152" cy="40" r="7" fill="rgba(216,178,94,.4)" stroke="#d8b25e" stroke-width="3"/><circle cx="170" cy="44" r="7" fill="rgba(216,178,94,.4)" stroke="#d8b25e" stroke-width="3"/><circle cx="134" cy="52" r="6" fill="rgba(216,178,94,.4)" stroke="#d8b25e" stroke-width="3"/><circle cx="114" cy="102" r="10" fill="none" stroke="#e2ab47" stroke-width="3" stroke-dasharray="3 4"/></svg>"""
C_HO = KC("el-kireclenmesi.html", TH_HO, "Hastalık rehberi", "El ve parmak kireçlenmesi", "Parmak eklemlerinizde sert boğumlar ve tutukluk mu var? Romatizmadan nasıl ayrılır, egzersiz işe yarar mı? Evde altı egzersiz.")
TH_WH = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M150 140 V96" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/><circle cx="160" cy="66" r="24" fill="none" stroke="#8fa476" stroke-width="7"/><path d="M120 50 A48 48 0 0 1 132 26 M108 72 A62 62 0 0 1 118 34" fill="none" stroke="#d8b25e" stroke-width="4" stroke-linecap="round"/><path d="M200 50 A48 48 0 0 0 188 26 M212 72 A62 62 0 0 0 202 34" fill="none" stroke="#d8b25e" stroke-width="4" stroke-linecap="round" opacity=".55"/><circle cx="150" cy="100" r="11" fill="rgba(226,171,71,.25)" stroke="#e2ab47" stroke-width="3"/></svg>"""
C_WH = KC("boyun-incinmesi.html", TH_WH, "Hastalık rehberi", "Boyun incinmesi (whiplash)", "Kaza ya da düşme sonrası boyun ağrısı mı? Ne kadar sürer, boyunluk gerekir mi, ne zaman hekime gitmeli? Evde altı egzersiz.")
TH_CF = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="150" cy="40" r="16" fill="none" stroke="#8fa476" stroke-width="7"/><path d="M118 140 V78 Q118 62 136 62 H170 Q186 62 190 78 L206 120" fill="none" stroke="#8fa476" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/><circle cx="180" cy="70" r="9" fill="rgba(226,171,71,.35)" stroke="#e2ab47" stroke-width="3"/><circle cx="186" cy="64" r="3" fill="#ece5cf"/><circle cx="176" cy="74" r="2.5" fill="#ece5cf"/><path d="M196 48 l8 -8 M204 58 l10 -2" stroke="#d8b25e" stroke-width="3" stroke-linecap="round"/></svg>"""
C_CF = KC("omuzda-kirec-birikmesi.html", TH_CF, "Hastalık rehberi", "Omuzda kireç birikmesi", "Omzunuzda birdenbire başlayan şiddetli ağrı ve röntgende kireç mi var? Kendiliğinden geçer mi, hangi tedaviler var? Evde altı egzersiz.")
TH_DR = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M126 30 Q112 80 126 130 M194 30 Q208 80 194 130" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/><path d="M142 36 V124 M178 36 V124" stroke="#8fa476" stroke-width="10" stroke-linecap="round" opacity=".55"/><path d="M150 80 H170 M150 80 l6 -5 M150 80 l6 5 M170 80 l-6 -5 M170 80 l-6 5" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" fill="none"/><circle cx="160" cy="98" r="4" fill="#d8b25e"/></svg>"""
C_DR = KC("karin-kasi-ayrilmasi.html", TH_DR, "Hastalık rehberi", "Doğum sonrası karın kası ayrılması", "Doğumdan sonra karnınızın ortasında kabarıklık mı var? Ne kadar sık, kendiliğinden kapanır mı, hangi egzersizler güvenli? Kendi kendine kontrol.")
TH_SV = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M130 20 V96 Q130 124 156 124 H214 Q226 124 226 112 Q226 104 214 102 L170 96 Q160 94 158 84 L156 20" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><circle cx="140" cy="114" r="12" fill="rgba(226,171,71,.3)" stroke="#e2ab47" stroke-width="3"/><path d="M112 70 V40 M112 40 l-6 8 M112 40 l6 8" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" fill="none"/></svg>"""
C_SV = KC("sever-hastaligi.html", TH_SV, "Hastalık rehberi", "Çocuklarda topuk ağrısı (Sever)", "Çocuğunuzun topuğu koşup zıpladıktan sonra mı ağrıyor? Ne kadar sürer, spor bırakılmalı mı, topukluk işe yarar mı? Evde üç egzersiz.")
TH_PD = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M128 14 L150 70 M150 70 L136 136" fill="none" stroke="#8fa476" stroke-width="9" stroke-linecap="round"/><ellipse cx="146" cy="70" rx="13" ry="16" fill="none" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-dasharray="5 5"/><ellipse cx="184" cy="68" rx="13" ry="16" fill="rgba(226,171,71,.3)" stroke="#e2ab47" stroke-width="4"/><path d="M162 70 H170 M166 64 l6 6 l-6 6" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" fill="none"/></svg>"""
C_PD = KC("diz-kapagi-cikigi.html", TH_PD, "Hastalık rehberi", "Diz kapağı çıkığı", "Diz kapağınız yerinden mi çıktı? İlk anda ne yapmalı, yeniden çıkar mı, spora ne zaman dönülür? Evde dört egzersiz.")
TH_CU = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M90 40 L160 96 L240 52" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M96 52 Q130 80 160 108 Q200 84 236 64" fill="none" stroke="#e2ab47" stroke-width="3" stroke-dasharray="6 5"/><circle cx="160" cy="104" r="11" fill="rgba(226,171,71,.3)" stroke="#e2ab47" stroke-width="3"/><path d="M250 46 l8 -6 M252 56 l10 -2" stroke="#d8b25e" stroke-width="3" stroke-linecap="round"/></svg>"""
C_CU = KC("kubital-tunel-sendromu.html", TH_CU, "Hastalık rehberi", "Kübital tünel sendromu", "Serçe ve yüzük parmağınız mı uyuşuyor? Dirsekte sinir sıkışması, gece ateli, ameliyat ne zaman gerekir? Evde iki egzersiz.")
TH_AR = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M150 14 V70 M150 92 V100 Q150 124 176 124 H226 Q238 124 238 112 Q238 104 226 102 L188 96" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M142 72 L158 76 M142 88 L158 92" stroke="#e2ab47" stroke-width="4" stroke-linecap="round"/><path d="M118 70 l-12 -6 M118 82 h-14 M118 94 l-12 6" stroke="#d8b25e" stroke-width="3" stroke-linecap="round"/></svg>"""
C_AR = KC("asil-tendonu-kopmasi.html", TH_AR, "Hastalık rehberi", "Aşil tendonu kopması", "Bacağın arkasında “çat” sesi ve ani ağrı mı? Ameliyat mı bot mu, iyileşme ne kadar sürer? Bot döneminde beş egzersiz.")
TH_SO = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="150" cy="62" r="30" fill="none" stroke="#8fa476" stroke-width="7"/><path d="M178 50 Q200 46 214 58 L248 120" fill="none" stroke="#8fa476" stroke-width="9" stroke-linecap="round"/><path d="M128 42 Q140 30 158 32" fill="none" stroke="#e2ab47" stroke-width="4" stroke-linecap="round" stroke-dasharray="4 5"/><path d="M96 40 l-12 -6 M94 56 h-14 M96 72 l-12 6" stroke="#d8b25e" stroke-width="3" stroke-linecap="round"/></svg>"""
C_SO = KC("omuz-kireclenmesi.html", TH_SO, "Hastalık rehberi", "Omuz kireçlenmesi", "Omzunuz ağrıyor, tutuk ve hareket ederken takılıyor mu? Kortizon iğnesi ve ameliyat ne zaman düşünülür? Evde dört egzersiz.")
TH_CZ = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M140 14 Q118 52 132 86 Q140 108 142 132 M176 14 Q192 50 180 86 Q172 108 170 132" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/><path d="M150 52 L160 62 L150 70 L162 80" fill="none" stroke="#e2ab47" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><path d="M206 50 l12 -6 M208 64 h14 M206 78 l12 6" stroke="#d8b25e" stroke-width="3" stroke-linecap="round"/></svg>"""
C_CZ = KC("baldir-kasi-zorlanmasi.html", TH_CZ, "Hastalık rehberi", "Baldır kası zorlanması", "Baldırınıza ani, keskin bir ağrı mı girdi? İlk 72 saatte ne yapmalı, ne zaman spora dönülür? Evde altı egzersiz.")
TH_AK = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M140 14 V92 Q140 120 166 120 H222 Q234 120 234 108 Q234 100 222 98 L182 92 Q170 90 170 80 V14" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M162 58 L172 64 L164 70 L174 76" fill="none" stroke="#e2ab47" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><rect x="122" y="40" width="70" height="62" rx="10" fill="none" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-dasharray="6 5"/></svg>"""
C_AK = KC("ayak-bilegi-kirigi.html", TH_AK, "Hastalık rehberi", "Ayak bileği kırığı sonrası", "Bot ne kadar kullanılır, şişlik ne zaman geçer, ne zaman araba kullanılır? İyileşmeyi hızlandıran öneriler ve evde altı egzersiz.")
TH_KL = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M70 60 Q120 40 156 54 M170 52 Q206 42 250 60" fill="none" stroke="#8fa476" stroke-width="10" stroke-linecap="round"/><path d="M156 46 L162 56 L156 62 L166 70" fill="none" stroke="#e2ab47" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><path d="M110 92 Q160 140 214 92" fill="none" stroke="rgba(236,229,207,.35)" stroke-width="6" stroke-linecap="round"/><circle cx="160" cy="30" r="12" fill="none" stroke="rgba(236,229,207,.3)" stroke-width="3"/></svg>"""
C_KL = KC("koprucuk-kemigi-kirigi.html", TH_KL, "Hastalık rehberi", "Köprücük kemiği kırığı", "Askı ne kadar takılır, iyileşme ne kadar sürer, spora ne zaman dönülür? İlk yardım, uyarı işaretleri ve evde altı egzersiz.")
TH_GRP = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M216 28 a26 26 0 1 0 22 40 a20 20 0 1 1 -22 -40 Z" fill="rgba(226,171,71,.3)" stroke="#e2ab47" stroke-width="3"/><path d="M126 20 Q118 70 128 130 M156 20 Q166 70 152 130" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/><path d="M108 64 l-12 -6 M108 78 h-14 M108 92 l-12 6" stroke="#d8b25e" stroke-width="3" stroke-linecap="round"/><circle cx="262" cy="98" r="3" fill="#ece5cf"/><circle cx="246" cy="118" r="2" fill="#ece5cf"/></svg>"""
C_GRP = KC("buyume-agrilari.html", TH_GRP, "Hastalık rehberi", "Çocuklarda büyüme ağrıları", "Çocuğunuz gece bacak ağrısıyla mı uyanıyor? Neden olur, ne iyi gelir, ne zaman hekime gidilmeli? Evde dört germe.")
TH_BFA = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M160 14 V136" stroke="rgba(236,229,207,.2)" stroke-width="18" stroke-linecap="round"/><g fill="#8fa476"><rect x="146" y="20" width="28" height="18" rx="5"/><rect x="146" y="44" width="28" height="18" rx="5"/><rect x="146" y="92" width="28" height="18" rx="5"/><rect x="146" y="116" width="28" height="18" rx="5"/></g><rect x="146" y="68" width="28" height="18" rx="5" fill="none" stroke="#e2ab47" stroke-width="3"/><path d="M200 78 h40 M226 66 l14 12 l-14 12" fill="none" stroke="#d8b25e" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><path d="M96 70 v18 M88 78 h16" stroke="#e2ab47" stroke-width="4" stroke-linecap="round"/></svg>"""
C_BFA = KC("bel-fitigi-ameliyati-sonrasi.html", TH_BFA, "Hastalık rehberi", "Bel fıtığı ameliyatı sonrası", "Mikrodiskektomiden sonra ne zaman yürünür, oturulur, işe ve spora dönülür? Uyarı işaretleri ve ilk haftalar için altı egzersiz.")
TH_KB = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M160 18 V132" stroke="rgba(236,229,207,.3)" stroke-width="8" stroke-linecap="round"/><g fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round"><path d="M156 34 C120 34 104 50 104 62"/><path d="M164 34 C200 34 216 50 216 62"/><path d="M156 58 C116 58 98 76 100 90"/><path d="M156 82 C120 82 106 98 110 112"/><path d="M164 82 C200 82 214 98 210 112"/></g><path d="M164 58 C204 58 222 76 220 90" fill="none" stroke="#e2ab47" stroke-width="7" stroke-linecap="round"/><path d="M196 54 l6 10 l-8 4 l6 10" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M244 40 c10 6 10 18 0 24 M256 34 c16 10 16 26 0 36" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" opacity=".8"/></svg>"""
C_KB = KC("kaburga-kirigi.html", TH_KB, "Hastalık rehberi", "Kaburga kırığı ve morarması", "Ağrı varken nasıl nefes alınır ve öksürülür, iyileşme ne kadar sürer? Aktif nefes döngüsü, dört egzersiz ve acil uyarı işaretleri.")
TH_KS = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="160" cy="18" r="12" fill="#8fa476"/><path d="M160 32 V76 M160 44 L140 66 M160 44 L182 64 M160 76 L150 140" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M160 76 L198 120 L214 118" stroke="#d8b25e" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M162 80 L174 96" stroke="#e2ab47" stroke-width="4" stroke-linecap="round"/><circle cx="166" cy="86" r="20" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><circle cx="236" cy="128" r="10" fill="none" stroke="rgba(236,229,207,.55)" stroke-width="3"/><path d="M110 140 H230" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/></svg>"""
C_KS = KC("kasik-zorlanmasi.html", TH_KS, "Hastalık rehberi", "Kasık zorlanması", "Kasıkta ve iç uylukta ağrı: ilk günlerde ne yapılmalı, ne zaman koşuya ve spora dönülür? Evde dört güçlendirme egzersizi.")
TH_MF = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M160 150 V108" stroke="#8fa476" stroke-width="16" stroke-linecap="round"/><rect x="138" y="66" width="44" height="46" rx="12" fill="#8fa476"/><path d="M144 66 V40 M166 66 V36 M177 68 V46" stroke="#8fa476" stroke-width="8" stroke-linecap="round" fill="none"/><path d="M155 66 V34 L166 22" stroke="#e2ab47" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"/><rect x="190" y="18" width="12" height="48" rx="6" fill="none" stroke="#d8b25e" stroke-width="3"/><path d="M196 74 v14 M190 82 l6 6 l6 -6" stroke="#d8b25e" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/><circle cx="158" cy="32" r="16" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/></svg>"""
C_MF = KC("cekic-parmak.html", TH_MF, "Hastalık rehberi", "Çekiç parmak (mallet finger)", "Parmak ucu düştü ve düzelmiyor mu? Atel ne kadar takılır, nasıl temizlenir? Atel dönemi ve sonrası için dört egzersiz.")
TH_ACJ = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="150" cy="22" r="13" fill="#8fa476"/><path d="M150 38 V96 M150 96 L140 146 M150 96 L162 146" stroke="#8fa476" stroke-width="7" stroke-linecap="round" fill="none"/><path d="M150 46 L192 44" stroke="#d8b25e" stroke-width="7" stroke-linecap="round"/><path d="M150 46 L116 50 L108 92 M192 44 L198 92" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="194" cy="42" r="8" fill="#e2ab47"/><circle cx="194" cy="42" r="20" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/><path d="M214 18 l8 -8 M222 34 h12 M206 12 v-10" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/></svg>"""
C_ACJ = KC("omuz-ucu-yaralanmasi.html", TH_ACJ, "Hastalık rehberi", "Omuz ucu (AC eklem) yaralanması", "Omzun üstüne düştükten sonra omuz ucunda ağrı ve tümsek: askı ne kadar takılır, ne zaman işe dönülür? Evde altı egzersiz.")
TH_MT5 = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M110 112 C110 70 128 40 160 34 C196 28 222 52 226 84 C228 104 214 118 196 118 L126 118 C116 118 110 116 110 112 Z" fill="rgba(143,164,118,.18)" stroke="#8fa476" stroke-width="5"/><g stroke="rgba(236,229,207,.45)" stroke-width="5" stroke-linecap="round"><path d="M150 100 L140 50"/><path d="M162 100 L160 46"/><path d="M174 100 L178 48"/><path d="M186 102 L196 54"/></g><path d="M196 104 L214 62" stroke="#d8b25e" stroke-width="6" stroke-linecap="round"/><path d="M200 92 l10 -4 l-6 -4 l10 -4" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><circle cx="206" cy="88" r="18" fill="none" stroke="#d8b25e" stroke-width="2.5" stroke-dasharray="4 5"/></svg>"""
C_MT5 = KC("besinci-metatars-kirigi.html", TH_MT5, "Hastalık rehberi", "Ayak dış kenarı (5. tarak kemiği) kırığı", "Bot ne zaman bırakılır, ne zaman yürünür, Jones kırığı neden farklıdır? Haftalara göre iyileşme ve altı egzersiz.")
TH_TOR = """<svg viewBox="0 0 320 150" aria-hidden="true"><rect x="140" y="64" width="40" height="60" rx="18" fill="#8fa476"/><path d="M146 80 L126 96 M174 80 L194 96 M152 120 L148 142 M168 120 L172 142" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/><g transform="rotate(-20 160 62)"><circle cx="160" cy="42" r="20" fill="#8fa476"/></g><path d="M160 62 L172 66" stroke="#e2ab47" stroke-width="5" stroke-linecap="round"/><path d="M116 22 A40 40 0 0 0 118 62" fill="none" stroke="#d8b25e" stroke-width="3" stroke-dasharray="4 5" stroke-linecap="round"/><circle cx="236" cy="56" r="10" fill="#d8b25e"/><path d="M236 66 V84" stroke="#d8b25e" stroke-width="3"/></svg>"""
C_TOR = KC("bebeklerde-tortikolis.html", TH_TOR, "Hastalık rehberi", "Bebeklerde tortikolis", "Bebeğinizin başı hep bir yana mı eğik? Doğumsal kas tortikolisi, günlük taşıma ve oyun önerileri, fizyoterapistin gösterdiği germeler.")
TH_GLP = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M50 136 H270" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><rect x="62" y="56" width="70" height="20" rx="10" fill="none" stroke="#d8b25e" stroke-width="4" transform="rotate(-30 97 66)"/><path d="M84 76 L110 58" stroke="#d8b25e" stroke-width="4"/><circle cx="206" cy="28" r="10" fill="#8fa476"/><path d="M206 40 V82 M206 82 L194 106 L194 134 M206 82 L218 106 L218 134 M206 52 L180 52 M206 52 L232 52" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M168 44 V60 M244 44 V60" stroke="#e2ab47" stroke-width="8" stroke-linecap="round"/></svg>"""
C_GLP = KC("zayiflama-ilaci-ve-kas.html", TH_GLP, "Rehabilitasyon rehberi", "Zayıflama ilacı kullanırken kaslarınızı koruyun", "Semaglutid ve tirzepatid gibi ilaçlarla kilo verirken kas kaybını sınırlamak: güç egzersizi, protein ve evde altı egzersiz.")
TH_LCOV = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M50 136 H270" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M70 100 H150 M80 100 V136 M140 100 V136" stroke="#8a6a44" stroke-width="6" stroke-linecap="round" fill="none"/><circle cx="112" cy="40" r="10" fill="#8fa476"/><path d="M112 52 L114 96 M114 96 L94 98 L92 134 M112 62 L98 82 L104 96" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M176 52 C190 46 200 58 214 52 C228 46 236 56 248 52 M176 74 C190 68 200 80 214 74 C228 68 236 78 248 74" fill="none" stroke="#d8b25e" stroke-width="3.5" stroke-linecap="round"/><path d="M184 104 H202 L208 94 L216 114 L222 104 H246" fill="none" stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
C_LCOV = KC("uzun-covid.html", TH_LCOV, "Rehabilitasyon rehberi", "Uzun COVID'de hareket ve nefes", "COVID-19 sonrası aylarca süren yorgunluk ve nefes darlığında güvenli hareket: egzersiz sonrası alevlenme, enerji planlaması ve hafif ev hareketleri.")
TH_ITB = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M40 136 H280" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><circle cx="118" cy="26" r="10" fill="#8fa476"/><path d="M118 38 L112 78 L132 100 L120 132 M112 78 L92 96 L72 104 M116 48 L134 64 M116 48 L98 60" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M124 64 C130 76 134 88 132 100" fill="none" stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round"/><circle cx="131" cy="99" r="7" fill="none" stroke="#e2ab47" stroke-width="3"/><path d="M196 56 C210 70 210 92 196 106 M214 46 C236 68 236 96 214 116" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" opacity=".7"/><path d="M246 120 L270 96" stroke="rgba(236,229,207,.35)" stroke-width="3" stroke-linecap="round" stroke-dasharray="4 6"/></svg>"""
C_ITB = KC("kosucu-dizi.html", TH_ITB, "Hastalık rehberi", "Koşucu dizi (iliotibial bant sendromu)", "Koşarken dizin dış yanında başlayan ağrı: neden olur, ne işe yarar, kalça güçlendirme egzersizleri ve koşuya güvenli dönüş.")
TH_HT = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M50 136 H270" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M66 20 V136" stroke="rgba(236,229,207,.45)" stroke-width="5" stroke-linecap="round"/><circle cx="84" cy="38" r="10" fill="#8fa476"/><path d="M80 50 V92 L118 92 L118 134 M80 62 L104 80" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><circle cx="216" cy="70" r="42" fill="none" stroke="#d8b25e" stroke-width="5"/><path d="M186 92 L192 88 M216 34 V40 M246 92 L240 88 M184 58 L190 60 M248 58 L242 60" stroke="#ece5cf" stroke-width="3" stroke-linecap="round" opacity=".7"/><path d="M216 70 L240 50" stroke="#e2ab47" stroke-width="4.5" stroke-linecap="round"/><circle cx="216" cy="70" r="5" fill="#ece5cf"/></svg>"""
C_HT = KC("yuksek-tansiyon.html", TH_HT, "Rehabilitasyon rehberi", "Yüksek tansiyonda egzersiz", "Düzenli egzersiz tansiyonu birkaç puan düşürür: yürüyüş, güç çalışması ve izometrik duvar oturuşu, evde doğru ölçüm ve dikkat edilecekler.")
TH_ICU = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M40 136 H280" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M60 98 H196 M60 98 V136 M196 98 V136 M60 78 V98" fill="none" stroke="#8a6a44" stroke-width="6" stroke-linecap="round"/><rect x="66" y="84" width="42" height="11" rx="5" fill="rgba(236,229,207,.35)"/><circle cx="168" cy="36" r="10" fill="#8fa476"/><path d="M168 48 L170 90 M170 90 L200 92 L202 134 M168 58 L184 80 L188 94" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><rect x="220" y="22" width="68" height="46" rx="7" fill="none" stroke="rgba(236,229,207,.45)" stroke-width="3"/><path d="M226 46 H240 L247 34 L255 58 L262 46 H282" fill="none" stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
C_ICU = KC("yogun-bakim-sonrasi.html", TH_ICU, "Rehabilitasyon rehberi", "Yoğun bakımdan sonra iyileşme", "Yoğun bakımdan sonra güçsüzlük, yorgunluk ve unutkanlık sık görülür: ilk haftalarda neler beklenir, nasıl güçlenilir, hangi destekler var.")
TH_DIA = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 136 H260" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><circle cx="112" cy="30" r="11" fill="#8fa476"/><path d="M112 44 L108 84 L94 106 L90 132 M108 84 L124 104 L130 130 M110 54 L94 74 M110 54 L130 66" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M212 28 C200 46 184 64 184 84 C184 100 197 112 212 112 C227 112 240 100 240 84 C240 64 224 46 212 28 Z" fill="none" stroke="#d8b25e" stroke-width="5" stroke-linejoin="round"/><path d="M212 60 V94 M201 83 L212 94 L223 83" fill="none" stroke="#e2ab47" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M146 62 H170" stroke="rgba(236,229,207,.4)" stroke-width="3" stroke-linecap="round" stroke-dasharray="4 5"/></svg>"""
C_DIA = KC("diyabette-egzersiz.html", TH_DIA, "Rehabilitasyon rehberi", "Tip 2 diyabette egzersiz", "Kan şekeri kontrolü için yürüyüş ve güç çalışması: ne kadar, ne zaman, düşük şekerden ve ayak sorunlarından korunma, altı ev egzersizi.")
TH_VF = """<svg viewBox="0 0 320 150" aria-hidden="true"><g fill="#8fa476"><rect x="128" y="14" width="44" height="16" rx="5"/><rect x="126" y="36" width="48" height="17" rx="5"/><rect x="124" y="82" width="52" height="18" rx="5"/><rect x="122" y="106" width="56" height="19" rx="5"/></g><path d="M124 60 L176 60 L176 76 L124 72 Z" fill="#e2ab47"/><path d="M180 66 H198" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/><g fill="none" stroke="#d8b25e" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><circle cx="242" cy="40" r="10" fill="#d8b25e" stroke="none"/><path d="M240 54 V96 L232 132 M240 96 L250 132 M240 64 L224 82 M240 64 L258 80"/></g><path d="M214 40 V132" stroke="rgba(236,229,207,.35)" stroke-width="3" stroke-dasharray="5 6"/></svg>"""
C_VF = KC("omurga-kirigi.html", TH_VF, "Hastalık rehberi", "Kemik erimesine bağlı omurga kırığı", "Ani sırt ağrısı, boy kısalması? Kemik erimesine bağlı omurga kırığında tanı, ağrıyla başa çıkma, güvenli egzersizler ve uyarı işaretleri.")
TH_DUP = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M120 136 V96 C120 84 126 76 136 74 L196 70 C206 70 212 78 212 88 V136" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M140 74 V28 M160 72 V20 M180 71 V26" stroke="#8fa476" stroke-width="12" stroke-linecap="round"/><path d="M200 72 C206 58 212 54 220 60 C226 66 222 78 214 82" fill="none" stroke="#8fa476" stroke-width="12" stroke-linecap="round"/><path d="M206 120 C206 104 208 90 212 82" fill="none" stroke="#e2ab47" stroke-width="4" stroke-linecap="round"/><circle cx="208" cy="104" r="5" fill="#d8b25e"/><path d="M236 104 H282" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M240 100 C252 84 268 84 280 100" fill="none" stroke="#ece5cf" stroke-width="3" stroke-dasharray="4 5" stroke-linecap="round" opacity=".7"/></svg>"""
C_DUP = KC("dupuytren-kontrakturu.html", TH_DUP, "Hastalık rehberi", "Dupuytren kontraktürü", "Avuç içinde sertlik, parmak bükülüp düzelmiyor mu? Masa testi, tedavi seçenekleri, işlemden sonra el egzersizleri ve atel.")
TH_HF = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 136 H260" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><circle cx="104" cy="34" r="11" fill="#8fa476"/><path d="M104 48 L100 88 L86 110 L82 134 M100 88 L116 108 L122 132 M102 58 L88 78 M102 58 L120 72" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M214 112 C186 92 166 74 166 54 C166 40 176 30 190 30 C200 30 208 36 214 46 C220 36 228 30 238 30 C252 30 262 40 262 54 C262 74 242 92 214 112 Z" fill="none" stroke="#d8b25e" stroke-width="6" stroke-linejoin="round"/><path d="M174 70 H196 L204 54 L214 88 L224 62 L230 70 H254" fill="none" stroke="#e2ab47" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
C_HF = KC("kalp-yetmezligi.html", TH_HF, "Rehabilitasyon rehberi", "Kalp yetmezliğinde egzersiz", "Nefes darlığı ve yorgunluk varken egzersiz güvenli mi? Kimler başlayabilir, nasıl ilerlenir, her gün tartılmak ve altı ev egzersizi.")
TH_POP = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M104 36 C96 84 124 120 160 120 C196 120 224 84 216 36" fill="none" stroke="#8fa476" stroke-width="8" stroke-linecap="round"/><path d="M122 104 C140 116 180 116 198 104" fill="none" stroke="#d8b25e" stroke-width="6" stroke-linecap="round"/><ellipse cx="160" cy="80" rx="20" ry="16" fill="#e2ab47" opacity=".8"/><path d="M160 136 V126 M152 132 l8 -8 l8 8" fill="none" stroke="#ece5cf" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M236 52 c10 -12 24 -12 34 0 M240 62 c8 -8 18 -8 26 0" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" opacity=".6"/></svg>"""
C_POP = KC("pelvik-organ-sarkmasi.html", TH_POP, "Hastalık rehberi", "Pelvik organ sarkması (rahim sarkması)", "Haznede ağırlık ya da aşağı inme hissi mi var? Rahim, mesane ve bağırsak sarkması: pelvik taban egzersizleri, pesser ve günlük öneriler.")
TH_CONC = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M134 128 C120 128 112 116 112 100 V86 C98 84 96 76 104 70 L112 62 C112 34 136 18 162 18 C192 18 212 40 212 68 C212 92 200 104 192 112 V128" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M150 52 C158 44 172 44 178 54 C186 50 196 58 192 68 C198 74 192 86 182 84 C178 92 164 92 160 84 C150 88 140 80 146 70 C138 64 142 54 150 52 Z" fill="#d8b25e" opacity=".85"/><g fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"><path d="M226 40 l12 -8 M230 60 h14 M226 80 l12 8"/></g><path d="M234 126 h10 v-10 h10 v-10 h10 v-10" fill="none" stroke="#ece5cf" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" opacity=".7"/></svg>"""
C_CONC = KC("beyin-sarsintisi.html", TH_CONC, "Hastalık rehberi", "Beyin sarsıntısı (konküzyon)", "Kafa darbesinden sonra baş ağrısı, sersemlik, baş dönmesi? Acil belirtiler, ilk 48 saat ve okula, işe, spora altı aşamada kademeli dönüş.")
TH_PAD = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 136 H260" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><circle cx="118" cy="30" r="11" fill="#8fa476"/><path d="M118 44 L114 84 L98 108 L92 132 M114 84 L132 106 L144 130 M116 54 L100 74 M116 54 L136 66" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M134 108 C138 116 140 122 142 128" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/><path d="M196 42 C214 42 222 54 230 54 C238 54 246 42 264 42 M196 74 C214 74 222 62 230 62 C238 62 246 74 264 74" fill="none" stroke="#d8b25e" stroke-width="4" stroke-linecap="round"/><path d="M200 58 H222 M238 58 H260" stroke="rgba(181,72,58,.8)" stroke-width="4" stroke-linecap="round"/><path d="M206 104 V126 M218 104 V126" stroke="#ece5cf" stroke-width="5" stroke-linecap="round" opacity=".7"/></svg>"""
C_PAD = KC("periferik-arter-hastaligi.html", TH_PAD, "Rehabilitasyon rehberi", "Periferik arter hastalığı ve yürüyüş egzersizi", "Yürürken baldırda kramp gibi ağrı, birkaç dakika durunca geçiyor mu? Ağrıya kadar yürüyüp dinlenerek yürüme mesafenizi uzatan program ve uyarı işaretleri.")
TH_SRT = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M58 134 H262" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><circle cx="112" cy="72" r="12" fill="#8fa476"/><path d="M112 86 V116 M112 94 L94 106 L84 106 M112 94 L130 106 L140 106" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M110 118 L86 126 L118 132 M114 118 L138 126 L106 132" stroke="#d8b25e" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M144 66 Q176 24 200 46" stroke="#e2ab47" stroke-width="3" stroke-dasharray="6 6" stroke-linecap="round" fill="none"/><path d="M190 36 L201 47 L187 52" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/><g opacity=".6"><circle cx="226" cy="30" r="12" fill="#8fa476"/><path d="M226 44 V90 M226 90 L216 132 M226 90 L236 132 M226 56 L208 70 M226 56 L244 70" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/></g></svg>"""
TH_WALLSIT = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M104 8 V140" stroke="#ece5cf" stroke-width="6" stroke-linecap="round" opacity=".55"/><path d="M96 140 H200" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><circle cx="122" cy="34" r="12" fill="#8fa476"/><path d="M120 50 V94 M120 60 L140 76 L154 78" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M120 94 L166 96 L167 136 L180 137" stroke="#d8b25e" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="238" cy="80" r="30" fill="none" stroke="rgba(236,229,207,.18)" stroke-width="6"/><path d="M238 50 A30 30 0 1 1 208 80" fill="none" stroke="#e2ab47" stroke-width="6" stroke-linecap="round"/><path d="M238 80 V62 M230 40 H246" stroke="#e2ab47" stroke-width="4" stroke-linecap="round"/></svg>"""
TH_SIGH = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M52 122 H268" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M60 120 C78 118 92 72 110 60 L124 44 C160 44 214 98 262 118 L262 122 L60 122 Z" fill="rgba(226,171,71,.14)"/><path d="M60 120 C78 118 92 72 110 60 C116 56 118 48 124 44 C160 44 214 98 262 118" fill="none" stroke="#e2ab47" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="110" cy="60" r="6" fill="#8fa476"/><circle cx="124" cy="44" r="6" fill="#8fa476"/><path d="M150 30 H236" stroke="#8fa476" stroke-width="3" stroke-dasharray="2 7" stroke-linecap="round"/><path d="M228 24 L237 30 L228 36" stroke="#8fa476" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>"""
TH_NATURE = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="234" cy="40" r="16" fill="#e2ab47"/><path d="M234 14 V8 M260 40 H266 M252 22 L256 18 M216 22 L212 18" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/><path d="M104 140 V98 M156 140 V92" stroke="#ece5cf" stroke-width="6" stroke-linecap="round" opacity=".55"/><circle cx="104" cy="80" r="26" fill="#8fa476" opacity=".75"/><circle cx="156" cy="66" r="34" fill="#8fa476"/><path d="M60 140 H270" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M178 148 Q214 118 272 124" stroke="#d8b25e" stroke-width="4" stroke-dasharray="6 7" stroke-linecap="round" fill="none"/></svg>"""
TH_SOCIAL = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M160 46 C142 32 148 14 160 24 C172 14 178 32 160 46Z" fill="#e2ab47"/><circle cx="126" cy="58" r="13" fill="#8fa476"/><circle cx="194" cy="58" r="13" fill="#8fa476"/><path d="M126 74 V112 M126 112 L116 146 M126 112 L136 146 M194 74 V112 M194 112 L184 146 M194 112 L204 146" stroke="#8fa476" stroke-width="7" stroke-linecap="round" fill="none"/><path d="M126 84 L150 96 L160 92 M194 84 L170 96 L160 92" stroke="#d8b25e" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M110 84 L100 104 M210 84 L220 104" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/></svg>"""
C_SRT = KC("otur-kalk-testi.html", TH_SRT, "Kendine iyi bak", "Yere oturup kalkabiliyor musunuz?", "Ellerinizi kullanmadan yere oturup kalkabilmek, 12 yıllık bir araştırmada sağlığın güçlü bir göstergesi çıktı. Puanınızı hesaplayın.")
TH_KNEE12 = """<svg viewBox="0 0 320 150" aria-hidden="true"><g fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M142 18v52l-10 22 6 40M178 18v50l8 26-4 38" stroke="#8fa476" stroke-width="7"/><ellipse cx="160" cy="80" rx="26" ry="12" stroke="#e2ab47" stroke-width="3" stroke-dasharray="4 6"/></g><g transform="translate(56 30) scale(.42)"><path d="M11 21v-6a9 9 0 0 1 18 0v6" fill="none" stroke="#e2ab47" stroke-width="3.4" stroke-linecap="round"/><rect x="6" y="20" width="28" height="23" rx="6" fill="#e2ab47" stroke="#e2ab47" stroke-width="3.4"/></g><g transform="translate(82 82) scale(.42)"><path d="M11 21v-6a9 9 0 0 1 18 0v6" fill="none" stroke="#e2ab47" stroke-width="3.4" stroke-linecap="round"/><rect x="6" y="20" width="28" height="23" rx="6" fill="#e2ab47" stroke="#e2ab47" stroke-width="3.4"/></g><g transform="translate(226 32) scale(.42)"><path d="M11 21v-6a9 9 0 0 1 18 0v6" fill="none" stroke="#e2ab47" stroke-width="3.4" stroke-linecap="round"/><rect x="6" y="20" width="28" height="23" rx="6" fill="none" stroke="#e2ab47" stroke-width="3.4"/></g><g transform="translate(248 84) scale(.42)"><path d="M11 21v-6a9 9 0 0 1 18 0v6" fill="none" stroke="#e2ab47" stroke-width="3.4" stroke-linecap="round"/><rect x="6" y="20" width="28" height="23" rx="6" fill="none" stroke="#e2ab47" stroke-width="3.4"/></g><g transform="translate(40 96) scale(.42)"><path d="M11 21v-6a9 9 0 0 1 18 0v6" fill="none" stroke="#e2ab47" stroke-width="3.4" stroke-linecap="round"/><rect x="6" y="20" width="28" height="23" rx="6" fill="#e2ab47" stroke="#e2ab47" stroke-width="3.4"/></g><g transform="translate(262 40) scale(.42)"><path d="M11 21v-6a9 9 0 0 1 18 0v6" fill="none" stroke="#e2ab47" stroke-width="3.4" stroke-linecap="round"/><rect x="6" y="20" width="28" height="23" rx="6" fill="none" stroke="#e2ab47" stroke-width="3.4"/></g></svg>"""
C_KNEE12 = KC("dizin-12-sirri.html", TH_KNEE12, "Kendine iyi bak", "Dizin 12 Sırrı", "Diz kireçlenmesi için altı haftalık etkileşimli ev programı: telefon sizin için sayar, her seans kilitli bir sırrı açar.")
TH_MINDEX = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="160" cy="40" r="24" fill="none" stroke="#8fa476" stroke-width="7"/><circle cx="160" cy="40" r="8" fill="#e2ab47"/><path d="M160 28 V24 M160 52 V56 M148 40 H144 M172 40 H176 M151.5 31.5 L148.7 28.7 M168.5 31.5 L171.3 28.7 M151.5 48.5 L148.7 51.3 M168.5 48.5 L171.3 51.3" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/><path d="M160 66 L156 104 M156 104 L140 144 M156 104 L176 144 M158 78 L138 98 M158 78 L184 94" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>"""
C_MINDEX = KC("ruh-sagligi-egzersiz.html", TH_MINDEX, "Kendine iyi bak", "Ruh sağlığı için egzersiz", "Depresyon ve kaygıda hangi egzersiz ne kadar işe yarar? 218 çalışmanın bulguları, doz önerileri ve evde altı hareket.")
TH_MOOD = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M100 120 A60 60 0 0 1 111.5 84.7" fill="none" stroke="#c96b5a" stroke-width="14"/><path d="M111.5 84.7 A60 60 0 0 1 141.5 62.9" fill="none" stroke="#d8b25e" stroke-width="14"/><path d="M141.5 62.9 A60 60 0 0 1 220 120" fill="none" stroke="#8fa476" stroke-width="14"/><path d="M160 120 L185 76.7" stroke="#ece5cf" stroke-width="5" stroke-linecap="round"/><circle cx="160" cy="120" r="8" fill="#ece5cf"/><path d="M84 132 H236" stroke="rgba(236,229,207,.25)" stroke-width="3" stroke-linecap="round"/></svg>"""
C_MOOD = KC("ruh-hali-olcumu.html", TH_MOOD, "Kendine iyi bak", "Ruh hâlinizi ölçün", "WHO-5 iyi oluş indeksi ve PHQ-4 kaygı-depresyon taramasıyla son iki haftanızı değerlendirin: 9 soru, 2 dakika. Yanıtlar cihazınızdan çıkmaz.")
TH_PMR = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 122 H262" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><circle cx="92" cy="98" r="12" fill="#8fa476"/><path d="M106 104 L178 106 L246 110 M150 106 L170 92 L196 98" stroke="#8fa476" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M118 70 q10 -9 20 0 t20 0 t20 0 M138 48 q10 -9 20 0 t20 0 t20 0 M158 26 q10 -9 20 0 t20 0" stroke="#e2ab47" stroke-width="4" stroke-linecap="round" fill="none" opacity=".9"/></svg>"""
C_PMR = KC("kas-gevsetme.html", TH_PMR, "Kendine iyi bak", "Kas gevşetme: sesli rehber", "Kasları sırayla sıkıp bırakarak gevşeyin: 18 bölgelik tam ya da 7 bölgelik kısa sürüm, sesli zamanlayıcıyla. Stres, kaygı ve uykuya dalmak için.")
TH_BA = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M70 130 H250" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><rect x="96" y="106" width="42" height="24" rx="3" fill="#8fa476" opacity=".55"/><rect x="138" y="82" width="42" height="48" rx="3" fill="#8fa476" opacity=".8"/><rect x="180" y="58" width="42" height="72" rx="3" fill="#8fa476"/><circle cx="201" cy="34" r="12" fill="#e2ab47"/><path d="M201 14 V8 M181 34 H175 M227 34 H221 M187 20 L183 16 M215 20 L219 16" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/><path d="M117 96 l5 5 9 -11" stroke="#ece5cf" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M159 72 l5 5 9 -11" stroke="#ece5cf" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
C_BA = KC("kucuk-adimlar.html", TH_BA, "Kendine iyi bak", "Küçük adımlar planlayıcısı", "Ruh hâliniz düşükken haftanızı küçük adımlarla planlayın; her adımdan önce ve sonra puanlayıp neyin iyi geldiğini görün.")
TH_KAPI = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="160" cy="52" r="34" fill="rgba(216,178,94,.28)" stroke="#d8b25e" stroke-width="3"/><circle cx="138" cy="92" r="34" fill="rgba(143,164,118,.3)" stroke="#8fa476" stroke-width="3"/><circle cx="182" cy="92" r="34" fill="rgba(143,179,196,.28)" stroke="#8fb3c4" stroke-width="3"/><circle cx="160" cy="79" r="5" fill="#ece5cf"/></svg>"""
C_KAPI = KC("uc-kapi.html", TH_KAPI, "Kendine iyi bak", "Üç Kapı: beden, nefes, zihin", "Duyguya üç yoldan yaklaşın: hareket, nefes ve bir isim. 6 dakikalık sesli seans, Freud’dan beyin araştırmalarına kanıt pusulası ve ustalardan öğrendiklerimiz.")
TH_SIT = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 132 H260" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M96 92 H138 M100 92 V132 M134 92 V132 M98 92 V56" stroke="rgba(236,229,207,.45)" stroke-width="5" stroke-linecap="round" fill="none"/><circle cx="116" cy="44" r="10" fill="#8fa476"/><path d="M114 56 L112 88 H146 V130" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="206" cy="66" r="30" fill="none" stroke="#d8b25e" stroke-width="4"/><path d="M206 46 V66 L220 74" fill="none" stroke="#d8b25e" stroke-width="4" stroke-linecap="round"/><path d="M246 112 l12 -14 l12 14" fill="none" stroke="#e2ab47" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><path d="M258 98 V128" stroke="#e2ab47" stroke-width="4" stroke-linecap="round"/></svg>"""
C_SIT = KC("oturma-suresi.html", TH_SIT, "Kendine iyi bak", "Günlük oturma süresi hesaplayıcısı", "Günde kaç saat oturuyorsunuz, ne kadar hareket ediyorsunuz? Bir milyon kişilik araştırmaya göre oturma ve hareket dengeniz.")
TH_AH = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M50 136 H270" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><g fill="#8fa476"><ellipse cx="96" cy="112" rx="10" ry="16" transform="rotate(-14 96 112)"/><ellipse cx="128" cy="82" rx="10" ry="16" transform="rotate(14 128 82)"/><ellipse cx="160" cy="52" rx="10" ry="16" transform="rotate(-14 160 52)"/></g><g fill="#d8b25e"><circle cx="90" cy="92" r="3"/><circle cx="134" cy="62" r="3"/><circle cx="154" cy="32" r="3"/></g><path d="M206 120 V98 M226 120 V84 M246 120 V66 M266 120 V50" stroke="#e2ab47" stroke-width="10" stroke-linecap="round"/></svg>"""
C_AH = KC("adim-hedefi.html", TH_AH, "Kendine iyi bak", "Adım hedefi planlayıcısı", "Günlük adım ortalamanıza göre haftalık hedef ve plan: 7.000 adım eşiği, yaşa göre hedef aralığı ve haftalık kayıt.")
TH_ISN = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M40 136 H280" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M58 134 L66 112 L74 134 Z M246 134 L254 112 L262 134 Z" fill="#e2ab47"/><circle cx="150" cy="30" r="10" fill="#8fa476"/><path d="M150 42 L144 78 L128 92 L118 116 M144 78 L162 98 L176 108 M148 52 L132 66 M148 52 L168 62" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><circle cx="198" cy="122" r="12" fill="none" stroke="#ece5cf" stroke-width="3"/><path d="M192 116 L204 128 M204 116 L192 128" stroke="#ece5cf" stroke-width="2" opacity=".5"/><path d="M96 70 C88 78 88 90 96 98" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" opacity=".7"/></svg>"""
C_ISN = KC("sakatlanmayi-onleyen-isinma.html", TH_ISN, "Kendine iyi bak", "Sakatlanmayı önleyen ısınma", "Futbolda sakatlanmaları azalttığı gösterilen FIFA 11+ programından uyarlanmış 20 dakikalık ısınma: zamanlayıcı ve haftalık takip.")
TH_AW = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M40 136 H280" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M50 134 L60 108 L70 134 Z M250 134 L260 108 L270 134 Z" fill="#e2ab47"/><path d="M80 124 H240" stroke="rgba(236,229,207,.4)" stroke-width="3" stroke-dasharray="6 7" stroke-linecap="round"/><path d="M228 116 L240 124 L228 132 M92 116 L80 124 L92 132" fill="none" stroke="rgba(236,229,207,.5)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><circle cx="150" cy="30" r="10" fill="#8fa476"/><path d="M150 42 L146 78 L134 96 L130 116 M146 78 L160 96 L166 114 M148 52 L134 70 M148 52 L166 64" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><circle cx="240" cy="54" r="22" fill="none" stroke="#d8b25e" stroke-width="4"/><path d="M240 54 V40 M240 54 L250 60 M234 28 H246" stroke="#ece5cf" stroke-width="3" stroke-linecap="round"/></svg>"""
C_AW = KC("alti-dakika-yurume-testi.html", TH_AW, "Kendine iyi bak", "6 dakika yürüme testi", "6 dakikada ne kadar yürüyebiliyorsunuz? Standart yönlendirmeli süreölçer, parkur sayacı, yaşa göre beklenen mesafe ve sonuç kaydı.")
TH_TG = """<svg viewBox="0 0 320 150" aria-hidden="true"><rect x="70" y="40" width="92" height="80" rx="12" fill="none" stroke="#8fa476" stroke-width="5"/><rect x="84" y="54" width="64" height="32" rx="5" fill="rgba(236,229,207,.12)"/><path d="M94 64 H122 M94 76 H112" stroke="#e2ab47" stroke-width="4" stroke-linecap="round"/><circle cx="116" cy="104" r="6" fill="#d8b25e"/><path d="M162 80 C178 80 176 112 192 112" fill="none" stroke="rgba(236,229,207,.4)" stroke-width="3"/><rect x="206" y="24" width="72" height="104" rx="8" fill="none" stroke="rgba(236,229,207,.45)" stroke-width="3"/><g fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M218 48 l4 4 l8 -9" stroke="#8fa476" stroke-width="3.5"/><path d="M238 48 H266" stroke="rgba(236,229,207,.4)" stroke-width="3"/><path d="M218 74 l4 4 l8 -9" stroke="#8fa476" stroke-width="3.5"/><path d="M238 74 H262" stroke="rgba(236,229,207,.4)" stroke-width="3"/><path d="M218 100 l4 4 l8 -9" stroke="#e2ab47" stroke-width="3.5"/><path d="M238 100 H258" stroke="rgba(236,229,207,.4)" stroke-width="3"/></g></svg>"""
C_TG = KC("tansiyon-gunlugu.html", TH_TG, "Kendine iyi bak", "Ev tansiyon günlüğü", "Evde doğru tansiyon ölçümü: 5 dakika dinlenme ve 1 dakika ara zamanlayıcısı, sabah-akşam kayıt, ilk gün hariç ortalama ve hekime götürülecek dosya.")
TH_DB = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 136 H260" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M188 76 H260 M200 76 V136 M250 76 V136" stroke="#8a6a44" stroke-width="6" stroke-linecap="round" fill="none"/><circle cx="146" cy="26" r="11" fill="#8fa476"/><path d="M146 40 V88 M146 88 L142 134 M146 88 L152 110 L150 134 M146 50 L174 72 L190 74 M146 50 L124 66" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M134 136 H162" stroke="#e2ab47" stroke-width="5" stroke-linecap="round"/><path d="M96 48 C88 60 88 76 96 88 M84 56 C80 64 80 72 84 80" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" opacity=".7"/></svg>"""
C_DB = KC("denge-antrenmani.html", TH_DB, "Kendine iyi bak", "Denge antrenmanı", "Düşmeleri önlemek için Otago programından uyarlanmış altı denge hareketi: üç destek seviyesi, duruş zamanlayıcısı ve 12 haftalık takip.")
TH_YY = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 136 H260" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><ellipse cx="104" cy="104" rx="42" ry="12" fill="none" stroke="rgba(236,229,207,.35)" stroke-width="4"/><ellipse cx="104" cy="100" rx="26" ry="6" fill="#d8b25e" opacity=".75"/><path d="M58 70 V96 M54 70 V80 M62 70 V80 M150 70 V96" stroke="rgba(236,229,207,.45)" stroke-width="3" stroke-linecap="round"/><circle cx="214" cy="32" r="11" fill="#8fa476"/><path d="M214 46 L210 86 L196 108 L192 132 M210 86 L226 106 L232 130 M212 56 L198 76 M212 56 L230 70" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M252 54 A16 16 0 1 1 252 86 A16 16 0 1 1 252 54" fill="none" stroke="#e2ab47" stroke-width="4"/><path d="M252 70 V60 M252 70 L260 74" stroke="#ece5cf" stroke-width="3" stroke-linecap="round"/></svg>"""
C_YY = KC("yemek-sonrasi-yuruyus.html", TH_YY, "Kendine iyi bak", "Yemek sonrası yürüyüş", "Yemekten sonra 10 dakika yürüyüş kan şekerinin yükselmesini yumuşatır: öğün ve süre seçimi, zamanlayıcı ve günlük takip.")
TH_AD = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 136 H260" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M96 20 V136" stroke="rgba(236,229,207,.35)" stroke-width="5" stroke-linecap="round"/><path d="M96 84 H188" stroke="#e2ab47" stroke-width="3" stroke-dasharray="6 6" stroke-linecap="round"/><circle cx="150" cy="26" r="11" fill="#8fa476"/><path d="M150 40 V84 M150 84 L148 110 L150 134 M150 84 L176 84 L172 110 M148 50 L132 70 M150 50 L168 64" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><rect x="208" y="44" width="56" height="70" rx="9" fill="none" stroke="rgba(236,229,207,.35)" stroke-width="4"/><text x="236" y="86" text-anchor="middle" font-family="Georgia,serif" font-size="20" fill="#ece5cf">2:00</text></svg>"""
C_AD = KC("iki-dakika-adim-testi.html", TH_AD, "Kendine iyi bak", "2 dakika adım testi", "2 dakika yerinde adım atarak kondisyonunuzu ölçün: adım sayacı, yaşa ve cinsiyete göre değerler ve bağımsızlık eşiği.")
TH_GD = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 136 H260" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M90 136 V98 H132 V136 M90 98 V56" stroke="#8a6a44" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="148" cy="38" r="11" fill="#8fa476"/><path d="M146 52 L138 86 L156 108 L152 134 M138 86 L122 100 M144 62 L166 78 M144 62 L164 58" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="226" cy="74" r="30" fill="none" stroke="rgba(236,229,207,.25)" stroke-width="6"/><path d="M226 44 A30 30 0 1 1 196 74" fill="none" stroke="#e2ab47" stroke-width="6" stroke-linecap="round"/><path d="M226 74 V58 M226 74 L238 80" stroke="#ece5cf" stroke-width="3.5" stroke-linecap="round"/></svg>"""
C_GD = KC("guc-devresi.html", TH_GD, "Kendine iyi bak", "Evde güç devresi", "Haftada 2 gün kas güçlendirme: 4 ya da 6 hareketlik ev devresi, sesli çalışma-dinlenme zamanlayıcısı ve haftalık takip.")
TH_GETUP = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M50 132 H270" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M226 92 H262 M228 92 V132 M260 92 V132 M260 92 V58" stroke="rgba(236,229,207,.45)" stroke-width="5" stroke-linecap="round" fill="none"/><circle cx="92" cy="96" r="9" fill="#8fa476"/><path d="M100 100 L140 102 M140 102 L140 130 M140 102 L166 128" stroke="#8fa476" stroke-width="7" stroke-linecap="round" fill="none"/><path d="M104 102 L104 130" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/><circle cx="196" cy="54" r="9" fill="#d8b25e"/><path d="M194 64 L186 98 L186 130 M186 98 L208 102 L208 132 M192 72 L226 90" stroke="#d8b25e" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M150 70 C162 54 172 50 180 50 M172 44 l8 6 l-9 4" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
C_GETUP = KC("dustukten-sonra-kalkma.html", TH_GETUP, "Kendine iyi bak", "Düştükten sonra yerden kalkma", "Düştüğünüzde ne yapmalı? Kalkamıyorsanız yardım beklerken yapılacaklar, incinmediyseniz 8 adımda güvenle kalkma.")
TH_TEMPO = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 132 H260" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><circle cx="128" cy="30" r="12" fill="#8fa476"/><path d="M128 44 L124 84 L106 108 L100 130 M124 84 L142 106 L156 128 M126 54 L108 74 M126 54 L148 66" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><g fill="#d8b25e"><circle cx="196" cy="70" r="7"/><circle cx="218" cy="70" r="7" opacity=".7"/><circle cx="240" cy="70" r="7" opacity=".45"/></g><path d="M190 46 c6 -6 6 -14 0 -20 M202 50 c10 -10 10 -24 0 -34" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/><text x="218" y="108" text-anchor="middle" font-family="Georgia,serif" font-size="22" fill="#ece5cf">100</text></svg>"""
C_TEMPO = KC("tempolu-yuruyus.html", TH_TEMPO, "Kendine iyi bak", "Tempolu yürüyüş metronomu", "Dakikada 100 adım orta yoğunluğun eşiği. Adım sesiyle tempo tutun, 15 saniyede temponuzu ölçün, haftanızı takip edin.")
TH_PFT = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M104 110 Q160 150 216 110" fill="none" stroke="rgba(236,229,207,.35)" stroke-width="5" stroke-linecap="round"/><path d="M110 96 Q160 128 210 96" fill="none" stroke="#8fa476" stroke-width="8" stroke-linecap="round"/><circle cx="160" cy="62" r="24" fill="#d8b25e"/><path d="M160 40 V20 M150 30 l10 -10 l10 10" fill="none" stroke="#e2ab47" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="242" cy="54" r="22" fill="none" stroke="rgba(236,229,207,.45)" stroke-width="3"/><path d="M242 42 V54 L250 60" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round"/></svg>"""
C_PFT = KC("pelvik-taban-zamanlayicisi.html", TH_PFT, "Kendine iyi bak", "Pelvik taban egzersiz zamanlayıcısı", "Kadınlar ve erkekler için: sıkın, tutun, gevşeyin. Sesli ve görsel uyarılı zamanlayıcı ve günlük seans takibi.")
TH_FR = """<svg viewBox="0 0 320 150" aria-hidden="true"><rect x="96" y="18" width="128" height="116" rx="12" fill="none" stroke="rgba(236,229,207,.4)" stroke-width="3"/><g stroke-linecap="round" stroke-width="5"><path d="M138 44 H204 M138 70 H204 M138 96 H190" stroke="rgba(236,229,207,.35)"/></g><g fill="none" stroke="#8fa476" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="M112 44 l5 5 l9 -10"/><path d="M112 70 l5 5 l9 -10"/></g><circle cx="119" cy="96" r="6" fill="none" stroke="#d8b25e" stroke-width="3"/><circle cx="252" cy="104" r="26" fill="#223020" stroke="#d8b25e" stroke-width="3"/><text x="252" y="113" text-anchor="middle" font-family="Georgia,serif" font-size="26" fill="#ece5cf">4+</text></svg>"""
C_FR = KC("dusme-riski-testi.html", TH_FR, "Kendine iyi bak", "Düşme riski testi", "On iki soruya evet ya da hayır deyin, düşme riskinizi bir dakikada öğrenin. CDC’nin öz değerlendirme listesi.")
TH_B4 = """<svg viewBox="0 0 320 150" aria-hidden="true"><g fill="#8fa476"><rect x="42" y="52" width="16" height="44" rx="8"/><rect x="62" y="52" width="16" height="44" rx="8"/><rect x="112" y="62" width="16" height="44" rx="8"/><rect x="126" y="34" width="16" height="44" rx="8"/><rect x="186" y="78" width="16" height="44" rx="8"/><rect x="186" y="28" width="16" height="44" rx="8"/><rect x="256" y="52" width="16" height="44" rx="8"/></g><rect x="278" y="40" width="16" height="44" rx="8" fill="none" stroke="rgba(236,229,207,.35)" stroke-width="2" stroke-dasharray="5 4"/><path d="M40 132 H290" stroke="rgba(236,229,207,.25)" stroke-width="3" stroke-linecap="round"/><g fill="#d8b25e"><circle cx="60" cy="132" r="5"/><circle cx="127" cy="132" r="5"/><circle cx="194" cy="132" r="5"/><circle cx="264" cy="132" r="5"/></g></svg>"""
C_B4 = KC("dort-asamali-denge-testi.html", TH_B4, "Kendine iyi bak", "4 aşamalı denge testi", "Giderek zorlaşan dört duruşta 10’ar saniye kalabiliyor musunuz? CDC’nin düşme riski testini süreölçerle yapın.")
TH_MOLA = """<svg viewBox="0 0 320 150" aria-hidden="true"><rect x="62" y="26" width="128" height="80" rx="8" fill="none" stroke="rgba(236,229,207,.45)" stroke-width="5"/><path d="M110 106 L104 126 H148 L142 106" fill="none" stroke="rgba(236,229,207,.45)" stroke-width="5" stroke-linejoin="round"/><circle cx="234" cy="70" r="36" fill="none" stroke="#8fa476" stroke-width="6"/><path d="M234 70 V48 M234 70 L250 80" stroke="#e2ab47" stroke-width="5" stroke-linecap="round"/><path d="M96 62 Q126 44 156 62 Q126 80 96 62 Z" fill="none" stroke="#d8b25e" stroke-width="3"/><circle cx="126" cy="62" r="6" fill="#d8b25e"/></svg>"""
C_MOLA = KC("mola-zamanlayicisi.html", TH_MOLA, "Kendine iyi bak", "Masa başı mola zamanlayıcısı", "Her 20 dakikada göz molası, her 30 dakikada 5 dakikalık hareket molası: ekran başında sesli hatırlatıcı.")
TH_TUG = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 128 H272" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M70 70 V128 M70 98 H104 V128 M104 98 V70" fill="none" stroke="rgba(236,229,207,.45)" stroke-width="5" stroke-linecap="round"/><circle cx="170" cy="40" r="11" fill="#8fa476"/><path d="M170 54 V92 L158 126 M170 92 L184 126 M170 66 L156 82 M170 66 L186 78" fill="none" stroke="#8fa476" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><path d="M236 116 V136" stroke="#e2ab47" stroke-width="5" stroke-linecap="round"/><path d="M210 104 h22 m-6 -6 l6 6 l-6 6" fill="none" stroke="#d8b25e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
C_TUG = KC("kalk-yuru-testi.html", TH_TUG, "Kendine iyi bak", "Kalk ve yürü testi (TUG)", "Sandalyeden kalkıp 3 metre yürüyüp geri oturmanız kaç saniye sürüyor? Süreölçerle ölçün, yaşınızdaki ortalamayla karşılaştırın.")
TH_WHTR = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M126 20 Q112 56 120 76 Q128 96 116 130 M194 20 Q208 56 200 76 Q192 96 204 130" fill="none" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/><ellipse cx="160" cy="78" rx="44" ry="11" fill="none" stroke="#e2ab47" stroke-width="5"/><path d="M252 22 V130 M244 22 H260 M244 130 H260 M246 76 H258" stroke="#d8b25e" stroke-width="3" stroke-linecap="round"/><text x="236" y="80" text-anchor="end" font-family="Georgia,serif" font-size="16" fill="#ece5cf">½</text></svg>"""
C_WHTR = KC("bel-boy-orani.html", TH_WHTR, "Kendine iyi bak", "Bel–boy oranı", "Bel çevreniz boyunuzun yarısından az mı? Oranınızı hesaplayın, NICE sınırlarıyla karşılaştırın, belinizi doğru ölçün.")
TH_PULSE = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M160 128 C104 92 82 66 82 46 a30 30 0 0 1 78 -12 a30 30 0 0 1 78 12 C238 66 216 92 160 128 Z" fill="rgba(201,105,79,.18)" stroke="#c9694f" stroke-width="4" stroke-linejoin="round"/><path d="M58 78 H120 L132 56 L148 104 L162 66 L172 82 H262" fill="none" stroke="#e2ab47" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
C_PULSE = KC("nabiz-olcer.html", TH_PULSE, "Kendine iyi bak", "Nabız ölçer ve hedef nabız", "Nabzınızı elle sayın, ritmin düzenini kontrol edin; yaşınıza göre egzersizde hedef nabız aralığınızı öğrenin.")
TH_AG = """<svg viewBox="0 0 320 150" aria-hidden="true"><rect x="78" y="22" width="164" height="112" rx="14" fill="none" stroke="rgba(236,229,207,.3)" stroke-width="4"/><path d="M96 104 L126 80 L152 92 L180 58 L206 70 L226 46" fill="none" stroke="#e2ab47" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="126" cy="80" r="5" fill="#8fa476"/><circle cx="180" cy="58" r="5" fill="#d8b25e"/><circle cx="226" cy="46" r="5" fill="#c9694f"/><path d="M96 120 H226" stroke="rgba(236,229,207,.18)" stroke-width="3"/></svg>"""
C_AG = KC("agri-gunlugu.html", TH_AG, "Kendine iyi bak", "Ağrı günlüğü", "Ağrınızı, uykunuzu ve hareketinizi her gün bir dakikada kaydedin; seyrini grafikte görün, özeti paylaşın.")
TH_YH = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M60 136 H260" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M80 128 V144 M240 128 V144" stroke="#d8b25e" stroke-width="4" stroke-linecap="round"/><circle cx="150" cy="34" r="11" fill="#8fa476"/><path d="M150 48 L146 88 L132 132 M146 88 L166 108 L176 132 M148 58 L132 80 M148 58 L168 74" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M196 40 H232 M204 52 H232 M212 64 H232" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" opacity=".8"/></svg>"""
C_YH = KC("yurume-hizi-testi.html", TH_YH, "Kendine iyi bak", "Yürüme hızı testi", "Her zamanki temponuzla 4 metreyi kaç saniyede yürüyorsunuz? Süreölçerle ölçün, yaşınızdaki ortalamayla karşılaştırın.")
TH_CST = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M70 140 H230" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M86 140 V100 H130 V140 M86 100 V52" stroke="#8a6a44" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="150" cy="28" r="11" fill="#8fa476"/><path d="M150 42 V86 M150 86 L148 112 L150 138 M150 86 L146 112" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M136 56 L164 56" stroke="#d8b25e" stroke-width="7" stroke-linecap="round"/><rect x="196" y="40" width="58" height="76" rx="9" fill="none" stroke="rgba(236,229,207,.35)" stroke-width="4"/><circle cx="225" cy="70" r="16" fill="none" stroke="#e2ab47" stroke-width="4"/><text x="225" y="76" text-anchor="middle" font-family="Georgia,serif" font-size="17" fill="#ece5cf">30</text></svg>"""
C_CST = KC("sandalye-testi.html", TH_CST, "Kendine iyi bak", "30 saniye sandalye testi", "30 saniyede sandalyeden kaç kez kalkabiliyorsunuz? Telefonunuzun kamerası saysın, sonucunuzu yaşıtlarınızla karşılaştırın.")
TH_PAINX = """<svg viewBox="0 0 320 150" aria-hidden="true"><rect x="132" y="10" width="56" height="130" rx="18" fill="#10170e" stroke="rgba(236,229,207,.3)" stroke-width="3"/><circle cx="160" cy="38" r="14" fill="#d9534f" opacity=".25"/><circle cx="160" cy="75" r="14" fill="#e8b83e" opacity=".25"/><circle cx="160" cy="112" r="14" fill="#7fb069"/><circle cx="160" cy="112" r="20" fill="none" stroke="#7fb069" stroke-width="2" opacity=".6"/><path d="M80 120 L96 96 L112 108 M226 60 h30 M226 75 h22 M226 90 h30" stroke="#8fa476" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>"""
C_PAINX = KC("egzersizde-agri.html", TH_PAINX, "Kendine iyi bak", "Egzersizde ağrı trafik ışığı", "Egzersiz yaparken ağrı normal mi, ne zaman durmalı? Üç soruyu yanıtlayın: yeşil devam, sarı izle, kırmızı yükü azalt.")
TH_PAINU = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M140 104 V74 a20 20 0 0 1 40 0 V104 Z" fill="rgba(216,178,94,.3)" stroke="#d8b25e" stroke-width="4" stroke-linejoin="round"/><path d="M130 104 H190 M154 112 a6 6 0 0 0 12 0" stroke="#d8b25e" stroke-width="4" stroke-linecap="round" fill="none"/><path d="M112 64 a50 50 0 0 0 0 44 M208 64 a50 50 0 0 1 0 44 M98 54 a68 68 0 0 0 0 64 M222 54 a68 68 0 0 1 0 64" fill="none" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" opacity=".8"/><path d="M70 136 H250" stroke="rgba(236,229,207,.2)" stroke-width="6" stroke-linecap="round"/><path d="M70 136 H150" stroke="#8fa476" stroke-width="6" stroke-linecap="round"/></svg>"""
C_PAINU = KC("agriyi-anlamak.html", TH_PAINU, "Kendine iyi bak", "Ağrıyı anlamak", "Ağrı her zaman gerçektir, ama şiddeti her zaman doku hasarını göstermez. Vücudun alarm sistemi ve ağrısız insanların MR bulguları.")
TH_SNACK = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M70 138 H110 V114 H150 V90 H190 V66 H230 V42 H260" fill="none" stroke="rgba(236,229,207,.35)" stroke-width="5" stroke-linejoin="round"/><circle cx="168" cy="30" r="11" fill="#8fa476"/><path d="M168 44 V70 L156 82 L160 90 M168 70 L182 74 L186 66 M168 50 L154 60 M168 50 L182 58" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="92" cy="58" r="22" fill="none" stroke="rgba(236,229,207,.18)" stroke-width="5"/><path d="M92 36 A22 22 0 1 1 70 58" fill="none" stroke="#e2ab47" stroke-width="5" stroke-linecap="round"/><text x="92" y="64" text-anchor="middle" font-family="Georgia,serif" font-size="15" fill="#ece5cf">1:00</text></svg>"""
C_SNACK = KC("hareket-atistirmaliklari.html", TH_SNACK, "Kendine iyi bak", "Hareket atıştırmalıkları", "Spora vakit yok mu? Gün içine serpiştirilmiş birer dakikalık hızlı hareketler: altı atıştırmalık ve bir dakikalık zamanlayıcı.")
TH_BAL = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M96 140 H200" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><circle cx="138" cy="30" r="12" fill="#8fa476"/><path d="M138 46 V92 M138 92 V138 M138 92 L156 104 L148 120" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M120 62 L156 62" stroke="#d8b25e" stroke-width="7" stroke-linecap="round"/><circle cx="238" cy="80" r="30" fill="none" stroke="rgba(236,229,207,.18)" stroke-width="6"/><path d="M238 50 A30 30 0 0 1 266 70" fill="none" stroke="#e2ab47" stroke-width="6" stroke-linecap="round"/><text x="238" y="88" text-anchor="middle" font-family="Georgia,serif" font-size="22" fill="#ece5cf">10</text></svg>"""
C_BAL = KC("denge-testi.html", TH_BAL, "Kendine iyi bak", "10 saniye denge testi", "Bir ayağınızın üzerinde 10 saniye durabiliyor musunuz? Süreölçerle deneyin, yaşınızdaki ortalamayla karşılaştırın.")
C_WALLSIT = KC("duvar-oturusu.html", TH_WALLSIT, "Kendine iyi bak", "Tansiyon için duvar oturuşu", "270 çalışmalık analizde tansiyonu en çok düşüren egzersiz türü. Haftada 3 gün, 4 × 2 dakika: zamanlayıcıyla birlikte yapın.")
C_SIGH = KC("ic-cekis.html", TH_SIGH, "Kendine iyi bak", "5 dakikalık iç çekiş nefesi", "Stanford'daki çalışmada ruh hâlini meditasyondan daha çok iyileştiren nefes: iki kez alın, uzun verin.")
C_NATURE = KC("doga-recetesi.html", TH_NATURE, "Kendine iyi bak", "Doğa reçetesi", "Haftada 120 dakika doğa; parça parça da olur. Haftalık doğa takviminiz ve İstanbul'dan öneriler.")
C_SOCIAL = KC("bag-kurmak.html", TH_SOCIAL, "Kendine iyi bak", "Sosyal bağ ve sağlık", "Güçlü sosyal ilişkileri olanların hayatta kalma olasılığı %50 daha yüksek. Şaşırtan bulgular ve her gün için küçük bir öneri.")
TH_DOST = """<svg viewBox="0 0 320 150" aria-hidden="true"><g transform="rotate(-4 160 80)"><rect x="102" y="32" width="116" height="96" rx="8" fill="#ece5cf"/><path d="M122 62 H170 M122 80 H198 M122 98 H184" stroke="#8fa476" stroke-width="6" stroke-linecap="round"/><rect x="138" y="24" width="44" height="14" rx="2" fill="#d8b25e" opacity=".85"/></g><path transform="translate(184 16) scale(.46)" d="M50 86 C22 64 8 46 8 30 C8 16 19 7 31 7 C39 7 46 12 50 20 C54 12 61 7 69 7 C81 7 92 16 92 30 C92 46 78 64 50 86Z" fill="#e2ab47"/></svg>"""
C_DOST = KC("dost-molasi.html", TH_DOST, "Kendine iyi bak", "DOST molası", "Zor bir günde kendinize dost olmanın dört adımı: dur, omuzlarını bırak, seslen, teşekkür et. Beş dakikada kendinize kısa bir not yazın.")
REGIONS = [("tum", "Tümü"), ("bel", "Bel ve sırt"), ("boyun", "Boyun, baş ve çene"), ("omuz", "Omuz, kol ve el"),
           ("diz", "Kalça ve diz"), ("ayak", "Ayak ve ayak bileği"), ("kadin", "Kadın sağlığı"), ("genel", "Tüm vücut")]
AGR = [(C_BACK, "bel"), (C_SCIATICA, "bel"), (C_BFA, "bel"), (C_PI, "bel"), (C_SI, "bel"), (C_LS, "bel"), (C_SPL, "bel"), (C_CX, "bel"), (C_AS, "bel"), (C_SCOLIOSIS, "bel"), (C_KY, "bel"), (C_VF, "bel"), (C_UB, "bel"), (C_KB, "bel"),
       (C_NECK, "boyun"), (C_BT, "boyun"), (C_TOR, "boyun"), (C_WH, "boyun"), (C_BD, "boyun"), (C_HERNIA, "boyun"), (C_HEADACHE, "boyun"), (C_TMJ, "boyun"), (C_VERTIGO, "boyun"), (C_CONC, "boyun"),
       (C_SHOULDER, "omuz"), (C_SO, "omuz"), (C_IMPINGE, "omuz"), (C_RC, "omuz"), (C_CF, "omuz"), (C_DI, "omuz"), (C_KL, "omuz"), (C_ACJ, "omuz"), (C_CTS, "omuz"), (C_CU, "omuz"), (C_ELBOW, "omuz"), (C_DQ, "omuz"), (C_TF, "omuz"), (C_DUP, "omuz"), (C_MF, "omuz"), (C_GG, "omuz"), (C_WB, "omuz"), (C_HO, "omuz"), (C_GOLF, "omuz"),
       (C_KNEE, "diz"), (C_MENISCUS, "diz"), (C_BK, "diz"), (C_ACL, "diz"), (C_PD, "diz"), (C_PFP, "diz"), (C_OS, "diz"), (C_GRP, "diz"), (C_JK, "diz"), (C_ITB, "diz"), (C_HS, "diz"), (C_HIP, "diz"), (C_FAI, "diz"), (C_KS, "diz"), (C_GTPS, "diz"),
       (C_HEEL, "ayak"), (C_SV, "ayak"), (C_ACHILLES, "ayak"), (C_AR, "ayak"), (C_SS, "ayak"), (C_CZ, "ayak"), (C_ANKLE, "ayak"), (C_AK, "ayak"), (C_MT5, "ayak"), (C_DN, "ayak"), (C_FLAT, "ayak"), (C_HV, "ayak"), (C_MN, "ayak"),
       (C_UI, "kadin"), (C_POP, "kadin"), (C_DR, "kadin"), (C_PREG, "kadin bel"), (C_OSTEO, "genel"), (C_SARC, "genel"), (C_FIBRO, "genel"), (C_RA, "genel"), (C_COLD, "genel"), (C_TREMOR, "genel"), (C_FACE, "genel"), (C_RLS, "genel"), (C_LC, "genel"), (C_JH, "genel")]
def region_filter():
    cnt = {r: sum(1 for _, rr in AGR if r in rr.split()) for r, _ in REGIONS}
    cnt["tum"] = len(AGR)
    return ('<div class="filt" role="group" aria-label="Bölgeye göre süz">' +
            "".join(f'<button type="button" data-f="{r}" aria-pressed="{"true" if r == "tum" else "false"}"><span>{t}</span><small>{cnt[r]}</small></button>' for r, t in REGIONS) +
            '</div>')
REHAB = [C_FALLS, C_PROSTH, C_STROKE, C_SCI, C_GBS, C_HIPFX, C_PARK, C_DEM, C_MS, C_ONCO, C_LYMPH, C_COPD, C_CARDIAC, C_PAD, C_HF, C_DIA, C_ICU, C_HT, C_LCOV, C_GLP]
SELF = [C_KNEE12, C_MINDEX, C_MOOD, C_PMR, C_BA, C_KAPI, C_DOST, C_SRT, C_BAL, C_B4, C_CST, C_YH, C_AD, C_AW, C_TUG, C_FR, C_GETUP, C_PULSE, C_TG, C_WHTR, C_WALLSIT, C_PFT, C_SNACK, C_GD, C_YY, C_DB, C_ISN, C_TEMPO, C_MOLA, C_PAINU, C_PAINX, C_AG, C_SIGH, C_NATURE, C_SOCIAL, C_MORNING, C_MOVE, C_AH, C_SIT, C_SLEEP, C_STRES, C_DESK]
def _kc_info(c):
    return _re.search(r'href="([^"]+)"', c).group(1), _re.search(r"<h3>(.*?)</h3>", c).group(1)
def agr_cards():
    """Kartlar + (liste görünümünde görünen) bölge başlıkları. Kart ilk bölge etiketinin başlığı altında durur."""
    names = dict(REGIONS); out = []; last = None
    for c, r in AGR:
        r0 = r.split()[0]
        if r0 != last:
            out.append(f'<p class="grp" data-r="{r0}"><span>{names[r0]}</span></p>'); last = r0
        out.append(c.replace('<a class="kc" ', f'<a class="kc" data-r="{r}" ', 1))
    return "\n          ".join(out)
AGR_CARDS = agr_cards()
REHAB_CARDS = "\n          ".join(REHAB)
SELF_CARDS = "\n          ".join(SELF)

def pulse(pre=""):
    """Yayın sayacı: kategori başına rehber sayısı (yukarı doğru sayar) ve sırayla dönen rehber başlıkları."""
    allc = [c for c, _ in AGR] + REHAB + SELF
    order = [allc[(i * 7) % len(allc)] for i in range(len(allc))] if len(allc) % 7 else allc
    rot = "".join(f'<a href="{h}"{" class=" + chr(34) + "on" + chr(34) if i == 0 else ""}>{t}</a>' for i, (h, t) in enumerate(map(_kc_info, order)))
    return f"""<div class="pulse" id="pulse">
        <p class="pulse-live">Sizin için yayında</p>
        <div class="pulse-nums">
          <a href="{pre}#agrilar"><b class="pn">{len(AGR)}</b><span>hastalık rehberi</span></a>
          <a href="{pre}#rehabilitasyon"><b class="pn">{len(REHAB)}</b><span>rehabilitasyon rehberi</span></a>
          <a href="{pre}#kendine-iyi-bak"><b class="pn">{len(SELF)}</b><span>kendine iyi bak rehberi</span></a>
          <a href="{pre}#tipta-yenilikler"><b class="pn">{len(NEWS)}</b><span>bilim haberi</span></a>
        </div>
        <p class="pulse-rot"><span>Örneğin</span><span class="rot">{rot}</span></p>
      </div>"""
PULSE_JS = """<script>
(function(){
  var box = document.getElementById('pulse'); if (!box) return;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function count(){
    [].forEach.call(box.querySelectorAll('.pn'), function(el, i){
      var to = +el.textContent, st = null, dur = 1100, delay = i * 160; if (!to) return;
      el.textContent = '0';
      function step(ts){
        if (st === null) st = ts;
        var t = Math.min(1, Math.max(0, (ts - st - delay) / dur)), e = 1 - Math.pow(1 - t, 3);
        el.textContent = Math.round(to * e);
        if (t < 1) requestAnimationFrame(step); else el.textContent = to;
      }
      requestAnimationFrame(step);
    });
  }
  var rot = box.querySelector('.rot'), items = rot ? rot.querySelectorAll('a') : [], k = 0, hold = false, tm = null, rel = null;
  function next(){
    if (hold || document.hidden) return;
    items[k].classList.remove('on'); k = (k + 1) % items.length; items[k].classList.add('on');
  }
  if (rot) {
    ['mouseenter', 'focusin'].forEach(function(ev){ rot.addEventListener(ev, function(){ hold = true; }); });
    ['mouseleave', 'focusout'].forEach(function(ev){ rot.addEventListener(ev, function(){ hold = false; }); });
    rot.addEventListener('touchstart', function(){ hold = true; clearTimeout(rel); rel = setTimeout(function(){ hold = false; }, 5000); }, {passive: true});
  }
  function run(){
    if (reduce) return;
    count();
    if (items.length > 1 && !tm) tm = setInterval(next, 2600);
  }
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(es){ if (es[0].isIntersecting) { io.disconnect(); run(); } }, {threshold: .4});
    io.observe(box);
  } else run();
})();
</script>
"""
PILL = {
    "adim-hedefi.html": "Adım hedefi",
    "sakatlanmayi-onleyen-isinma.html": "Sakatlanmayı önleyen ısınma",
    "zayiflama-ilaci-ve-kas.html": "Zayıflama ilacı ve kas",
    "uzun-covid.html": "Uzun COVID",
    "kosucu-dizi.html": "Koşucu dizi",
    "alti-dakika-yurume-testi.html": "6 dk yürüme testi",
    "tansiyon-gunlugu.html": "Tansiyon günlüğü",
    "yuksek-tansiyon.html": "Yüksek tansiyon",
    "yogun-bakim-sonrasi.html": "Yoğun bakım sonrası",
    "diyabette-egzersiz.html": "Diyabet",
    "denge-antrenmani.html": "Denge antrenmanı",
    "yemek-sonrasi-yuruyus.html": "Yemek sonrası yürüyüş",
    "omurga-kirigi.html": "Omurga kırığı",
    "dupuytren-kontrakturu.html": "Dupuytren",
    "kalp-yetmezligi.html": "Kalp yetmezliği",
    "iki-dakika-adim-testi.html": "2 dakika adım testi",
    "guc-devresi.html": "Güç devresi",
    "pelvik-organ-sarkmasi.html": "Rahim sarkması",
    "beyin-sarsintisi.html": "Beyin sarsıntısı",
    "periferik-arter-hastaligi.html": "Periferik arter hastalığı",
    "bel-agrisi.html": "Bel ağrısı", "bel-fitigi.html": "Bel fıtığı", "dar-kanal.html": "Dar kanal", "bel-kaymasi.html": "Bel kayması", "huzursuz-bacak.html": "Huzursuz bacak", "kuyruk-sokumu-agrisi.html": "Kuyruk sokumu", "bebeklerde-tortikolis.html": "Bebeklerde tortikolis", "besinci-metatars-kirigi.html": "5. tarak kemiği kırığı", "omuz-ucu-yaralanmasi.html": "Omuz ucu yaralanması", "cekic-parmak.html": "Çekiç parmak", "kasik-zorlanmasi.html": "Kasık zorlanması", "kaburga-kirigi.html": "Kaburga kırığı", "bel-fitigi-ameliyati-sonrasi.html": "Bel fıtığı ameliyatı sonrası", "buyume-agrilari.html": "Büyüme ağrıları", "koprucuk-kemigi-kirigi.html": "Köprücük kemiği kırığı", "ayak-bilegi-kirigi.html": "Ayak bileği kırığı", "baldir-kasi-zorlanmasi.html": "Baldır kası zorlanması", "omuz-kireclenmesi.html": "Omuz kireçlenmesi", "asil-tendonu-kopmasi.html": "Aşil kopması", "kubital-tunel-sendromu.html": "Kübital tünel", "diz-kapagi-cikigi.html": "Diz kapağı çıkığı", "sever-hastaligi.html": "Sever hastalığı", "karin-kasi-ayrilmasi.html": "Karın kası ayrılması", "omuzda-kirec-birikmesi.html": "Omuzda kireç birikmesi", "boyun-incinmesi.html": "Boyun incinmesi", "el-kireclenmesi.html": "El ve parmak kireçlenmesi", "eklem-hipermobilitesi.html": "Eklem hipermobilitesi", "el-bilegi-kirigi.html": "El bileği kırığı sonrası", "morton-noromasi.html": "Morton nöroması", "osgood-schlatter.html": "Osgood-Schlatter", "sakroiliak-eklem-agrisi.html": "Sakroiliak eklem ağrısı", "arka-uyluk-zorlanmasi.html": "Arka uyluk zorlanması", "kaval-kemigi-agrisi.html": "Kaval kemiği ağrısı", "boyun-tutulmasi.html": "Boyun tutulması", "ganglion-kisti.html": "Ganglion kisti", "gece-bacak-kramplari.html": "Gece bacak krampları", "kurek-kemigi-arasi-agri.html": "Kürek kemiği arası ağrı", "baker-kisti.html": "Baker kisti", "kambur-durus.html": "Kambur duruş", "piriformis-sendromu.html": "Piriformis sendromu", "omuz-cikigi.html": "Omuz çıkığı", "atlet-dizi.html": "Atlet dizi", "kalca-sikismasi.html": "Kalça sıkışması", "boyun-duzlesmesi.html": "Boyun düzleşmesi", "on-capraz-bag.html": "Ön çapraz bağ", "romatoid-artrit.html": "Romatoid artrit", "yuz-felci.html": "Yüz felci", "kalca-yan-agrisi.html": "Kalça yan ağrısı", "lenfodem.html": "Lenfödem", "de-quervain.html": "De Quervain", "duztabanlik.html": "Düztabanlık", "halluks-valgus.html": "Halluks valgus", "golfcu-dirsegi.html": "Golfçü dirseği", "guillain-barre.html": "Guillain-Barré", "sarkopeni.html": "Sarkopeni", "demans-egzersiz.html": "Demansta egzersiz", "tetik-parmak.html": "Tetik parmak", "omurilik-yaralanmasi.html": "Omurilik yaralanması", "diyabetik-noropati.html": "Diyabetik nöropati", "surekli-usume.html": "Sürekli üşüme", "titreme.html": "Titreme", "boyun-agrisi.html": "Boyun ağrısı",
    "boyun-fitigi.html": "Boyun fıtığı", "bas-agrisi.html": "Baş ağrısı", "cene-eklemi.html": "Çene eklemi",
    "diz-kireclenmesi.html": "Diz kireçlenmesi", "menisku-yirtigi.html": "Menisküs yırtığı", "diz-onu-agrisi.html": "Diz önü ağrısı",
    "kalca-kireclenmesi.html": "Kalça kireçlenmesi", "donuk-omuz.html": "Donuk omuz", "omuz-sikismasi.html": "Omuz sıkışması",
    "rotator-manset-yirtigi.html": "Rotator manşet yırtığı", "karpal-tunel-sendromu.html": "Karpal tünel", "tenisci-dirsegi.html": "Tenisçi dirseği",
    "kemik-erimesi.html": "Kemik erimesi", "fibromiyalji.html": "Fibromiyalji", "ankilozan-spondilit.html": "Ankilozan spondilit",
    "bas-donmesi.html": "Baş dönmesi", "ayak-bilegi-burkulmasi.html": "Ayak bileği burkulması", "asil-tendinopatisi.html": "Aşil tendinopatisi",
    "skolyoz.html": "Skolyoz", "idrar-kacirma.html": "İdrar kaçırma", "gebelikte-bel-agrisi.html": "Gebelikte bel ağrısı",
    "topuk-dikeni.html": "Topuk dikeni",
    "inme-rehabilitasyonu.html": "İnme sonrası", "dusme-onleme.html": "Düşmeyi önleme", "protez-sonrasi.html": "Protez sonrası",
    "kalca-kirigi.html": "Kalça kırığı", "parkinson.html": "Parkinson", "multipl-skleroz.html": "Multipl skleroz (MS)", "kanser-egzersiz.html": "Kanser ve egzersiz", "koah.html": "KOAH", "kalp-rehabilitasyonu.html": "Kalp rehabilitasyonu",
    "masa-basi.html": "Masa başı", "sabah-rutini.html": "Sabah rutini", "hareket.html": "Ne kadar hareket?", "uyku.html": "İyi uyku",
    "otur-kalk-testi.html": "Otur-kalk testi", "dizin-12-sirri.html": "Dizin 12 Sırrı", "duvar-oturusu.html": "Tansiyon için duvar oturuşu", "ic-cekis.html": "İç çekiş nefesi",
    "doga-recetesi.html": "Doğa reçetesi", "bag-kurmak.html": "Sosyal bağ", "dost-molasi.html": "DOST molası", "stres.html": "Stres",
    "uc-kapi.html": "Üç Kapı",
    "oturma-suresi.html": "Oturma süresi",
    "dustukten-sonra-kalkma.html": "Düştükten sonra kalkma",
    "tempolu-yuruyus.html": "Tempolu yürüyüş",
    "pelvik-taban-zamanlayicisi.html": "Pelvik taban zamanlayıcısı",
    "dusme-riski-testi.html": "Düşme riski testi",
    "dort-asamali-denge-testi.html": "4 aşamalı denge testi",
    "mola-zamanlayicisi.html": "Mola zamanlayıcısı",
    "kalk-yuru-testi.html": "Kalk ve yürü testi",
    "bel-boy-orani.html": "Bel–boy oranı",
    "nabiz-olcer.html": "Nabız ölçer",
    "agri-gunlugu.html": "Ağrı günlüğü",
    "yurume-hizi-testi.html": "Yürüme hızı testi",
    "sandalye-testi.html": "Sandalye testi",
    "egzersizde-agri.html": "Egzersizde ağrı",
    "agriyi-anlamak.html": "Ağrıyı anlamak",
    "hareket-atistirmaliklari.html": "Hareket atıştırmalıkları",
    "denge-testi.html": "Denge testi",
    "kucuk-adimlar.html": "Küçük adımlar",
    "kas-gevsetme.html": "Kas gevşetme",
    "ruh-hali-olcumu.html": "Ruh hâli ölçümü",
    "ruh-sagligi-egzersiz.html": "Ruh sağlığı için egzersiz",
}
def pill_group(label, anchor, cards):
    pills = "".join(f'<a class="{_pc(h)}" href="{h}">{PILL[h]}{STAR if h in PREM else ""}</a>' for h, _ in map(_kc_info, cards))
    return (f'<div class="kg"><a class="lbl" href="bilgi.html#{anchor}"><span>{label}</span><small>{len(cards)}</small></a>'
            f'<div class="pl">{pills}</div></div>')
HUB_JS = """<script>
(function(){
  var sec = document.getElementById('agrilar'); if (!sec) return;
  var bar = sec.querySelector('.filt'); if (!bar) return;
  bar.addEventListener('click', function(e){
    var b = e.target.closest('button'); if (!b) return;
    var f = b.getAttribute('data-f');
    bar.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
    sec.querySelectorAll('.kose > [data-r]').forEach(function(c){ c.hidden = f !== 'tum' && c.getAttribute('data-r').split(' ').indexOf(f) < 0; });
  });
})();
(function(){
  var hub = document.getElementById('hub'), tabs = document.getElementById('tabs'); if (!hub || !tabs) return;
  var top = document.querySelector('header.bar'), root = document.documentElement;
  function fit(){ if (top) root.style.setProperty('--barh', top.offsetHeight + 'px'); root.style.setProperty('--tabsh', tabs.offsetHeight + 'px'); }
  fit(); window.addEventListener('resize', fit);
  // kategori çubuğu: görünen bölümü işaretle
  var strip = tabs.querySelector('.tabs-s'), links = strip.querySelectorAll('a'), cur = null;
  function mark(id){
    if (id === cur) return; cur = id;
    [].forEach.call(links, function(a){
      if (id && a.getAttribute('href') === '#' + id) {
        a.setAttribute('aria-current', 'true');
        var l = a.offsetLeft - 12; if (l < strip.scrollLeft || a.offsetLeft + a.offsetWidth > strip.scrollLeft + strip.clientWidth - 24) strip.scrollLeft = l;
      } else a.removeAttribute('aria-current');
    });
  }
  var cats = hub.querySelectorAll('.cat'), tick = false;
  function spy(){
    tick = false;
    var line = tabs.getBoundingClientRect().bottom + 48, id = null;
    [].forEach.call(cats, function(c){ if (c.getBoundingClientRect().top <= line) id = c.id; });
    // son bölüm kısa olduğu için başlığı çubuğun altına kadar çıkamayabilir: sayfa sonunda onu işaretle
    if (id && window.innerHeight + window.pageYOffset >= root.scrollHeight - 4) id = cats[cats.length - 1].id;
    mark(id);
  }
  window.addEventListener('scroll', function(){ if (!tick) { tick = true; requestAnimationFrame(spy); } }, {passive: true});
  spy();
  // liste / kart görünümü: sayfa her açıldığında liste görünümüyle başlar; kart görünümü yalnızca o ziyarette geçerli
  var vb = document.querySelectorAll('.view button');
  function setView(v, user){
    hub.setAttribute('data-view', v);
    [].forEach.call(vb, function(b){ b.setAttribute('aria-pressed', b.getAttribute('data-v') === v ? 'true' : 'false'); });
    if (!user) return;
    var el = cur && document.getElementById(cur);
    if (el && tabs.getBoundingClientRect().top <= (top ? top.offsetHeight : 0) + 2) el.scrollIntoView();
  }
  try { localStorage.removeItem('bk-view'); } catch (e) {}
  setView('list', false);
  [].forEach.call(vb, function(b){ b.addEventListener('click', function(){ setView(b.getAttribute('data-v'), true); }); });
})();
</script>
""" + PULSE_JS

HOME_SECTION = f"""  <section id="bilgi">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Bilgi köşesi</p>
        <h2>Herkes için kısa rehberler</h2>
        <p class="intro">Sık karşılaşılan ağrılar ve hastalıklar, kendinize iyi bakmanız için pratik egzersizler ve güncel bilimsel gelişmeler. Her yazının kaynağı belirtilmiştir.</p>
      </div>
      {search_field()}
      {pulse("bilgi.html")}
      <div class="kose">
        {C_BACK}
        {C_STRES}
        {C_NEWS}
      </div>
      <div class="kose-idx">
        {pill_group("Hastalıklar", "agrilar", [c for c, _ in AGR])}
        {pill_group("Evde rehabilitasyon", "rehabilitasyon", REHAB)}
        {pill_group("Kendine iyi bak", "kendine-iyi-bak", SELF)}
        <div class="kg"><a class="lbl" href="yenilikler.html"><span>Bilim gündemi</span><small>{len(NEWS)}</small></a><div class="pl">{headlines("yenilikler.html", NEWS[:4])}</div></div>
        <a class="all" href="bilgi.html">Tüm konular →</a>
      </div>
    </div>
  </section>
{PULSE_JS}"""

# ------------------------------------------------------------------ BİLGİ KÖŞESİ (hub)
HUB_CSS = HOME_CSS + """
  .cat h2{margin-bottom:6px}
  .cat > p{color:var(--ink-soft);margin-bottom:18px}
  .cat + .cat{margin-top:clamp(36px,6vw,56px)}
  .cat{scroll-margin-top:calc(var(--barh,57px) + var(--tabsh,50px) + 16px)}
  .filt{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 20px}
  .filt button{all:unset;cursor:pointer;padding:8px 14px;border-radius:999px;border:1px solid var(--line-strong);font-size:14px;color:var(--ink-soft)}
  .filt button:hover{border-color:var(--foil);color:var(--ink)}
  .filt button[aria-pressed="true"]{background:var(--foil);border-color:var(--foil);color:var(--ground);font-weight:600}
  .filt button:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
  .filt small{font-size:12px;opacity:.75;margin-left:4px}
  .kose > [hidden]{display:none!important}
  .hl-all{margin:14px 0 26px;max-width:none;text-align:right;font-weight:600;font-size:15px}
  .hl-all a{text-decoration:none}
  .hl-all a:hover{text-decoration:underline}
  header.page .pulse{margin-bottom:0}
  /* yapışkan kategori çubuğu + görünüm düğmesi */
  .tabs{position:sticky;top:calc(env(safe-area-inset-top,0px) + var(--barh,57px));z-index:30;background:rgba(28,40,25,.94);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
  .tabs .wrap{display:flex;align-items:center;gap:10px;padding-block:8px}
  .tabs-s{flex:1;min-width:0;display:flex;gap:4px;overflow-x:auto;scrollbar-width:none;-webkit-overflow-scrolling:touch;
    -webkit-mask-image:linear-gradient(90deg,#000 calc(100% - 22px),transparent);mask-image:linear-gradient(90deg,#000 calc(100% - 22px),transparent)}
  .tabs-s::-webkit-scrollbar{display:none}
  .tabs-s a{flex:none;display:inline-flex;align-items:baseline;gap:6px;padding:7px 13px;border-radius:999px;border:1px solid transparent;color:var(--ink-soft);text-decoration:none;font-size:14px;line-height:1.2;white-space:nowrap}
  .tabs-s a:last-child{margin-right:18px}
  .tabs-s a:hover{color:var(--foil)}
  .tabs-s a[aria-current]{border-color:var(--line-strong);color:var(--foil);background:rgba(216,178,94,.08)}
  .tabs-s small{font-size:12px;color:var(--muted)}
  .view{flex:none;display:inline-flex;gap:2px;padding:2px;border:1px solid var(--line-strong);border-radius:999px}
  .view button{all:unset;cursor:pointer;display:grid;place-items:center;width:34px;height:30px;border-radius:999px;color:var(--ink-soft)}
  .view button:hover{color:var(--foil)}
  .view button[aria-pressed="true"]{background:var(--foil);color:var(--ground)}
  .view button:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
  .view svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
  .view-m{display:none}
  /* telefon ve tablet: dört başlık yana kaydırmadan, iki satırda */
  @media (max-width:1040px){
    .tabs .wrap{padding-block:7px}
    .tabs-s{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:5px;overflow:visible;-webkit-mask-image:none;mask-image:none}
    .tabs-s a{min-width:0;justify-content:space-between;padding:7px 11px;font-size:13px;border-color:var(--line)}
    .tabs-s a:last-child{margin-right:0}
    .tabs-s a span{min-width:0;overflow:hidden;text-overflow:ellipsis}
  }
  /* telefon: görünüm düğmesi listenin üstünde */
  @media (max-width:700px){
    .tabs .view{display:none}
    .view-m{display:flex;align-items:center;justify-content:flex-end;gap:10px;margin:0 0 14px;font-size:13px;color:var(--muted)}
  }
  @media (max-width:379px){.tabs-s small{display:none}}
  /* liste görünümü: aynı kartlar, sıkı satırlar ve bölge başlıkları */
  .grp{display:none;margin:0;max-width:none}
  .hub[data-view="list"] .kose{grid-template-columns:repeat(2,minmax(0,1fr));gap:0 34px}
  @media (max-width:820px){.hub[data-view="list"] .kose{grid-template-columns:minmax(0,1fr)}}
  .hub[data-view="list"] .kc{grid-template-rows:none;grid-template-columns:64px minmax(0,1fr) 10px;align-items:center;gap:14px;padding:11px 6px 11px 2px;border:0;border-bottom:1px solid var(--line);border-radius:0;background:none}
  .hub[data-view="list"] .kc svg{border:1px solid var(--line);border-radius:8px}
  .hub[data-view="list"] .kc .b{padding:0;gap:1px;min-width:0}
  .hub[data-view="list"] .kc .k,.hub[data-view="list"] .kc .go{display:none}
  .hub[data-view="list"] .kc h3{font-size:18px;line-height:1.25}
  .hub[data-view="list"] .kc p{font-size:13.5px;line-height:1.4;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .hub[data-view="list"] .kc::after{content:"";width:7px;height:7px;border-top:2px solid var(--foil);border-right:2px solid var(--foil);transform:rotate(45deg);opacity:.75}
  .hub[data-view="list"] .kc:hover h3{color:var(--foil)}
  .hub[data-view="list"] .kc .kc-star{top:3px;right:auto;left:46px;width:24px;height:24px}
  .hub[data-view="list"] .kc .kc-star svg{width:13px;height:13px;border:0;border-radius:0}
  .hub[data-view="list"] .kose > .grp{display:flex;align-items:baseline;gap:8px;grid-column:1/-1;margin-top:24px;padding-bottom:7px;border-bottom:1px solid var(--line-strong);
    font-size:12px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;color:var(--foil)}
  .hub[data-view="list"] .kose > .grp:first-child{margin-top:2px}
"""
HUB_BODY = f"""<header class="page">
  <div class="wrap">
    <a class="back" href="index.html">{BACK}Ana sayfa</a>
    <p class="eyebrow">Bilgi köşesi</p>
    <h1>Herkes için kısa rehberler</h1>
    <p class="lede">Sık karşılaşılan ağrılar ve hastalıklar, kendinize iyi bakmanız için pratik egzersizler ve güncel bilimsel gelişmeler. Her yazının kaynağı belirtilmiştir.</p>
    {search_field()}
    {pulse()}
  </div>
</header>
<nav class="tabs" id="tabs" aria-label="Kategoriler">
  <div class="wrap">
    <div class="tabs-s">
      <a href="#agrilar"><span>Ağrılar ve hastalıklar</span><small>{len(AGR)}</small></a>
      <a href="#rehabilitasyon"><span>Evde rehabilitasyon</span><small>{len(REHAB)}</small></a>
      <a href="#kendine-iyi-bak"><span>Kendine iyi bak</span><small>{len(SELF)}</small></a>
      <a href="#tipta-yenilikler"><span>Bilim gündemi</span><small>{len(NEWS)}</small></a>
    </div>
    <div class="view" role="group" aria-label="Görünüm">
      <button type="button" data-v="list" aria-pressed="true" aria-label="Liste görünümü"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6h11M9 12h11M9 18h11M4 6h.01M4 12h.01M4 18h.01"/></svg></button>
      <button type="button" data-v="grid" aria-pressed="false" aria-label="Kart görünümü"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="4" width="6.5" height="6.5" rx="1.5"/><rect x="13.5" y="4" width="6.5" height="6.5" rx="1.5"/><rect x="4" y="13.5" width="6.5" height="6.5" rx="1.5"/><rect x="13.5" y="13.5" width="6.5" height="6.5" rx="1.5"/></svg></button>
    </div>
  </div>
</nav>
<main class="hub" id="hub" data-view="list">
  <section>
    <div class="wrap">
      <div class="view-m"><span>Görünüm</span><div class="view" role="group" aria-label="Görünüm">
      <button type="button" data-v="list" aria-pressed="true" aria-label="Liste görünümü"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6h11M9 12h11M9 18h11M4 6h.01M4 12h.01M4 18h.01"/></svg></button>
      <button type="button" data-v="grid" aria-pressed="false" aria-label="Kart görünümü"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="4" width="6.5" height="6.5" rx="1.5"/><rect x="13.5" y="4" width="6.5" height="6.5" rx="1.5"/><rect x="4" y="13.5" width="6.5" height="6.5" rx="1.5"/><rect x="13.5" y="13.5" width="6.5" height="6.5" rx="1.5"/></svg></button>
      </div></div>
      <div class="cat" id="agrilar">
        <h2>Ağrılar ve hastalıklar</h2>
        <p>Nedir, neden olur, nasıl tedavi edilir? Evde yapılabilecek egzersizler, videolar ve ne zaman hekime başvurmanız gerektiği.</p>
        {region_filter()}
        <div class="kose">
          {AGR_CARDS}
        </div>
      </div>
      <div class="cat" id="rehabilitasyon">
        <h2>Evde rehabilitasyon</h2>
        <p>İnme sonrası toparlanma, düşmeleri önleme, ameliyat ve kırık sonrası süreç, Parkinson hastalığında, MS'te ve kanser tedavisinde egzersiz: evde güvenle yapılabilecek egzersizler ve pratik öneriler.</p>
        <div class="kose">
          {REHAB_CARDS}
        </div>
      </div>
      <div class="cat" id="kendine-iyi-bak">
        <h2>Kendine iyi bak</h2>
        <p>Günlük hayatta kendinize iyi bakmanız için bilimsel kanıta dayanan pratik yöntemler: kendinizi test edebileceğiniz, zamanlayıcıyla birlikte uygulayabileceğiniz ve takip edebileceğiniz küçük araçlarla.</p>
        <div class="kose">
          {SELF_CARDS}
        </div>
      </div>
      <div class="cat" id="tipta-yenilikler">
        <h2>Bilim gündemi</h2>
        <p>Tıbbın öncü alanlarındaki önemli gelişmelerin kısa ve anlaşılır özetleri. Başlığa dokunun, haberin kendisine gidin.</p>
        {headlines("yenilikler.html")}
        <p class="hl-all"><a href="yenilikler.html">Tüm haberleri oku →</a></p>
        <div class="kose">
          {C_IDEA}
        </div>
      </div>
    </div>
  </section>
</main>"""
page("bilgi.html", "Bilgi Köşesi",
     "Bel, boyun, omuz, diz ve ayak ağrıları, kadın sağlığı, evde rehabilitasyon, kendinize iyi bakmanız için pratik egzersizler ve güncel bilimsel gelişmeler: fizyoterapist İhsan Eren'den kaynaklı, kısa ve anlaşılır rehberler.",
     "bilgi.html", HUB_CSS, HUB_BODY, HUB_JS, seo_title="Bilgi Köşesi: Ağrılar, Egzersizler ve Sağlık Rehberleri | İhsan Eren")

open(os.path.join(OUT, "_home_css.txt"), "w", encoding="utf-8").write(HOME_CSS)
open(os.path.join(OUT, "_home_section.txt"), "w", encoding="utf-8").write(HOME_SECTION)
def hx_groups():
    """Girişteki açılır liste: bölgeye göre hastalıklar + evde rehabilitasyon, kısa adlarla."""
    names = dict(REGIONS); out = []
    for r0, _ in REGIONS[1:]:
        cs = [c for c, r in AGR if r.split()[0] == r0]
        if cs:
            out.append((names[r0], cs))
    out.append(("Evde rehabilitasyon", REHAB))
    return "\n".join('        <div class="hx-g"><span>' + n + '</span><div>' +
                     "".join(f'<a class="{_pc(h)}" href="{h}">{PILL[h]}{STAR if h in PREM else ""}</a>' for h, _ in map(_kc_info, cs)) + '</div></div>'
                     for n, cs in out)
SELF_GROUPS = [
    ("Kendinizi ölçün", ["otur-kalk-testi.html", "denge-testi.html", "dort-asamali-denge-testi.html", "sandalye-testi.html", "yurume-hizi-testi.html", "iki-dakika-adim-testi.html", "alti-dakika-yurume-testi.html", "kalk-yuru-testi.html", "dusme-riski-testi.html", "nabiz-olcer.html", "tansiyon-gunlugu.html", "bel-boy-orani.html", "hareket.html", "adim-hedefi.html", "oturma-suresi.html"]),
    ("Zamanlayıcıyla birlikte yapın", ["dizin-12-sirri.html", "duvar-oturusu.html", "pelvik-taban-zamanlayicisi.html", "ic-cekis.html", "sabah-rutini.html", "hareket-atistirmaliklari.html", "guc-devresi.html", "tempolu-yuruyus.html", "yemek-sonrasi-yuruyus.html", "denge-antrenmani.html", "sakatlanmayi-onleyen-isinma.html", "mola-zamanlayicisi.html"]),
    ("Ruh sağlığı için", ["uc-kapi.html", "ruh-sagligi-egzersiz.html", "ruh-hali-olcumu.html", "kas-gevsetme.html", "kucuk-adimlar.html", "dost-molasi.html", "stres.html"]),
    ("Ağrıyla yaşamak", ["agriyi-anlamak.html", "egzersizde-agri.html", "agri-gunlugu.html"]),
    ("Günlük hayat için", ["dustukten-sonra-kalkma.html", "uyku.html", "masa-basi.html", "doga-recetesi.html", "bag-kurmak.html"]),
]
def hx_self():
    """Kendine iyi bak rehberleri, ne işe yaradıklarına göre üç grupta. Listeye yeni eklenen rehber son gruba düşer."""
    hrefs = [h for h, _ in map(_kc_info, SELF)]
    used = {h for _, hs in SELF_GROUPS for h in hs}
    assert used <= set(hrefs), used - set(hrefs)
    groups = [(n, list(hs)) for n, hs in SELF_GROUPS]
    groups[-1][1].extend(h for h in hrefs if h not in used)
    return "\n".join('        <div class="hx-g"><span>' + n + '</span><div>' +
                     "".join(f'<a class="{_pc(h)}" href="{h}">{PILL[h]}{STAR if h in PREM else ""}</a>' for h in hs) + '</div></div>'
                     for n, hs in groups)
HOME_TRIO = f"""    <p class="trio-k">Bilgi köşesi</p>
    <ul class="trio">
      <li><a href="bilgi.html"><b>Hastalık rehberleri</b><span><i>{len(AGR) + len(REHAB)}</i><em>rehber</em></span></a></li>
      <li><a href="bilgi.html#kendine-iyi-bak"><b>Kendine iyi bak</b><span><i>{len(SELF)}</i><em>rehber</em></span></a></li>
      <li><a href="yenilikler.html"><b>Bilim gündemi</b><span><i>{len(NEWS)}</i><em>haber</em></span></a></li>
    </ul>
    <details class="hx">
      <summary><b>Hangi hastalıklar anlatılıyor?</b><span>Bel fıtığı, boyun ağrısı, diz kireçlenmesi, donuk omuz, inme, Parkinson, MS ve daha fazlası.</span><em>Tam liste için dokunun</em></summary>
      <div class="hx-list">
{hx_groups()}
        <a class="hx-all" href="bilgi.html">Tüm rehberler →</a>
      </div>
    </details>
    <details class="hx">
      <summary><b>Kendine iyi bak ne işe yarar?</b><span>Ağrınız olmasa da işinize yarar: kendinizi ölçebileceğiniz kısa testler, zamanlayıcıyla birlikte yapılan egzersizler ve ruh sağlığı, uyku, duruş için öneriler.</span><em>Tam liste için dokunun</em></summary>
      <div class="hx-list">
{hx_self()}
        <a class="hx-all" href="bilgi.html#kendine-iyi-bak">Tüm rehberler →</a>
      </div>
    </details>
"""
open(os.path.join(OUT, "_home_trio.txt"), "w", encoding="utf-8").write(HOME_TRIO)
print("built", MODE, OUT)
