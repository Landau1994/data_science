---
title: "习题 ST358：Fisher相关系数z变换的一阶与修正正态近似"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.4，印刷页456／PDF物理页487"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.4"
source_stars: 0
source_refs: ["DS011 Exercise 11.4，印刷456／PDF物理487", "DS011 习题10.17(d)的样本相关渐近输入，印刷410／PDF物理441"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST358：Fisher相关系数z变换的一阶与修正正态近似

## 题目

### 英文原题

> [!question] 英文原题
> **11.4** A most famous (and useful) variance stabilizing transformation is Fisher’s $z$-transformation, which we have already encountered in Exercise 10.17. Here we will look at a few more details. Suppose that $(X,Y)$ are bivariate normal with correlation coefficient $\rho$ and sample correlation $r$.
>
> (a) Starting from Exercise 10.17, part (d), use the Delta Method to show that
> $$
> \frac12\left[\log\left(\frac{1+r}{1-r}\right)-\log\left(\frac{1+\rho}{1-\rho}\right)\right]
> $$
> is approximately normal with mean 0 and variance $1/n$.
>
> (b) Fisher actually used a somewhat more accurate expansion (Stuart and Ord 1987, Section 16.33) and established that the quantity in part (a) is approximately normal with
> $$
> \text{mean}=\frac\rho{2(n-1)}\quad\text{and variance}=\frac1{n-1}+\frac{4-\rho^2}{2(n-1)^2}.
> $$
> Show that for small $\rho$ and moderate $n$, we can approximate this mean and variance by 0 and $1/(n-3)$, which is the most popular form of the Fisher’s $z$-transformation.

### 中文转述

> [!question] 中文转述
> **原题11.4。** 一种极著名且有用的方差稳定变换是Fisher的$z$变换，在习题10.17已遇到. 这里再考察一些细节. 假设$(X,Y)$服从二元正态分布，相关系数为$\rho$，样本相关系数为$r$.
>
> (a)  从习题10.17(d)出发，用Delta方法证明
>
> $$
> \frac12\left[\log\left(\frac{1+r}{1-r}\right)-\log\left(\frac{1+\rho}{1-\rho}\right)\right]
> $$
>
> 近似正态，均值为0，方差为$1/n$.
>
> (b)  Fisher实际上使用了稍精确的展开（Stuart和Ord，1987，第16.33节），证明(a)中的量近似正态，且
>
> $$
> \text{均值}=\frac\rho{2(n-1)},\qquad\text{方差}=\frac1{n-1}+\frac{4-\rho^2}{2(n-1)^2}.
> $$
>
> 证明，对较小的$\rho$和中等的$n$，可将此均值、方差近似为0和$1/(n-3)$，这就是Fisher $z$变换最常用的形式.

## 提示

> [!hint]- 提示
> atanh的导数正好消去样本相关系数的一阶渐近标准差。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 假定非退化二维正态、$|\rho|<1$，样本量足以定义相关系数。
>
> **(a)** 10.17(d)的输入为$\sqrt n(r-\rho)\Rightarrow n(0,(1-\rho^2)^2)$。令$g(u)=\tfrac12\log[(1+u)/(1-u)]=\operatorname{arctanh}u$，其导数$g'(\rho)=1/(1-\rho^2)$。Delta方法给$\sqrt n[g(r)-g(\rho)]\Rightarrow n(0,1)$，所以未缩放差近似均值0、方差$1/n$。这是一阶渐近输入的推导，不是有限$n$的精确正态分布。
>
> **(b)** 本题给定的高阶展开作为输入，不在此重新证明Fisher的展开。记$m=n-1>2$，其均值$\rho/(2m)$在小$|\rho|$、中等以上$m$时相对标准差约$1/\sqrt m$的比例为$|\rho|/(2\sqrt m)$，可近似忽略。其方差为$1/m+2/m^2-\rho^2/(2m^2)$；而
> $$
> \frac1{n-3}=\frac1{m-2}=\frac1m+\frac2{m^2}+\frac4{m^2(m-2)}.
> $$
> 故二者的精确差（相对于题给截断展开）为$-\rho^2/(2m^2)-4/[m^2(m-2)]$，在小$\rho$与较大$m$时是较高阶项，说明为何常用方差$1/(n-3)$。$n\le3$或$|\rho|$接近1不能机械套该修正，也未声称误差有统一精确界。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=487|印刷第456页／PDF物理第487页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 题引Fisher高阶展开为原题给定输入，未将其标为本题独立复证。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
