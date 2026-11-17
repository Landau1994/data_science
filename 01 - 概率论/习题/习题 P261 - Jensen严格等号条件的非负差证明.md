---
title: "习题 P261：Jensen严格等号条件的非负差证明"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第4章习题4.62，印刷页166／PDF物理页197"
source_id: "DS011"
source_chapter: 4
source_exercise: "4.62"
source_stars: 0
source_refs: ["DS011 Exercise 4.62，印刷166／PDF物理197", "DS011 所引正文，印刷155／PDF物理186", "DS011 所引正文，印刷156／PDF物理187"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P261：Jensen严格等号条件的非负差证明

## 题目

### 英文原题

> [!question] 英文原题
> **4.62** Finish the proof of the equality in Jensen’s Inequality (Theorem 4.7.7). Let $g(x)$ be a convex function. Suppose $a+bx$ is a line tangent to $g(x)$ at $x=EX$, and $g(x)>a+bx$ except at $x=EX$. Then $Eg(X)>g(EX)$ unless $P(X=EX)=1$.

### 中文转述

> [!question] 中文转述
> **原题4.62。**
> 完成 Jensen 不等式（定理4.7.7）中等号情形的证明. 设 $g$ 为凸函数，$a+bx$ 是它在 $x=EX$ 处的切线，且除 $x=EX$ 外都有 $g(x)>a+bx$. 则除非 $P(X=EX)=1$，否则 $Eg(X)>g(EX)$.

## 提示

> [!hint]- 提示
> 凸函数与支撑直线的差非负，且只在均值处为0。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$E|X|<\infty$、$\mu=EX$，切线$\ell(x)=a+bx$满足$\ell(\mu)=g(\mu)$且题设给$D(x)=g(x)-\ell(x)\ge0$，仅在$x=\mu$为0。于是$Eg(X)=E\ell(X)+ED(X)=g(\mu)+ED(X)$，允许右侧为$+\infty$。若$P(X\ne\mu)>0$，则$P(D(X)>0)>0$；由$\{D>0\}=\bigcup_{n\ge1}\{D\ge1/n\}$，至少一项概率正，故$ED\ge P(D\ge1/n)/n>0$。所以严格大于。若$P(X=\mu)=1$，差恒0，等号成立。论证不要求$g$处处可微，只需题设在均值处确有该支撑直线。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=197|印刷第166页／PDF物理第197页]]；教材信息与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。原题无星号。
- 题内引用正文已核对：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=186|印刷155／PDF186]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=187|印刷156／PDF187]]。所需条件在解答重述，原文输入与独立补充分开。
- `source_status: verified`仅指本题题干、公式及所列来源定位已核对，不表示全章正文独立复证。解答写成不等于个人已完成练习，学习状态保持`not-started`；未实测Obsidian界面渲染。
