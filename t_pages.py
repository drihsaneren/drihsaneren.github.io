import asyncio, sys, http.server, threading, functools
from playwright.async_api import async_playwright
root=sys.argv[1]
class QuietH(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
H=functools.partial(QuietH, directory=root)
srv=http.server.ThreadingHTTPServer(('127.0.0.1',8765),H); threading.Thread(target=srv.serve_forever,daemon=True).start()
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for name in ['bel-agrisi','bel-fitigi','diz-kireclenmesi','bilgi','index']:
            for vw,tag in [(1280,'pc'),(390,'tel')]:
                pg=await b.new_page(viewport={'width':vw,'height':900})
                errs=[]
                pg.on('pageerror',lambda e: errs.append(str(e)))
                pg.on('console',lambda m: errs.append('console:'+m.text) if m.type=='error' else None)
                await pg.route('**/*', lambda r: r.abort() if not r.request.url.startswith('http://127.0.0.1') else r.continue_())
                await pg.goto(f'http://127.0.0.1:8765/{name}.html'); await pg.wait_for_timeout(1200)
                over=await pg.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth')
                await pg.screenshot(path=f'shot_{name}_{tag}.png', full_page=True)
                print(name,tag,'overflow',over,'errors',[e for e in errs if 'net::' not in e][:3])
                await pg.close()
        await b.close()
asyncio.run(main())
