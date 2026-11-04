"""只修末轮实际目视和PDF审计已确认的局部排版/锚点，不改数学内容。"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
changes = []


def replace(file, old, new):
    path = root / file
    text = path.read_text(encoding='utf-8')
    assert text.count(old) == 1, (file, old, text.count(old))
    path.write_text(text.replace(old, new, 1), encoding='utf-8')
    changes.append(file)


for file, title in [
    ('frontmatter/00-preface.tex', '前言'),
    ('frontmatter/00-acknowledgments.tex', '致谢'),
    ('frontmatter/00-source-contents.tex', '原书目录（页码沿用原书）'),
    ('frontmatter/00-notation.tex', '记号'),
]:
    replace(file, rf'\section*{{{title}}}\label', rf'\section*{{{title}}}\phantomsection\label')
for title in ['丛书信息', '题名与版权']:
    replace('frontmatter/00-publication.tex', rf'\section*{{{title}}}\addcontentsline',
            rf'\section*{{{title}}}\phantomsection\addcontentsline')
replace('frontmatter/00-publication.tex', r'\url{10.1007/978-3-319-20828-2}',
        r'\href{https://doi.org/10.1007/978-3-319-20828-2}{\nolinkurl{10.1007/978-3-319-20828-2}}')
replace('frontmatter/00-publication.tex', r'\url{www.springer.com}',
        r'\href{https://www.springer.com}{\nolinkurl{www.springer.com}}')
replace('sections-tex/01-03.tex', r'\begin{remark}\label{obj:1.26}',
        r'\begin{remark}\leavevmode\label{obj:1.26}')
replace('sections-tex/04-04-2.tex', r'\begin{proposition}\label{obj:4.41}',
        r'\begin{proposition}\leavevmode\label{obj:4.41}')
for file, title in [
    ('sections-tex/03-02.tex', '知识回顾：密度点'),
    ('sections-tex/03-03.tex', '重要概念：近似梯度'),
    ('sections-tex/04-02.tex', '知识回顾：一元有界变差函数'),
]:
    replace(file, rf'\begin{{sourcebox}}{{{title}}}',
            '\\Needspace{8\\baselineskip}\n' + rf'\begin{{sourcebox}}{{{title}}}')
for file, label, size in [
    ('sections-tex/06-04.tex', 'obj:6.5', 10),
    ('sections-tex/08-03.tex', 'obj:8.9', 12),
]:
    replace(file, rf'\begin{{lemma}}\label{{{label}}}',
            rf'\Needspace{{{size}\baselineskip}}' + '\n' + rf'\begin{{lemma}}\label{{{label}}}')

for file, phrase in [
    ('sections-tex/01-04.tex', '相同结果）.'),
    ('sections-tex/01-05.tex', '（例如小立方体）.'),
    ('sections-tex/01-07.tex', r'（见\cite{b109}）.'),
    ('sections-tex/07-01.tex', r'就有$F(\mu)=+\infty$）.'),
    ('sections-tex/07-04.tex', r'（即$W(z)$随$|z|$递增）.'),
    ('backmatter/09-hints.tex', '用严格凸性证明唯一性）.'),
]:
    replace(file, phrase, phrase[:-1] + r'\nobreak.')

file = 'sections-tex/04-03.tex'
figure = r'''\begin{figure}[htbp]\centering
\includegraphics[width=.95\textwidth]{assets/ch04b-fig4-2.pdf}
\caption{集合$\Omega_i(t)$的不交性.}\label{fig:4.2}
\end{figure}'''
text = (root / file).read_text(encoding='utf-8')
assert text.count(figure) == 1
sentence = '因而，只需假设$|A|<(1-t)^d\\delta(\\varepsilon)$，就得到$\\mu_t(A)<\\varepsilon$. 这确认了$\\mu_t\\ll\\mathscr L^d$，并给出一个可以传递到极限的估计.'
assert text.count(sentence) == 1
text = text.replace(figure + '\n', '', 1)
text = text.replace(sentence, sentence + '\n\n' + figure, 1)
(root / file).write_text(text, encoding='utf-8')
changes.append(file)

style = root / 'work/translated-index.ist'
text = style.read_text(encoding='utf-8')
assert 'delim_0' not in text
text += '\n' + '\n'.join(f'delim_{n} "\\\\nobreak, "' for n in range(3)) + '\n'
style.write_text(text, encoding='utf-8')
print('局部修复完成：', len(changes), '次替换／移动；尚须重编译与变化页实看。')
