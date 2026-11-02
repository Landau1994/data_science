---
title: 习题 DL318：扩散反向条件的一致性高斯KL
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags:
- exercise
- deep-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]'
source_id: DS003
source_chapter: 20
source_exercise: '20.11'
source_stars: 2
source_refs:
- DS003 Exercise 20.11，印刷605/PDF615
- DS003 §20.1.2，式(20.15)–(20.17)，印刷585/PDF595；§20.2，式(20.18)，印刷587/PDF597
- DS003 §20.2.3–20.2.4，式(20.32)–(20.39)，印刷590–592/PDF600–602
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 DL318：扩散反向条件的一致性高斯KL

## 题目

### 英文原题

> [!question] 英文原题
> **20.11 (★★)** By making use of (20.15) for the distribution $q(\mathbf z_{t-1}\mid\mathbf z_t,\mathbf x)$ and (20.18) for the distribution $p(\mathbf z_{t-1}\mid\mathbf z_t,\mathbf w)$, show that the Kullback–Leibler divergence appearing in the consistency terms in (20.32) is given by (20.33).

### 中文转述

> [!question] 中文转述
> **原题20.11。** 计算真实后向条件与模型高斯之间的KL，证明与参数有关的部分为均值差的平方损失(20.33)。

## 提示

> [!hint]- 提示
> 模型协方差固定为 $\beta_tI$；真实后向协方差为 $\sigma_t^2I$，通常不相等。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 取 $t\ge2$，两分布为 $q=\mathcal N(\mathbf m_t,\sigma_t^2I)$、$p=\mathcal N(\boldsymbol\mu(\mathbf z_t,\mathbf w,t),\beta_tI)$，尺度均正。由多元高斯对数比取期望，
> $$
> \operatorname{KL}(q\Vert p)=\frac{\|\mathbf m_t-\boldsymbol\mu\|^2}{2\beta_t}
> +\frac D2\left\{\frac{\sigma_t^2}{\beta_t}-1+\ln\frac{\beta_t}{\sigma_t^2}\right\}.
> $$
> 后一项不含可训练参数 $\mathbf w$，故可写成(20.33)的 $\|\mathbf m_t-\boldsymbol\mu\|^2/(2\beta_t)+\text{const}$。这是在方差日程固定、只学习均值时的结论；若学习协方差，后一项也会参与优化，不能丢弃。$t=1$ 的真实条件退化于已知数据，本式不应用于该点质量，而由单独重建项处理。

## 相关概念

- [[06 - 深度学习/概念/扩散模型|扩散模型]]
- [[01 - 概率论/概念/相对熵|相对熵]]
- [[04 - 统计学习/概念/损失函数与经验风险|损失函数与经验风险]]

## 备注

- 原题已实际对照[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=615|印刷605／PDF615]]；正文引用范围见 `source_refs`。
- 英文原题与中文转述分列，原文疑误另注；未使用配套答案册。`source_status: verified` 仅表示本题及所列公式的实际核对范围；解答写成不表示个人学习完成，状态保持 `not-started`。
