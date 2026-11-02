---
title: "习题 DL209：混合权重Softmax预激活的梯度"
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags: [exercise, deep-learning]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]"
source_id: DS003
source_chapter: 6
source_exercise: "6.18"
source_stars: 2
source_refs:
  - "DS003 Exercise 6.18，印刷207/PDF225"
  - "DS003 §6.5.2–6.5.3，式(6.38)–(6.45)，印刷200–202/PDF218–220"
  - "DS004 Solution 6.18，式(221)–(223)及链式求和，印刷68–69/PDF68–69"
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 DL209：混合权重Softmax预激活的梯度

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 6.18（★★）** Derive the result (6.45) for the derivative of the error function with respect to the network output pre-activations controlling the mixing coefficients in the mixture density network.

### 中文转述

> [!question] 中文转述
> **原题6.18（★★）。** 推导混合密度网络（mixture density network）的误差函数关于控制混合系数的输出预激活量（pre-activations）的导数式 (6.45)：
> $$
> \frac{\partial E_n}{\partial a_k^\pi}=\pi_k-\gamma_{nk}.\tag{6.45}
> $$
> 模型在输入 $\mathbf x_n$ 处使用
> $$
> \pi_k=\frac{e^{a_k^\pi}}{\sum_le^{a_l^\pi}},\qquad
> E_n=-\ln\sum_j\pi_j\mathcal N_{nj},\qquad
> \gamma_{nk}=\frac{\pi_k\mathcal N_{nk}}{\sum_j\pi_j\mathcal N_{nj}},
> $$
> 其中 $\mathcal N_{nk}$ 是第 $k$ 个高斯分量在目标 $\mathbf t_n$ 处的密度。

## 提示

> [!hint]- 提示 1
> 输出权重由Softmax耦合，因此对 $a_k^\pi$ 求导要对所有 $\pi_j$ 求链式贡献。

> [!hint]- 提示 2
> 先求 $\partial E_n/\partial\pi_j=-\mathcal N_{nj}/\sum_l\pi_l\mathcal N_{nl}$，再用责任度消去混合密度分母。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 固定输入 $\mathbf x_n$ 和目标 $\mathbf t_n\in\mathbb R^L$。按原书参数化，混合系数是Softmax，分量标准差 $\sigma_j=e^{a_j^\sigma}>0$，均值分量 $\mu_{jl}=a_{jl}^\mu$。对 $a_k^\pi$ 求偏导时，其他类型的输出预激活坐标保持固定，因此分量密度保持固定。
>
> 记
> $$
> \mathcal N_{nj}=(2\pi\sigma_j^2)^{-L/2}\exp\left(-\frac{\|\mathbf t_n-\boldsymbol\mu_j\|^2}{2\sigma_j^2}\right),
> \qquad S_n=\sum_j\pi_j\mathcal N_{nj}.
> $$
> 所有预激活有限时，$\pi_j>0$、$S_n>0$。由 $E_n=-\ln S_n$，
> $$
> \frac{\partial E_n}{\partial\pi_j}
> =-\frac{\mathcal N_{nj}}{S_n}
> =-\frac{\gamma_{nj}}{\pi_j}.
> $$
> 对Softmax直接使用商法则，得
> $$
> \frac{\partial\pi_j}{\partial a_k^\pi}=\pi_j(\delta_{jk}-\pi_k).
> $$
> 因此
> $$
> \begin{aligned}
> \frac{\partial E_n}{\partial a_k^\pi}
> &=\sum_{j=1}^K\frac{\partial E_n}{\partial\pi_j}\frac{\partial\pi_j}{\partial a_k^\pi}\\
> &=-\sum_j\gamma_{nj}(\delta_{jk}-\pi_k)\\
> &=-\gamma_{nk}+\pi_k\sum_j\gamma_{nj}\\
> &=\pi_k-\gamma_{nk}.
> \end{aligned}
> $$
> 最后一步由责任度定义的归一化 $\sum_j\gamma_{nj}=1$ 得到。这是“给定输入、尚未观察目标时的分量权重”与“观察目标后的分量责任度”之差。
>
> 对单样本的全部权重预激活求和，导数之和为零，与Softmax对共同平移不变的性质一致。网络内部参数通常同时影响权重、均值和尺度，因此对内部参数求梯度时还必须合并其他输出的链式贡献；本题计算的是输出预激活坐标上的偏导数。

## 相关概念

- [[06 - 深度学习/概念/激活函数|激活函数]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[06 - 深度学习/概念/反向传播|反向传播]]

## 备注

- 原题：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=225|印刷207／PDF225]]；模型、输出参数化及式 (6.45) 的原页为PDF218–220，均已实际查看。
- 已实际查看[[00 - 首页/教材归档/DS004 - Bishop 深度学习答案册|DS004]]印刷68–69／PDF68–69的6.18；独立推导保留了Softmax全部输出的耦合求和，没有把 $\pi_k$ 单独当作一个独立sigmoid。
- `source_status: verified` 仅指本题及所列引用范围已核对；独立解答不等于完成个人学习，状态保持 `not-started`。
