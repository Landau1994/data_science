from pathlib import Path
import csv,json,math
import numpy as np
from scipy import stats
ROOT=Path.cwd();HERE=Path(__file__).parent;FIG=ROOT/'附件/习题图/DS011';R=json.loads((HERE/'results.json').read_text())
def read(name):return np.genfromtxt(HERE/name,delimiter=',',names=True)
def dat(name,head,rows):
 with (FIG/name).open('w',encoding='ascii',newline='') as f:
  w=csv.writer(f,delimiter=' ');w.writerow(head);w.writerows(rows)
def tex(name,body):
 s=r'''\documentclass[tikz,border=6pt]{standalone}
\usepackage{fontspec,xeCJK,amsmath,pgfplots}
\setCJKmainfont{SimSun}
\pgfplotsset{compat=1.18}
\usepgfplotslibrary{groupplots}
\begin{document}\begin{tikzpicture}
'''+body+r'\end{tikzpicture}\end{document}'
 (FIG/(name+'.tex')).write_text(s,encoding='utf-8')
def hist(name,x,edges,extra=None):
 counts,_=np.histogram(x,edges);y=counts/(len(x)*np.diff(edges));rows=[[v,d] for v,d in zip(edges,np.r_[y,0])];dat(name,['x','density'],rows)
z=read('10.11-mean-ARE.csv');dat('10.11-mean.dat',['mu','b1','b3','b5','b10','inv1','inv3','inv5','inv10'],zip(z['mu'],*[z[f'beta{i}'] for i in [1,3,5,10]],*[1/z[f'beta{i}'] for i in [1,3,5,10]]))
z=read('10.11-scale-ARE.csv');dat('10.11-scale.dat',['beta','m1','m3','m5','m10'],zip(z['beta'],*[z[f'mu{i}'] for i in [1,3,5,10]]))
styles=['solid','densely dotted','dashdotted','dashed']
body=r'''\begin{groupplot}[group style={group size=3 by 1,horizontal sep=1.4cm},width=6.5cm,height=6cm,xmin=1,xmax=10,tick label style={font=\small},legend style={font=\scriptsize,at={(.5,-.25)},anchor=north},title style={font=\small}]
\nextgroupplot[title={定义10.1.16的正确方向},xlabel={均值 $\mu$},ylabel={$\mathrm{ARE}(\bar X,\hat\mu)$},ymin=0,ymax=1.05]
'''
for v,style in zip([1,3,5,10],styles):body+=r'\addplot[black,'+style+r'] table[x=mu,y=b'+str(v)+r'] {10.11-mean.dat};\addlegendentry{$\beta='+str(v)+r'$}'+'\n'
body+=r'\nextgroupplot[title={原图方向：上述ARE的倒数},xlabel={均值 $\mu$},ylabel={$v_{MOM}/v_{ML}$},ymin=1,ymax=8]'+'\n'
for v,style in zip([1,3,5,10],styles):body+=r'\addplot[black,'+style+r'] table[x=mu,y=inv'+str(v)+r'] {10.11-mean.dat};\addlegendentry{$\beta='+str(v)+r'$}'+'\n'
body+=r'\nextgroupplot[title={未知均值时尺度估计的效率},xlabel={尺度 $\beta$},ylabel={$\mathrm{ARE}(\tilde\beta,\hat\beta)$},ymin=0,ymax=1.05]'+'\n'
for v,style in zip([1,3,5,10],styles):body+=r'\addplot[black,'+style+r'] table[x=beta,y=m'+str(v)+r'] {10.11-scale.dat};\addlegendentry{$\mu='+str(v)+r'$}'+'\n'
body+=r'\end{groupplot}';tex('习题10.11-Gamma效率比较',body)
z=read('10.14-fish-variances.csv');edges=np.linspace(0,130,53)
for col in ['nonparametric','parametric']:hist('10.14-'+col+'.dat',z[col],edges)
tex('习题10.14-自助分布比较',r'''\begin{groupplot}[group style={group size=2 by 1,horizontal sep=1.3cm},width=8cm,height=6cm,xlabel={13个计数的无偏样本方差 $S^2$},ylabel={密度},xmin=0,xmax=130,ymin=0,ymax=.06,title style={font=\small}]
\nextgroupplot[title={非参数：20,000次重抽样}]
\addplot[ybar interval,fill=gray!35,draw=black] table[x=x,y=density] {10.14-nonparametric.dat};
\addplot[dashed,domain=0:.06,variable=\y] ({44.8974358974359},\y);
\nextgroupplot[title={参数：拟合泊松，20,000次}]
\addplot[ybar interval,fill=gray!35,draw=black] table[x=x,y=density] {10.14-parametric.dat};
\addplot[dashed,domain=0:.06,variable=\y] ({44.8974358974359},\y);
\node[anchor=north east,font=\small] at (rel axis cs:.98,.96) {虚线：观测 $s^2=44.8974$};
\end{groupplot}''')
body=r'''\begin{groupplot}[group style={group size=2 by 2,horizontal sep=1.5cm,vertical sep=1.8cm},width=8.5cm,height=6cm,xlabel={相关系数 $r$},ylabel={密度},xmin=-1,xmax=1,ymin=0,legend style={font=\scriptsize,at={(.02,.98)},anchor=north west},title style={font=\small}]
'''
for j,kind in [(0,'nonparametric'),(1,'nonparametric'),(0,'parametric'),(1,'parametric')]:
 z=read(f'10.17-{j}-bootstrap.csv');hist(f'10.17-{j}-{kind}.dat',z[kind+'_r'],np.linspace(-1,1,41))
 mean=R['10.17'][j]['r'];sd=R['10.17'][j]['delta_sd'];x=np.linspace(-.9999,.9999,801);normal=stats.norm.pdf(x,loc=mean,scale=sd);fisher=np.sqrt(15)/(1-x*x)*stats.norm.pdf(np.sqrt(15)*(np.arctanh(x)-np.arctanh(mean)))
 dat(f'10.17-{j}-curves.dat',['x','normal','fisher'],zip(x,normal,fisher))
 title=('A：保留5.58' if j==0 else 'B：明确假设558')+('；非参数重抽' if kind=='nonparametric' else '；参数重抽')
 body+=r'\nextgroupplot[title={'+title+r'}]'+'\n'+r'\addplot[ybar interval,fill=gray!30,draw=gray] table[x=x,y=density] {10.17-'+str(j)+'-'+kind+r'.dat};\addlegendentry{实际1,000次}'+'\n'
 body+=r'\addplot[black,thick] table[x=x,y=normal] {10.17-'+str(j)+r'-curves.dat};\addlegendentry{一阶正态近似}'+'\n'
 body+=r'\addplot[black,dashed,thick] table[x=x,y=fisher] {10.17-'+str(j)+r'-curves.dat};\addlegendentry{Fisher z推回密度}'+'\n'
