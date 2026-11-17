---
title: "习题 ST184：缩放卡方方差似然与Stein损失的精确关系"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.61，印刷页296／PDF物理页327"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.61"
source_stars: 0
source_refs: ["DS011 Exercise 7.61，印刷296／PDF物理327", "DS011 例7.3.27的Stein损失，印刷284／PDF物理315"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST184：缩放卡方方差似然与Stein损失的精确关系

## 题目

### 英文原题

> [!question] 英文原题
> **7.61** Show that the log of the likelihood function for estimating $\sigma^2$, based on observing $S^2\sim\sigma^2\chi_\nu^2/\nu$, can be written in the form
> $$
> \log L(\sigma^2\mid s^2)=K_1\frac{s^2}{\sigma^2}-K_2\log\frac{s^2}{\sigma^2}+K_3,
> $$
> where $K_1,K_2$, and $K_3$ are constants, not dependent on $\sigma^2$. Relate the above log likelihood to the loss function discussed in Example 7.3.27. See Anderson (1984a) for a discussion of this relationship.

### 中文转述

> [!question] 中文转述
> **原题7.61。** 说明基于观测$S^2\sim\sigma^2\chi_\nu^2/\nu$估计$\sigma^2$时，似然函数的对数可写为
>
> $$
> \log L(\sigma^2\mid s^2)=K_1\frac{s^2}{\sigma^2}-K_2\log\frac{s^2}{\sigma^2}+K_3,
> $$
>
> 其中$K_1,K_2,K_3$是不依赖于$\sigma^2$的常数.将上述对数似然与例7.3.27讨论的损失函数联系起来.Anderson（1984a）讨论了这种关系.

## 提示

> [!hint]- 提示
> 把方差参数改写成比值$r=s^2/\sigma^2$，再和$r-1-\log r$比较。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$\nu>0,q=\sigma^2>0,s^2>0$。缩放卡方密度为
> $$
> f(s^2\mid q)=\frac{(\nu/(2q))^{\nu/2}}{\Gamma(\nu/2)}(s^2)^{\nu/2-1}e^{-\nu s^2/(2q)}.
> $$
> 令$r=s^2/q$，用$\log q=\log s^2-\log r$整理，
> $$
> \ell(q)=-\frac\nu2 r+\frac\nu2\log r+
> \frac\nu2\log(\nu/2)-\log\Gamma(\nu/2)-\log s^2.
> $$
> 因此可取$K_1=-\nu/2,K_2=-\nu/2$，$K_3=(\nu/2)\log(\nu/2)-\log\Gamma(\nu/2)-\log s^2$。这里“常数”只是不随待估参数$q$变化，允许依赖已观测$s^2$。
>
> 例7.3.27的Stein损失为$L(q,a)=a/q-1-\log(a/q)$，所以
> $$
> \ell(q)=-\frac\nu2L(q,s^2)+K_3-\frac\nu2.
> $$
> 即固定数据时，负对数似然与把行动取为观察值$s^2$的Stein损失只差正比例和参数无关常数。$r-1-\log r\ge0$、仅$r=1$取零，故其最小点/似然最大点为$q=s^2$。这不把一般的随机估计量风险与单次似然混为同一个函数。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=327|印刷第296页／PDF物理第327页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
