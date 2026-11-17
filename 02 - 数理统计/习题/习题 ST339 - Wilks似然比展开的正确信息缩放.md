---
title: 习题 ST339：Wilks似然比展开的正确信息缩放
topic: mathematical-statistics
topic_label: 数理统计
difficulty: advanced
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.33，印刷页415／PDF物理页446
source_id: DS011
source_chapter: 10
source_exercise: '10.33'
source_stars: 0
source_refs:
- DS011 Exercise 10.33，印刷415／PDF物理446
- DS011题内依赖核对：印刷381／PDF物理412；印刷395／PDF物理426
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST339：Wilks似然比展开的正确信息缩放

## 题目

### 英文原题

> [!question] 英文原题
> **10.33** Fill in the gap in Theorem 10.3.1. Use Theorem 10.1.12 and Slutsky's Theorem (Theorem 5.5.17) to show that $(\theta-\hat\theta)/\sqrt{-l''(\hat\theta\mid x)}\to\operatorname n(0,1)$, and therefore $-2\log\lambda(X)\to\chi_1^2$.

### 中文转述

> [!question] 中文转述
> **原题10.33。** 补全定理10.3.1中的空缺. 用定理10.1.12及Slutsky定理（定理5.5.17）证明$(\theta-\hat\theta)/\sqrt{-l''(\hat\theta\mid\boldsymbol x)}\to\mathrm n(0,1)$，从而$-2\log\lambda(\boldsymbol X)\to\chi_1^2$.

## 提示

> [!hint]- 提示
> 观测信息是n阶，参数误差是n^(−1/2)阶，二者应相乘平方根，不能相除。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 原显示归一化错误。设$J_n=-l_n''(\hat\theta)$，在真值$\theta_0$的常规正则条件下$J_n/n\to_pI(\theta_0)>0$且$\sqrt n(\hat\theta-\theta_0)\Rightarrow N(0,1/I)$。因此题中比值
> $$
> \frac{\theta_0-\hat\theta}{\sqrt{J_n}}=\frac{\sqrt n(\theta_0-\hat\theta)}{n\sqrt{J_n/n}}\to_p0,
> $$
> 不可能趋于标准正态。正确式为$\sqrt{J_n}(\hat\theta-\theta_0)\Rightarrow N(0,1)$，由MLE极限乘以$\sqrt{J_n/n}\to_p\sqrt I$直接应用Slutsky得到。
>
> 在$H_0:\theta=\theta_0$下，Taylor展开、$l_n'(\hat\theta)=0$及足够小的余项给
> $$
> -2\log\lambda=2[l_n(\hat\theta)-l_n(\theta_0)]=J_n(\hat\theta-\theta_0)^2+o_p(1)\Rightarrow\chi^2_1.
> $$
> 这里余项$o_p(1)$须由局部三阶导控制或等价似然正则性保证，不能只依赖点态二阶导大数定律。原定理证明也把乘法写成分母，错误原样保留；修正后才是Wilks结论。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=446|印刷第415页／PDF物理第446页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实读定理10.3.1：印刷395／PDF426；定理10.1.12见PDF412。原式归一化反向用阶数和极限直接反驳。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=412|印刷381／PDF物理412]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=426|印刷395／PDF物理426]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
