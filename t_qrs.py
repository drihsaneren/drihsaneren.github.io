import asyncio, zxingcpp, io
from PIL import Image, ImageFilter
from playwright.async_api import async_playwright
async def shot():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1366,"height":800},device_scale_factor=2)
        await pg.goto("http://127.0.0.1:8765/index.html"); await pg.add_style_tag(content="html{scroll-behavior:auto!important}")
        await pg.evaluate("document.getElementById('iletisim').scrollIntoView({block:'center'})"); await pg.wait_for_timeout(2400)
        el=await pg.query_selector("#nq .code"); await el.screenshot(path="shots6/qr_s.png"); await b.close()
asyncio.run(shot())
im=Image.open("shots6/qr_s.png").convert("RGB")
ok=0;tot=0
for rot in (0,7,-12,20):
    for blur in (0,1.2,2.2):
        for w in (110,160,260):
            j=im.rotate(rot,expand=True,fillcolor=(40,57,30)).filter(ImageFilter.GaussianBlur(blur)); j=j.resize((w,int(w*j.height/j.width)))
            b=io.BytesIO(); j.save(b,"JPEG",quality=55); j=Image.open(b)
            r=zxingcpp.read_barcodes(j); ok+=bool(r and r[0].text.lower()=="https://wa.me/905538815568"); tot+=1
print(ok,tot)
