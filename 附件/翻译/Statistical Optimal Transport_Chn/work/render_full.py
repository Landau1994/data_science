from pathlib import Path
from PIL import Image,ImageDraw
import sys,json,hashlib
sys.path.insert(0,r'E:/project/math/ant/tmp/pypackages')
import pymupdf as fitz
BASE=Path(__file__).resolve().parents[1]
d=fitz.open(BASE/'work/full-build/Statistical Optimal Transport_Chn.pdf')
OUT=BASE/'work/full-temp/output-pages'; OUT.mkdir(parents=True,exist_ok=True)
hashes={}
for i,p in enumerate(d):
    path=OUT/f'page-{i+1:03}.png'; p.get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(path)
    hashes[str(i+1)]=hashlib.sha256(path.read_bytes()).hexdigest()
for start in range(1,len(d)+1,4):
    nums=list(range(start,min(len(d)+1,start+4)))
    ims=[Image.open(OUT/f'page-{n:03}.png').convert('RGB') for n in nums]
    w=max(im.width for im in ims); h=max(im.height for im in ims)+25
    canvas=Image.new('RGB',(w*2,h*((len(ims)+1)//2)),'white'); draw=ImageDraw.Draw(canvas)
    for k,(n,im) in enumerate(zip(nums,ims)):
        x=(k%2)*w; y=(k//2)*h; draw.text((x+8,y+5),f'Output physical {n}',fill='black'); canvas.paste(im,(x,y+25))
    canvas.save(OUT/f'contact-{nums[0]:03}-{nums[-1]:03}.png')
(BASE/'work/full-output-page-digests.json').write_text(json.dumps(hashes,indent=2),encoding='utf-8')
print('Rendered',len(d),'pages with',((len(d)+3)//4),'four-page contacts.')
