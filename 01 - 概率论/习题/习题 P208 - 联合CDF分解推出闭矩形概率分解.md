---
title: "习题 P208：联合CDF分解推出闭矩形概率分解"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第4章习题4.9，印刷页158／PDF物理页189"
source_id: "DS011"
source_chapter: 4
source_exercise: "4.9"
source_stars: 0
source_refs: ["DS011 Exercise 4.9，印刷158／PDF物理189"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P208：联合CDF分解推出闭矩形概率分解

## 题目

### 英文原题

> [!question] 英文原题
> **4.9** Prove that if the joint cdf of $X$ and $Y$ satisfies
> $$
> F_{X,Y}(x,y)=F_X(x)F_Y(y),
> $$
> then for any pair of intervals $(a,b)$, and $(c,d)$,
> $$
> P(a\le X\le b,c\le Y\le d)=P(a\le X\le b)P(c\le Y\le d).
> $$

### 中文转述

> [!question] 中文转述
> **原题4.9。**
> 证明：若 $X,Y$ 的联合 cdf 满足 $F_{X,Y}(x,y)=F_X(x)F_Y(y)$，则对任意一对区间 $(a,b)$、$(c,d)$，
>
> $$
> P(a\le X\le b,c\le Y\le d)=P(a\le X\le b)P(c\le Y\le d).
> $$

## 提示

> [!hint]- 提示
> 闭区间左端可能有原子，必须用左极限而不是直接减$F(a)$。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$a\le b,c\le d$，记$F_X(a-)=P(X<a)$，类似定义$F_Y(c-)$。通过从下趋近$a,c$取极限，联合CDF乘积分解仍给$F(a-,d)=F_X(a-)F_Y(d)$等。矩形的四项容斥于是为
> $$
> \begin{aligned}P(a\le X\le b,c\le Y\le d)&=F(b,d)-F(a-,d)-F(b,c-)+F(a-,c-)\\&=[F_X(b)-F_X(a-)][F_Y(d)-F_Y(c-)].\end{aligned}
> $$
> 两因子就是题目右侧的两个闭区间概率。此证明适用于有原子的分布；原文先称区间$(a,b),(c,d)$而所列事件实际为闭区间，英文两处均保留。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=189|印刷第158页／PDF物理第189页]]；教材信息与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。原题无星号。
- `source_status: verified`仅指本题题干、公式及所列来源定位已核对，不表示全章正文独立复证。解答写成不等于个人已完成练习，学习状态保持`not-started`；未实测Obsidian界面渲染。
