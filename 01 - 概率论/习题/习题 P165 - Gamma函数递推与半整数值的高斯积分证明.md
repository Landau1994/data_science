---
title: "习题 P165：Gamma函数递推与半整数值的高斯积分证明"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第3章习题3.16，印刷页107／PDF物理页138"
source_id: "DS011"
source_chapter: 3
source_exercise: "3.16"
source_stars: 0
source_refs: ["DS011 Exercise 3.16，印刷107／PDF物理138", "DS011 Gamma函数定义及式(3.3.2)–(3.3.4)，印刷81／PDF物理112"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P165：Gamma函数递推与半整数值的高斯积分证明

## 题目

### 英文原题

> [!question] 英文原题
> **3.16** Verify these two identities regarding the gamma function that were given in the text.
>
> (a) $\Gamma(\alpha+1)=\alpha\Gamma(\alpha)$
>
> (b) $\Gamma(\frac12)=\sqrt\pi$

### 中文转述

> [!question] 中文转述
> **原题3.16。** 验证正文中给出的关于Gamma函数的以下两个恒等式.
>
> (a)  $\Gamma(\alpha+1)=\alpha\Gamma(\alpha)$.
>
> (b)  $\Gamma(1/2)=\sqrt\pi$.

## 提示

> [!hint]- 提示
> 递推用分部积分；半整数值换成高斯积分后平方转极坐标。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 使用定义$\Gamma(a)=\int_0^\infty t^{a-1}e^{-t}dt$，$a>0$。
>
> **(a)** 分部积分得到$\Gamma(a+1)=[-t^ae^{-t}]_0^\infty+a\int_0^\infty t^{a-1}e^{-t}dt=a\Gamma(a)$；两端边界项均为0。
>
> **(b)** 换元$t=u^2$给$\Gamma(1/2)=2\int_0^\infty e^{-u^2}du$。令$I=\int_{-\infty}^\infty e^{-u^2}du>0$，对非负积分用Tonelli及二维极坐标，
> $$
> I^2=\int_{\mathbb R^2}e^{-x^2-y^2}dxdy=\int_0^{2\pi}\int_0^\infty e^{-r^2}rdrd\theta=\pi.
> $$
> 故$I=\sqrt\pi$，所求相同。递推(a)的积分证明要求$a>0$，未把它无条件延伸到Gamma的极点。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=138|印刷第107页／PDF物理第138页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；所用正文实际核对位置列于`source_refs`。题内文献只保留原题引用，不表示已查阅原文献。`source_status: verified`只指本题及所列位置核对，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
