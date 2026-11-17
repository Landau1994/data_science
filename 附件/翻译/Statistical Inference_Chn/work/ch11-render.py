import sys,pathlib
b=pathlib.Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn');sys.path.insert(0,str(b/'work/python-deps'));import pymupdf as f
d=f.open(b/'work/ch11-build/ch11-preview.pdf');o=b/'work/ch11-output';o.mkdir(exist_ok=True)
for i,p in enumerate(d):p.get_pixmap(matrix=f.Matrix(1.3,1.3)).save(o/f'page-{i+1:03}.png')
print(len(d))
