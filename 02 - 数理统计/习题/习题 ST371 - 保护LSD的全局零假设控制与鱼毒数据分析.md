---
title: "习题 ST371：保护LSD的全局零假设控制与鱼毒数据分析"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.17，印刷页458–459／PDF物理页489,490"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.17"
source_stars: 0
source_refs: ["DS011 Exercise 11.17，印刷458–459／PDF物理489,490", "DS011 例11.2.1完整鱼毒数据，印刷422／PDF物理453", "DS011 合并方差与单对t统计量，印刷427／PDF物理458"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST371：保护LSD的全局零假设控制与鱼毒数据分析

## 题目

### 英文原题

> [!question] 英文原题
> **11.17** A multiple comparison procedure called the Protected LSD (Protected Least Significant Difference) is performed as follows. If the ANOVA $F$ test rejects $H_0$ at level $\alpha$, then for each pair of means $\theta_i$ and $\theta_{i'}$, declare the means different if
> $$
> \frac{|\bar Y_{i\cdot}-\bar Y_{i'\cdot}|}{\sqrt{S_p^2(1/n_i+1/n_{i'})}}>t_{\alpha/2,N-k}.
> $$
> Note that each $t$ test is done at the same $\alpha$ level as the ANOVA $F$ test. Here we are using an experimentwise $\alpha$ level, where
> $$
> \text{experimentwise }\alpha=P\left(\text{at least one false assertion of difference}\mid\text{all the means are equal}\right).
> $$
> (a) Prove that no matter how many means are in the experiment, simultaneous inference from the Protected LSD is made at level $\alpha$.
>
> (b) The ordinary (or unprotected) LSD simply does the individual $t$ tests, at level $\alpha$, no matter what the outcome of the ANOVA $F$ test. Show that the ordinary LSD can have an experimentwise error rate greater than $\alpha$. (The unprotected LSD does maintain a comparisonwise error rate of $\alpha$.)
>
> (c) Perform the LSD procedure on the fish toxin data of Example 11.2.1. What are the conclusions?

### 中文转述

> [!question] 中文转述
> **原题11.17。** 一种称为受保护LSD（Protected Least Significant Difference，受保护的最小显著差）的多重比较程序如下进行：若ANOVA $F$检验在水平$\alpha$拒绝$H_0$，则对每对均值$\theta_i,\theta_{i'}$，在
>
> $$
> \frac{|\bar Y_{i\cdot}-\bar Y_{i'\cdot}|}{\sqrt{S_p^2(1/n_i+1/n_{i'})}}>t_{\alpha/2,N-k}
> $$
>
> 时判定均值不同. 注意，每个$t$检验都在与ANOVA $F$检验相同的$\alpha$水平进行. 这里使用全实验$\alpha$水平（experimentwise $\alpha$），其中
>
> $$
> \text{全实验 }\alpha=P\left(\text{至少作出一个错误的差异断言}\mid\text{所有均值相等}\right).
> $$
>
> (a)  证明，无论实验中有多少均值，受保护LSD所作的同时推断都处于水平$\alpha$.
>
> (b)  普通（或不受保护的）LSD不论ANOVA $F$检验结果如何，都直接进行水平$\alpha$的各个$t$检验. 证明，普通LSD的全实验错误率可能大于$\alpha$. （不受保护LSD确实维持了每次比较的错误率$\alpha$.）
>
> (c)  对例11.2.1的鱼类毒素数据进行LSD程序. 结论是什么？

## 提示

> [!hint]- 提示
> 保护方法的错误事件是F拒绝事件的子集；普通方法则是多个拒绝事件的并集。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(a)** 在题目明确规定的“所有均值相等”全局原假设下，任一保护LSD错误宣告都必须先发生整体F拒绝。因此$P(\text{至少一个错误宣告})\le P(F\text{拒绝})=\alpha$，对任意处理数成立。一般只是“不超过$\alpha$”，未必恰等于。这个证明只给全局零假设下的**弱控制**，不证明部分均值相等、部分不同情况下的强家族错误率控制。
>
> **(b)** 对$k\ge3$，全局原假设下任一单对拒绝事件$A_{12}$的概率为$\alpha$。正态均值向量及正合并方差有连续正密度，存在正概率的开集合使$|T_{12}|$小而$|T_{13}|$超过阈值，所以$P(A_{13}\setminus A_{12})>0$，从而$P(\bigcup A_{ij})\ge\alpha+P(A_{13}\setminus A_{12})>\alpha$。每个单对仍为水平$\alpha$，不意味着并集也是。
>
> **(c)** 原题未指定数值$\alpha$；以下明确用$\alpha=.05$，并给完整p值供其他水平判断。PDF453数据按“毒素1、毒素2、毒素3、对照”依次为$(28,23,14,27)$、$(33,36,34,29,31,34)$、$(18,21,20,22,24)$、$(11,14,11,16)$。均值为23、32.833333、21、13，组样本量4、6、5、4；$S_p^2=12.72222222$，残差自由度15，整体$F=26.09354171$、p值$3.34797\times10^{-6}$，先通过保护门槛。$t_{15,.025}=2.13144955$。
>
> | 成对处理 | 带符号$t$ | 双侧p值 | .05结论 |
> | --- | --- | --- | --- |
> | 1−2 | −4.270954 | 0.000669843 | 不同，2较大 |
> | 1−3 | 0.835877 | 0.416341127 | 未拒绝 |
> | 1−对照 | 3.964912 | 0.001245126 | 1较大 |
> | 2−3 | 5.478856 | 0.000063523 | 2较大 |
> | 2−对照 | 8.614297 | 0.000000342 | 2较大 |
> | 3−对照 | 3.343507 | 0.004444141 | 3较大 |
>
> 所以毒素2高于其他组，三种毒素均高于对照；毒素1与3的差异未显著，不等于证明相等。此数据下保护与普通LSD给相同成对结果，因为整体F已拒绝。表中是原LSD的未多重调整单项p值，不能误称对任意部分零假设具有强保护。全部计算已执行[[工具/StatisticalInference/ch11_numeric_checks.py|程序]]，数据及结果见[[工具/StatisticalInference/ch11-numeric-results.json|记录]]。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=489|印刷第458页／PDF物理第489页]]及[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=490|续页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 原题临界值下标顺序不同但按右尾分位数解释；计算明确指定.05，学习状态不随有解答而改变。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
