---
title: 习题 ML072：含缺失观测的PPCA联合潜变量EM
topic: statistical-learning
topic_label: 统计学习
difficulty: advanced
status: not-started
tags:
- exercise
- statistical-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 16
source_exercise: '16.22'
source_stars: 3
source_refs:
- DS003 Exercise 16.22，印刷530/PDF544
- DS003 模型(16.31)–(16.33)，印刷507/PDF521；后验(16.43)，印刷509/PDF523；§16.3.1 PPCA EM，印刷518–519/PDF532–533；缺失措辞及§16.3.2，印刷519–520/PDF533–534
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 ML072：含缺失观测的PPCA联合潜变量EM

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 16.22（★★★）** One benefit of a probabilistic formulation of principal component analysis is that it can be applied to a data set in which some of the values are missing, provided they are missing at random. Derive the EM algorithm for maximizing the likelihood function for the probabilistic PCA model in this situation. Note that the $\{\mathbf z_n\}$, as well as the missing data values that are components of the vectors $\{\mathbf x_n\}$, are now latent variables. Show that in the special case in which all the data values are observed, this reduces to the EM algorithm for probabilistic PCA derived in Section 16.3.2.

### 中文转述

> [!question] 中文转述
> **原题16.22。** 概率PCA可以用于某些数值随机缺失（missing at random）的数据集。把各潜向量 $\mathbf z_n$ 和观测向量 $\mathbf x_n$ 中缺失的分量都视为潜变量，推导最大化该情形似然的EM算法。证明当全部数据值均被观测到时，它退化为§16.3.2所推导的概率PCA EM算法。

## 提示

> [!hint]- 提示 1
> 先求 $p(z_n|x_{n,O})$，再利用 $x_{n,H}=\mu_H+W_Hz_n+\epsilon_H$ 得到完整数据所需的条件一阶、二阶矩。

> [!hint]- 提示 2
> 用增广潜向量 $u_n=(1,z_n^T)^T$ 将均值和载荷联合更新，避免把缺失数据的均值误写成已知完整样本均值。

## 解答

> [!success]- 解答
> **独立完整推导。** 模型为 $z_n\sim\mathcal N(0,I_M)$，$x_n=\mu+Wz_n+\epsilon_n$，$\epsilon_n\sim\mathcal N(0,vI_D)$，$v>0$。记各行已观测坐标为 $O_n$、缺失坐标为 $H_n$。忽略缺失机制需要其可忽略：例如MAR（给定已观测值后缺失不再依赖未观测值）且缺失机制与模型参数可分。正文把“missing at random”解释为不依赖任何观测／未观测值，实际上是更强的MCAR，足以满足这里条件。
>
> **E步。** 以下均用旧参数，省略下标 $n$。令
> $$G=(I+v^{-1}W_O^TW_O)^{-1},\quad m=Gv^{-1}W_O^T(x_O-\mu_O),\quad R=G+mm^T.$$
> 则 $z|x_O\sim\mathcal N(m,G)$。对缺失分量令 $a_H=\mu_H+W_Hm$。组成期望向量 $\bar x_n^*=\mathrm E[x_n|x_{n,O}]$，其观测部分就是 $x_O$、缺失部分为 $a_H$。为M步还须保留不确定性和交叉矩：
> $$\mathrm E[x_Hz^T|x_O]=\mu_Hm^T+W_HR,\qquad\mathrm E[x_Oz^T|x_O]=x_Om^T,$$
> $$\mathrm E[x_Hx_H^T|x_O]=vI+W_HGW_H^T+a_Ha_H^T,$$
> $$\mathrm E[x_Ox_H^T|x_O]=x_Oa_H^T,\qquad\mathrm E[x_Ox_O^T|x_O]=x_Ox_O^T.$$
> 这些式子来自独立噪声条件关系；不能只用缺失值的均值填补后当成确定数据，否则丢失协方差项。
>
> **M步。** 定义 $u_n=(1,z_n^T)^T$、$B=[\mu\ W]$，聚合
> $$V=\sum_n\begin{pmatrix}1&m_n^T\\m_n&R_n\end{pmatrix},\quad A=\sum_n\big[\mathrm E[x_n]\ \mathrm E[x_nz_n^T]\big],\quad T=\sum_n\mathrm E[x_nx_n^T].$$
> 所有期望均条件于已观测数据并使用旧参数。相关期望完整对数似然为
> $$Q(B,v)=\text{常数}-\frac{ND}2\ln v-\frac1{2v}\operatorname{Tr}(T-2BA^T+BVB^T).$$
> 因此当 $V$ 可逆时
> $$B_{\mathrm{new}}=AV^{-1},\qquad v_{\mathrm{new}}=\frac1{ND}\operatorname{Tr}(T-2B_{\mathrm{new}}A^T+B_{\mathrm{new}}VB_{\mathrm{new}}^T).$$
> 第一列给 $\mu_{\mathrm{new}}$，其余列给 $W_{\mathrm{new}}$。正噪声且至少一个样本时，$\mathrm E[u_nu_n^T]$ 正定，故 $V\succ0$。重复E/M步使可忽略机制下的观测对数似然不下降；EM通常只保证到驻点／边界，不保证全局最优。残差为零的噪声边界需单独处理。
>
> **无缺失的退化。** 若全部 $x_n$ 已知，$A,T$ 中观测矩不再需要填补，E步成为(16.66)–(16.67)。将完整数据均值初始化并保持为 $\mu=\bar x$，有 $\sum_nm_n=Gv^{-1}W^T\sum_n(x_n-\bar x)=0$，所以 $V$ 的常数／潜变量交叉块为零，$B$ 更新给 $\mu_{\mathrm{new}}=\bar x$ 及
> $$W_{\mathrm{new}}=\left[\sum_n(x_n-\bar x)m_n^T\right]\left[\sum_nR_n\right]^{-1}.$$
> 噪声更新展开为(16.69)，即标准PPCA EM。原题引用§16.3.2，该小节实际为零噪声PCA迭代；正噪声PPCA EM在§16.3.1。若再令 $v\to0$ 且相应矩满秩，才得到§16.3.2的(16.70)–(16.71)。

## 相关概念

- [[04 - 统计学习/概念/无监督学习|无监督学习]]
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]
- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/期望|期望]]
- [[05 - 概率模型与推断/概念/概率推断|概率推断]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=544|印刷530／PDF544]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- 原题对PPCA EM的小节号引用、正文MAR/MCAR术语范围分别说明；没有把EM内部估计或独立推导记作用户已完成学习。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
