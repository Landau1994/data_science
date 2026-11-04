"""构建已完成章节的整合预览，不覆盖正式PDF；未译章节不造占位正文。"""
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parent.parent
work = root / 'work'
main = root / 'Optimal Transport for Applied Mathematicians_Chn.tex'
preamble = main.read_text(encoding='utf-8').split(r'\begin{document}')[0]
chapters = [(1, '原问题与对偶问题'), (2, '一维问题'), (3, r'$L^1$与$L^\infty$理论'),
            (4, '最小流、散度约束与运输密度'), (5, 'Wasserstein距离与Wasserstein空间中的曲线'),
            (6, 'Benamou--Brenier及其他连续数值方法'),
            (7, '概率测度空间上的泛函'), (8, '梯度流')]
body = [r'\begin{document}', r'\tableofcontents']
for number, title in chapters:
    short = 'L1与L∞理论' if number == 3 else title
    body += [rf'\setcounter{{section}}{{{number-1}}}\setcounter{{footnote}}{{0}}',
             rf'\section[{short}]{{{title}}}\label{{sec:{number}}}']
    for path in sorted((root / 'sections-tex').glob(f'{number:02d}-*.tex')):
        if path.name.count('-') == 1:
            body.append(r'\input{sections-tex/' + path.name + '}')
body += [r'\input{backmatter/09-exercises.tex}', r'\input{backmatter/09-hints.tex}',
         r'\clearpage\nocite{*}\bibliographystyle{plain}\bibliography{bib/references}\end{document}']
(work / 'progress-preview.tex').write_text(preamble + '\n'.join(body), encoding='utf-8')
command = ['xelatex', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', '-output-directory=work', 'work/progress-preview.tex']
for index, args in enumerate([command, ['bibtex', 'work/progress-preview'], command, command], 1):
    result = subprocess.run(args, cwd=root, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (work / f'progress-preview-build-{index}.log').write_bytes(result.stdout)
    if result.returncode:
        print(result.stdout.decode('utf-8', errors='replace')[-3000:])
        raise SystemExit(result.returncode)
print('已完成章节整合预览构建完毕，仍需补齐全书与全页审阅。')
