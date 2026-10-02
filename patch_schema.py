# -*- coding: utf-8 -*-
import re
def sub1(s, old, new, label):
    assert s.count(old) == 1, (label, s.count(old))
    return s.replace(old, new)

# ---------------------------------------------------------------- neck_part.py
n = open("neck_part.py", encoding="utf-8").read()
faq_css_block = n[n.index("  .faq{max-width:820px"):n.index("  .callout{")]
n = sub1(n, faq_css_block, "", "neck faq css")
n = sub1(n, '''def faq(items):
    return '<div class="faq">\\n' + "\\n".join(
        f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + '\\n      </div>'
''', "", "neck faq def")
# boyun ağrısı SSS listesi -> değişken
i = n.index('("Boyun ağrısı ne kadar sürer?"'); j = n.index("      ])}", i)
agri_items = n[i:j]
n = n[:i-len("{faq([\n        ")] + "{faq(BOYUN_AGRI_FAQ)}" + n[j+len("      ])}"):]
i = n.index('("Boyun fıtığı kendiliğinden geçer mi?"'); j = n.index("      ])}", i)
fitik_items = n[i:j]
n = n[:i-len("{faq([\n        ")] + "{faq(BOYUN_FITIK_FAQ)}" + n[j+len("      ])}"):]
def as_list(name, items):
    lines = [l.strip() for l in items.strip().splitlines()]
    return name + " = [\n" + "\n".join(" " + l for l in lines) + "\n]\n"
# listeleri ilk gövde tanımından önce koy
anchor = "AGRI_BODY = f'''"
assert n.count(anchor) == 1
n = n.replace(anchor, as_list("BOYUN_AGRI_FAQ", agri_items) + anchor)
anchor = "FITIK_BODY = f'''"
assert n.count(anchor) == 1
n = n.replace(anchor, as_list("BOYUN_FITIK_FAQ", fitik_items) + anchor)
n = sub1(n, 'condition="Boyun ağrısı")',
         'condition="Boyun ağrısı", about=cond("Boyun ağrısı", "neck-pain"),\n     faq_items=pick(BOYUN_AGRI_FAQ, 0, 4, 3, 5))', "neck page")
n = sub1(n, 'condition="Boyun fıtığı (servikal disk hernisi)")',
         'condition="Boyun fıtığı (servikal disk hernisi)", about=cond("Boyun fıtığı (servikal disk hernisi)", "cervical-disc-herniation"),\n     faq_items=pick(BOYUN_FITIK_FAQ, 0, 1, 2, 3))', "fitik page")
open("neck_part.py", "w", encoding="utf-8").write(n)

# ---------------------------------------------------------------- lowback / knee
l = open("lowback_part.py", encoding="utf-8").read()
l = sub1(l, 'condition="Bel ağrısı")',
         'condition="Bel ağrısı", about=cond("Bel ağrısı", "low-back-pain"),\n     faq_items=pick(BEL_FAQ, 0, 2, 1, 4))', "bel page")
l = sub1(l, 'condition="Bel fıtığı (lomber disk hernisi)")',
         'condition="Bel fıtığı (lomber disk hernisi)",\n     faq_items=pick(FITIK_FAQ2, 0, 1, 3, 4))', "belf page")
open("lowback_part.py", "w", encoding="utf-8").write(l)
k = open("knee_part.py", encoding="utf-8").read()
k = sub1(k, 'condition="Diz kireçlenmesi (osteoartrit)")',
         'condition="Diz kireçlenmesi (osteoartrit)", about=cond("Diz kireçlenmesi (osteoartrit)", "knee-osteoarthritis"),\n     faq_items=pick(KNEE_FAQ, 0, 3, 4, 2))', "knee page")
open("knee_part.py", "w", encoding="utf-8").write(k)

# ---------------------------------------------------------------- build_pages.py
b = open("build_pages.py", encoding="utf-8").read()
helpers = '''UPDATED = "28 Eylül 2026"

# ------------------------------------------------------------------ SSS + yapısal veri
import json as _json, re as _re, html as _html
FAQ_CSS = """
''' + faq_css_block + '''"""
def faq(items):
    return '<div class="faq">\\n' + "\\n".join(
        f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + '\\n      </div>'
def pick(items, *idx):
    return [items[i] for i in idx]
def _plain(s):
    return _re.sub(r"\\s+", " ", _html.unescape(_re.sub(r"<[^>]+>", "", s))).strip()
HOME = "https://drihsaneren.com/"
AUTHOR_ID = HOME + "#ihsan-eren"
AUTHOR = {"@type": "Person", "@id": AUTHOR_ID, "name": "İhsan Eren", "url": HOME,
          "jobTitle": ["Fizyoterapist", "İntörn Tıp Doktoru"]}
def cond(name, home_id=None):
    d = {"@type": "MedicalCondition", "name": name}
    if home_id: d["@id"] = HOME + "#" + home_id
    return d
def ld(obj):
    return ('<script type="application/ld+json">\\n'
            + _json.dumps(obj, ensure_ascii=False, indent=2).replace("</", "<\\\\/")
            + '\\n</script>\\n')
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
'''
b = sub1(b, 'UPDATED = "28 Eylül 2026"\n', helpers, "helpers")

