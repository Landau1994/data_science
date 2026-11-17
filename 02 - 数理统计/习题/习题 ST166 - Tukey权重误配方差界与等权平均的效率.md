---
title: "习题 ST166：Tukey权重误配方差界与等权平均的效率"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.43，印刷页294／PDF物理页325"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.43"
source_stars: 0
source_refs: ["DS011 Exercise 7.43，印刷294／PDF物理325"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST166：Tukey权重误配方差界与等权平均的效率

## 题目

### 英文原题

> [!question] 英文原题
> **7.43** Exercise 7.42 established that the optimal weights are $q_i^*=(1/\sigma_i^2)/(\sum_j1/\sigma_j^2)$. A result due to Tukey (see Bloch and Moses 1988) states that if $W=\sum_iq_iW_i$ is an estimator based on another sets of weights $q_i\ge0$, $\sum_iq_i=1$, then
> $$
> \frac{\operatorname{Var}W}{\operatorname{Var}W^*}\le\frac1{1-\lambda^2}
> $$
> where $\lambda$ satisfies $(1+\lambda)/(1-\lambda)=b_{\max}/b_{\min}$, and $b_{\max}$ and $b_{\min}$ are the largest and smallest of $b_i=q_i/q_i^*$.
>
> (a) Prove Tukey’s inequality.
>
> (b) Use the inequality to assess the performance of the usual mean $\sum_iW_i/k$ as a function of $\sigma_{\max}^2/\sigma_{\min}^2$.

### 中文转述

> [!question] 中文转述
> **原题7.43。** 习题7.42确立了最优权重$q_i^*=(1/\sigma_i^2)/(\sum_j1/\sigma_j^2)$.Tukey的一个结果（见Bloch和Moses 1988）指出：若$W=\sum_iq_iW_i$基于另一组权重$q_i\ge0$、$\sum_iq_i=1$，则
>
> $$
> \frac{\operatorname{Var}W}{\operatorname{Var}W^*}\le\frac1{1-\lambda^2},
> $$
>
> 其中$\lambda$满足$(1+\lambda)/(1-\lambda)=b_{\max}/b_{\min}$，而$b_{\max}$与$b_{\min}$分别为$b_i=q_i/q_i^*$的最大和最小值.
>
> (a)  证明Tukey不等式.
>
> (b)  利用该不等式，作为$\sigma_{\max}^2/\sigma_{\min}^2$的函数评估通常均值$\sum_iW_i/k$的表现.

## 提示

> [!hint]- 提示
> 把最优权重当作概率质量，方差比就成了相对权重的二阶矩。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 沿用7.42的正有限方差与两两不相关假设。令$C=\sum_i1/\sigma_i^2$，以$q_i^*$作为一个离散概率分布的质量，记对应期望为$E_*$。
>
> **(a)** $E_*b=\sum_i q_i=1$，且
> $$
> \frac{\operatorname{Var}W}{\operatorname{Var}W^*}
> =C\sum_iq_i^2\sigma_i^2=\sum_iq_i^*b_i^2=E_*b^2.
> $$
> 设$a=b_{\min}>0,B=b_{\max}$。逐点$(b-a)(b-B)\le0$给$E_*b^2\le a+B-aB$。令$r=B/a\ge1$，再配方得
> $$
> a+B-aB=(1+r)a-ra^2\le\frac{(1+r)^2}{4r}.
> $$
> 题中$\lambda=(r-1)/(r+1)$，所以右边正是$1/(1-\lambda^2)$，证明完成。若$a=0$，原比$r$为无穷，$\lambda=1$，只剩无穷的平凡上界；原题允许零权重，必须说明这个极限情形。若$r=1$，所有$b_i=1$、$W=W^*$，界为1。
>
> **(b)** 等权$q_i=1/k$时$b_i=C\sigma_i^2/k$，故$r=\sigma_{\max}^2/\sigma_{\min}^2$。从最优性及上界得到
> $$
> 1\le\frac{\operatorname{Var}(k^{-1}\sum_iW_i)}{\operatorname{Var}W^*}
> \le\frac{(r+1)^2}{4r}.
> $$
> 例如$r=1$时等权最优；$r=4$时方差损失至多$25/16$，效率（最优方差除以实际方差）至少$16/25$。这是极差比给的保证，实际损失也取决于各方差在范围内的分布，不能把上界说成精确比值。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=325|印刷第294页／PDF物理第325页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
