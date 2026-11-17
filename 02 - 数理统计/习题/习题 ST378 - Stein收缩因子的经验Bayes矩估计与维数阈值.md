---
title: "习题 ST378：Stein收缩因子的经验Bayes矩估计与维数阈值"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.24，印刷页459–460／PDF物理页490,491"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.24"
source_stars: 0
source_refs: ["DS011 Exercise 11.24，印刷459–460／PDF物理490,491", "DS011 杂录11.5.6 Stein规则与典范模型，印刷465／PDF物理496"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST378：Stein收缩因子的经验Bayes矩估计与维数阈值

## 题目

### 英文原题

> [!question] 英文原题
> **11.24** The form of the Stein estimator of Miscellanea 11.5.6 can be justified somewhat by an empirical Bayes argument given in Efron and Morris (1972), which can be quite useful in data analysis. Such an argument may have been known by Stein (1956), although he makes no mention of it. Let $X_i\sim n(\theta_i,1)$, $i=1,\ldots,p$, and $\theta_i$ be iid $n(0,\tau^2)$.
>
> (a) Show that the $X_i$s, marginally, are iid $n(0,\tau^2+1)$, hence, $\sum X_i^2/(\tau^2+1)\sim\chi_p^2$.
>
> (b) Using the marginal distribution, show that $E(1-((p-2)/\sum_{j=1}^pX_j^2))=\tau^2/(\tau^2+1)$ if $p\ge3$. Thus, the Stein estimator of Miscellanea 11.5.6 is an empirical Bayes version of the Bayes estimator $\delta_i^\pi(\mathbf X)=[\tau^2/(\tau^2+1)]X_i$.
>
> (c) Show that the argument fails if $p<3$ by showing that $E(1/Y)=\infty$ if $Y\sim\chi_p^2$ with $p<3$.

### 中文转述

> [!question] 中文转述
> **原题11.24。** 杂录11.5.6的Stein估计量形式，可以通过Efron和Morris（1972）给出的经验贝叶斯论证得到一定解释，该论证在数据分析中相当有用. Stein（1956）可能已经知道这样的论证，但未提及. 设$X_i\sim\mathrm n(\theta_i,1)$，$i=1,\ldots,p$，且$\theta_i$独立同分布于$\mathrm n(0,\tau^2)$.
>
> (a)  证明$X_i$的边缘分布独立同为$\mathrm n(0,\tau^2+1)$，从而$\sum X_i^2/(\tau^2+1)\sim\chi^2_p$.
>
> (b)  利用边缘分布，证明若$p\ge3$，则
>
> $$
> E\left(1-\frac{p-2}{\sum_{j=1}^pX_j^2}\right)=\frac{\tau^2}{\tau^2+1}.
> $$
>
> 因此，杂录11.5.6的Stein估计量是贝叶斯估计量$\delta_\pi^i(\boldsymbol X)=[\tau^2/(\tau^2+1)]X_i$的经验贝叶斯版本.
>
> (c)  证明：若$Y\sim\chi^2_p$且$p<3$，则$E(1/Y)=\infty$，从而说明$p<3$时该论证失效.

## 提示

> [!hint]- 提示
> 边际正态平方和是缩放卡方，关键是卡方的逆一阶矩。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 按层级模型理解：给定独立$\theta_i$，各$X_i\mid\theta_i\sim n(\theta_i,1)$条件独立。
>
> **(a)** 写$X_i=\theta_i+\epsilon_i$，$\epsilon_i\sim n(0,1)$与所有参数独立，则各和独立且为$n(0,1+\tau^2)$。所以$Q=\sum_iX_i^2=(1+\tau^2)V$，$V\sim\chi_p^2$。
>
> **(b)** 当$p>2$，用卡方Gamma积分
> $$
> EV^{-1}=\frac{\Gamma(p/2-1)}{2\Gamma(p/2)}=\frac1{p-2}.
> $$
> 于是$E[1-(p-2)/Q]=1-1/(1+\tau^2)=\tau^2/(1+\tau^2)$。正态后验均值本为该确定收缩因子乘$X_i$；用其数据无偏估计替代便产生Stein经验Bayes规则。因子自身可能为负，不能凭这个期望等式声称其每份数据都在$[0,1]$，也不在此重新证明Stein全风险优越性。
>
> **(c)** 卡方密度在0附近与$y^{p/2-1}$成正比，乘$1/y$后积分为$\int_0^\epsilon y^{p/2-2}dy$，仅当$p>2$有限。因此$p=1,2$时逆矩发散，(b)的计算不能用。特别$p=2$时形式上$p-2=0$，因子退化为1，不能把$0\times\infty$当作逆矩推导后得到目标；其均值1通常不等于$\tau^2/(1+\tau^2)$。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=490|印刷第459页／PDF物理第490页]]及[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=491|续页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
