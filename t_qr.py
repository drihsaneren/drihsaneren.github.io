import asyncio, cv2, numpy as np
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={"width":1366,"height":800},device_scale_factor=2)
        await pg.goto("http://127.0.0.1:8765/index.html"); await pg.add_style_tag(content="html{scroll-behavior:auto!important}")
        await pg.evaluate("document.getElementById('iletisim').scrollIntoView({block:'center'})")
        el=await pg.query_selector("#nq")
        for t in [150,500,900,1400,2600]:
            await pg.wait_for_timeout(t if t==150 else t-prev); prev=t
            await el.screenshot(path=f"shots6/qr_{t}.png")
        await pg.wait_for_timeout(2500)
        for k in range(6):
            await el.screenshot(path=f"shots6/qr_w{k}.png"); await pg.wait_for_timeout(250)
        await b.close()
prev=0
asyncio.run(main())
det=cv2.QRCodeDetector()
import glob
for f in sorted(glob.glob("shots6/qr_*.png")):
    im=cv2.imread(f); im=cv2.copyMakeBorder(im,40,40,40,40,cv2.BORDER_CONSTANT,value=(40,57,30))
    res=[]
    for sc in (1.0,.6,.4):
        v=det.detectAndDecode(cv2.resize(im,None,fx=sc,fy=sc))[0]; res.append(v=="https://wa.me/905538815568")
    print(f,res)