body+=r'\end{groupplot}';tex('习题10.17-相关自助分布',body)
body=r'''\begin{groupplot}[group style={group size=2 by 2,horizontal sep=1.5cm,vertical sep=1.8cm},width=8cm,height=5.7cm,xlabel={$-2\log\lambda$},ylabel={每箱平均密度},xmin=0,xmax=10,ymin=0,title style={font=\small},legend style={font=\scriptsize,at={(.98,.98)},anchor=north east}]
'''
for i,z in enumerate(R['10.34']['models']):
 x=read(f"10.34-n{z['n']}-p{z['p0']}-lrt.csv")['LRT'];edges=np.linspace(0,10,26);hist(f'10.34-hist-{i}.dat',x,edges)
 theory=np.diff(stats.chi2.cdf(edges,1))/np.diff(edges);dat(f'10.34-theory-{i}.dat',['x','density'],zip(edges,np.r_[theory,0]))
 body+=r'\nextgroupplot[title={$n='+str(z['n'])+r',p_0='+str(z['p0'])+r'$；10,000次}]'+'\n'
 body+=r'\addplot[ybar interval,fill=gray!35,draw=gray] table[x=x,y=density] {10.34-hist-'+str(i)+r'.dat};\addlegendentry{实际模拟}'+'\n'
 body+=r'\addplot[black,thick,const plot] table[x=x,y=density] {10.34-theory-'+str(i)+r'.dat};\addlegendentry{$\chi^2_1$每箱平均密度}'+'\n'
body+=r'\end{groupplot}';tex('习题10.34-伯努利LRT分布',body)
# Exact piecewise coverage: split at every endpoint instead of smoothing jumps.
def bounds(n,method):
 z=stats.norm.ppf(.975);p=np.arange(n+1)/n
 def root(q,s):return (2*n*q+z*z+s*z*np.sqrt(z*z+4*n*q*(1-q)))/(2*(n+z*z))
 if method=='Wilson':return root(p,-1),root(p,1)
 if method=='CC':
  lo=root(np.maximum(p-.5/n,0),-1);hi=root(np.minimum(p+.5/n,1),1);lo[0]=0;hi[-1]=1;return lo,hi
 p=(np.arange(n+1)+2)/(n+4);h=z*np.sqrt(p*(1-p)/(n+4));return np.maximum(p-h,0),np.minimum(p+h,1)
for n in [12,100]:
 for method in ['Wilson','CC','AC']:
  lo,hi=bounds(n,method);bp=np.unique(np.r_[0,lo,hi,1]);bp=np.clip(bp,0,1);rows=[]
  for a,b in zip(bp[:-1],bp[1:]):
   if b-a<1e-13:continue
   for p in np.linspace(a+min((b-a)/100,1e-10),b-min((b-a)/100,1e-10),12):
    prob=stats.binom.pmf(np.arange(n+1),n,p);rows.append([p,float(prob@((lo<=p)&(p<=hi))),float(prob@(hi-lo))])
   rows.append(['nan','nan','nan'])
  dat(f'10.44-{n}-{method}.dat',['p','coverage','length'],rows)
body=r'''\begin{groupplot}[group style={group size=2 by 2,horizontal sep=2cm,vertical sep=1.8cm},width=8.5cm,height=6cm,xlabel={$p$},xmin=0,xmax=1,unbounded coords=jump,title style={font=\small},legend style={font=\scriptsize,at={(.5,.02)},anchor=south},scaled y ticks=false,yticklabel style={/pgf/number format/fixed,/pgf/number format/precision=2}]
'''
for n,col,title in [(12,'coverage','覆盖概率'),(12,'length','期望长度'),(100,'coverage','覆盖概率'),(100,'length','期望长度')]:
 body+=r'\nextgroupplot[title={95\%名义；$n='+str(n)+r'$},ylabel={'+title+r'},'+('ymin=.8,ymax=1.005' if col=='coverage' else 'ymin=0')+r']'+'\n'
 for method,style,label in [('Wilson','black,solid','Wilson'),('CC','black,dashed','连续性校正score'),('AC','gray,thick,dotted','加二成功二失败')]:
  body+=r'\addplot['+style+r'] table[x=p,y='+col+r'] {10.44-'+str(n)+'-'+method+r'.dat};\addlegendentry{'+label+r'}'+'\n'
 if col=='coverage':body+=r'\addplot[black,thin,domain=0:1] {.95};'+'\n'
body+=r'\end{groupplot}';tex('习题10.44-二项区间比较',body)
print('Prepared 5 figure sources; coverage curves split at every interval endpoint.')
