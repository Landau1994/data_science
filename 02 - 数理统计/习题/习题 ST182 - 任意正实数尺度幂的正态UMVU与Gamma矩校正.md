---
title: "习题 ST182：任意正实数尺度幂的正态UMVU与Gamma矩校正"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.59，印刷页296／PDF物理页327"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.59"
source_stars: 0
source_refs: ["DS011 Exercise 7.59，印刷296／PDF物理327", "DS011 满秩指数族的完备性定理6.2.25，印刷234／PDF物理265", "DS011 定理7.3.23完备充分量的无偏最优性，印刷280／PDF物理311"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST182：任意正实数尺度幂的正态UMVU与Gamma矩校正

## 题目

### 英文原题

> [!question] 英文原题
> **7.59** Let $X_1,\ldots,X_n$ be iid $n(\mu,\sigma^2)$. Find the best unbiased estimator of $\sigma^p$, where $p$ is a known positive constant, not necessarily an integer.

### 中文转述

> [!question] 中文转述
> **原题7.59。** 设$X_1,\ldots,X_n$独立同分布于$n(\mu,\sigma^2)$.求$\sigma^p$的最佳无偏估计量，其中$p$是已知正常数，不一定是整数.

## 提示

> [!hint]- 提示
> 卡方变量的任意正实数矩可直接用Gamma积分计算。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 要求$n\ge2$、$\sigma>0$，令$\nu=n-1$、$S^2=\sum_i(X_i-\bar X)^2/\nu$。$Q=\nu S^2/\sigma^2\sim\chi_\nu^2$，直接Gamma积分给
> $$
> EQ^{p/2}=2^{p/2}\frac{\Gamma((\nu+p)/2)}{\Gamma(\nu/2)},
> \quad
> E(S^p)=\sigma^p(2/\nu)^{p/2}\frac{\Gamma((\nu+p)/2)}{\Gamma(\nu/2)}.
> $$
> 因此无偏规则为
> $$
> \widehat{\sigma^p}=\left(\frac\nu2\right)^{p/2}
> \frac{\Gamma(\nu/2)}{\Gamma((\nu+p)/2)}S^p.
> $$
> 因为$p>0$，卡方的$p$及$2p$相关正矩都有限，方差比较合法。正态两参数族自然统计量$(\sum_iX_i,\sum_iX_i^2)$的自然参数空间$\{(\mu/\sigma^2,-1/(2\sigma^2))\}=\mathbb R\times(-\infty,0)$为二维开区域，所以由满秩指数族完备性准则，这个统计量完备充分。它与$(\bar X,S^2)$一一等价，所给估计是其函数，故为唯一最佳无偏估计。$p=2$时系数为1恢复$S^2$，$p=1$恢复样本标准差的经典无偏Gamma校正。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=327|印刷第296页／PDF物理第327页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
