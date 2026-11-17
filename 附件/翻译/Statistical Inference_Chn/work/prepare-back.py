from pathlib import Path
import sys,json
B=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(B/'work/python-deps'))
import pymupdf as fitz
s=json.loads((B/'work/source-baseline.json').read_text(encoding='utf-8'))
d=fitz.open(s['path'])
r=B/'work/back-source';r.mkdir(exist_ok=True)
for n in range(528,567):
    d[n-1].get_pixmap(dpi=120).save(r/f'{n}.png')
print('Rendered source PDF 528–566.')
