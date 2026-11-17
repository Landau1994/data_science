---
title: "习题 ST363：ANOVA线性组合的双侧与单侧Student检验"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.9，印刷页457／PDF物理页488"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.9"
source_stars: 0
source_refs: ["DS011 Exercise 11.9，印刷457／PDF物理488", "DS011 线性对比Student统计量式(11.2.7)，印刷427／PDF物理458"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST363：ANOVA线性组合的双侧与单侧Student检验

## 题目

### 英文原题

> [!question] 英文原题
> **11.9** Using an argument similar to that which led to the $t$ test in (11.2.7), show how to construct a $t$ test for
>
> (a) $H_0:\sum a_i\theta_i=\delta$ versus $H_1:\sum a_i\theta_i\ne\delta$,
>
> (b) $H_0:\sum a_i\theta_i\le\delta$ versus $H_1:\sum a_i\theta_i>\delta$, where $\delta$ is a specified constant.

### 中文转述

> [!question] 中文转述
> **原题11.9。** 利用类似推导式11.2.7的$t$检验的论证，说明如何对下列假设构造$t$检验：
>
> (a)  $H_0:\sum a_i\theta_i=\delta$对$H_1:\sum a_i\theta_i\ne\delta$.
>
> (b)  $H_0:\sum a_i\theta_i\le\delta$对$H_1:\sum a_i\theta_i>\delta$，其中$\delta$为指定常数.

## 提示

> [!hint]- 提示
> 正态线性组合除以独立合并标准差，得到Student枢轴。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 假定独立正态同方差ANOVA，$\nu=N-k>0$、$C=\sum_i a_i^2/n_i>0$，$S_p^2=\sum_{ij}(Y_{ij}-\bar Y_i)^2/\nu$。组均值向量与$S_p^2$独立，$\nu S_p^2/\sigma^2\sim\chi_\nu^2$。令$\psi=\sum_i a_i\theta_i$、$W=\sum_i a_i\bar Y_i$，有$(W-\psi)/(\sigma\sqrt C)\sim n(0,1)$。因此边界$\psi=\delta$下
> $$
> T=\frac{W-\delta}{S_p\sqrt C}\sim t_\nu.
> $$
> 用$t_{\nu,\gamma}$表示右尾概率$\gamma$的分位数。
>
> **(a)** 水平$\alpha$双侧检验在$|T|>t_{\nu,\alpha/2}$时拒绝，边界下尺寸恰为$\alpha$，p值$2P(t_\nu\ge|T_{obs}|)$。
>
> **(b)** 在$T>t_{\nu,\alpha}$时拒绝。对任意$\psi\le\delta$，条件于正分母，$W-\delta$相对边界正态向左移，所以拒绝概率不大于边界的$\alpha$；因此对复合原假设有效，最不利参数在$\psi=\delta$。
>
> 若$C=0$，全部系数为0，目标恒等于0，只能按给定$\delta$判断空或平凡假设，Student标准化不可用。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=488|印刷第457页／PDF物理第488页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
