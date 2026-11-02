---
title: 习题 ML044：Logistic sigmoid的导数恒等式
topic: statistical-learning
topic_label: 统计学习
difficulty: beginner
status: not-started
tags:
- exercise
- statistical-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 5
source_exercise: '5.18'
source_stars: 1
source_refs:
- DS003 Exercise 5.18，印刷168/PDF187
- DS003 §5.3，式(5.42)，印刷151/PDF170
- DS003 §5.4.3，式(5.72)，印刷160/PDF179
- DS004 Solution 5.18，印刷57/PDF57
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML044：Logistic sigmoid的导数恒等式

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 5.18（★）** Verify the relation (5.72) for the derivative of the logistic sigmoid function defined by (5.42).

### 中文转述

> [!question] 中文转述
> **原题5.18（★）。** 验证式 (5.42) 定义的 Logistic sigmoid 函数（logistic sigmoid function）
> $$
> \sigma(a)=\frac1{1+e^{-a}}\tag{5.42}
> $$
> 满足导数关系
> $$
> \frac{\mathrm d\sigma}{\mathrm da}=\sigma(a)(1-\sigma(a)).\tag{5.72}
> $$

## 提示

> [!hint]- 提示 1
> 先把分母整体看成一个函数，使用倒数求导和链式法则。

> [!hint]- 提示 2
> 把 $e^{-a}/(1+e^{-a})$ 改写成 $1-1/(1+e^{-a})$。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 对任意有限实数 $a$，$1+e^{-a}>0$，函数光滑且 $0<\sigma(a)<1$。逐步求导得
> $$
> \begin{aligned}
> \sigma'(a)
> &=-(1+e^{-a})^{-2}(-e^{-a})\\
> &=\frac{e^{-a}}{(1+e^{-a})^2}\\
> &=\frac1{1+e^{-a}}\left(1-\frac1{1+e^{-a}}\right)\\
> &=\sigma(a)(1-\sigma(a)).
> \end{aligned}
> $$
> 这就得到式 (5.72)。因为 $u(1-u)=1/4-(u-1/2)^2$，还有 $0<\sigma'(a)\leq1/4$，等号仅当 $a=0$；当 $a\to\pm\infty$ 时导数趋于零。最后的极限不意味着在有限输入处导数等于零。

## 相关概念

- [[06 - 深度学习/概念/激活函数|激活函数]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]

## 备注

- 原题与星号：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=187|印刷168／PDF物理187]]；原题及实际引用的正文页均已对照原始PDF图像。正文精确定位见 `source_refs`。
- 已查看[[00 - 首页/教材归档/DS004 - Bishop 深度学习答案册|DS004]]印刷57／PDF57的5.18；上述求导为独立展开。
- `source_status: verified` 仅指本题及所列实际核对范围；独立解答不构成个人完成学习，状态保持 `not-started`。
