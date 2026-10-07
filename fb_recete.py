# -*- coding: utf-8 -*-
# Örnek egzersiz reçetesi (recete.html): beyaz/turkuaz tasarım yerine sitenin koyu yeşil-altın
# tasarımı; masaüstünde iki sütun kart, telefonda tek sütun; yazdırınca yine beyaz kâğıt.
import re
import os
S = os.path.dirname(os.path.abspath(__file__)) + "/"
R = os.environ.get("REPO", "/home/claude/drihsaneren.github.io") + "/"
s = open(S + "recete.orig.html", encoding="utf-8").read()


def rep(old, new, cnt=1):
    global s
    assert s.count(old) == cnt, (old[:80], s.count(old))
    s = s.replace(old, new)


CSS = r'''
:root{color-scheme:dark;--ground:#1c2819;--ground-2:#223020;--ink:#ece5cf;--ink-soft:#c9c6ad;--muted:#9fab90;--sage:#8fa476;--gold:#e2ab47;--foil:#d8b25e;
  --line:rgba(236,229,207,.14);--line-strong:rgba(216,178,94,.55);--paper:#efe9d6;--display:"Marcellus",Georgia,serif}
*{margin:0;padding:0;box-sizing:border-box}
html{background:#1c2819}
body{font-family:"Figtree","Segoe UI",system-ui,-apple-system,sans-serif;color:var(--ink);line-height:1.55;font-size:15.5px;-webkit-font-smoothing:antialiased;
  background:radial-gradient(120% 40% at 50% 0%,rgba(143,164,118,.13),transparent 60%),var(--ground)}
.wrap{max-width:1060px;margin:0 auto;padding:0 clamp(16px,4vw,32px) 52px}
.top{display:flex;align-items:center;gap:16px;padding:12px 0;margin-bottom:22px;border-bottom:1px solid var(--line)}
.top .brand{position:relative}
.top .brand img{height:36px;width:auto;display:block}
.top .brand .reg{position:absolute;top:-3px;right:-9px;font:600 9px/1 "Figtree",system-ui,sans-serif;color:var(--foil)}
.back{color:var(--ink-soft);text-decoration:none;font-size:14px;font-weight:600}
.back:hover{color:var(--foil)}
.head{display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:16px;padding:clamp(18px,3.4vw,30px);border:1px solid var(--line-strong);border-radius:18px;
  background:radial-gradient(100% 140% at 0% 0%,rgba(226,171,71,.13),transparent 60%),var(--ground-2);box-shadow:0 18px 50px rgba(0,0,0,.28)}
.head h1{font-family:var(--display);font-weight:400;font-size:clamp(28px,5vw,42px);line-height:1.1;color:var(--foil)}
.head .sub{margin-top:10px;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);font-weight:600}
.head .rt{text-align:right;font-size:14px;line-height:1.75;color:var(--ink-soft)}
.head .rt b{font-size:16px;color:var(--ink)}
@media(max-width:620px){.head .rt{text-align:left}}
.kick{font-size:11.5px;font-weight:700;color:var(--gold);letter-spacing:.14em;text-transform:uppercase}
h2.sec{font-family:var(--display);font-weight:400;font-size:clamp(23px,3.4vw,29px);color:var(--ink);margin:38px 0 12px;padding-bottom:8px;border-bottom:1px solid var(--line)}
.target{margin-top:14px;padding:16px 20px;border-radius:16px;border:1px solid rgba(226,171,71,.65);background:linear-gradient(120deg,rgba(226,171,71,.20),rgba(226,171,71,.05));box-shadow:0 0 34px rgba(226,171,71,.12)}
.target b{display:block;margin:6px 0;font-family:var(--display);font-weight:400;font-size:clamp(19px,2.6vw,24px);line-height:1.3;color:var(--ink)}
.target p{font-size:14.5px;color:var(--ink-soft)}
.week{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px;margin-top:8px}
.day{padding:11px 12px;border-radius:12px;border:1px solid var(--line-strong);background:var(--ground-2);font-size:14.5px;color:var(--ink)}
.day .dn{margin-bottom:3px;font-size:12px;letter-spacing:.1em;text-transform:uppercase;font-weight:700;color:var(--foil)}
.day span{font-size:13px;color:var(--muted)}
.day.rest{background:transparent;border-color:var(--line);color:var(--ink-soft)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,430px),1fr));gap:14px;margin-top:12px}
.card{overflow:hidden;border:1px solid var(--line);border-radius:16px;background:var(--ground-2)}
.card.key{border-color:var(--gold);box-shadow:0 0 0 1px rgba(226,171,71,.35),0 0 34px rgba(226,171,71,.14)}
.card-h{display:flex;align-items:center;gap:12px;padding:14px 16px 0}
.num{flex-shrink:0;width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;border:1px solid var(--foil);color:var(--foil);font-family:var(--display);font-size:16px}
.num.gold{background:var(--gold);border-color:var(--gold);color:var(--ground)}
.card-h .nm{font-weight:600;font-size:16.5px;color:var(--ink)}
.card-h .tg{font-size:12.5px;color:var(--muted)}
.viz{display:flex;align-items:center;justify-content:center;margin:12px 16px 0;padding:10px;border-radius:12px;background:var(--paper)}
.viz svg{width:150px;height:160px}
.body{padding:12px 16px 16px}
.dose{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:8px}
.pill{padding:3px 11px;border-radius:999px;border:1px solid var(--line-strong);font-size:12.5px;font-weight:600;color:var(--ink)}
.pill.g{background:var(--gold);border-color:var(--gold);color:var(--ground)}
.lbl{margin-top:10px;font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--foil)}
.body ul{margin:4px 0 0 18px;font-size:14px;color:var(--ink-soft)}
.body li{margin:3px 0}
.body li::marker{color:var(--sage)}
.body b{color:var(--ink)}
.warn{color:#f0a78e}
.body li.warn b{color:#f7bba6}
.tbl{margin-top:10px;overflow-x:auto;border:1px solid var(--line);border-radius:14px}
table{width:100%;min-width:540px;border-collapse:collapse;font-size:14px}
th{padding:10px 12px;text-align:left;font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;font-weight:700;color:var(--foil);background:rgba(216,178,94,.10)}
td{padding:10px 12px;border-top:1px solid var(--line);color:var(--ink-soft);vertical-align:top}
td b{color:var(--ink)}
td.warn,td.warn b{color:#f0a78e}
.chk{display:inline-block;width:16px;height:16px;border:1.5px solid var(--foil);border-radius:4px;vertical-align:-3px}
.note{margin-top:14px;padding:14px 16px;border-radius:14px;border:1px solid var(--line);background:rgba(236,229,207,.04);font-size:14.5px;color:var(--ink-soft)}
.note b{color:var(--ink)}
.note.stop{border-color:rgba(221,138,111,.55);background:rgba(221,138,111,.08)}
.note.stop > b:first-child{color:#f0a78e}
.small{margin-top:6px;font-size:12.5px;color:var(--muted)}
.cta{display:inline-flex;align-items:center;gap:8px;margin-top:24px;padding:12px 20px;border-radius:999px;background:var(--foil);color:var(--ground);font-weight:600;text-decoration:none}
.cta:hover{background:var(--gold)}
.foot{margin-top:22px;padding-top:12px;border-top:1px solid var(--line);font-size:12.5px;font-style:italic;color:var(--muted)}
/* ---- ANİMASYON (kâğıt panelde) ---- */
.band{fill:none;stroke:#C8963E;stroke-width:3.5;stroke-linecap:round;}
.fig{fill:none;stroke:#2A6F6B;stroke-width:5;stroke-linecap:round;stroke-linejoin:round;}
.fig.hl{stroke:#C8963E;stroke-width:6;}
.hd{fill:#2A6F6B;stroke:none;} .hd.hl{fill:#C8963E;}
.grd{stroke:#B9CBC6;stroke-width:3;stroke-linecap:round;}
.obj{stroke:#8FA8A2;stroke-width:4;fill:none;stroke-linecap:round;}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
/* yazdırırken beyaz kâğıt */
@media print{
  html,body{background:#fff!important;color:#1c2b2a}
  .top,.cta{display:none}
  .head,.card,.day,.note,.tbl,.target{background:#fff!important;border-color:#cfd8d4!important;box-shadow:none!important}
  .head h1,.day .dn,.lbl,th,.kick{color:#1E4F4C}
  .body ul,td,.target p,.head .rt,.note,.day span,.card-h .tg,.head .sub,.foot,.small{color:#333}
  .body b,td b,.note b,.target b,.card-h .nm,.head .rt b,.day{color:#000}
  .pill{color:#1E4F4C;border-color:#9fb5af} .pill.g{background:#C8963E;color:#fff}
  .num{color:#1E4F4C;border-color:#1E4F4C} .num.gold{background:#C8963E;color:#fff;border-color:#C8963E}
  .card{break-inside:avoid}
}
'''
i = s.index("<style>") + len("<style>")
j = s.index("</style>")
s = s[:i] + CSS + s[j:]
rep('<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
    '<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
    '<meta name="color-scheme" content="dark">\n<meta name="theme-color" content="#1c2819">\n<link rel="icon" type="image/png" href="logo.png">')
