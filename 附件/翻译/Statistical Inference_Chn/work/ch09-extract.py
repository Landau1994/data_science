import sys,json,pathlib
base=pathlib.Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn')
sys.path.insert(0,str(base/'work/python-deps'))
import pymupdf as fitz
doc=fitz.open(json.loads((base/'work/source-baseline.json').read_text())['path'])
for n,start,end in [(9,368,407),(10,408,451),(11,452,497),(12,498,526)]:
 out=base/f'work/ch{n:02d}-source';out.mkdir(exist_ok=True)
 with (base/f'work/ch{n:02d}-source.txt').open('w',encoding='utf-8') as f:
  for p in range(start,end+1):
   f.write(f'\n\n=== PDF {p}; PRINT {p-31} ===\n'+doc[p-1].get_text(sort=True))
   doc[p-1].get_pixmap(matrix=fitz.Matrix(1.6,1.6)).save(out/f'page-{p:03d}.png')
print('Rendered ch9-12 source pages 368-526')
