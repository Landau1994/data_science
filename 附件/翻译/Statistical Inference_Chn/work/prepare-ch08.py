from pathlib import Path
import json,sys
r=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(r/'work/python-deps'))
import pymupdf as fitz
doc=fitz.open(json.loads((r/'work/source-baseline.json').read_text(encoding='utf-8'))['path'])
d=r/'work/ch08-source';d.mkdir(exist_ok=True)
for n in range(333,368):
 p=d/f'p{n}.png'
 if not p.exists():doc[n-1].get_pixmap(dpi=120).save(p)
print('Rendered source pages 333–367; visual review pending.')
