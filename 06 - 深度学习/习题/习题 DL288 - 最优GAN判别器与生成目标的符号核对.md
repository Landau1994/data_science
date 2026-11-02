---
title: 习题 DL288：最优GAN判别器与生成目标的符号核对
topic: deep-learning
topic_label: 深度学习
difficulty: advanced
status: not-started
tags:
- exercise
- deep-learning
source: '[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]'
source_id: DS003
source_chapter: 17
source_exercise: '17.1'
source_stars: 3
source_refs:
- DS003 Exercise 17.1，印刷544/PDF557
- DS003 §17.1.1，式(17.5)–(17.6)及判别器最小化/生成器最大化约定，印刷535/PDF548
source_status: verified
solution_status: independently-derived
created: '2026-11-02'
---

# 习题 DL288：最优GAN判别器与生成目标的符号核对

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 17.1（★★★）** We would like the GAN error function (17.6) to have the property that, given sufficiently flexible neural networks, the stationary point is obtained when the generator distribution matches the true data distribution. In this exercise we prove this result for network models with infinite flexibility by optimizing over the full space of probability distributions $p_G(\mathbf x)$ and over the full space of functions $d(\mathbf x)$ corresponding to the generative and discriminative networks, respectively. Specifically, we assume that the discriminative model is optimized in an inner loop, giving rise to an effective outer loop error function for the generative model. First, show that, in the limit of an infinite number of data samples, the GAN error function (17.6) can be rewritten in the form
> $$
> E(p_G,d)=-\int p_{\mathrm{data}}(\mathbf x)\ln d(\mathbf x)\,\mathrm d\mathbf x-\int p_G(\mathbf x)\ln(1-d(\mathbf x))\,\mathrm d\mathbf x\tag{17.14}
> $$
> where $p_{\mathrm{data}}(\mathbf x)$ is the fixed distribution of real data points. Now consider a variational optimization over all functions $d(\mathbf x)$. Show that, for a fixed generative network, the solution for the discriminator $d(\mathbf x)$ that minimizes $E$ is given by
> $$
> d^*(\mathbf x)=\frac{p_{\mathrm{data}}(\mathbf x)}{p_{\mathrm{data}}(\mathbf x)+p_G(\mathbf x)}.\tag{17.15}
> $$
> Hence, show that the error function $E$ can be written as a function of the generator network $p_G(\mathbf x)$ in the form
> $$
> \begin{aligned}
> C(p_G)&=-\int p_{\mathrm{data}}(\mathbf x)\ln\left\{\frac{p_{\mathrm{data}}(\mathbf x)}{p_{\mathrm{data}}(\mathbf x)+p_G(\mathbf x)}\right\}\,\mathrm d\mathbf x\\
> &\quad-\int p_G(\mathbf x)\ln\left\{\frac{p_G(\mathbf x)}{p_{\mathrm{data}}(\mathbf x)+p_G(\mathbf x)}\right\}\,\mathrm d\mathbf x.\tag{17.16}
> \end{aligned}
> $$
> Now show that this can be rewritten in the form
> $$
> C(p_G)=-\ln(4)+\operatorname{KL}\left(p_{\mathrm{data}}\middle\|\frac{p_{\mathrm{data}}+p_G}{2}\right)+\operatorname{KL}\left(p_G\middle\|\frac{p_{\mathrm{data}}+p_G}{2}\right)\tag{17.17}
> $$
> where the Kullback–Leibler divergence $\operatorname{KL}(p\|q)$ is defined by (2.100). Finally, using the property that $\operatorname{KL}(p\|q)\geq0$ with equality if, and only if, $p(\mathbf x)=q(\mathbf x)$ for all $\mathbf x$, show that the minimum of $C(p_G)$ occurs when $p_G(\mathbf x)=p_{\mathrm{data}}(\mathbf x)$. Note that the sum of the two Kullback–Leibler divergence terms in (17.17) is known as the Jensen–Shannon divergence between $p_{\mathrm{data}}$ and $p_G$. Like the Kullback–Leibler divergence, this is a non-negative quantity that vanishes if, and only if, the two distributions are equal, but unlike the KL divergence, it is symmetric with respect to the two distributions.

### 中文转述

