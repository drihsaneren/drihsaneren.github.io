import asyncio, sys
from playwright.async_api import async_playwright
from PIL import Image, ImageDraw
async def main():
    shots=[]
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1280,'height':900})
        for page in sys.argv[1:]:
            await pg.goto('file://'+page); await pg.wait_for_timeout(300)
            cards=await pg.query_selector_all('#egzersizler .exc')
            for i,c in enumerate(cards):
                await c.scroll_into_view_if_needed()
                row=[]
                for t in [0,1.6,2.4]:
                    await pg.evaluate(f"(()=>{{const s=document.querySelectorAll('#egzersizler .exc')[{i}].querySelector('svg');s.pauseAnimations();s.setCurrentTime({t});}})()")
                    fn=f'/tmp/_f.png'; await (await c.query_selector('.an')).screenshot(path=fn)
                    row.append(Image.open(fn).convert('RGB').copy())
                title=await (await c.query_selector('h3')).inner_text()
                shots.append((title,row))
        await b.close()
    w=max(sum(im.width for im in r)+40 for _,r in shots); h=sum(r[0].height+24 for _,r in shots)
    out=Image.new('RGB',(w,h),'white'); d=ImageDraw.Draw(out); y=0
    for t,r in shots:
        d.text((4,y+4),t,fill='black'); y+=20; x=0
        for im in r: out.paste(im,(x,y)); x+=im.width+10
        y+=r[0].height+4
    out.save('exframes.png'); print(out.size, len(shots))
asyncio.run(main())
