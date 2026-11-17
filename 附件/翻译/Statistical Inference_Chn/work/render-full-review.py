from pathlib import Path
import sys,json,hashlib
B=Path(__file__).resolve().parents[1];sys.path.insert(0,str(B/'work/python-deps'))
import pymupdf as fitz
from PIL import Image,ImageDraw
pdf=B/'work/Statistical Inference_Chn.pdf'
out=B/'work/wholebook-review';out.mkdir(exist_ok=True)
doc=fitz.open(pdf);hashes=[]
for i,page in enumerate(doc):
    p=out/f'p{i+1:04}.png';pix=page.get_pixmap(dpi=120,alpha=False)
    pix.save(p);hashes.append(hashlib.sha256(pix.samples).hexdigest())
for start in range(1,len(doc)+1,4):
    nums=list(range(start,min(start+4,len(doc)+1)));imgs=[Image.open(out/f'p{n:04}.png')for n in nums]
    w,h=imgs[0].size;sheet=Image.new('RGB',(2*w+30,2*h+80),'#e5e7eb');draw=ImageDraw.Draw(sheet)
    for j,(n,im)in enumerate(zip(nums,imgs)):
        x=(j%2)*(w+10)+10;y=(j//2)*(h+35)+30
        sheet.paste(im,(x,y));draw.text((x+8,y-22),f'PDF {n}',fill='black')
    sheet.save(out/f'sheet{start:04}-{nums[-1]:04}.png')
manifest={'pdf':str(pdf),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pages':len(doc),'dpi':120,'page_pixel_sha256':hashes}
(out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print('Rendered',len(doc),'pages and',(len(doc)+3)//4,'four-page sheets into',out)
