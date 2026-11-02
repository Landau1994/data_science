---
title: 习题 LA016：由Euler公式推导周期变量的三角恒等式
topic: linear-algebra-optimization
topic_label: 线性代数与优化
difficulty: beginner
status: not-started
tags:
- exercise
- linear-algebra-optimization
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 3
source_exercise: '3.30'
source_stars: 1
source_refs:
- DS003 Exercise 3.30，印刷109–110/PDF128–129
- DS003 §3.3，式(3.127)–(3.128)及(3.133)，印刷91–92/PDF110–111
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 LA016：由Euler公式推导周期变量的三角恒等式

## 题目

### 英文原题

> [!question] 英文原题
> **3.30 (★)** The various trigonometric identities used in the discussion of periodic variables in this chapter can be proven easily from the relation
> $$
> \exp(iA)=\cos A+i\sin A\tag{3.214}
> $$
> in which $i$ is the square root of minus one. By considering the identity
> $$
> \exp(iA)\exp(-iA)=1\tag{3.215}
> $$
> prove the result (3.127). Similarly, using the identity
> $$
> \cos(A-B)=\Re\exp\{i(A-B)\}\tag{3.216}
> $$
> where $\Re$ denotes the real part, prove (3.128). Finally, by using $\sin(A-B)=\Im\exp\{i(A-B)\}$, where $\Im$ denotes the imaginary part, prove the result (3.133).

### 中文转述

> [!question] 中文转述
> **原题3.30。** 利用Euler公式（Euler formula）分别证明平方和、余弦差角与正弦差角恒等式，即(3.127)、(3.128)、(3.133)。

## 提示

> [!hint]- 提示
> 将两个复指数展开相乘，比较实部和虚部。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 由复共轭，$e^{iA}e^{-iA}=(\cos A+i\sin A)(\cos A-i\sin A)=\cos^2A+\sin^2A=1$，得到(3.127)。再展开
> $$
> \begin{aligned}
> e^{i(A-B)}&=(\cos A+i\sin A)(\cos B-i\sin B)\\
> &=\cos A\cos B+\sin A\sin B+i(\sin A\cos B-\cos A\sin B).
> \end{aligned}
> $$
> 取实部得 $\cos(A-B)=\cos A\cos B+\sin A\sin B$，即(3.128)；取虚部得 $\sin(A-B)=\cos B\sin A-\cos A\sin B$，即(3.133)。所有角均为实数，无需除以正弦或余弦，因此在这些函数为零时也成立。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=128|印刷109–110／PDF128–129]]；正文引用范围见 `source_refs`。
- 原题跨印刷109–110／PDF128–129。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
