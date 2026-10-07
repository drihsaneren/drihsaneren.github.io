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

KOSE_PAGES = {"bilgi.html", "duztabanlik.html", "omurilik-yaralanmasi.html", "de-quervain.html", "diyabetik-noropati.html", "kalca-yan-agrisi.html", "lenfodem.html", "yuz-felci.html", "titreme.html", "surekli-usume.html", "romatoid-artrit.html", "kalp-rehabilitasyonu.html", "koah.html", "on-capraz-bag.html", "dost-molasi.html", "stres.html", "donuk-omuz.html", "boyun-agrisi.html", "boyun-fitigi.html", "bel-agrisi.html", "bel-fitigi.html", "diz-kireclenmesi.html", "inme-rehabilitasyonu.html", "topuk-dikeni.html", "omuz-sikismasi.html", "karpal-tunel-sendromu.html", "dusme-onleme.html", "protez-sonrasi.html", "masa-basi.html", "kalca-kireclenmesi.html", "tenisci-dirsegi.html", "kemik-erimesi.html", "ayak-bilegi-burkulmasi.html", "sabah-rutini.html", "hareket.html", "uyku.html", "parkinson.html", "kalca-kirigi.html", "kanser-egzersiz.html", "menisku-yirtigi.html", "fibromiyalji.html", "bas-donmesi.html", "ankilozan-spondilit.html", "diz-onu-agrisi.html", "asil-tendinopatisi.html", "bas-agrisi.html", "skolyoz.html", "rotator-manset-yirtigi.html", "cene-eklemi.html", "idrar-kacirma.html", "gebelikte-bel-agrisi.html", "dar-kanal.html", "multipl-skleroz.html", "otur-kalk-testi.html", "duvar-oturusu.html", "ic-cekis.html", "doga-recetesi.html", "bag-kurmak.html"}
NEWS_PAGES = {"nobel-2026.html"}   # Bilim gündemi'nin özel sayfaları
SELF_PAGES = {"dost-molasi.html", "stres.html", "masa-basi.html", "sabah-rutini.html", "hareket.html", "uyku.html", "otur-kalk-testi.html", "duvar-oturusu.html", "ic-cekis.html", "doga-recetesi.html", "bag-kurmak.html"}
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
    "stres.html": ("Kendine iyi bak", "Stresli anlarda ne yapabilirsiniz?"),
    "masa-basi.html": ("Kendine iyi bak", "Masa başında çalışanlar için"),
    "sabah-rutini.html": ("Kendine iyi bak", "Güne 5 dakikayla başlayın"),
    "hareket.html": ("Kendine iyi bak", "Ne kadar hareket yeterli?"),
    "uyku.html": ("Kendine iyi bak", "İyi uyku için"),
    "otur-kalk-testi.html": ("Kendine iyi bak", "Yere oturup kalkabiliyor musunuz?"),
    "duvar-oturusu.html": ("Kendine iyi bak", "Tansiyon için duvar oturuşu"),
    "ic-cekis.html": ("Kendine iyi bak", "5 dakikalık iç çekiş nefesi"),
    "doga-recetesi.html": ("Kendine iyi bak", "Doğa reçetesi"),
    "bag-kurmak.html": ("Kendine iyi bak", "Sosyal bağ ve sağlık"),
    "dost-molasi.html": ("Kendine iyi bak", "DOST molası"),
    "yenilikler.html": ("Bilim gündemi", "Geleceğin tıbbı, bugün"),
    "nobel-2026.html": ("Bilim gündemi", "2026 Nobel ödülleri"),
}
RELATED = {
    "bel-agrisi.html": ["bel-fitigi.html", "ankilozan-spondilit.html"],
    "bel-fitigi.html": ["bel-agrisi.html", "dar-kanal.html"],
    "diz-kireclenmesi.html": ["menisku-yirtigi.html", "kalca-kireclenmesi.html"],
    "boyun-agrisi.html": ["boyun-fitigi.html", "bas-agrisi.html"],
    "boyun-fitigi.html": ["boyun-agrisi.html", "bel-fitigi.html"],
    "donuk-omuz.html": ["boyun-agrisi.html", "diz-kireclenmesi.html"],
    "stres.html": ["uyku.html", "sabah-rutini.html"],
    "sabah-rutini.html": ["hareket.html", "bel-agrisi.html"],
    "hareket.html": ["sabah-rutini.html", "dusme-onleme.html"],
    "uyku.html": ["stres.html", "sabah-rutini.html"],
    "inme-rehabilitasyonu.html": ["dusme-onleme.html", "parkinson.html", "omurilik-yaralanmasi.html"],
    "parkinson.html": ["dusme-onleme.html", "multipl-skleroz.html"],
    "multipl-skleroz.html": ["dusme-onleme.html", "parkinson.html"],
    "kalca-kirigi.html": ["kemik-erimesi.html", "dusme-onleme.html"],
    "kanser-egzersiz.html": ["lenfodem.html", "hareket.html"],
    "koah.html": ["kalp-rehabilitasyonu.html", "ic-cekis.html"],
    "kalp-rehabilitasyonu.html": ["koah.html", "duvar-oturusu.html"],
    "dusme-onleme.html": ["bas-donmesi.html", "diyabetik-noropati.html"],
    "protez-sonrasi.html": ["diz-kireclenmesi.html", "dusme-onleme.html"],
    "masa-basi.html": ["boyun-agrisi.html", "bel-agrisi.html"],
    "kalca-kireclenmesi.html": ["kalca-yan-agrisi.html", "protez-sonrasi.html"],
    "tenisci-dirsegi.html": ["karpal-tunel-sendromu.html", "masa-basi.html"],
    "kemik-erimesi.html": ["dusme-onleme.html", "kalca-kirigi.html"],
    "ayak-bilegi-burkulmasi.html": ["topuk-dikeni.html", "dusme-onleme.html"],
    "topuk-dikeni.html": ["duztabanlik.html", "asil-tendinopatisi.html"],
    "omuz-sikismasi.html": ["rotator-manset-yirtigi.html", "donuk-omuz.html"],
    "karpal-tunel-sendromu.html": ["de-quervain.html", "boyun-fitigi.html"],
    "yenilikler.html": ["stres.html", "diz-kireclenmesi.html"],
    "nobel-2026.html": ["yenilikler.html", "parkinson.html"],
    "menisku-yirtigi.html": ["diz-kireclenmesi.html", "on-capraz-bag.html"],
    "on-capraz-bag.html": ["menisku-yirtigi.html", "diz-onu-agrisi.html"],
    "romatoid-artrit.html": ["ankilozan-spondilit.html", "karpal-tunel-sendromu.html"],
    "surekli-usume.html": ["titreme.html", "uyku.html"],
    "titreme.html": ["parkinson.html", "surekli-usume.html"],
    "yuz-felci.html": ["inme-rehabilitasyonu.html", "cene-eklemi.html"],
    "kalca-yan-agrisi.html": ["kalca-kireclenmesi.html", "bel-agrisi.html"],
    "lenfodem.html": ["kanser-egzersiz.html", "hareket.html"],
    "de-quervain.html": ["karpal-tunel-sendromu.html", "tenisci-dirsegi.html"],
    "diyabetik-noropati.html": ["dusme-onleme.html", "surekli-usume.html"],
    "duztabanlik.html": ["topuk-dikeni.html", "asil-tendinopatisi.html"],
    "omurilik-yaralanmasi.html": ["inme-rehabilitasyonu.html", "multipl-skleroz.html"],
    "fibromiyalji.html": ["uyku.html", "stres.html"],
    "bas-donmesi.html": ["dusme-onleme.html", "boyun-agrisi.html"],
    "ankilozan-spondilit.html": ["bel-agrisi.html", "boyun-agrisi.html"],
    "diz-onu-agrisi.html": ["diz-kireclenmesi.html", "menisku-yirtigi.html"],
    "asil-tendinopatisi.html": ["topuk-dikeni.html", "ayak-bilegi-burkulmasi.html"],
    "bas-agrisi.html": ["boyun-agrisi.html", "cene-eklemi.html"],
    "skolyoz.html": ["bel-agrisi.html", "masa-basi.html"],
    "rotator-manset-yirtigi.html": ["omuz-sikismasi.html", "donuk-omuz.html"],
    "cene-eklemi.html": ["bas-agrisi.html", "yuz-felci.html"],
    "idrar-kacirma.html": ["gebelikte-bel-agrisi.html", "hareket.html"],
    "gebelikte-bel-agrisi.html": ["idrar-kacirma.html", "bel-agrisi.html"],
    "dar-kanal.html": ["bel-fitigi.html", "bel-agrisi.html"],
    "otur-kalk-testi.html": ["dusme-onleme.html", "hareket.html"],
    "duvar-oturusu.html": ["hareket.html", "otur-kalk-testi.html"],
    "ic-cekis.html": ["stres.html", "uyku.html"],
    "doga-recetesi.html": ["bag-kurmak.html", "stres.html"],
    "bag-kurmak.html": ["doga-recetesi.html", "stres.html"],
    "dost-molasi.html": ["ic-cekis.html", "bag-kurmak.html"],
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
for _p in ("lowback_part.py", "knee_part.py", "stroke_part.py", "heel_part.py", "shoulder_part.py", "cts_part.py", "falls_part.py", "protez_part.py", "desk_part.py", "hip_part.py", "elbow_part.py", "osteo_part.py", "ankle_part.py", "self_part.py", "rehab_part.py", "cond2_part.py", "cond3_part.py", "cond4_part.py", "cond5_part.py", "cond6_part.py", "cond7_part.py", "cond8_part.py", "cond9_part.py", "cond10_part.py", "cond11_part.py", "cond12_part.py", "cond13_part.py", "cond14_part.py", "cond15_part.py", "cond16_part.py", "self2_part.py", "self3_part.py", "nobel_part.py"):
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

NEWS = [
 dict(il=IL_NOBEL, g="beyin", cat="Nobel 2026", feat=True, date="Ekim 2026",
      title="Işık, ayna ve buz: 2026 Nobel ödülleri",
      text="Tıp ödülü, beyin hücrelerini ışıkla çalıştırıp durdurmayı sağlayan optogenetiğin üç öncüsüne; kimya ödülü, ayna görüntüsü moleküllerden yalnızca birini üretmenin yolunu gösteren Henri Kagan ve Kenso Soai'ye; fizik ödülü ise Güney Kutbu'nun buzunda kozmik nötrinoları yakalayan Francis Halzen'e verildi.",
      point="Üçünün de çıkış noktası, o gün hiçbir işe yaramayacak gibi görünen bir meraktı: bir gölet yosunu, hesaba uymayan bir tepkime ve buzun dibinde çakan bir ışık. Üçünü de canlandırmalarla, sade bir dille anlattım.",
      src=[("STAT, 5 Ekim 2026", "https://www.statnews.com/2026/10/05/nobel-prize-medicine-2026-winner-deisseroth-hegemann-nagel/"), ("IceCube, 6 Ekim 2026", "https://icecube.wisc.edu/news/awards/2026/10/francis-halzen-icecube-principal-investigator-wins-2026-physics-nobel-prize/"), ("Forbes, 7 Ekim 2026", "https://www.forbes.com/sites/michaeltnietzel/2026/10/07/the-2026-nobel-prize-in-chemistry-is-awarded-to-henri-kagan-and-kenso-soai/")],
      rel=("Canlandırmalı anlatımı aç", "nobel-2026.html")),
 dict(il=IL_BLOOD, g="tani", cat="Alzheimer", feat=True, date="Eylül 2026",
      title="Alzheimer için kan testleri çoğalıyor",
      text="ABD'de Gıda ve İlaç Dairesi (FDA), Mayıs 2025'ten bu yana beyindeki amiloid ve tau değişikliklerini kandan ölçen dört testi onayladı. Son ikisi Ağustos 2026'da geldi. Bu testler beyin görüntülemesine ya da bel sıvısı alınmasına gerek kalmadan tanıyı kolaylaştırabilir.",
      point="Önemli: Testler yalnızca hafıza şikâyeti olan kişilerde, hekim değerlendirmesinin parçası olarak kullanılmak için onaylandı. Şikâyeti olmayan sağlıklı kişilerde tarama için uygun değiller.",
      src=[("TIME, 22 Eylül 2026", "https://time.com/article/2026/09/22/who-should-get-new-blood-tests-for-alzheimers-disease/")]),
 dict(il=IL_KIDNEY, g="gen", cat="Organ nakli", date="Eylül 2026",
      title="Domuz böbreği, insan böbreğine köprü oldu",
      text="ABD'de son dönem böbrek yetmezliği olan 66 yaşındaki Tim Andrews'a genetiği düzenlenmiş bir domuzdan böbrek nakledildi. Böbrek onu 271 gün diyalizden uzak tuttu; bu, yaşayan bir alıcıda belgelenen en uzun süre. Enfeksiyon nedeniyle bağışıklık baskılayıcı ilaçlar azaltılınca domuz böbreği hasar görüp işlevini yitirdi; Andrews Ocak 2026'da bağışçıdan insan böbreği aldı ve yeni böbrek hemen çalışmaya başladı.",
      point="Organ bekleme listelerinin uzunluğu düşünüldüğünde umut verici bir adım. Ancak şimdilik az sayıda hastadan elde edilen deneyimler var; genetiği düzenlenmiş domuz böbreklerinin güvenliği ve kalıcılığı klinik çalışmalarda araştırılıyor.",
      src=[("The Lancet, 9 Eylül 2026", "https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(26)01295-X/abstract"), ("Mass General Brigham", "https://news.massgeneralbrigham.org/en/pig-kidney-xenotransplant-bridge-to-human-transplant")]),
 dict(il=IL_HD, g="beyin", cat="Huntington", date="Eylül 2026",
      title='Huntington hastalığında ilk gen tedavisi onay kapısında',
      text="Huntington, kalıtsal ve ilerleyici bir beyin hastalığı; hareketi, düşünmeyi ve duygu durumunu etkiliyor ve gidişini yavaşlattığı kanıtlanmış bir tedavisi yok. uniQure'un geliştirdiği AMT-130, MR eşliğinde yapılan tek seferlik bir ameliyatla beynin derinindeki striatum bölgesine veriliyor ve hastalığa yol açan hatalı huntingtin proteininin üretimini azaltmayı hedefliyor. Yüksek dozu alan hastalarda 3. yılda hastalığın ilerlemesi, karşılaştırma grubuna göre %75 daha yavaştı; şirket Eylül 2026'da ABD ve İngiltere'de onay başvurusu yaptı.",
      point="Sonuçlar az sayıda hastaya ve plasebo grubu yerine hastalık kayıtlarından seçilen benzer hastalarla karşılaştırmaya dayanıyor. 29 Eylül'de açıklanan 4. yıl verilerinde ana ölçekteki fark %44'e indi ve istatistiksel olarak anlamlı değildi; günlük işlev ölçeğinde %61'lik yavaşlama sürüyordu. Yüksek dozu alanların %17'sinde beyinde iltihapla ilişkili ciddi yan etki görüldü; bunların hepsi düzeldi.",
      src=[('uniQure, 29 Eylül 2026', 'https://www.globenewswire.com/news-release/2026/09/29/3370692/0/en/uniqure-announces-additional-data-from-ongoing-phase-i-ii-studies-of-ifezuntirgene-inilparvovec-amt-130-in-huntington-s-disease-showing-continued-slowing-of-disease-progression.html'), ('BioPharm International, 2 Eylül 2026', 'https://www.biopharminternational.com/view/uniqure-submits-bla-and-maa-for-amt-130-gene-therapy-in-huntington-s-disease')]),
 dict(il=IL_TAVA, g="beyin", cat="Parkinson", date="Eylül 2026",
      title="Parkinson'da yeni etki biçimli ilaç: tavapadon",
      text="FDA, 28 Eylül 2026'da AbbVie'nin tavapadon (JUVMO) adlı ilacını onayladı. Günde bir kez alınan tablet, beyindeki dopamin reseptörlerinden D1 ve D5'i seçici olarak uyaran ilk ilaç; bugün kullanılan dopamin agonistleri ağırlıklı olarak D2 ve D3 reseptörlerine etki ediyor. Tek başına ya da levodopayla birlikte kullanılabiliyor. Levodopa alan hastalarda, rahatsız edici istemsiz hareketler olmadan iyi geçen “açık” süreyi günde 1,7 saat artırdı; plaseboda artış 0,6 saatti.",
      point='En sık yan etkiler bulantı, baş ağrısı, tat bozukluğu, yorgunluk ve baş dönmesi; ayağa kalkarken tansiyon düşmesi, halüsinasyon ve kumar gibi dürtü kontrol sorunları açısından dikkatli olunmalı. Yeni ilaçlar hareketi kolaylaştırsa da Parkinson hastalığında düzenli egzersiz tedavinin temel parçası olmaya devam ediyor.',
      src=[('AbbVie, 28 Eylül 2026', 'https://news.abbvie.com/2026-09-28-U-S-FDA-Approves-AbbVies-JUVMO-TM-tavapadon-for-Parkinsons-Disease')],
      rel=('Parkinson rehberi', 'parkinson.html')),
 dict(il=IL_OREX, g="beyin", cat="Uyku", date="Ağustos 2026",
      title='Tip 1 narkolepside eksik beyin sinyalinin yerini tutan ilk ilaç',
      text="Tip 1 narkolepside beyinde uyanıklığı düzenleyen oreksin (hipokretin) adlı maddeyi üreten hücreler kaybolur; kişi gün içinde karşı konulamaz uyku ataklarıyla boğuşur, güldüğünde ya da heyecanlandığında kasları aniden gevşeyebilir (katapleksi). FDA, 5 Ağustos 2026'da Takeda'nın oveporekston (Orzeyful) adlı ilacını, eksik oreksin sinyalinin yerini tutan ilk ilaç olarak onayladı. 273 hastalık iki çalışmada gündüz uyanıklığı arttı, uykululuk ve katapleksi atakları belirgin şekilde azaldı.",
      point="FDA'ya göre hastalığın altta yatan biyolojisini etkileyen ilk ilaç. Günde iki kez alınıyor; en sık yan etkiler uykusuzluk, sık idrara çıkma ve tükürük artışı. 18 yaş altında güvenliği ve etkinliği henüz bilinmiyor.",
      src=[('FDA, 5 Ağustos 2026', 'https://www.fda.gov/news-events/press-announcements/fda-approves-first-drug-treat-full-range-narcolepsy-type-1-symptoms')]),
 dict(il=IL_RAS, g="gen", cat="Kanser", feat=True, date="Ağustos 2026",
      title="Pankreas kanserinde RAS'ı hedefleyen ilk ilaç",
      text="Pankreas kanserlerinin %90'dan fazlasında tümörü büyüten RAS genlerinde (çoğunlukla KRAS) mutasyon bulunuyor. Uzun süre ilaçla hedeflenemez sanılan RAS'ın yalnızca tek bir mutasyonunu hedefleyen ilaçlar akciğer ve kalın bağırsak kanserlerinde kullanılıyordu; RAS'ın birçok biçimini birden engelleyen daraksonrasib (Rasonque) ise 26 Ağustos 2026'da FDA onayı aldı. Daha önce tedavi görmüş, yayılmış pankreas kanseri olan 500 hastalık RASolute 302 çalışmasında ortanca yaşam süresi kemoterapiyle 6,7 ay, daraksonrasiple 13,2 ay oldu.",
      point="Günde bir kez tablet olarak alınıyor. En sık yan etkiler döküntü, ishal, ağız yaraları ve bulantı. STAT'a konuşan bir onkolog onu pankreas kanserinde onlarca yılın en önemli gelişmesi olarak niteledi; ilacın ilk basamak tedavide kullanıldığı çalışmalar sürüyor.",
      src=[('FDA, 26 Ağustos 2026', 'https://www.fda.gov/news-events/press-announcements/fda-approves-first-class-targeted-therapy-metastatic-pancreatic-cancer'), ('STAT', 'https://www.statnews.com/2026/08/26/pancreatic-cancer-drug-rasonque-approved/')]),
 dict(il=IL_VACCINE, g="gen", cat="Kanser", date="Ağustos 2026",
      title="Kişiye özel mRNA kanser aşısı ilk kez faz III'te başarılı",
      text="Merck ve Moderna'nın geliştirdiği intismeran, her hastanın tümöründeki mutasyonlara göre ayrı ayrı üretilen bir mRNA aşısı. Ameliyatla tümörü tamamen çıkarılmış evre IIB–IV melanomlu 1.137 hastanın katıldığı INTerpath-001 çalışmasında aşı, bir bağışıklık ilacıyla (pembrolizumab) birlikte verildi ve tek başına ilaca göre hastalığın geri dönmesini ve uzak organlara yayılmasını geciktirdi.",
      point="Ayrıntılı sayılar henüz açıklanmadı; sonuçlar bir tıp kongresinde sunulacak. Önceki faz IIb çalışmasında nüks ya da ölüm riski %49 daha düşük bulunmuştu. Yeni bir güvenlik sorunu görülmedi.",
      src=[("Merck, 19 Ağustos 2026", "https://www.merck.com/news/merck-and-moderna-announce-phase-3-interpath-001-trial-of-intismeran-autogene-plus-keytruda-met-endpoints-of-recurrence-free-survival-rfs-and-distant-metastasis-free-survival-dmfs-in-patient/"), ("STAT", "https://www.statnews.com/2026/08/19/mrna-cancer-vaccine-trial-melanoma-merck-moderna/")]),
 dict(il=IL_PARK, g="beyin", cat="Parkinson", date="Temmuz 2026",
      title="Parkinson'da kök hücreden beyin hücresi nakli",
      text="İsveç'teki Lund Üniversitesi ile İngiltere'deki Cambridge Üniversitesi'nin yürüttüğü STEM-PD çalışmasında, kök hücreden üretilen dopamin salgılayan hücreler orta evre Parkinson hastası 8 kişinin beynine nakledildi. Bir yıl sonra değerlendirilen 7 hastanın 6'sı ilaç dozunu belirgin şekilde azalttı; beyin görüntülemesi nakledilen hücrelerin yaşadığına işaret etti.",
      point="Hücrelere bağlı ciddi bir yan etki görülmedi. Küçük ve erken evre bir çalışma olduğu için etkinin kalıcılığını görmek üzere daha uzun takip ve daha büyük çalışmalar gerekiyor; tedavi henüz rutin kullanımda değil.",
      src=[("Nature Medicine, 9 Temmuz 2026", "https://www.nature.com/articles/s41591-026-04525-0"), ("Parkinson's UK", "https://www.parkinsons.org.uk/news/2026/landmark-european-stem-cell-trial-announces-positive-results")]),
 dict(il=IL_SHUTTLE, g="beyin", cat="Alzheimer", date="Temmuz 2026",
      title="Beyne “mekikle” taşınan ilaç: trontinemab",
      text="Roche'un geliştirdiği trontinemab, kan-beyin engelini bir taşıyıcı sayesinde daha kolay geçmek üzere tasarlandı. Temmuz 2026'daki Alzheimer kongresinde (AAIC) açıklanan erken faz verilerine göre yüksek dozu alan hastaların %92'sinde 28 haftada beyindeki amiloid birikimi eşik değerin altına indi.",
      point="İlaç henüz onaylı değil; büyük faz III çalışmaları sürüyor. Az sayıda hastada beyinde mikro kanama gibi yan etkiler izlendi.",
      src=[("Clinical Trials Arena, 16 Temmuz 2026", "https://www.clinicaltrialsarena.com/news/roche-alzheimers-trontinemab-aaic-26/")]),
 dict(il=IL_LDL, g="kalp", cat="Kolesterol", date="Temmuz 2026",
      title='Kolesterol için ilk PCSK9 hapı',
      text="PCSK9 ilaçları kötü kolesterolü (LDL) güçlü şekilde düşürüyor, ama bugüne kadar yalnızca iğne olarak kullanılabiliyordu. FDA, 17 Temmuz 2026'da Merck'in enlisitid (Lipfendra) adlı ilacını günde bir kez alınan ilk PCSK9 hapı olarak onayladı. Zaten statin kullanan toplam 3.207 kişilik iki çalışmada LDL kolesterol 24. haftada plaseboya göre, kalp-damar hastalığı olan ya da riski yüksek kişilerde %56, ailesel yüksek kolesterolü olanlarda %59 daha fazla düştü.",
      point='Diyet ve egzersize ek olarak kullanılmak üzere onaylandı. Kalp krizi ve inmeyi azaltıp azaltmadığını gösterecek sonuç çalışması henüz tamamlanmadı.',
      src=[('FDA, 17 Temmuz 2026', 'https://www.fda.gov/news-events/press-announcements/fda-approves-first-oral-pcsk9-inhibitor-lower-ldl-cholesterol-adults-high-cholesterol')]),
 dict(il=IL_CART, g="gen", cat="Bağışıklık", date="Haziran 2026",
      title="Ağır lupusta CAR-T hücre tedavisi",
      text="Kanser tedavisinde kullanılan CAR-T yöntemi, bağışıklık sisteminin kendi dokularına saldırdığı hastalıklarda da deneniyor. University College London'ın (UCL) yürüttüğü CARLYSLE çalışmasında ağır lupus hastalarının bağışıklık hücreleri, hastalıktan sorumlu B hücrelerini hedefleyecek şekilde yeniden programlandı. Düşük doz grubundaki 6 hastanın 5'i standart ölçütlere göre remisyona girdi; böbrek tutulumu olanlarda idrarla protein kaybı azaldı.",
      point="Ağır sitokin salınım sendromu ya da sinir sistemi yan etkisi görülmedi; bir hastada gelişen karaciğer hasarı tamamen düzeldi. Sonuçlar 9 hastalık erken bir çalışmaya ait; İngiltere'de daha geniş bir faz II çalışması hasta almaya başladı.",
      src=[("UCL, 12 Haziran 2026", "https://www.ucl.ac.uk/news/2026/jun/car-t-cell-therapy-shows-early-promise-severe-lupus")]),
 dict(il=IL_GAE, g="hareket", cat="Kas-iskelet", date="Haziran 2026",
      title="Diz kireçlenmesi ağrısında damar tıkama (GAE)",
      text="Berlin'deki Charité Üniversite Hastanesi'nde, en az 3 aydır diğer tedavilerle geçmeyen kireçlenme ağrısı olan 194 hastaya genikülat arter embolizasyonu uygulandı: ince bir kateterle dizin çevresindeki küçük damarlara, birkaç saat içinde çözünen mikroküreler verildi. Ağrı 10 üzerinden ortanca 7'den 12. ayda 3'e indi; hastaların %80'inde anlamlı iyileşme görüldü.",
      point="Orta ya da ağır yan etki görülmedi. Ancak kontrol grubu olmayan, tek merkezli bir çalışma ve 12. ayda hastaların %79'una ulaşılabildi. Egzersiz, diz kireçlenmesinde tedavinin temeli olmaya devam ediyor.",
      src=[("Radiology, 16 Haziran 2026 · ScienceDaily", "https://www.sciencedaily.com/releases/2026/06/260616102217.htm")],
      rel=("Diz kireçlenmesi rehberi", "diz-kireclenmesi.html")),
 dict(il=IL_MCED, g="tani", cat="Kanser taraması", date="Haziran 2026",
      title='Tek kan testiyle birçok kanseri erken yakalamak: ilk büyük sonuçlar',
      text="İngiltere'de 50–77 yaş arası, şikâyeti olmayan 142.942 kişinin katıldığı NHS-Galleri çalışmasında katılımcıların yarısına 3 yıl boyunca yılda bir, kanda tümörlerin bıraktığı DNA parçalarını arayan Galleri testi yapıldı. Test grubunda taramayla yakalanan kanser sayısı yaklaşık 4 kat arttı; evre IV (yayılmış) kanser tanıları %14 azaldı ve daha erken evrede yakalanan kanserler arttı.",
      point='Çalışmanın ana hedefi olan evre III–IV kanserlerde anlamlı azalma sağlanamadı. Erken tanının yaşam süresini uzatıp uzatmadığı henüz bilinmiyor. Bu test meme, rahim ağzı ve kolon kanseri taramalarının yerine geçmiyor.',
      src=[('ASCO, Haziran 2026', 'https://www.asco.org/about-asco/press-center/galleri-early-detection-shift-timing-cancer-detection'), ('The ASCO Post', 'https://ascopost.com/news/june-2026/annual-galleri-screening-reduced-stage-iv-cancer-diagnoses-but-missed-primary-endpoint-in-first-randomized-mced-trial/')]),
 dict(il=IL_RETA, g="hareket", cat="Kas-iskelet", date="Haziran 2026",
      title='Kilo verdiren yeni ilaç diz kireçlenmesi ağrısını da azalttı',
      text="Eli Lilly'nin geliştirdiği retatrutid, iştah ve metabolizmayla ilgili üç hormon reseptörünü (GLP-1, GIP ve glukagon) birlikte uyaran, haftada bir yapılan bir iğne. Obezite ve diz kireçlenmesi olan 445 kişilik TRIUMPH-4 çalışmasında en yüksek dozu alanlar 68 haftada vücut ağırlıklarının ortalama %28,7'sini kaybetti; diz ağrısı iki dozda %74–76 azaldı, plasebo grubunda ise %40,3. Haziran 2026'da açıklanan 2.339 kişilik TRIUMPH-1 çalışmasında da diz kireçlenmesi olan katılımcılarda ağrı %73'e kadar azaldı; ancak TRIUMPH-4'te plasebo grubunda da ağrının %40 azaldığını unutmamak gerekir.",
      point="Retatrutid henüz onaylı değil, yalnızca klinik çalışmalarda kullanılıyor; internette satılan “retatrutid” ürünleri yasa dışı ve güvenilmez. Bulantı, ishal ve kusma sık görüldü; en yüksek dozda hastaların yaklaşık %18'i yan etki nedeniyle ilacı bıraktı. Diz kireçlenmesinde kilo vermeyi güçlendirme egzersizleriyle birleştirmek önemini koruyor.",
      src=[('Eli Lilly, 11 Aralık 2025', 'https://investor.lilly.com/news-releases/news-release-details/lillys-triple-agonist-retatrutide-delivered-weight-loss-average'), ('Eli Lilly, 6 Haziran 2026', 'https://investor.lilly.com/news-releases/news-release-details/lillys-triple-agonist-retatrutide-drove-substantial-improvements')],
      rel=('Diz kireçlenmesi rehberi', 'diz-kireclenmesi.html')),
 dict(il=IL_BAX, g="kalp", cat="Tansiyon", date="Mayıs 2026",
      title='Zor kontrol edilen tansiyonda yeni ilaç sınıfı',
      text="Birden fazla ilaca rağmen tansiyonu yüksek kalan hastalarda, vücutta tuz ve su tutulmasına yol açan aldosteron hormonu önemli bir etken. AstraZeneca'nın baksdrostat (Baxfendy) adlı ilacı, aldosteronu üreten enzimi (aldosteron sentaz) seçici olarak engelleyen ilk ilaç olarak Mayıs 2026'da FDA onayı aldı. En az iki tansiyon ilacı kullanan 796 hastalık BaxHTN çalışmasında büyük tansiyon 12 haftada plaseboya göre 8,7–9,8 mmHg daha fazla düştü.",
      point="Başlıca dikkat edilmesi gereken yan etki kanda potasyum yükselmesi: potasyumun 6,0 mmol/L'nin üzerine çıkması yüksek dozda %3, plaseboda %0,4 oranında görüldü; bu yüzden potasyum düzeyi kan tahliliyle izlenir. Tansiyon ilacınızı hekiminize danışmadan değiştirmeyin. İlaçların yanında düzenli egzersizin, özellikle izometrik egzersizlerin de tansiyonu düşürdüğü gösterildi.",
      src=[('New England Journal of Medicine, 2025', 'https://www.nejm.org/doi/full/10.1056/NEJMoa2507109'), ('Pharmacy Times, Mayıs 2026', 'https://www.pharmacytimes.com/view/fda-approves-baxdrostat-as-first-in-class-aldosterone-synthase-inhibitor-for-hypertension')],
      rel=('Tansiyon için duvar oturuşu', 'duvar-oturusu.html')),
 dict(il=IL_ORFO, g="kalp", cat="Obezite", date="Nisan 2026",
      title='Yemek ve su kısıtlaması olmayan ilk GLP-1 zayıflama hapı',
      text="GLP-1 ilaçları şimdiye kadar çoğunlukla haftalık iğne olarak kullanılıyordu; Aralık 2025'te onaylanan ağızdan semaglutidin (Wegovy hap) ise aç karnına alınması gerekiyor. FDA, 1 Nisan 2026'da Eli Lilly'nin orforglipron (Foundayo) adlı hapını, günün herhangi bir saatinde yemek ve su kısıtlaması olmadan alınabilen ilk GLP-1 hapı olarak onayladı. 72 haftalık ATTAIN-1 çalışmasında en yüksek dozu alanlar vücut ağırlıklarının ortalama %12,4'ünü kaybetti; plaseboda kayıp %0,9'du.",
      point='Azaltılmış kalorili beslenme ve daha fazla hareketle birlikte kullanılmak üzere onaylandı. Bulantı, kabızlık ve ishal sık; tiroid tümörü riski, pankreatit ve safra kesesi sorunlarıyla ilgili uyarılar bu ilaç için de geçerli. Kilo verirken kas kaybını azaltmak için güçlendirme egzersizleri önemli.',
      src=[('Eli Lilly, 1 Nisan 2026', 'https://investor.lilly.com/news-releases/news-release-details/fda-approves-lillys-foundayotm-orforglipron-only-glp-1-pill')],
      rel=('Ne kadar hareket yeterli?', 'hareket.html')),
 dict(il=IL_FORK, g="hareket", cat="Kas-iskelet", feat=True, date="Nisan 2026",
      title="Kronik bel ağrısında hangi tedaviyle başlamalı?",
      text="ABD'de 749 kronik bel ağrısı hastasıyla yapılan OPTIMIZE çalışmasında katılımcılar önce 8 hafta fizyoterapi ya da bilişsel davranışçı terapi aldı; yeterli fayda görmeyenler tedavi değiştirdi ya da farkındalık (mindfulness) programına geçti. 10. haftada fizyoterapiyle başlayanların günlük işlevi biraz daha iyiydi; ağrı düzeyi ise gruplar arasında benzerdi.",
      point="Kazanım mütevazı olsa da fizyoterapi makul bir ilk adım olarak öne çıktı. Bir yılın sonunda ikinci aşamadaki seçenekler arasında anlamlı fark çıkmadı; sonradan tedavi değiştirmek ya da eklemek uzun vadeli sonucu pek değiştirmedi.",
      src=[("Annals of Internal Medicine, 20 Nisan 2026", "https://doi.org/10.7326/annals-25-04645")],
      rel=("Bel ağrısı rehberi", "bel-agrisi.html")),
 dict(il=IL_EAR, g="gen", cat="Genetik", date="Nisan 2026",
      title="Doğuştan işitme kaybında gen tedavisi kalıcı görünüyor",
      text="OTOF genindeki bir bozukluk nedeniyle işitme kaybı olan 9 aylık ile 32 yaş arasındaki 42 kişinin iç kulağına, sağlam bir gen kopyası taşıyan zararsız hale getirilmiş bir virüs verildi. Çin'deki sekiz merkezde yapılan çalışmada 2,5 yıllık izlemde katılımcıların %90'ının işitmesi düzeldi, yarısından fazlası normal işitme düzeyine ulaştı. Çocuklar seslere tepki vermekten kısa cümleler kurmaya, hatta şarkı söylemeye kadar ilerledi.",
      point="Ciddi yan etki görülmedi. Etki en çok 18 yaş ve altındakilerde belirgindi; katılımcıların %10'unda yanıt olmadı. Tedavi yalnızca OTOF kaynaklı işitme kaybı içindir ve onay süreci yeni başlıyor.",
      src=[("Nature, 22 Nisan 2026 · Harvard Gazette", "https://news.harvard.edu/gazette/story/2026/04/hearing-breakthrough-holds-up/")]),
 dict(il=IL_BCI, g="beyin", cat="Nöroteknoloji", date="Mart 2026",
      title="Beyin-bilgisayar arayüzüyle evde hızlı yazı",
      text="ABD'deki BrainGate çalışmasında, biri ileri evre ALS, diğeri boyun hizasında omurilik yaralanması olan iki katılımcının beynin hareket bölgesine küçük elektrotlar yerleştirildi. Sistem, parmakları hareket ettirme girişimini klavyedeki harflere çevirdi. Katılımcılardan biri kendi evinde dakikada 22 kelime yazdı ve kelime hatası oranı %1,6'da kaldı; kurulum için yaklaşık 30 cümlelik bir ayar yeterli oldu.",
      point="Konuşamayan ve elini kullanamayan kişiler için iletişimde büyük bir adım. Cihaz henüz yalnızca araştırma amaçlı kullanılıyor ve beyin ameliyatı gerektiriyor.",
      src=[("Nature Neuroscience · Brown Üniversitesi, 16 Mart 2026", "https://www.brown.edu/news/2026-03-16/braingate-rapid-communication")]),
 dict(il=IL_SPINE, g="beyin", cat="Rehabilitasyon", date="2026",
      title="Omurilik yaralanmasında elektrik uyarımı: umut ve gerçek",
      text="ABD'deki Brown Üniversitesi'nin küçük bir çalışmasında tam omurilik yaralanması olan 3 kişiye yaralanmanın altına ve üstüne elektrot yerleştirildi. Alttaki uyarım bacak kaslarını çalıştırırken üstteki uyarım göğüs, kol ya da sırtta hissedilen sinyallerle diz açısı ve adım hakkında geri bildirim verdi; katılımcılar askı ve terapist desteğiyle koşu bandında yürüdü. 48 kişilik uluslararası eWALK çalışmasında ise deri üzerinden verilen uyarım, 12 haftalık yürüme eğitimine ek fayda sağlamadı.",
      point="eWALK'un asıl mesajı: yürüme eğitimi tek başına, uzun süredir omurilik yaralanması olan kişilerde bile yürümeyi belirgin şekilde iyileştirdi. Uyarım teknolojileri umut vadediyor ama henüz rehabilitasyonun yerini tutmuyor.",
      src=[("Brown Üniversitesi, 11 Mart 2026", "https://www.brown.edu/news/2026-03-11/spinal-cord-stimulation"), ("eClinicalMedicine, 2026", "https://www.thelancet.com/journals/eclinm/article/PIIS2589-5370(26)00049-0/fulltext")]),
 dict(il=IL_MAMMO, g="tani", cat="Yapay zekâ", date="Ocak 2026",
      title="Mamografide yapay zekâ desteği: ilk randomize çalışmanın sonuçları",
      text="İsveç'te 105 binden fazla kadının katıldığı MASAI çalışmasında mamografiler ya yapay zekâ desteğiyle ya da standart şekilde iki radyolog tarafından okundu. Yapay zekâ destekli grupta kanserlerin %81'i taramada yakalandı (standart grupta %74); iki tarama arasında ortaya çıkan kanserler %12, agresif alt tipteki kanserler %27 daha azdı. Yanlış alarm oranı iki grupta benzerdi.",
      point="Yapay zekâ radyoloğun yerini almıyor, ona destek oluyor; ara sonuçlarda radyologların okuma yükü %44 azalmıştı. Çalışma tek bir ülkede, tek bir cihaz ve tek bir yazılımla, deneyimli radyologlarla yapıldı.",
      src=[("The Lancet, 29 Ocak 2026", "https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)02464-X/abstract"), ("EurekAlert!", "https://www.eurekalert.org/news-releases/1114399")]),
 dict(il=IL_GAIT, g="hareket", cat="Kas-iskelet", date="Ekim 2025",
      title="Diz kireçlenmesinde yürüyüş şeklini değiştirmek",
      text="ABD'de Utah, New York ve Stanford üniversitelerinden araştırmacıların yürüttüğü, dizin iç kısmında kireçlenmesi olan 68 kişilik bir çalışmada her katılımcı için ayak ucunu 5 ya da 10 derece içe veya dışa çevirmekten hangisinin daha yararlı olacağı hareket analiziyle belirlendi ve 6 seanslık yürüyüş eğitimi verildi. Bir yılda ağrı 10 üzerinden ortalama 2,5 puan azaldı (sahte eğitim grubunda 1,3). MR'da kıkırdak yıkımının daha yavaş ilerlediğine işaret eden bulgular görüldü.",
      point="Bu, “ayak ucunuzu içe çevirin” gibi herkese uyan bir öneri değil; kişiye özel ölçüm ve uzman eşliği gerekiyor. Yöntemin yaygınlaşması için ölçümün basitleştirilmesi gerekiyor.",
      src=[("The Lancet Rheumatology, Ekim 2025", "https://www.thelancet.com/journals/lanrhe/article/PIIS2665-9913(25)00151-1/abstract")],
      rel=("Diz kireçlenmesi rehberi", "diz-kireclenmesi.html")),
 dict(il=IL_RUN, g="hareket", cat="Egzersiz", date="Haziran 2025",
      title="Kolon kanseri sonrası egzersiz hayat kurtarıyor",
      text="6 ülkede, kemoterapisini tamamlamış 889 kolon kanseri hastasıyla yapılan CHALLENGE çalışmasında bir grup 3 yıllık, antrenör desteğiyle kişiye özel bir egzersiz programına katıldı (tempolu yürüyüşten grup derslerine kadar); diğer grup yalnızca sağlık eğitimi aldı. 5 yılda egzersiz grubunun %80'i, diğer grubun %74'ü kanserden arınmış kaldı; 8 yılda hayatta kalma %90'a karşı %83'tü.",
      point="Egzersiz grubunda kanserin geri dönme, yeni kanser ya da ölüm riski %28, ölüm riski %37 daha düşüktü. Egzersizin kanser tedavisinin bir parçası olabileceğini gösteren ilk büyük randomize çalışma.",
      src=[("New England Journal of Medicine, Haziran 2025", "https://www.nejm.org/doi/abs/10.1056/NEJMoa2502760"), ("Oncology Central", "https://www.oncology-central.com/world-first-trial-highlights-survival-benefits-of-exercise-for-colon-cancer/")],
      rel=("Ne kadar hareket yeterli?", "hareket.html")),
 dict(il=IL_ISLET, g="gen", cat="Diyabet", date="Haziran 2025",
      title="Tip 1 diyabette kök hücreden üretilen insülin hücreleri",
      text="Vertex'in geliştirdiği zimislecel, kök hücreden laboratuvarda üretilen ve insülin salgılayan adacık hücrelerinden oluşuyor. Tam doz alan 12 hastanın 10'u bir yılın sonunda insülin iğnesine ihtiyaç duymadı; 12 hastanın tamamında HbA1c %7'nin altına indi ve ağır şeker düşmesi yaşanmadı.",
      point="Hücrelerin reddedilmemesi için bağışıklık baskılayıcı ilaç kullanmak gerekiyor. Çalışmada iki hasta hayatını kaybetti; biri bu ilaçlara bağlı bir enfeksiyon nedeniyle. Faz III çalışmaları sürüyor.",
      src=[("New England Journal of Medicine, Haziran 2025", "https://www.nejm.org/doi/abs/10.1056/NEJMoa2506549"), ("HCPLive", "https://www.hcplive.com/view/zimislecel-enables-insulin-independence-in-10-participants-with-type-1-diabetes")]),
 dict(il=IL_DNA, g="gen", cat="Genetik", date="2025–2026",
      title="Tek bir bebek için tasarlanan gen tedavisi",
      text="ABD'de KJ adlı bir bebekte, vücutta amonyak birikmesine yol açan nadir bir genetik hastalık (CPS1 eksikliği) vardı. Araştırmacılar bebeğin kendi mutasyonunu düzelten kişiye özel bir gen düzenleme tedavisini yaklaşık altı ayda geliştirip uyguladı.",
      point="Çok nadir hastalıklar için “her hastaya özel” tedavi üretmenin mümkün olduğunu gösteren ilk örneklerden biri.",
      src=[("Innovative Genomics Institute, 2026", "https://innovativegenomics.org/news/crispr-clinical-trials-2026/")]),
 dict(il=IL_CRISPR, g="gen", cat="Genetik", feat=True, date="2026",
      title="CRISPR tedavileri klinikte",
      text="Onaylı ilk CRISPR tedavisi Casgevy, orak hücreli anemi ve beta talasemide kullanılıyor. Çalışmalarda orak hücre hastalarının 17'de 16'sı ağrı krizi yaşamadı, talasemi hastalarının 27'de 25'i kan nakline ihtiyaç duymadı. Vücut içinde doğrudan yapılan gen düzenlemesinde de umut verici sonuçlar var.",
      point="Talasemi ve orak hücreli anemi Türkiye'de özellikle Akdeniz bölgesinde sık görülüyor. Tedavi pahalı ve her merkezde uygulanamıyor.",
      src=[("Innovative Genomics Institute, 2026", "https://innovativegenomics.org/news/crispr-clinical-trials-2026/")]),
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
def headlines(pre="", items=None):
    """Haber başlıkları: konu etiketi, başlık ve tarih; her satır haberin kendisine gider."""
    rows = "".join(f'<li><a href="{pre}#{news_id(n)}"><span class="hl-c">{n["cat"]}</span><span class="hl-t">{n["title"]}</span><small>{n["date"]}</small></a></li>'
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
"""
def card(n):
    chip = {"Alzheimer": "chip", "Parkinson": "chip", "Huntington": "chip", "Uyku": "chip", "Nöroteknoloji": "chip", "Genetik": "chip g", "Kanser": "chip g", "Diyabet": "chip g"}.get(n["cat"], "chip o")
    srcs = " · ".join(f'<a href="{u}" target="_blank" rel="noopener">{t}</a>' for t, u in n["src"])
    rel = f'\n    <p class="rel"><a href="{n["rel"][1]}">{n["rel"][0]} →</a></p>' if n.get("rel") else ""
    return f'''<article class="card{' feat' if n.get('feat') else ''}" id="{news_id(n)}" data-g="{n["g"]}">
  <div class="il">{n["il"]}</div>
  <div class="body">
    <div class="tags"><span class="{chip}">{n["cat"]}</span><span>{n["date"]}</span></div>
    <h2>{n["title"]}</h2>
    <p>{n["text"]}</p>
    <p class="point">{n["point"]}</p>
    <p class="src">{"Kaynaklar" if len(n["src"]) > 1 else "Kaynak"}: {srcs}</p>{rel}
  </div>
</article>'''

NEWS_FAQ = [
 ("Alzheimer kan testiyle anlaşılabilir mi?", "ABD'de FDA, Mayıs 2025'ten bu yana beyindeki amiloid ve tau değişikliklerini kandan ölçen dört testi onayladı. Ancak bu testler yalnızca hafıza şikâyeti olan kişilerde, hekim değerlendirmesinin parçası olarak kullanılmak için onaylandı; şikâyeti olmayan sağlıklı kişilerde tarama için uygun değildir."),
 ("Trontinemab onaylı bir Alzheimer ilacı mı?", "Hayır, henüz onaylı değildir; büyük faz III çalışmaları sürmektedir. Erken faz verilerine göre yüksek dozu alan hastaların %92'sinde 28 haftada beyindeki amiloid birikimi eşik değerin altına indi. Az sayıda hastada beyinde mikro kanama gibi yan etkiler izlendi."),
 ("Mamografiyi artık yapay zekâ mı okuyacak?", "Hayır. İsveç'teki MASAI çalışmasında yapay zekâ radyologların yerine değil, onlara destek olarak kullanıldı. Bu düzende kanserlerin daha fazlası taramada yakalandı, iki tarama arasında ortaya çıkan kanserler %12 azaldı ve yanlış alarm oranı artmadı."),
 ("Domuz organları insanlara nakledilebiliyor mu?", "Henüz deneysel. ABD'de bir hastaya nakledilen genetiği düzenlenmiş domuz böbreği onu 271 gün diyalizden uzak tuttu ve ardından insan böbreği nakline köprü oldu. Bu yöntemin güvenliği ve kalıcılığı klinik çalışmalarda araştırılıyor."),
 ("GLP-1 zayıflama ilaçları artık hap olarak da var mı?", "Evet. ABD'de Aralık 2025'te ağızdan semaglutid (Wegovy hap), Nisan 2026'da da yemek ve su kısıtlaması olmadan alınabilen orforglipron (Foundayo) onaylandı. 72 haftalık çalışmada orforglipronun en yüksek dozuyla ortalama kilo kaybı %12,4 oldu. Bu ilaçlar beslenme düzeni ve hareketle birlikte, hekim kontrolünde kullanılır."),
 ("Kanseri kandan erken yakalayan testler kullanıma hazır mı?", "Henüz değil. 142.942 kişilik NHS-Galleri çalışmasında test, taramayla yakalanan kanser sayısını yaklaşık 4 kat artırdı ve evre IV tanıları %14 azalttı; ancak evre III–IV kanserlerde hedeflenen azalma sağlanamadı ve yaşam süresine etkisi henüz bilinmiyor. Bu testler mevcut tarama programlarının yerine geçmez."),
 ("Parkinson hastalığında kök hücre tedavisi var mı?", "Henüz rutin bir tedavi değildir. STEM-PD adlı erken evre çalışmada kök hücreden üretilen dopamin hücreleri 8 hastaya nakledildi; bir yıl sonra değerlendirilen 7 hastanın 6'sı ilaç dozunu belirgin şekilde azalttı ve hücrelere bağlı ciddi yan etki görülmedi. Etkinin kalıcılığını görmek için daha uzun takip ve daha büyük çalışmalar gerekiyor."),
 ("Diz kireçlenmesinde yürüyüş şeklini değiştirmek ağrıyı azaltır mı?", "68 kişilik bir çalışmada kişiye özel belirlenen ayak açısıyla yapılan yürüyüş eğitimi, bir yılda ağrıyı 10 üzerinden ortalama 2,5 puan azalttı; sahte eğitim grubunda azalma 1,3 puandı. Bu herkese uyan bir öneri değildir; kişiye özel ölçüm ve uzman eşliği gerekir."),
 ("Egzersiz kanser tedavisinin bir parçası olabilir mi?", "Kolon kanseri tedavisini tamamlamış 889 hastayla yapılan CHALLENGE çalışmasında 3 yıllık, antrenör destekli egzersiz programına katılanlarda kanserin geri dönme, yeni kanser ya da ölüm riski %28, ölüm riski %37 daha düşüktü. Egzersiz programına başlamadan önce tedavi ekibinizle görüşün."),
 ("Talasemi ve orak hücreli anemi gen tedavisiyle tedavi edilebilir mi?", "Onaylı ilk CRISPR tedavisi Casgevy, orak hücreli anemi ve beta talasemide kullanılmaktadır. Çalışmalarda orak hücre hastalarının 17'de 16'sı ağrı krizi yaşamadı, talasemi hastalarının 27'de 25'i kan nakline ihtiyaç duymadı. Tedavi pahalıdır ve her merkezde uygulanamamaktadır."),
]
NEWS_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Bilim gündemi</p>
    <h1>Geleceğin tıbbı, bugün</h1>
    <p class="lede">Tıbbın öncü alanlarındaki önemli gelişmelerin kısa ve anlaşılır özetleri. Her haberin altında kaynağı var.</p>
    <p class="meta">Son güncelleme: 7 Ekim 2026</p>
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

def KC(href, th, k, title, text, go="Oku →", ext_link=False):
    tgt = ' target="_blank" rel="noopener"' if ext_link else ""
    return f'<a class="kc" href="{href}"{tgt}>{th}<span class="b"><span class="k">{k}</span><h3>{title}</h3><p>{text}</p><span class="go">{go}</span></span></a>'

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
TH_SRT = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M58 134 H262" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><circle cx="112" cy="72" r="12" fill="#8fa476"/><path d="M112 86 V116 M112 94 L94 106 L84 106 M112 94 L130 106 L140 106" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M110 118 L86 126 L118 132 M114 118 L138 126 L106 132" stroke="#d8b25e" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M144 66 Q176 24 200 46" stroke="#e2ab47" stroke-width="3" stroke-dasharray="6 6" stroke-linecap="round" fill="none"/><path d="M190 36 L201 47 L187 52" stroke="#e2ab47" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/><g opacity=".6"><circle cx="226" cy="30" r="12" fill="#8fa476"/><path d="M226 44 V90 M226 90 L216 132 M226 90 L236 132 M226 56 L208 70 M226 56 L244 70" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/></g></svg>"""
TH_WALLSIT = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M104 8 V140" stroke="#ece5cf" stroke-width="6" stroke-linecap="round" opacity=".55"/><path d="M96 140 H200" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><circle cx="122" cy="34" r="12" fill="#8fa476"/><path d="M120 50 V94 M120 60 L140 76 L154 78" stroke="#8fa476" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M120 94 L166 96 L167 136 L180 137" stroke="#d8b25e" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="238" cy="80" r="30" fill="none" stroke="rgba(236,229,207,.18)" stroke-width="6"/><path d="M238 50 A30 30 0 1 1 208 80" fill="none" stroke="#e2ab47" stroke-width="6" stroke-linecap="round"/><path d="M238 80 V62 M230 40 H246" stroke="#e2ab47" stroke-width="4" stroke-linecap="round"/></svg>"""
TH_SIGH = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M52 122 H268" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M60 120 C78 118 92 72 110 60 L124 44 C160 44 214 98 262 118 L262 122 L60 122 Z" fill="rgba(226,171,71,.14)"/><path d="M60 120 C78 118 92 72 110 60 C116 56 118 48 124 44 C160 44 214 98 262 118" fill="none" stroke="#e2ab47" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="110" cy="60" r="6" fill="#8fa476"/><circle cx="124" cy="44" r="6" fill="#8fa476"/><path d="M150 30 H236" stroke="#8fa476" stroke-width="3" stroke-dasharray="2 7" stroke-linecap="round"/><path d="M228 24 L237 30 L228 36" stroke="#8fa476" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>"""
TH_NATURE = """<svg viewBox="0 0 320 150" aria-hidden="true"><circle cx="234" cy="40" r="16" fill="#e2ab47"/><path d="M234 14 V8 M260 40 H266 M252 22 L256 18 M216 22 L212 18" stroke="#e2ab47" stroke-width="3" stroke-linecap="round"/><path d="M104 140 V98 M156 140 V92" stroke="#ece5cf" stroke-width="6" stroke-linecap="round" opacity=".55"/><circle cx="104" cy="80" r="26" fill="#8fa476" opacity=".75"/><circle cx="156" cy="66" r="34" fill="#8fa476"/><path d="M60 140 H270" stroke="rgba(236,229,207,.3)" stroke-width="3" stroke-linecap="round"/><path d="M178 148 Q214 118 272 124" stroke="#d8b25e" stroke-width="4" stroke-dasharray="6 7" stroke-linecap="round" fill="none"/></svg>"""
TH_SOCIAL = """<svg viewBox="0 0 320 150" aria-hidden="true"><path d="M160 46 C142 32 148 14 160 24 C172 14 178 32 160 46Z" fill="#e2ab47"/><circle cx="126" cy="58" r="13" fill="#8fa476"/><circle cx="194" cy="58" r="13" fill="#8fa476"/><path d="M126 74 V112 M126 112 L116 146 M126 112 L136 146 M194 74 V112 M194 112 L184 146 M194 112 L204 146" stroke="#8fa476" stroke-width="7" stroke-linecap="round" fill="none"/><path d="M126 84 L150 96 L160 92 M194 84 L170 96 L160 92" stroke="#d8b25e" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M110 84 L100 104 M210 84 L220 104" stroke="#8fa476" stroke-width="7" stroke-linecap="round"/></svg>"""
C_SRT = KC("otur-kalk-testi.html", TH_SRT, "Kendine iyi bak", "Yere oturup kalkabiliyor musunuz?", "Ellerinizi kullanmadan yere oturup kalkabilmek, 12 yıllık bir araştırmada sağlığın güçlü bir göstergesi çıktı. Puanınızı hesaplayın.")
C_WALLSIT = KC("duvar-oturusu.html", TH_WALLSIT, "Kendine iyi bak", "Tansiyon için duvar oturuşu", "270 çalışmalık analizde tansiyonu en çok düşüren egzersiz türü. Haftada 3 gün, 4 × 2 dakika: zamanlayıcıyla birlikte yapın.")
C_SIGH = KC("ic-cekis.html", TH_SIGH, "Kendine iyi bak", "5 dakikalık iç çekiş nefesi", "Stanford'daki çalışmada ruh hâlini meditasyondan daha çok iyileştiren nefes: iki kez alın, uzun verin.")
C_NATURE = KC("doga-recetesi.html", TH_NATURE, "Kendine iyi bak", "Doğa reçetesi", "Haftada 120 dakika doğa; parça parça da olur. Haftalık doğa takviminiz ve İstanbul'dan öneriler.")
C_SOCIAL = KC("bag-kurmak.html", TH_SOCIAL, "Kendine iyi bak", "Sosyal bağ ve sağlık", "Güçlü sosyal ilişkileri olanların hayatta kalma olasılığı %50 daha yüksek. Şaşırtan bulgular ve her gün için küçük bir öneri.")
TH_DOST = """<svg viewBox="0 0 320 150" aria-hidden="true"><g transform="rotate(-4 160 80)"><rect x="102" y="32" width="116" height="96" rx="8" fill="#ece5cf"/><path d="M122 62 H170 M122 80 H198 M122 98 H184" stroke="#8fa476" stroke-width="6" stroke-linecap="round"/><rect x="138" y="24" width="44" height="14" rx="2" fill="#d8b25e" opacity=".85"/></g><path transform="translate(184 16) scale(.46)" d="M50 86 C22 64 8 46 8 30 C8 16 19 7 31 7 C39 7 46 12 50 20 C54 12 61 7 69 7 C81 7 92 16 92 30 C92 46 78 64 50 86Z" fill="#e2ab47"/></svg>"""
C_DOST = KC("dost-molasi.html", TH_DOST, "Kendine iyi bak", "DOST molası", "Zor bir günde kendinize dost olmanın dört adımı: dur, omuzlarını bırak, seslen, teşekkür et. Beş dakikada kendinize kısa bir not yazın.")
REGIONS = [("tum", "Tümü"), ("bel", "Bel ve sırt"), ("boyun", "Boyun, baş ve çene"), ("omuz", "Omuz, kol ve el"),
           ("diz", "Kalça ve diz"), ("ayak", "Ayak ve ayak bileği"), ("kadin", "Kadın sağlığı"), ("genel", "Tüm vücut")]
AGR = [(C_BACK, "bel"), (C_SCIATICA, "bel"), (C_LS, "bel"), (C_AS, "bel"), (C_SCOLIOSIS, "bel"),
       (C_NECK, "boyun"), (C_HERNIA, "boyun"), (C_HEADACHE, "boyun"), (C_TMJ, "boyun"), (C_VERTIGO, "boyun"),
       (C_SHOULDER, "omuz"), (C_IMPINGE, "omuz"), (C_RC, "omuz"), (C_CTS, "omuz"), (C_ELBOW, "omuz"), (C_DQ, "omuz"),
       (C_KNEE, "diz"), (C_MENISCUS, "diz"), (C_ACL, "diz"), (C_PFP, "diz"), (C_HIP, "diz"), (C_GTPS, "diz"),
       (C_HEEL, "ayak"), (C_ACHILLES, "ayak"), (C_ANKLE, "ayak"), (C_DN, "ayak"), (C_FLAT, "ayak"),
       (C_UI, "kadin"), (C_PREG, "kadin bel"), (C_OSTEO, "genel"), (C_FIBRO, "genel"), (C_RA, "genel"), (C_COLD, "genel"), (C_TREMOR, "genel"), (C_FACE, "genel")]
def region_filter():
    cnt = {r: sum(1 for _, rr in AGR if r in rr.split()) for r, _ in REGIONS}
    cnt["tum"] = len(AGR)
    return ('<div class="filt" role="group" aria-label="Bölgeye göre süz">' +
            "".join(f'<button type="button" data-f="{r}" aria-pressed="{"true" if r == "tum" else "false"}"><span>{t}</span><small>{cnt[r]}</small></button>' for r, t in REGIONS) +
            '</div>')
REHAB = [C_FALLS, C_PROSTH, C_STROKE, C_SCI, C_HIPFX, C_PARK, C_MS, C_ONCO, C_LYMPH, C_COPD, C_CARDIAC]
SELF = [C_DOST, C_SRT, C_WALLSIT, C_SIGH, C_NATURE, C_SOCIAL, C_MORNING, C_MOVE, C_SLEEP, C_STRES, C_DESK]
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
    "bel-agrisi.html": "Bel ağrısı", "bel-fitigi.html": "Bel fıtığı", "dar-kanal.html": "Dar kanal", "on-capraz-bag.html": "Ön çapraz bağ", "romatoid-artrit.html": "Romatoid artrit", "yuz-felci.html": "Yüz felci", "kalca-yan-agrisi.html": "Kalça yan ağrısı", "lenfodem.html": "Lenfödem", "de-quervain.html": "De Quervain", "duztabanlik.html": "Düztabanlık", "omurilik-yaralanmasi.html": "Omurilik yaralanması", "diyabetik-noropati.html": "Diyabetik nöropati", "surekli-usume.html": "Sürekli üşüme", "titreme.html": "Titreme", "boyun-agrisi.html": "Boyun ağrısı",
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
    "otur-kalk-testi.html": "Otur-kalk testi", "duvar-oturusu.html": "Tansiyon için duvar oturuşu", "ic-cekis.html": "İç çekiş nefesi",
    "doga-recetesi.html": "Doğa reçetesi", "bag-kurmak.html": "Sosyal bağ", "dost-molasi.html": "DOST molası", "stres.html": "Stres",
}
def pill_group(label, anchor, cards):
    pills = "".join(f'<a class="pill" href="{h}">{PILL[h]}</a>' for h, _ in map(_kc_info, cards))
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
  // liste / kart görünümü (seçim bu tarayıcıda hatırlanır)
  var vb = document.querySelectorAll('.view button');
  function setView(v, user){
    hub.setAttribute('data-view', v);
    [].forEach.call(vb, function(b){ b.setAttribute('aria-pressed', b.getAttribute('data-v') === v ? 'true' : 'false'); });
    if (!user) return;
    try { localStorage.setItem('bk-view', v); } catch (e) {}
    var el = cur && document.getElementById(cur);
    if (el && tabs.getBoundingClientRect().top <= (top ? top.offsetHeight : 0) + 2) el.scrollIntoView();
  }
  var v0 = null; try { v0 = localStorage.getItem('bk-view'); } catch (e) {}
  if (v0 === 'grid' || v0 === 'list') setView(v0, false);
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
                     "".join(f'<a class="pill" href="{h}">{PILL[h]}</a>' for h, _ in map(_kc_info, cs)) + '</div></div>'
                     for n, cs in out)
SELF_GROUPS = [
    ("Kendinizi ölçün", ["otur-kalk-testi.html", "hareket.html"]),
    ("Zamanlayıcıyla birlikte yapın", ["duvar-oturusu.html", "ic-cekis.html", "sabah-rutini.html"]),
    ("Günlük hayat için", ["dost-molasi.html", "uyku.html", "stres.html", "masa-basi.html", "doga-recetesi.html", "bag-kurmak.html"]),
]
def hx_self():
    """Kendine iyi bak rehberleri, ne işe yaradıklarına göre üç grupta. Listeye yeni eklenen rehber son gruba düşer."""
    hrefs = [h for h, _ in map(_kc_info, SELF)]
    used = {h for _, hs in SELF_GROUPS for h in hs}
    assert used <= set(hrefs), used - set(hrefs)
    groups = [(n, list(hs)) for n, hs in SELF_GROUPS]
    groups[-1][1].extend(h for h in hrefs if h not in used)
    return "\n".join('        <div class="hx-g"><span>' + n + '</span><div>' +
                     "".join(f'<a class="pill" href="{h}">{PILL[h]}</a>' for h in hs) + '</div></div>'
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
      <summary><b>Kendine iyi bak ne işe yarar?</b><span>Ağrınız olmasa da işinize yarar: kendinizi ölçebileceğiniz kısa testler, zamanlayıcıyla birlikte yapılan egzersizler ve uyku, stres, duruş için öneriler.</span><em>Tam liste için dokunun</em></summary>
      <div class="hx-list">
{hx_self()}
        <a class="hx-all" href="bilgi.html#kendine-iyi-bak">Tüm rehberler →</a>
      </div>
    </details>
"""
open(os.path.join(OUT, "_home_trio.txt"), "w", encoding="utf-8").write(HOME_TRIO)
print("built", MODE, OUT)
