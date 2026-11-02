---
title: "习题 LA025：ReLU初始化的二阶矩与方差之别"
topic: linear-algebra-optimization
topic_label: 线性代数与优化
difficulty: intermediate
status: not-started
tags: [exercise, linear-algebra-optimization]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 7
source_exercise: "7.9"
source_stars: 2
source_refs: ["DS003 Exercise 7.9，印刷231／PDF物理248", "DS003 §7.2.4，式(7.19)–(7.23)，印刷217–218/PDF234–235"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 LA025：ReLU初始化的二阶矩与方差之别

## 题目

### 英文原题

> [!question] 英文原题
> **7.9 (★★)** Consider a layered network that computes the functions (7.19) and (7.20) in layer $l$. Suppose we initialize the weights using a Gaussian $\mathcal N(0,\epsilon^2)$, and suppose that the outputs $z_j^{(l-1)}$ of the units in layer $l-1$ have variance $\lambda^2$. By using the form of the ReLU activation function, show that the mean and variance of the outputs in layer $l$ are given by (7.21) and (7.22), respectively. Hence, show that if we want the units in layer $l$ also to have pre-activations with variance $\lambda^2$ then the value of $\epsilon$ should be given by (7.23).

### 中文转述

> [!question] 中文转述
> 分层网络的第 $l$ 层计算(7.19)和(7.20)。权重由 $\mathcal N(0,\epsilon^2)$ 初始化，前一层输出 $z_j^{(l-1)}$ 的方差为 $\lambda^2$。利用ReLU激活的形式，证明第 $l$ 层输出的均值和方差分别由(7.21)、(7.22)给出。再证明若希望第 $l$ 层预激活也具有方差 $\lambda^2$，则 $\epsilon$ 应取(7.23)的值。

## 提示

> [!hint]- 提示
> ReLU输出通常有正均值，不能把二阶矩当成方差。先固定前层输出求条件高斯分布，再计算截断高斯矩。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> **原式存在均值、方差与二阶矩的混用。** 核对正文后，所引公式为
> $$
> a_i^{(l)}=\sum_{j=1}^Mw_{ij}z_j^{(l-1)},\quad z_i^{(l)}=\max(0,a_i^{(l)}),\tag{7.19–7.20}
> $$
> $$
> \mathbb E[a_i^{(l)}]=0,\tag{7.21}\qquad
> \operatorname{var}[z_j^{(l)}]=\frac M2\epsilon^2\lambda^2,\tag{7.22}\qquad
> \epsilon=\sqrt{2/M}.\tag{7.23}
> $$
> 注意(7.21)实际是**预激活**均值，不是ReLU输出均值。
>
> 令 $Z=(Z_1,\ldots,Z_M)$ 为前层输出，权重 $W_j$ 独立且与 $Z$ 独立，无偏置，$W_j\sim\mathcal N(0,\epsilon^2)$。条件于 $Z$，有 $A=\sum_jW_jZ_j\sim\mathcal N(0,s_Z^2)$，其中 $s_Z^2=\epsilon^2\|Z\|^2$（$s_Z=0$ 时按退化分布理解）。高斯积分直接给出
> $$
> \mathbb E[\max(0,A)\mid Z]=\frac{s_Z}{\sqrt{2\pi}},\qquad
> \mathbb E[\max(0,A)^2\mid Z]=\frac{s_Z^2}{2}.
> $$
> 第一式来自 $\int_0^\infty a e^{-a^2/(2s^2)}da=s^2$，第二式来自偶对称性。因此对 $Z$ 再平均，得到精确关系
> $$
> \mathbb E A=0,\quad \operatorname{var}A=\epsilon^2\sum_j\mathbb E Z_j^2,
> $$
> $$
> \mathbb E Z_{\rm new}=\frac{\epsilon}{\sqrt{2\pi}}\mathbb E\|Z\|,\quad
> \mathbb E Z_{\rm new}^2=\frac{\epsilon^2}{2}\sum_j\mathbb E Z_j^2,
> $$
> $$
> \operatorname{var}Z_{\rm new}=\frac{\epsilon^2}{2}\sum_j\mathbb E Z_j^2
> -\frac{\epsilon^2}{2\pi}(\mathbb E\|Z\|)^2.
> $$
> 故仅知前层 $\operatorname{var}Z_j=\lambda^2$ 不够，还需其均值确定 $\mathbb E Z_j^2=\lambda^2+(\mathbb E Z_j)^2$。即使均值为0，(7.22)右侧也是输出**二阶矩**，还须减正的均值平方才是方差。
>
> 常用的正确He尺度解释是：把 $q=\mathbb E Z_j^2$ 作为共同二阶矩，则 $q_{\rm new}=M\epsilon^2q/2$，要求 $q_{\rm new}=q>0$ 正好得 $\epsilon^2=2/M$。在层宽与尺度一致的这一矩递推下，下一层预激活方差 $M\epsilon^2q_{\rm new}$ 也不再逐层变化。若前层输入的二阶矩恰为 $\lambda^2$，却要求当前层**预激活**方差直接等于 $\lambda^2$，应取 $\epsilon^2=1/M$，不是 $2/M$。
>
> 若额外近似 $A\sim\mathcal N(0,v)$（无随机条件方差混合），ReLU输出的矩为 $\mathbb E Z=\sqrt{v/(2\pi)}$、$\operatorname{var}Z=v(1/2-1/(2\pi))$，同样显示原式遗漏均值平方。以上精确条件矩及明确近似分别陈述，不以原题为由证明错误等式。

## 相关概念

- [[06 - 深度学习/概念/参数初始化|参数初始化]]
- [[06 - 深度学习/概念/激活函数|激活函数]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=248|印刷231／PDF物理248]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 原题与正文混用输出/预激活以及方差/二阶矩。英文任务忠实保留，解答说明不可由所给方差假设直接得到(7.22)，并给出He尺度的正确二阶矩推导。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
