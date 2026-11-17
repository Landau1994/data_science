from pathlib import Path
import sys,json
B=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(B/'work/python-deps'))
import pymupdf as fitz
p=B/'work/back-preview.pdf';out=B/'work/back-render';out.mkdir(exist_ok=True)
d=fitz.open(p)
for i,page in enumerate(d):page.get_pixmap(dpi=100).save(out/f'{i+1:03}.png')
print('rendered',len(d))
