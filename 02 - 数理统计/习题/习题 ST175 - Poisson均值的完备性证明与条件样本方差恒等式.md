---
title: "习题 ST175：Poisson均值的完备性证明与条件样本方差恒等式"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.52，印刷页295／PDF物理页326"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.52"
source_stars: 0
source_refs: ["DS011 Exercise 7.52，印刷295／PDF物理326", "DS011 例7.3.8的Poisson估计问题，印刷271／PDF物理302", "DS011 定理7.3.23及条件化原则，印刷280／PDF物理311"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST175：Poisson均值的完备性证明与条件样本方差恒等式

## 题目

### 英文原题

> [!question] 英文原题
> **7.52** Let $X_1,\ldots,X_n$ be iid Poisson$(\lambda)$, and let $\bar X$ and $S^2$ denote the sample mean and variance, respectively. We now complete Example 7.3.8 in a different way. There we used the Cramér–Rao Bound; now we use completeness.
>
> (a) Prove that $\bar X$ is the best unbiased estimator of $\lambda$, without using the Cramér–Rao Theorem.
>
> (b) Prove the rather remarkable identity $E(S^2\mid\bar X)=\bar X$, and use it to explicitly demonstrate that $\operatorname{Var}S^2>\operatorname{Var}\bar X$.
>
> (c) Using completeness, can a general theorem be formulated for which the identity in part (b) is a special case?

### 中文转述

> [!question] 中文转述
> **原题7.52。** 设$X_1,\ldots,X_n$独立同分布于$\operatorname{Poisson}(\lambda)$，$\bar X$与$S^2$分别表示样本均值和样本方差.现在用另一种方法完成例7.3.8.那里用了Cramér--Rao下界，这里使用完备性.
>
> (a)  不用Cramér--Rao定理，证明$\bar X$是$\lambda$的最佳无偏估计量.
>
> (b)  证明颇为惊人的恒等式$E(S^2\mid\bar X)=\bar X$，并用它明确说明$\operatorname{Var}S^2>\operatorname{Var}\bar X$.
>
> (c)  利用完备性，能否表述一个一般定理，使(b)中的恒等式成为其特殊情形？

## 提示

> [!hint]- 提示
> 条件于Poisson总和后得到多项分配；完备性用指数幂级数系数唯一性。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 取$n\ge2$，先令$\lambda>0$。
>
> **(a)** 总数$T=\sum_iX_i\sim\operatorname{Poisson}(n\lambda)$由联合pmf因子分解而充分。若$E_\lambda h(T)=0$且绝对期望有限，对每个$\lambda>0$有$\sum_{t\ge0}h(t)(n\lambda)^t/t!=0$。绝对可积性在任意更大正参数成立，故此幂级数在每个有限圆盘绝对收敛；解析函数唯一性给每个系数为零，所以$T$完备。$T/n=\bar X$无偏，条件化任意无偏估计后由完备性只能得到它，全方差证明最佳无偏，无需信息下界。
>
> **(b)** 条件于$T=t$，$(X_1,\ldots,X_n)$有Multinomial$(t;1/n,\ldots,1/n)$分布。故$E(\sum_iX_i^2\mid T=t)=t(1-1/n)+t^2/n$，代入$S^2=[\sum_iX_i^2-T^2/n]/(n-1)$，得$E(S^2\mid T)=T/n=\bar X$。
>
> Poisson中心四阶矩为$\lambda+3\lambda^2$，可由阶乘矩$E(X)_j=\lambda^j$展开得到。样本方差的精确方差因而为
> $$
> \operatorname{Var}S^2=\frac\lambda n+\frac{2\lambda^2}{n-1},\qquad
> \operatorname{Var}\bar X=\lambda/n.
> $$
> 严格差$2\lambda^2/(n-1)>0$，这比仅引用全方差的非严格不等式更明确。$\lambda=0$时两估计均为零、方差相等，故原严格号须排除该退化端点。
>
> **(c)** 一般地，若$T$完备充分，$V=v(T)$无偏估计目标$g(\theta)$，且$U$是任意另一可积无偏估计，则$E(U\mid T)=V$几乎必然。证明是充分性使条件期望不依赖未知参数，迭代期望使其与$V$同均值，完备性使差为零。有二阶矩时$\operatorname{Var}U=\operatorname{Var}V+E\operatorname{Var}(U\mid T)$，这包含(b)。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=326|印刷第295页／PDF物理第326页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 原(b)严格不等式在λ=0端点退化为等号；解答明确该边界。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
