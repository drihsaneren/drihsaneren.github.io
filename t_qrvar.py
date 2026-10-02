import math, qrcode, cairosvg, io, sys
from PIL import Image
from t_st2 import run
def f(v): return f"{v:.2f}".rstrip("0").rstrip(".")
def build(data, ec, CLR, R, LW, shape="c", Q=3.4, erx=1.5, RR=.22):
    qr=qrcode.QRCode(error_correction=getattr(qrcode.constants,"ERROR_CORRECT_"+ec),border=0); qr.add_data(data); qr.make(fit=True)
    M=qr.get_matrix(); n=len(M); N=n+2*Q; c0=(n-CLR)//2
    fnd=lambda x,y:(x<7 and y<7) or (x>=n-7 and y<7) or (x<7 and y>=n-7)
    clr=lambda x,y:c0<=x<c0+CLR and c0<=y<c0+CLR
    on=lambda x,y:0<=x<n and 0<=y<n and M[y][x] and not fnd(x,y) and not clr(x,y)
    d=[]
    for y in range(n):
        for x in range(n):
            if not on(x,y): continue
            cx,cy=x+Q+.5,y+Q+.5
            if shape=="c": d.append(f"M{f(cx-R)} {f(cy)}a{f(R)} {f(R)} 0 1 0 {f(2*R)} 0a{f(R)} {f(R)} 0 1 0 {f(-2*R)} 0")
            else:
                h=R; r=RR; d.append(f"M{f(cx-h+r)} {f(cy-h)}h{f(2*h-2*r)}a{r} {r} 0 0 1 {r} {r}v{f(2*h-2*r)}a{r} {r} 0 0 1 -{r} {r}h{f(-(2*h-2*r))}a{r} {r} 0 0 1 -{r} -{r}v{f(-(2*h-2*r))}a{r} {r} 0 0 1 {r} -{r}z")
            if on(x+1,y): d.append(f"M{f(cx)} {f(cy)}h1")
            if on(x,y+1): d.append(f"M{f(cx)} {f(cy)}v1")
    eyes=""
    for fx,fy in ((0,0),(n-7,0),(0,n-7)):
        ox,oy=fx+Q,fy+Q
        eyes+=f'<rect x="{f(ox+.5)}" y="{f(oy+.5)}" width="6" height="6" rx="{erx}" fill="none" stroke="#101a13" stroke-width="1"/><rect x="{f(ox+2)}" y="{f(oy+2)}" width="3" height="3" rx=".8" fill="#101a13"/>'
    cxm=Q+n/2
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(N)} {f(N)}" width="416" height="416"><rect width="{f(N)}" height="{f(N)}" rx="3.2" fill="#f4ecd4"/>
<path d="{''.join(d)}" fill="#101a13" stroke="#101a13" stroke-width="{LW}" stroke-linecap="round"/>{eyes}
<circle cx="{f(cxm)}" cy="{f(cxm)}" r="{f(CLR/2-.35)}" fill="#fbf5e3" stroke="#c8963e" stroke-width=".18"/>
<circle cx="{f(cxm)}" cy="{f(cxm)}" r="{f(CLR/2-1.2)}" fill="#7a8a5a"/></svg>'''
    return svg,n
if __name__=="__main__":
    for cfg in [("https://wa.me/905538815568","Q",7,.5,.5,"c"),("https://wa.me/905538815568","Q",7,.46,.5,"s"),("https://wa.me/905538815568","M",5,.5,.5,"c"),("https://wa.me/905538815568","M",5,.46,.5,"s"),("HTTPS://WA.ME/905538815568","Q",5,.5,.5,"c"),("HTTPS://WA.ME/905538815568","Q",5,.46,.5,"s"),("https://wa.me/905538815568","Q",7,.5,.62,"c")]:
        svg,n=build(*cfg)
        png=cairosvg.svg2png(bytestring=svg.encode())
        im=Image.open(io.BytesIO(png)).convert("RGB")
        ok,tot,fails=run(im); print(cfg[1:],n,ok,tot)
