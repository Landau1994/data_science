---
title: "习题 P227：正态变量不同分母比值的Cauchy律"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第4章习题4.28，印刷页160／PDF物理页191"
source_id: "DS011"
source_chapter: 4
source_exercise: "4.28"
source_stars: 0
source_refs: ["DS011 Exercise 4.28，印刷160／PDF物理191"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P227：正态变量不同分母比值的Cauchy律

## 题目

### 英文原题

> [!question] 英文原题
> **4.28** Let $X$ and $Y$ be independent standard normal random variables.
> (a) Show that $X/(X+Y)$ has a Cauchy distribution.
> (b) Find the distribution of $X/|Y|$.
> (c) Is the answer to part (b) surprising? Can you formulate a general theorem?

### 中文转述

> [!question] 中文转述
> **原题4.28。**
> 设 $X,Y$ 为独立的标准正态随机变量.
>
> (a)  证明 $X/(X+Y)$ 服从 Cauchy 分布.
>
> (b)  求 $X/|Y|$ 的分布.
>
> (c)  (b) 的答案是否出乎意料？你能提出一个一般定理吗？

## 提示

> [!hint]- 提示
> 先用正交和差得到独立正态比值，再利用对称性消除分母符号。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 先记录独立标准正态$A,B$的比值密度：变换$(R,B)=(A/B,B)$给$f_R(r)=\int_{\mathbb R}|b|e^{-(1+r^2)b^2/2}/(2\pi)db=1/[\pi(1+r^2)]$。
> (a) $A=(X-Y)/\sqrt2,B=(X+Y)/\sqrt2$独立标准正态，且$X/(X+Y)=1/2+A/(2B)$，故为位置$1/2$、尺度$1/2$的Cauchy；密度为$2/[\pi(1+4(z-1/2)^2)]$。不是标准Cauchy。
> (b) 给定$Y=y\ne0$，$X$的对称性使$X/|y|$与$X/y$同分布，积分后仍标准Cauchy。
> (c) 一般若$A$关于0对称，与$B$独立且$P(B=0)=0$，则$A/B$与$A/|B|$同分布：在$B>0$时相等，在$B<0$时条件分布只差一个负号，由对称性相同。此定理不要求$B$自身对称；若$A$与$B$依赖，则条件对称性未必成立。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=191|印刷第160页／PDF物理第191页]]；教材信息与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。原题无星号。
- `source_status: verified`仅指本题题干、公式及所列来源定位已核对，不表示全章正文独立复证。解答写成不等于个人已完成练习，学习状态保持`not-started`；未实测Obsidian界面渲染。
