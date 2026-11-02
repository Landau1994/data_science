---
title: "习题 PM005：带泄漏概率的Noisy-OR模型"
topic: probabilistic-models
topic_label: 概率模型与推断
difficulty: beginner
status: not-started
tags:
  - exercise
  - probabilistic-models
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop 深度学习（DS003）]]"
source_id: DS003
source_chapter: 11
source_exercise: "11.5"
source_stars: 1
source_refs:
  - "DS003 Exercise 11.5，印刷354/PDF370"
  - "DS003 图11.6及§11.1.4，印刷332/PDF348"
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 PM005：带泄漏概率的Noisy-OR模型

## 题目

### 英文原题

> [!question] 英文原题
> **11.5 (★)** For the model shown in Figure 11.6, we have seen that the number of parameters required to specify the conditional distribution $p(y\mid x_1,\ldots,x_M)$, where $x_i\in\{0,1\}$, could be reduced from $2^M$ to $M+1$ by making use of the logistic sigmoid representation (11.8). An alternative representation (Pearl, 1988) is given by
> $$
> p(y=1\mid x_1,\ldots,x_M)=1-(1-\mu_0)\prod_{i=1}^M(1-\mu_i)^{x_i}.\tag{11.49}
> $$
> where the parameters $\mu_i$ represent the probabilities $p(x_i=1)$ and $\mu_0$ is an additional parameter satisfying $0\leq\mu_0\leq1$. The conditional distribution (11.49) is known as the noisy-OR. Show that this can be interpreted as a ‘soft’ (probabilistic) form of the logical OR function (i.e., the function that gives $y=1$ whenever at least one of the $x_i=1$). Discuss the interpretation of $\mu_0$.
>
> ![[附件/习题图/DS003/原图-11.6.png]]

### 中文转述

> [!question] 中文转述
> 图11.6中，$x_i\in\{0,1\}$。用逻辑Sigmoid形式(11.8)可将$p(y\mid x_1,\ldots,x_M)$的参数数目从$2^M$减到$M+1$。另一表示为式(11.49)：
> $$
> p(y=1\mid x_1,\ldots,x_M)=1-(1-\mu_0)\prod_{i=1}^M(1-\mu_i)^{x_i}.
> $$
> 其中参数$\mu_i$表示$p(x_i=1)$，且另有$0\leq\mu_0\leq1$。这种条件分布称为带噪声或（noisy-OR）。证明它可解释为逻辑OR的“软”概率形式；逻辑OR在至少一个$x_i=1$时输出$y=1$。讨论$\mu_0$的含义。

## 提示

> [!hint]- 提示 1
> 把每个活跃输入看成一次独立触发机会，再计算所有机会均失败的概率。

## 解答

> [!success]- 解答
> **独立推导。**
>
> 给定输入$x$，引入相互独立的二值触发变量$Z_0,Z_1,\ldots,Z_M$，令$P(Z_i=1)=\mu_i$，并定义
> $$
> Y=Z_0\ \operatorname{OR}\ (x_1Z_1)\ \operatorname{OR}\cdots\operatorname{OR}\ (x_MZ_M).
> $$
> 因此$Y=0$当且仅当泄漏触发$Z_0$失败，而且每个活跃输入的触发都失败。于是
> $$
> P(Y=0\mid x)=(1-\mu_0)\prod_{i:x_i=1}(1-\mu_i),
> $$
> 取补集即得(11.49)。$x_i=0$的因子解释为$1$，包括$\mu_i=1$时的形式$0^0$。
>
> 当$\mu_0=0$且所有$\mu_i=1$时，所有输入为零给出$P(Y=1)=0$，任一输入为一给出$P(Y=1)=1$，恰为确定性OR。一般$\mu_i$是输入已激活时成功触发输出的概率，使OR关系变软；$\mu_0=P(Y=1\mid x_1=\cdots=x_M=0)$是未建模原因或自发激活带来的泄漏概率。
>
> 上述解释中的$\mu_i$是触发成功率，并不是输入的边缘概率$P(X_i=1)$。条件分布给定了输入，无法仅凭输入的边缘发生率推导各输入的触发能力；若额外令两者数值相等，那是另加的模型限制。

## 相关概念

- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题已核对 DS003 印刷354页／PDF物理370页；正文引用的实际核对范围见 `source_refs`。
- 保留原题把$\mu_i$称为$p(x_i=1)$的文字；独立解答区分输入发生率与给定输入时的触发成功率。
- 解答为独立推导；归档与个人学习状态分开，学习状态保持 `not-started`。
