import asyncio, sys, http.server, threading, functools
from playwright.async_api import async_playwright
root=sys.argv[1]
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',8769),functools.partial(Q,directory=root)); threading.Thread(target=srv.serve_forever,daemon=True).start()
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for page,tag in [('bilgi.html','tr'),('en/health-library.html','en')]:
            for vw,dev in [(1280,'pc'),(390,'tel')]:
                pg=await b.new_page(viewport={'width':vw,'height':1000})
                errs=[]; pg.on('pageerror',lambda e: errs.append(str(e)))
                await pg.route('**/*', lambda r: r.abort() if not r.request.url.startswith('http://127.0.0.1') else r.continue_())
                await pg.goto(f'http://127.0.0.1:8769/{page}'); await pg.wait_for_timeout(500)
                await pg.add_style_tag(content='html{scroll-behavior:auto!important}')
                el=await pg.query_selector('#kendine-iyi-bak'); await el.screenshot(path=f'shots2/hub_{tag}_{dev}.png')
                over=await pg.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth')
                print(page,dev,'overflow',over,errs[:2]); await pg.close()
        pg=await b.new_page(viewport={'width':1280,'height':900})
        await pg.route('**/*', lambda r: r.abort() if not r.request.url.startswith('http://127.0.0.1') else r.continue_())
        await pg.goto('http://127.0.0.1:8769/index.html'); await pg.wait_for_timeout(500)
        el=await pg.query_selector('#bilgi .kose-more'); await el.screenshot(path='shots2/home_pills.png')
        await b.close()
asyncio.run(main())
