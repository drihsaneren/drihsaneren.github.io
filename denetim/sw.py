import asyncio, sys
from playwright.async_api import async_playwright
async def main(pages):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for w in (360, 390, 1366, 1440):
            pg = await b.new_page(viewport={"width": w, "height": 900})
            await pg.route("**/*", lambda r: r.abort() if not r.request.url.startswith("http://127.0.0.1") else r.continue_())
            for u in pages:
                await pg.goto("http://127.0.0.1:8765/" + u); await pg.wait_for_timeout(250)
                sw = await pg.evaluate("[document.documentElement.scrollWidth, document.documentElement.clientWidth]")
                if sw[0] > sw[1]: print("TAŞMA", w, u, sw)
            await pg.close()
        await b.close(); print("sw bitti")
asyncio.run(main(sys.argv[1:]))
