---
title: "习题 ST272：Poisson区间覆盖率的有限指标和与跳跃"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第9章习题9.24，印刷页368／PDF物理页399"
source_id: "DS011"
source_chapter: 9
source_exercise: "9.24"
source_stars: 0
source_refs: ["DS011 Exercise 9.24，印刷368／PDF物理399", "DS011 Example 9.2.15及Figure 9.2.5，印刷351、355／PDF物理382、386"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST272：Poisson区间覆盖率的有限指标和与跳跃

## 题目

### 英文原题

> [!question] 英文原题
> **9.24** For $X\sim\operatorname{Poisson}(\lambda)$, show that the coverage probability of the confidence interval $[L(X),U(X)]$ in Example 9.2.15 is given by
> $$
> P_\lambda(\lambda\in[L(X),U(X)])=\sum_{x=0}^\infty I_{[L(x),U(x)]}(\lambda)\frac{e^{-\lambda}\lambda^x}{x!},
> $$
> and that we can define functions $x_l(\lambda)$ and $x_u(\lambda)$ so that
> $$
> P_\lambda(\lambda\in[L(X),U(X)])=\sum_{x=x_l(\lambda)}^{x_u(\lambda)}\frac{e^{-\lambda}\lambda^x}{x!}.
> $$
> Hence, explain why the graph of the coverage probability of the Poisson intervals given in Figure 9.2.5 has jumps occurring at the endpoints of the different confidence intervals.

### 中文转述

> [!question] 中文转述
> **原题9.24。**
> 对于$X\sim\operatorname{Poisson}(\lambda)$，证明例9.2.15中置信区间$[L(X),U(X)]$的覆盖概率为
>
> $$
> P_\lambda(\lambda\in[L(X),U(X)])=\sum_{x=0}^\infty I_{[L(x),U(x)]}(\lambda)\frac{e^{-\lambda}\lambda^x}{x!},
> $$
>
> 并且可以定义函数$x_l(\lambda),x_u(\lambda)$使
>
> $$
> P_\lambda(\lambda\in[L(X),U(X)])=\sum_{x=x_l(\lambda)}^{x_u(\lambda)}\frac{e^{-\lambda}\lambda^x}{x!}.
> $$
>
> 由此解释为什么9.2.5所给泊松区间的覆盖概率图像，在各个置信区间的端点处发生跳跃.

## 提示

> [!hint]- 提示
> 对每个可能观测$x$写出事件$\lambda\in[L(x),U(x)]$的指示量；当$\lambda$穿过某个区间端点时，求和中会增减哪一项？

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> 对事件按$X=x$分割，全概率公式直接给第一式。例中$L(x)=q_{2x,\alpha/2}/2$（$L(0)=0$）、$U(x)=q_{2(x+1),1-\alpha/2}/2$，二者随$x$严格增加；可由独立正Gamma增量的随机序证明分位数单调。
> 定义$x_l(\lambda)=\min\{x\ge0:U(x)\ge\lambda\}$，$x_u(\lambda)=\max\{x\ge0:L(x)\le\lambda\}$。则$L(x)\le\lambda\le U(x)$当且仅当$x_l\le x\le x_u$；空范围约定概率0，得到第二式。
> 在任何不含端点$L(x),U(x)$的开参数区间，求和指标固定，覆盖率是有限个Poisson概率的解析和。经过$L(x)$时新添$x$项，经过$U(x)$时失去$x$项，产生以对应质量为大小的跳跃；若多个端点重合则合并增减，不能保证每个重合点净跳跃非零。闭端点的覆盖值包含该端点对应项，所以需分清左右极限。

## 相关概念

- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=399|印刷368／PDF物理399]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
