---
title: "习题 ST150：多Poisson率模型的完全缺失似然与EM收敛证明"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.27，印刷页291／PDF物理页322"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.27"
source_stars: 0
source_refs: ["DS011 Exercise 7.27，印刷291／PDF物理322", "DS011 例7.2.17与完全似然(7.2.11)–(7.2.12)，印刷264／PDF物理295", "DS011 不完全似然及方程(7.2.15)–(7.2.16)，印刷265／PDF物理296", "DS011 EM序列(7.2.23)，印刷266／PDF物理297"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST150：多Poisson率模型的完全缺失似然与EM收敛证明

## 题目

### 英文原题

> [!question] 英文原题
> **7.27** Refer to Exercise 7.2.17.
>
> (a) Show that the likelihood estimators from the complete-data likelihood (7.2.11) are given by (7.2.12).
>
> (b) Show that the limit of the EM sequence in (7.2.23) satisfies (7.2.16).
>
> (c) A direct solution of the original (incomplete-data) likelihood equations is possible. Show that the solution to (7.2.16) is given by
> $$
> \widehat\beta=\frac{\sum_{i=2}^n y_i}{\sum_{i=2}^n x_i},\quad,\quad\widehat\tau_1=\frac{y_1}{\widehat\beta},\quad,\quad\widehat\tau_j=\frac{x_j+y_j}{\widehat\beta+1},\quad j=2,3,\ldots,n,
> $$
> and that this is the limit of the EM sequence in (7.2.23).

### 中文转述

> [!question] 中文转述
> **原题7.27。** 参见习题7.2.17.
>
> (a)  说明完全数据似然式7.2.11所给的似然估计量为式7.2.12.
>
> (b)  说明式7.2.23中EM序列的极限满足式7.2.16.
>
> (c)  原始（不完全数据）似然方程可以直接求解.说明式7.2.16的解为
>
> $$
> \widehat\beta=\frac{\sum_{i=2}^ny_i}{\sum_{i=2}^nx_i},\qquad\widehat\tau_1=\frac{y_1}{\widehat\beta},\qquad\widehat\tau_j=\frac{x_j+y_j}{\widehat\beta+1},\quad j=2,3,\ldots,n,
> $$
>
> 并且它就是式7.2.23中EM序列的极限.

## 提示

> [!hint]- 提示
> 剖面化各单元率，再把EM的一维更新写成与固定点的差。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 原题所指为**例**7.2.17：各$X_i\sim\operatorname{Poisson}(\tau_i)$、$Y_i\sim\operatorname{Poisson}(\beta\tau_i)$，所有变量独立。令$X=\sum_i x_i,Y=\sum_i y_i,X_-=\sum_{i\ge2}x_i,Y_-=\sum_{i\ge2}y_i$。以下假定$X_-,Y_->0$，并在出现零单元时允许$\tau_i=0$这一自然闭边界。
>
> **(a)** 完全数据对数似然的参数项为$Y\log\beta+\sum_i(x_i+y_i)\log\tau_i-(1+\beta)\sum_i\tau_i$。对固定$\beta$，$\widehat\tau_i(\beta)=(x_i+y_i)/(1+\beta)$；代入后关于$\beta$为$Y\log\beta-(X+Y)\log(1+\beta)+C$，导数$(Y-X\beta)/[\beta(1+\beta)]$在$Y/X$前正后负。因此$\widehat\beta=Y/X$、$\widehat\tau_i=(x_i+y_i)/(1+\widehat\beta)$，是全局MLE。
>
> **(b)** 缺$x_1$时，独立性使$E(X_1\mid\text{已观测},\beta^{(r)},\tau^{(r)})=\tau_1^{(r)}$。故EM更新为
> $$
> \beta^{(r+1)}=\frac{Y}{\tau_1^{(r)}+X_-},\quad
> \tau_1^{(r+1)}=\frac{\tau_1^{(r)}+y_1}{1+\beta^{(r+1)}},\quad
> \tau_j^{(r+1)}=\frac{x_j+y_j}{1+\beta^{(r+1)}}\ (j\ge2).
> $$
> 若存在有限内点极限$(\beta,\tau)$，连续性给$\beta\sum_i\tau_i=Y$、$\beta\tau_1=y_1$、$(1+\beta)\tau_j=x_j+y_j$，正是(7.2.16)。
>
> **(c)** 不完全似然对$(\beta\tau_1)$的部分是$y_1\log(\beta\tau_1)-\beta\tau_1$，最大值在$\beta\tau_1=y_1$，而其余完整成对单元如(a)优化，得到
> $$
> \widehat\beta=Y_-/X_-,\quad\widehat\tau_1=y_1X_-/Y_-,\quad
> \widehat\tau_j=\frac{x_j+y_j}{1+Y_-/X_-}.
> $$
> 这也证明是全局最大点，而非只解得分方程。再令$a_r=\tau_1^{(r)}$、$a_*=y_1X_-/Y_-$、$B=X_-+Y$。更新化为$F(a)=(a+y_1)(a+X_-)/(a+B)$，并有精确恒等式
> $$
> F(a)-a_*=(a-a_*)\left(1-\frac{Y_-}{a+B}\right).
> $$
> 因$0<Y_-/(a+B)<1$，每步处在$a$与$a_*$之间。正初值序列因而单调有界；其极限代回$F(a)=a$只能是$a_*$。其余参数由连续更新式收敛到上述MLE，完成原题要求的收敛证明。零总数可能给边界或不可识别，须另论，不能无条件套比值。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=322|印刷第291页／PDF物理第322页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 原题Exercise 7.2.17误称与多余逗号照录；模型实际在例7.2.17。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
