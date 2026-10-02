# Dar kanal sayfası: taşma, konsol hatası, bağlantı ve kart sınaması (TR + EN). Kullanım: ./srv.sh python3 t_ls.py [ekran-görüntüsü-dizini]
import asyncio, sys, os
from playwright.async_api import async_playwright
OUT = sys.argv[1] if len(sys.argv) > 1 else "shots6"
PAGES = ["dar-kanal.html", "en/lumbar-spinal-stenosis.html", "bilgi.html", "en/health-library.html",
         "bel-fitigi.html", "en/lumbar-disc-herniation.html", "index.html", "en/index.html"]
async def main():
    os.makedirs(OUT, exist_ok=True); bad = 0
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name in PAGES:
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
                if name.endswith(("dar-kanal.html", "lumbar-spinal-stenosis.html")):
                    n_ex = await pg.locator("#egzersizler .exc").count()
                    n_vid = await pg.locator("#videolar .vbox").count()
                    n_faq = await pg.locator(".faq details").count()
                    extra = f" egzersiz={n_ex} video={n_vid} sss={n_faq}"
                    bad += (n_ex != 6) + (n_vid != 2) + (n_faq != 4)
                    if vw in (390, 1366):
                        await pg.screenshot(path=f"{OUT}/ls_{'en' if name.startswith('en/') else 'tr'}_{vw}.png", full_page=True)
                if name.endswith(("bilgi.html", "health-library.html")):
                    slug = "lumbar-spinal-stenosis.html" if name.startswith("en/") else "dar-kanal.html"
                    card = pg.locator(f'#agrilar a.kc[href="{slug}"]')
                    n = await card.count(); extra = f" kart={n}"; bad += (n != 1)
                    if n and vw == 1366:
                        await card.scroll_into_view_if_needed(); await card.screenshot(path=f"{OUT}/ls_card_{'en' if name.startswith('en/') else 'tr'}.png")
                    await pg.locator('#agrilar .filt button[data-f="bel"]').click()
                    vis = await pg.locator("#agrilar .kose > a:not([hidden])").count()
                    extra += f" bel-süzgeci={vis}"; bad += (vis != 6)
                if name.endswith("index.html"):
                    slug = "lumbar-spinal-stenosis.html" if name.startswith("en/") else "dar-kanal.html"
                    n = await pg.locator(f'#bilgi a.pill[href="{slug}"]').count(); extra = f" hap={n}"; bad += (n != 1)
                if name.endswith(("bel-fitigi.html", "lumbar-disc-herniation.html")):
                    slug = "lumbar-spinal-stenosis.html" if name.startswith("en/") else "dar-kanal.html"
                    n = await pg.locator(f'.more a[href="{slug}"]').count(); extra = f" ilgili={n}"; bad += (n != 1)
                bad += (over > 0) + len(errs)
                print(name, vw, "taşma", over, "hata", errs[:3], extra)
                await pg.close()
        # iç bağlantılar
        pg = await b.new_page()
        for name in ("dar-kanal.html", "en/lumbar-spinal-stenosis.html"):
            await pg.goto("http://127.0.0.1:8765/" + name)
            hrefs = await pg.evaluate("[...document.querySelectorAll('a[href]')].map(a=>a.href).filter(h=>h.startsWith('http://127.0.0.1'))")
            for h in sorted(set(x.split('#')[0] for x in hrefs)):
                r = await pg.request.get(h)
                if r.status != 200: print("KIRIK", name, h, r.status); bad += 1
            body = (await pg.content())
            for w in ("randevu", "appointment", "tel:"):
                if w in body.lower(): print("YASAK", name, w); bad += 1
        await b.close()
    print("sorun:", bad)
    sys.exit(1 if bad else 0)
asyncio.run(main())
