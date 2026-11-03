from pathlib import Path
import sys, json, subprocess, re
sys.path.insert(0,r'E:/project/math/ant/tmp/pypackages')
import pymupdf as fitz
BASE=Path(__file__).resolve().parents[1]
SOURCE=BASE.parents[1]/'books/Statistical Optimal Transport.pdf'
d=fitz.open(SOURCE)
TEMP=BASE/'work/full-temp'
(TEMP/'pages').mkdir(parents=True,exist_ok=True)
ranges={'front':(1,14),'02':(51,90),'03':(91,108),'04':(109,133),'05':(134,162),'06':(163,198),'07':(199,222),'08':(223,239),'A':(240,246),'B':(247,249),'references':(250,265),'index':(266,267),'publisher':(268,269)}
for key,(lo,hi) in ranges.items():
    layout=TEMP/f'{key}-layout.txt'
    if not layout.exists(): subprocess.run(['pdftotext','-layout','-f',str(lo),'-l',str(hi),str(SOURCE),str(layout)],check=True)
    alt=TEMP/f'{key}-mathtext.txt'
    if not alt.exists(): alt.write_text('\n\f\n'.join(f'PHYSICAL PAGE {i+1}\n'+d[i].get_text() for i in range(lo-1,hi)),encoding='utf-8')
    for i in range(lo-1,hi):
        p=TEMP/'pages'/f'physical-{i+1:03}.png'
        if not p.exists(): d[i].get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save(p)
(BASE/'work/full-page-ranges.json').write_text(json.dumps(ranges,ensure_ascii=False,indent=2),encoding='utf-8')
(BASE/'work/full-toc-source.json').write_text(json.dumps(d.get_toc(),ensure_ascii=False,indent=2),encoding='utf-8')
print('Prepared original physical ranges:',ranges)
