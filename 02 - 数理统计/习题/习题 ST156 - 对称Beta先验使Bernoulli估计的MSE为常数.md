---
title: "习题 ST156：对称Beta先验使Bernoulli估计的MSE为常数"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.33，印刷页293／PDF物理页324"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.33"
source_stars: 0
source_refs: ["DS011 Exercise 7.33，印刷293／PDF物理324", "DS011 例7.2.14后验均值，印刷263／PDF物理294", "DS011 例7.3.5的MSE公式，印刷269／PDF物理300"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST156：对称Beta先验使Bernoulli估计的MSE为常数

## 题目

### 英文原题

> [!question] 英文原题
> **7.33** In Example 7.3.5, the MSE of the Bayes estimator, $\widehat p_B$, of a success probability was calculated (the estimator was derived in Example 7.2.14). Show that the choice $\alpha=\beta=\sqrt{n/4}$ yields a constant MSE for $\widehat p_B$.

### 中文转述

> [!question] 中文转述
> **原题7.33。** 例7.3.5计算了成功概率的Bayes估计量$\widehat p_B$的MSE（估计量在例7.2.14中导出）.说明取$\alpha=\beta=\sqrt{n/4}$，可使$\widehat p_B$的MSE为常数.

## 提示

> [!hint]- 提示
> 把偏差与方差相加，利用$(1-2p)^2=1-4p(1-p)$消去参数项。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 例中$S=\sum_iX_i\sim\operatorname{binomial}(n,p)$，Beta$(\alpha,\beta)$先验给$\widehat p_B=(S+\alpha)/(n+\alpha+\beta)$。令$\alpha=\beta=a>0$，方差为$np(1-p)/(n+2a)^2$，偏差为$a(1-2p)/(n+2a)$，所以
> $$
> \operatorname{MSE}_p(\widehat p_B)=\frac{np(1-p)+a^2(1-2p)^2}{(n+2a)^2}.
> $$
> 当$a=\sqrt{n/4}=\sqrt n/2$，利用$(1-2p)^2=1-4p(1-p)$，分子恰好等于$n/4$。因而
> $$
> \operatorname{MSE}_p(\widehat p_B)=\frac{n}{4(n+\sqrt n)^2}=\frac1{4(\sqrt n+1)^2},\qquad0\le p\le1,
> $$
> 与$p$无关，包括端点。这里常数风险的估计量仍有偏，常数风险并不声称它在每个$p$都优于$\bar X$。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=324|印刷第293页／PDF物理第324页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
