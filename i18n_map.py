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
    "multipl-skleroz.html": "multiple-sclerosis.html",
    "otur-kalk-testi.html": "sitting-rising-test.html",
    "duvar-oturusu.html": "wall-sit-blood-pressure.html",
    "ic-cekis.html": "cyclic-sighing.html",
    "doga-recetesi.html": "nature-prescription.html",
    "bag-kurmak.html": "social-connection.html",
}
# Türkçe dosya adı -> Almanca dosya adı (de/ klasörü içinde)
DE = {
    "index.html": "index.html",
    "bilgi.html": "ratgeber.html",
    "stres.html": "stress.html",
    "yenilikler.html": "wissenschaft-aktuell.html",
    "bel-agrisi.html": "rueckenschmerzen.html",
    "bel-fitigi.html": "bandscheibenvorfall-lws.html",
    "boyun-agrisi.html": "nackenschmerzen.html",
    "boyun-fitigi.html": "bandscheibenvorfall-hws.html",
    "diz-kireclenmesi.html": "kniearthrose.html",
    "donuk-omuz.html": "schultersteife.html",
    "inme-rehabilitasyonu.html": "schlaganfall-rehabilitation.html",
    "topuk-dikeni.html": "plantarfasziitis.html",
    "omuz-sikismasi.html": "schulter-impingement.html",
    "karpal-tunel-sendromu.html": "karpaltunnelsyndrom.html",
    "dusme-onleme.html": "sturzpraevention.html",
    "protez-sonrasi.html": "nach-gelenkersatz.html",
    "masa-basi.html": "bueroarbeit.html",
    "kalca-kireclenmesi.html": "hueftarthrose.html",
    "tenisci-dirsegi.html": "tennisellenbogen.html",
    "kemik-erimesi.html": "osteoporose.html",
    "ayak-bilegi-burkulmasi.html": "sprunggelenk-verstauchung.html",
    "recete.html": "uebungsplan.html",
    "sabah-rutini.html": "morgenroutine.html",
    "hareket.html": "wie-viel-bewegung.html",
    "uyku.html": "schlaf.html",
    "parkinson.html": "parkinson.html",
    "kalca-kirigi.html": "hueftfraktur-rehabilitation.html",
    "kanser-egzersiz.html": "bewegung-und-krebs.html",
    "menisku-yirtigi.html": "meniskusriss.html",
    "fibromiyalji.html": "fibromyalgie.html",
    "bas-donmesi.html": "lagerungsschwindel.html",
    "ankilozan-spondilit.html": "morbus-bechterew.html",
    "diz-onu-agrisi.html": "vorderer-knieschmerz.html",
    "asil-tendinopatisi.html": "achillessehnen-tendinopathie.html",
    "bas-agrisi.html": "kopfschmerzen.html",
    "skolyoz.html": "skoliose.html",
    "rotator-manset-yirtigi.html": "rotatorenmanschettenriss.html",
    "cene-eklemi.html": "kiefergelenk-cmd.html",
    "idrar-kacirma.html": "harninkontinenz.html",
    "gebelikte-bel-agrisi.html": "rueckenschmerzen-schwangerschaft.html",
    "dar-kanal.html": "spinalkanalstenose.html",
    "multipl-skleroz.html": "multiple-sklerose.html",
    "otur-kalk-testi.html": "sitz-steh-test.html",
    "duvar-oturusu.html": "wandsitzen-blutdruck.html",
    "ic-cekis.html": "zyklisches-seufzen.html",
    "doga-recetesi.html": "natur-auf-rezept.html",
    "bag-kurmak.html": "soziale-verbundenheit.html",
}
assert set(DE) == set(EN), set(DE) ^ set(EN)
assert len(set(DE.values())) == len(DE)
TR = {v: k for k, v in EN.items()}
MAPS = {"en": EN, "de": DE}          # yabancı diller: klasör adı = dil kodu
LANGS = ("tr", "en", "de")
HTML_LOCALE = {"tr": "tr_TR", "en": "en_GB", "de": "de_DE"}


def tr_url(fname):
    return SITE if fname == "index.html" else SITE + fname


def lang_url(fname, lang):
    if lang == "tr":
        return tr_url(fname)
    e = MAPS[lang][fname]
    return SITE + lang + "/" if e == "index.html" else SITE + lang + "/" + e


def en_url(fname):
    return lang_url(fname, "en")


def hreflang(fname):
    """Aynı bloğu her dildeki sayfanın <head>'ine koyarız."""
    return ("".join(f'<link rel="alternate" hreflang="{l}" href="{lang_url(fname, l)}">\n' for l in LANGS)
            + f'<link rel="alternate" hreflang="x-default" href="{tr_url(fname)}">\n')


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
    .lang{padding:0;border:0;gap:4px;font-size:11px}.lang a[aria-current]{display:none}
    .lang a{display:grid;place-items:center;width:31px;height:31px;box-sizing:border-box;padding:0;border:1px solid var(--line-strong)}
    .lang a:hover{border-color:var(--foil)}}
  @media (max-width:350px){.brand{font-size:0;gap:0}}
"""


def switcher(fname, lang="tr"):
    """Dil seçici. `lang` dilindeki sayfadan öbür dillere göreli bağlantılar; etkin dil işaretli."""
    def href(to):
        if to == "tr":
            target = "" if fname == "index.html" else fname
            return (target or "index.html") if lang == "tr" else "../" + target
        page = MAPS[to][fname]
        target = "" if page == "index.html" else page
        if to == lang:
            return page
        return ("" if lang == "tr" else "../") + to + "/" + target
    label = {"tr": "Dil seçimi", "en": "Language", "de": "Sprache"}[lang]
    name = {"tr": "Türkçe", "en": "English", "de": "Deutsch"}
    links = "".join(f'<a href="{href(l)}" lang="{l}" hreflang="{l}" aria-label="{name[l]}"' + (' aria-current="true"' if l == lang else "") + f'>{l.upper()}</a>'
                    for l in LANGS)
    return f'<div class="lang" role="group" aria-label="{label}">{links}</div>'
