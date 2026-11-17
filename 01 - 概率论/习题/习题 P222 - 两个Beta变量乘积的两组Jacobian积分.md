---
title: "习题 P222：两个Beta变量乘积的两组Jacobian积分"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第4章习题4.23，印刷页160／PDF物理页191"
source_id: "DS011"
source_chapter: 4
source_exercise: "4.23"
source_stars: 0
source_refs: ["DS011 Exercise 4.23，印刷160／PDF物理191", "DS011 所引正文，印刷130／PDF物理161", "DS011 所引正文，印刷131／PDF物理162"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P222：两个Beta变量乘积的两组Jacobian积分

## 题目

### 英文原题

> [!question] 英文原题
> **4.23** For $X$ and $Y$ as in Example 4.3.3, find the distribution of $XY$ by making the transformations given in (a) and (b), and integrating out $V$.
> (a) $U=XY$, $V=Y$
> (b) $U=XY$, $V=X/Y$

### 中文转述

> [!question] 中文转述
> **原题4.23。**
> 设 $X,Y$ 如例4.3.3 所述，分别作 (a)、(b) 中的变换，并将 $V$ 积掉，求 $XY$ 的分布.
>
> (a)  $U=XY$，$V=Y$.
>
> (b)  $U=XY$，$V=X/Y$.

## 提示

> [!hint]- 提示
> 重述原例两个不同参数的Beta分布，再核两个支持区域。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 原例假定$X\sim\operatorname{Beta}(\alpha,\beta)$与$Y\sim\operatorname{Beta}(\alpha+\beta,\gamma)$独立，参数均正。令$K=\Gamma(\alpha+\beta+\gamma)/(\Gamma(\alpha)\Gamma(\beta)\Gamma(\gamma))$。
> (a) 逆变换$x=u/v,y=v$，Jacobian绝对值$1/v$，支持$0<u<v<1$。代入得
> $$
> f_{U,V}(u,v)=Ku^{\alpha-1}(v-u)^{\beta-1}(1-v)^{\gamma-1}.
> $$
> 置$v=u+(1-u)t$，对$v$从$u$到1积分得到$K B(\beta,\gamma)u^{\alpha-1}(1-u)^{\beta+\gamma-1}$，故$U\sim\operatorname{Beta}(\alpha,\beta+\gamma)$。
> (b) 逆变换$x=\sqrt{uv},y=\sqrt{u/v}$，绝对Jacobian$1/(2v)$，支持$0<u<1,u<v<1/u$。所以联合密度为
> $$
> \frac K{2v}(\sqrt{uv})^{\alpha-1}(1-\sqrt{uv})^{\beta-1}(\sqrt{u/v})^{\alpha+\beta-1}(1-\sqrt{u/v})^{\gamma-1}.
> $$
> 对$v$积分时置$t=\sqrt{u/v}$，$dv/(2v)=-dt/t$，积分界由$v=u,1/u$变为$t=1,u$，化简成(a)中同一积分。故两种变换给出相同Beta边缘密度；均在支持上为一一变换，未遗漏额外分支。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=191|印刷第160页／PDF物理第191页]]；教材信息与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。原题无星号。
- 题内引用正文已核对：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=161|印刷130／PDF161]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=162|印刷131／PDF162]]。所需条件在解答重述，原文输入与独立补充分开。
- `source_status: verified`仅指本题题干、公式及所列来源定位已核对，不表示全章正文独立复证。解答写成不等于个人已完成练习，学习状态保持`not-started`；未实测Obsidian界面渲染。
