# -*- coding: utf-8 -*-
"""TR <-> EN sayfa eşlemesi, dil seçici ve hreflang bağlantıları."""
SITE = "https://drihsaneren.com/"

# Türkçe dosya adı -> İngilizce dosya adı (en/ klasörü içinde)
EN = {
    "index.html": "index.html",
    "bilgi.html": "health-library.html",
    "stres.html": "stress.html",
    "yenilikler.html": "medical-advances.html",
    "bel-agrisi.html": "low-back-pain.html",
    "bel-fitigi.html": "lumbar-disc-herniation.html",
    "boyun-agrisi.html": "neck-pain.html",
    "boyun-fitigi.html": "cervical-disc-herniation.html",
    "diz-kireclenmesi.html": "knee-osteoarthritis.html",
    "donuk-omuz.html": "frozen-shoulder.html",
    "inme-rehabilitasyonu.html": "stroke-rehabilitation.html",
    "topuk-dikeni.html": "plantar-fasciitis.html",
    "omuz-sikismasi.html": "shoulder-impingement.html",
    "karpal-tunel-sendromu.html": "carpal-tunnel-syndrome.html",
    "dusme-onleme.html": "fall-prevention.html",
    "protez-sonrasi.html": "joint-replacement-rehab.html",
    "masa-basi.html": "desk-work.html",
    "kalca-kireclenmesi.html": "hip-osteoarthritis.html",
    "tenisci-dirsegi.html": "tennis-elbow.html",
    "kemik-erimesi.html": "osteoporosis.html",
    "ayak-bilegi-burkulmasi.html": "ankle-sprain.html",
    "recete.html": "exercise-plan.html",
    "sabah-rutini.html": "morning-routine.html",
    "hareket.html": "how-much-exercise.html",
    "uyku.html": "sleep.html",
    "parkinson.html": "parkinsons-disease.html",
    "kalca-kirigi.html": "hip-fracture-rehab.html",
    "kanser-egzersiz.html": "exercise-and-cancer.html",
    "menisku-yirtigi.html": "meniscus-tear.html",
    "fibromiyalji.html": "fibromyalgia.html",
    "bas-donmesi.html": "vertigo-bppv.html",
    "ankilozan-spondilit.html": "ankylosing-spondylitis.html",
    "diz-onu-agrisi.html": "anterior-knee-pain.html",
    "asil-tendinopatisi.html": "achilles-tendinopathy.html",
    "bas-agrisi.html": "headache.html",
    "skolyoz.html": "scoliosis.html",
    "rotator-manset-yirtigi.html": "rotator-cuff-tear.html",
    "cene-eklemi.html": "jaw-joint-tmd.html",
    "idrar-kacirma.html": "urinary-incontinence.html",
    "gebelikte-bel-agrisi.html": "pregnancy-back-pain.html",
    "dar-kanal.html": "lumbar-spinal-stenosis.html",
    "on-capraz-bag.html": "acl-injury.html",
    "romatoid-artrit.html": "rheumatoid-arthritis.html",
    "surekli-usume.html": "always-feeling-cold.html",
    "titreme.html": "tremor.html",
    "yuz-felci.html": "bells-palsy.html",
    "kalca-yan-agrisi.html": "lateral-hip-pain.html",
    "lenfodem.html": "lymphoedema.html",
    "de-quervain.html": "de-quervains-tenosynovitis.html",
    "diyabetik-noropati.html": "diabetic-neuropathy.html",
    "duztabanlik.html": "flat-feet.html",
    "halluks-valgus.html": "bunions.html",
    "tetik-parmak.html": "trigger-finger.html",
    "golfcu-dirsegi.html": "golfers-elbow.html",
    "guillain-barre.html": "guillain-barre-syndrome.html",
    "omurilik-yaralanmasi.html": "spinal-cord-injury.html",
    "koah.html": "copd-pulmonary-rehabilitation.html",
    "kalp-rehabilitasyonu.html": "cardiac-rehabilitation.html",
    "multipl-skleroz.html": "multiple-sclerosis.html",
    "otur-kalk-testi.html": "sitting-rising-test.html",
    "duvar-oturusu.html": "wall-sit-blood-pressure.html",
    "ic-cekis.html": "cyclic-sighing.html",
    "doga-recetesi.html": "nature-prescription.html",
    "bag-kurmak.html": "social-connection.html",
    "dost-molasi.html": "self-kindness-break.html",
    "nobel-2026.html": "nobel-prizes-2026.html",
}
TR = {v: k for k, v in EN.items()}


def tr_url(fname):
    return SITE if fname == "index.html" else SITE + fname


def en_url(fname):
    e = EN[fname]
    return SITE + "en/" if e == "index.html" else SITE + "en/" + e


def hreflang(fname):
    """Aynı bloğu hem TR hem EN sayfanın <head>'ine koyarız."""
    return (f'<link rel="alternate" hreflang="tr" href="{tr_url(fname)}">\n'
            f'<link rel="alternate" hreflang="en" href="{en_url(fname)}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{tr_url(fname)}">\n')


LANG_CSS = """
  .lang{display:inline-flex;align-items:center;flex:none;gap:2px;padding:2px;border:1px solid var(--line-strong);border-radius:999px;font-size:12px;font-weight:600;letter-spacing:.08em;line-height:1}
  .lang a{display:block;padding:6px 9px;border-radius:999px;color:var(--ink-soft);text-decoration:none}
  .lang a:hover{color:var(--foil)}
  .lang a[aria-current]{background:var(--foil);color:var(--ground)}
  .bar .lang{margin-left:auto}
  .links + .lang{margin-left:0}
  .bar .lang + .cta{margin-left:0}
  @media (max-width:900px){.links + .lang{margin-left:auto}}
  .bar .cta,.links a{white-space:nowrap}
  @media (min-width:901px) and (max-width:1099px){.links a.opt{display:none}}
  @media (max-width:480px){.bar .wrap{gap:10px}.brand{font-size:16px;gap:8px}.bar .cta{padding:8px 11px;font-size:13.5px}
    .lang{padding:0;border:0;gap:0;font-size:11px}.lang a[aria-current]{display:none}
    .lang a{display:grid;place-items:center;width:31px;height:31px;box-sizing:border-box;padding:0;border:1px solid var(--line-strong)}
    .lang a:hover{border-color:var(--foil)}}
  @media (max-width:350px){.brand{font-size:0;gap:0}}
"""


def switcher(fname, lang="tr"):
    """TR sayfada: TR etkin, EN -> en/<slug>. EN sayfada: EN etkin, TR -> ../<dosya>."""
    if lang == "tr":
        tr_href = fname
        en_href = "en/" if fname == "index.html" else "en/" + EN[fname]
        return (f'<div class="lang" role="group" aria-label="Dil seçimi">'
                f'<a href="{tr_href}" lang="tr" hreflang="tr" aria-label="Türkçe" aria-current="true">TR</a>'
                f'<a href="{en_href}" lang="en" hreflang="en" aria-label="English">EN</a></div>')
    tr_href = "../" if fname == "index.html" else "../" + fname
    en_href = EN[fname]
    return (f'<div class="lang" role="group" aria-label="Language">'
            f'<a href="{tr_href}" lang="tr" hreflang="tr" aria-label="Türkçe">TR</a>'
            f'<a href="{en_href}" lang="en" hreflang="en" aria-label="English" aria-current="true">EN</a></div>')
