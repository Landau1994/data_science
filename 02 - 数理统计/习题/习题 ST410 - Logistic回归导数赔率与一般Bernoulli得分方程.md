---
title: "习题 ST410：Logistic回归导数赔率与一般Bernoulli得分方程"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.15，印刷页490／PDF物理页521"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.15"
source_stars: 0
source_refs: ["DS011 Exercise 12.15，印刷页490／PDF物理页521", "DS011 所引正文，印刷479／PDF物理510", "DS011 所引正文，印刷480／PDF物理511"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST410：Logistic回归导数赔率与一般Bernoulli得分方程

## 题目

### 英文原题

> [!question] 英文原题
> **12.15** For the logistic regression function in (12.3.2), verify these relationships.
> (a) $\pi(-\alpha/\beta)=1/2$.
> (b) $\pi((-\alpha/\beta)+c)=1-\pi((-\alpha/\beta)-c)$, for any $c$.
> (c) Verify (12.3.3) for $d\pi(x)/dx$.
> (d) Verify (12.3.4) about the odds ratio.
> (e) Verify (12.3.5) about the multiplicative change in odds.
> (f) Verify (12.3.6) and (12.3.8) regarding the likelihood equations for a Bernoulli GLM.
> (g) Verify that for logistic regression, $f_i/[F_i(1-F_i)]=1$, in (12.3.7) and (12.3.8).

### 中文转述

> [!question] 中文转述
> **原题12.15。**
> 对式12.3.2的逻辑回归函数，验证以下关系.
>
> (a)  $\pi(-\alpha/\beta)=1/2$.
>
> (b)  对任意$c$，$\pi((-\alpha/\beta)+c)=1-\pi((-\alpha/\beta)-c)$.
>
> (c)  验证关于$d\pi(x)/dx$的式12.3.3.
>
> (d)  验证关于优势比的式12.3.4.
>
> (e)  验证关于优势乘法变化的式12.3.5.
>
> (f)  验证Bernoulli GLM似然方程的式12.3.6、式12.3.8.
>
> (g)  验证逻辑回归中，式12.3.7、式12.3.8内$f_i/(F_i(1-F_i)=1$.

## 提示

> [!hint]- 提示
> 先写$\eta=\alpha+\beta x$和$\Lambda(-\eta)=1-\Lambda(\eta)$；最后用链式法则。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 记$\Lambda(u)=e^u/(1+e^u)$，$\pi(x)=\Lambda(\alpha+\beta x)$。
> (a) 当$\beta\ne0$，代$x=-\alpha/\beta$得$\Lambda(0)=1/2$。(b) 两线性预测值分别$\pm\beta c$，且$\Lambda(-u)=1-\Lambda(u)$，即得。$\beta=0$时这两式中的除法不定义，实际函数恒为$\Lambda(\alpha)$，不能无条件写中点。
> (c) $\Lambda'(u)=e^u/(1+e^u)^2=\Lambda(u)[1-\Lambda(u)]$，链式法则给$\pi'(x)=\beta\pi(x)(1-\pi(x))$。
> (d) 赔率$O(x)=\pi(x)/(1-\pi(x))=e^{\alpha+\beta x}$，故$O(x+1)/O(x)=e^\beta$。(e) 移项即$O(x+1)=e^\beta O(x)$，是一次预测变量增加对应的赔率乘法变化；不是概率本身乘$e^\beta$。
> (f) 对一般可微CDF链接$F_i=F(\alpha+\beta x_i)$、$f_i=F'(\alpha+\beta x_i)$，假设$0<F_i<1$。链式法则给$\partial_\alpha\log(1-F_i)=-f_i/(1-F_i)=-F_if_i/[F_i(1-F_i)]$，$\partial_\alpha\log[F_i/(1-F_i)]=f_i/[F_i(1-F_i)]$，即(12.3.6)。独立Bernoulli对数似然为$\sum_i[\log(1-F_i)+y_i\log(F_i/(1-F_i))]$，故$\partial_\beta\ell=\sum_i(y_i-F_i)f_i x_i/[F_i(1-F_i)]$，即(12.3.8)；对截距求导同式不带$x_i$为(12.3.7)。
> (g) Logistic下$f_i=F_i(1-F_i)$，比值恰为1，得分方程简化为$\sum_i(y_i-\pi_i)=0$与$\sum_i x_i(y_i-\pi_i)=0$。这些是有限内部MLE的必要方程；分离数据可能没有有限解，不能由形式方程保证MLE存在。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=521|印刷490／PDF物理521]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=510|印刷479／PDF物理510]]、[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=511|印刷480／PDF物理511]]；所需模型、公式、数据在解答重述。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
