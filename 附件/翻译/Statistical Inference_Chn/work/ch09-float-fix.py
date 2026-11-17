from pathlib import Path
b=Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn')
for p in (b/'sections-tex').glob('09-*.tex'):
 t=p.read_text(encoding='utf-8')
 for e in ['figure','table']:
  t=t.replace('\\begin{'+e+'}', '\\par\n\\begin{'+e+'}').replace('\\end{'+e+'}', '\\end{'+e+'}\n\\par')
 p.write_text(t,encoding='utf-8')
p=b/'sections-tex/09-05.tex';t=p.read_text(encoding='utf-8').replace('$(X_1,Y_1),\\ldots,(X_n,Y_n)$','$(X_1,Y_1),\\allowbreak\\ldots,\\allowbreak(X_n,Y_n)$');p.write_text(t,encoding='utf-8')
p=b/'sections-tex/09-02.tex';t=p.read_text(encoding='utf-8');t=t.replace('只须证明它们的pdf不依赖\n\\sourcepageanchor{377}','只须证明它们的pdf不依赖参数（详见\\autoref{exercise:9.9}）.\n\\sourcepageanchor{377}');t=t.replace('参数（详见\\autoref{exercise:9.9}）. 特别地','特别地');p.write_text(t,encoding='utf-8')
