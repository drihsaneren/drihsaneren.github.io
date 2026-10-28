import asyncio, sys
from playwright.async_api import async_playwright
async def main(url, vw):
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": vw, "height": 900})
        await pg.route("**/*", lambda r: r.abort() if not r.request.url.startswith("http://127.0.0.1") else r.continue_())
        await pg.goto("http://127.0.0.1:8765/" + url); await pg.wait_for_timeout(500)
        r = await pg.evaluate("""() => { const W = document.documentElement.clientWidth, out = [];
          document.querySelectorAll('body *').forEach(e => { const b = e.getBoundingClientRect(); if (b.right > W + 1 && b.width > 0) out.push(e.tagName + '.' + e.className + ' ' + Math.round(b.right) + ' ' + (e.textContent||'').trim().slice(0,60)); });
          return out.slice(0, 15); }""")
        print("\n".join(r)); await b.close()
asyncio.run(main(sys.argv[1], int(sys.argv[2])))
