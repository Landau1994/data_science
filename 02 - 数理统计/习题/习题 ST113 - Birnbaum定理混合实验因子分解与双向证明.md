---
title: "习题 ST113：Birnbaum定理混合实验因子分解与双向证明"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第6章习题6.33，印刷页247／PDF物理页278"
source_id: "DS011"
source_chapter: 6
source_exercise: "6.33"
source_stars: 0
source_refs: ["DS011 Exercise 6.33，印刷247／PDF物理278", "DS011 定义与条件性原则，印刷238／PDF269", "DS011 Theorem 6.3.6及式(6.3.3)–(6.3.5)，印刷239／PDF270"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST113：Birnbaum定理混合实验因子分解与双向证明

## 题目

### 英文原题

> [!question] 英文原题
> **6.33** Fill in the gaps in the proof of Theorem 6.3.6, Birnbaum's Theorem.
>
> (a) Define $g(t\mid\theta)=g((j,\mathbf x_j)\mid\theta)=f^*((j,\mathbf x_j)\mid\theta)$ and
> $$
> h(j,\mathbf x_j)=\begin{cases}C,&\text{if }(j,\mathbf x_j)=(2,\mathbf x_2^*),\\1,&\text{otherwise}.\end{cases}
> $$
> Show that $T(j,\mathbf x_j)$ is a sufficient statistic in the $E^*$ experiment by verifying that
> $$
> g(T(j,\mathbf x_j)\mid\theta)h(j,\mathbf x_j)
> =g((j,\mathbf x_j)\mid\theta)(1)
> =f^*((j,\mathbf x_j)\mid\theta),
> $$
> for all $(j,\mathbf x_j)$.
>
> (b) As $T$ is sufficient, show that the Formal Sufficiency Principle implies (6.3.4). Also the Conditionality Principle implies (6.3.5), and hence deduce the Formal Likelihood Principle.
>
> (c) To prove the converse, first let one experiment be the $E^*$ experiment and the other $E_j$ and deduce that $\operatorname{Ev}(E^*,(j,\mathbf x_j))=\operatorname{Ev}(E_j,\mathbf x_j)$, the Conditionality Principle. Then, if $T(\mathbf X)$ is sufficient and $T(\mathbf x)=T(\mathbf y)$, show that the likelihoods are proportional and then use the Formal Likelihood Principle to deduce $\operatorname{Ev}(E,\mathbf x)=\operatorname{Ev}(E,\mathbf y)$, the Formal Sufficiency Principle.

### 中文转述

> [!question] 中文转述
> **原题6.33。**
> 补全定理6.3.6（Birnbaum定理）证明中的细节.
>
> (a)  定义$g(t\mid\theta)=g((j,\boldsymbol x_j)\mid\theta)=f^*((j,\boldsymbol x_j)\mid\theta)$及
>
> $$
> h(j,\boldsymbol x_j)=\begin{cases}C,&\text{若 }(j,\boldsymbol x_j)=(2,\boldsymbol x_2^*),\\1,&\text{其他情形}.\end{cases}
> $$
>
> 通过验证对所有$(j,\boldsymbol x_j)$均有下式，说明$T(j,\boldsymbol x_j)$是$E^*$试验中的充分统计量：
>
> $$
> \begin{aligned}
> g(T(j,\boldsymbol x_j)\mid\theta)h(j,\boldsymbol x_j)
> &=g((j,\boldsymbol x_j)\mid\theta)(1)\\
> &=f^*((j,\boldsymbol x_j)\mid\theta).
> \end{aligned}
> $$
>
> (b)  由于$T$充分，说明形式充分性原则蕴含式6.3.4.条件性原则也蕴含式6.3.5，由此推出形式似然原则.
>
> (c)  为证明逆命题，先取一个试验为$E^*$试验，另一个为$E_j$，推出$\operatorname{Ev}(E^*,(j,\boldsymbol x_j))=\operatorname{Ev}(E_j,\boldsymbol x_j)$，即条件性原则.然后，若$T(\boldsymbol X)$充分且$T(\boldsymbol x)=T(\boldsymbol y)$，说明似然成比例，再利用形式似然原则推出$\operatorname{Ev}(E,\boldsymbol x)=\operatorname{Ev}(E,\boldsymbol y)$，即形式充分性原则.

### 题内引用与条件

原书§6.3.2的离散设置：两个实验同参数$\theta$，指定有效点满足$f_2(x_2^*\mid\theta)=C f_1(x_1^*\mid\theta)$，$C>0$不含参数。独立等概率选$J=1,2$，混合密度$f^*(j,x_j\mid\theta)=\tfrac12 f_j(x_j\mid\theta)$。统计量$T$把$(1,x_1^*)$和$(2,x_2^*)$都映到$(1,x_1^*)$，其余点保持原值。

## 提示

> [!hint]- 提示 1
> 先检查混合实验的1/2及比例常数C的方向，再分别处理唯一被合并的特殊点。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> **(a)** 对普通点$z\ne(2,x_2^*)$，有$T(z)=z,h(z)=1$，故$g(T(z))h(z)=f^*(z)$。对特殊点，
> $$
> g(T(2,x_2^*)\mid\theta)h(2,x_2^*)
> =\tfrac12 f_1(x_1^*\mid\theta)C
> =\tfrac12 f_2(x_2^*\mid\theta)=f^*(2,x_2^*\mid\theta).
> $$
> 因此所有点均因子分解，$T$充分。原文中间的$g(z)\cdot1$在特殊点不是“直接把$h$恒置为1”的代入，而是需要先用似然比例关系；用该关系后数值等式确实成立。本解答逐点说明这一点，不将原式直接判为数值错误。
>
> **(b)** $T(1,x_1^*)=T(2,x_2^*)$，形式充分性给出
> $$
> \operatorname{Ev}(E^*,(1,x_1^*))
> =\operatorname{Ev}(E^*,(2,x_2^*)).
> $$
> 条件性分别将两边换成$\operatorname{Ev}(E_1,x_1^*)$与$\operatorname{Ev}(E_2,x_2^*)$，所以成比例似然的两个实验结果证据相同，即形式似然原则。
>
> **(c)** 反向假设形式似然原则。观测$(j,x_j)$的混合实验似然为$\tfrac12 f_j(x_j\mid\theta)$，与单独$E_j$的似然成参数无关比例，故证据相同，得到条件性。
>
> 若$T$对$E$充分，因子分解为$f_\theta(x)=a_\theta(T(x))b(x)$。在有效观测点$T(x)=T(y)$时，
> $$
> f_\theta(x)=\frac{b(x)}{b(y)}f_\theta(y),
> $$
> 比例不含$\theta$（在共同零概率点之外选择适当版本）。形式似然原则遂给$\operatorname{Ev}(E,x)=\operatorname{Ev}(E,y)$，正是形式充分性。至此两个方向均完成。

## 相关概念

- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=278|印刷247／PDF物理278]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 保留原(a)全部连等式；特殊点需用f2=Cf1才能解释中间项，不能把h直接当作恒1。原译稿脚注对这一中间步骤有疑虑，本笔记以逐点计算给出核验边界，不修改原译稿。形式原则按原书离散设置讨论。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