# page(): eski tek satırlık şemayı kaldır, </head> öncesine yenisini koy
old_ld = b[b.index("        if condition:\n            seo += ('<script type=\"application/ld+json\">"):b.index("    html = f'''<!doctype html>")]
b = sub1(b, old_ld, "", "old ld")
b = sub1(b, 'def page(fname, title, desc, current, head_extra_css, body, script="", seo_title=None, condition=None):\n    full_title = seo_title or f"{title} | İhsan Eren"\n',
         'def page(fname, title, desc, current, head_extra_css, body, script="", seo_title=None, condition=None, about=None, faq_items=None):\n    full_title = seo_title or f"{title} | İhsan Eren"\n'
         '    ldj = ""\n'
         '    if MODE == "github" and (condition or about):\n'
         '        ldj = schema(fname, full_title, desc, about if about is not None else cond(condition), faq_items)\n'
         '    faq_css = FAQ_CSS if \'<div class="faq">\' in body else ""\n', "page sig")
b = sub1(b, "  {FONTFACE}{CSS}{FAB_CSS}{head_extra_css}\n</style>\n</head>",
         "  {FONTFACE}{CSS}{FAB_CSS}{faq_css}{head_extra_css}\n</style>\n{ldj}</head>", "head tpl")

# --- Stres: görünür SSS
STRES_DEF = '''STRES_HELP = ("Ne zaman destek almalı?", "Stres, kaygı ya da çökkünlük haftalardır uykunuzu, işinizi veya ilişkilerinizi etkiliyorsa bir hekime ya da ruh sağlığı uzmanına başvurun. Kendinize zarar verme düşünceleriniz varsa hemen <strong>112</strong>'yi arayın.")
STRES_FAQ = [
 ("Stres anında nefes egzersizi nasıl yapılır?", "Rahat bir yere oturun ve omuzlarınızı bırakın. Burnunuzdan 4 saniye nefes alın, 6 saniyede yavaşça verin. Bir tur 10 saniye sürer; 6 tur yaklaşık 1 dakikadır. Nefesi yavaşlatmak bedenin sakinleşmesine yardım eder."),
 ("Kutu nefesi ve 4-7-8 nefesi nasıl yapılır?", "Kutu nefesinde 4 saniye nefes alın, 4 saniye tutun, 4 saniye verin ve 4 saniye tutun. 4-7-8 tekniğinde burnunuzdan 4 saniye alın, 7 saniye tutun ve dudaklarınız hafif aralık, 8 saniyede verin. Tutma aşamalarını zorlamadan yapın; ciddi kalp ya da akciğer hastalığınız varsa tutmalı teknikleri doktorunuza danışın."),
 ("Dünya Sağlık Örgütü'nün stres rehberindeki beş beceri nedir?", "Ayağınızı yere basmak, zor düşüncelerden sıyrılmak, değerlerinize göre davranmak, kendinize nazik olmak ve duygulara yer açmaktır. Amaç stresi tamamen yok etmek değil, zor duygular varken de sizin için önemli olana dönebilmektir."),
]
'''
b = sub1(b, "STRES_BODY = f'''", STRES_DEF + "STRES_BODY = f'''", "stres def")
b = sub1(b, '''    </div>
  </section>

  <section id="kaynaklar">''', '''    </div>
  </section>

  <section id="sss">
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(STRES_FAQ)}
    </div>
  </section>

  <section id="kaynaklar">''', "stres sss")
old_box = b[b.index('<div class="note warn"><strong>Ne zaman destek almalı?</strong>'):]
old_box = old_box[:old_box.index("</div>") + 6]
b = sub1(b, old_box, '<div class="note warn"><strong>{STRES_HELP[0]}</strong> {STRES_HELP[1]}</div>', "stres box")
b = sub1(b, '''     "stres.html", STRES_CSS, STRES_BODY, STRES_JS,''',
            '''     "stres.html", STRES_CSS, STRES_BODY, STRES_JS, about=cond("Stres"), faq_items=STRES_FAQ + [STRES_HELP],''', "stres page")

