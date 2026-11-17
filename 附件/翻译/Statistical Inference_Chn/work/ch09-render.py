import pathlib,sys
b=pathlib.Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn');sys.path.insert(0,str(b/'work/python-deps'));import pymupdf as f
p=f.open(b/'work/ch09-build/ch09-preview.pdf');o=b/'work/ch09-output';o.mkdir(exist_ok=True)
for i,page in enumerate(p):page.get_pixmap(matrix=f.Matrix(1.3,1.3)).save(o/f'page-{i+1:03d}.png')
print(len(p))
