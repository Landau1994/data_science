---
title: "习题 ST415：零斜率二项LogitMLE及全同结果的LRT上确界"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.20，印刷页491／PDF物理页522"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.20"
source_stars: 0
source_refs: ["DS011 Exercise 12.20，印刷页491／PDF物理页522", "DS011 所引正文，印刷479／PDF物理510", "DS011 所引正文，印刷483／PDF物理514"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST415：零斜率二项LogitMLE及全同结果的LRT上确界

## 题目

### 英文原题

> [!question] 英文原题
> **12.20** Consider a logistic regression model and assume $\beta=0$.
> (a) If $0<\sum_{i=1}^ny_i<n$, show that the MLE of $\pi(x)$ (which does not depend on $x$ in this case) is $\hat\pi=\sum_{i=1}^ny_i/n$.
> (b) If $0<\sum_{i=1}^ny_i<n$, show that the MLE of $\alpha$ is $\hat\alpha_0=\log[(\sum_{i=1}^ny_i)/(n-\sum_{i=1}^ny_i)]$.
> (c) Show that if $\sum_{i=1}^ny_i=0$ or $n$, $\hat\alpha_0$ does not exist, but the LRT statistic for testing $H_0:\beta=0$ is still well defined.

### 中文转述

> [!question] 中文转述
> **原题12.20。**
> 考虑逻辑回归模型，并假定$\beta=0$.
>
> (a)  若$0<\sum_{i=1}^ny_i<n$，证明$\pi(x)$的MLE为$\hat\pi=\sum_{i=1}^ny_i/n$，此时它不依赖$x$.
>
> (b)  若$0<\sum_{i=1}^ny_i<n$，证明$\alpha$的MLE为$\hat\alpha_0=\log\bigl((\sum_{i=1}^ny_i)/(n-\sum_{i=1}^ny_i)\bigr)$.
>
> (c)  证明若$\sum_{i=1}^ny_i=0$或$n$，$\hat\alpha_0$不存在，但检验$H_0:\beta=0$的似然比统计量仍有良好定义.

## 提示

> [!hint]- 提示
> 区分参数最大点不取得和似然上确界不存在。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 写$S=\sum_i y_i$。当$\beta=0$，共同成功概率$p=\Lambda(\alpha)$，似然核$L(p)=p^S(1-p)^{n-S}$。
> (a) $0<S<n$时对数导数$S/p-(n-S)/(1-p)$唯一零点$p=S/n$，二阶导负，故为全局MLE。
> (b) Logit为一一变换，$\hat\alpha_0=\log[\hat p/(1-\hat p)]=\log[S/(n-S)]$。
> (c) 若$S=0$，$L=(1-\Lambda(\alpha))^n$随$\alpha\to-\infty$趋1但任何有限值均小于1；$S=n$时相反令$\alpha\to\infty$。故有限$\hat\alpha_0$不存在，但原假设似然sup为1。全模型也不可能超过1，取$\beta=0$及同一极限已能逼近1，所以全似然sup也是1。LRT$\lambda=\sup_{\beta=0}L/\sup_{\alpha,\beta}L=1$，$-2\log\lambda=0$，明确可定义。它不会因MLE系数无穷而自动变为缺失或$0/0$。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[02 - 数理统计/概念/假设检验|假设检验]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=522|印刷491／PDF物理522]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=510|印刷479／PDF物理510]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=514|印刷483／PDF物理514]]；所需模型、公式、数据在解答重述。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