# --- Donuk omuz: görünür SSS
OMUZ_DEF = '''OMUZ_FAQ = [
 ("Donuk omuz kendiliğinden geçer mi?", "Çoğu zaman kendi seyrinde düzelir ama bu aylar, hatta yıllar sürebilir; hastalığın tipik süresi 1–3 yıldır. Bazı kişilerde hafif kısıtlılık uzun süre kalabilir. Doğru egzersiz ve tedaviyle bu süreci daha rahat geçirmek mümkündür."),
 ("Ağrılı omzumu hareket ettirmeli miyim?", "Evet, ama zorlamadan. Ağrılı evrede ağrısız aralıkta nazik hareketler, katılaşma evresinde germe ve eklem mobilizasyonu öne çıkar. Egzersizler hafif bir gerginlik hissi verecek kadar yapılır, keskin ağrıya kadar zorlanmaz."),
 ("Donuk omuz için MR gerekir mi?", "Tanı çoğunlukla muayeneyle konur: omuz hem sizin kaldırdığınızda hem de başkası kaldırdığında aynı şekilde kısıtlıdır. Röntgen, ultrason veya MR tanı için şart değildir ama kireçlenme ya da yırtık gibi başka nedenleri dışlamak için istenebilir."),
 ("Kortizon iğnesi işe yarar mı?", "Eklem içi kortizon iğnesi özellikle erken, ağrılı evrede ağrıyı birkaç hafta içinde belirgin azaltabilir. Etkisi daha çok kısa vadelidir ve hekim kararıyla yapılır. Tedavinin temeli ise fizyoterapi ve düzenli egzersizdir."),
]
'''
b = sub1(b, "OMUZ_BODY = f'''", OMUZ_DEF + "OMUZ_BODY = f'''", "omuz def")
b = sub1(b, '''      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Omuz ağrısı her zaman donuk omuz değildir.''', '''      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
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
      <p class="soft">Omuz ağrısı her zaman donuk omuz değildir.''', "omuz sss")
b = sub1(b, 'condition="Donuk omuz (adeziv kapsülit)")',
         'condition="Donuk omuz (adeziv kapsülit)", about=cond("Donuk omuz (adeziv kapsülit)", "frozen-shoulder"),\n     faq_items=OMUZ_FAQ)', "omuz page")

# --- Yenilikler: görünür SSS
NEWS_DEF = '''NEWS_FAQ = [
 ("Alzheimer kan testiyle anlaşılabilir mi?", "ABD'de FDA, Mayıs 2025'ten bu yana beyindeki amiloid ve tau değişikliklerini kandan ölçen dört testi onayladı. Ancak bu testler yalnızca hafıza şikâyeti olan kişilerde, hekim değerlendirmesinin parçası olarak kullanılmak için onaylandı; şikâyeti olmayan sağlıklı kişilerde tarama için uygun değildir."),
 ("Trontinemab onaylı bir Alzheimer ilacı mı?", "Hayır, henüz onaylı değildir; büyük faz III çalışmaları sürmektedir. Erken faz verilerine göre yüksek dozu alan hastaların %92'sinde 28 haftada beyindeki amiloid birikimi eşik değerin altına indi. Az sayıda hastada beyinde mikro kanama gibi yan etkiler izlendi."),
 ("Talasemi ve orak hücreli anemi gen tedavisiyle tedavi edilebilir mi?", "Onaylı ilk CRISPR tedavisi Casgevy, orak hücreli anemi ve beta talasemide kullanılmaktadır. Çalışmalarda orak hücre hastalarının 17'de 16'sı ağrı krizi yaşamadı, talasemi hastalarının 27'de 25'i kan nakline ihtiyaç duymadı. Tedavi pahalıdır ve her merkezde uygulanamamaktadır."),
]
'''
b = sub1(b, "NEWS_BODY = f'''", NEWS_DEF + "NEWS_BODY = f'''", "news def")
b = sub1(b, '''{"".join(card(n) for n in NEWS)}
      </div>
      <div class="note" style="margin-top:28px">''', '''{"".join(card(n) for n in NEWS)}
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(NEWS_FAQ)}
      <div class="note" style="margin-top:28px">''', "news sss")
b = sub1(b, '''     "yenilikler.html", NEWS_CSS, NEWS_BODY,
     seo_title="Geleceğin Tıbbı: Güncel Bilimsel Gelişmeler | İhsan Eren")''',
            '''     "yenilikler.html", NEWS_CSS, NEWS_BODY,
     seo_title="Geleceğin Tıbbı: Güncel Bilimsel Gelişmeler | İhsan Eren",
     about=[cond("Alzheimer hastalığı"), cond("CPS1 eksikliği"), cond("Orak hücreli anemi"), cond("Beta talasemi")],
     faq_items=NEWS_FAQ)''', "news page")
open("build_pages.py", "w", encoding="utf-8").write(b)
print("patched")
