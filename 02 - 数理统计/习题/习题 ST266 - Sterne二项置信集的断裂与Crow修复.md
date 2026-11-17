---
title: "习题 ST266：Sterne二项置信集的断裂与Crow修复"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第9章习题9.18，印刷页367／PDF物理页398"
source_id: "DS011"
source_chapter: 9
source_exercise: "9.18"
source_stars: 0
source_refs: ["DS011 Exercise 9.18，印刷367／PDF物理398", "DS011 Example 9.2.11及Table 9.2.2，印刷348–349／PDF物理379–380"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST266：Sterne二项置信集的断裂与Crow修复

## 题目

### 英文原题

> [!question] 英文原题
> **9.18** In this exercise we will investigate some more properties of binomial confidence sets and the Sterne (1954) construction in particular. As in Example 9.2.11, we will again consider the binomial(3,$p$) distribution.
> (a) Draw, as a function of $p$, a graph of the four probability functions $P_p(X=x)$, $x=0,\ldots,3$. Identify the maxima of $P_p(X=1)$ and $P_p(X=2)$.
> (b) Show that for small $\varepsilon$, $P_p(X=0)>P_p(X=2)$ for $p=\frac13+\varepsilon$.
> (c) Show that the most probable construction is to blame for the difficulties with the Sterne sets by showing that the following acceptance regions can be inverted to obtain a $1-\alpha=.442$ confidence interval.
>
> | $p$ | Acc. region |
> |---|---|
> | $[.000,.238]$ | $\{0\}$ |
> | $(.238,.305)$ | $\{0,1\}$ |
> | $[.305,.362]$ | $\{1\}$ |
> | $(.362,.634)$ | $\{1,2\}$ |
> | $[.634,.695]$ | $\{2\}$ |
> | $(.695,.762)$ | $\{2,3\}$ |
> | $[.762,1.00]$ | $\{3\}$ |
>
> (This is essentially Crow’s (1956) modification of Sterne’s construction; see Miscellanea 9.5.2.)

### 中文转述

> [!question] 中文转述
> **原题9.18。**
> 本题进一步研究二项置信集的性质，特别是Sterne（1954）的构造. 与例9.2.11一样，仍考虑$\operatorname{binomial}(3,p)$分布.
>
> (a)  画出四个概率函数$P_p(X=x)$，$x=0,\ldots,3$，随$p$变化的图像. 确定$P_p(X=1)$和$P_p(X=2)$的最大值.
>
> (b)  证明对于小的$\varepsilon$，当$p=\frac13+\varepsilon$时有$P_p(X=0)>P_p(X=2)$.
>
> (c)  证明以下接受域可被反演为$1-\alpha=.442$置信区间，从而说明Sterne集合中的困难应归咎于最大概率构造.
>
> | $p$ | 接受域 |
> | --- | --- |
> | $[.000,.238]$ | $\{0\}$ |
> | $(.238,.305)$ | $\{0,1\}$ |
> | $[.305,.362]$ | $\{1\}$ |
> | $(.362,.634)$ | $\{1,2\}$ |
> | $[.634,.695]$ | $\{2\}$ |
> | $(.695,.762)$ | $\{2,3\}$ |
> | $[.762,1.00]$ | $\{3\}$ |
>
> （这实质上是Crow（1956）对Sterne构造的修改，参见节9.5.2.）

## 提示

> [!hint]- 提示
> 先写出四个三次二项概率函数；反演表格时固定观察值$x$，收集所有把它列入接受域的$p$，并逐段核查覆盖概率。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> (a) 四条函数是$(1-p)^3,3p(1-p)^2,3p^2(1-p),p^3$。中间两条分别在$p=1/3,2/3$达到$4/9$。独立计算图：![[附件/习题图/DS011/习题9.18-二项概率曲线.png]]。
> (b) 差为$(1-p)[(1-p)^2-3p^2]=(1-p)(1-2p-2p^2)$，在$0\le p<(\sqrt3-1)/2=0.3660254\ldots$为正，故$0<\varepsilon<(\sqrt3-1)/2-1/3$即满足。按概率排序会在$p\approx.362$后重新选择0，从而使反演的$x=0$集合断裂。
> (c) **原表不能逐字证明精确$.442$覆盖。** 例如$p=.634$只接受2，概率$3(.634)^2(.366)=.441347688<.442$。此外三位小数舍入还造成其他微小下穿。反演原表仍得到四个连通区间$[0,.305)$、$(.238,.634)$、$(.362,.762)$、$(.695,1]$，但其覆盖并非声明值。
> 给出精确修复：令$c=.442$，$u=1-c^{1/3}=.2382588396906727$；令$a<1/3<b$为$3p(1-p)^2=c$的两根，实际$a=.3051818741797506,b=.3623009389479504$。将七段边界改为$u,a,b,1-b,1-a,1-u$，接受集仍依序为$\{0\},\{0,1\},\{1\},\{1,2\},\{2\},\{2,3\},\{3\}$，根处保留足够的集合（可取邻段并集）。单点段概率至少$c$；$\{0,1\}$段概率不小于$P(X=1)$或$P(X=0)$在相应端点的下界；中央$\{1,2\}$概率$3p(1-p)$在$[b,1-b]$超过$c$，其余由对称性。于是每个参数接受概率至少$c$，反演各观测仍为连通区间。修复展示问题来自最高概率排序的跳换，不能以舍入表代替精确保证。

## 相关概念

- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=398|印刷367／PDF物理398]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
