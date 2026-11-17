from pathlib import Path
import sys,re,json
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'work/python-deps'))
import pymupdf as fitz
src=next((ROOT.parents[1]/'books').glob('George Casella*.pdf'))
d=fitz.open(src)
figs=[('fig-1-5-1',56,(.105,.075,.89,.415)),('fig-1-5-2',58,(.16,.075,.83,.365)),('fig-1-6-1',61,(.16,.08,.84,.305))]
for name,page,ratios in figs:
    p=d[page-1]; w,h=p.rect.width,p.rect.height
    rect=fitz.Rect(ratios[0]*w,ratios[1]*h,ratios[2]*w,ratios[3]*h)
    out=fitz.open(); q=out.new_page(width=rect.width,height=rect.height)
    q.show_pdf_page(q.rect,d,page-1,clip=rect)
    out.save(ROOT/'assets/chapter1'/f'{name}.pdf')
    q.get_pixmap(matrix=fitz.Matrix(2,2)).save(ROOT/'work'/f'{name}.png')
counts={}; labels=[]; issues=[]
for i in range(3,7):
    path=ROOT/'sections-tex'/f'01-{i:02}.tex'; t=path.read_text('utf-8')
    envs=re.findall(r'\\(begin|end)\{([^}]+)\}',t); stack=[]
    for typ,env in envs:
        if typ=='begin':stack.append(env)
        elif not stack or stack.pop()!=env:issues.append((path.name,env))
    if stack: issues.append((path.name,stack))
    labels+=re.findall(r'\\label\{([^}]+)\}',t)
    counts[path.name]={e:len(re.findall(r'\\begin\{'+e+r'\}',t)) for e in ['definition','example','theorem','proof','equation','equation\*','figure','tabular']}
    counts[path.name]['double_dollar_pairs']=t.count('$$')//2
(ROOT/'work/ch01b-static.json').write_text(json.dumps({'counts':counts,'environment_issues':issues,'duplicate_labels':[x for x in set(labels) if labels.count(x)>1]},indent=2,ensure_ascii=False),'utf-8')
tex=r'''\documentclass[UTF8,12pt]{ctexart}
\usepackage[a4paper,left=2.5cm,right=2.5cm,top=3cm,bottom=3cm]{geometry}
\usepackage{amsmath,amsthm,amssymb,mathrsfs,graphicx,enumitem,multirow,hyperref}
\newtheorem{theorem}{定理}[subsection]
\newtheorem{definition}[theorem]{定义}
\newtheorem{example}[theorem]{例}
\numberwithin{equation}{subsection}
\numberwithin{figure}{subsection}
\renewcommand{\proofname}{证明}
\newcommand{\sourcepageref}[2]{#2}
\setlength{\emergencystretch}{1em}
\begin{document}
\setcounter{section}{1}\setcounter{subsection}{2}
\input{sections-tex/01-03.tex}
\input{sections-tex/01-04.tex}
\input{sections-tex/01-05.tex}
\input{sections-tex/01-06.tex}
\end{document}
'''
(ROOT/'work/ch01b-preview.tex').write_text(tex,'utf-8')
print(json.dumps(counts,ensure_ascii=False));print('environment issues',issues)
