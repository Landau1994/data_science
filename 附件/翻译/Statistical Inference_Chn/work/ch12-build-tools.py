import sys,pathlib,json,re
b=pathlib.Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn')
sys.path.insert(0,str(b/'work/python-deps'));import pymupdf as fitz
src=fitz.open(json.loads((b/'work/source-baseline.json').read_text(encoding='utf-8'))['path'])
a=b/'assets/chapter12';a.mkdir(exist_ok=True)
for name,page,rect in [('12.2.1',501,(160,55,352,250)),('12.2.2',503,(94,55,410,470)),('12.2.3',509,(110,55,390,272)),('12.3.1',512,(60,400,440,615)),('12.4.1',516,(125,230,385,463))]:
    target=a/f'fig-{name}.pdf'
    if not target.exists():
        r=fitz.Rect(rect);d=fitz.open();p=d.new_page(width=r.width,height=r.height);p.show_pdf_page(p.rect,src,page-1,clip=r);d.save(target);d.close()
    d=fitz.open(target);d[0].get_pixmap(matrix=fitz.Matrix(2,2)).save(b/f'work/ch12-source/fig-{name}.png')
s=(b/'Statistical Inference_Chn.tex').read_text(encoding='utf-8').split(r'\begin{document}')[0]
s+=r'\providecommand{\sourcepageanchor}[1]{\phantomsection\label{src:#1}}'+'\n'+r'\begin{document}\setcounter{section}{11}'+'\n'
s+=(b/'chapters-tex/12.tex').read_text(encoding='utf-8').split(r'\input')[0]+'\n'
for f in sorted((b/'sections-tex').glob('12-*.tex')):s+=r'\input{'+f.relative_to(b).as_posix()+'}\n'
s+=r'\end{document}'
(b/'work/ch12-preview.tex').write_text(s,encoding='utf-8');(b/'work/ch12-build').mkdir(exist_ok=True)
