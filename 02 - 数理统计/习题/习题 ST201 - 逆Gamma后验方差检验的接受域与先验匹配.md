---
title: "习题 ST201：逆Gamma后验方差检验的接受域与先验匹配"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.11，印刷页327／PDF物理页358"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.11"
source_stars: 0
source_refs: ["DS011 Exercise 8.11，印刷页327／PDF物理页358", "DS011 所引正文，印刷290／PDF物理321"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST201：逆Gamma后验方差检验的接受域与先验匹配

## 题目

### 英文原题

> [!question] 英文原题
> **8.11** In Exercise 7.23 the posterior distribution of $\sigma^2$, the variance of a normal population, given $S^2$, the sample variance based on a sample of size $n$, was found using a conjugate prior for $\sigma^2$ (the inverted gamma pdf with parameters $\alpha$ and $\beta$). Based on observing $S^2$, a decision about the hypotheses $H_0:\sigma\le1$ versus $H_1:\sigma>1$ is to be made.
> (a) Find the region of the sample space for which $P(\sigma\le1\mid s^2)>P(\sigma>1\mid s^2)$, the region for which a Bayes test will decide that $\sigma\le1$.
> (b) Compare the region in part (a) with the acceptance region of an LRT. Is there any choice of prior parameters for which the regions agree?

### 中文转述

> [!question] 中文转述
> **原题8.11。**
> 习题7.23使用 $\sigma^2$ 的共轭先验（参数为 $\alpha,\beta$ 的逆伽马密度），求出了给定大小为 $n$ 的样本的样本方差 $S^2$ 后，正态总体方差 $\sigma^2$ 的后验分布. 现要根据观测到的 $S^2$，对假设 $H_0:\sigma\le1$ 与 $H_1:\sigma>1$ 作出决定.
>
> (a)  求样本空间中满足 $P(\sigma\le1\mid s^2)>P(\sigma>1\mid s^2)$ 的区域，即贝叶斯检验判定 $\sigma\le1$ 的区域.
>
> (b)  将(a) 的区域与似然比检验的接受域比较. 是否存在先验参数的选择，使两区域一致？

## 提示

> [!hint]- 提示
> 倒数方差的后验为Gamma，把后验一半阈值写成Gamma中位数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 取$n\ge2$，$\nu=n-1$。按习题7.23的密度，先验核为$(\sigma^2)^{-\alpha-1}e^{-1/(\beta\sigma^2)}$，$\alpha,\beta>0$。由于$\nu S^2/\sigma^2\sim\chi^2_\nu$，后验倒数$U=1/\sigma^2$为形状$A=\alpha+\nu/2$、率$B=1/\beta+\nu s^2/2$的Gamma。
> (a) 若$G_A$为尺度1 Gamma$(A,1)$的CDF，其唯一中位数为$m_A$，则$P(\sigma\le1\mid s^2)=P(U\ge1\mid s^2)=1-G_A(B)$。严格大于$1/2$等价于
> $$s^2<\frac{2(m_A-1/\beta)}\nu.$$
> 若右端非正，则正样本方差没有接受点；等号是后验平局。
> (b) 以$S^2$的抽样密度作似然，令$w=\sigma^2$，其核为$w^{-\nu/2}e^{-\nu s^2/(2w)}$。自由最大点$w=s^2$；$w\le1$下最大点$\min(s^2,1)$，故似然比在$s^2\le1$时为1，在$s^2>1$时为$[s^2e^{1-s^2}]^{\nu/2}$，后者严格递减。因此非平凡LRT接受域为$s^2<c$（端点约定不影响连续概率），其中$c>1$由所需大小决定；通常$c=\chi^2_{\nu,1-\alpha_0}/\nu$，这里$\chi^2_{\nu,1-\alpha_0}$明确表示CDF的$1-\alpha_0$分位数。
> 给定这样的$c$，选择足够大的$A>\nu/2$使$m_A>\nu c/2$，再令先验形状$\alpha=A-\nu/2$、$\beta=[m_A-\nu c/2]^{-1}$，即可使(a)阈值等于$c$。存在性来自Gamma中位数随形状趋无穷（例如均值$A$方差$A$及Chebyshev不等式即可证明）。若用原始正态样本连同未知均值作全样本LRT，剖面似然的指数为$n/2$、平顶界为$\nu s^2/n=1$；其非平凡拒绝域仍是样本方差上尾，先验阈值可用同一匹配方式比较。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=358|印刷327／PDF物理358]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 引用输入实际核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=321|印刷290／PDF物理321]]；解答已重述所需假设及结果。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
