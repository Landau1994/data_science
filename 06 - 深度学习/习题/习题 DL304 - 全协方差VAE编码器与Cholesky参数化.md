---
title: 习题 DL304：全协方差VAE编码器与Cholesky参数化
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags:
- exercise
- deep-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 19
source_exercise: '19.3'
source_stars: 2
source_refs:
- DS003 Exercise 19.3，印刷578/PDF589
- DS003 编码器式(19.13)，印刷573/PDF584
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 DL304：全协方差VAE编码器与Cholesky参数化

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 19.3（★★）** In this exercise we extend the diagonal covariance VAE encoder network (19.13) to one with a general covariance matrix. Consider a $K$-dimensional random vector drawn from a simple Gaussian:
> $$
> \boldsymbol\epsilon\sim\mathcal N(\mathbf z|\mathbf0,\mathbf I),\tag{19.22}
> $$
> which is then linearly transformed using the relation
> $$
> \mathbf z=\boldsymbol\mu+\mathbf L\boldsymbol\epsilon\tag{19.23}
> $$
> where $\mathbf L$ is a lower-triangular matrix (i.e., a $K\times K$ matrix with all elements above the leading diagonal being zero). Show that $\mathbf z$ has a distribution $\mathcal N(\mathbf z|\boldsymbol\mu,\boldsymbol\Sigma)$, and write down an expression for $\boldsymbol\Sigma$ in terms of $\mathbf L$. Explain why the diagonal elements of $\mathbf L$ must be non-negative. Describe how $\boldsymbol\mu$ and $\mathbf L$ can be expressed as the outputs of a neural network, and discuss suitable choices for output-unit activation functions.

### 中文转述

> [!question] 中文转述
> **原题19.3。** 将式(19.13)的对角协方差VAE编码器扩展为一般协方差。取(19.22)的 $K$ 维标准高斯随机向量，经下三角矩阵按(19.23)变换。证明结果为 $\mathcal N(\boldsymbol\mu,\boldsymbol\Sigma)$ 并求 $\boldsymbol\Sigma$；解释为何 $L$ 的对角元必须非负；说明网络如何输出均值和下三角矩阵，以及输出激活函数的选择。

## 提示

> [!hint]- 提示 1
> 计算仿射高斯的均值与协方差，注意是 $LL^T$。

> [!hint]- 提示 2
> 区分“任意生成协方差的三角因子”与“约定对角为正的唯一Cholesky因子”。

## 解答

> [!success]- 解答
> **独立推导。** 按题意将(19.22)理解为 $\epsilon\sim\mathcal N(0,I_K)$。任意 $v$ 下 $v^Tz=v^T\mu+(L^Tv)^T\epsilon$ 是一维高斯，因此 $z$ 为多元高斯。其矩为
> $$
> \mathrm Ez=\mu,\qquad\Sigma=\mathrm E[L\epsilon\epsilon^TL^T]=LL^T.
> $$
> 任意实下三角 $L$ 都产生半正定协方差，因为 $v^T\Sigma v=\|L^Tv\|^2\geq0$。非退化密度要求 $L$ 可逆，即每个对角元非零。
>
> **“对角元必须非负”是Cholesky规范化的选择，不是高斯生成的必要条件。** 例如 $L=-I$ 同样给 $\Sigma=I$。右乘任意对角符号矩阵 $S$ 不改变 $(LS)(LS)^T$，取对角正消除这种符号歧义。对于正定 $\Sigma$，其唯一Cholesky因子对角元严格为正；允许零仅对应退化情况及额外非唯一性。
>
> 网络以 $x$ 为输入，输出 $K$ 个均值和 $K(K+1)/2$ 个三角参数，共 $K+K(K+1)/2$ 个实数。均值和严格下三角元用线性输出；对角用 $L_{jj}=\exp(a_j)$ 或 $\operatorname{softplus}(a_j)+\delta$（固定 $\delta>0$ 保证数值下界）。上三角固定为零，不输出。于是采样 $z=\mu(x,\phi)+L(x,\phi)\epsilon$ 可对全部编码器参数反向传播。
>
> 若希望允许退化协方差，可用非负激活如平方，但零对角处不存在普通高斯密度，常规VAE的KL／熵公式不再适用，所以训练密度模型通常选严格正参数化。

## 相关概念

- [[06 - 深度学习/概念/VAE（变分自编码器）|VAE（变分自编码器）]]
- [[05 - 概率模型与推断/概念/变分推断|变分推断]]
- [[01 - 概率论/概念/期望|期望]]
- [[06 - 深度学习/概念/激活函数|激活函数]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=589|印刷578／PDF589]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- 原式(19.22)的高斯密度自变量印为 $\mathbf z$ 而非 $\boldsymbol\epsilon$，上面照录；对角非负的充分性、正定性与规范化要求分开说明。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
