---
title: "习题 ML004：Lasso与岭回归的偏差方差权衡"
topic: statistical-learning
topic_label: 统计学习
difficulty: beginner
status: not-started
tags:
  - exercise
  - statistical-learning
source: "[[00 - 首页/教材归档/DS013 - Introduction to Statistical Learning R|ISLR（DS013）]]"
source_id: DS013
source_chapter: 6
source_exercise: "6.2"
source_refs: ["DS013 §6.6 Exercise 2，印刷283–284/PDF294–295"]
source_status: verified
solution_status: independently-derived
created: 2026-10-25
---

# 习题 ML004：Lasso与岭回归的偏差方差权衡

## 题目

### 英文原题

> [!question] 英文原题
> **2.** For parts (a) through (c), indicate which of i. through iv. is correct. Justify your answer.
>
> **(a)** The lasso, relative to least squares, is:
>
> **i.** More flexible and hence will give improved prediction accuracy when its increase in bias is less than its decrease in variance.
>
> **ii.** More flexible and hence will give improved prediction accuracy when its increase in variance is less than its decrease in bias.
>
> **iii.** Less flexible and hence will give improved prediction accuracy when its increase in bias is less than its decrease in variance.
>
> **iv.** Less flexible and hence will give improved prediction accuracy when its increase in variance is less than its decrease in bias.
>
> **(b)** Repeat (a) for ridge regression relative to least squares.
>
> **(c)** Repeat (a) for non-linear methods relative to least squares.

### 中文转述

> [!question] 中文转述
> **ISLR 第 6 章原题 2（记作 6.2）。** 对 (a)–(c)，从 i–iv 中选择正确选项，并解释理由。
>
> **(a)** 与最小二乘（least squares）相比，Lasso 回归（lasso）：
>
> **i.** 灵活性更高，因此当偏差增加小于方差减少时，预测准确性改善。
>
> **ii.** 灵活性更高，因此当方差增加小于偏差减少时，预测准确性改善。
>
> **iii.** 灵活性更低，因此当偏差增加小于方差减少时，预测准确性改善。
>
> **iv.** 灵活性更低，因此当方差增加小于偏差减少时，预测准确性改善。
>
> **(b)** 将 (a) 中的 Lasso 换成岭回归（ridge regression），仍与最小二乘比较。
>
> **(c)** 将 (a) 中的方法换成非线性方法（non-linear methods），仍与最小二乘比较。

## 提示

> [!hint]- 提示 1
> 惩罚或约束如何限制系数的可选范围？更小的训练误差是否必然意味着更小的测试误差？

> [!hint]- 提示 2
> 对同一个预测目标，在平方损失下比较“平方偏差 + 方差 + 不可约误差”。原题选项中的 bias 在这个比较中应如何理解？

## 解答

> [!success]- 解答
> **证明范围：独立推导，并说明教材概括的适用边界。** 按本章讨论的典型模型复杂度比较，答案为 **(a) iii，(b) iii，(c) ii**。原题的“偏差增加／减少”在平方误差比较中应理解为**平方偏差的增加／减少**，不能直接将有量纲差异的偏差与方差相减。
>
> **平方误差分解。** 固定预测位置 $x$，设新响应 $Y=f(x)+\epsilon$，其中 $E[\epsilon\mid x]=0$、$\operatorname{Var}(\epsilon\mid x)=\sigma^2$，新噪声与训练资料独立。对训练资料的随机性取期望，令 $m(x)=E[\hat f(x)]$，则
> $$
> \begin{aligned}
> E[(Y-\hat f(x))^2]
> &=\sigma^2+E[(f(x)-\hat f(x))^2]\\
> &=\sigma^2+(f(x)-m(x))^2
> +E[(\hat f(x)-m(x))^2].
> \end{aligned}
> $$
> 第一行的交叉项因新噪声条件均值为零而消失，第二行的交叉项因 $E[\hat f(x)-m(x)]=0$ 而消失。因此同一问题下的误差变化是
> $$
> \Delta\operatorname{MSE}(x)
> =\Delta\operatorname{Bias}^2(x)
> +\Delta\operatorname{Var}(\hat f(x)).
> $$
>
> **(a) Lasso：iii。** 对给定的非平凡惩罚，Lasso 将线性模型的系数向零收缩，并可能把部分斜率设为零；约束形式把可选参数限制在一个 $\ell_1$ 球内。因此它相对于不受约束的最小二乘具有较低的拟合灵活性。典型情况下，限制带来平方偏差增加及方差减少；当方差的减少量超过平方偏差的增加量时，上式给出负的误差变化，预测准确性改善。
>
> **(b) 岭回归：iii。** 岭惩罚也限制系数大小，通常收缩而不精确筛掉变量。它同样以引入收缩偏差换取较小波动；在平方偏差增加少于方差减少时改善预测。惩罚为零时可与最小二乘重合，不能把“更低”理解为所有参数值下都严格降低。
>
> **(c) 典型的更灵活非线性方法：ii。** 本题把非线性方法作为比线性最小二乘更灵活的模型族来讨论。例如在相同输入上加入可自由估计的非线性基函数，可以降低线性模型的近似偏差，同时增加估计方差。若平方偏差的减少量超过方差的增加量，则测试均方误差下降。
>
> **结论边界。** “非线性”本身并不逻辑蕴含“更灵活”：一个固定的非线性函数可能完全没有待估参数；强约束非线性模型也未必比无约束线性模型灵活。Lasso、岭回归的偏差与方差变化也依赖数据分布、设计、惩罚强度及评价位置。本题答案对应本章的典型权衡图景，不是对所有数据与所有模型逐一成立的严格排序，更不是一次训练集拟合就能确定的实测结论。

## 相关概念

- [[04 - 统计学习/概念/Lasso回归|Lasso回归]]：稀疏约束与拟合灵活性。
- [[04 - 统计学习/概念/岭回归|岭回归]]：连续收缩与偏差方差权衡。
- [[04 - 统计学习/概念/正则化|正则化]]：惩罚改变可选参数及拟合行为。
- [[04 - 统计学习/概念/泛化、欠拟合与过拟合|泛化、欠拟合与过拟合]]：训练拟合与测试预测的差异。
- [[04 - 统计学习/概念/损失函数与经验风险|损失函数与经验风险]]：平方损失下的误差分解。

## 备注

- 原题逐句对照 [[附件/books/ISLR.pdf#page=294|ISLR 印刷第 283 页／PDF 物理第 294 页]] 与 [[附件/books/ISLR.pdf#page=295|印刷第 284 页／PDF 物理第 295 页]]；(c) 位于后一页。原题没有星号。
- 英文保留原文的 bias 用语；平方偏差解释及非线性方法的反例边界属于本笔记独立补充，没有混入英文原题。
- `source_status: verified` 只覆盖本题原文和页码核对；解答为独立推导，未核对官方答案，未运行统计实验。学习状态保持 `not-started`。
