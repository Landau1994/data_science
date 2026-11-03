from pathlib import Path
import re, subprocess, sys
BASE=Path(__file__).resolve().parents[1]
NAME='Statistical Optimal Transport_Chn'
SKILL=Path(r'C:/Users/Administrator/.codex/skills/pdf-to-chinese-tex')
# Reuse the repaired original template preamble from the verified chapter.
# Strip a previous full-book extension so this generator is idempotent.
current=(BASE/(NAME+'.tex')).read_text('utf-8').split(r'\begin{document}')[0]
current=current.split('% FULL BOOK EXTENSIONS')[0]
current=re.sub(r'\\renewcommand\{\\refname\}\{[^}]*\}',r'\\renewcommand{\\refname}{参考文献}',current)
current=re.sub(r'\\hypersetup\{pdftitle=.*?bookmarksnumbered=true\}',r'\\hypersetup{pdftitle={统计最优传输：完整中文译稿},pdfauthor={Sinho Chewi; Jonathan Niles-Weed; Philippe Rigollet},bookmarksnumbered=true}',current,flags=re.S)
extra=r'''
% FULL BOOK EXTENSIONS
\usepackage{wrapfig,multicol,makeidx,xurl}
\setlength{\emergencystretch}{1em}
\newaliascnt{assumption}{theorem}
\newtheorem{assumption}[assumption]{假设}
\aliascntresetthe{assumption}
\providecommand{\assumptionautorefname}{假设}
\newtheorem*{remark*}{注}
\makeatletter
\@addtoreset{exercise}{section}
\@addtoreset{footnote}{section}
\providecommand{\theHexercise}{\thesection.\arabic{exercise}}
\renewcommand{\theHexercise}{\thesection.\arabic{exercise}}
\makeatother
\makeindex
\providecommand{\appendixautorefname}{附录}
\renewcommand{\appendixautorefname}{附录}
\renewcommand{\indexname}{索引}
\renewcommand{\seename}{见}
\makeatletter
\renewenvironment{theindex}{%
  \clearpage\phantomsection\section*{索引}\label{sec:index}%
  \addcontentsline{toc}{section}{索引}%
  \@mkboth{索引}{索引}\thispagestyle{plain}%
  \parindent\z@\parskip\z@\@plus.3\p@\relax%
  \columnsep 28\p@\columnseprule\z@\let\item\@idxitem%
  \begin{multicols}{2}\small%
}{\end{multicols}}
\makeatother
'''
body=r'''
\begin{document}
\hypersetup{pageanchor=false}
\begin{titlepage}
\flushleft
\rule{\textwidth}{1.2pt}\\[0.1cm]
\rule{\textwidth}{0.8pt}\\[1.4cm]
{\fontsize{40pt}{52pt}\selectfont\bfseries 统计最优传输}\\[0.8cm]
{\fontsize{22pt}{30pt}\selectfont\textit{Statistical Optimal Transport}}\\[1.0cm]
\rule{\textwidth}{0.6pt}\\[1.0cm]
{\Large 圣弗卢尔概率论暑期学校\\[0.3cm]第XLIX届——2019年}\\[1cm]
{\large Sinho Chewi\\[0.15cm]Jonathan Niles-Weed\\[0.15cm]Philippe Rigollet}\\[1.2cm]
{\small Lecture Notes in Mathematics 2364；Springer，2025.\\
本稿为学习用完整中文译稿，原书版权归原权利人.\\
章节、陈述、公式、图及习题编号沿用原书.\\
来源疑误照录并另记于随附核验说明.}
\vfill
\begin{flushright}{\small 中文译稿整理于2026年11月3日}\end{flushright}
\end{titlepage}
\pagenumbering{roman}\hypersetup{pageanchor=true}
\input{frontmatter/00-series.tex}
\input{frontmatter/00-school.tex}
\input{frontmatter/00-title.tex}
\input{frontmatter/00-copyright.tex}
\begingroup\renewcommand{\thefigure}{\arabic{figure}}
\input{frontmatter/00-preface.tex}
\endgroup
\clearpage\tableofcontents\clearpage
\pagenumbering{arabic}
'''
chapters=[('最优传输',8),('Wasserstein距离的估计',10),('传输映射的估计',8),('熵正则最优传输',6),('Wasserstein梯度流：理论',10),('Wasserstein梯度流：应用',8),('Wasserstein空间的度量几何',5),('Wasserstein重心',5)]
inputs=[]
for n,(title,count) in enumerate(chapters,1):
    body+=f'\\section{{{title}}}\\label{{sec:{n}}}\n'
    for k in range(1,count+1):
        rel=f'sections-tex/{n:02}-{k:02}.tex'
        inputs.append(rel)
        body+=f'\\input{{{rel}}}\n'
body+=r'\appendix'+'\n'
for letter,title,count in [('A','凸分析',3),('B','概率论',1)]:
    body+=f'\\section{{{title}}}\\label{{sec:{letter}}}\n'
    for k in range(1,count+1):
        rel=f'sections-tex/{letter}-{k:02}.tex'; inputs.append(rel)
        body+=f'\\input{{{rel}}}\n'
body+=r'''
\clearpage\phantomsection\addcontentsline{toc}{section}{参考文献}
\nocite{*}
\bibliographystyle{plain}
\bibliography{bib/references-full}
\input{backmatter/index-crossrefs.tex}
\printindex
\input{backmatter/publisher-policy.tex}
\end{document}
'''
missing=[p for p in inputs if not (BASE/p).exists()]
if missing:
    print('Waiting for source sections:',', '.join(missing))
    # Do not replace the verified chapter-only main file until all source
    # fragments exist. A draft generator output stays in the work directory.
    (BASE/'work/full-main-draft.tex').write_text(current+extra+body,encoding='utf-8')
else:
    (BASE/(NAME+'.tex')).write_text(current+extra+body,encoding='utf-8')
    print('Created full-book main file with',len(inputs),'unique section inputs.')
