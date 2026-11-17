---
title: "习题 P179：借助指数族归一化导数求二项与Beta矩"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第3章习题3.30，印刷页109／PDF物理页140"
source_id: "DS011"
source_chapter: 3
source_exercise: "3.30"
source_stars: 0
source_refs: ["DS011 Exercise 3.30，印刷109／PDF物理140", "DS011 定理3.4.2与式(3.4.4)–(3.4.5)，印刷92／PDF物理123"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P179：借助指数族归一化导数求二项与Beta矩

## 题目

### 英文原题

> [!question] 英文原题
> **3.30** Use the identities of Theorem 3.4.2 to
>
> (a) calculate the variance of a binomial random variable.
>
> (b) calculate the mean and variance of a beta$(a,b)$ random variable.

### 中文转述

> [!question] 中文转述
> **原题3.30。** 使用定理3.4.2的恒等式：
>
> (a)  计算二项随机变量的方差.
>
> (b)  计算Beta$(a,b)$随机变量的均值和方差.

## 提示

> [!hint]- 提示
> 对T=X使用配分函数二阶对数导数；Beta需要明确构造含该统计量的倾斜族。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 定理3.4.2的可用形式为：在共同支持及可交换求导/积分条件下，$f_u=h(x)c(u)e^{uT(x)}$满足$E_uT=-(\log c)'$、$\operatorname{Var}_uT=-(\log c)''$。
>
> **(a)** 二项自然参数$u=\log[p/(1-p)]$，$c(u)=(1+e^u)^{-n}$、$T=X$。于是$EX=n e^u/(1+e^u)=np$，再求导得$\operatorname{Var}X=n e^u/(1+e^u)^2=np(1-p)$。
>
> **(b)** Beta本身的自然统计量是$\log X,\log(1-X)$，不能把它们错误替换成$X$。为实际使用定理而求$X$矩，固定$a,b>0$，构造独立补充的指数倾斜族
> $$
> f_u(x)=\frac{e^{ux}x^{a-1}(1-x)^{b-1}}{B(a,b)Z(u)},\quad
> Z(u)=\frac1{B(a,b)}\int_0^1e^{ux}x^{a-1}(1-x)^{b-1}dx.
> $$
> 因$0<x<1$，任意有限$u$邻域上各阶导数均可由可积Beta核控制，定理适用且$c(u)=1/Z(u)$。在$u=0$，$Z=1$、$Z'=B(a+1,b)/B(a,b)=a/(a+b)$、$Z''=a(a+1)/[(a+b)(a+b+1)]$。因此
> $$
> EX=(\log Z)'(0)=\frac a{a+b},\quad
> \operatorname{Var}X=(\log Z)''(0)=\frac{ab}{(a+b)^2(a+b+1)}.
> $$
> Beta函数比用$B(a,b)=\Gamma(a)\Gamma(b)/\Gamma(a+b)$与Gamma递推化简。辅助倾斜族是本库构造，不冒充原题正文中已经给出的族。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=140|印刷第109页／PDF物理第140页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；所用正文实际核对位置列于`source_refs`。题内文献只保留原题引用，不表示已查阅原文献。`source_status: verified`只指本题及所列位置核对，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
