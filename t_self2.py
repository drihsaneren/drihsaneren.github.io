import asyncio, sys, http.server, threading, functools
from playwright.async_api import async_playwright
root=sys.argv[1]; pages=sys.argv[2].split(','); out=sys.argv[3]
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',8766),functools.partial(Q,directory=root)); threading.Thread(target=srv.serve_forever,daemon=True).start()
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for name in pages:
            for vw,tag in [(1280,'pc'),(390,'tel')]:
                pg=await b.new_page(viewport={'width':vw,'height':900})
                errs=[]
                pg.on('pageerror',lambda e: errs.append(str(e)))
                pg.on('console',lambda m: errs.append('console:'+m.text) if m.type=='error' else None)
                await pg.route('**/*', lambda r: r.abort() if not r.request.url.startswith('http://127.0.0.1') else r.continue_())
                await pg.goto(f'http://127.0.0.1:8766/{name}'); await pg.wait_for_timeout(900)
                over=await pg.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth')
                await pg.screenshot(path=f'{out}/{name[:-5]}_{tag}.png', full_page=True)
                print(name,tag,'overflow',over,'errors',[e for e in errs if 'net::' not in e][:3])
                await pg.close()
        await b.close()
asyncio.run(main())
