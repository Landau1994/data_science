"""精确计数并生成习题1.30、1.51的PGFPlots源稿；无随机抽样。"""

from collections import Counter
import csv
from fractions import Fraction
from itertools import product
import json
from math import comb
from pathlib import Path
import platform
import shutil
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FIGURES = HERE / "figures"
FIGURES.mkdir(exist_ok=True)

values = (1, 2, 7, 8, 14, 20)
sample_size = 6  # 原题未指定；本库明确选用的示例参数，不冒充原文条件。
counts = Counter(sum(row) for row in product(values, repeat=sample_size))
total = len(values) ** sample_size
assert sum(counts.values()) == total == 46656
assert len(counts) == 85 and counts[52] == max(counts.values()) == 2520
with (FIGURES / "exercise-1.30.csv").open("w", encoding="utf-8", newline="") as stream:
    writer = csv.writer(stream)
    writer.writerow(["sum", "sample_mean_exact", "ordered_count", "probability_exact"])
    writer.writerows((s, str(Fraction(s, sample_size)), counts[s], str(Fraction(counts[s], total))) for s in sorted(counts))

denominator = comb(30, 4)
weights = [comb(5, k) * comb(25, 4 - k) for k in range(5)]
assert sum(weights) == denominator == 27405
pmf = [Fraction(c, denominator) for c in weights]
cdf = [sum(pmf[: k + 1]) for k in range(5)]
assert cdf[-1] == 1
with (FIGURES / "exercise-1.51.csv").open("w", encoding="utf-8", newline="") as stream:
    writer = csv.writer(stream)
    writer.writerow(["defective_count", "sample_count", "probability_exact", "cdf_exact"])
    writer.writerows((k, weights[k], str(pmf[k]), str(cdf[k])) for k in range(5))

preamble = r"""\documentclass[border=8pt]{standalone}
\usepackage[UTF8,fontset=fandol]{ctex}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\begin{document}
"""
coordinates = "\n".join(f"({s/sample_size:.12f},{counts[s]/total:.12f})" for s in sorted(counts))
histogram = preamble + r"""\begin{tikzpicture}
\begin{axis}[width=15cm,height=7.5cm,xmin=0.5,xmax=20.5,ymin=0,ymax=0.06,
  axis lines=left,xtick={1,4,7,10,13,16,20},ytick={0,0.01,0.02,0.03,0.04,0.05,0.06},
  xlabel={样本均值 $\bar X_6$},ylabel={概率},
  title={习题1.30：独立等概率有放回抽取6次的精确分布},
  tick label style={font=\small},label style={font=\small},title style={font=\small}]
\addplot[ybar,bar width=1.15pt,fill=black!55,draw=black!80] coordinates {
""" + coordinates + r"""
};
\end{axis}
\end{tikzpicture}
\end{document}
"""
(FIGURES / "exercise-1.30.tex").write_text(histogram, encoding="utf-8")


def step_commands(zoom=False):
    """逐段作图；右连续函数在左端实心、右端空心，不画伪连续斜线。"""
    commands = []
    segments = [(-0.7, 0, Fraction(0))] + [(k, k + 1, cdf[k]) for k in range(4)] + [(4, 4.7, Fraction(1))]
    for left, right, height in segments:
        if zoom and not 0.9996 <= height <= 1.00004:
            continue
        commands.append(rf"\addplot[black,thick] coordinates {{({left},{float(height):.12f}) ({right},{float(height):.12f})}};")
    for k in range(5):
        below = Fraction(0) if k == 0 else cdf[k - 1]
        if not zoom or 0.9996 <= cdf[k] <= 1.00004:
            commands.append(rf"\addplot[only marks,mark=*,mark size=1.6pt,black] coordinates {{({k},{float(cdf[k]):.12f})}};")
        if not zoom or 0.9996 <= below <= 1.00004:
            commands.append(rf"\addplot[only marks,mark=o,mark size=1.6pt,mark options={{solid,fill=white}},black] coordinates {{({k},{float(below):.12f})}};")
    return "\n".join(commands)


distribution = preamble + r"""\begin{tikzpicture}
\begin{axis}[name=main,width=10cm,height=7cm,xmin=-0.7,xmax=4.7,ymin=-0.04,ymax=1.04,
  axis lines=left,xtick={0,1,2,3,4},ytick={0,0.2,0.4,0.6,0.8,1},
  xlabel={$x$},ylabel={$F_X(x)$},title={习题1.51：超几何分布函数},
  tick label style={font=\small},title style={font=\small}]
""" + step_commands() + r"""
\end{axis}
\begin{axis}[at={(main.east)},anchor=west,xshift=1.5cm,width=6.3cm,height=7cm,
  xmin=2.7,xmax=4.4,ymin=0.9996,ymax=1.00004,axis lines=left,
  xtick={3,4},ytick={0.9996,0.9998,1},scaled y ticks=false,
  yticklabel style={/pgf/number format/fixed,/pgf/number format/precision=4},
  xlabel={$x$},title={上尾局部放大},
  tick label style={font=\small},title style={font=\small}]
""" + step_commands(True) + r"""
\end{axis}
\end{tikzpicture}
\end{document}
"""
(FIGURES / "exercise-1.51.tex").write_text(distribution, encoding="utf-8")

report = {
    "checked": "2026-11-12", "python": platform.python_version(), "randomness": "none",
    "exercise_1.30": {"values": values, "sample_size": sample_size, "assumption": "原题未写样本量；本库明示的独立等概率有放回抽6次示例", "ordered_outcomes": total, "distinct_means": len(counts), "mode_mean": str(Fraction(52, 6)), "mode_probability": str(Fraction(2520, total))},
    "exercise_1.51": {"population": 30, "defectives": 5, "sample_size": 4, "replacement": False, "denominator": denominator, "pmf": list(map(str, pmf)), "cdf": list(map(str, cdf))},
    "boundary": "精确枚举只支持上述有限模型；图中坐标转为小数显示，CSV保留精确分数。编译与视觉检查另行执行。",
}
(FIGURES / "exact-checks.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))

if "--render" in sys.argv:
    build = ROOT / "tmp" / "pdfs" / "DS011-figures"
    build.mkdir(parents=True, exist_ok=True)
    for suffix, label in (("30", "样本均值分布"), ("51", "超几何分布函数")):
        job = f"si-ch1-{suffix}"
        run = subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-halt-on-error", f"-output-directory={build}", f"-jobname={job}", f"exercise-1.{suffix}.tex"],
            cwd=FIGURES, capture_output=True,
        )
        if run.returncode:
            raise RuntimeError(run.stdout.decode("utf-8", errors="replace")[-3000:])
        log = (build / f"{job}.log").read_text(encoding="utf-8", errors="replace")
        if any(warning in log for warning in ("Overfull", "Missing character", "! LaTeX Error")):
            raise RuntimeError(f"请检查编译日志：{build / (job + '.log')}")
        output = ROOT / f"附件/习题图/DS011/习题1.{suffix}-{label}.pdf"
        shutil.copy2(build / f"{job}.pdf", output)
        subprocess.run(["pdftoppm", "-singlefile", "-scale-to", "2000", "-png", str(output), str(output.with_suffix(""))], check=True, capture_output=True)
