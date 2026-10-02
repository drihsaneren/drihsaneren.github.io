import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        ctx=await b.new_context(viewport={"width":390,"height":844},is_mobile=True,has_touch=True,device_scale_factor=3); pg=await ctx.new_page()
        await pg.goto("http://127.0.0.1:8765/index.html"); await pg.wait_for_timeout(1200)
        await pg.screenshot(path="shots6/reg_tel.png",clip={"x":0,"y":0,"width":200,"height":60})
        await pg.goto("http://127.0.0.1:8765/recete.html"); await pg.wait_for_timeout(600)
        await pg.screenshot(path="shots6/reg_rec.png",clip={"x":0,"y":0,"width":260,"height":64}); await ctx.close()
        pg=await b.new_page(viewport={"width":1366,"height":900},device_scale_factor=2)
        await pg.goto("http://127.0.0.1:8765/index.html"); await pg.add_style_tag(content="html{scroll-behavior:auto!important}")
        await pg.wait_for_timeout(800); await pg.screenshot(path="shots6/reg_pc.png",clip={"x":180,"y":0,"width":200,"height":60})
        await pg.evaluate("document.getElementById('logo').scrollIntoView()"); await pg.wait_for_timeout(1200)
        el=await pg.query_selector("#logo .annot"); await el.screenshot(path="shots6/reg_annot.png")
        await b.close()
asyncio.run(main())
from PIL import Image
a=Image.open("shots6/reg_tel.png"); b_=Image.open("shots6/reg_pc.png"); c=Image.open("shots6/reg_rec.png")
W=max(a.width,b_.width,c.width); im=Image.new("RGB",(W,a.height+b_.height+c.height+20),(0,0,0)); y=0
for x in (a,b_,c): im.paste(x,(0,y)); y+=x.height+10
im.save("shots6/reg_hdrs.png")
