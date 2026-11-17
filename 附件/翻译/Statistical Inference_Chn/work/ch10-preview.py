import pathlib
b=pathlib.Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn')
s=(b/'Statistical Inference_Chn.tex').read_text(encoding='utf-8').split(r'\begin{document}')[0]
s+=r'\providecommand{\sourcepageanchor}[1]{\phantomsection\label{src:#1}}'+'\n'+r'\begin{document}\setcounter{section}{9}'+'\n'
c=(b/'chapters-tex/10.tex').read_text(encoding='utf-8').split(r'\input')[0]
s+=c+'\n'
for f in sorted((b/'sections-tex').glob('10-*.tex')):s+=r'\input{'+f.relative_to(b).as_posix()+'}\n'
s+=r'\end{document}'
(b/'work/ch10-preview.tex').write_text(s,encoding='utf-8')
(b/'work/ch10-build').mkdir(exist_ok=True)
