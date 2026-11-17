import sys,pathlib
b=pathlib.Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn');sys.path.insert(0,str(b/'work/python-deps'));import pymupdf as f
d=f.open(b/'work/ch10-build/ch10-preview.pdf');out=b/'work/ch10-output';out.mkdir(exist_ok=True)
for i,p in enumerate(d):p.get_pixmap(matrix=f.Matrix(1.3,1.3)).save(out/f'page-{i+1:03d}.png')
print(len(d))
