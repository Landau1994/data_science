---
title: "习题 ST355：Delta线性化的方差近似与稳定变换积分"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.1，印刷页455–456／PDF物理页486,487"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.1"
source_stars: 0
source_refs: ["DS011 Exercise 11.1，印刷455–456／PDF物理486,487"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST355：Delta线性化的方差近似与稳定变换积分

## 题目

### 英文原题

> [!question] 英文原题
> **11.1** An ANOVA variance-stabilizing transformation stabilizes variances in the following approximate way. Let $Y$ have mean $\theta$ and variance $v(\theta)$.
>
> (a) Use arguments as in Section 10.1.3 to show that a one-term Taylor series approximation of the variance of $g(y)$ is given by $\operatorname{Var}(g(Y))=[\frac d{d\theta}g(\theta)]^2v(\theta)$.
>
> (b) Show that the approximate variance of $g^*(Y)$ is independent of $\theta$, where $g^*(y)=\int[1/\sqrt{v(y)}]dy$.

### 中文转述

> [!question] 中文转述
> **原题11.1。** ANOVA中的方差稳定变换（variance-stabilizing transformation）以下述近似方式稳定方差. 设$Y$的均值为$\theta$，方差为$v(\theta)$.
>
> (a)  用类似节10.1.3的论证，说明单项Taylor级数近似给出$g(y)$的方差为
>
> $$
> \operatorname{Var}(g(Y))=\left[\frac d{d\theta}g(\theta)\right]^2v(\theta).
> $$
>
> (b)  证明$g^*(Y)$的近似方差与$\theta$无关，其中$g^*(y)=\int[1/\sqrt{v(y)}]\,dy$.

## 提示

> [!hint]- 提示
> 只保留Taylor展开的随机一次项；稳定方差要求导数抵消标准差。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(a)** 在$\theta$附近展开$g(Y)=g(\theta)+g'(\theta)(Y-\theta)+R$，舍去余项后常数不影响方差，因此一阶近似为$\operatorname{Var}g(Y)\approx g'(\theta)^2v(\theta)$。原题等号是在线性化模型内的近似等号，不是任意分布的精确恒等式。
>
> 若要控制近似，设$ER^2<\infty$，则精确误差满足
> $$
> |\operatorname{Var}g(Y)-g'(\theta)^2v(\theta)|
> \le2|g'(\theta)|\sqrt{v(\theta)ER^2}+ER^2.
> $$
> 当余项的二阶矩相对线性项方差足够小时才有可靠方差近似；单凭均值方差信息不保证任意非线性$g(Y)$可积。
>
> **(b)** 在$v>0$且连续的均值区间，令$g^*(y)=\int^y v(u)^{-1/2}du$，则$(g^*)'(\theta)=v(\theta)^{-1/2}$。代入(a)得到近似方差1，与$\theta$无关；再作$Ag^*+B$会得到近似常数方差$A^2$。若$v=0$或存在定义域端点、奇点，须另查变换及近似的适用性。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=486|印刷第455页／PDF物理第486页]]及[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=487|续页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
