---
title: "习题 ST151：白血病人口计数模型的两种缺失拟合与实际EM"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.28，印刷页291／PDF物理页322"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.28"
source_stars: 0
source_refs: ["DS011 Exercise 7.28，印刷291／PDF物理322", "DS011 例7.2.17完全模型，印刷264／PDF物理295", "DS011 不完全似然及方程(7.2.16)，印刷265／PDF物理296", "DS011 人口缺失EM式(7.2.23)，印刷266／PDF物理297"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST151：白血病人口计数模型的两种缺失拟合与实际EM

## 题目

### 英文原题

> [!question] 英文原题
> **7.28** Use the model of Exercise 7.2.17 on the data in Table 7.4.2, adapted from Lange et al. (1994). These are leukemia counts, and the associated population, for a number of areas in New York state.
>
> (a) Fit the Poisson model to the data of Table 7.4.2, both to the full data set and an “incomplete” data set where we suppose that the first population count ($x_1=3,540$ is missing).
>
> **Table 7.4.2 Counts of leukemia cases**
>
> | Population | 3,540 | 3,560 | 3,739 | 2,784 | 2,571 | 2,729 | 3,952 | 993 | 1,908 |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | Number of Cases | 3 | 4 | 1 | 1 | 3 | 1 | 2 | 0 | 2 |
> | Population | 948 | 1,172 | 1,047 | 3,138 | 5,485 | 5,554 | 2,943 | 4,969 | 4,828 |
> | Number of Cases | 0 | 1 | 3 | 5 | 4 | 6 | 2 | 5 | 4 |
>
> (b) Suppose that instead of having an $x$ value missing, we actually have lost a leukemia count (assume that $y_1=3$ is missing). Use the EM algorithm to find the MLEs in this case, and compare your answers to those of part (a).

### 中文转述

> [!question] 中文转述
> **原题7.28。** 把习题7.2.17的模型用于表7.4.2的数据，数据改编自Lange等（1994）.这些是纽约州若干地区的白血病病例数及相应人口数.
>
> (a)  对表7.4.2的完整数据，以及假设首个人口数$x_1=3540$缺失的“不完全”数据，分别拟合Poisson模型.
>
> **表：白血病病例计数**
>
> | 人口数 | 3540 | 3560 | 3739 | 2784 | 2571 | 2729 | 3952 | 993 | 1908 |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | 病例数 | 3 | 4 | 1 | 1 | 3 | 1 | 2 | 0 | 2 |
> | 人口数 | 948 | 1172 | 1047 | 3138 | 5485 | 5554 | 2943 | 4969 | 4828 |
> | 病例数 | 0 | 1 | 3 | 5 | 4 | 6 | 2 | 5 | 4 |
>
> (b)  假设缺失的不是$x$值，而是一项白血病计数（设$y_1=3$缺失）.用EM算法求此时的MLE，并与(a)的答案比较.

## 提示

> [!hint]- 提示
> 两种缺失分别替换一个Poisson计数的条件期望；最后用直接剖面MLE核对。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 使用独立$X_i\sim\operatorname{Poisson}(\tau_i)$、$Y_i\sim\operatorname{Poisson}(\beta\tau_i)$模型；这是原题的统计拟合，不作病因或医疗判断。
>
> **(a)** 表中$X=55860,Y=47,X_-=52320,Y_-=44$。完全数据MLE为$\widehat\beta_F=47/55860=0.000841389187254$，$\widehat\tau_{i,F}=(x_i+y_i)/(1+\widehat\beta_F)$。缺$x_1$时，7.27的剖面推导给
> $$
> \widehat\beta_X=44/52320=0.000840978593272,\quad
> \widehat\tau_{1,X}=3/\widehat\beta_X=3567.27272727,
> $$
> 其余$\widehat\tau_{i,X}=(x_i+y_i)/(1+\widehat\beta_X)$。
>
> **(b)** 缺$y_1$时，条件期望为$E(Y_1\mid\text{观测},\beta^{(r)},\tau^{(r)})=\beta^{(r)}\tau_1^{(r)}$。每步将$y_1$替为该期望，然后用完全数据更新：
> $$
> \beta^{(r+1)}=\frac{\beta^{(r)}\tau_1^{(r)}+Y_-}{X},\quad
> \tau_1^{(r+1)}=\frac{x_1+\beta^{(r)}\tau_1^{(r)}}{1+\beta^{(r+1)}},\quad
> \tau_j^{(r+1)}=\frac{x_j+y_j}{1+\beta^{(r+1)}}\ (j\ge2).
> $$
> 直接剖面亦给$\widehat\beta_Y=Y_-/X_- =\widehat\beta_X$、$\widehat\tau_{1,Y}=x_1=3540$；其余与缺$x_1$的拟合相同。预测缺失病例均值$\widehat\beta_Yx_1=2.97706422018$。完整三组率如下（四舍五入）：
>
> | 单元 | 完全数据$\widehat\tau_F$ | 缺$x_1$的$\widehat\tau_X$ | 缺$y_1$的$\widehat\tau_Y$ |
> | --- | --- | --- | --- |
> | 1 | 3540.021464 | 3567.272727 | 3540.000000 |
> | 2 | 3561.003810 | 3561.005271 | 3561.005271 |
> | 3 | 3736.855850 | 3736.857383 | 3736.857383 |
> | 4 | 2782.658701 | 2782.659843 | 2782.659843 |
> | 5 | 2571.836085 | 2571.837140 | 2571.837140 |
> | 6 | 2727.704939 | 2727.706058 | 2727.706058 |
> | 7 | 3950.675944 | 3950.677565 | 3950.677565 |
> | 8 | 992.165203 | 992.165610 | 992.165610 |
> | 9 | 1908.394298 | 1908.395081 | 1908.395081 |
> | 10 | 947.203034 | 947.203422 | 947.203422 |
> | 11 | 1172.013880 | 1172.014361 | 1172.014361 |
> | 12 | 1049.117284 | 1049.117714 | 1049.117714 |
> | 13 | 3140.357737 | 3140.359025 | 3140.359025 |
> | 14 | 5484.385497 | 5484.387747 | 5484.387747 |
> | 15 | 5555.325809 | 5555.328088 | 5555.328088 |
> | 16 | 2942.524192 | 2942.525399 | 2942.525399 |
> | 17 | 4969.818448 | 4969.820487 | 4969.820487 |
> | 18 | 4827.937825 | 4827.939806 | 4827.939806 |
>
> 已实际执行[[工具/StatisticalInference/ch07_numeric_checks.py|EM与闭式交叉核验]]，初值$\beta^{(0)}=0.001,\tau_1^{(0)}=1000$，其余率从观测人口数开始；相对改变量阈值$10^{-12}$，上限100000步。缺$x_1$用24991步，最终$\beta\approx0.000840978593378$；缺$y_1$用10步，最终$\beta\approx0.000840978593272$。两者对数似然在$10^{-8}$浮点容差内不下降。完整环境、实际迭代数、端点似然和参数向量存于[[工具/StatisticalInference/ch07-numeric-results.json|运行结果]]。慢迭代是此初值与停止规则下的事实，不据此声称所有初值的速度或收敛性。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=322|印刷第291页／PDF物理第322页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 原题Exercise 7.2.17误称及括号位置照录；表7.4.2全部18组数字逐项对照原图。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
