---
title: "习题 ST157：二项互补群下的等变Bayes规则与无统一最优MSE"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.34，印刷页293／PDF物理页324"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.34"
source_stars: 0
source_refs: ["DS011 Exercise 7.34，印刷293／PDF物理324", "DS011 例6.4.1的二项互补变换群，印刷242／PDF物理273", "DS011 例7.2.14共轭后验均值，印刷263／PDF物理294", "DS011 例7.3.5风险比较，印刷269／PDF物理300"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST157：二项互补群下的等变Bayes规则与无统一最优MSE

## 题目

### 英文原题

> [!question] 英文原题
> **7.34** Let $X_1,\ldots,X_n$ be a random sample from a binomial$(n,p)$. We want to find equivariant point estimators of $p$ using the group described in Example 6.4.1.
>
> (a) Find the class of estimators that are equivariant with respect to this group.
>
> (b) Within the class of Bayes estimators of Example 7.2.14, find the estimators that are equivariant with respect to this group.
>
> (c) From the equivariant Bayes estimators of part (b), find the one with the smallest MSE.

### 中文转述

> [!question] 中文转述
> **原题7.34。** 设$X_1,\ldots,X_n$为来自$\operatorname{binomial}(n,p)$的随机样本.希望利用例6.4.1描述的群，寻找$p$的等变点估计量.
>
> (a)  求关于此群等变的估计量类.
>
> (b)  在例7.2.14的Bayes估计量类中，求关于此群等变的估计量.
>
> (c)  从(b)的等变Bayes估计量中，求MSE最小者.

## 提示

> [!hint]- 提示
> 先写互补等变方程，再比较参数端点与中点的风险。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 互补群把成功与失败交换：$g(x_1,\ldots,x_n)=(n-x_1,\ldots,n-x_n)$，对应$p\mapsto1-p$。原题每个$X_i$均为Binomial$(n,p)$，故总试验数$N=n^2$；若本意沿用例中的$n$个Bernoulli，只需把下文$N$改成$n$，不能默默混用。
>
> **(a)** 全部等变估计量恰满足$\delta(g\mathbf x)=1-\delta(\mathbf x)$。等价地$\delta=1/2+h$，其中$h(g\mathbf x)=-h(\mathbf x)$；在每个两点轨道任选一个值，互补点被确定，固定点必须取1/2。若只考虑充分总数$S=\sum_iX_i$，则写为$\delta(N-S)=1-\delta(S)$。
>
> **(b)** Beta先验均值规则为$\delta_{a,b}(S)=(S+a)/(N+a+b)$。把$S$换成$N-S$并与$1-\delta_{a,b}(S)$比较，等变充要条件是$a=b>0$，即对称Beta先验。
>
> **(c)** 一般不存在对所有$p$同时MSE最小的单一规则。对称族的风险为
> $$
> R_p(a)=\frac{Np(1-p)+a^2(1-2p)^2}{(N+2a)^2}.
> $$
> 在$p=0$，风险随$a$严格增加；在$p=1/2$，风险随$a$严格减少，故任何固定$a>0$都不能在这两处同时最优。固定但未知$p\ne1/2$时求导给最优$a_p=2p(1-p)/(1-2p)^2$（端点取$a\downarrow0$极限），$p=1/2$时最优在$a\to\infty$，均不是可用的参数无关统一选择。
>
> 若另外明确采用**最小最大风险**标准，对称族中$a=\sqrt N/2$给常数风险$1/[4(\sqrt N+1)^2]$，且它在该族最小最大：$a<\sqrt N/2$时最大风险在$p=1/2$，随$a$下降；$a>\sqrt N/2$时最大风险在端点，随$a$上升。因此原(c)只能在补充这样的标准后给单一答案；不能把minimax与逐参数最小MSE混为一谈。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=324|印刷第293页／PDF物理第324页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 原题Binomial(n,p)与例中的Bernoulli样本量有差别；(c)缺少单一最优的准则，解答给风险冲突及明确标记的minimax补充。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
