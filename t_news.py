import asyncio, sys, http.server, threading, functools
from playwright.async_api import async_playwright
root=sys.argv[1]; page=sys.argv[2]; tag=sys.argv[3]
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',8770),functools.partial(Q,directory=root)); threading.Thread(target=srv.serve_forever,daemon=True).start()
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for vw,dev in [(1280,'pc'),(390,'tel')]:
            pg=await b.new_page(viewport={'width':vw,'height':900}); errs=[]
            pg.on('pageerror',lambda e: errs.append(str(e)))
            await pg.route('**/*', lambda r: r.abort() if not r.request.url.startswith('http://127.0.0.1') else r.continue_())
            await pg.goto(f'http://127.0.0.1:8770/{page}'); await pg.wait_for_timeout(600)
            over=await pg.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth')
            grid=await pg.query_selector('.grid'); await grid.screenshot(path=f'shots3/news_{tag}_{dev}.png')
            await pg.click('.filt button[data-f="kalp"]'); await pg.wait_for_timeout(300)
            vis=await pg.eval_on_selector_all('.grid .card:not([hidden]) h2','els=>els.map(e=>e.textContent)')
            print(dev,'overflow',over,'errors',errs[:2],'kalp:',vis)
            await pg.close()
        await b.close()
asyncio.run(main())
