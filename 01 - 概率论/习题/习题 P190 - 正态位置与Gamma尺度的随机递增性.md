---
title: "习题 P190：正态位置与Gamma尺度的随机递增性"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第3章习题3.41，印刷页110／PDF物理页141"
source_id: "DS011"
source_chapter: 3
source_exercise: "3.41"
source_stars: 0
source_refs: ["DS011 Exercise 3.41，印刷110／PDF物理141", "DS011 Gamma尺度参数式(3.3.6)，印刷81／PDF物理112"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P190：正态位置与Gamma尺度的随机递增性

## 题目

### 英文原题

> [!question] 英文原题
> **3.41** A family of cdfs $\{F(x\mid\theta),\theta\in\Theta\}$ is stochastically increasing in $\theta$ if $\theta_1>\theta_2\Rightarrow F(x\mid\theta_1)$ is stochastically greater than $F(x\mid\theta_2)$. (See Exercise 1.49 for the definition of stochastically greater.)
>
> (a) Show that the $\mathrm n(\mu,\sigma^2)$ family is stochastically increasing in $\mu$ for fixed $\sigma^2$.
>
> (b) Show that the gamma$(\alpha,\beta)$ family of (3.3.6) is stochastically increasing in $\beta$ (scale parameter) for fixed $\alpha$ (shape parameter).

### 中文转述

> [!question] 中文转述
> **原题3.41。** 若$\theta_1>\theta_2$蕴含$F(x\mid\theta_1)$在随机意义下大于$F(x\mid\theta_2)$，则称cdf族$\{F(x\mid\theta),\theta\in\Theta\}$关于$\theta$随机递增（stochastically increasing）. （随机大于的定义见习题1.49.）
>
> (a)  证明，固定$\sigma^2$时，$\operatorname n(\mu,\sigma^2)$族关于$\mu$随机递增.
>
> (b)  证明，固定形状参数$\alpha$时，式3.3.6的Gamma$(\alpha,\beta)$族关于尺度参数$\beta$随机递增.

## 提示

> [!hint]- 提示
> 随机较大的变量有更小的CDF；尺度放大只对非负支持有固定方向。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 随机较大表示CDF逐点不大于另一CDF，并至少一点严格；不是CDF数值较大。
>
> **(a)** 固定$\sigma>0$，$F(x|\mu)=\Phi((x-\mu)/\sigma)$。若$\mu_1>\mu_2$，则每个有限$x$的标准化值严格更小；标准正态密度处处正，所以$\Phi$严格递增，$F(x|\mu_1)<F(x|\mu_2)$。
>
> **(b)** 固定$\alpha>0$，令$Z\sim\operatorname{Gamma}(\alpha,1)$，$X_\beta=\beta Z$。则$F(x|\beta)=G_\alpha(x/\beta)$。对$x\le0$均为0；对$x>0$及$\beta_1>\beta_2$，$x/\beta_1<x/\beta_2$，且Gamma密度在正半轴严格正，故CDF严格更小。题目要求的弱比较和至少一点严格均成立。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=141|印刷第110页／PDF物理第141页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；所用正文实际核对位置列于`source_refs`。题内文献只保留原题引用，不表示已查阅原文献。`source_status: verified`只指本题及所列位置核对，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
