import sys,pathlib,json
b=pathlib.Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn');sys.path.insert(0,str(b/'work/python-deps'));import pymupdf as f
s=f.open(json.loads((b/'work/source-baseline.json').read_text())['path']);r=f.Rect(108,143,396,449);d=f.open();p=d.new_page(width=r.width,height=r.height);p.show_pdf_page(p.rect,s,393,clip=r);d.save(b/'assets/chapter9/fig-9.3.1.pdf');p.get_pixmap(matrix=f.Matrix(2,2)).save(b/'work/ch09-source/fig-9.3.1.png')
