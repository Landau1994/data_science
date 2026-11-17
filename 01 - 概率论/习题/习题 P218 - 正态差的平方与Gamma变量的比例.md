---
title: "习题 P218：正态差的平方与Gamma变量的比例"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第4章习题4.19，印刷页159／PDF物理页190"
source_id: "DS011"
source_chapter: 4
source_exercise: "4.19"
source_stars: 0
source_refs: ["DS011 Exercise 4.19，印刷159／PDF物理190"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P218：正态差的平方与Gamma变量的比例

## 题目

### 英文原题

> [!question] 英文原题
> **4.19** (a) Let $X_1$ and $X_2$ be independent n$(0,1)$ random variables. Find the pdf of $(X_1-X_2)^2/2$.
> (b) If $X_i$, $i=1,2$, are independent gamma$(\alpha_i,1)$ random variables, find the marginal distributions of $X_1/(X_1+X_2)$ and $X_2/(X_1+X_2)$.

### 中文转述

> [!question] 中文转述
> **原题4.19。**
> (a)  设 $X_1,X_2$ 为独立的 $n(0,1)$ 随机变量. 求 $(X_1-X_2)^2/2$ 的 pdf.
>
> (b)  若 $X_i$，$i=1,2$，为独立的 $\operatorname{gamma}(\alpha_i,1)$ 随机变量，求 $X_1/(X_1+X_2)$ 和 $X_2/(X_1+X_2)$ 的边缘分布.

## 提示

> [!hint]- 提示
> (a)先标准化正态差；(b)取总和与比例。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** (a) $W=(X_1-X_2)/\sqrt2\sim N(0,1)$（mgf相乘得$e^{t^2/2}$），故$W^2$密度为$e^{-z/2}/\sqrt{2\pi z}$，$z>0$，即$\chi_1^2$。
> (b) 设$s=X_1+X_2,u=X_1/s$，反变换$x_1=su,x_2=s(1-u)$，Jacobian为$s$。联合密度为
> $$
> \frac{s^{\alpha_1+\alpha_2-1}e^{-s}}{\Gamma(\alpha_1)\Gamma(\alpha_2)}u^{\alpha_1-1}(1-u)^{\alpha_2-1},\quad s>0,0<u<1.
> $$
> 对$s$积分得$U\sim\operatorname{Beta}(\alpha_1,\alpha_2)$；$1-U$则为$\operatorname{Beta}(\alpha_2,\alpha_1)$。二者相加为1，虽各有Beta边缘却不独立。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=190|印刷第159页／PDF物理第190页]]；教材信息与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。原题无星号。
- `source_status: verified`仅指本题题干、公式及所列来源定位已核对，不表示全章正文独立复证。解答写成不等于个人已完成练习，学习状态保持`not-started`；未实测Obsidian界面渲染。
