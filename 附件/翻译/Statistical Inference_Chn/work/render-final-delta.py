from pathlib import Path
import sys,json,hashlib
B=Path(__file__).resolve().parents[1];sys.path.insert(0,str(B/'work/python-deps'))
import pymupdf as fitz
from PIL import Image,ImageDraw
before=json.loads((B/'work/wholebook-review/manifest.json').read_text(encoding='utf-8'))
pdf=B/'work/Statistical Inference_Chn.pdf';doc=fitz.open(pdf)
out=B/'work/wholebook-final-review';out.mkdir(exist_ok=True)
hashes=[];changed=[]
for i,page in enumerate(doc):
 pix=page.get_pixmap(dpi=120,alpha=False);h=hashlib.sha256(pix.samples).hexdigest();hashes.append(h)
 if i>=before['pages']or h!=before['page_pixel_sha256'][i]:
  changed.append(i+1);pix.save(out/f'p{i+1:04}.png')
sheets=[]
for start in range(0,len(changed),4):
 nums=changed[start:start+4];imgs=[Image.open(out/f'p{n:04}.png')for n in nums];w,h=imgs[0].size
 sheet=Image.new('RGB',(2*w+30,2*h+80),'#e5e7eb');draw=ImageDraw.Draw(sheet)
 for j,(n,im)in enumerate(zip(nums,imgs)):
  x=(j%2)*(w+10)+10;y=(j//2)*(h+35)+30;sheet.paste(im,(x,y));draw.text((x+8,y-22),f'PDF {n}',fill='black')
 name=f'changes-{start//4+1:03}.png';sheet.save(out/name);sheets.append({'file':name,'pages':nums})
manifest={'pdf':str(pdf),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pages':len(doc),'dpi':120,'page_pixel_sha256':hashes,'sheets':sheets}
(out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
delta={'before_pdf_sha256':before['pdf_sha256'],'after_pdf_sha256':manifest['pdf_sha256'],'before_pages':before['pages'],'after_pages':len(doc),'changed_pages':changed,'unchanged_pages':[i for i in range(1,len(doc)+1)if i not in changed],'reviewed_pages':[],'sheets':sheets,'method':'相同120dpi渲染设置，对全部页比较RGB像素SHA256；变化页须实际目视后补入reviewed_pages。'}
(B/'work/wholebook-visual-delta.json').write_text(json.dumps(delta,ensure_ascii=False,indent=2),encoding='utf-8')
print('Changed',len(changed),'of',len(doc),'pages:',changed)
