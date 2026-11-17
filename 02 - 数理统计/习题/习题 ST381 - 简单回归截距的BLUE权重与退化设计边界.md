---
title: "习题 ST381：简单回归截距的BLUE权重与退化设计边界"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.27，印刷页460／PDF物理页491"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.27"
source_stars: 0
source_refs: ["DS011 Exercise 11.27，印刷460／PDF物理491"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST381：简单回归截距的BLUE权重与退化设计边界

## 题目

### 英文原题

> [!question] 英文原题
> **11.27** Observations $(x_i,Y_i)$, $i=1,\ldots,n$, follow the model $Y_i=\alpha+\beta x_i+\varepsilon_i$, where $E\varepsilon_i=0$, $\operatorname{Var}\varepsilon_i=\sigma^2$, and $\operatorname{Cov}(\varepsilon_i,\varepsilon_j)=0$ if $i\ne j$. Find the best linear, unbiased estimator of $\alpha$.

### 中文转述

> [!question] 中文转述
> **原题11.27。** 观测$(x_i,Y_i)$，$i=1,\ldots,n$，服从模型$Y_i=\alpha+\beta x_i+\varepsilon_i$，其中$E\varepsilon_i=0$、$\operatorname{Var}\varepsilon_i=\sigma^2$，且$i\ne j$时$\operatorname{Cov}(\varepsilon_i,\varepsilon_j)=0$. 求$\alpha$的最优线性无偏估计量.

## 提示

> [!hint]- 提示
> 把任意无偏权重写成最小二乘权重加上满足两个零约束的扰动。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 先假定$S_{xx}=\sum_i(x_i-\bar x)^2>0$、$\sigma^2>0$。常数权重线性规则$T=\sum_iw_iY_i$对全部$\alpha,\beta$无偏的充要条件为$\sum_iw_i=1$、$\sum_iw_ix_i=0$。
>
> 令$c_i=1/n-\bar x(x_i-\bar x)/S_{xx}$，则这两个约束成立，给$\widehat\alpha=\sum_i c_iY_i=\bar Y-\widehat\beta\bar x$。对任何其他可行权重，写$w_i=c_i+h_i$，有$\sum_i h_i=\sum_i h_ix_i=0$；因为$c_i$是$x_i$的仿射函数，$\sum_i c_i h_i=0$，所以
> $$
> \operatorname{Var}T=\sigma^2\sum_iw_i^2
> =\sigma^2\sum_i c_i^2+\sigma^2\sum_i h_i^2
> \ge\sigma^2\left(\frac1n+\frac{\bar x^2}{S_{xx}}\right).
> $$
> 等号只在$h_i=0$，故$\widehat\alpha$为唯一最佳线性无偏估计（BLUE）。证明只需不相关同方差与有限二阶矩，无需正态性。
>
> 若全部$x_i=x_0\ne0$，可观测均值只有$\alpha+\beta x_0$，约束$\sum_i w_ix_i=0$与$\sum_iw_i=1$矛盾，因此截距不可无偏线性估计。若全部$x_i=0$，则$\bar Y$是截距的BLUE、方差$\sigma^2/n$，虽然斜率不可识别。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=491|印刷第460页／PDF物理第491页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
