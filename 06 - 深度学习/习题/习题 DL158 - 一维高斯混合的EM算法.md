---
title: "习题 DL158：一维高斯混合的EM算法"
topic: deep-learning
topic_label: 深度学习
difficulty: advanced
status: not-started
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08 修订稿），Problem 17.7，印刷348／PDF物理362"
source_id: DS001
source_chapter: 17
source_exercise: "17.7"
source_refs: ["DS001 Problem 17.7*，印刷348/PDF362", "DS001 式17.3–17.4，印刷328/PDF342"]
source_status: verified
solution_status: independently-derived
created: 2026-10-28
---

# 习题 DL158：一维高斯混合的EM算法

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 17.7\*** Derive the EM algorithm for fitting the 1D mixture of Gaussians model with $N$ components. To do this, you need to (i) find an expression for the posterior distribution $Pr(z|x)$ over the latent variable $z\in\{1,2,\ldots,N\}$ for a data point $x$ and (ii) find an expression that updates the evidence lower bound given the posterior distributions for all of the data points. You will need to use Lagrange multipliers to ensure that the weights $\lambda_1,\ldots,\lambda_N$ of the Gaussians sum to one.

### 中文转述

> [!question] 中文转述
> 推导含 $N$ 个成分的一维高斯混合的EM算法：计算每个数据点的成分后验，构造并更新所有样本的证据下界；用拉格朗日乘子保证混合权重和为1。


## 提示

> [!hint]- 提示
> 先用当前参数计算责任度，再固定这些责任度最大化完全数据对数似然的期望。分别对权重、均值和方差求极值。

## 解答

> [!success]- 解答
> 设数据为 $x_1,\ldots,x_I$，模型为 $p_\theta(x,z=n)=\lambda_n\mathcal N(x;\mu_n,v_n)$，其中 $v_n=\sigma_n^2>0$。先从正权重、正方差的参数初始化。
>
> **E步。** 用当前参数 $\theta^{\mathrm{old}}$ 和贝叶斯公式，求责任度（responsibility）
> $$
> r_{in}=p_{\theta^{\mathrm{old}}}(z_i=n|x_i)=\frac{\lambda_n^{\mathrm{old}}\mathcal N(x_i;\mu_n^{\mathrm{old}},v_n^{\mathrm{old}})}{\sum_{m=1}^N\lambda_m^{\mathrm{old}}\mathcal N(x_i;\mu_m^{\mathrm{old}},v_m^{\mathrm{old}})}.
> $$
> 每行满足 $r_{in}\ge0$、$\sum_n r_{in}=1$。
>
> **下界。** 对任意这样的 $r$，Jensen不等式给出
> $$
> \begin{aligned}
> \ell(\theta)&=\sum_i\log\sum_n\lambda_n\mathcal N(x_i;\mu_n,v_n)\ge\mathcal L(r,\theta),\\
> \mathcal L(r,\theta)&=\sum_{i,n}r_{in}\left[\log\lambda_n-\frac12\log(2\pi v_n)-\frac{(x_i-\mu_n)^2}{2v_n}-\log r_{in}\right].
> \end{aligned}
> $$
> 在E步的后验 $r$ 下，$\mathcal L(r,\theta^{\mathrm{old}})=\ell(\theta^{\mathrm{old}})$。固定 $r$ 后，熵项 $-\sum r\log r$ 与新参数无关，M步最大化其余部分 $Q$。
>
> **M步权重。** 令 $N_n=\sum_i r_{in}$，则 $\sum_nN_n=I$。拉格朗日函数为 $\sum_nN_n\log\lambda_n+\eta(1-\sum_n\lambda_n)$。内部驻点满足 $N_n/\lambda_n=\eta$，加总得 $\eta=I$，所以
> $$
> \lambda_n^{\mathrm{new}}=\frac{N_n}{I}.
> $$
> $\log$ 的凹性保证这是权重子问题的全局最大值。
>
> **M步均值与方差。** 对 $N_n>0$，关于 $\mu_n$ 求导得 $\sum_i r_{in}(x_i-\mu_n)/v_n=0$，故
> $$
> \mu_n^{\mathrm{new}}=\frac{\sum_i r_{in}x_i}{N_n}.
> $$
> 再以此均值计算 $S_n=\sum_i r_{in}(x_i-\mu_n^{\mathrm{new}})^2$。方差部分为 $-\frac{N_n}{2}\log v_n-\frac{S_n}{2v_n}$，导数为 $-N_n/(2v_n)+S_n/(2v_n^2)$。当 $S_n>0$ 时唯一最大值为
> $$
> v_n^{\mathrm{new}}=\frac{S_n}{N_n}.
> $$
> 于是得到完整循环：后验责任度 $\to$ 上述权重、均值、方差更新 $\to$ 重新计算后验，直至指定停止准则。
>
> 在每次M步确实提高下界时，
> $$
> \ell(\theta^{\mathrm{new}})\ge\mathcal L(r,\theta^{\mathrm{new}})\ge\mathcal L(r,\theta^{\mathrm{old}})=\ell(\theta^{\mathrm{old}}).
> $$
> 它保证似然不下降，并不保证达到全局最大值。若 $N_n=0$，该成分参数不由本轮下界确定，应删除或重新初始化。若 $S_n=0$，最大化会推动 $v_n\downarrow0$；无约束高斯混合似然确有方差塌缩导致无上界的问题。实际可明确约束 $v_n\ge v_{\min}>0$，此时精确的方差更新为 $\max(v_{\min},S_n/N_n)$。这些是实现边界，不能把方差0写成合法密度参数。

## 相关概念

- [[05 - 概率模型与推断/概念/潜变量|潜变量]]：混合成分的隐含标签。
- [[05 - 概率模型与推断/概念/变分推断|变分推断]]：后验与证据下界。

## 备注

- 原题：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=362|印刷 348／PDF 362]]；教材记录见 [[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001]]。
- 题干、公式及所引原页已核对；解答为独立推导。
