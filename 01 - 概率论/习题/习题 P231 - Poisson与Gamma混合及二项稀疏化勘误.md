---
title: "习题 P231：Poisson与Gamma混合及二项稀疏化勘误"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第4章习题4.32，印刷页160／PDF物理页191"
source_id: "DS011"
source_chapter: 4
source_exercise: "4.32"
source_stars: 0
source_refs: ["DS011 Exercise 4.32，印刷160／PDF物理191", "DS011 所引正文，印刷78／PDF物理109", "DS011 所引正文，印刷83／PDF物理114"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P231：Poisson与Gamma混合及二项稀疏化勘误

## 题目

### 英文原题

> [!question] 英文原题
> **4.32** (a) For the hierarchical model
> $$
> Y\mid\Lambda\sim\operatorname{Poisson}(\Lambda)\quad\text{and}\quad\Lambda\sim\operatorname{gamma}(\alpha,\beta),
> $$
> find the marginal distribution, mean and variance of $Y$. Show that the marginal distribution of $Y$ is negative binomial if $\alpha$ is an integer.
> (b) Show that the three-stage model
> $$
> Y\mid N\sim\operatorname{binomial}(N,p),\quad N\mid\Lambda\sim\operatorname{Poisson}(\Lambda),\quad\text{and}\quad\Lambda\sim\operatorname{gamma}(\alpha,\beta),
> $$
> leads to the same marginal (unconditional) distribution of $Y$.

### 中文转述

> [!question] 中文转述
> **原题4.32。**
> (a)  对分层模型 $Y\mid\Lambda\sim\operatorname{Poisson}(\Lambda)$，$\Lambda\sim\operatorname{gamma}(\alpha,\beta)$，求 $Y$ 的边缘分布、均值和方差. 证明当 $\alpha$ 为整数时，$Y$ 的边缘分布为负二项分布.
>
> (b)  证明三层模型
>
> $$
> Y\mid N\sim\operatorname{binomial}(N,p),\quad N\mid\Lambda\sim\operatorname{Poisson}(\Lambda),\quad\Lambda\sim\operatorname{gamma}(\alpha,\beta)
> $$
>
> 得到 $Y$ 的同一边缘（无条件）分布.

## 提示

> [!hint]- 提示
> Gamma的第二参数是尺度；稀疏化把Poisson均值乘$p$。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** (a) 对$y\in\mathbb N_0$，将两个密度相乘积分给
> $$
> P(Y=y)=\frac{\Gamma(\alpha+y)}{\Gamma(\alpha)y!}\frac{\beta^y}{(1+\beta)^{\alpha+y}}.
> $$
> 积分来自$\int_0^\infty\lambda^{\alpha+y-1}e^{-(1+1/\beta)\lambda}d\lambda=\Gamma(\alpha+y)/(1+1/\beta)^{\alpha+y}$。由全期望和全方差，$EY=\alpha\beta$，$\operatorname{Var}Y=\alpha\beta+\alpha\beta^2$。这是成功数参数$\alpha$、成功概率$1/(1+\beta)$的“失败次数”负二项分布；$\alpha$为正整数时可解释为第$\alpha$次成功前的失败数，本书默认采用该失败次数版本（式3.2.10）；若另采用式3.2.9的总试验次数版本则须加$\alpha$。
> (b) 给定$\Lambda=\lambda$，pgf为$E[s^Y\mid\lambda]=E[(1-p+ps)^N\mid\lambda]=e^{p\lambda(s-1)}$，故$Y\mid\lambda\sim\operatorname{Poisson}(p\lambda)$。于是边缘是(a)中把尺度$\beta$改为$p\beta$的同族分布：$P(Y=y)=\Gamma(\alpha+y)(p\beta)^y/[\Gamma(\alpha)y!(1+p\beta)^{\alpha+y}]$，均值$\alpha p\beta$、方差$\alpha p\beta+\alpha p^2\beta^2$。因此原题“same”若指完全相同参数的分布是不成立的，除$p=1$外均值就不同；若指同一个负二项族则成立。$p=0$时退化于0。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=191|印刷第160页／PDF物理第191页]]；教材信息与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。原题无星号。
- 题内引用正文已核对：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=109|印刷78／PDF109]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=114|印刷83／PDF114]]。所需条件在解答重述，原文输入与独立补充分开。
- 明确区分同分布族与同参数分布，并区分失败次数与总试验次数版本。
- `source_status: verified`仅指本题题干、公式及所列来源定位已核对，不表示全章正文独立复证。解答写成不等于个人已完成练习，学习状态保持`not-started`；未实测Obsidian界面渲染。
