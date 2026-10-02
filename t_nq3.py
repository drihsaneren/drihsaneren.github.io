import asyncio, zxingcpp
from PIL import Image
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1366,"height":800},device_scale_factor=2)
        await pg.goto("http://127.0.0.1:8765/index.html"); await pg.add_style_tag(content="html{scroll-behavior:auto!important}")
        await pg.evaluate("document.getElementById('iletisim').scrollIntoView({block:'center'})")
        el=await pg.query_selector("#nq .code"); await pg.wait_for_timeout(1500)
        ok=0; fails=[]
        for i in range(44):
            await el.screenshot(path=f"/tmp/l_{i}.png")
            r=zxingcpp.read_barcodes(Image.open(f"/tmp/l_{i}.png"))
            g=bool(r and r[0].text=="https://wa.me/905538815568"); ok+=g
            if not g: fails.append(i)
            await pg.wait_for_timeout(80)
        print("decoded",ok,"/44 fails",fails)
        await b.close()
asyncio.run(main())
