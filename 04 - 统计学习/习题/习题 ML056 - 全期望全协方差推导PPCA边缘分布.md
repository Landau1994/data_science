---
title: 习题 ML056：全期望全协方差推导PPCA边缘分布
topic: statistical-learning
topic_label: 统计学习
difficulty: intermediate
status: not-started
tags:
- exercise
- statistical-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 16
source_exercise: '16.6'
source_stars: 2
source_refs:
- DS003 Exercise 16.6，印刷528/PDF542
- DS003 全期望／全方差(2.122)–(2.123)，印刷59/PDF79；模型(16.31)–(16.33)，印刷507/PDF521；边缘及矩(16.35)–(16.39)，印刷508/PDF522
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML056：全期望全协方差推导PPCA边缘分布

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 16.6（★★）** By making use of the results (2.122) and (2.123) for the mean and covariance of a general distribution, derive the result (16.35) for the marginal distribution $p(\mathbf x)$ in the probabilistic PCA model.

### 中文转述

> [!question] 中文转述
> **原题16.6。** 利用一般分布的全期望和全协方差公式(2.122)–(2.123)，推导PPCA的观测边缘高斯分布(16.35)。

## 提示

> [!hint]- 提示 1
> 分别求 $\mathrm E_Z[\mathrm E(X|Z)]$ 与 $\mathrm E_Z\operatorname{Cov}(X|Z)+\operatorname{Cov}_Z\mathrm E(X|Z)$；另解释高斯性。

## 解答

> [!success]- 解答
> **独立推导。** 模型为 $Z\sim\mathcal N(0,I_M)$，$X|Z\sim\mathcal N(WZ+\mu,\sigma^2I_D)$。全期望给
> $$\mathrm EX=\mathrm E_Z(WZ+\mu)=\mu.$$
> 对向量推广(2.123)，有
> $$\operatorname{Cov}X=\mathrm E_Z\operatorname{Cov}(X|Z)+\operatorname{Cov}_Z\mathrm E(X|Z)=\sigma^2I_D+W\operatorname{Cov}(Z)W^T=\sigma^2I_D+WW^T.$$
> 向量公式可逐分量由标量全方差用极化恢复，或把 $X-\mathrm EX=[X-\mathrm E(X|Z)]+[\mathrm E(X|Z)-\mathrm EX]$ 展开；交叉项条件期望为零。
>
> 均值和协方差本身不能判定任意分布高斯。此处可写 $X=WZ+\mu+\epsilon$，其中 $Z,\epsilon$ 独立高斯，因此拼接向量是联合高斯，仿射变换 $X$ 也是高斯。综上
> $$p(x)=\mathcal N(x|\mu,WW^T+\sigma^2I),$$
> 即(16.35)。$\sigma^2>0$ 保证边缘协方差正定。

## 相关概念

- [[04 - 统计学习/概念/无监督学习|无监督学习]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=542|印刷528／PDF542]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
