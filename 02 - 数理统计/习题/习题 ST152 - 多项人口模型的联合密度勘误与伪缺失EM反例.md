---
title: "习题 ST152：多项人口模型的联合密度勘误与伪缺失EM反例"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.29，印刷页291–292／PDF物理页322,323"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.29"
source_stars: 0
source_refs: ["DS011 Exercise 7.29，印刷291–292／PDF物理322,323", "DS011 表7.4.2全部计数，印刷291／PDF物理322", "DS011 例7.2.17对比模型，印刷264／PDF物理295"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST152：多项人口模型的联合密度勘误与伪缺失EM反例

## 题目

### 英文原题

> [!question] 英文原题
> **7.29** An alternative to the model of Example 7.2.17 is the following, where we observe $(Y_i,X_i)$, $i=1,2,\ldots,n$ where $Y_i\sim\operatorname{Poisson}(m\beta\tau_i)$ and $(X_1,X_2,\ldots,X_n)\sim\operatorname{multinomial}(m;\boldsymbol\tau)$, where $\boldsymbol\tau=(\tau_1,\tau_2,\ldots,\tau_n)$ with $\sum_{i=1}^n\tau_i=1$. So here, for example, we assume that the population counts are multinomial allocations rather than Poisson counts. (Treat $m=\sum x_i$ as known.)
>
> (a) Show that the joint density of $\mathbf Y=(Y_1,Y_2,\ldots,Y_n)$ and $\mathbf X=(X_1,X_2,\ldots,X_n)$ is
> $$
> f(\mathbf y,\mathbf x\mid\beta,\boldsymbol\tau)=\prod_{i=1}^n\frac{e^{-m\beta\tau_i}(m\beta\tau_i)^{y_i}}{y_i!}\,m!\frac{\tau_i^{x_i}}{x_i!}.
> $$
> (b) If the complete data are observed, show that the MLEs are given by
> $$
> \widehat\beta=\frac{\sum_{i=1}^n y_i}{\sum_{i=1}^n x_i}\quad\text{and}\quad
> \widehat\tau_j=\frac{x_j+y_j}{\sum_{i=1}^n x_i+y_i},\qquad j=1,2,\ldots,n.
> $$
> (c) Suppose that $x_1$ is missing. Use the fact that $X_1\sim\operatorname{binomial}(m,t_1)$ to calculate the expected complete-data log likelihood. Show that the EM sequence is given by
> $$
> \widehat\beta^{(r+1)}=\frac{\sum_{i=1}^ny_i}{m\widehat\tau_1^{(r)}+\sum_{i=2}^nx_i}\quad\text{and}\quad
> \widehat\tau_j^{(r+1)}=\frac{x_j+y_j}{m\widehat\tau_1^{(r)}+\sum_{i=2}^nx_i+\sum_{i=1}^ny_i},\quad j=1,2,\ldots,n.
> $$
> (d) Use this model to find the MLEs for the data of Table 7.4.2, first assuming that you have all the data, then assuming that $x_1=3,540$ is missing.

### 中文转述

> [!question] 中文转述
> **原题7.29。** 例7.2.17模型的一个替代如下：观测$(Y_i,X_i)$，$i=1,2,\ldots,n$，其中$Y_i\sim\operatorname{Poisson}(m\beta\tau_i)$，而$(X_1,X_2,\ldots,X_n)\sim\operatorname{multinomial}(m;\boldsymbol\tau)$，$\boldsymbol\tau=(\tau_1,\tau_2,\ldots,\tau_n)$且$\sum_{i=1}^n\tau_i=1$.例如，这里假设人口计数是多项分配，而非Poisson计数.（把$m=\sum x_i$视为已知.）
>
> (a)  说明$\boldsymbol Y=(Y_1,Y_2,\ldots,Y_n)$与$\boldsymbol X=(X_1,X_2,\ldots,X_n)$的联合密度为
>
> $$
> f(\boldsymbol y,\boldsymbol x\mid\beta,\boldsymbol\tau)=\prod_{i=1}^n\frac{e^{-m\beta\tau_i}(m\beta\tau_i)^{y_i}}{y_i!}\,m!\frac{\tau_i^{x_i}}{x_i!}.
> $$
>
> (b)  若观测到完全数据，说明MLE为
>
> $$
> \widehat\beta=\frac{\sum_{i=1}^ny_i}{\sum_{i=1}^nx_i}\qquad\text{及}\qquad\widehat\tau_j=\frac{x_j+y_j}{\sum_{i=1}^nx_i+y_i},\quad j=1,2,\ldots,n.
> $$
>
> (c)  假设$x_1$缺失.利用$X_1\sim\operatorname{binomial}(m,t_1)$这一事实，计算期望完全数据对数似然.说明EM序列为
>
> $$
> \begin{aligned}
> \widehat\beta^{(r+1)}&=\frac{\sum_{i=1}^ny_i}{m\widehat\tau_1^{(r)}+\sum_{i=2}^nx_i},\\
> \widehat\tau_j^{(r+1)}&=\frac{x_j+y_j}{m\widehat\tau_1^{(r)}+\sum_{i=2}^nx_i+\sum_{i=1}^ny_i},\qquad j=1,2,\ldots,n.
> \end{aligned}
> $$
>
> (d)  用此模型求表7.4.2数据的MLE，先假设全部数据可用，再假设$x_1=3540$缺失.

## 提示

> [!hint]- 提示
> 固定多项总数使一个缺失格可以由其余格恢复；E步必须用条件分布。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 按原模型，$Y_i$之间及$\mathbf Y$与$\mathbf X$独立，$m>0$固定已知、$\tau_i\ge0,\sum\tau_i=1$。原题多处公式不能原样证明，以下分别保留问题并给正确结论。
>
> **(a)** 多项系数$m!$只能出现一次。正确联合pmf为
> $$
> f(\mathbf y,\mathbf x)=m!\prod_{i=1}^n
> \frac{e^{-m\beta\tau_i}(m\beta\tau_i)^{y_i}\tau_i^{x_i}}{y_i!x_i!},
> \quad\sum_i x_i=m.
> $$
> 原式按乘积作用范围会产生$(m!)^n$，相差常数$(m!)^{n-1}$，虽不改MLE，却不能是归一化联合密度。
>
> **(b)** 令$Y=\sum_i y_i$，对数似然参数项为$Y\log\beta-m\beta+\sum_i(x_i+y_i)\log\tau_i$。第一部分在$\widehat\beta=Y/m$全局最大；单纯形上的第二部分用Lagrange乘子或严格凹性得到
> $$
> \widehat\tau_j=\frac{x_j+y_j}{m+Y}=\frac{x_j+y_j}{\sum_i(x_i+y_i)}.
> $$
> 零单元对应$\tau_j=0$的闭边界。原(b)求和括号未完整覆盖$x_i+y_i$，须按此解释。
>
> **(c)** $m$已知且$x_2,\ldots,x_n$均被观测时，$X_1=m-\sum_{i\ge2}x_i$已经确定。因此其**条件分布是该确定值的点质量**，不是边际$\operatorname{binomial}(m,\tau_1)$。正确E步将缺失值替为这个确定值，完全与不完全似然相同，一次M步即得(b)，不需要原迭代。
>
> 显式反例：$n=2,m=10,x_2=7,\mathbf y=(1,2)$，则$x_1=3$；从$\tau_1^{(r)}=1/2$出发，原式给$\beta^{(r+1)}=3/12=1/4$，而正确值$3/10$。即便把已确定的$x_1=3$放回其分子，原式仍给$\sum_j\tau_j^{(r+1)}=13/15\ne1$；若不放回，则$j=1$分子仍含未定义的缺失值。故原(c)在原述模型下不成立，$t_1$也是$\tau_1$的误排。
>
> **(d)** 表7.4.2的18组数据完整列于[[02 - 数理统计/习题/习题 ST151 - 白血病人口计数模型的两种缺失拟合与实际EM|习题7.28]]；其$m=55860,Y=47$。所以两种“全观测/缺$x_1$”情况均有
> $$
> \widehat\beta=47/55860=0.000841389187254,\qquad
> \widehat{\boldsymbol\tau}=\frac1{55907}(3543,3564,3740,2785,2574,2730,3954,993,1910,948,1173,1050,3143,5489,5560,2945,4974,4832).
> $$
> 缺失$x_1=55860-52320=3540$被准确恢复，拟合不变。此向量已实际计算核对和为1，见[[工具/StatisticalInference/ch07_numeric_checks.py|核验程序]]及[[工具/StatisticalInference/ch07-numeric-results.json|结果]]。不对错误的“EM”运行后冒称为该模型MLE。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=322|印刷第291页／PDF物理第322页]]及[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=323|续页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 原(a)的重复m!、(b)求和范围、(c)的t1及缺失分子均原样保留；正确条件化与明确反例另放解答。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
