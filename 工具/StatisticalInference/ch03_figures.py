"""按习题3.33–3.36的参数方程生成独立PGFPlots图；无随机。"""
from pathlib import Path
import subprocess,shutil,json,hashlib,re
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'附件/习题图/DS011';OUT.mkdir(exist_ok=True)
TEXDIR=Path(__file__).with_name('ch03-figures');TEXDIR.mkdir(exist_ok=True)
BUILD=ROOT/'tmp/pdfs/DS011-rest/ch03-build';BUILD.mkdir(parents=True,exist_ok=True)
PRE=r'''\documentclass[border=8pt]{standalone}
\usepackage[UTF8,fontset=fandol]{ctex}
\usepackage{pgfplots}
\usepgfplotslibrary{groupplots}
\pgfplotsset{compat=1.18,every axis/.append style={axis lines=left,tick label style={font=\small},label style={font=\small},title style={font=\small},samples=151}}
\begin{document}
\begin{tikzpicture}
'''
POST='\n\\end{tikzpicture}\n\\end{document}\n'
plots={
'3.33':('参数轨迹',r'''\begin{groupplot}[group style={group size=2 by 3,horizontal sep=2.2cm,vertical sep=1.7cm},width=7.4cm,height=5.4cm]
\nextgroupplot[title={(a) 正态：$v=\mu$},xlabel={$\mu$},ylabel={$v$},xmin=0,xmax=4.2,ymin=0,ymax=4.2]
\addplot[black,thick,domain=0:4]{x};\addplot[only marks,mark=o,mark options={fill=white},mark size=2pt] coordinates {(0,0)};
\nextgroupplot[title={(b) 正态：$v=a\mu^2$，图取$a=1$},xlabel={$\mu$},ylabel={$v$},xmin=-2.2,xmax=2.2,ymin=0,ymax=4.5]
\addplot[black,thick,domain=-2:2]{x^2};\addplot[only marks,mark=o,mark options={fill=white},mark size=2pt] coordinates {(0,0)};
\nextgroupplot[title={(c) Gamma：$\alpha\beta=1$},xlabel={$\alpha$},ylabel={$\beta$},xmin=0,xmax=4.2,ymin=0,ymax=4.5]
\addplot[black,thick,domain=.23:4]{1/x};
\nextgroupplot[title={(d) 第一投影：$v=-3u^2/8$},xlabel={$u=4\theta$},ylabel={$v=-6\theta^2$},xmin=-4.2,xmax=4.2,ymin=-6.5,ymax=.2]
\addplot[black,thick,domain=-4:4]{-3*x^2/8};
\nextgroupplot[title={(d) 第二投影：$w=u^3/16$},xlabel={$u=4\theta$},ylabel={$w=4\theta^3$},xmin=-4.2,xmax=4.2,ymin=-4.5,ymax=4.5]
\addplot[black,thick,domain=-4:4]{x^3/16};
\end{groupplot}'''),
'3.34':('近似族曲线',r'''\begin{groupplot}[group style={group size=3 by 1,horizontal sep=1.5cm},width=6.5cm,height=6.1cm]
\nextgroupplot[title={(a) Poisson，$n=5$},xlabel={$\mu$},ylabel={$v$},xmin=0,xmax=5.2,ymin=0,ymax=1.1]
\addplot[black,thick,domain=0:5]{x/5};\addplot[only marks,mark=o,mark options={fill=white}] coordinates {(0,0)};
\nextgroupplot[title={(b) 二项，$n=5$},xlabel={$\mu=p$},ylabel={$v$},xmin=0,xmax=1.05,ymin=0,ymax=.055,scaled y ticks=false]
\addplot[black,thick,domain=0:1]{x*(1-x)/5};\addplot[only marks,mark=o,mark options={fill=white}] coordinates {(0,0)(1,0)};
\nextgroupplot[title={(c) 负二项，$n=5,r=2$},xlabel={$\mu$},ylabel={$v$},xmin=0,xmax=5.2,ymin=0,ymax=3.7]
\addplot[black,thick,domain=0:5]{x*(x+2)/10};\addplot[only marks,mark=o,mark options={fill=white}] coordinates {(0,0)};
\end{groupplot}'''),
'3.35':('重参数化与均值约束',r'''\begin{groupplot}[group style={group size=2 by 1,horizontal sep=2.2cm},width=8cm,height=6.2cm]
\nextgroupplot[title={(a) 正态的方差缩放比较},xlabel={$\mu$},ylabel={$v$},xmin=0,xmax=4.2,ymin=0,ymax=4.3,legend style={font=\small,at={(.02,.98)},anchor=north west}]
\addplot[black,thick,domain=0:4]{x};\addlegendentry{原式：$v=\mu=e^\theta$}
\addplot[black,dashed,thick,domain=0:4]{x/5};\addlegendentry{3.34(a)：$v=\mu/5$}
\addplot[only marks,mark=o,mark options={fill=white},forget plot] coordinates {(0,0)};
\nextgroupplot[title={(b) Gamma：$\alpha\beta=\mu$，图取$\mu=1$},xlabel={$\alpha$},ylabel={$\beta$},xmin=0,xmax=4.2,ymin=0,ymax=4.5]
\addplot[black,thick,domain=.23:4]{1/x};
\end{groupplot}'''),
'3.36':('位置尺度密度',r'''\begin{axis}[width=15.8cm,height=7.8cm,xmin=-1.5,xmax=5.5,ymin=0,ymax=1.85,xlabel={$x$},ylabel={密度},title={习题3.36：三个位置—尺度密度同轴比较},legend style={font=\small,at={(.5,-.18)},anchor=north,legend columns=3}]
\addplot[black,thick,domain=-1:1]{63/4*(x^6-x^8)};\addlegendentry{$\mu=0,\sigma=1$}
\addplot[black,dashed,thick,domain=2:4]{63/4*((x-3)^6-(x-3)^8)};\addlegendentry{$\mu=3,\sigma=1$}
\addplot[black,densely dotted,very thick,domain=1:5]{63/8*(((x-3)/2)^6-((x-3)/2)^8)};\addlegendentry{$\mu=3,\sigma=2$}
\end{axis}''')}
report={}
for ex,(label,plot) in plots.items():
    def open_points(match):
        return ''.join(r'\draw[black,fill=white] (axis cs:'+coord+r') circle[radius=1.7pt];' for coord in re.findall(r'\(([^)]+)\)',match[1]))
    plot=re.sub(r'\\addplot\[only marks[^\n]*?\] coordinates \{([^}]+)\};',open_points,plot)
    name='exercise-'+ex.replace('.','-');tex=TEXDIR/(name+'.tex');tex.write_text(PRE+plot+POST,encoding='utf-8')
    run=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error',f'-output-directory={BUILD}',f'-jobname={name}',tex.name],cwd=TEXDIR,capture_output=True)
    if run.returncode:raise RuntimeError(run.stdout.decode('utf-8',errors='replace')[-2500:])
    log=(BUILD/(name+'.log')).read_text(encoding='utf-8',errors='replace')
    assert not any(x in log for x in ['Overfull','Missing character','! LaTeX Error']),name
    pdf=OUT/f'习题{ex}-{label}.pdf';shutil.copy2(BUILD/(name+'.pdf'),pdf)
    subprocess.run(['pdftoppm','-singlefile','-scale-to','2200','-png',str(pdf),str(pdf.with_suffix(''))],check=True,capture_output=True)
    report[ex]={'tex':tex.relative_to(ROOT).as_posix(),'pdf':pdf.relative_to(ROOT).as_posix(),'png':pdf.with_suffix('.png').relative_to(ROOT).as_posix(),'parameters':{'a':1} if ex=='3.33' else {'n':5,'r':2} if ex=='3.34' else {'n_comparison':5,'gamma_mean':1} if ex=='3.35' else {'cases':[[0,1],[3,1],[3,2]]},'construction':'independent-PGFPlots','sha256_png':hashlib.sha256(pdf.with_suffix('.png').read_bytes()).hexdigest()}
(TEXDIR/'figure-manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
