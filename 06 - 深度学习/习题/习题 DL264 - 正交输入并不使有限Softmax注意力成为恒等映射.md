---
title: "习题 DL264：正交输入并不使有限Softmax注意力成为恒等映射"
topic: deep-learning
topic_label: 深度学习
difficulty: beginner
status: not-started
tags:
  - exercise
  - deep-learning
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop 深度学习（DS003）]]"
source_id: DS003
source_chapter: 12
source_exercise: "12.3"
source_stars: 1
source_refs:
  - "DS003 Exercise 12.3，印刷404/PDF420"
  - "DS003 §12.1.2–12.1.3，式12.2–12.6，印刷362–363/PDF378–379"
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL264：正交输入并不使有限Softmax注意力成为恒等映射

## 题目

### 英文原题

> [!question] 英文原题
> **12.3 (★)** Consider the input vectors $\mathbf{x}_n$ in the simple transformation defined by (12.2), in which the weighting coefficients $a_{nm}$ are defined by (12.5). Show that if all the input vectors are orthogonal, so that $\mathbf{x}_n^T\mathbf{x}_m=0$ for $n\ne m$, then the output vectors will simply be equal to the input vectors so that $\mathbf{y}_n=\mathbf{x}_n$ for $n=1,\ldots,N$.

### 中文转述

> [!question] 中文转述
> 考虑式(12.2)的简单变换，其权重由(12.5)定义。若输入向量两两正交，即$n\ne m$时$\mathbf x_n^T\mathbf x_m=0$，证明输出等于输入，即对$n=1,\ldots,N$有$\mathbf y_n=\mathbf x_n$。

## 提示

> [!hint]- 提示 1
> 正交时非对角打分为零，但$\exp(0)$是多少？

## 解答

> [!success]- 解答
> **独立推导。**
>
> 原命题对一般有限输入不成立。正交性只使非对角打分为零，并不使其Softmax权重为零。实际上
> $$
> a_{nn}=\frac{e^{\|x_n\|^2}}{e^{\|x_n\|^2}+N-1},\qquad
> a_{nm}=\frac1{e^{\|x_n\|^2}+N-1}\quad(m\ne n),
> $$
> 故
> $$
> y_n=\frac{e^{\|x_n\|^2}x_n+\sum_{m\ne n}x_m}{e^{\|x_n\|^2}+N-1}.
> $$
> 取$N=D=2$、$x_1=(1,0)^T$、$x_2=(0,1)^T$，两输入正交，却有
> $$
> y_1=\left(\frac e{e+1},\frac1{e+1}\right)^T\ne x_1.
> $$
> 对非零两两正交向量，若$N>1$，其他正交方向出现的严格正系数不能相互抵消，所以通常不可能等于$x_n$。
>
> 若改用硬注意力选择唯一最大打分，或固定非零正交输入后把打分除以温度$\tau$并令$\tau\downarrow0$，才会使$a_{nn}\to1$、非对角权重趋零，从而$y_n\to x_n$。$N=1$也是精确成立的特例。这些是补充条件或极限，均不是题述有限Softmax自动满足的结论。

## 相关概念

- [[06 - 深度学习/概念/自注意力|自注意力]]
- [[06 - 深度学习/概念/Transformer|Transformer]]

## 备注

- 原题已核对 DS003 印刷404页／PDF物理420页；正文引用的实际核对范围见 `source_refs`。
- 原题及正文印刷363/PDF379均有相同断言，完整保留；解答以式12.5直接计算并给出反例，不伪造证明。
- 解答为独立推导；归档与个人学习状态分开，学习状态保持 `not-started`。
