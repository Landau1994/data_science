---
title: 习题 P119：离散分布的CDF变换在随机序上偏大
topic: probability-theory
topic_label: 概率论
difficulty: advanced
status: not-started
tags:
- exercise
- probability-theory
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第2章习题2.10，印刷页63／PDF物理页94
source_id: DS011
source_chapter: 2
source_exercise: '2.10'
source_stars: 0
source_refs:
- DS011 Exercise 2.10，印刷63／PDF物理94
- DS011 Theorem 2.1.10，印刷43／PDF74
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 P119：离散分布的CDF变换在随机序上偏大

## 题目

### 英文原题

> [!question] 英文原题
> **2.10** In Theorem 2.1.10 the probability integral transform was proved, relating the uniform cdf to any continuous cdf. In this exercise we investigate the relationship between discrete random variables and uniform random variables. Let $X$ be a discrete random variable with cdf $F_X(x)$ and define the random variable $Y$ as $Y=F_X(X)$.
>
> (a) Prove that $Y$ is stochastically greater than a uniform$(0,1)$; that is, if $U\sim\operatorname{uniform}(0,1)$, then
> $$
> \begin{aligned}
> P(Y>y)&\ge P(U>y)=1-y,&\text{for all }y,\ 0<y<1,\\
> P(Y>y)&>P(U>y)=1-y,&\text{for some }y,\ 0<y<1.
> \end{aligned}
> $$
> (Recall that stochastically greater was defined in Exercise 1.49.)
>
> (b) Equivalently, show that the cdf of $Y$ satisfies $F_Y(y)\le y$ for all $0<y<1$ and $F_Y(y)<y$ for some $0<y<1$. (Hint: Let $x_0$ be a jump point of $F_X$, and define $y_0=F_X(x_0)$. Show that $P(Y\le y_0)=y_0$. Now establish the inequality by considering $y=y_0+\varepsilon$. Pictures of the cdfs will help.)

### 中文转述

> [!question] 中文转述
> **原题2.10。** 定理2.1.10证明了概率积分变换，把均匀累积分布函数与任意连续累积分布函数联系起来. 本题研究离散随机变量与均匀随机变量之间的关系. 设 $X$ 是累积分布函数为 $F_X(x)$ 的离散随机变量，定义 $Y=F_X(X)$.
>
> (a)  证明，$Y$ 在随机意义下大于 $\operatorname{uniform}(0,1)$；即若 $U\sim\operatorname{uniform}(0,1)$，则
>
> $$
> \begin{aligned}
> P(Y>y)&\ge P(U>y)=1-y,&&\text{对所有 }0<y<1,\\
> P(Y>y)&>P(U>y)=1-y,&&\text{对某个 }0<y<1.
> \end{aligned}
> $$
>
> （回顾，习题1.49定义了“在随机意义下大于”.）
>
> (b)  等价地，证明 $Y$ 的累积分布函数满足：对所有 $0<y<1$，$F_Y(y)\le y$，并且对某个 $0<y<1$，$F_Y(y)<y$. （提示：设 $x_0$ 为 $F_X$ 的一个跳跃点，定义 $y_0=F_X(x_0)$. 证明 $P(Y\le y_0)=y_0$. 然后考虑 $y=y_0+\varepsilon$，建立所需不等式. 画累积分布函数的图会有帮助.）

## 提示

> [!hint]- 提示
> 用补事件把两问联系起来。对严格不等式，取原CDF的某个跳跃区间内部，不要求跳点有“下一个”支持点。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(b) 先证明CDF比较。** 设正质量支持为可数集$S$，固定$0<y<1$并令$A_y=\{x\in S:F_X(x)\le y\}$。任意有限子集$B\subseteq A_y$若非空，其最大点$b$满足
> $$
> \sum_{x\in B}P(X=x)\le P(X\le b)=F_X(b)\le y.
> $$
> 将$A_y$按可数序列穷尽，非负级数的极限给出
> $$
> F_Y(y)=\sum_{x\in A_y}P(X=x)\le y.
> $$
> 取任一正质量点$x_0$，令$a=F_X(x_0-)$、$b=F_X(x_0)$，则$b>a$。对$a<y<b$，$\{F_X(X)\le y\}$与$\{X<x_0\}$只可能差零概率点，因此$F_Y(y)=a<y$。该区间内存在$0<y<1$，即使$X$退化为单点也成立。
>
> **(a)** 由$P(Y>y)=1-F_Y(y)$，上述非严格及严格比较恰好转成题目所要求的尾概率比较。
>
> 原提示的$P(Y\le F_X(x_0))=F_X(x_0)$成立：$X\le x_0$贡献该质量；$x>x_0$而CDF仍等于该值的部分没有新增质量。然而直接取$y_0+\varepsilon$未必落在合适范围，特别是顶端跳跃$y_0=1$时无可用的正$\varepsilon$。本解答改在跳跃区间内部取点，适用于任意离散支持，不依赖支持点彼此孤立。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=94|印刷第63页／PDF物理第94页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 原Hint照录，严格比较的完整证明不依赖原Hint对epsilon的未写限制。
- 已逐题查看原始页面，英文原题、全部分题与原附提示／引用照录；原题无星号。所列正文定位已经实读，题内补充、原文及独立推导分开。未查阅题内外部文献或答案册。
- 来源核对状态不表示个人学习完成；学习状态保持not-started。公式与链接检查不等于Obsidian实际渲染检查。
