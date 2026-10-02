import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1366,"height":900},device_scale_factor=1.5)
        await pg.goto("http://127.0.0.1:8765/index.html"); await pg.add_style_tag(content="html{scroll-behavior:auto!important}")
        await pg.evaluate("document.getElementById('logo').scrollIntoView()"); await pg.wait_for_timeout(1200)
        el=await pg.query_selector("#logo .annot"); await el.screenshot(path="shots6/annot.png")
        print(await pg.evaluate("[...document.querySelectorAll('#logo .pin')].map(p=>{const b=p.getBBox();return [Math.round(b.x),Math.round(b.y),Math.round(b.width)]})"))
        await b.close()
asyncio.run(main())
