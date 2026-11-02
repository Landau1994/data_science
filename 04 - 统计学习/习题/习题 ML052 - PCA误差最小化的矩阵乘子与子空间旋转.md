---
title: 习题 ML052：PCA误差最小化的矩阵乘子与子空间旋转
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
source_exercise: '16.2'
source_stars: 2
source_refs:
- DS003 Exercise 16.2，印刷528/PDF542
- DS003 正交约束(16.7)，印刷499/PDF513；误差式(16.15)，印刷500/PDF514
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML052：PCA误差最小化的矩阵乘子与子空间旋转

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 16.2（★★）** Show that the minimum value of the PCA error measure $J$ given by (16.15) with respect to the $\mathbf u_i$, subject to the orthonormality constraints (16.7), is obtained when the $\mathbf u_i$ are eigenvectors of the data covariance matrix $\mathbf S$. To do this, introduce a matrix $\mathbf H$ of Lagrange multipliers, one for each constraint, so that the modified error measure, in matrix notation reads
> $$\widetilde J=\operatorname{Tr}\{\widehat{\mathbf U}^T\mathbf S\widehat{\mathbf U}\}+\operatorname{Tr}\{\mathbf H(\mathbf I-\widehat{\mathbf U}^T\widehat{\mathbf U})\}\tag{16.87}$$
> where $\widehat{\mathbf U}$ is a matrix of dimension $D\times(D-M)$ whose columns are given by $\mathbf u_i$. Now minimize $\widetilde J$ with respect to $\widehat{\mathbf U}$ and show that the solution satisfies $\mathbf S\widehat{\mathbf U}=\widehat{\mathbf U}\mathbf H$. Clearly, one possible solution is that the columns of $\widehat{\mathbf U}$ are eigenvectors of $\mathbf S$, in which case $\mathbf H$ is a diagonal matrix containing the corresponding eigenvalues. To obtain the general solution, show that $\mathbf H$ can be assumed to be a symmetric matrix, and by using its eigenvector expansion, show that the general solution to $\mathbf S\widehat{\mathbf U}=\widehat{\mathbf U}\mathbf H$ gives the same value for $\widetilde J$ as the specific solution in which the columns of $\widehat{\mathbf U}$ are the eigenvectors of $\mathbf S$. Because these solutions are all equivalent, it is convenient to choose the eigenvector solution.

### 中文转述

> [!question] 中文转述
> **原题16.2。** 在正交约束(16.7)下最小化PCA误差(16.15)。以舍弃方向组成 $D\times(D-M)$ 矩阵 $\widehat U$，引入乘子矩阵 $H$ 得到(16.87)。证明驻点满足 $S\widehat U=\widehat UH$；说明 $H$ 可取对称，再用其谱分解把一般驻点旋转成由 $S$ 的特征向量组成的解，目标值不变，从而可以选取特征向量形式的最优解。

## 提示

> [!hint]- 提示 1
> 反对称乘子与对称约束矩阵的迹乘积为零；令 $H=R\Lambda R^T$，考察 $\widehat UR$。

## 解答

> [!success]- 解答
> **独立推导。** 记 $r=D-M$。因 $I-\widehat U^T\widehat U$ 对称，$H$ 的反对称部分对迹无贡献，可令 $H=H^T$。对 $\widehat U$ 求导有 $2S\widehat U-2\widehat UH=0$；左乘 $\widehat U^T$ 还得 $H=\widehat U^TS\widehat U$，确实对称。
>
> 作谱分解 $H=R\Lambda R^T$，$R^TR=I$。令 $V=\widehat UR$，则 $V^TV=I$、$SV=V\Lambda$，所以其列为 $S$ 的正交特征向量。约束满足时乘子项为零，且
> $$\widetilde J=J=\operatorname{Tr}(\widehat U^TS\widehat U)=\operatorname{Tr}(H)=\operatorname{Tr}(\Lambda)=\operatorname{Tr}(V^TSV).$$
> 因此每个驻点子空间内的基旋转都不改变目标，可用特征基代表。但不同特征子空间的值并不全相等；原题“all equivalent”应限于同一子空间的正交基变换。
>
> 设 $S$ 特征值降序为 $\lambda_i$。任意可行 $\widehat U$ 下，令 $a_i=\|\widehat U^Tv_i\|^2$，则 $0\leq a_i\leq1,\sum a_i=r$，故 $J=\sum\lambda_i a_i\geq\sum_{i=M+1}^D\lambda_i$。取舍弃方向为最小的 $r$ 个特征值的特征向量达到下界，保留方向即前 $M$ 个。重特征值允许非唯一最优基／子空间，不影响最小误差。

## 相关概念

- [[04 - 统计学习/概念/无监督学习|无监督学习]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[03 - 线性代数与优化/概念/最优性条件|最优性条件]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=542|印刷528／PDF542]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- 区分同一驻点子空间的基旋转等价与不同驻点的目标值，未把所有驻点误判为全局最小。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
