---
title: "习题 P234：层次混合中的超二项与超Poisson方差"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第4章习题4.35，印刷页161／PDF物理页192"
source_id: "DS011"
source_chapter: 4
source_exercise: "4.35"
source_stars: 0
source_refs: ["DS011 Exercise 4.35，印刷161／PDF物理192", "DS011 所引正文，印刷137／PDF物理168", "DS011 所引正文，印刷138／PDF物理169"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P234：层次混合中的超二项与超Poisson方差

## 题目

### 英文原题

> [!question] 英文原题
> **4.35** (a) For the hierarchy in Example 4.4.6, show that the variance of $X$ can be written
> $$
> \operatorname{Var}X=nEP(1-EP)+n(n-1)\operatorname{Var}P.
> $$
> (The first term reflects binomial variation with success probability $EP$, and the second term is often called “extra-binomial” variation, showing how the hierarchical model has a variance that is larger than the binomial alone.)
> (b) For the hierarchy in Exercise 4.32, show that the variance of $Y$ can be written
> $$
> \operatorname{Var}Y=E\Lambda+\operatorname{Var}\Lambda=\mu+\frac1\alpha\mu^2,
> $$
> where $\mu=E\Lambda$. Identify the “extra-Poisson” variation induced by the hierarchy.

### 中文转述

> [!question] 中文转述
> **原题4.35。**
> (a)  对例4.4.6 的层次结构，证明 $X$ 的方差可写为
>
> $$
> \operatorname{Var}X=nEP(1-EP)+n(n-1)\operatorname{Var}P.
> $$
>
> 第一项反映成功概率为 $EP$ 的二项变异，第二项常称为“超二项”（extra-binomial）变异，表明分层模型的方差大于单纯二项模型的方差.
>
> (b)  对习题4.32 的层次结构，证明 $Y$ 的方差可写为
>
> $$
> \operatorname{Var}Y=E\Lambda+\operatorname{Var}\Lambda=\mu+\frac1\alpha\mu^2,
> $$
>
> 其中 $\mu=E\Lambda$. 指出层次结构引入的“超 Poisson”（extra-Poisson）变异.

## 提示

> [!hint]- 提示
> 将条件方差与条件均值的方差分开。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** (a) 令$m=EP,v=\operatorname{Var}P$。全方差给$nE[P(1-P)]+n^2v=n[m(1-m)-v]+n^2v=nm(1-m)+n(n-1)v$。若$P$为Beta，则$v=\alpha\beta/[(\alpha+\beta)^2(\alpha+\beta+1)]$。额外项非负；只有$n>1$且$v>0$时严格增加，不能把$n=1$等边界称为严格大于。
> (b) 对4.32(a)的Poisson–Gamma模型，$E(Y\mid\Lambda)=\Lambda$、$\operatorname{Var}(Y\mid\Lambda)=\Lambda$，所以$\operatorname{Var}Y=\mu+\alpha\beta^2=\mu+\mu^2/\alpha$，其中$\mu=\alpha\beta$。$\mu$是同均值Poisson的方差，$\mu^2/\alpha$是混合带来的额外变异。若使用4.32(b)三阶段稀疏模型，须把$\mu$改为$E(p\Lambda)$，不能仍取未稀疏化的$E\Lambda$。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=192|印刷第161页／PDF物理第192页]]；教材信息与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。原题无星号。
- 题内引用正文已核对：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=168|印刷137／PDF168]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=169|印刷138／PDF169]]。所需条件在解答重述，原文输入与独立补充分开。
- `source_status: verified`仅指本题题干、公式及所列来源定位已核对，不表示全章正文独立复证。解答写成不等于个人已完成练习，学习状态保持`not-started`；未实测Obsidian界面渲染。
