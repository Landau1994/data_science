---
title: "习题 P235：逐试验独立Beta混合与共享概率的差别"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第4章习题4.36，印刷页161／PDF物理页192"
source_id: "DS011"
source_chapter: 4
source_exercise: "4.36"
source_stars: 0
source_refs: ["DS011 Exercise 4.36，印刷161／PDF物理192", "DS011 所引正文，印刷137／PDF物理168", "DS011 所引正文，印刷138／PDF物理169"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P235：逐试验独立Beta混合与共享概率的差别

## 题目

### 英文原题

> [!question] 英文原题
> **4.36** One generalization of the Bernoulli trials hierarchy in Example 4.4.6 is to allow the success probability to vary from trial to trial, keeping the trials independent. A standard model for this situation is
> $$
> X_i\mid P_i\sim\operatorname{Bernoulli}(P_i),\quad i=1,\ldots,n,\qquad P_i\sim\operatorname{beta}(\alpha,\beta).
> $$
> This model might be appropriate, for example, if we are measuring the success of a drug on $n$ patients and, because the patients are different, we are reluctant to assume that the success probabilities are constant. (This can be thought of as an empirical Bayes model; see Miscellanea 7.5.6.)
> A random variable of interest is $Y=\sum_{i=1}^nX_i$, the total number of successes.
> (a) Show that $EY=n\alpha/(\alpha+\beta)$.
> (b) Show that $\operatorname{Var}Y=n\alpha\beta/(\alpha+\beta)^2$, and hence $Y$ has the same mean and variance as a binomial$(n,\alpha/(\alpha+\beta))$ random variable. What is the distribution of $Y$?
> (c) Suppose now that the model is
> $$
> X_i\mid P_i\sim\operatorname{binomial}(n_i,P_i),\quad i=1,\ldots,k,\qquad P_i\sim\operatorname{beta}(\alpha,\beta).
> $$
> Show that for $Y=\sum_{i=1}^kX_i$, $EY=\frac\alpha{\alpha+\beta}\sum_{i=1}^kn_i$ and $\operatorname{Var}Y=\sum_{i=1}^k\operatorname{Var}X_i$ where
> $$
> \operatorname{Var}X_i=n_i\frac{\alpha\beta(\alpha+\beta+n_i)}{(\alpha+\beta)^2(\alpha+\beta+1)}.
> $$

### 中文转述

> [!question] 中文转述
> **原题4.36。**
> 例4.4.6 中 Bernoulli 试验层次结构的一种推广，是允许成功概率随试验而变化，同时保持各次试验独立. 标准模型为
>
> $$
> \begin{aligned}X_i\mid P_i&\sim\operatorname{Bernoulli}(P_i),\qquad i=1,\ldots,n,\\P_i&\sim\operatorname{beta}(\alpha,\beta).\end{aligned}
> $$
>
> 例如，测量药物对 $n$ 名患者的疗效时，因为患者各不相同，不愿假定成功概率恒定，这个模型可能合适. 它可视为一种经验 Bayes 模型（empirical Bayes model），见杂录 7.5.6. 感兴趣的随机变量为总成功次数 $Y=\sum_{i=1}^nX_i$.
>
> (a)  证明 $EY=n\alpha/(\alpha+\beta)$.
>
> (b)  证明 $\operatorname{Var}Y=n\alpha\beta/(\alpha+\beta)^2$，因而 $Y$ 与 $\operatorname{binomial}(n,\alpha/(\alpha+\beta))$ 随机变量具有相同均值和方差. $Y$ 的分布是什么？
>
> (c)  现在假设模型为
>
> $$
> \begin{aligned}X_i\mid P_i&\sim\operatorname{binomial}(n_i,P_i),\qquad i=1,\ldots,k,\\P_i&\sim\operatorname{beta}(\alpha,\beta).\end{aligned}
> $$
>
> 证明对 $Y=\sum_{i=1}^kX_i$，有 $EY=\frac\alpha{\alpha+\beta}\sum_{i=1}^kn_i$，$\operatorname{Var}Y=\sum_{i=1}^k\operatorname{Var}X_i$，其中
>
> $$
> \operatorname{Var}X_i=n_i\frac{\alpha\beta(\alpha+\beta+n_i)}{(\alpha+\beta)^2(\alpha+\beta+1)}.
> $$

## 提示

> [!hint]- 提示
> 独立的是整组$(P_i,X_i)$；每次使用新的独立Beta变量。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 按原文“keeping the trials independent”明确采用$P_i$相互独立，且给定全部$P_i$后$X_i$条件独立并仅依赖自己的$P_i$。令$m=\alpha/(\alpha+\beta)$、$s=\alpha+\beta$。
> (a) $EX_i=EP_i=m$，所以$EY=nm$。(b) 每个$X_i$只有0和1两个取值，边缘成功概率$m$，故是Bernoulli$(m)$；联合概率积分按$i$分解，使它们边缘仍独立。于是$Y\sim\operatorname{Bin}(n,m)$，方差$nm(1-m)=n\alpha\beta/s^2$。这不是共享同一$P$的Beta二项混合。
> (c) 对每组，$EX_i=n_im$，全方差为$n_iE[P_i(1-P_i)]+n_i^2\operatorname{Var}P_i$。用$E[P_i(1-P_i)]=\alpha\beta/[s(s+1)]$和$\operatorname{Var}P_i=\alpha\beta/[s^2(s+1)]$，化为题列式。各组依然独立，所以均值与方差均可求和。若只给同Beta边缘而不规定$P_i$独立，则这些独立/方差求和结论不成立。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=192|印刷第161页／PDF物理第192页]]；教材信息与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。原题无星号。
- 题内引用正文已核对：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=168|印刷137／PDF168]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=169|印刷138／PDF169]]。所需条件在解答重述，原文输入与独立补充分开。
- `source_status: verified`仅指本题题干、公式及所列来源定位已核对，不表示全章正文独立复证。解答写成不等于个人已完成练习，学习状态保持`not-started`；未实测Obsidian界面渲染。
