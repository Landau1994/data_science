---
title: "习题 P207：交换信封的离散先验与连续Jacobian修正"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第4章习题4.8，印刷页158／PDF物理页189"
source_id: "DS011"
source_chapter: 4
source_exercise: "4.8"
source_stars: 0
source_refs: ["DS011 Exercise 4.8，印刷158／PDF物理189", "DS011 所引正文，印刷166／PDF物理197", "DS011 所引正文，印刷167／PDF物理198", "DS011 所引正文，印刷83／PDF物理114"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P207：交换信封的离散先验与连续Jacobian修正

## 题目

### 英文原题

> [!question] 英文原题
> **4.8** Referring to Miscellanea 4.9.1:
> (a) Show that $P(X=m\mid M=m)=P(X=2m\mid M=m)=1/2$, and verify the expressions for $P(M=x\mid X=x)$ and $P(M=x/2\mid X=x)$.
> (b) Verify that one should trade only if $\pi(x/2)<2\pi(x)$, and if $\pi$ is the exponential$(\lambda)$ density, show that it is optimal to trade if $x<2\log2/\lambda$.
> (c) For the classical approach, show that $P(Y=2x\mid X=m)=1$ and $P(Y=x/2\mid X=2m)=1$ and that your expected winning if you trade or keep your envelope is $E(Y)=3m/2$.

### 中文转述

> [!question] 中文转述
> **原题4.8。**
> 参照杂录 4.9.1：
>
> (a)  证明 $P(X=m\mid M=m)=P(X=2m\mid M=m)=1/2$，并验证 $P(M=x\mid X=x)$ 和 $P(M=x/2\mid X=x)$ 的表达式.
>
> (b)  验证仅当 $\pi(x/2)<2\pi(x)$ 时应当交换；若 $\pi$ 是 $\operatorname{exponential}(\lambda)$ 密度，证明 $x<2\log2/\lambda$ 时交换最优.
>
> (c)  对经典方法，证明 $P(Y=2x\mid X=m)=1$ 和 $P(Y=x/2\mid X=2m)=1$；无论交换还是保留自己的信封，期望所得为 $E(Y)=3m/2$.

## 提示

> [!hint]- 提示
> 连续密度先验下，观察$X=2M$的分支带有尺度Jacobian；先区分概率质量和密度。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 杂录模型：小信封金额$M>0$，大信封为$2M$，独立公平随机分配；$X$是手中金额，$Y$是另一金额。(a) 给定$M=m$，$X=m,2m$各以$1/2$发生，因而两项条件概率成立。若$\pi$是离散质量函数，贝叶斯权重为$\pi(x)$与$\pi(x/2)$，原杂录后验正好为
> $$
> P(M=x\mid X=x)=\frac{\pi(x)}{\pi(x)+\pi(x/2)},\quad P(M=x/2\mid X=x)=\frac{\pi(x/2)}{\pi(x)+\pi(x/2)}.
> $$
> 但杂录明确称$\pi$为pdf。在连续模型下，两个观察分支的密度权重是$\pi(x)/2$与$\pi(x/2)/4$，故正确后验权重为$2\pi(x)/(2\pi(x)+\pi(x/2))$与$\pi(x/2)/(2\pi(x)+\pi(x/2))$，而不是上述质量函数公式。
> (b) 离散版本比较$2xq+(x/2)(1-q)$与$x$，等价于$\pi(x/2)<2\pi(x)$；形式代入指数函数给原阈值$2\log2/\lambda$，但把连续指数密度代入离散后验不成立。正确连续版本令$q=2\pi(x)/(2\pi(x)+\pi(x/2))$，则收益大于$x$当且仅当$q>1/3$，即$\pi(x/2)<4\pi(x)$。若$\pi(m)=\lambda e^{-\lambda m}$（率参数），阈值为$x<4\log2/\lambda$；等号时两策略等效。
> (c) 固定$m$时，$X=m$则另一封为$2m$；$X=2m$则另一封为$m$。原式中的$x$应随条件分别代为$m$与$2m$，不能保持一个同时不变的观察值。无条件地，换与不换都以$1/2$得到$m$或$2m$，期望均为$3m/2$。原文错误与连续模型修正已分开，未以错误公式作证明。 另需区分参数记号：本书§3.3式(3.3.11)（印刷83／PDF114）将exponential$(\lambda)$定义为尺度$\lambda$，而原题阈值按率参数写。在本书的尺度约定下，连续模型正确阈值应为$x<4\lambda\log2$；上述$4\log2/\lambda$仅适用于明确指定率为$\lambda$的另一记号。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=189|印刷第158页／PDF物理第189页]]；教材信息与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。原题无星号。
- 题内引用正文已核对：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=197|印刷166／PDF197]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=198|印刷167／PDF198]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=114|印刷83／PDF114]]。所需条件在解答重述，原文输入与独立补充分开。
- 原题及杂录的连续pdf后验漏掉尺度Jacobian；本题分别给出成立的离散解释与正确连续解释。未查阅题内外部文献。
- `source_status: verified`仅指本题题干、公式及所列来源定位已核对，不表示全章正文独立复证。解答写成不等于个人已完成练习，学习状态保持`not-started`；未实测Obsidian界面渲染。
