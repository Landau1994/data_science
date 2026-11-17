---
title: "习题 ST364：Helmert正交对比的含义与肥料计划对比"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.10，印刷页457／PDF物理页488"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.10"
source_stars: 0
source_refs: ["DS011 Exercise 11.10，印刷457／PDF物理488", "DS011 例11.2.3完整五处理肥料配比，印刷424／PDF物理455"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST364：Helmert正交对比的含义与肥料计划对比

## 题目

### 英文原题

> [!question] 英文原题
> **11.10** Suppose we have a oneway ANOVA with five treatments. Denote the treatment means by $\theta_1,\ldots,\theta_5$, where $\theta_1$ is a control and $\theta_2,\ldots,\theta_5$ are alternate new treatments and assume that an equal number of observations per treatment is taken. Consider the four contrasts $\sum a_i\theta_i$ defined by
> $$
> \mathbf a_1=(1,-1/4,-1/4,-1/4,-1/4),\quad
> \mathbf a_2=(0,1,-1/3,-1/3,-1/3),
> $$
> $$
> \mathbf a_3=(0,0,1,-1/2,-1/2),\qquad\mathbf a_4=(0,0,0,1,-1).
> $$
> (a) Argue that the results of the four $t$ tests using these contrasts can lead to conclusions about the ordering of $\theta_1,\ldots,\theta_5$. What conclusions might be made?
>
> (b) Show that any two contrasts $\sum a_i\bar Y_{i\cdot}$ formed from the four $\mathbf a_i$s in part (a) are uncorrelated. (Recall that these are called orthogonal contrasts.)
>
> (c) For the fertilizer experiment of Example 11.2.3, the following contrasts were planned:
> $$
> \mathbf a_1=(-1,1,0,0,0),\quad\mathbf a_2=(0,-1,1/2,1/2,0),\quad
> \mathbf a_3=(0,0,1,-1,0),\quad\mathbf a_4=(0,-1,0,0,1,).
> $$
> Show that these contrasts are not orthogonal. Interpret these contrasts in the context of the fertilizer experiment, and argue that they are a sensible set of contrasts.

### 中文转述

> [!question] 中文转述
> **原题11.10。** 假设有一个五处理的单因素ANOVA. 处理均值记为$\theta_1,\ldots,\theta_5$，其中$\theta_1$为对照，$\theta_2,\ldots,\theta_5$为备选新处理，并假设每个处理取相同数量的观测. 考虑由下列向量定义的四个对比$\sum a_i\theta_i$：
>
> $$
> \begin{aligned}
> \boldsymbol a_1&=(1,-\tfrac14,-\tfrac14,-\tfrac14,-\tfrac14),\\
> \boldsymbol a_2&=(0,1,-\tfrac13,-\tfrac13,-\tfrac13),\\
> \boldsymbol a_3&=(0,0,1,-\tfrac12,-\tfrac12),\\
> \boldsymbol a_4&=(0,0,0,1,-1).
> \end{aligned}
> $$
>
> (a)  说明使用这些对比进行四个$t$检验，其结果可以对$\theta_1,\ldots,\theta_5$的排序得出结论. 可能得到哪些结论？
>
> (b)  证明由(a)中的四个$\boldsymbol a_i$形成的任意两个对比$\sum a_i\bar Y_{i\cdot}$互不相关. （回顾它们称为正交对比.）
>
> (c)  对例11.2.3的肥料实验，预先安排了以下对比：
>
> $$
> \begin{aligned}
> \boldsymbol a_1&=(-1,1,0,0,0),\\
> \boldsymbol a_2&=(0,-1,\tfrac12,\tfrac12,0),\\
> \boldsymbol a_3&=(0,0,1,-1,0),\\
> \boldsymbol a_4&=(0,-1,0,0,1,).
> \end{aligned}
> $$
>
> 证明这些对比并不正交. 在肥料实验的背景下解释这些对比，说明它们是一组合理的对比.

## 提示

> [!hint]- 提示
> Helmert对比比较一个处理与后面处理的平均；正交性由向量内积判断。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(a)** 四个目标依次为对照减四种新处理的平均、处理2减处理3–5的平均、处理3减处理4–5的平均、处理4减处理5。相应正向或负向的显著结果提供的是这些**均值与后续平均的相对大小**；最后一项直接比较4与5。不能仅由四项均为正推出$\theta_1>\theta_2>\cdots>\theta_5$：例如$(200,150,60,100,0)$使四项都正，但$\theta_3<\theta_4$。未拒绝零对比也不证明相等。联合推断若要控制总体错误率，仍需指定适当同时检验校正。
>
> **(b)** 每组样本量相同为$n$时，两个对比的协方差为$(\sigma^2/n)\mathbf a_i^\mathsf T\mathbf a_j$。对$i<j$，$\mathbf a_j$非零部分处在$\mathbf a_i$的同一个常系数尾段，且$\mathbf a_j$系数和为0，因此内积为0；六个非对角内积均如此。正态下这四个未Student化对比相互独立，但各$t$统计量共用$S_p$，不能据此称其相互独立。
>
> **(c)** 按五维向量解释末项多余逗号，第一和第二向量内积为$-1$，第一与第四为$-1$，第二与第四为1，所以不是正交组。例11.2.3的五处理（镁、钾、锌，磅/英亩）分别为$(0,0,0),(0,200,0),(50,200,0),(200,200,0),(0,200,15)$。因此四项分别衡量：施钾与不施肥之差；在施钾基线上两种镁剂量的平均附加作用；两种镁剂量之间的作用差；施钾基线上加锌的附加作用。它们紧扣预先关心的处理问题，故合理；科学解释合理不要求所有计划对比恰好正交。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=488|印刷第457页／PDF物理第488页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 原(c)末向量多余逗号照录，解答明确按五维系数解释；不把平均排序扩大成逐对全排序。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
