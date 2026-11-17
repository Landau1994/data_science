from pathlib import Path
import re
B=Path(__file__).resolve().parents[1]
for name,title,label in [('contents','原书目录（原书页码）','source-contents'),('tables','表目录（原书页码）','tables'),('figures','图目录（原书页码）','figures')]:
    rows=[]
    for line in (B/f'work/front-{name}.tsv').read_text(encoding='utf-8').splitlines():
        cells=line.split('|'); text,page=cells[:2]; target=int(cells[2]) if len(cells)>2 else int(page)+31
        rows.append(r'\sourcepageref{'+str(target)+'}{'+text+'} & '+r'\sourcepageref{'+str(target)+'}{'+page+r'} \\')
    prefix='\\section*{'+title+'}\\label{front:'+label+'}\n'
    if name!='contents':prefix+='\\addcontentsline{toc}{section}{'+title+'}\n'
    prefix+='\\begingroup\\small\n\\begin{longtable}{@{}p{.86\\textwidth}r@{}}\n'
    (B/f'frontmatter/00-{name}.tex').write_text(prefix+'\n'.join(rows)+'\n\\end{longtable}\\endgroup\n',encoding='utf-8')
src=(B.parent/'Statistical Optimal Transport_Chn/Statistical Optimal Transport_Chn.tex').read_text(encoding='utf-8')
preamble=src[:src.index(r'\newcommand{\externalref}')]
preamble=preamble.replace(r'\newtheorem{theorem}{定理}[section]',r'\newtheorem{theorem}{定理}[subsection]')
preamble=preamble.replace(r'\newtheorem{exercise}{习题}',r'\newtheorem{exercise}{习题}[section]')
preamble=preamble.replace(r'\numberwithin{equation}{section}',r'\numberwithin{equation}{subsection}')
preamble=preamble.replace(r'\numberwithin{figure}{section}',r'\numberwithin{figure}{subsection}'+'\n'+r'\numberwithin{table}{subsection}')
source=next((B.parents[1]/'books').glob('George Casella*.pdf'))
extra=r'''
\usepackage{longtable,booktabs,enumitem,array,xurl,float}
\setlist[enumerate,1]{label=(\alph*),leftmargin=2.6em}
\setlength{\emergencystretch}{2em}
\setcounter{tocdepth}{3}
\setcounter{secnumdepth}{3}
\renewcommand{\subsubsectionautorefname}{节}
\newcommand{\sourcepageref}[2]{\href[page=#1]{SOURCEPATH}{#2}}
\hypersetup{pdftitle={统计推断：书前材料及第1章中文译稿},pdfauthor={George Casella; Roger L. Berger},bookmarksnumbered=true}
\begin{document}
\hypersetup{pageanchor=false}
\begin{titlepage}
\noindent\rule{\textwidth}{1.2pt}\\[0.1cm]\rule{\textwidth}{.8pt}\\[1.4cm]
{\fontsize{40pt}{52pt}\selectfont\bfseries 统计推断}\\[.8cm]
{\fontsize{22pt}{30pt}\selectfont\textit{Statistical Inference}}\\[1cm]
\rule{\textwidth}{.6pt}\\[1cm]
{\Large 第二版}\\[1cm]
{\large George Casella\\[.15cm]Roger L. Berger}\\[1.2cm]
{\small 2001年第二版的2024年CRC重印本.\\
中文译稿：书前材料及第1章.\\
按章校对，持续汇总全书；原书版权归原权利人.\\
原编号与原疑误保留；核验范围及说明见DS011统一台账.}
\vfill\begin{flushright}\small 2026年11月4日\end{flushright}
\end{titlepage}
\pagenumbering{roman}\hypersetup{pageanchor=true}
\input{frontmatter/00-publication.tex}
\input{frontmatter/00-contents.tex}
\input{frontmatter/00-preface-second.tex}
\input{frontmatter/00-preface-first.tex}
\input{frontmatter/00-authors.tex}
\input{frontmatter/00-tables.tex}
\input{frontmatter/00-figures.tex}
\input{frontmatter/00-example-list.tex}
\clearpage\renewcommand{\contentsname}{本册译稿目录}\tableofcontents\clearpage
\pagenumbering{arabic}
\section{概率论}\label{sec:1}
INPUTS
\end{document}
'''
extra=extra.replace('SOURCEPATH', '../../books/'+source.name)
extra=extra.replace('INPUTS','\n'.join(r'\input{sections-tex/01-'+str(i).zfill(2)+'.tex}' for i in range(9)))
(B/'Statistical Inference_Chn.tex').write_text(preamble+extra,encoding='utf-8')
print('frontmatter tables/contents and main written')
