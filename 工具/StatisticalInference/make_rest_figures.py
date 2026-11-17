"""由题设公式生成2.37及4.61的独立图；无随机模拟。"""

import csv
import json
import math
from pathlib import Path
import shutil
import subprocess


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DATA = HERE / "rest-figures"
DATA.mkdir(exist_ok=True)
BUILD = ROOT / "tmp/pdfs/DS011-rest-figures"
BUILD.mkdir(parents=True, exist_ok=True)
amplitude = 0.5 * math.exp(-2 * math.pi**2)
rows = []
for index in range(801):
    x = -4 + index / 100
    density = math.exp(-x*x/2) / math.sqrt(2*math.pi)
    delta = math.log1p(amplitude * math.sin(2*math.pi*x))
    rows.append((x, density, density*(1+0.5*math.sin(2*math.pi*x)), x*x/2, x*x/2+delta, delta*1e9))
with (DATA / "exercise-2.37.csv").open("w", encoding="utf-8", newline="") as stream:
    writer = csv.writer(stream)
    writer.writerow(["x_or_t", "f1", "f2", "K1", "K2", "K_difference_times_1e9"])
    writer.writerows(rows)

header = r"""\documentclass[border=8pt]{standalone}
\usepackage[UTF8,fontset=fandol]{ctex}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\begin{document}
"""


def coordinates(column):
    return "\n".join(f"({row[0]:.10f},{row[column]:.15f})" for row in rows)


comparison = header + r"""\begin{tikzpicture}
\begin{axis}[name=density,width=8cm,height=6cm,xmin=-4,xmax=4,ymin=0,ymax=0.62,
axis lines=left,xlabel={$x$},ylabel={密度},title={习题2.37：不同密度},
legend style={font=\small,at={(0.98,0.98)},anchor=north east},title style={font=\small}]
\addplot[black,thick] coordinates {""" + coordinates(1) + r"""};\addlegendentry{$f_1$}
\addplot[black,dashed,thick] coordinates {""" + coordinates(2) + r"""};\addlegendentry{$f_2$}
\end{axis}
\begin{axis}[name=cumulant,at={(density.east)},anchor=west,xshift=1.4cm,width=8cm,height=6cm,
xmin=-4,xmax=4,ymin=0,ymax=8.4,axis lines=left,xlabel={$t$},ylabel={累积量生成函数},
title={两条曲线在此尺度几乎重合},title style={font=\small},
legend style={font=\small,at={(0.5,0.96)},anchor=north}]
\addplot[black,thick] coordinates {""" + coordinates(3) + r"""};\addlegendentry{$K_1$}
\addplot[black,dashed] coordinates {""" + coordinates(4) + r"""};\addlegendentry{$K_2$}
\end{axis}
\begin{axis}[at={(density.south west)},anchor=north west,yshift=-1.8cm,width=16.5cm,height=5.5cm,
xmin=-4,xmax=4,ymin=-1.5,ymax=1.5,axis lines=left,xlabel={$t$},ylabel={$10^9(K_2-K_1)$},
title={用稳定公式计算的累积量差异放大图},title style={font=\small},scaled y ticks=false]
\addplot[black,thick] coordinates {""" + coordinates(5) + r"""};
\end{axis}
\end{tikzpicture}
\end{document}
"""
(DATA / "exercise-2.37.tex").write_text(comparison, encoding="utf-8")

borel = header + r"""\begin{tikzpicture}
\begin{axis}[name=wedge,width=8.5cm,height=6.5cm,xmin=0,xmax=6.3,ymin=0,ymax=2.35,
axis lines=left,xlabel={$x_1$},ylabel={$x_2$},xtick={0,1,3,5,6},ytick={0,0.8,1,1.2,2},
title={$B_1:\ |x_2-1|<0.2x_1$},title style={font=\small},clip=true]
\addplot[draw=none,fill=black!14] coordinates {(0,1)(6,2.2)(6,0)(5,0)(0,1)}\closedcycle;
\addplot[black,dashed,thick] coordinates {(0,1)(6,2.2)};
\addplot[black,dashed,thick] coordinates {(0,1)(5,0)};
\addplot[black] coordinates {(0,1)(6,1)};
\end{axis}
\begin{axis}[at={(wedge.east)},anchor=west,xshift=1.6cm,width=8.5cm,height=6.5cm,
xmin=0,xmax=6.3,ymin=0,ymax=2.35,axis lines=left,xlabel={$x_1$},ylabel={$x_2$},
xtick={0,1,3,5,6},ytick={0,0.8,1,1.2,2},title={$B_2:\ 0.8<x_2<1.2$},title style={font=\small},clip=true]
\addplot[draw=none,fill=black!14] coordinates {(0,0.8)(6,0.8)(6,1.2)(0,1.2)}\closedcycle;
\addplot[black,dashed,thick] coordinates {(0,0.8)(6,0.8)};
\addplot[black,dashed,thick] coordinates {(0,1.2)(6,1.2)};
\addplot[black] coordinates {(0,1)(6,1)};
\end{axis}
\end{tikzpicture}
\end{document}
"""
(DATA / "exercise-4.61.tex").write_text(borel, encoding="utf-8")

targets = [("2.37", "密度与累积量比较"), ("4.61", "Borel条件邻域")]
for exercise, label in targets:
    job = "exercise-" + exercise.replace(".", "-")
    run = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", f"-output-directory={BUILD}", f"-jobname={job}", f"exercise-{exercise}.tex"], cwd=DATA, capture_output=True)
    if run.returncode:
        raise RuntimeError(run.stdout.decode("utf-8", errors="replace")[-3500:])
    log = (BUILD / f"{job}.log").read_text(encoding="utf-8", errors="replace")
    assert not any(x in log for x in ["Overfull", "Missing character", "! LaTeX Error"])
    output = ROOT / f"附件/习题图/DS011/习题{exercise}-{label}.pdf"
    shutil.copy2(BUILD / f"{job}.pdf", output)
    subprocess.run(["pdftoppm", "-singlefile", "-scale-to", "2100", "-png", str(output), str(output.with_suffix(""))], check=True, capture_output=True)
report = {"date": "2026-11-13", "randomness": "none", "density_coefficient": 0.5, "frequency": "2*pi", "cumulant_amplitude": amplitude, "domain": [-4, 4], "Borel_epsilon": 0.2, "Borel_display_window": {"x1": [0, 6.3], "x2": [0, 2.35]}, "source_pages": {"2.37": 100, "4.61": 197}, "boundary": "独立公式构造；图4.61只显示正象限的有限窗口，阴影表示集合而非概率密度。编译后须另行目视。"}
(DATA / "checks.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
