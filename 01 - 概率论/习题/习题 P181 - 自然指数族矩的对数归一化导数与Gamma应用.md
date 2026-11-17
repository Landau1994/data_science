---
title: "习题 P181：自然指数族矩的对数归一化导数与Gamma应用"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第3章习题3.32，印刷页109／PDF物理页140"
source_id: "DS011"
source_chapter: 3
source_exercise: "3.32"
source_stars: 0
source_refs: ["DS011 Exercise 3.32，印刷109／PDF物理140", "DS011 定理3.4.2，印刷92／PDF物理123", "DS011 自然形式式(3.4.7)，印刷94／PDF物理125"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P181：自然指数族矩的对数归一化导数与Gamma应用

## 题目

### 英文原题

> [!question] 英文原题
> **3.32** (a) If an exponential family can be written in the form (3.4.7), show that the identities of Theorem 3.4.2 simplify to
> $$
> E(t_j(X))=-\frac\partial{\partial\eta_j}\log c^*(\eta),\qquad
> \operatorname{Var}(t_j(X))=-\frac{\partial^2}{\partial\eta_j^2}\log c^*(\eta).
> $$
> (b) Use this identity to calculate the mean and variance of a gamma$(a,b)$ random variable.

### 中文转述

> [!question] 中文转述
> **原题3.32。** (a)  若一个指数族可写成式3.4.7的形式，证明定理3.4.2中的恒等式简化为
>
> $$
> \begin{aligned}
> E(t_j(X))&=-\frac\partial{\partial\eta_j}\log c^*(\eta),\\
> \operatorname{Var}(t_j(X))&=-\frac{\partial^2}{\partial\eta_j^2}\log c^*(\eta).
> \end{aligned}
> $$
>
> (b)  用这个恒等式计算Gamma$(a,b)$随机变量的均值与方差.

## 提示

> [!hint]- 提示
> 自然参数对自身的导数为单位向量，二阶参数映射项消失。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **(a)** 设$f(x|\eta)=h(x)c^*(\eta)\exp[\sum_i\eta_it_i(x)]$，自然参数为可微内点并可交换两次求导。对$\eta_j$，$\partial_j w_i=\mathbf1_{i=j}$且二阶导数为0，代入定理3.4.2即得题设两式。也可直接对$\int f=1$求导两次：得分为$t_j+\partial_j\log c^*$，其均值0、平方均值为$-\partial_j^2\log c^*$。
>
> **(b)** Gamma$(a,b)$取$t=(\log x,x)$、$\eta_1=a-1>-1$、$\eta_2=-1/b<0$，则
> $$
> c^*(\eta)=\frac{(-\eta_2)^{\eta_1+1}}{\Gamma(\eta_1+1)}.
> $$
> 对$\eta_2$求导，$\partial_2\log c^*=(\eta_1+1)/\eta_2$、$\partial_2^2\log c^*=-(\eta_1+1)/\eta_2^2$。因为$t_2(X)=X$，得到$EX=ab$、$\operatorname{Var}X=ab^2$。固定$a$而让$\eta_2$变化的内点邻域上Gamma尾与原点幂均允许求导交换。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=140|印刷第109页／PDF物理第140页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 英文原文、中文转述与本库独立解答分别保留；所用正文实际核对位置列于`source_refs`。题内文献只保留原题引用，不表示已查阅原文献。`source_status: verified`只指本题及所列位置核对，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
