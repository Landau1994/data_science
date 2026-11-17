import pathlib
b=pathlib.Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn')
t=(b/'Statistical Inference_Chn.tex').read_text(encoding='utf-8').split(r'\begin{document}')[0]
t+=r'\providecommand{\sourcepageanchor}[1]{\phantomsection\label{src:#1}}'+'\n'+r'\begin{document}\setcounter{section}{8}\section{区间估计}\input{sections-tex/09-01.tex}\input{sections-tex/09-02.tex}\input{sections-tex/09-03.tex}\end{document}'
(b/'work/ch09-preview.tex').write_text(t,encoding='utf-8');(b/'work/ch09-build').mkdir(exist_ok=True)
