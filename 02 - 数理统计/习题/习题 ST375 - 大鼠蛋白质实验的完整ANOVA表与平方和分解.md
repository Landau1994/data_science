---
title: "习题 ST375：大鼠蛋白质实验的完整ANOVA表与平方和分解"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.21，印刷页459／PDF物理页490"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.21"
source_stars: 0
source_refs: ["DS011 Exercise 11.21，印刷459／PDF物理490", "DS011 定理11.2.11及式(11.2.15)，印刷433／PDF物理464"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST375：大鼠蛋白质实验的完整ANOVA表与平方和分解

## 题目

### 英文原题

> [!question] 英文原题
> **11.21** (a) Illustrate the partitioning of the sums of squares in the ANOVA by calculating the complete ANOVA table for the following data. To determine diet quality, male weanling rats were fed diets with various protein levels. Each of fifteen rats was randomly assigned to one of three diets, and their weight gain in grams was recorded.
>
> **Diet protein level**
>
> | Low | Medium | High |
> | --- | --- | --- |
> | 3.89 | 8.54 | 20.39 |
> | 3.87 | 9.32 | 24.22 |
> | 3.26 | 8.76 | 30.91 |
> | 2.70 | 9.30 | 22.78 |
> | 3.82 | 10.45 | 26.33 |
>
> (b) Analytically verify the partitioning of the ANOVA sums of squares by completing the proof of Theorem 11.2.11.
>
> (c) Illustrate the relationship between the $t$ and $F$ statistics, given in Exercise 11.12b, using the data of part (a).

### 中文转述

> [!question] 中文转述
> **原题11.21。** (a)  计算下列数据的完整ANOVA表，说明ANOVA中的平方和分解. 为确定饲料质量，对雄性断奶大鼠喂食不同蛋白质水平的饲料. 将15只大鼠分别随机分配至三种饲料之一，记录其体重增加量，单位为克.
>
> **饲料蛋白质水平**
>
> | 低 | 中 | 高 |
> | --- | --- | --- |
> | 3.89 | 8.54 | 20.39 |
> | 3.87 | 9.32 | 24.22 |
> | 3.26 | 8.76 | 30.91 |
> | 2.70 | 9.30 | 22.78 |
> | 3.82 | 10.45 | 26.33 |
>
> (b)  完成定理11.2.11的证明，以解析方式验证ANOVA平方和分解.
>
> (c)  用(a)的数据说明习题11.12(b)中$t$统计量与$F$统计量的关系.

## 提示

> [!hint]- 提示
> 组内中心化使交叉项为零；平衡设计的成对t平方均值应复现F。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(a)** 三组样本量均为5，均值为$3.508,9.274,24.926$克，总均值$12.5693333333$克。以组内、组间、总体为行，实际计算得到：
>
> | 变异来源 | 平方和SS | 自由度 | 均方MS | F | p值 |
> | --- | --- | --- | --- | --- | --- |
> | 组间 | 1228.270973333 | 2 | 614.135486667 | 110.429673255 | $1.87294675\times10^{-8}$ |
> | 组内 | 66.735920000 | 12 | 5.561326667 | — | — |
> | 总体 | 1295.006893333 | 14 | — | — | — |
>
> 组间SS加组内SS恰等总体SS（显示值有舍入）。F与p值使用经典独立正态同方差ANOVA参考分布，不把数据本身当作正态假设的证明。
>
> **(b)** 对任意数据，$y_{ij}-\bar{\bar y}=(y_{ij}-\bar y_i)+(\bar y_i-\bar{\bar y})$。平方后加总，交叉项为$2\sum_i(\bar y_i-\bar{\bar y})\sum_j(y_{ij}-\bar y_i)=0$。故
> $$
> \sum_{ij}(y_{ij}-\bar{\bar y})^2
> =\sum_{ij}(y_{ij}-\bar y_i)^2+\sum_i n_i(\bar y_i-\bar{\bar y})^2,
> $$
> 这是定理11.2.11的全部代数证明，不需概率或原假设。
>
> **(c)** 共用合并方差的三个无序成对$t^2$分别为$14.9455147992$（低−中）、$206.2146100631$（低−高）、$110.1288949040$（中−高）。有序对把每项计两次，故$\sum_{i,i'}t_{ii'}^2/[3(3-1)]=(14.9455147992+206.2146100631+110.1288949040)/3=110.4296732554=F$。这些数字与ANOVA表已在[[工具/StatisticalInference/ch11_numeric_checks.py|计算程序]]执行，完整输入与结果存于[[工具/StatisticalInference/ch11-numeric-results.json|记录]]。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=490|印刷第459页／PDF物理第490页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