rep('<a href="index.html" style="display:inline-block;margin:0 0 12px;color:#1E4F4C;font-weight:600;text-decoration:none;font-size:14px">← İhsan Eren ana sayfa</a>',
    '<header class="top"><a class="brand" href="index.html"><img src="logo-mark.svg" alt="İhsan Eren" width="44" height="36"><sup class="reg">®</sup></a><a class="back" href="index.html">← İhsan Eren ana sayfa</a></header>')
rep('<div class="sub">Longevity Kliniği · Faz 1–2 · Değerlendirme sonrası program</div>',
    '<div class="sub">Örnek reçete · Faz 1–2 · Değerlendirme sonrası program</div>')
rep('<b style="font-size:15px;color:#fff;">A.Y.</b>', '<b>A.Y.</b>')
rep('<div class="kick" style="color:#3B2E12;">', '<div class="kick">')
rep('Sol-sağ farkı %11 (hedef &lt;%10)', 'Sol-sağ farkı %13 (hedef &lt;%10)')
s = s.replace('<span style="color:#5A6B69;">', '<span>')
rep('<div class="note" style="margin-top:10px;">', '<div class="note">')
rep('<div class="card" style="border:2px solid #C8963E;">', '<div class="card key">')
# tablolar yatay kaydırılabilir kutuda
s = s.replace('<table>', '<div class="tbl"><table>').replace('</table>', '</table></div>')
rep('<div style="font-size:12px;color:#5A6B69;margin-top:6px;">', '<div class="small">')
rep('''<div class="note" style="background:#FCEEEB;">
<b style="color:#C0554A;">Şu durumlarda dur ve kliniği ara:</b>''', '''<div class="note stop">
<b>Şu durumlarda dur ve hemen haber ver:</b>''')
rep('Egzersizler klinik ekip gözetiminde öğrenildikten sonra evde sürdürülür.', 'Egzersizler fizyoterapist gözetiminde öğrenildikten sonra evde sürdürülür.')
rep(' · Longevity Kliniği</div>', ' · İhsan Eren</div>')
rep('<div class="foot">', '<a class="cta" href="index.html#tanisma">Ücretsiz ön görüşme planla</a>\n<div class="foot">')
assert "Longevity Kliniği" not in s and "kliniği" not in s.lower().replace("klinik ekip", ""), "klinik kaldı"
# Site Core v2 (7 Ekim 2026): ortak yazı tipleri/yardımcılar /assets/ altında; açıklama ve sosyal kart üst verileri
DESC = "Kişiye özel hazırlanmış örnek egzersiz reçetesi: haftalık plan, egzersiz dozları, uygulama notları ve güvenlik uyarıları."
rep('<link rel="icon" type="image/png" href="logo.png">', '<link rel="icon" type="image/png" href="logo.png">\n<link rel="stylesheet" href="/assets/site-core.css">')
rep('<title>Egzersiz Reçetesi — A.Y.</title>', '<title>Egzersiz Reçetesi — A.Y.</title>\n\n'
    f'<meta name="description" content="{DESC}">\n<meta property="og:type" content="article">\n<meta property="og:title" content="Egzersiz Reçetesi — A.Y.">\n'
    f'<meta property="og:description" content="{DESC}">\n<meta property="og:image" content="https://drihsaneren.com/logo.png">\n'
    '<meta property="og:url" content="https://drihsaneren.com/recete.html">\n<meta name="twitter:title" content="Egzersiz Reçetesi — A.Y.">\n'
    f'<meta name="twitter:description" content="{DESC}">\n<meta name="twitter:image" content="https://drihsaneren.com/logo.png">')
rep('</head>', '<meta name="twitter:card" content="summary_large_image">\n</head>')
rep('</div></body></html>', '</div><script src="/assets/site-core.js" defer></script>\n</body></html>')
open(R + "recete.html", "w", encoding="utf-8").write(s)
print("ok", len(s))
