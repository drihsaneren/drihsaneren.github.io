import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        ctx=await b.new_context(viewport={"width":1366,"height":768},reduced_motion="reduce")
        pg=await ctx.new_page()
        await pg.goto("http://127.0.0.1:8765/index.html"); await pg.wait_for_timeout(400)
        await pg.screenshot(path="shots5/rm_hero.png")
        await pg.evaluate("document.getElementById('rapor').scrollIntoView({block:'center'})"); await pg.wait_for_timeout(800)
        el=await pg.query_selector("#rapor"); await el.screenshot(path="shots5/rm_rs0.png")
        await pg.wait_for_timeout(9000)
        print(await pg.evaluate("document.getElementById('rs-n').textContent"), await pg.get_attribute("#rs-play","aria-pressed"))
        await pg.evaluate("document.getElementById('rs-next').click()"); await pg.wait_for_timeout(300)
        await el.screenshot(path="shots5/rm_rs1.png")
        await b.close()
asyncio.run(main())
