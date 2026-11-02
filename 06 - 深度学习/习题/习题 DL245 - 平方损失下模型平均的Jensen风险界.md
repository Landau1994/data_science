---
title: "习题 DL245：平方损失下模型平均的Jensen风险界"
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags: [exercise, deep-learning]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 9
source_exercise: "9.15"
source_stars: 2
source_refs: ["DS003 Exercise 9.15，印刷284／PDF物理301", "DS003 §9.6，式(9.43)–(9.50)，印刷278–279/PDF295–296"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL245：平方损失下模型平均的Jensen风险界

## 题目

### 英文原题

> [!question] 英文原题
> **9.15 (★★)** By making use of Jensen’s inequality (2.102) for the special case of the convex function $f(x)=x^2$, show that the average expected sum-of-squares error $E_{\rm AV}$ of the members of a simple committee model, given by (9.46), and the expected error $E_{\rm COM}$ of the committee itself, given by (9.47), satisfy
> $$
> E_{\rm COM}\le E_{\rm AV}.\tag{9.64}
> $$

### 中文转述

> [!question] 中文转述
> 对凸函数 $f(x)=x^2$ 使用Jensen不等式(2.102)，证明(9.46)的个体平均平方风险与(9.47)的委员会风险满足 $E_{\rm COM}\le E_{\rm AV}$。

## 提示

> [!hint]- 提示
> 可先逐个固定输入证明平方平均不超过平均平方，再对输入分布积分。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 令 $M\ge1$，$y_m(x)=h(x)+\epsilon_m(x)$，委员会平均为 $y_{\rm COM}=M^{-1}\sum_my_m$。所引两个风险为
> $$
> E_{\rm AV}=\frac1M\sum_m\mathbb E_X[\epsilon_m(X)^2],\quad
> E_{\rm COM}=\mathbb E_X\left[\left(\frac1M\sum_m\epsilon_m(X)\right)^2\right].\tag{9.46–9.47}
> $$
> 对固定 $x$，记 $\bar\epsilon=M^{-1}\sum_m\epsilon_m$。平方函数凸性的有限Jensen式为 $(M^{-1}\sum_m\epsilon_m)^2\le M^{-1}\sum_m\epsilon_m^2$。其差也能直接算为
> $$
> \frac1M\sum_m\epsilon_m^2-\bar\epsilon^2
> =\frac1M\sum_m(\epsilon_m-\bar\epsilon)^2\ge0.
> $$
> 若各误差二阶矩有限，取 $X$ 期望便得 $E_{\rm COM}\le E_{\rm AV}$。由差值公式，等号当且仅当所有模型的误差在共同输入分布下几乎处处相同（等价所有预测几乎处处相同）。无需误差零均值或不相关，因此此界比上题的 $1/M$ 因子需要更少假设。但它比较的是**个体风险的平均**，不保证委员会优于其中每个成员或最好的成员。

## 相关概念

- [[04 - 统计学习/概念/集成学习|集成学习]]
- [[03 - 线性代数与优化/概念/凸函数|凸函数]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=301|印刷284／PDF物理301]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
