import sys,pathlib,json
b=pathlib.Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn');sys.path.insert(0,str(b/'work/python-deps'));import pymupdf as f
s=f.open(json.loads((b/'work/source-baseline.json').read_text())['path']);a=b/'assets/chapter11';a.mkdir(parents=True,exist_ok=True)
for name,p,box in [('11.3.1',469,(85,55,418,484)),('11.3.2',474,(130,55,374,201)),('11.3.3',486,(101,55,405,485))]:
 d=f.open();r=f.Rect(box);q=d.new_page(width=r.width,height=r.height);q.show_pdf_page(q.rect,s,p-1,clip=r);d.save(a/f'fig-{name}.pdf');q.get_pixmap(matrix=f.Matrix(2,2)).save(b/f'work/ch11-source/fig-{name}.png')
