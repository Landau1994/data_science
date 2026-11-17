from pathlib import Path
import sys, re, json, hashlib, subprocess
BASE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE/'work/python-deps'))
import pymupdf as fitz
from PIL import Image,ImageDraw
SOURCE=next((BASE.parents[1]/'books').glob('George Casella*.pdf'))
d=fitz.open(SOURCE)
for folder in ['frontmatter','sections-tex','assets','work/render-source']:
    (BASE/folder).mkdir(parents=True,exist_ok=True)
subprocess.run(['pdftotext','-layout',str(SOURCE),str(BASE/'work/source-layout.txt')],check=True)
pages=(BASE/'work/source-layout.txt').read_text(encoding='utf-8').split('\f')
(BASE/'work/reference-plan.json').write_text(json.dumps([{'physical_page':i+1,'kind':m[0],'number':m[1]} for i,t in enumerate(pages[:68]) for m in re.findall(r'\b(Definition|Theorem|Example|Figure|Table|Exercise|Section)\s+(\d+(?:\.\d+)+)',t)],indent=2),encoding='utf-8')
(BASE/'work/source-baseline.json').write_text(json.dumps({'path':str(SOURCE),'sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'pages':len(d)},indent=2),encoding='utf-8')
for i in range(31):
    d[i].get_pixmap(dpi=110).save(BASE/f'work/render-source/front-{i+1:02}.png')
for start in range(0,31,4):
    ims=[]
    for i in range(start,min(start+4,31)):
        im=Image.open(BASE/f'work/render-source/front-{i+1:02}.png').convert('RGB')
        im.thumbnail((850,1100))
        ims.append((i+1,im))
    sheet=Image.new('RGB',(1700,2260),'#dddddd'); draw=ImageDraw.Draw(sheet)
    for j,(num,im) in enumerate(ims):
        x=(j%2)*850;y=(j//2)*1130
        sheet.paste(im,(x,y+25));draw.text((x+10,y+5),f'PDF {num}',fill='black')
    sheet.save(BASE/f'work/render-source/contact-{start+1:02}.png')
print('prepared',len(d),'source pages')
