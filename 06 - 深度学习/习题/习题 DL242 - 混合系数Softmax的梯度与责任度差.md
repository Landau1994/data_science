---
title: "习题 DL242：混合系数Softmax的梯度与责任度差"
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags: [exercise, deep-learning]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: DS003
source_chapter: 9
source_exercise: "9.12"
source_stars: 2
source_refs: ["DS003 Exercise 9.12，印刷283／PDF物理300", "DS003 §9.4.2，式(9.21)–(9.31)，印刷272–273/PDF289–290"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL242：混合系数Softmax的梯度与责任度差

## 题目

### 英文原题

> [!question] 英文原题
> **9.12 (★★)** Show that the derivatives of the mixing coefficients $\{\pi_k\}$ defined by (9.30) with respect to the auxiliary parameters $\{\eta_j\}$ are given by
> $$
> \frac{\partial\pi_k}{\partial\eta_j}=\delta_{jk}\pi_j-\pi_j\pi_k.\tag{9.63}
> $$
> Hence, by making use of the constraint $\sum_k\gamma_k(w_i)=1$ for all $i$, derive the result (9.31).

### 中文转述

> [!question] 中文转述
> 混合系数按(9.30)由辅助参数 $\eta_j$ 作softmax参数化。证明导数为(9.63)的 $\delta_{jk}\pi_j-\pi_j\pi_k$，再用每个权重处责任度和为1，推出(9.31)。

## 提示

> [!hint]- 提示
> 商法则求softmax导数，然后对 $-\ln\sum_k\pi_k\phi_k(w_i)$ 应用链式法则。

## 解答

> [!success]- 解答
> **证明范围：独立推导。**
> 所引软权重共享模型为
> $$
> \phi_j(w)=\mathcal N(w\mid\mu_j,\sigma_j^2)
> =\frac{e^{-(w-\mu_j)^2/(2\sigma_j^2)}}{\sqrt{2\pi\sigma_j^2}},\quad
> p_i=\sum_j\pi_j\phi_j(w_i),
> $$
> $$
> p(w)=\prod_ip_i,\quad \Omega(w)=-\sum_i\ln p_i,\quad
> \widetilde E=E(w)+\lambda\Omega(w),\quad
> \gamma_j(w_i)=\frac{\pi_j\phi_j(w_i)}{p_i}.\tag{9.21–9.24}
> $$
> 取有限参数、$\sigma_j^2>0$、$\pi_j\ge0$ 且 $\sum_j\pi_j=1$，则每个 $p_i>0$，全部对数及责任度有定义。
>
> 令 $Z=\sum_le^{\eta_l}$、$\pi_k=e^{\eta_k}/Z$。有限 $\eta$ 保证 $\pi_k>0$。由商法则
> $$
> \frac{\partial\pi_k}{\partial\eta_j}
> =\frac{\delta_{jk}e^{\eta_k}Z-e^{\eta_k}e^{\eta_j}}{Z^2}
> =\delta_{jk}\pi_k-\pi_k\pi_j
> =\delta_{jk}\pi_j-\pi_j\pi_k.\tag{9.63}
> $$
> 于是（数据项与 $\eta$ 无关）
> $$
> \frac{\partial\widetilde E}{\partial\eta_j}
> =-\lambda\sum_i\sum_k\frac{\phi_k(w_i)}{p_i}\frac{\partial\pi_k}{\partial\eta_j}
> =-\lambda\sum_i\sum_k\gamma_k(w_i)(\delta_{jk}-\pi_j)
> =\lambda\sum_i[\pi_j-\gamma_j(w_i)].\tag{9.31}
> $$
> 最后一步使用后验责任度和为1。所有 $\eta$ 同加常数不改变 $\pi$，故各分量梯度之和也为0；这核对了softmax参数冗余下的方向不变性。

## 相关概念

- [[06 - 深度学习/概念/激活函数|激活函数]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]

## 备注

- 原题已实际查看 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=300|印刷283／PDF物理300]]；所列依赖正文亦逐页核对，精确位置见 `source_refs`。
- 解答未使用配套答案册。`source_status: verified` 指本题原文与所列依赖的核对范围；独立推导不代表个人学习完成，状态保持 `not-started`。
