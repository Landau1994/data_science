import sys,pathlib,json
b=pathlib.Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn');sys.path.insert(0,str(b/'work/python-deps'));import pymupdf as f
s=f.open(json.loads((b/'work/source-baseline.json').read_text())['path']);a=b/'assets/chapter9'
for name,p,box in [('9.2.3',384,(135,267,368,415)),('9.2.4',385,(102,169,402,324)),('9.2.5',386,(101,56,405,242))]:
 d=f.open();r=f.Rect(box);q=d.new_page(width=r.width,height=r.height);q.show_pdf_page(q.rect,s,p-1,clip=r);d.save(a/f'fig-{name}.pdf');q.get_pixmap(matrix=f.Matrix(2,2)).save(b/f'work/ch09-source/fig-{name}.png')
