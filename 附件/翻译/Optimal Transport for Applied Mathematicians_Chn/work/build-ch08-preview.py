"""构建第8章在写部分的排版预览，不覆盖正式阶段PDF。"""
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parent.parent
work = root / 'work'
main = root / 'Optimal Transport for Applied Mathematicians_Chn.tex'
preamble = main.read_text(encoding='utf-8').split(r'\begin{document}')[0]
inputs = ''.join('\\input{sections-tex/' + path.name + '}\n' for path in sorted((root / 'sections-tex').glob('08-*.tex')) if path.name.count('-') == 1)
body = (r'\begin{document}\setcounter{section}{7}\setcounter{footnote}{0}'
        '\n' + r'\section{梯度流}\label{sec:8}' + '\n' + inputs + '\n'
        + r'\clearpage\bibliographystyle{plain}\bibliography{bib/references}\end{document}')
(work / 'ch08-preview.tex').write_text(preamble + body, encoding='utf-8')
command = ['xelatex', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', '-output-directory=work', 'work/ch08-preview.tex']
for index, args in enumerate([command, ['bibtex', 'work/ch08-preview'], command, command], 1):
    result = subprocess.run(args, cwd=root, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (work / f'ch08-preview-build-{index}.log').write_bytes(result.stdout)
    if result.returncode:
        print(result.stdout.decode('utf-8', errors='replace')[-2500:])
        raise SystemExit(result.returncode)
print('第8章预览已构建；章外引用暂未集成，不作完整引用核验。')
