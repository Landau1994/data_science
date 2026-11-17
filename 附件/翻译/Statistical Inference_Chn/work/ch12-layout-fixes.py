import pathlib
b=pathlib.Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn')
spec={
'12-02.tex': [('原式第二行分母', '定义$r_\\lambda(\\beta)$为$\\beta\\lambda Y_i+X_i$与$Y_i-\\beta X_i$的样本相关系数，即')],
'12-03.tex': [('原式第一项使用', '\\operatorname{binomial}(n_j,\\pi(x_j))$. 似然为'),('括号中第二项', '也可用对数似然比检验统计量检验$H_0$：')],
'12-04.tex': [('原文$\\psi=\\rho', '其中\n$$\\psi(y_i-\\beta x_i)'),('按上文$\\psi$', '在$\\beta_0=\\beta$处计算导数，得')],
'12-05.tex': [('后一等式比较', '即验证'),('本题重复', '并结合\\hyperref[item:12.27.a]{(a)}得出$\\sqrt n(\\hat\\beta_L-\\beta)\\to\\mathrm n\\bigl(0,1/(4f(0)^2\\sigma_x^2)\\bigr)$.')],
'12-06.tex': [('原图将含随机', '对函数模型的参数赋予分布，就得到结构关系模型：')]
}
for name,changes in spec.items():
 p=b/'sections-tex'/name;s=p.read_text(encoding='utf-8')
 for start,needle in changes:
  lines=s.splitlines();notes=[line for line in lines if line.startswith('\\footnote{译注：'+start)]
  if not notes:continue
  assert len(notes)==1,(name,start)
  note=notes[0];s=s.replace(note+'\n','',1)
  if '\n$$' in needle:
   first,tail=needle.split('\n',1);s=s.replace(needle,first+note+'\n'+tail,1)
  else:
   assert s.count(needle)==1,(name,needle,s.count(needle));s=s.replace(needle,needle+note,1)
 if name=='12-05.tex':s=s.replace('{(1+\\lambda\\beta^2)^2(S_{xx}S_{yy}-S_{xy}^2)}.$$）','{(1+\\lambda\\beta^2)^2(S_{xx}S_{yy}-S_{xy}^2)}.\\quad\\text{）}$$')
 if name=='12-03.tex':s=s.replace('原文引用式12.3.6和12.3.7，但求解两参数的似然方程应为\\eqref{eq:12.3.7}和\\eqref{eq:12.3.8}. 原引用保留.','这里实际应解\\eqref{eq:12.3.7}、\\eqref{eq:12.3.8}；原引用照录.')
 p.write_text(s,encoding='utf-8')
