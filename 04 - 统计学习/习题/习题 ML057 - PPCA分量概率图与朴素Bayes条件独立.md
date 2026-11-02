---
title: 习题 ML057：PPCA分量概率图与朴素Bayes条件独立
topic: statistical-learning
topic_label: 统计学习
difficulty: beginner
status: not-started
tags:
- exercise
- statistical-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 16
source_exercise: '16.7'
source_stars: 1
source_refs:
- DS003 Exercise 16.7，印刷528、529/PDF542、543
- DS003 条件高斯(16.32)及对朴素Bayes结构的正文说明，印刷507/PDF521；样本plate图16.8，印刷509/PDF523
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML057：PPCA分量概率图与朴素Bayes条件独立

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 16.7（★）** Draw a directed probabilistic graph for the probabilistic PCA model described in Section 16.2 in which the components of the observed variable $\mathbf x$ are shown explicitly as separate nodes. Hence, verify that the probabilistic PCA model has the same independence structure as the naive Bayes model discussed in Section 11.2.3.

### 中文转述

> [!question] 中文转述
> **原题16.7。** 为§16.2的PPCA画有向概率图，将观测向量 $\mathbf x$ 的各分量分别画为节点。由此验证其独立结构与§11.2.3讨论的朴素Bayes（naive Bayes）模型相同。

## 提示

> [!hint]- 提示 1
> 给定整个潜向量 $z$ 后，噪声协方差为 $\sigma^2I$，所以所有 $x_i$ 条件独立。

## 解答

> [!success]- 解答
> **独立构图与验证。** 以下图把整个连续潜向量 $z_n$ 作为一个父节点，灰色节点是分别画出的观测分量；外框表示 $N$ 个独立样本，固定参数省略。
>
> ![[附件/习题图/DS003/解答-16.7.png]]
>
> 设 $w_i^T$ 是 $W$ 的第 $i$ 行，则
> $$p(z,x)=\mathcal N(z|0,I)\prod_{i=1}^D\mathcal N(x_i|w_i^Tz+\mu_i,\sigma^2).$$
> 因此 $p(x|z)=\prod_i p(x_i|z)$，给定共同父节点 $z$，任意不相交观测子集条件独立。图中路径 $x_i\leftarrow z\rightarrow x_j$ 被条件 $z$ 阻断；未给定 $z$ 时通常相关，因为 $\operatorname{Cov}(X_i,X_j)=w_i^Tw_j$。
>
> 朴素Bayes的共同父节点通常为离散类别；PPCA这里为连续向量，但共同父节点给定后子节点相互独立的结构相同。可进一步把先验的 $z_j$ 分开，各自独立，且每个 $z_j$ 一般指向所有 $x_i$；题目只要求拆开观测分量，向量父节点已经完整表达所需结构。

## 相关概念

- [[04 - 统计学习/概念/无监督学习|无监督学习]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=542|印刷528、529／PDF542、543]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- 图由TikZ按模型新绘，源码／矢量PDF与PNG同名保存在附件/习题图/DS003，已编译并目视检查；不声称核对了§11.2.3的全部内容。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
