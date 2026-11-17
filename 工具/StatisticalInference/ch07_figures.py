"""第7章7.63风险曲线与7.65 LINEX损失，独立公式构造，保留TeX。"""
from pathlib import Path
import subprocess,shutil,json,hashlib,math
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'附件/习题图/DS011';OUT.mkdir(exist_ok=True)
TEXDIR=Path(__file__).with_name('ch07-figures');TEXDIR.mkdir(exist_ok=True)
BUILD=ROOT/'tmp/pdfs/DS011-rest/ch07-build';BUILD.mkdir(parents=True,exist_ok=True)
PRE=r'''\documentclass[border=8pt]{standalone}
\usepackage[UTF8,fontset=fandol]{ctex}
\usepackage{pgfplots}
\usepgfplotslibrary{groupplots}
\pgfplotsset{compat=1.18,every axis/.append style={axis lines=left,tick label style={font=\small},label style={font=\small},title style={font=\small},samples=201}}
\begin{document}\begin{tikzpicture}
'''
POST='\n\\end{tikzpicture}\\end{document}\n'
plots={'7.63':('正态先验风险比较',r'''\begin{axis}[width=13cm,height=8cm,xmin=-4,xmax=4,ymin=0,ymax=4.5,xlabel={$\mu$},ylabel={平方误差风险},title={习题7.63：先验方差与频率风险},legend style={font=\small,at={(.5,-.17)},anchor=north,legend columns=1}]
\addplot[black,thick,domain=-4:4]{(1+x^2)/4};\addlegendentry{$\pi_1=n(0,1)$：$R=(1+\mu^2)/4$}
\addplot[black,dashed,thick,domain=-4:4]{(100+x^2)/121};\addlegendentry{$\pi_{10}=n(0,10)$：$R=(100+\mu^2)/121$}
\addplot[black,densely dotted,domain=-4:4]{1};\addlegendentry{参考：$\delta(X)=X$，风险为1}
\end{axis}'''),
'7.65':('LINEX损失曲线',r'''\begin{groupplot}[group style={group size=2 by 1,horizontal sep=1.8cm},width=8cm,height=6.6cm,xlabel={$d=a-\theta$},ylabel={$e^{cd}-cd-1$},legend style={font=\small,at={(.02,.98)},anchor=north west}]
\nextgroupplot[xmin=-3,xmax=3,ymin=0,ymax=17,title={完整比较区间}]
\addplot[black,densely dotted,very thick,domain=-3:3]{exp(.2*x)-.2*x-1};\addlegendentry{$c=0.2$}
\addplot[black,dashed,thick,domain=-3:3]{exp(.5*x)-.5*x-1};\addlegendentry{$c=0.5$}
\addplot[black,thick,domain=-3:3]{exp(x)-x-1};\addlegendentry{$c=1$}
\nextgroupplot[xmin=-1,xmax=1,ymin=0,ymax=.75,title={最小点附近放大}]
\addplot[black,densely dotted,very thick,domain=-1:1]{exp(.2*x)-.2*x-1};
\addplot[black,dashed,thick,domain=-1:1]{exp(.5*x)-.5*x-1};
\addplot[black,thick,domain=-1:1]{exp(x)-x-1};
\end{groupplot}''')}
report={}
for ex,(label,plot) in plots.items():
    name='exercise-'+ex.replace('.','-');tex=TEXDIR/(name+'.tex');tex.write_text(PRE+plot+POST,encoding='utf-8')
    p=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error',f'-output-directory={BUILD}',f'-jobname={name}',tex.name],cwd=TEXDIR,capture_output=True)
    if p.returncode:raise RuntimeError(p.stdout.decode('utf-8',errors='replace')[-2000:])
    log=(BUILD/(name+'.log')).read_text(encoding='utf-8',errors='replace')
    assert not any(x in log for x in ['Overfull','Missing character','! LaTeX Error']),ex
    pdf=OUT/f'习题{ex}-{label}.pdf';shutil.copy2(BUILD/(name+'.pdf'),pdf)
    subprocess.run(['pdftoppm','-singlefile','-scale-to','2200','-png',str(pdf),str(pdf.with_suffix(''))],check=True,capture_output=True)
    report[ex]={'tex':tex.relative_to(ROOT).as_posix(),'pdf':pdf.relative_to(ROOT).as_posix(),'png':pdf.with_suffix('.png').relative_to(ROOT).as_posix(),'construction':'independent-PGFPlots','sha256_png':hashlib.sha256(pdf.with_suffix('.png').read_bytes()).hexdigest()}
report['analytic_checks']={'7.63_intersections':[-math.sqrt(31/13),math.sqrt(31/13)],'7.63_at_zero':[.25,100/121],'7.65_unique_minimum':0,'7.65_parameters':[.2,.5,1],'scope':'公式与实际渲染核对；不以绘图区间外推替代解析推导。'}
(TEXDIR/'figure-manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('created TeX/PDF/PNG for7.63 and7.65')