> [!question] 中文转述
> **原题17.1。** 希望GAN误差函数(17.6)在网络足够灵活时，使生成分布与真实数据分布匹配。本题在全部生成分布 $p_G$ 和全部判别函数 $d$ 上优化，先在内循环优化判别器，再得到生成器的外循环目标。
>
> 先证明无限数据下误差为(17.14)。对固定生成分布变分优化 $d$，证明最小化误差的判别器为(17.15)；将其代回得到生成目标(17.16)。再证明它可重写为(17.17)，并利用按(2.100)定义的KL散度非负、仅在两分布相同时为零这一性质，证明 $C(p_G)$ 在 $p_G=p_{\mathrm{data}}$ 时最小。两项KL之和称为Jensen–Shannon散度；它非负、仅在分布相同时为零，并且对两个分布对称。

## 提示

> [!hint]- 提示 1
> 固定输入位置，最小化 $-p\ln d-q\ln(1-d)$。区分 $p,q$ 都为正与只有一者为正的情形。

> [!hint]- 提示 2
> 代回后令 $m=(p+q)/2$，逐项展开对数；检查原式(17.16)与(17.17)在 $p=q$ 时的符号。

## 解答

> [!success]- 解答
> **证明范围：独立推导与原式符号修正。** 记 $p=p_{\mathrm{data}}$、$q=p_G$，二者相对于共同基准测度具有密度。按原书§17.1.1，判别器最小化负交叉熵 $E$，生成器最大化它。
>
> 式(17.6)的两项经验平均在相应可积条件下分别趋于 $-\mathrm E_p\ln d$ 与 $-\mathrm E_q\ln(1-d)$，得到(17.14)。对每个位置，若 $p,q>0$，
> $$
> \frac{\partial}{\partial d}[-p\ln d-q\ln(1-d)]=-\frac pd+\frac q{1-d},
> \quad\frac{\partial^2}{\partial d^2}=\frac p{d^2}+\frac q{(1-d)^2}>0.
> $$
> 故最小点为 $d^*=p/(p+q)$。若 $q=0<p$，最小点为 $d=1$；若 $p=0<q$，为 $d=0$；若两者都为零，函数值任意且不影响积分。有限sigmoid参数只能逼近端点，这是理想函数空间中的解。代入即得原式(17.16)。
>
> **原题(17.17)的符号不成立。** 令 $m=(p+q)/2$，因 $\ln\{p/(p+q)\}=\ln(p/m)-\ln2$，且两密度各积分为1，实际得到
> $$
> C(q)=\ln4-\operatorname{KL}(p\|m)-\operatorname{KL}(q\|m).
> $$
> 若定义 $\operatorname{JS}(p,q)=\tfrac12[\operatorname{KL}(p\|m)+\operatorname{KL}(q\|m)]$，则 $C=\ln4-2\operatorname{JS}$。两KL有限，因为 $m\geq p/2,q/2$；非负性给出 $C\leq\ln4$，等号当且仅当 $p=q$ 几乎处处。因此对应原题(17.14)负交叉熵约定的结论应是：生成器在 $q=p$ 时**最大化**最优判别器误差。
>
> 若改定义生成器要最小化的 $V=-C$，则 $V=-\ln4+\operatorname{KL}(p\|m)+\operatorname{KL}(q\|m)$，这才是原题(17.17)的右端。不能让(17.16)保留负号，同时把它与这个相反目标等同。直接检查 $p=q$ 时 $d^*=1/2$，(17.16)给出 $+\ln4$，而印出的(17.17)给出 $-\ln4$，已构成反例。
>
> 这说明理想分布空间博弈的全局均衡目标；不证明有限网络的交替梯度算法收敛，下一题给出不收敛的简单动力学。

## 相关概念

- [[06 - 深度学习/概念/生成对抗网络|生成对抗网络]]
- [[01 - 概率论/概念/相对熵|相对熵]]
- [[04 - 统计学习/概念/交叉熵|交叉熵]]

## 备注

- 原题及星数：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=557|印刷544／PDF557]]；题页及引用正文已实际查看原PDF图像，精确定位见 `source_refs`。
- 原题(17.16)到(17.17)整体符号翻转及“minimum”要求已照录，在解答中明确修正；两KL之和与带1/2系数的JS规范化也分别写明。不使用未覆盖第17章的本地答案册。
- `source_status: verified` 仅指本题及所列实际核对范围；解答独立推导，不构成用户已完成学习，状态保持 `not-started`。
