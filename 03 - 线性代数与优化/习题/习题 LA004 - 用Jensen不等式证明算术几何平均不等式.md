---
title: 习题 LA004：用Jensen不等式证明算术几何平均不等式
topic: linear-algebra-optimization
topic_label: 线性代数与优化
difficulty: beginner
status: not-started
tags:
- exercise
- linear-algebra-optimization
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 2
source_exercise: '2.37'
source_stars: 1
source_refs:
- DS003 Exercise 2.37，印刷62/PDF82
- DS003 §2.5.5，式(2.101)–(2.102)，印刷52/PDF72
source_status: verified
solution_status: independently-derived
created: '2026-11-01'
---

# 习题 LA004：用Jensen不等式证明算术几何平均不等式

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 2.37（★）** By applying Jensen’s inequality (2.102) with $f(x)=\ln x$, show that the arithmetic mean of a set of real numbers is never less than their geometrical mean.

### 中文转述

> [!question] 中文转述
> **原题2.37（★）。** 对 $f(x)=\ln x$ 应用 Jensen 不等式 (2.102)，证明一组实数的算术平均（arithmetic mean）不小于几何平均（geometrical mean）。

## 提示

> [!hint]- 提示 1
> $\ln x$ 在正半轴上严格凹，使用凸函数版本时应改取 $-\ln x$。

> [!hint]- 提示 2
> 取相等权重 $1/M$，再对对数不等式两边取指数。

## 解答

> [!success]- 解答
> **证明范围：独立推导，补明定义域。** 设 $M\geq1$ 且 $a_1,\ldots,a_M>0$。由于 $f''(x)=-1/x^2<0$，对数是严格凹函数，因此 Jensen 的凹函数版本给出
> $$
> \ln\left(\frac1M\sum_{i=1}^Ma_i\right)
> \geq\frac1M\sum_{i=1}^M\ln a_i
> =\ln\left(\prod_{i=1}^Ma_i\right)^{1/M}.
> $$
> 指数函数严格递增，故
> $$
> \frac{a_1+\cdots+a_M}{M}\geq(a_1\cdots a_M)^{1/M}.
> $$
> $M\geq2$ 时，由对数的严格凹性，等号成立当且仅当所有 $a_i$ 相等；$M=1$ 时恒等。
>
> 若允许 $a_i\geq0$，当存在零项时，几何平均为零而算术平均非负，结论直接成立；等号要求全部为零，仍等价于各数相等。也可先对 $a_i+\varepsilon$ 用上式再令 $\varepsilon\downarrow0$。
>
> 题面若真的允许任意实数则不成立。例如两个数均为 $-1$ 时，按正平方根取几何平均为1，算术平均为 $-1$，反向违背原断言；有的负数集合还没有实数几何平均。故本题应在非负实数上陈述，并在使用 $\ln$ 时先限制为正数。

## 相关概念

- [[03 - 线性代数与优化/概念/凸函数|凸函数]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=82|印刷62／PDF物理82]]；已对照原始页面核对英文、星号与分问。
- 补充正数／非负数条件，并说明ln是凹函数，因此不等号方向与正文的凸函数式(2.102)相反。未把该修正写入英文原题。
- `source_status: verified` 仅指本题及实际所用定位核对；独立解答不等于用户已完成学习，状态保持 `not-started`。
