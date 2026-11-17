---
title: "习题 ST422：LAD渐近正态的得分勘误与凸目标完整证明"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.27，印刷页492／PDF物理页523"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.27"
source_stars: 0
source_refs: ["DS011 Exercise 12.27，印刷页492／PDF物理页523", "DS011 所引正文，印刷485／PDF物理516", "DS011 所引正文，印刷486／PDF物理517"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST422：LAD渐近正态的得分勘误与凸目标完整证明

## 题目

### 英文原题

> [!question] 英文原题
> **12.27** (a) Verify that $-n^{-1/2}\sum_{i=1}^n\psi(Y_i-\hat\beta x_i)\to\mathrm n(0,\sigma_x^2)$.
> (b) Verify that
> $$\left.\frac1n\sum_{i=1}^n\frac d{d\beta_0}E_\beta[\psi(Y_i-\beta_0x_i)]\right|_{\beta_0=\beta}=2f(0)\frac1n\sum_{i=1}^nx_i^2,$$
> and, with part (a), that $\sqrt n(\hat\beta_L-\beta)\to\mathrm n(0,1/[4f(0)^2\sigma_x^2])$.

### 中文转述

> [!question] 中文转述
> **原题12.27。**
> (a)  验证$-\frac1{\sqrt n}\sum_{i=1}^n\psi(Y_i-\hat\beta x_i)\to\mathrm n(0,\sigma_x^2)$.
>
> (b)  验证
>
> $$
> \left.\frac1n\sum_{i=1}^n\frac d{d\beta_0}E_\beta[\psi(Y_i-\beta_0x_i)]\right|_{\beta_0=\beta}
> =2f(0)\frac1n\sum_{i=1}^nx_i^2,
> $$
>
> 并结合(a)得出$\sqrt n(\hat\beta_L-\beta)\to\mathrm n\bigl(0,1/(4f(0)^2\sigma_x^2)\bigr)$.

## 提示

> [!hint]- 提示
> 在真参数处用CLT，在估计值处用次梯度；不可把不可微样本得分直接作普通Taylor级数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 重述足够条件：$Y_i=\beta x_i+\varepsilon_i$，误差iid，$P(\varepsilon_i\le0)=1/2$，分布在0附近可微、密度$f$连续且$f(0)>0$；固定设计$q_n=n^{-1}\sum x_i^2\to q=\sigma_x^2\in(0,\infty)$，并$\max_{i\le n}|x_i|/\sqrt n\to0$（有界设计且$q_n\to q>0$足够）。$\psi_i(Y_i-bx_i)=x_i\operatorname{sign}(Y_i-bx_i)$为原定义。
> (a) 原文在$\hat\beta$处写CLT不正确。例如$x_i=1$、$\hat\beta$取样本中位数时，$|\sum\operatorname{sign}(Y_i-\hat\beta)|\le1$，除以$\sqrt n$趋0，不能趋$N(0,1)$。正确CLT在真参数处：$Z_n=n^{-1/2}\sum_i x_i\operatorname{sign}\varepsilon_i$均值0、方差$q_n$，每项绝对值被$\max|x_i|/\sqrt n=o(1)$控制，Lindeberg条件成立，故$Z_n\Rightarrow N(0,q)$，负号不改变极限。
> (b) $E_\beta\psi_i(Y_i-bx_i)=x_i[1-2F((b-\beta)x_i)]$，所以导数在$b=\beta$为$-2f(0)x_i^2$。原题正号漏负号；以该式作合法估计方程线性化仍给最终正方差，但样本得分不可微，下面提供不依赖伪Taylor的证明。
> 设局部目标差$D_n(t)=\sum_i[|\varepsilon_i-tx_i/\sqrt n|-|\varepsilon_i|]$。绝对值恒等式给
> $$D_n(t)=-tZ_n+R_n(t),\quad R_n(t)=2\sum_i\int_0^{t x_i/\sqrt n}[I(\varepsilon_i\le s)-I(\varepsilon_i\le0)]ds.$$
> 由$F(s)=1/2+f(0)s+o(|s|)$及最大小步长趋0，任意固定有界$t$有$ER_n(t)=f(0)t^2q_n+o(1)$。每项余量绝对值不超过$2|h_i|I(|\varepsilon_i|\le|h_i|)$，$h_i=tx_i/\sqrt n$；局部密度有界使其二阶矩不超过常数$|h_i|^3$。独立性给$\operatorname{Var}R_n(t)\le C\max_i|h_i|\sum_i h_i^2\to0$，所以$R_n(t)-f(0)t^2q\to0$依概率。目标差是凸函数，对有限网格用上述收敛，再用网格之间的凸性上下界，可将收敛推广为任意紧区间上的一致收敛。
> 极限二次目标$-tZ_n+f(0)qt^2$的唯一极小点为$Z_n/[2f(0)q]$。该极小点紧；取充分大$M$时二次项支配紧随机线性项，$D_n(-M),D_n(M)>0$的概率任意接近1，凸性使LAD极小点不能逃出此区间。紧区间一致逼近及严格二次曲率遂给
> $$\sqrt n(\hat\beta_L-\beta)=\frac{Z_n}{2f(0)q}+o_P(1)\Rightarrow N\left(0,\frac1{4f(0)^2q}\right).$$
> 这在明确条件下证明最终结论，同时保留(a)估计值符号和(b)导数正号的两处源错。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=523|印刷492／PDF物理523]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=516|印刷485／PDF物理516]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=517|印刷486／PDF物理517]]；所需模型、公式、数据在解答重述。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
