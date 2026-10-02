import sys, qrcode, cv2
from PIL import Image, ImageDraw
def make(badge_mod, fr, gapf, ec, out):
    URL = "https://drihsaneren.com"
    BG, DK = (241, 234, 215), (29, 39, 28)
    qr = qrcode.QRCode(error_correction=ec, border=0); qr.add_data(URL); qr.make(fit=True)
    m = qr.get_matrix(); n = len(m); Q = 4; SS = 3; OUT = 1600
    W = OUT*SS; ms = W/(n+2*Q)
    img = Image.new("RGB", (W, W), BG); d = ImageDraw.Draw(img)
    box = lambda x,y,w,h,r,f: d.rounded_rectangle([x,y,x+w,y+h], radius=r, fill=f)
    inf = lambda x,y: (x<7 and y<7) or (x>=n-7 and y<7) or (x<7 and y>=n-7)
    c0 = (n-badge_mod)/2
    inb = lambda x,y: badge_mod>0 and c0-0.3 <= x+0.5 <= c0+badge_mod+0.3 and c0-0.3 <= y+0.5 <= c0+badge_mod+0.3
    g = gapf*ms
    for y in range(n):
        for x in range(n):
            if m[y][x] and not inf(x,y) and not inb(x,y):
                box((x+Q)*ms+g, (y+Q)*ms+g, ms-2*g, ms-2*g, 0.18*ms, DK)
    for fx,fy in ((0,0),(n-7,0),(0,n-7)):
        ox,oy = (fx+Q)*ms,(fy+Q)*ms
        box(ox,oy,7*ms,7*ms,fr*ms,DK); box(ox+ms,oy+ms,5*ms,5*ms,fr*0.6*ms,BG); box(ox+2*ms,oy+2*ms,3*ms,3*ms,fr*0.5*ms,DK)
    if badge_mod:
        bx=(c0+Q)*ms; bw=badge_mod*ms
        box(bx,bx,bw,bw,1.4*ms,DK)
        logo = Image.open("../site/img/logo.png").convert("RGBA")
        lw=int(bw*0.8); lh=int(lw*logo.height/logo.width); lg=logo.resize((lw,lh),Image.LANCZOS)
        img.paste(lg,(int(bx+(bw-lw)/2),int(bx+(bw-lh)/2)),lg)
    img = img.resize((OUT,OUT), Image.LANCZOS); img.save(out, dpi=(300,300))
    det = cv2.QRCodeDetector(); res=[]
    for s in (1600,1200,800,400,250):
        img.resize((s,s)).save("/tmp/_t.png"); v,_,_ = det.detectAndDecode(cv2.imread("/tmp/_t.png")); res.append(1 if v==URL else 0)
    return n, res
H = qrcode.constants.ERROR_CORRECT_H; Qv = qrcode.constants.ERROR_CORRECT_Q
for args in [(7.5,0.5,0.06,H),(7,0.5,0.05,H),(0,0.5,0.06,H),(7.5,0.5,0.03,H),(8.5,0.5,0.05,H)]:
    print(args[:3], make(*args, out="/tmp/_try.png"))
