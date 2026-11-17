---
title: "习题 ST356：Poisson二项与乘性方差模型的稳定变换"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.2，印刷页456／PDF物理页487"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.2"
source_stars: 0
source_refs: ["DS011 Exercise 11.2，印刷456／PDF物理487"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST356：Poisson二项与乘性方差模型的稳定变换

## 题目

### 英文原题

> [!question] 英文原题
> **11.2** Verify that the following transformations are approximately variance-stabilizing in the sense of Exercise 11.1.
>
> (a) $Y\sim\operatorname{Poisson}$, $g^*(y)=\sqrt y$.
>
> (b) $Y\sim\operatorname{binomial}(n,p)$, $g^*(y)=\sin^{-1}(\sqrt{y/n})$.
>
> (c) $Y$ has variance $v(\theta)=K\theta^2$ for some constant $K$, $g^*(y)=\log(y)$.
>
> (Conditions for the existence of variance-stabilizing transformations go back at least to Curtiss 1943, with refinements given by Bar-Lev and Enis 1988, 1990.)

### 中文转述

> [!question] 中文转述
> **原题11.2。** 验证下列变换在习题11.1的意义下近似稳定方差.
>
> (a)  $Y\sim\operatorname{Poisson}$，$g^*(y)=\sqrt y$.
>
> (b)  $Y\sim\operatorname{binomial}(n,p)$，$g^*(y)=\sin^{-1}(\sqrt{y/n})$.
>
> (c)  $Y$的方差为$v(\theta)=K\theta^2$，其中$K$为常数，$g^*(y)=\log y$.
>
> （方差稳定变换的存在条件至少可追溯至Curtiss，1943；Bar-Lev和Enis，1988、1990，给出了改进.）

## 提示

> [!hint]- 提示
> 把每个模型的均值方差关系代入一阶Delta方差公式。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 全部结论是11.1的一阶线性化近似，非精确有限样本方差公式。
>
> **(a)** Poisson均值$\theta>0$且方差$\theta$。$g'(\theta)=1/(2\sqrt\theta)$，故近似方差$g'(\theta)^2\theta=1/4$。$Y=0$时平方根本身定义良好，但均值接近零时导数与线性化并不稳定，不能声称小均值也精确。
>
> **(b)** 以$\theta=np$为均值，方差$\theta(1-\theta/n)$。对$0<y<n$，$g'(y)=1/[2\sqrt{y(n-y)}]$，故
> $$
> g'(\theta)^2v(\theta)=\frac{\theta(1-\theta/n)}{4\theta(n-\theta)}=\frac1{4n}.
> $$
> 因此与$p$无关；这里$\sin^{-1}$表示反正弦而非倒数。$p=0,1$的退化端点不满足导数条件，小成功/失败期望时该近似也可能欠佳。
>
> **(c)** 必须额外有$Y>0$几乎必然、$\theta>0$，否则方差信息本身不足以定义$\log Y$。在这些定义域与余项可控条件下，$g'(\theta)=1/\theta$，故近似方差$K$。若$K=0$则退化，若$K<0$且$\theta\ne0$根本不能是方差。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=487|印刷第456页／PDF物理第487页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 对数变换所需正支持及端点近似条件明确补充；题引论文未另行查阅。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
