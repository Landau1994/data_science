---
title: 习题 ML053：快照PCA特征向量的归一化
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
source_exercise: '16.3'
source_stars: 1
source_refs:
- DS003 Exercise 16.3，印刷528/PDF542
- DS003 式(16.26)–(16.30)及数据矩阵定义，印刷505/PDF519
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML053：快照PCA特征向量的归一化

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 16.3（★）** Verify that the eigenvectors defined by (16.30) are normalized to unit length, assuming that the eigenvectors $\mathbf v_i$ have unit length.

### 中文转述

> [!question] 中文转述
> **原题16.3。** 假设Gram矩阵特征向量 $v_i$ 为单位向量，验证式(16.30)构造的原数据空间特征向量 $u_i$ 也为单位长度。

## 提示

> [!hint]- 提示 1
> 代入 $u_i=(N\lambda_i)^{-1/2}X^Tv_i$ 和 $XX^Tv_i=N\lambda_i v_i$。

## 解答

> [!success]- 解答
> **独立推导。** $X$ 为行向量已中心化的 $N\times D$ 数据矩阵。对正特征值 $\lambda_i>0$，设 $N^{-1}XX^Tv_i=\lambda_i v_i$、$v_i^Tv_i=1$，则
> $$u_i^Tu_i=\frac{v_i^TXX^Tv_i}{N\lambda_i}=\frac{N\lambda_i v_i^Tv_i}{N\lambda_i}=1.$$
> 同时 $N^{-1}X^TXu_i=\lambda_i u_i$，所以归一化后的向量确实是样本协方差的特征向量。若 $v_i,v_j$ 正交，则 $u_i^Tu_j=v_i^TXX^Tv_j/(N\sqrt{\lambda_i\lambda_j})=0$。
>
> 当 $\lambda_i=0$ 时，$\|X^Tv_i\|^2=0$，因此式(16.30)出现 $0/0$，不能生成单位向量。该公式只适用于正特征值；原空间零特征空间须另取正交基。

## 相关概念

- [[04 - 统计学习/概念/无监督学习|无监督学习]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=542|印刷528／PDF542]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
