---
title: "习题 P250：均匀变量的比值乘积及乘积除比的CDF"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第4章习题4.51，印刷页164／PDF物理页195"
source_id: "DS011"
source_chapter: 4
source_exercise: "4.51"
source_stars: 0
source_refs: ["DS011 Exercise 4.51，印刷164／PDF物理195"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P250：均匀变量的比值乘积及乘积除比的CDF

## 题目

### 英文原题

> [!question] 英文原题
> **4.51** Let $X,Y,$ and $Z$ be independent uniform$(0,1)$ random variables.
> (a) Find $P(X/Y\le t)$ and $P(XY\le t)$. (Pictures will help.)
> (b) Find $P(XY/Z\le t)$.

### 中文转述

> [!question] 中文转述
> **原题4.51。**
> 设 $X,Y,Z$ 为独立的 $\operatorname{uniform}(0,1)$ 随机变量.
>
> (a)  求 $P(X/Y\le t)$ 和 $P(XY\le t)$. 画图会有帮助.
>
> (b)  求 $P(XY/Z\le t)$.

## 提示

> [!hint]- 提示
> (a)在单位正方形积分；(b)再对$Z$条件化。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** (a) 对$t\le0$两个CDF都为0。对比值，固定$Y=y$后可用长度为$\min(ty,1)$的$X$区间，故
> $$
> P(X/Y\le t)=\begin{cases}0,&t\le0,\\t/2,&0<t\le1,\\1-1/(2t),&t>1.\end{cases}
> $$
> 当$t>1$，计算是$\int_0^{1/t}tydy+\int_{1/t}^1dy$。对乘积，$0<t<1$时分$y<t$与$y\ge t$，得$t+\int_t^1(t/y)dy=t(1-\log t)$；$t\ge1$为1。
> (b) 令$F_U$为$U=XY$的上述CDF，由独立性$P(U/Z\le t)=\int_0^1F_U(tz)dz$。$0<t\le1$时积分$tz[1-\log(tz)]$，利用$\int_0^1z dz=1/2,\int_0^1z\log z dz=-1/4$，得$t(3/4-\tfrac12\log t)$。$t>1$时在$z=1/t$处分开，得$(1/t)\int_0^1u(1-\log u)du+1-1/t=1-1/(4t)$。完整CDF为
> $$
> P(XY/Z\le t)=\begin{cases}0,&t\le0,\\t(3/4-\tfrac12\log t),&0<t\le1,\\1-1/(4t),&t>1.\end{cases}
> $$
> 在$t=1$两式均为$3/4$，在0右极限为0。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=195|印刷第164页／PDF物理第195页]]；教材信息与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。原题无星号。
- `source_status: verified`仅指本题题干、公式及所列来源定位已核对，不表示全章正文独立复证。解答写成不等于个人已完成练习，学习状态保持`not-started`；未实测Obsidian界面渲染。
