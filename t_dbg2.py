import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        ctx=await b.new_context(viewport={"width":390,"height":844},device_scale_factor=2,is_mobile=True,has_touch=True)
        pg=await ctx.new_page()
        await pg.goto("http://127.0.0.1:8765/index.html"); await pg.add_style_tag(content="html{scroll-behavior:auto!important}")
        await pg.evaluate("document.getElementById('rapor').scrollIntoView({block:'center'})")
        for i in range(8):
            r=await pg.evaluate("[scrollY, JSON.stringify(document.getElementById('rs-next').getBoundingClientRect()), document.getElementById('rapor').offsetHeight, document.documentElement.scrollHeight]")
            print(r); await pg.wait_for_timeout(700)
        await b.close()
asyncio.run(main())
