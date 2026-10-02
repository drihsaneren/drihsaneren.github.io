import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for vw,tag in [(1280,'pc'),(390,'tel')]:
            pg=await b.new_page(viewport={'width':vw,'height':900}, device_scale_factor=2)
            errs=[]; pg.on('pageerror',lambda e: errs.append(str(e)))
            await pg.goto('file://'+sys.argv[1]); await pg.wait_for_timeout(500)
            box=await pg.query_selector('#hizli-test'); await box.scroll_into_view_if_needed()
            await box.screenshot(path=f'qt_{tag}_0.png')
            await pg.fill('#qt-age','58'); await pg.dispatch_event('#qt-age','input')
            await pg.click('#hizli-test [data-s="0"] [data-next]')
            await pg.click('#qt-sw'); await pg.wait_for_timeout(1300); await pg.click('#qt-sw')
            print(tag,'kronometre sonrası:', await pg.inner_text('#qt-sts-v'))
            await pg.fill('#qt-sts','8.4'); await pg.dispatch_event('#qt-sts','input')
            await box.screenshot(path=f'qt_{tag}_1.png')
            await pg.click('#hizli-test [data-s="1"] [data-next]')
            dis=await pg.eval_on_selector('#hizli-test [data-s="2"] [data-next]','e=>e.disabled'); print(tag,'seçim yokken devam kapalı:',dis)
            await pg.click('#hizli-test [data-s="2"] .qt-opt >> nth=1')
            await box.screenshot(path=f'qt_{tag}_2.png')
            await pg.click('#hizli-test [data-s="2"] [data-next]')
            await pg.fill('#qt-steps','6000'); await pg.dispatch_event('#qt-steps','input')
            await pg.click('#hizli-test [data-s="3"] [data-next]')
            await pg.click('#hizli-test [data-s="4"] .qt-opt >> nth=1')
            await pg.click('#hizli-test [data-s="4"] [data-next]'); await pg.wait_for_timeout(500)
            print(tag,'sonuç:', await pg.inner_text('#qt-title'))
            href=await pg.get_attribute('#qt-wa','href'); 
            import urllib.parse; print(tag,'WA:', urllib.parse.unquote(href.split('text=')[1])[:260])
            await box.screenshot(path=f'qt_{tag}_5.png')
            over=await pg.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth')
            print(tag,'overflow',over,'errors',errs); await pg.close()
        await b.close()
asyncio.run(main())
