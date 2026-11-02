---
title: 习题 DL297：共享参数神经ODE梯度与积分符号修正
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags:
- exercise
- deep-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 18
source_exercise: '18.7'
source_stars: 2
source_refs:
- DS003 Exercise 18.7，印刷560/PDF572
- DS003 式(8.10)，印刷236/PDF253；共享参数与式(18.26)，印刷556/PDF568
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 DL297：共享参数神经ODE梯度与积分符号修正

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 18.7（★★）** By making use of the result (8.10), write down an expression for the gradient of a loss function $L(\mathbf z(T))$ for a multilayered residual network defined by (18.38) in which all layers share the same parameter vector $\mathbf w$. By taking the limit $\epsilon\to0$, derive the equation (18.26) for the derivative of the loss function.

### 中文转述

> [!question] 中文转述
> **原题18.7。** 利用(8.10)，写出由(18.38)定义、各层共享同一参数向量 $\mathbf w$ 的多层残差网络对损失 $L(\mathbf z(T))$ 的梯度表达式。令步长 $\epsilon\to0$，推导损失导数的公式(18.26)。

## 提示

> [!hint]- 提示 1
> 共享参数的各个使用位置贡献相加：每层贡献为 $\epsilon(\partial_w f)^Ta_{k+1}$。

> [!hint]- 提示 2
> 用极简单的 $z'=w$、固定 $z(0)$、$L=z(T)$ 检查积分前的正负号。

## 解答

> [!success]- 解答
> **独立推导，并修正源公式符号。** 使用列伴随 $a_k=\nabla_{z_k}L$，记 $B_k=\partial_w f(z_k,w)$（状态维数乘参数维数）。在固定初值 $z_0$ 下，各层共享参数的贡献必须求和：
> $$\nabla_w L=\sum_{k=0}^{N-1}\epsilon B_k^Ta_{k+1}.$$
> 这是(8.10)“上游梯度乘本地参数导数”的矩阵形式，残差恒等支路不含 $w$。令 $N\epsilon=T$，Riemann和趋于
> $$\boxed{\nabla_wL=\int_0^T[\partial_w f(z(t),w)]^Ta(t)\,\mathrm dt}.$$
> 行向量约定则为 $\mathrm dL/\mathrm dw=\int_0^Ta(t)^T\partial_w f\,\mathrm dt$。若数值上从 $T$ 向0积分，可写 $-\int_T^0(\partial_w f)^Ta\,\mathrm dt$。
>
> 正文(18.26)实际印成 $-\int_0^Ta^T\nabla_w f\,\mathrm dt$，在其前向ODE $z'=f$ 的约定下多了负号。检验 $z'=w$、$z(0)=0$、$L=z(T)$：精确梯度为 $T$，$a(t)=1$，正积分得 $T$，原式得 $-T$，故不能照其符号得出正确导数。
>
> 也可令状态灵敏度 $S=\partial z/\partial w$，满足 $S'=JS+B,S(0)=0$，用前题伴随有 $(a^TS)'=a^TB$，从0到T积分得到同一结果。若初值依赖参数，额外加入 $(\partial_wz_0)^Ta(0)$。

## 相关概念

- [[06 - 深度学习/概念/归一化流|归一化流]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]
- [[06 - 深度学习/概念/反向传播|反向传播]]
- [[06 - 深度学习/概念/自动微分|自动微分]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=572|印刷560／PDF572]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- 正文(18.26)的负号已明确展示、用解析反例核查后修正；不把反向积分的时间方向与固定0到T积分混淆。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
