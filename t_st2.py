import zxingcpp, io, numpy as np, cv2, sys
from PIL import Image, ImageFilter
def persp(im, k):
    a=np.array(im); h,w=a.shape[:2]
    src=np.float32([[0,0],[w,0],[w,h],[0,h]]); dst=np.float32([[w*k,h*k*.5],[w*(1-k*.3),0],[w,h],[0,h*(1-k*.2)]])
    M=cv2.getPerspectiveTransform(src,dst); return Image.fromarray(cv2.warpPerspective(a,M,(w,h),borderValue=(40,57,30)))
def run(im):
    ok=tot=0; fails=[]
    for k in (0,.12):
        for rot in (0,10,-18,25):
            for blur in (0,1.5,2.5):
                for w in (180,240,320):
                    j=persp(im,k) if k else im
                    j=j.rotate(rot,expand=True,fillcolor=(40,57,30)).filter(ImageFilter.GaussianBlur(blur)); j=j.resize((w,int(w*j.height/j.width)))
                    b=io.BytesIO(); j.save(b,"JPEG",quality=50); j=Image.open(b)
                    r=zxingcpp.read_barcodes(j); g=bool(r and r[0].text.lower().startswith("https://wa.me/905538815568")); ok+=g; tot+=1
                    if not g: fails.append((k,rot,blur,w))
    return ok,tot,fails
if __name__=="__main__":
    print(sys.argv[1], run(Image.open(sys.argv[1]).convert("RGB")))
