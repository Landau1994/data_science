---
title: "习题 ST277：二项贝塔可信区间与Clopper和Pearson区间比较"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第9章习题9.29，印刷页369／PDF物理页400"
source_id: "DS011"
source_chapter: 9
source_exercise: "9.29"
source_stars: 0
source_refs: ["DS011 Exercise 9.29，印刷369／PDF物理400"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST277：二项贝塔可信区间与Clopper和Pearson区间比较

## 题目

### 英文原题

> [!question] 英文原题
> **9.29** If $X_1,\ldots,X_n$ are a sequence of $n$ Bernoulli($p$) trials,
> (a) Calculate a $1-\alpha$ credible set for $p$ using the conjugate beta($a,b$) prior.
> (b) Using the relationship between the beta and $F$ distributions, write the credible set in a form that is comparable to the form of the intervals in Exercise 9.21. Compare the intervals.

### 中文转述

> [!question] 中文转述
> **原题9.29。**
> 若$X_1,\ldots,X_n$是一系列$n$次$\operatorname{Bernoulli}(p)$试验，
>
> (a)  采用共轭$\operatorname{beta}(a,b)$先验，计算$p$的$1-\alpha$可信集.
>
> (b)  利用贝塔分布和$F$分布的关系，将可信集写成可与习题9.21的区间形式比较的形式. 比较这些区间.

## 提示

> [!hint]- 提示
> 更新Beta先验的两个形状参数为成功数加$a$、失败数加$b$；与Clopper–Pearson比较时逐端核对其Beta参数，而非只看分位水平。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> (a) $y=\sum x_i$时后验$\mathrm{Beta}(A,B)$，$A=a+y,B=b+n-y$。取等尾集$[B_{A,B;\alpha/2},B_{A,B;1-\alpha/2}]$，质量$1-\alpha$。
> (b) 贝塔与$F$关系给
> $$
> L=\frac1{1+(B/A)F_{2B,2A,\alpha/2}},\qquad
> U=\frac{(A/B)F_{2A,2B,\alpha/2}}{1+(A/B)F_{2A,2B,\alpha/2}}.
> $$
> Clopper–Pearson下端来自$\mathrm{Beta}(y,n-y+1)$，上端来自$\mathrm{Beta}(y+1,n-y)$，不是同一个后验；没有同一固定正规贝塔先验能同时逐样本给这两个端点。可形式地用先验$a=0,b=1$匹配下端、$a=1,b=0$匹配上端，但这两者都在正规先验边界且不是同一先验。可信区间保证后验质量，Clopper–Pearson保证逐参数至少标称的频率覆盖，二者不可互换。

## 相关概念

- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=400|印刷369／PDF物理400]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
