import asyncio, sys
from PIL import Image
from playwright.async_api import async_playwright
from t_st2 import run
EXP={"base":"", "flat":"document.querySelector('.nq-pl').setAttribute('fill','#f4ecd4')", "nologo":"document.querySelector('.nq-logo').style.display='none'",
     "noshadow":"document.querySelector('#nq .code').style.boxShadow='none'", "noround":"document.querySelector('.nq').style.borderRadius='0'"}
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for k,js in EXP.items():
            pg=await b.new_page(viewport={"width":1366,"height":800},device_scale_factor=2)
            await pg.goto("http://127.0.0.1:8765/index.html"); await pg.add_style_tag(content="html{scroll-behavior:auto!important}")
            await pg.evaluate("document.getElementById('iletisim').scrollIntoView({block:'center'})"); await pg.wait_for_timeout(2600)
            if js: await pg.evaluate(js); await pg.wait_for_timeout(100)
            el=await pg.query_selector("#nq .nq"); await el.screenshot(path=f"/tmp/qx_{k}.png"); await pg.close()
            print(k, run(Image.open(f"/tmp/qx_{k}.png").convert("RGB"))[:2])
        await b.close()
asyncio.run(main())
