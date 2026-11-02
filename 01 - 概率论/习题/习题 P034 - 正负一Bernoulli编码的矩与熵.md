---
title: 习题 P034：正负一Bernoulli编码的矩与熵
topic: probability-theory
topic_label: 概率论
difficulty: intermediate
status: not-started
tags:
- exercise
- probability-theory
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 3
source_exercise: '3.2'
source_stars: 2
source_refs:
- DS003 Exercise 3.2，印刷105/PDF124
- DS003 §3.1.1–3.1.2，式(3.2)、(3.9)，印刷66–67/PDF85–86
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 P034：正负一Bernoulli编码的矩与熵

## 题目

### 英文原题

> [!question] 英文原题
> **3.2 (★★)** The form of the Bernoulli distribution given by (3.2) is not symmetric between the two values of $x$. In some situations, it will be more convenient to use an equivalent formulation for which $x\in\{-1,1\}$, in which case the distribution can be written
> $$
> p(x\mid\mu)=\left(\frac{1-\mu}{2}\right)^{(1-x)/2}\left(\frac{1+\mu}{2}\right)^{(1+x)/2}\tag{3.195}
> $$
> where $\mu\in[-1,1]$. Show that the distribution (3.195) is normalized, and evaluate its mean, variance, and entropy.

### 中文转述

> [!question] 中文转述
> **原题3.2。** 将二元变量改用 $\{-1,1\}$ 对称编码，验证式(3.195)的归一化，计算均值、方差和熵。参数范围为 $[-1,1]$。

## 提示

> [!hint]- 提示
> 分别代入两个可能值；此时 $X^2=1$。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 由定义，$p_-=(1-\mu)/2$、$p_+=(1+\mu)/2$ 均非负且和为1，故归一化。均值及二阶矩为
> $$
> \mathrm EX=-p_-+p_+=\mu,\quad\mathrm EX^2=p_-+p_+=1,
> \quad\operatorname{var}X=1-\mu^2.
> $$
> 熵为
> $$
> \mathrm H(X)=-\frac{1-\mu}{2}\ln\frac{1-\mu}{2}-\frac{1+\mu}{2}\ln\frac{1+\mu}{2}.
> $$
> 端点仍用 $0\ln0=0$；$\mu=0$ 时均匀，熵为 $\ln2$。若 $B=(X+1)/2$，则 $B$ 的成功概率为 $(1+\mu)/2$，故这里的 $\mu$ 是对称编码的均值，并不是0／1编码中的成功概率。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=124|印刷105／PDF124]]；正文引用范围见 `source_refs`。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
