---
title: "习题 ST411：两组二项数据的准分离与无有限LogisticMLE"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.16，印刷页490／PDF物理页521"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.16"
source_stars: 0
source_refs: ["DS011 Exercise 12.16，印刷页490／PDF物理页521", "DS011 所引正文，印刷479／PDF物理510", "DS011 所引正文，印刷481／PDF物理512"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST411：两组二项数据的准分离与无有限LogisticMLE

## 题目

### 英文原题

> [!question] 英文原题
> **12.16** Consider this logistic regression data. Only two values, $x=0$ and 1, are observed. For $x=0$ there are ten successes in ten trials. For $x=1$ there are five successes in ten trials. Show that the logistic regression MLEs $\hat\alpha$ and $\hat\beta$ do not exist for these data by verifying the following.
> (a) The MLEs for $\pi(0)$ and $\pi(1)$, not restricted by (12.3.2), are given by $\hat\pi(0)=1$ and $\hat\pi(1)=.5$.
> (b) The overall maximum of the likelihood function given by the estimates in part (a) cannot be achieved at any finite values of the logistic regression parameters $\alpha$ and $\beta$, but can be achieved in the limit as $\beta\to-\infty$ and $\alpha=-\beta$.

### 中文转述

> [!question] 中文转述
> **原题12.16。**
> 考虑以下逻辑回归数据，只观测两个取值$x=0,1$. 在$x=0$处，十次试验有十次成功；在$x=1$处，十次试验有五次成功. 验证以下结论，证明这些数据的逻辑回归MLE $\hat\alpha,\hat\beta$不存在.
>
> (a)  不受式12.3.2限制时，$\pi(0),\pi(1)$的MLE为$\hat\pi(0)=1$、$\hat\pi(1)=.5$.
>
> (b)  (a)的估计所给似然函数整体最大值，不能在逻辑回归参数$\alpha,\beta$的任何有限值处取得，但可在$\beta\to-\infty$、$\alpha=-\beta$的极限中达到.

## 提示

> [!hint]- 提示
> 二项比例可以落边界，有限Logit只能产生严格内部概率。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** (a) 令$p_0=\pi(0),p_1=\pi(1)$，忽略与参数无关的组合因子，$L=p_0^{10}p_1^5(1-p_1)^5$。第一因子在$[0,1]$最大于1，第二对数导数$5/p_1-5/(1-p_1)$唯一零点$.5$且严格凹，故最大点$(1,.5)$。
> (b) Logistic约束给$p_0=\Lambda(\alpha)$、$p_1=\Lambda(\alpha+\beta)$。任意有限$\alpha$都使$p_0<1$，因此不能达到(a)的上界，即不存在有限MLE。取$\beta=-t,\alpha=t,t\to\infty$，有$p_0\to1,p_1=\Lambda(0)=.5$，似然逼近同一个sup。因此是上确界存在而最大点不取得；把无穷参数称普通MLE会掩盖边界问题。若保留分组二项常数，sup为$\binom{10}5 2^{-10}$，若逐试验记录则是$2^{-10}$，两者不影响估计结论。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=521|印刷490／PDF物理521]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=510|印刷479／PDF物理510]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=512|印刷481／PDF物理512]]；所需模型、公式、数据在解答重述。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
