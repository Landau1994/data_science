import pathlib
b=pathlib.Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn')
s=(b/'Statistical Inference_Chn.tex').read_text(encoding='utf-8').split(r'\begin{document}')[0]
s+=r'\providecommand{\sourcepageanchor}[1]{\phantomsection\label{src:#1}}'+'\n'+r'\begin{document}\setcounter{section}{10}'+'\n'
s+=(b/'chapters-tex/11.tex').read_text(encoding='utf-8').split(r'\input')[0]+'\n'
for f in sorted((b/'sections-tex').glob('11-*.tex')):s+=r'\input{'+f.relative_to(b).as_posix()+'}\n'
s+=r'\end{document}'
(b/'work/ch11-preview.tex').write_text(s,encoding='utf-8');(b/'work/ch11-build').mkdir(exist_ok=True)
