---
title: 习题 ML070：PPCA混合模型与完全共享参数的概率图
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
source_exercise: '16.20'
source_stars: 2
source_refs:
- DS003 Exercise 16.20，印刷530/PDF544
- DS003 PPCA模型(16.31)–(16.36)，印刷507–508/PDF521–522；样本图16.8，印刷509/PDF523
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML070：PPCA混合模型与完全共享参数的概率图

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 16.20（★★）** Draw a directed probabilistic graphical model representing a discrete mixture of probabilistic PCA models in which each PCA model has its own values of $\mathbf W$, $\boldsymbol\mu$, and $\sigma^2$. Now draw a modified graph in which these parameter values are shared between the components of the mixture.

### 中文转述

> [!question] 中文转述
> **原题16.20。** 画离散PPCA混合模型的有向概率图，每个成分有各自的 $W,\mu,\sigma^2$；再画这些参数在成分间全部共享后的修改图。

## 提示

> [!hint]- 提示 1
> 引入选择成分的离散变量 $c_n$ 与标准高斯潜变量 $z_n$。

> [!hint]- 提示 2
> 若所有成分的三个参数全部相同，条件分布不再依赖成分标签。

## 解答

> [!success]- 解答
> **独立构图与分布验证。** 令 $c_n\sim\operatorname{Cat}(\pi)$、$z_n\sim\mathcal N(0,I_M)$ 独立，给定 $c_n=k,z_n$，
> $$x_n\sim\mathcal N(W_kz_n+\mu_k,\sigma_k^2I_D).$$
> 图(a)中 $c_n,z_n$ 都指向观测 $x_n$；矩形是固定模型参数，不是新增随机变量，外框表示独立样本。
>
> ![[附件/习题图/DS003/解答-16.20.png]]
>
> 其联合分布 $p(c,z,x)=\pi_c\mathcal N(z|0,I)\mathcal N(x|W_cz+\mu_c,\sigma_c^2I)$，边缘为
> $$p(x)=\sum_k\pi_k\mathcal N(x|\mu_k,W_kW_k^T+\sigma_k^2I).$$
> 在图(b)要求的**全部共享**条件下，$W_k=W,\mu_k=\mu,\sigma_k^2=\sigma^2$，条件密度不再依赖 $c$。故可从最小依赖图中删除 $c_n\to x_n$，$c_n$ 成为与观测无关的冗余变量。边缘退化为单一PPCA：
> $$p(x)=\left(\sum_k\pi_k\right)\mathcal N(x|\mu,WW^T+\sigma^2I)=\mathcal N(x|\mu,WW^T+\sigma^2I).$$
> 保留一条参数化后无效的 $c\to x$ 边仍可画成非最小DAG，但不能声称全部参数共享仍产生不同的PPCA成分。若只共享部分参数，未共享部分会使成分选择仍有效，那是另外的模型。

## 相关概念

- [[04 - 统计学习/概念/无监督学习|无监督学习]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=544|印刷530／PDF544]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- 两面板图按题目模型用TikZ新绘，tex/pdf/png均保存并实际目视核对。解释完全共享导致混合成分不可区分，不擅自添加成分专属先验。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
