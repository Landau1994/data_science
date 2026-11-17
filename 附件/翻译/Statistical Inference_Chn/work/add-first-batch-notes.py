from pathlib import Path
B=Path(__file__).resolve().parents[1]
edits={
'frontmatter/00-publication.tex':[(r'Berger, Roger W.，作者.',r'Berger, Roger W.，作者.\footnote{译注：原编目写Roger W.，本书扉页及版权正文写Roger L.，此处保留原编目姓名.}')],
'frontmatter/00-preface-second.tex':[(r'\sourcepageref{219}{第5.5节}',r'\sourcepageref{219}{第5.5节}\footnote{译注：原文指向第5.5节；本版目录中“随机样本的生成”实际列于第5.6节.原引用保留.}')],
'frontmatter/00-figures.tex':[(r'2.1.2 递增与非递增的累积分布函数}',r'2.1.2 递增与非递增的累积分布函数}\footnote{译注：原图目录写“increasing and nonincreasing cdfs”，这里照译；累积分布函数应为非递减函数.}')],
'frontmatter/00-example-list.tex':[(r'例 2.4.9（习题2.4.7续）',r'例 2.4.9（习题2.4.7续）\footnote{译注：原例目录写“Exercise 2.4.7”，但2.4.7是例的编号，原目录用词保留.}')],
'sections-tex/01-02.tex':[(r'图\ref{fig:1.2.2}是样本平均数概率分布的直方图，反映了对样本所作的多项式计数.',r'图\ref{fig:1.2.2}是样本平均数概率分布的直方图，反映了对样本所作的多项式计数.\footnote{译注：原图注明写总体$\{2,4,4,9\}$，正文及直方图对应的却是$\{2,4,9,12\}$；下方保留原图注.}'),(r'（图注数字按原文保留）',''),(r'$9/128=.07$.',r'$9/128=.07$.\footnote{译注：原文使用等号；精确值为$0.0703125$，$.07$只是近似值.}')],
'sections-tex/01-03.tex':[(r'设$A_1,A_2,\ldots$是样本空间的一个划分，$B$为任意集合.则对每个$i=1,2,\ldots$，',r'设$A_1,A_2,\ldots$是样本空间的一个划分，$B$为任意集合.则对每个$i=1,2,\ldots$，\footnote{译注：按本章的条件概率比值定义，须有$P(B)>0$，且使用$P(B\mid A_j)$的各项须有$P(A_j)>0$；零概率分块应剔除或另约定其贡献为0.原定理没有显写这些条件.}')],
'sections-tex/01-04.tex':[(r'每个样本点对应的$X$值完整列举如下：',r'每个样本点对应的$X$值完整列举如下：\footnote{译注：原表第六、七列重复写成HTH、THH，却令$X=1$；按正面次数，这两列应为THT、TTH.原表保留，下文事件集合使用的是正确的三个单正面结果.}')],
'sections-tex/01-07.tex':[(r'\item[(d)] 利用上一小题的结果，建立恒等式',r'\item[(d)] 利用上一小题的结果，建立恒等式\footnote{译注：以下等式原样保留.若$k_1,\ldots,k_m$遍历非负整数且和为$k$，多项式定理给出左端为$m^k$；右端组合数是这类重数配置的个数，并非多项系数之和.}'),(r'从六个数$\{1,2,7,8,14,20\}$中作有放回抽样，画出所有可能样本均值的分布直方图.',r'从六个数$\{1,2,7,8,14,20\}$中作有放回抽样，画出所有可能样本均值的分布直方图.\footnote{译注：原题未给样本容量，因此不能唯一确定该分布；需要先补充样本容量.}'),(r'其概率为$\dfrac{n!}{n^n}$.',r'其概率为$\dfrac{n!}{n^n}$.\footnote{译注：该值是每个原数恰出现一次的无序样本的概率，不能一般地直接当作样本均值的概率.例如从$\{0,1,2\}$有放回抽取3次，均值1还可由$\{1,1,1\}$产生，概率为$7/27$而非$6/27$.}'),(r'聘用到最优秀候选人的概率是多少？',r'聘用到最优秀候选人的概率是多少？\footnote{译注：规则(ii)只给出了允许聘用的必要条件，未完全规定何时停止及聘用.若需要唯一的条件概率，还须明确决策机制；译文未替原题补写.}'),(r'（见习题\ref{exercise:1.27}.）',r'（见习题\ref{exercise:1.27}.）\footnote{译注：原式在$\binom k3$后排成“$-+\cdots$”，保留该排印；意图应为继续交替加减.}'),(r'从而建立容斥恒等式.',r'从而建立容斥恒等式.\footnote{译注：原题在$P_1-P_2$后写等号；标准容斥和应为$P_1-P_2+P_3-\cdots+(-1)^{n+1}P_n$.}'),(r'并证明杂录\ref{sec:1.8.1}中的界限序列随着项数增加而得到改进.',r'并证明杂录\ref{sec:1.8.1}中的界限序列随着项数增加而得到改进.\footnote{译注：原题的不等号方向与杂录相反，且这些交集概率和一般不具单调性.例如4个事件都等于$A$时，$P_1=4P(A)$、$P_2=6P(A)$；更高阶又会下降.另见杂录处译注.}'),(r'\item[(d)] $1-e^{-x}$，$x\in(0,\infty)$.',r'\item[(d)] $1-e^{-x}$，$x\in(0,\infty)$.\footnote{译注：要作为整个实数轴上的cdf，还须在$x\le0$时取0；原题只写出了正半轴上的形式.}'),(r'\item[(a)] 验证$F_Y(y)$是累积分布函数.',r'\item[(a)] 验证$F_Y(y)$是累积分布函数.\footnote{译注：原题只给$y\ge1$上的表达式；在全实数轴上定义cdf时，需在$y<1$处取0.}')],
'sections-tex/01-08.tex':[(r'并且有下列一系列上界和下界：',r'并且有下列一系列上界和下界：\footnote{译注：这里关于$P_i$单调的断言一般不成立.例如4个相同事件给出$P_1=4P(A)<6P(A)=P_2$（若$P(A)>0$）.以下Bonferroni上下界本身成立，但不同截断阶数的界不必单调变紧.}'),(r'这些界限随项数增加而越来越紧，从而改进了最初的Bonferroni界.',r'这些界限随项数增加而越来越紧，从而改进了最初的Bonferroni界.\footnote{译注：此一般性断言需要附加条件.例如6个事件都等于$A$时，一阶上界是$6P(A)$，三阶上界却是$(6-15+20)P(A)=11P(A)$，反而更松.}')]
}
for name,replacements in edits.items():
    p=B/name;t=p.read_text(encoding='utf-8')
    if '% 用户授权疑误脚注：2026-11-04' in t:continue
    for old,new in replacements:
        assert t.count(old)==1,(name,old,t.count(old))
        t=t.replace(old,new)
    p.write_text(t+'\n% 用户授权疑误脚注：2026-11-04\n',encoding='utf-8')
print('Added source-preserving translator notes to',len(edits),'files.')
