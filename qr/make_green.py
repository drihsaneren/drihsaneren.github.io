import qrcode, cv2, numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps
def make(qr_px=740, logo_w=236, clear_w=10, clear_h=8.6, out="karekod-kartvizit-yesil.png"):
    URL = "https://drihsaneren.com"
    BG, FG = (40, 57, 25), (199, 196, 135)
    CW, CH, SS = 1600, 1035, 2
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, border=0)
    qr.add_data(URL); qr.make(fit=True); m = qr.get_matrix(); n = len(m)
    W, H = CW*SS, CH*SS; ms = qr_px*SS/n
    ox, oy = (W - n*ms)/2, (H - n*ms)/2
    # background with a little grain
    rng = np.random.default_rng(7)
    base = np.zeros((H, W, 3), np.float32) + np.array(BG, np.float32)
    base += rng.normal(0, 2.2, (H, W, 1)).astype(np.float32)
    bg = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))
    shapes = Image.new("L", (W, H), 0); d = ImageDraw.Draw(shapes)
    box = lambda x,y,w,h,r,f: d.rounded_rectangle([x,y,x+w,y+h], radius=r, fill=f)
    inf = lambda x,y: (x<7 and y<7) or (x>=n-7 and y<7) or (x<7 and y>=n-7)
    cx0, cy0 = (n-clear_w)/2, (n-clear_h)/2
    inc = lambda x,y: cx0-0.2 <= x+0.5 <= cx0+clear_w+0.2 and cy0-0.2 <= y+0.5 <= cy0+clear_h+0.2
    g = 0.07*ms
    for y in range(n):
        for x in range(n):
            if m[y][x] and not inf(x,y) and not inc(x,y):
                box(ox+x*ms+g, oy+y*ms+g, ms-2*g, ms-2*g, 0.2*ms, 255)
    for fx,fy in ((0,0),(n-7,0),(0,n-7)):
        px,py = ox+fx*ms, oy+fy*ms
        box(px,py,7*ms,7*ms,0.55*ms,255); box(px+ms,py+ms,5*ms,5*ms,0.35*ms,0); box(px+2*ms,py+2*ms,3*ms,3*ms,0.4*ms,255)
    # soft drop shadow for a slight printed-emboss feel
    sh = shapes.filter(ImageFilter.GaussianBlur(3*SS))
    shadow = Image.new("RGB", (W,H), (10, 16, 5))
    bg.paste(shadow, (int(2*SS), int(3*SS)), sh.point(lambda v: int(v*0.55)))
    bg.paste(Image.new("RGB",(W,H),FG), (0,0), shapes)
    # logo straight on the green, with its own soft shadow
    logo = Image.open("../site/img/logo.png").convert("RGBA")
    lw = int(logo_w*SS); lh = int(lw*logo.height/logo.width); lg = logo.resize((lw,lh), Image.LANCZOS)
    lx, ly = int((W-lw)/2), int((H-lh)/2)
    la = lg.split()[3].filter(ImageFilter.GaussianBlur(3*SS)).point(lambda v:int(v*0.5))
    bg.paste(Image.new("RGB",(lw,lh),(10,16,5)), (lx+2*SS, ly+3*SS), la)
    bg.paste(lg, (lx,ly), lg)
    img = bg.resize((CW,CH), Image.LANCZOS); img.save(out, dpi=(470,470))
    det = cv2.QRCodeDetector(); res=[]
    inv = ImageOps.invert(img)
    for s in (1600,1200,900,700,500):
        inv.resize((s, int(s*CH/CW))).save("/tmp/_g.png"); v,_,_ = det.detectAndDecode(cv2.imread("/tmp/_g.png")); res.append(1 if v==URL else 0)
    return n, res
if __name__ == "__main__":
    for kw in [dict(), dict(clear_w=9, clear_h=8), dict(qr_px=760, clear_w=9.4, clear_h=8)]:
        print(kw, make(out="/tmp/_try.png", **kw))
