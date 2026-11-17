---
title: "习题 ST290：Gamma尺度枢轴区间的加权等高端点"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第9章习题9.42，印刷页371／PDF物理页402"
source_id: "DS011"
source_chapter: 9
source_exercise: "9.42"
source_stars: 0
source_refs: ["DS011 Exercise 9.42，印刷371／PDF物理402", "DS011 Example 9.3.4，印刷359／PDF物理390"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST290：Gamma尺度枢轴区间的加权等高端点

## 题目

### 英文原题

> [!question] 英文原题
> **9.42** Referring to Example 9.3.4, to find the shortest pivotal interval for a gamma scale parameter, we had to solve a constrained minimization problem.
> (a) Show that the solution is given by the $a$ and $b$ that satisfy $\int_a^bf_Y(y)\,dy=1-\alpha$ and $f(b)b^2=f(a)a^2$.
> (b) With one observation from a gamma($k,\beta$) pdf with known shape parameter $k$, find the shortest $1-\alpha$ (pivotal) confidence interval of the form $\{\beta:x/b\le\beta\le x/a\}$.

### 中文转述

> [!question] 中文转述
> **原题9.42。**
> 回顾例9.3.4，为寻找伽马尺度参数的最短枢轴区间，我们必须解一个约束极小化问题.
>
> (a)  证明解由满足$\int_a^b f_Y(y)\,dy=1-\alpha$以及$f(b)b^2=f(a)a^2$的$a,b$给出.
>
> (b)  对来自$\operatorname{gamma}(k,\beta)$密度的一个观测，已知形状参数$k$，求形式为$\{\beta:x/b\le\beta\le x/a\}$的最短$1-\alpha$（枢轴）置信区间.

## 提示

> [!hint]- 提示
> 由覆盖约束求$b'(a)=f(a)/f(b)$，再对$1/a-1/b$求导；全局最短性可改在倒数枢轴的密度上检查。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> (a) $Y=X/\beta\sim\mathrm{Gamma}(k,1)$，区间长度$x(1/a-1/b)$。固定质量时$f(b)b'(a)=f(a)$；对长度求导得$-1/a^2+b'(a)/b^2=0$，故$f(a)a^2=f(b)b^2$。
> (b) 密度$f(y)=y^{k-1}e^{-y}/\Gamma(k)$，需解
> $$
> F_k(b)-F_k(a)=1-\alpha,\qquad a^{k+1}e^{-a}=b^{k+1}e^{-b},\quad0<a<k+1<b.
> $$
> 方程唯一确定有限正端点，所求区间$[x/b,x/a]$。可对$a\in(0,F_k^{-1}(\alpha))$求根，令$b=F_k^{-1}(F_k(a)+1-\alpha)$。全局最优不只依赖驻点：长度系数$\int_a^by^{-2}dy$，每单位概率的代价$g/f=y^{-2}/f(y)$，选择其最低值区域等价于选择$y^2f(y)$的高水平集。该函数严格单峰于$k+1$，故最佳区域正是以上两端等高区间；阈值随质量严格变化，给唯一解。

## 相关概念

- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=402|印刷371／PDF物理402]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
