---
title: "习题 ST388：儿童身高回归的ANOVA与决定系数"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.34，印刷页461／PDF物理页492"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.34"
source_stars: 0
source_refs: ["DS011 Exercise 11.34，印刷461／PDF物理492", "DS011 (11.3.36)及决定系数，印刷449–450／PDF物理480–481"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST388：儿童身高回归的ANOVA与决定系数

## 题目

### 英文原题

> [!question] 英文原题
> **11.34** (a) Illustrate the partitioning of the sum of squares for simple linear regression by calculating the regression ANOVA table for the following data. Parents are often interested in predicting the eventual heights of their children. The following is a portion of the data taken from a study that might have been suggested by Galton’s analysis.
>
> | | | | | | | | | |
> |---|---|---|---|---|---|---|---|---|
> | Height (inches) at age two ($x$) |39|30|32|34|35|36|36|30|
> | Height (inches) as an adult ($y$) |71|63|63|67|68|68|70|64|
>
> (b) Analytically establish the partitioning of the sum of squares for simple linear regression by verifying (11.3.36).
> (c) Prove that the two expressions for the regression sum of squares are, in fact, equal. That is, show that
> $$
> \sum_{i=1}^n(\widehat y_i-\bar y)^2=\frac{S_{xy}^2}{S_{xx}}.
> $$
> (d) Show that the coefficient of determination, $r^2$, given by
> $$
> r^2=\frac{\sum_{i=1}^n(\widehat y_i-\bar y)^2}{\sum_{i=1}^n(y_i-\bar y)^2},
> $$
> can be derived as either the square of the sample correlation coefficient of the $n$ pairs $(y_1,x_1),\ldots,(y_n,x_n)$ or of the $n$ pairs $(y_1,\widehat y_1),\ldots,(y_n,\widehat y_n)$.

### 中文转述

> [!question] 中文转述
> **原题11.34。** (a)  计算下列数据的回归ANOVA表，说明简单线性回归的平方和分解. 父母常希望预测孩子成年后的身高. 以下数据来自一项可能受到Galton分析启发的研究，是其中的一部分.
>
> | 两岁身高（英寸）（$x$） | 39 | 30 | 32 | 34 | 35 | 36 | 36 | 30 |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | 成年身高（英寸）（$y$） | 71 | 63 | 63 | 67 | 68 | 68 | 70 | 64 |
>
> (b)  验证式11.3.36，从解析上建立简单线性回归的平方和分解.
>
> (c)  证明回归平方和的两个表达式确实相等，即
>
> $$
> \sum_{i=1}^n(\hat y_i-\bar y)^2=\frac{S_{xy}^2}{S_{xx}}.
> $$
>
> (d)  证明决定系数
>
> $$
> r^2=\frac{\sum_{i=1}^n(\hat y_i-\bar y)^2}{\sum_{i=1}^n(y_i-\bar y)^2}
> $$
>
> 既可以推导为$n$对$(y_1,x_1),\ldots,(y_n,x_n)$的样本相关系数平方，也可以推导为$n$对$(y_1,\hat y_1),\ldots,(y_n,\hat y_n)$的样本相关系数平方.

## 提示

> [!hint]- 提示
> 由正规方程消去平方和分解的交叉项；再把拟合偏差写成斜率乘中心化预测变量。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> (a) 原表完整数据为$x=(39,30,32,34,35,36,36,30)$、$y=(71,63,63,67,68,68,70,64)$。实际计算$\bar x=34,\bar y=66.75,S_{xx}=70,S_{xy}=65,S_{yy}=67.5$。拟合线$\widehat y=35.1785714286+.9285714286x$，得到：
>
> | 来源 | 自由度 | 平方和 | 均方 | $F$ |
> |---|---:|---:|---:|---:|
> | 回归 |1|60.3571428571|60.3571428571|50.7|
> | 残差 |6|7.1428571429|1.1904761905| |
> | 总计 |7|67.5| | |
>
> 双侧零斜率检验$p=.0003860027$；$r^2=.8941798942$。数据与确定性结果保留于[[工具/StatisticalInference/ch11-numeric-results.json|第11章数值记录]]。
> (b) $y_i-\bar y=(y_i-\widehat y_i)+(\widehat y_i-\bar y)$。交叉项为$\sum\widehat\varepsilon_i(\widehat\alpha+\widehat\beta x_i-\bar y)=0$，因为带截距正规方程给$\sum\widehat\varepsilon_i=\sum x_i\widehat\varepsilon_i=0$。平方求和即(11.3.36)。
> (c) $\widehat y_i-\bar y=\widehat\beta(x_i-\bar x)$，所以回归平方和$\widehat\beta^2S_{xx}=S_{xy}^2/S_{xx}$。
> (d) $r_{xy}^2=S_{xy}^2/(S_{xx}S_{yy})$，由(c)即决定系数。又$\overline{\widehat y}=\bar y$、$\sum(y_i-\bar y)(\widehat y_i-\bar y)=\mathrm{SSR}$、$\sum(\widehat y_i-\bar y)^2=\mathrm{SSR}$，所以$r_{y,\widehat y}=\sqrt{\mathrm{SSR}/S_{yy}}\ge0$，平方同值。若$\mathrm{SSR}=0$则拟合值恒定，其相关系数未定义，虽然决定系数仍为0；若$S_{yy}=0$，决定系数本身也未定义。原(d)需排除这些退化。

## 相关概念

- [[03 - 线性代数与优化/概念/正规方程|正规方程]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=492|印刷461／PDF物理492]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
