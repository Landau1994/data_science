---
title: "习题 P214：独立Poisson和给定总数后的二项分配"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第4章习题4.15，印刷页159／PDF物理页190"
source_id: "DS011"
source_chapter: 4
source_exercise: "4.15"
source_stars: 0
source_refs: ["DS011 Exercise 4.15，印刷159／PDF物理190"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P214：独立Poisson和给定总数后的二项分配

## 题目

### 英文原题

> [!question] 英文原题
> **4.15** Let $X\sim\operatorname{Poisson}(\theta)$, $Y\sim\operatorname{Poisson}(\lambda)$, independent. It was shown in Theorem 4.3.2 that the distribution of $X+Y$ is Poisson$(\theta+\lambda)$. Show that the distribution of $X\mid X+Y$ is binomial with success probability $\theta/(\theta+\lambda)$. What is the distribution of $Y\mid X+Y$?

### 中文转述

> [!question] 中文转述
> **原题4.15。**
> 设 $X\sim\operatorname{Poisson}(\theta)$，$Y\sim\operatorname{Poisson}(\lambda)$，且二者独立. 定理4.3.2 已证明 $X+Y\sim\operatorname{Poisson}(\theta+\lambda)$. 证明 $X\mid X+Y$ 的分布是成功概率为 $\theta/(\theta+\lambda)$ 的二项分布. $Y\mid X+Y$ 的分布是什么？

## 提示

> [!hint]- 提示
> 固定总数$s$，联合pmf除以总数的Poisson概率。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$\theta,\lambda>0$且$s\in\mathbb N_0$。对$0\le x\le s$，
> $$
> P(X=x\mid X+Y=s)=\frac{e^{-(\theta+\lambda)}\theta^x\lambda^{s-x}/[x!(s-x)!]}{e^{-(\theta+\lambda)}(\theta+\lambda)^s/s!}=\binom sx\left(\frac\theta{\theta+\lambda}\right)^x\left(\frac\lambda{\theta+\lambda}\right)^{s-x}.
> $$
> 因此$X\mid S=s\sim\operatorname{Bin}(s,\theta/(\theta+\lambda))$，$Y\mid S=s\sim\operatorname{Bin}(s,\lambda/(\theta+\lambda))$。给定总数后两变量的和固定，一般不独立。若仅一个参数为0且总参数正，结论用退化二项分布解释；两者都0时只有$s=0$有正概率，二项概率参数的比值不定义但$X=Y=0$确定。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=190|印刷第159页／PDF物理第190页]]；教材信息与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。原题无星号。
- `source_status: verified`仅指本题题干、公式及所列来源定位已核对，不表示全章正文独立复证。解答写成不等于个人已完成练习，学习状态保持`not-started`；未实测Obsidian界面渲染。
