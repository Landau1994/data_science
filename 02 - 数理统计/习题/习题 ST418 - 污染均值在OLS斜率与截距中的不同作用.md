---
title: "习题 ST418：污染均值在OLS斜率与截距中的不同作用"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第12章习题12.23，印刷页491／PDF物理页522"
source_id: "DS011"
source_chapter: 12
source_exercise: "12.23"
source_stars: 0
source_refs: ["DS011 Exercise 12.23，印刷页491／PDF物理页522", "DS011 所引正文，印刷484／PDF物理515"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST418：污染均值在OLS斜率与截距中的不同作用

## 题目

### 英文原题

> [!question] 英文原题
> **12.23** In Example 12.4.1, in contrast to Exercise 10.2.1, when we introduced the contaminated distribution for $\varepsilon_i$, we did not introduce a bias. Show that if we had, it would not have mattered. That is, if we assume
> $$ (E\varepsilon_i,\operatorname{Var}\varepsilon_i)=\begin{cases}(0,\sigma^2)&\text{with probability }1-\delta,\\(\mu,\tau^2)&\text{with probability }\delta,\end{cases}$$
> then
> (a) the least squares estimator $b$ would still be an unbiased estimator of $\beta$.
> (b) the least squares estimator $a$ has expectation $\alpha+\delta\mu$, so the model may just as well be assumed to be $Y_i=\alpha+\delta\mu+\beta x_i+\varepsilon_i$.

### 中文转述

> [!question] 中文转述
> **原题12.23。**
> 例12.4.1与习题10.2.1不同，引入$\varepsilon_i$的污染分布时没有引入偏倚. 证明即使引入偏倚也不会有影响. 即假设
>
> $$
> \bigl(E\varepsilon_i,\operatorname{Var}\varepsilon_i\bigr)=
> \begin{cases}(0,\sigma^2),&\text{概率为 }1-\delta,\\(\mu,\tau^2),&\text{概率为 }\delta,
> \end{cases}
> $$
>
> 则
>
> (a)  最小二乘估计量$b$仍为$\beta$的无偏估计量.
>
> (b)  最小二乘估计量$a$的期望为$\alpha+\delta\mu$，所以也可将模型假设为$Y_i=\alpha+\delta\mu+\beta x_i+\varepsilon_i$.

## 提示

> [!hint]- 提示
> 混合误差的共同均值被斜率中心化权重消去，被截距权重总和保留。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 把题内两组矩理解为污染类别条件矩，则误差的无条件均值$m=\delta\mu$，无条件方差为$(1-\delta)\sigma^2+\delta\tau^2+\delta(1-\delta)\mu^2$，不是只平均两个条件方差。
> (a) 固定设计$S_{xx}>0$，斜率$b=\beta+\sum_i(x_i-\bar x)\varepsilon_i/S_{xx}$。各误差有同一均值$m$，而中心化权重和0，所以$Eb=\beta$。不需要用均值零来偷换题设。
> (b) $Ea=E\bar Y-\bar xEb=(\alpha+\beta\bar x+m)-\bar x\beta=\alpha+\delta\mu$。因此定义**中心化误差**$\varepsilon_i^*=\varepsilon_i-\delta\mu$，可将模型写成$Y_i=(\alpha+\delta\mu)+\beta x_i+\varepsilon_i^*$，$E\varepsilon_i^*=0$。原文最后仍写$\varepsilon_i$应理解为重新中心化后的新误差；若继续让同一符号具有原先均值$\delta\mu$，就会重复加入偏移。斜率不变，但若科学目标是未污染截距$\alpha$，估计$a$确有$\delta\mu$偏差，不能说截距也不受影响。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计（parameter estimation）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/随机变量|随机变量]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=522|印刷491／PDF物理522]]；原题无星号。教材信息与归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实际引用输入核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=515|印刷484／PDF物理515]]；所需模型、公式、数据在解答重述。
- 来源已核对与解答写成不表示个人学习已完成；学习状态保留`not-started`。未实测Obsidian界面渲染。
