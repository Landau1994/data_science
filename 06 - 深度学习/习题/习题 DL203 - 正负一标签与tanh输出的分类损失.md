---
title: "习题 DL203：正负一标签与tanh输出的分类损失"
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags:
  - exercise
  - deep-learning
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop 深度学习（DS003）]]"
source_id: DS003
source_chapter: 6
source_exercise: "6.12"
source_stars: 2
source_refs: ["DS003 Exercise 6.12，印刷207/PDF225", "DS003 §6.4.2，式(6.32)–(6.33)，印刷196/PDF214", "DS003 §6.2.3，式(6.13)–(6.14)，印刷183–184/PDF201–202"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL203：正负一标签与tanh输出的分类损失

## 题目

### 英文原题

> [!question] 英文原题
> **6.12 (★★)** The error function (6.33) for binary classification problems was derived for a network having a logistic-sigmoid output activation function, so that $0\le y(\mathbf x,\mathbf w)\le1$, and data having target values $t\in\{0,1\}$. Derive the corresponding error function if we consider a network having an output $-1\le y(\mathbf x,\mathbf w)\le1$ and target values $t=1$ for class $C_1$ and $t=-1$ for class $C_2$. What would be the appropriate choice of output-unit activation function?

### 中文转述

> [!question] 中文转述
> **原题6.12。** 原书式(6.33)针对输出范围为 $[0,1]$ 的逻辑Sigmoid网络，标签编码为 $t\in\{0,1\}$。现改为输出 $-1\le y(\mathbf x,\mathbf w)\le1$，类别 $C_1$ 标签为1、类别 $C_2$ 标签为 $-1$。推导相应误差函数，并指出合适的输出激活函数（output-unit activation function）。

## 提示

> [!hint]- 提示 1
> 令 $p(C_1\mid x)=(1+y)/2$、$p(C_2\mid x)=(1-y)/2$，同时把标签指示量写成 $(1+t)/2$ 与 $(1-t)/2$。

> [!hint]- 提示 2
> 激活函数应将实数预激活映射到 $(-1,1)$。不要直接把可能为负的输出 $y$ 代入普通伯努利交叉熵的 $\ln y$。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 用输出 $y$ 表示两类概率之差，即 $y=p(C_1\mid x)-p(C_2\mid x)$。由两类概率和为1，得到
> $$
> p(C_1\mid x)=\frac{1+y}{2},\qquad p(C_2\mid x)=\frac{1-y}{2}.
> $$
> 对 $t\in\{-1,1\}$，$(1+t)/2$ 与 $(1-t)/2$ 恰好是两类的指示量。因此条件概率为
> $$
> p(t\mid\mathbf x,\mathbf w)
> =\left(\frac{1+y}{2}\right)^{(1+t)/2}
> \left(\frac{1-y}{2}\right)^{(1-t)/2}.
> $$
> 在独立训练样本下取负对数，得到完整误差
> $$
> E(\mathbf w)=-\frac12\sum_{n=1}^N
> \left[(1+t_n)\ln\frac{1+y_n}{2}
> +(1-t_n)\ln\frac{1-y_n}{2}\right].
> $$
> 因为每个标签只能为 $\pm1$，也可简写成
> $$
> E(\mathbf w)=-\sum_n\ln\frac{1+t_ny_n}{2}.
> $$
> 这些对数中的除以2保证了确切的概率与似然；若只优化参数，可把相应常数单独拿出，但不能把未经归一化的 $1+y$ 当作概率。
>
> 一个自然的输出激活是 $y_n=\tanh(a_n)$。它对有限实数 $a_n$ 取值于 $(-1,1)$，并满足
> $$
> \frac{1+\tanh a_n}{2}=\sigma(2a_n).
> $$
> 于是模型等价于使用二倍logit的普通伯努利分类器，单样本损失也可写为 $\ln(1+e^{-2t_na_n})$。直接求导得到
> $$
> \frac{\partial E_n}{\partial a_n}
> =-\frac{t_n(1-y_n^2)}{1+t_ny_n}=y_n-t_n,
> $$
> 最后一步使用 $t_n^2=1$。这同时核对了输出概率与标签编码的尺度。
>
> 端点 $y=\pm1$ 对应一个类别概率为0，有限tanh预激活不能精确达到；若被赋零概率的类别恰为观察标签，负对数似然为 $+\infty$。因此用端点时应按概率边界或极限解释，而非对负数或零作不合法的普通对数运算。

## 相关概念

- [[04 - 统计学习/概念/交叉熵|交叉熵]]
- [[06 - 深度学习/概念/激活函数|激活函数]]
- [[01 - 概率论/概念/条件概率|条件概率]]

## 备注

- 原题已核对 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=225|印刷207／PDF物理225]]；所引正文公式的实际位置见 `source_refs`。
- 原题允许闭区间输出；所选tanh对有限预激活只取开区间值，闭端点及零概率的意义在解答中分别说明。
- `source_status: verified` 只指本题原文、所列公式与定位核对，不表示整章或整书理论全部核验。解答未使用配套答案册；个人学习状态保留 `not-started`。
