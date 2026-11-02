---
title: "习题 ML042：多状态朴素贝叶斯的线性softmax分数"
topic: statistical-learning
topic_label: 统计学习
difficulty: intermediate
status: not-started
tags:
  - exercise
  - statistical-learning
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop 深度学习（DS003）]]"
source_id: DS003
source_chapter: 5
source_exercise: "5.16"
source_stars: 2
source_refs: ["DS003 Exercise 5.16，印刷168/PDF187", "DS003 §5.3，softmax及式(5.45)–(5.46)，印刷152/PDF171", "DS003 §5.3.3，式(5.64)–(5.65)及多状态说明，印刷156/PDF175"]
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 ML042：多状态朴素贝叶斯的线性softmax分数

## 题目

### 英文原题

> [!question] 英文原题
> **5.16 (★★)** Consider a classification problem with $K$ classes for which the feature vector $\boldsymbol\phi$ has $M$ components each of which can take $L$ discrete states. Let the values of the components be represented by a 1-of-$L$ binary coding scheme. Further suppose that, conditioned on the class $C_k$, the $M$ components of $\boldsymbol\phi$ are independent, so that the class-conditional density factorizes with respect to the feature vector components. Show that the quantities $a_k$ given by (5.46), which appear in the argument to the softmax function describing the posterior class probabilities, are linear functions of the components of $\boldsymbol\phi$. Note that this represents an example of a naive Bayes model.

### 中文转述

> [!question] 中文转述
> **原题5.16。** 在一个 $K$ 类分类问题中，特征向量 $\boldsymbol\phi$ 有 $M$ 个分量，每个分量可取 $L$ 个离散状态，并以1-of-$L$二元编码表示。假设给定类别 $C_k$ 后，这 $M$ 个分量相互独立，因而类条件分布按分量分解。证明后验概率softmax函数中的式(5.46)分数 $a_k$ 是编码后特征分量的线性函数；这是一个朴素贝叶斯（naive Bayes）模型。

## 提示

> [!hint]- 提示 1
> 令 $z_{i\ell}$ 表示第 $i$ 个特征是否处于状态 $\ell$，并用 $\theta_{ki\ell}$ 表示相应的类条件概率。给定类别后的似然是所有被选择状态概率的乘积。

> [!hint]- 提示 2
> 取对数后，每个特征编码只以一次项出现；先验贡献偏置。有限对数系数需要所用概率严格为正。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 为区分原始离散特征与编码，令
> $$
> z_{i\ell}=\mathbf1_{\{\text{第 }i\text{ 个特征的状态为 }\ell\}},
> \qquad\sum_{\ell=1}^Lz_{i\ell}=1,
> $$
> 其中 $i=1,\ldots,M$、$\ell=1,\ldots,L$。把全部 $ML$ 个编码分量拼成向量 $z$。记 $\pi_k=P(C_k)$，$\theta_{ki\ell}=P(\text{第 }i\text{ 个特征为 }\ell\mid C_k)$，满足 $\sum_\ell\theta_{ki\ell}=1$。
>
> 先假设所有 $\pi_k>0$、$\theta_{ki\ell}>0$，保证对数有限。由给定类别后的独立性，
> $$
> p(z\mid C_k)=\prod_{i=1}^M\prod_{\ell=1}^L\theta_{ki\ell}^{z_{i\ell}}.
> $$
> 对式(5.46) $a_k(z)=\ln\{p(z\mid C_k)\pi_k\}$ 取对数展开，
> $$
> a_k(z)=\ln\pi_k+\sum_{i=1}^M\sum_{\ell=1}^Lz_{i\ell}\ln\theta_{ki\ell}
> =b_k+w_k^{\mathsf T}z,
> $$
> 其中 $b_k=\ln\pi_k$、$w_{k,i\ell}=\ln\theta_{ki\ell}$。所以分数是编码变量的仿射函数；加入常数特征 $z_0=1$ 后就是严格意义的线性函数。由贝叶斯公式，
> $$
> p(C_k\mid z)=\frac{e^{a_k(z)}}{\sum_je^{a_j(z)}}.
> $$
> 由于 $M\ge1$ 且第一组编码满足 $\sum_\ell z_{1\ell}=1$，还可以不增加常数特征，直接令第一组的全部权重同加 $\ln\pi_k$：
> $$
> w'_{k,1\ell}=\ln\theta_{k,1\ell}+\ln\pi_k,\qquad
> w'_{k,i\ell}=\ln\theta_{ki\ell}\quad(i>1),
> $$
> 便有 $a_k(z)=\sum_{i,\ell}w'_{k,i\ell}z_{i\ell}$。这在原编码约束下给出严格的线性表达。这里的线性是对1-of-$L$指示变量而言，不表示对任意给状态编号1至 $L$ 后的原始数值也一定线性。
>
> 也可消去每组的基准状态 $L$，写为
> $$
> a_k(z)=\underbrace{\ln\pi_k+\sum_i\ln\theta_{kiL}}_{\widetilde b_k}
> +\sum_{i=1}^M\sum_{\ell=1}^{L-1}z_{i\ell}\ln\frac{\theta_{ki\ell}}{\theta_{kiL}}.
> $$
> 这说明编码约束造成系数表示的冗余，不影响分数值或后验。
>
> **零概率边界。** 若某个状态在某类下概率为0，原始乘积仍有概率意义，但该状态出现时该类联合概率为0，分数应记为 $-\infty$；不能将它表示成处处有限系数的普通线性函数。若某类先验为0，同样得到零后验。可通过正参数趋近边界来理解，或直接在概率域计算；当一个特征组合在所有类别下都为零概率时，贝叶斯分母为0，该点的后验并没有由模型确定。概率等于1也可能迫使同组其他状态为0，需要相同的边界处理。

## 相关概念

- [[05 - 概率模型与推断/概念/生成模型|生成模型]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[06 - 深度学习/概念/激活函数|激活函数]]

## 备注

- 原题已核对 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=187|印刷168／PDF物理187]]；所引正文公式的实际位置见 `source_refs`。
- 先验先写成偏置，再利用1-of-L编码约束吸收入一个特征块，或以增广常数特征给出线性形式。内点概率、零概率和不可能特征组合分别处理。
- `source_status: verified` 仅指本题原文、引用公式与定位核对，不表示整章或整书理论全部核验。解答未使用配套答案册；个人学习状态保留 `not-started`。
