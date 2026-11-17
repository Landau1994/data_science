---
title: "习题 ST360：ANOVA组均值与合并方差的充分独立及典范化"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.6，印刷页456／PDF物理页487"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.6"
source_stars: 0
source_refs: ["DS011 Exercise 11.6，印刷456／PDF物理487", "DS011 单因素ANOVA模型(11.2.1)，印刷422／PDF物理453", "DS011 经典ANOVA假设，印刷423／PDF物理454", "DS011 杂录11.5.6的典范正态均值模型，印刷465／PDF物理496"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST360：ANOVA组均值与合并方差的充分独立及典范化

## 题目

### 英文原题

> [!question] 英文原题
> **11.6** Under the oneway ANOVA assumptions:
>
> (a) Show that the set of statistics $(\bar Y_{1\cdot},\bar Y_{2\cdot},\ldots,\bar Y_{k\cdot},S_p^2)$ is sufficient for $(\theta_1,\theta_2,\ldots,\theta_k,\sigma^2)$.
>
> (b) Show that $S_p^2=\frac1{N-k}\sum_{i=1}^k(n_i-1)S_i^2$ is independent of each $\bar Y_{i\cdot}$, $i=1,\ldots,k$. (See Lemma 5.3.3.)
>
> (c) If $\sigma^2$ is known, explain how the anova data are equivalent to their canonical version in Miscellanea 11.5.6.

### 中文转述

> [!question] 中文转述
> **原题11.6。** 在单因素ANOVA假设下：
>
> (a)  证明统计量组$(\bar Y_{1\cdot},\bar Y_{2\cdot},\ldots,\bar Y_{k\cdot},S_p^2)$对$(\theta_1,\theta_2,\ldots,\theta_k,\sigma^2)$充分.
>
> (b)  证明$S_p^2=\frac1{N-k}\sum_{i=1}^k(n_i-1)S_i^2$与每个$\bar Y_{i\cdot}$独立，$i=1,\ldots,k$. （见引理5.3.3.）
>
> (c)  若$\sigma^2$已知，说明ANOVA数据如何等价于杂录11.5.6中的典范形式.

## 提示

> [!hint]- 提示
> 组内平方分解给充分性，正态均值与残差的零协方差给独立性。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 单因素ANOVA假设为全部$Y_{ij}$独立、$Y_{ij}\sim n(\theta_i,\sigma^2)$，$\sigma^2>0$。令$N=\sum_i n_i$、$\nu=N-k>0$、$W=\sum_{ij}(Y_{ij}-\bar Y_{i\cdot})^2$，$S_p^2=W/\nu$。若某$n_i=1$，用$W$定义其零残差贡献，避免写未定义的单组$S_i^2$。
>
> **(a)** 分组平方分解给
> $$
> \sum_{ij}(y_{ij}-\theta_i)^2=W+\sum_i n_i(\bar y_{i\cdot}-\theta_i)^2.
> $$
> 联合密度$(2\pi\sigma^2)^{-N/2}\exp[-\{W+\sum_i n_i(\bar y_i-\theta_i)^2\}/(2\sigma^2)]$只通过组均值和$W$依赖数据，因子分解定理给充分性。
>
> **(b)** 每组均值与其残差向量的协方差为$\operatorname{Cov}(\bar Y_i,Y_{ij}-\bar Y_i)=\sigma^2/n_i-\sigma^2/n_i=0$。这些变量联合正态，故均值与整组残差独立；不同组独立，因而整份组均值向量与整份残差向量独立。$S_p^2$是残差函数，所以它与所有组均值**联合独立**，比单独两两独立更强。每组残差的正交分解还给$W/\sigma^2\sim\chi_\nu^2$。
>
> **(c)** 已知$\sigma$时，充分组均值经一一变换$X_i=\sqrt{n_i}\bar Y_i/\sigma$，有独立$X_i\sim n(\eta_i,1)$，其中$\eta_i=\sqrt{n_i}\theta_i/\sigma$，正是典范正态均值模型。残差与均值独立且分布不含$\boldsymbol\theta$；给定组均值可按参数无关条件分布恢复原实验，所以在关于均值参数的信息上等价。估计与损失须按这一定标同步变换，不能仅将异方差组均值直接称作单位方差。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=487|印刷第456页／PDF物理第487页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
