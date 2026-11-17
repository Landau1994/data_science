---
title: "习题 ST262：正态均值方差同时推断的两种Bonferroni集合"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第9章习题9.14，印刷页366、367／PDF物理页397、398"
source_id: "DS011"
source_chapter: 9
source_exercise: "9.14"
source_stars: 0
source_refs: ["DS011 Exercise 9.14，印刷366／PDF物理397"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST262：正态均值方差同时推断的两种Bonferroni集合

## 题目

### 英文原题

> [!question] 英文原题
> **9.14** Let $X_1,\ldots,X_n$ be iid $n(\mu,\sigma^2)$, where both parameters are unknown. Simultaneous inference on both $\mu$ and $\sigma$ can be made using the Bonferroni Inequality in a number of ways.
> (a) Using the Bonferroni Inequality, combine the two confidence sets
> $$
> \left\{\mu:\bar x-\frac{ks}{\sqrt n}\le\mu\le\bar x+\frac{ks}{\sqrt n}\right\}\quad\text{and}\quad
> \left\{\sigma^2:\frac{(n-1)s^2}{b}\le\sigma^2\le\frac{(n-1)s^2}{a}\right\}
> $$
> into one confidence set for $(\mu,\sigma)$. Show how to choose $a,b,$ and $k$ to make the simultaneous set a $1-\alpha$ confidence set.
> (b) Using the Bonferroni Inequality, combine the two confidence sets
> $$
> \left\{\mu:\bar x-\frac{k\sigma}{\sqrt n}\le\mu\le\bar x+\frac{k\sigma}{\sqrt n}\right\}\quad\text{and}\quad
> \left\{\sigma^2:\frac{(n-1)s^2}{b}\le\sigma^2\le\frac{(n-1)s^2}{a}\right\}
> $$
> into one confidence set for $(\mu,\sigma)$. Show how to choose $a,b,$ and $k$ to make the simultaneous set a $1-\alpha$ confidence set.
> (c) Compare the confidence sets in parts (a) and (b).

### 中文转述

> [!question] 中文转述
> **原题9.14。**
> 设$X_1,\ldots,X_n$独立同分布于$\mathrm n(\mu,\sigma^2)$，两个参数均未知. 可以用多种方式通过Bonferroni不等式对$\mu,\sigma$进行同时推断.
>
> (a) 利用Bonferroni不等式，将两个置信集
>
> $$
> \left\{\mu:\bar x-\frac{ks}{\sqrt n}\le\mu\le\bar x+\frac{ks}{\sqrt n}\right\}\quad\text{与}\quad\left\{\sigma^2:\frac{(n-1)s^2}b\le\sigma^2\le\frac{(n-1)s^2}a\right\}
> $$
>
> 合并为$(\mu,\sigma)$的一个置信集. 说明如何选择$a,b,k$，使该同时置信集为$1-\alpha$置信集.
>
> (b) 利用Bonferroni不等式，将两个置信集
>
> $$
> \left\{\mu:\bar x-\frac{k\sigma}{\sqrt n}\le\mu\le\bar x+\frac{k\sigma}{\sqrt n}\right\}\quad\text{与}\quad\left\{\sigma^2:\frac{(n-1)s^2}b\le\sigma^2\le\frac{(n-1)s^2}a\right\}
> $$
>
> 合并为$(\mu,\sigma)$的一个置信集. 说明如何选择$a,b,k$，使该同时置信集为$1-\alpha$置信集.
>
> (c)  比较(a)和(b)中的置信集.

## 提示

> [!hint]- 提示
> 将总错误预算拆成均值部分与方差部分；(a)均值用$t$枢轴，(b)保留未知$\sigma$在联合集合内时可用标准正态枢轴。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> 令$\nu=n-1$，$\beta_1+\beta_2=\alpha$，$\beta_i\ge0$。记$q_{\nu,u}$为卡方下侧$u$分位数。
> (a) 选$k=t_{\nu,\beta_1/2}$（上侧分位），$a=q_{\nu,\beta_2/2},b=q_{\nu,1-\beta_2/2}$。取两个条件的交集，分别失败概率为$\beta_1,\beta_2$，并集界给同时成功概率至少$1-\alpha$。在$(\mu,\sigma)$坐标中是矩形：$\mu$界固定，$\sigma$在相应平方根界之间。
> (b) 改取$k=z_{\beta_1/2}$，$a,b$同上。标准化均值为$Z=\sqrt n(\bar X-\mu)/\sigma$，与$\nu S^2/\sigma^2$独立，故除Bonferroni下界外，还有精确同时覆盖$(1-\beta_1)(1-\beta_2)=1-\alpha+\beta_1\beta_2$。若要求恰好$1-\alpha$，可改选$(1-\beta_1)(1-\beta_2)=1-\alpha$。集合的左右边界$\mu=\bar x\pm k\sigma/\sqrt n$随$\sigma$张开。
> (c) 同一误差分配下$t$分位一般大于$z$分位，但(b)半宽还随候选$\sigma$变化；当$z\sigma<ts$时(b)较窄，反之较宽，因此一般无全局包含关系。(a)的均值事件含$S$，不能直接套用上述独立概率乘法。

## 相关概念

- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=397|印刷366／PDF物理397]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=398|印刷367／PDF物理398]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
