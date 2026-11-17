import sys,pathlib,json
b=pathlib.Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn');sys.path.insert(0,str(b/'work/python-deps'));import pymupdf as f
s=f.open(json.loads((b/'work/source-baseline.json').read_text())['path']);a=b/'assets/chapter10';a.mkdir(parents=True,exist_ok=True)
for name,p,box in [('10.1.1',417,(73,55,440,238)),('10.3.1',427,(117,56,389,196)),('10.4.1',437,(88,203,416,401)),('10.4.2',438,(92,55,410,264))]:
 d=f.open();r=f.Rect(box);q=d.new_page(width=r.width,height=r.height);q.show_pdf_page(q.rect,s,p-1,clip=r);d.save(a/f'fig-{name}.pdf');q.get_pixmap(matrix=f.Matrix(2,2)).save(b/f'work/ch10-source/fig-{name}.png')
