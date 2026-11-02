---
title: 习题 ML063：由PPCA后验恢复最小二乘投影重构
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
source_exercise: '16.13'
source_stars: 2
source_refs:
- DS003 Exercise 16.13，印刷529/PDF543
- DS003 后验与M定义(16.42)–(16.43)，印刷509/PDF523；投影重构与极限(16.50)–(16.51)，印刷512/PDF526
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML063：由PPCA后验恢复最小二乘投影重构

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 16.13（★★）** Show that the optimal reconstruction of a data point under probabilistic PCA, according to the least-squares projection cost of conventional PCA, is given by
> $$\widetilde{\mathbf x}=\mathbf W_{\mathrm{ML}}(\mathbf W_{\mathrm{ML}}^T\mathbf W_{\mathrm{ML}})^{-1}\mathbf M\mathrm E[\mathbf z|\mathbf x].\tag{16.88}$$

### 中文转述

> [!question] 中文转述
> **原题16.13。** 证明，若按传统PCA的最小二乘投影误差定义最优重构，PPCA数据点可由(16.88)的后验均值变换得到。

## 提示

> [!hint]- 提示 1
> 后验均值满足 $M\mathrm E[z|x]=W_{\mathrm{ML}}^T(x-\mu)$；代入后辨认投影矩阵，并检查中心化。

## 解答

> [!success]- 解答
> **独立推导与中心化修正。** 设 $W=W_{\mathrm{ML}}$ 满列秩、$\mu=\bar x$，$M=W^TW+\sigma^2I$。后验均值 $m=M^{-1}W^T(x-\mu)$，故原式右端为
> $$W(W^TW)^{-1}Mm=W(W^TW)^{-1}W^T(x-\mu)=P_W(x-\mu).$$
> 对任意重构 $\mu+Wz$，最小化 $\|x-\mu-Wz\|^2$，正规方程为 $W^TWz=W^T(x-\mu)$，所以最优重构确实是
> $$\boxed{\widehat x=\mu+W(W^TW)^{-1}M\mathrm E[z|x]}.$$
> 由于投影误差与 $\operatorname{col}W$ 正交，该点唯一；在PPCA最大似然子空间中与传统PCA一致。后验均值产生的默认重构 $\mu+Wm$ 有噪声收缩，通常并非最小二乘投影；乘以 $(W^TW)^{-1}M$ 恰消除这种收缩。
>
> 原式(16.88)没有最后加回 $\mu$，因此其 $\widetilde x$ 应理解为**中心化后的重构**。若把它解释为原始未中心化数据的重构，式子缺少均值。例如 $x=\mu\ne0$ 时，原右端为零而正确重构为 $\mu$。

## 相关概念

- [[04 - 统计学习/概念/无监督学习|无监督学习]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[03 - 线性代数与优化/概念/正规方程|正规方程]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=543|印刷529／PDF543]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- 原式(16.88)完整照录，中心化约定／均值漏项在解答独立处理。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
