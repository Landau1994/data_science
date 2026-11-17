---
title: 习题 ST316：伯努利方差MLE的精确方差与二阶退化
topic: mathematical-statistics
topic_label: 数理统计
difficulty: intermediate
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.10，印刷页409／PDF物理页440
source_id: DS011
source_chapter: 10
source_exercise: '10.10'
source_stars: 0
source_refs:
- DS011 Exercise 10.10，印刷409／PDF物理440
- DS011题内依赖核对：印刷383／PDF物理414；印刷198／PDF物理229
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST316：伯努利方差MLE的精确方差与二阶退化

## 题目

### 英文原题

> [!question] 英文原题
> **10.10** Continue the calculations of Example 10.1.14, where the properties of the estimator of $p(1-p)$ we looked at.
>
> (a) Show that, if $p\ne1/2$, the MLE $\hat p(1-\hat p)$ is asymptotically efficient.
>
> (b) If $p=1/2$, use Theorem 5.5.26 to find a limiting distribution of $\hat p(1-\hat p)$.
>
> (c) Calculate the exact expression for $\operatorname{Var}[\hat p(1-\hat p)]$. Is the reason for the failure of the approximations any clearer?

### 中文转述

> [!question] 中文转述
> **原题10.10。** 继续例10.1.14的计算，那里考察了$p(1-p)$估计量的性质.
>
> (a)  证明若$p\ne1/2$，MLE $\hat p(1-\hat p)$渐近有效.
>
> (b)  若$p=1/2$，用定理5.5.26求$\hat p(1-\hat p)$的极限分布.
>
> (c)  计算$\operatorname{Var}[\hat p(1-\hat p)]$的精确表达式. 近似失效的原因是否更清楚了？

## 提示

> [!hint]- 提示
> 记q=p(1−p)。一阶项系数1−2p在1/2处消失，剩余方差是n^(−2)阶。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$K\sim\operatorname{Bin}(n,p),\hat p=K/n$、$H=\hat p(1-\hat p)$、$q=p(1-p)$。
>
> **(a)** 对$0<p<1,p\ne1/2$，CLT与Delta方法给$\sqrt n(H-q)\Rightarrow N(0,(1-2p)^2q)$。每观测信息$I(p)=1/q$，目标导数$1-2p$，故达到下界$[g'(p)]^2/I(p)=(1-2p)^2q$，渐近有效。
>
> **(b)** $p=1/2$时$H-1/4=-(\hat p-1/2)^2$，因此$n(H-1/4)\Rightarrow-\chi_1^2/4$。未标准化$H\to_p1/4$；$\sqrt n$尺度仅给退化0，非退化极限必须使用$n$。
>
> **(c)** $E H=(n-1)q/n$。利用$K$的阶乘矩$E(K)_r=(n)_rp^r$展开$H^2=(K/n-K^2/n^2)^2$，或将$H=(n-1)S^2/n$代入Bernoulli中心矩$\theta_2=q,\theta_4=q(1-3q)$的样本方差公式，均得
> $$
> \operatorname{Var}H=\frac{(n-1)^2}{n^3}q(1-4q)+\frac{2(n-1)}{n^3}q^2.
> $$
> 第一项是常规$n^{-1}$阶，第二项为$n^{-2}$阶。$p=1/2$时第一项为0，精确方差为$(n-1)/(8n^3)$，二阶近似$1/(8n^2)$接近，而一阶公式错误给0。接近1/2时第二项不能忽略，解释近似失效。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=440|印刷第409页／PDF物理第440页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 原题引例10.1.14，直接讨论该统计量的是例10.1.15；原引用保留，解答独立建立模型与矩，不依赖错误编号。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=414|印刷383／PDF物理414]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=229|印刷198／PDF物理229]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
