---
title: "习题 ST291：加权最短枢轴区域的Neyman和Pearson型证明"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第9章习题9.43，印刷页371／PDF物理页402"
source_id: "DS011"
source_chapter: 9
source_exercise: "9.43"
source_stars: 0
source_refs: ["DS011 Exercise 9.43，印刷371／PDF物理402"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST291：加权最短枢轴区域的Neyman和Pearson型证明

## 题目

### 英文原题

> [!question] 英文原题
> **9.43** Juola (1993) makes the following observation. If we have a pivot $Q(X,\theta)$, a $1-\alpha$ confidence interval involves finding $a$ and $b$ so that $P(a<Q<b)=1-\alpha$. Typically the length of the interval will be some function of $a$ and $b$ like $b-a$ or $1/b^2-1/a^2$. If $Q$ has density $f$ and the length can be expressed as $\int_a^bg(t)\,dt$, the shortest pivotal interval is the solution to
> $$
> \min_{\{a,b\}}\int_a^bg(t)\,dt\quad\text{subject to}\quad\int_a^bf(t)\,dt=1-\alpha
> $$
> or, more generally,
> $$
> \min_C\int_Cg(t)\,dt\quad\text{subject to}\quad\int_Cf(t)\,dt\ge1-\alpha.
> $$
> (a) Prove that the solution is $C=\{t:g(t)<\lambda f(t)\}$, where $\lambda$ is chosen so that $\int_Cf(t)\,dt=1-\alpha$. (Hint: You can adapt the proof of Theorem 8.3.12, the Neyman-Pearson Lemma.)
> (b) Apply the result in part (a) to get the shortest intervals in Exercises 9.37 and 9.42.

### 中文转述

> [!question] 中文转述
> **原题9.43。**
> Juola（1993）作了如下观察. 若有枢轴量$Q(\boldsymbol X,\theta)$，构造$1-\alpha$置信区间涉及寻找$a,b$使$P(a<Q<b)=1-\alpha$. 通常区间长度是$a,b$的某个函数，例如$b-a$或$1/b^2-1/a^2$. 若$Q$的密度为$f$，且长度可表示为$\int_a^b g(t)\,dt$，则最短枢轴区间是下述问题的解：
>
> $$
> \min_{\{a,b\}}\int_a^b g(t)\,dt\qquad\text{满足}\quad\int_a^b f(t)\,dt=1-\alpha,
> $$
>
> 或更一般地，
>
> $$
> \min_C\int_C g(t)\,dt\qquad\text{满足}\quad\int_C f(t)\,dt\ge1-\alpha.
> $$
>
> (a) 证明解为$C=\{t:g(t)<\lambda f(t)\}$，其中$\lambda$选为使$\int_C f(t)\,dt=1-\alpha$.（提示：可以改编Neyman--Pearson引理定理8.3.12的证明.）
>
> (b)  应用(a)的结果，得到习题9.37和习题9.42中的最短区间.

## 提示

> [!hint]- 提示
> 比较候选集合与阈值集合的指示量，乘以$g-\lambda f$后逐点确定符号；按Neyman–Pearson证明处理覆盖约束与长度差。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> (a) 取非负可积代价$g$，$\lambda\ge0$，令$C_*$包含$g<\lambda f$且在$g=\lambda f$处酌情选子集，使$\int_{C_*}f=1-\alpha$。对任何可行$C$，逐点$(I_C-I_{C_*})(g-\lambda f)\ge0$，积分得
> $$
> \int_Cg-\int_{C_*}g\ge\lambda\left(\int_Cf-\int_{C_*}f\right)\ge0.
> $$
> 所以$C_*$全局最优。严格水平集能达到指定质量时即题中公式；若平局具有正$f$质量需补选边界或随机化。例如$f=g=1$于$(0,1)$，严格水平集只可能空或全区间，无法直接达到中间质量，不能遗漏该边界条件。允许$g<0$时所有负代价区域应先加入，原证明的$\lambda\ge0$与单纯长度解释也须相应修改。
> (b) 9.37中$Q=Y/\theta$，$f(q)=nq^{n-1}$于$(0,1)$，代价$g=q^{-2}$。$g/f=1/(nq^{n+1})$严格下降，选$[a,1]$，$a^n=\alpha$，给$[Y,Y/\alpha^{1/n}]$。9.42中$f(q)=q^{k-1}e^{-q}/\Gamma(k)$、$g=q^{-2}$，低比值集就是$q^{k+1}e^{-q}$高水平区间，两端满足$a^{k+1}e^{-a}=b^{k+1}e^{-b}$且Gamma质量$1-\alpha$，给$[X/b,X/a]$。

## 相关概念

- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=402|印刷371／PDF物理402]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
