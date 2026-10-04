# Yeni konu sayfası sınaması (TR + EN): taşma (390/1366/1440), konsol hatası, kart, hap, iç bağlantılar, yasak kelimeler.
# Kullanım: ./srv.sh python3 t_ls.py <görüntü-dizini> <tr.html> <en.html> <video-sayısı> [ilgili-tr.html ilgili-en.html]
#   ör. ./srv.sh python3 t_ls.py shots6 dar-kanal.html lumbar-spinal-stenosis.html 2 bel-fitigi.html lumbar-disc-herniation.html
#       ./srv.sh python3 t_ls.py shots6 multipl-skleroz.html multiple-sclerosis.html 0
import asyncio, sys, os
from playwright.async_api import async_playwright
a = sys.argv[1:]
OUT = a[0] if a else "shots6"
TR = a[1] if len(a) > 1 else "dar-kanal.html"
EN = a[2] if len(a) > 2 else "lumbar-spinal-stenosis.html"
NVID = int(a[3]) if len(a) > 3 else 2
REL = a[4:6] if len(a) > 5 else (["bel-fitigi.html", "lumbar-disc-herniation.html"] if len(a) <= 1 else [])
TAG = TR[:-5]
PAGES = [TR, "en/" + EN, "bilgi.html", "en/health-library.html", "index.html", "en/index.html"] + ([REL[0], "en/" + REL[1]] if REL else [])
async def main():
    os.makedirs(OUT, exist_ok=True); bad = 0
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name in PAGES:
            en = name.startswith("en/"); slug = EN if en else TR; base = name.split("/")[-1]
            for vw in (390, 1366, 1440):
                pg = await b.new_page(viewport={"width": vw, "height": 900})
                errs = []
                pg.on("pageerror", lambda e: errs.append(str(e)))
                pg.on("console", lambda m: errs.append("console:" + m.text) if m.type == "error" else None)
                await pg.route("**/*", lambda r: r.abort() if not r.request.url.startswith("http://127.0.0.1") else r.continue_())
                await pg.goto("http://127.0.0.1:8765/" + name); await pg.wait_for_timeout(700)
                over = await pg.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth")
                errs = [e for e in errs if "net::" not in e]
                extra = ""
                if base == slug:
                    n_ex = await pg.locator("#egzersizler .exc").count()
                    n_vid = await pg.locator("#videolar .vbox").count()
                    n_faq = await pg.locator(".faq details").count()
                    extra = f" egzersiz={n_ex} video={n_vid} sss={n_faq}"
                    bad += (n_ex != 6) + (n_vid != NVID) + (n_faq != 4)
                    if vw in (390, 1366):
                        await pg.screenshot(path=f"{OUT}/{TAG}_{'en' if en else 'tr'}_{vw}.png", full_page=True)
                elif base in ("bilgi.html", "health-library.html"):
                    card = pg.locator(f'a.kc[href="{slug}"]')
                    n = await card.count(); extra = f" kart={n}"; bad += (n != 1)
                    if n and vw == 1366:
                        await card.scroll_into_view_if_needed(); await card.screenshot(path=f"{OUT}/{TAG}_card_{'en' if en else 'tr'}.png")
                    reg = await card.get_attribute("data-r") if n else None
                    if reg:   # bölge süzgeci: kart kendi bölgesinde görünür, başka bölgede gizlenir
                        r0 = reg.split()[0]; other = "ayak" if r0 != "ayak" else "bel"
                        await pg.locator(f'#agrilar .filt button[data-f="{r0}"]').click(); v1 = await card.is_visible()
                        await pg.locator(f'#agrilar .filt button[data-f="{other}"]').click(); v2 = await card.is_visible()
                        extra += f" süzgeç={v1}/{v2}"; bad += (not v1) + v2
                elif base == "index.html":
                    n = await pg.locator(f'#bilgi a.pill[href="{slug}"]').count(); extra = f" hap={n}"; bad += (n != 1)
                else:
                    n = await pg.locator(f'.more a[href="{slug}"]').count(); extra = f" ilgili={n}"; bad += (n != 1)
                bad += (over > 0) + len(errs)
                print(name, vw, "taşma", over, "hata", errs[:3], extra)
                await pg.close()
        pg = await b.new_page()
        for name in (TR, "en/" + EN):
            await pg.goto("http://127.0.0.1:8765/" + name)
            hrefs = await pg.evaluate("[...document.querySelectorAll('a[href]')].map(a=>a.href).filter(h=>h.startsWith('http://127.0.0.1'))")
            for h in sorted(set(x.split('#')[0] for x in hrefs)):
                r = await pg.request.get(h)
                if r.status != 200: print("KIRIK", name, h, r.status); bad += 1
            body = (await pg.content()).lower()
            for w in ("randevu", "appointment", "tel:", "biruni"):
                if w in body: print("YASAK", name, w); bad += 1
        await b.close()
    print("sorun:", bad)
    sys.exit(1 if bad else 0)
asyncio.run(main())
