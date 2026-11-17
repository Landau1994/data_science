"""Prepare transparent PGFPlots sources and data from the saved independent results."""
from pathlib import Path
import csv,json,math
import numpy as np
from scipy import stats
ROOT=Path.cwd();HERE=Path(__file__).parent
FIG=ROOT/'附件/习题图/DS011';FIG.mkdir(parents=True,exist_ok=True)
r=json.loads((HERE/'results.json').read_text())
def save(name,header,rows):
    with (FIG/name).open('w',encoding='ascii',newline='') as f:
        w=csv.writer(f,delimiter=' ');w.writerow(header);w.writerows(rows)
def read(name):return np.genfromtxt(HERE/name,delimiter=',',names=True)
def tex(name,body):
    s=r'''\documentclass[tikz,border=6pt]{standalone}
\usepackage{fontspec,xeCJK,amsmath,pgfplots}
\setCJKmainfont{SimSun}
\pgfplotsset{compat=1.18}
\usepgfplotslibrary{groupplots}
\begin{document}
\begin{tikzpicture}
'''+body+r'''
\end{tikzpicture}
\end{document}
'''
    (FIG/(name+'.tex')).write_text(s,encoding='utf-8')
for label in ['binomial','hypergeometric','negative_binomial']:
    z=read('5.53-'+label+'-frequency.csv');save('5.53-'+label+'.dat',['x','empirical','theoretical'],zip(z['x'],z['empirical'],z['theoretical']))
body=r'''\begin{groupplot}[group style={group size=3 by 1,horizontal sep=1.3cm},width=5.4cm,height=5cm,xlabel={$y$},ylabel={概率／相对频率},ymin=0,legend style={font=\scriptsize,at={(0.5,-0.25)},anchor=north},tick label style={font=\scriptsize},title style={font=\small}]
'''
for label,title in [('binomial',r'二项 $n=8,p=2/3$'),('hypergeometric',r'超几何 $10,8,4$'),('negative_binomial',r'负二项 $r=5,p=1/3$')]:
    body+=r'\nextgroupplot[title={'+title+r'}]'+ '\n'
    body+=r'\addplot[ybar,bar width=3pt,fill=gray!30,draw=gray] table[x=x,y=empirical] {5.53-'+label+r'.dat};'+'\n'
    body+=r'\addplot[black,mark=*,mark size=1pt] table[x=x,y=theoretical] {5.53-'+label+r'.dat};\legend{模拟频率,精确PMF}'+'\n'
body+=r'\end{groupplot}';tex('习题5.53-离散模拟对照',body)
v=read('5.54-poisson-variance.csv')['variance'];edges=np.linspace(0,400,51);count,_=np.histogram(v,edges);centers=(edges[:-1]+edges[1:])/2
save('5.54-poisson.dat',['x','frequency'],zip(edges,np.r_[count/len(v),0]))
rows=[]
for z in r['5.54']['nb_grid']:
    expected=r['5.54']['mean']+r['5.54']['mean']**2/z['r'];lo,hi=z['interval_025_975'];rows.append([z['r'],expected,hi-expected,expected-lo])
save('5.54-nb-intervals.dat',['r','expected','plus','minus'],rows)
tex('习题5.54-方差模拟比较',r'''\begin{groupplot}[group style={group size=2 by 1,horizontal sep=1.8cm},width=8cm,height=6cm,tick label style={font=\small},title style={font=\small}]
\nextgroupplot[title={拟合泊松：50,000次方差},xlabel={$S^2$},ylabel={相对频率},xmin=0,xmax=400,ymin=0]
\addplot[ybar interval,fill=gray!30,draw=black] table[x=x,y=frequency] {5.54-poisson.dat};
\node[align=center,font=\small,anchor=north east] at (rel axis cs:0.98,0.96) {观测 $s^2=6370.60$\\远在右侧图域外};
\nextgroupplot[title={负二项：方差的模拟中央95\%区间},xlabel={$r$（对数刻度）},ylabel={$S^2$（对数刻度）},xmode=log,ymode=log,xmin=.4,xmax=130,ymin=100,ymax=200000,legend style={font=\small,at={(.5,-.25)},anchor=north}]
\addplot[only marks,mark=*,error bars/.cd,y dir=both,y explicit] table[x=r,y=expected,y error plus=plus,y error minus=minus] {5.54-nb-intervals.dat};
\addlegendentry{点：理论均值；线：模拟区间}
\addplot[black,dashed,domain=.4:130] {6370.602564102565};\addlegendentry{观测 $s^2$}
\end{groupplot}''')
z=read('5.66-density.csv');save('5.66-density.dat',['x','empirical','exact','asymptotic'],zip(z['x'],z['empirical_density'],z['exact_density'],z['asymptotic_density']))
save('5.66-histogram.dat',['x','density'],zip(np.r_[z['x']-.02,z['x'][-1]+.02],np.r_[z['empirical_density'],0]))
tex('习题5.66-中位数分布对照',r'''\begin{axis}[width=12cm,height=7cm,xlabel={15个标准正态观测的中位数},ylabel={密度},xmin=-1.4,xmax=1.4,ymin=0,legend style={font=\small,at={(.5,-.2)},anchor=north},title={独立模拟200,000次；精确密度与渐近近似}]
\addplot[ybar interval,fill=gray!25,draw=gray] table[x=x,y=density] {5.66-histogram.dat};\addlegendentry{模拟密度}
\addplot[black,thick] table[x=x,y=exact] {5.66-density.dat};\addlegendentry{精确次序统计量密度}
\addplot[black,dashed,thick] table[x=x,y=asymptotic] {5.66-density.dat};\addlegendentry{渐近 $N(0,\pi/30)$}
\end{axis}''')
body=r'''\begin{groupplot}[group style={group size=3 by 1,horizontal sep=1.2cm},width=5.6cm,height=5.5cm,xlabel={$x$},ylabel={CDF},xmin=-5,xmax=5,ymin=0,ymax=1,tick label style={font=\small},legend style={font=\scriptsize,at={(.5,-.22)},anchor=north}]
'''
for nu in [2,10,25]:
    z=read(f'5.68-nu{nu}-samples.csv');x=np.linspace(-5,5,501)
    save(f'5.68-nu{nu}.dat',['x','target','mh','ar','direct'],zip(x,stats.t.cdf(x,nu),[(z['metropolis']<=v).mean() for v in x],[(z['accept_reject']<=v).mean() for v in x],[(z['direct']<=v).mean() for v in x]))
    body+=r'\nextgroupplot[title={$\nu='+str(nu)+r'$；各100个保留值}]'+'\n'
    for col,sty in [('target','black,thick'),('mh','black,dashed,const plot'),('ar','gray,densely dotted,thick,const plot'),('direct','gray,solid,const plot')]:
        body+=r'\addplot['+sty+r'] table[x=x,y='+col+r'] {5.68-nu'+str(nu)+r'.dat};'+'\n'
    body+=r'\legend{目标CDF,MH,接受拒绝,直接变换}'+'\n'
body+=r'\end{groupplot}';tex('习题5.68-t生成经验分布',body)
print('prepared 4 PGFPlots sources; all plotted values derived from actual saved samples or explicit target formulas')
