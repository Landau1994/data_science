from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
pairs={
'06-01.tex':[(r'不过引理的某个变体',r'不过\autoref{lem:6.2}的某个变体'),(r'测地凸（\autoref{exer:5.2}）',r'测地凸（\autoref{sec:5}的\autoref{exer:5.2}）')],
'06-02.tex':[(r'该 Markov 链的平稳分布',r'Markov 链\eqref{eq:6.11}的平稳分布')],
'06-03.tex':[(r'为用相互作用粒子系统逼近它',r'为用相互作用粒子系统逼近\eqref{eq:6.17}'),(r'可以证明，它的 Wasserstein 梯度流',r'可以证明，\eqref{eq:6.19}的 Wasserstein 梯度流')],
'06-05.tex':[(r'这一目标的训练动力学',r'目标\eqref{eq:6.25}的训练动力学')],
'06-07.tex':[(r'在这一背景下，\autoref{exer:5.4}',r'在这一背景下，\autoref{sec:5}的\autoref{exer:5.4}')],
'06-08.tex':[(r'解释\autoref{exer:5.4}和',r'解释\autoref{sec:5}的\autoref{exer:5.4}和'),(r'计算该格式的平稳分布',r'计算格式\eqref{eq:6.11}的平稳分布'),(r'证明可以恢复\autoref{exer:5.11}',r'证明可以恢复\autoref{sec:5}的\autoref{exer:5.11}')]
}
for name,changes in pairs.items():
    p=BASE/'sections-tex'/name; t=p.read_text('utf-8')
    for old,new in changes:
        if old in t:
            assert t.count(old)==1,(name,old,t.count(old))
            t=t.replace(old,new)
        else: assert new in t,(name,old)
    p.write_text(t,encoding='utf-8')
print('Restored ten explicit source references in Chapter 6.')
