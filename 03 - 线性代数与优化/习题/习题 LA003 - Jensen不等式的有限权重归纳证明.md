---
title: 习题 LA003：Jensen不等式的有限权重归纳证明
topic: linear-algebra-optimization
topic_label: 线性代数与优化
difficulty: intermediate
status: not-started
tags:
- exercise
- linear-algebra-optimization
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 2
source_exercise: '2.33'
source_stars: 2
source_refs:
- DS003 Exercise 2.33，印刷62/PDF82
- DS003 §2.5.5，式(2.101)–(2.102)，印刷52/PDF72
source_status: verified
solution_status: independently-derived
created: '2026-11-01'
---

# 习题 LA003：Jensen不等式的有限权重归纳证明

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 2.33（★★）** Using proof by induction, show that the inequality (2.101) for convex functions implies the result (2.102).

### 中文转述

> [!question] 中文转述
> **原题2.33（★★）。** 用数学归纳法（proof by induction），从凸函数的二点不等式 (2.101)
> $$
> f(\lambda a+(1-\lambda)b)\leq\lambda f(a)+(1-\lambda)f(b),\quad0\leq\lambda\leq1
> $$
> 证明有限加权的 Jensen 不等式 (2.102)：对于 $\lambda_i\geq0$、$\sum_{i=1}^M\lambda_i=1$，
> $$
> f\!\left(\sum_{i=1}^M\lambda_ix_i\right)\leq\sum_{i=1}^M\lambda_if(x_i).
> $$

## 提示

> [!hint]- 提示 1
> 把前 $M$ 个权重之和记为 $s$，将它们归一化后看成一个点。

> [!hint]- 提示 2
> 归一化前先单独处理 $s=0$；否则会出现除以零。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设 $f$ 定义在凸域上，所有 $x_i$ 在该域内；权重非负且总和为一。证明对任意有限正整数 $M$ 成立。
>
> $M=1$ 时是恒等式；$M=2$ 时就是 (2.101)。假设结论对 $M$ 个点成立，考虑 $M+1$ 个点。置
> $$
> s=\sum_{i=1}^M\lambda_i=1-\lambda_{M+1}.
> $$
> 若 $s=0$，则前 $M$ 个权重全为零且 $\lambda_{M+1}=1$，结论仍是恒等式。
>
> 若 $s>0$，定义 $\alpha_i=\lambda_i/s$ 与 $\bar x=\sum_{i=1}^M\alpha_ix_i$。这时 $\sum_i\alpha_i=1$，且 $\bar x$ 仍在凸域内。先用二点凸性，再用归纳假设：
> $$
> \begin{aligned}
> f\!\left(\sum_{i=1}^{M+1}\lambda_ix_i\right)
> &=f\bigl(s\bar x+(1-s)x_{M+1}\bigr)\\
> &\leq sf(\bar x)+(1-s)f(x_{M+1})\\
> &\leq s\sum_{i=1}^M\alpha_if(x_i)+\lambda_{M+1}f(x_{M+1})\\
> &=\sum_{i=1}^{M+1}\lambda_if(x_i).
> \end{aligned}
> $$
> 其中 $s=1$ 也完全允许。归纳完成，零权重无需删除也能覆盖。本题仅证明有限和形式；连续分布下的积分版本还需可积性及适当极限论证。

## 相关概念

- [[03 - 线性代数与优化/概念/凸函数|凸函数]]
- [[03 - 线性代数与优化/概念/凸集|凸集]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=82|印刷62／PDF物理82]]；已对照原始页面核对英文、星号与分问。
- 题面只有公式引用，中文转述按实际查看的正文补出两式，方便独立阅读。
- `source_status: verified` 仅指本题及实际所用定位核对；独立解答不等于用户已完成学习，状态保持 `not-started`。
