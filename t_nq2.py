import asyncio, zxingcpp
from PIL import Image
from playwright.async_api import async_playwright
TS=[700,1200,2450,2750,3050,3350,3700,5300,5700]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1366,"height":800},device_scale_factor=2)
        await pg.goto("http://127.0.0.1:8765/index.html"); await pg.add_style_tag(content="html{scroll-behavior:auto!important}")
        await pg.evaluate("document.getElementById('iletisim').scrollIntoView({block:'center'})")
        el=await pg.query_selector("#nq .code"); prev=0
        for t in TS:
            await pg.wait_for_timeout(t-prev); prev=t
            await el.screenshot(path=f"shots6/n2_{t}.png")
        await b.close()
asyncio.run(main())
ims=[Image.open(f"shots6/n2_{t}.png") for t in TS]
for t,im in zip(TS,ims):
    r=zxingcpp.read_barcodes(im); print(t, bool(r and r[0].text=="https://wa.me/905538815568"))
w,h=ims[0].size; c=Image.new("RGB",(w*3+20,h*3+20),(20,30,18))
for i,im in enumerate(ims): c.paste(im,((i%3)*(w+10),(i//3)*(h+10)))
c.save("shots6/n2_grid.png")
