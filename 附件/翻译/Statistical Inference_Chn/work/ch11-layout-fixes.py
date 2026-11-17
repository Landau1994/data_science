import pathlib
b=pathlib.Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn')
for p in sorted((b/'sections-tex').glob('11-*.tex')):
 s=p.read_text(encoding='utf-8').replace(r'),\ldots,(',r'),\allowbreak\ldots,\allowbreak(')
 if p.name=='11-02.tex':
  s=s.replace(r'''\left\{\sum_{i=1}^k\left(\frac{b_i}{c_i}\right)(v_i)\left(\frac{c_i}{C}\right)\right\}^2
&=(EBV)^2\\
&=(\operatorname{Cov}(B,V))^2 &&(EB=0)\\
&\le(\operatorname{Var}B)(\operatorname{Var}V)&&\text{（Cauchy--Schwarz不等式）}\\''',r'''&\left\{\sum_{i=1}^k\left(\frac{b_i}{c_i}\right)(v_i)\left(\frac{c_i}{C}\right)\right\}^2\\
&\quad=(EBV)^2\\
&\quad=(\operatorname{Cov}(B,V))^2\qquad(EB=0)\\
&\quad\le(\operatorname{Var}B)(\operatorname{Var}V)\qquad\text{（Cauchy--Schwarz不等式）}\\''')
 p.write_text(s,encoding='utf-8')
