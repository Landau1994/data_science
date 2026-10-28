---
title: "习题 ML009：Lasso与岭回归的贝叶斯解释"
topic: statistical-learning
topic_label: 统计学习
difficulty: advanced
status: not-started
tags:
  - exercise
  - statistical-learning
source: "[[00 - 首页/教材归档/DS013 - Introduction to Statistical Learning R|ISLR（DS013）]]"
source_id: DS013
source_chapter: 6
source_exercise: "6.7"
source_refs: ["DS013 第6章习题7(a)–(b)，印刷285/PDF296", "DS013 第6章习题7(c)–(e)，印刷286/PDF297"]
source_status: verified
solution_status: independently-derived
created: 2026-10-25
---

# 习题 ML009：Lasso与岭回归的贝叶斯解释

## 题目

### 英文原题

> [!question] 英文原题
> **7.** We will now derive the Bayesian connection to the lasso and ridge regression discussed in Section 6.2.2.
>
> (a) Suppose that $y_i=\beta_0+\sum_{j=1}^p x_{ij}\beta_j+\epsilon_i$ where $\epsilon_1,\ldots,\epsilon_n$ are independent and identically distributed from a $N(0,\sigma^2)$ distribution. Write out the likelihood for the data.
>
> (b) Assume the following prior for $\beta$: $\beta_1,\ldots,\beta_p$ are independent and identically distributed according to a double-exponential distribution with mean $0$ and common scale parameter $b$: i.e. $p(\beta)=\frac{1}{2b}\exp(-|\beta|/b)$. Write out the posterior for $\beta$ in this setting.
>
> (c) Argue that the lasso estimate is the mode for $\beta$ under this posterior distribution.
>
> (d) Now assume the following prior for $\beta$: $\beta_1,\ldots,\beta_p$ are independent and identically distributed according to a normal distribution with mean zero and variance $c$. Write out the posterior for $\beta$ in this setting.
>
> (e) Argue that the ridge regression estimate is both the mode and the mean for $\beta$ under this posterior distribution.

### 中文转述

> [!question] 中文转述
> **ISLR 第6章习题7。** 推导 §6.2.2 提到的 Lasso 和岭回归的贝叶斯联系。
>
> (a) 设 $y_i=\beta_0+\sum_{j=1}^p x_{ij}\beta_j+\epsilon_i$，误差 $\epsilon_1,\ldots,\epsilon_n$ 独立同分布于 $N(0,\sigma^2)$。写出数据的似然函数（likelihood）。
>
> (b) 假设斜率 $\beta_1,\ldots,\beta_p$ 独立同分布于均值为零、公共尺度为 $b$ 的双指数分布（double-exponential distribution），单个系数密度为 $p(\beta)=(2b)^{-1}\exp(-|\beta|/b)$。写出系数的后验分布（posterior distribution）。
>
> (c) 说明 Lasso 估计为何是该后验的众数（mode）。
>
> (d) 改设各斜率独立同分布于均值为零、方差为 $c$ 的正态分布，写出后验。
>
> (e) 说明岭回归估计为何同时是此后验的众数与均值（mean）。

## 提示

> [!hint]- 提示 1
> 用“似然乘先验”写出后验核，再取负对数。与系数无关的加法常数不影响众数。

> [!hint]- 提示 2
> 后验中残差平方和的系数是 $1/(2\sigma^2)$。乘以 $2\sigma^2$ 后比较教材的惩罚形式；高斯先验时再完成平方，才能证明后验均值等于众数。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 条件于固定设计矩阵 $X\in\mathbb R^{n\times p}$，假设 $\sigma^2>0$ 已知，先把截距 $\beta_0$ 当作固定值；$b>0$、$c>0$ 也是已知超参数。记 $\beta=(\beta_1,\ldots,\beta_p)^\top$、$r=y-\beta_0\mathbf1$。
>
> **(a) 似然。** 误差独立，所以
> $$
> L(\beta_0,\beta; y,X,\sigma^2)
> =(2\pi\sigma^2)^{-n/2}
> \exp\left[-\frac{1}{2\sigma^2}
> \sum_{i=1}^{n}\left(y_i-\beta_0-\sum_{j=1}^p x_{ij}\beta_j\right)^2\right].
> $$
> **(b) 双指数先验的后验。** 联合先验是各系数单变量密度的乘积：
> $$
> \pi_L(\beta)=(2b)^{-p}\exp\left(-\frac{\|\beta\|_1}{b}\right).
> $$
> 因而后验密度为
> $$
> \pi_L(\beta\mid y,X,\beta_0,\sigma^2,b)
> =Z_L^{-1}\exp\left(-\frac{\|r-X\beta\|_2^2}{2\sigma^2}
> -\frac{\|\beta\|_1}{b}\right),
> $$
> 其中 $Z_L$ 是对全部 $\beta\in\mathbb R^p$ 积分得到的正规化常数。这个常数有限且为正：似然核不超过1，且双指数先验可积；即使 $p>n$ 或 $X$ 秩不足，后验仍然适定。
>
> **(c) 众数与 Lasso。** 最大化后验等价于最小化负对数并乘以 $2\sigma^2$，即
> $$
> \min_\beta\left\{\|r-X\beta\|_2^2
> +\frac{2\sigma^2}{b}\|\beta\|_1\right\}.
> $$
> 这正是残差平方和约定下的 Lasso，权重为 $\lambda_L=2\sigma^2/b$。若设计列相关导致众数不唯一，Lasso 最优解集合与后验众数集合相同；这里没有断言 Lasso 等于后验均值。
>
> **(d) 高斯先验的后验。** 先验和后验核分别为
> $$
> \pi_R(\beta)=(2\pi c)^{-p/2}\exp\left(-\frac{\|\beta\|_2^2}{2c}\right),
> $$
> $$
> \pi_R(\beta\mid y,X,\beta_0,\sigma^2,c)
> \propto\exp\left(-\frac{\|r-X\beta\|_2^2}{2\sigma^2}
> -\frac{\|\beta\|_2^2}{2c}\right).
> $$
> 令
> $$
> A=\frac{X^\top X}{\sigma^2}+\frac{I_p}{c},\qquad
> m=A^{-1}\frac{X^\top r}{\sigma^2},\qquad V=A^{-1}.
> $$
> 对任意非零 $v$，$v^\top Av=\|Xv\|_2^2/\sigma^2+\|v\|_2^2/c>0$，所以 $A$ 正定。展开并完成平方得
> $$
> \frac{\|r-X\beta\|_2^2}{\sigma^2}+\frac{\|\beta\|_2^2}{c}
> =(\beta-m)^\top A(\beta-m)
> +\frac{r^\top r}{\sigma^2}-m^\top Am.
> $$
> 因此正规化后的后验是 $N_p(m,V)$。
>
> **(e) 均值与众数。** 正定高斯密度唯一最大于 $m$，且关于 $m$ 对称、积分的一阶偏移为零，故后验均值也是 $m$。将矩阵式改写为
> $$
> m=\left(X^\top X+\frac{\sigma^2}{c}I_p\right)^{-1}X^\top r,
> $$
> 它正是最小化 $\|r-X\beta\|_2^2+\lambda_R\|\beta\|_2^2$ 的岭回归估计，权重为 $\lambda_R=\sigma^2/c$。这个结论在秩不足及 $p>n$ 时仍成立，因为 $c$ 有限且为正。
>
> **截距的另一种处理。** 若截距也未知，可给 $\beta_0$ 平坦先验而只惩罚斜率，假设 $n\ge1$。对任意斜率，联合后验最优截距是 $\bar y-\bar x^\top\beta$，把 $X$ 和 $y$ 中心化后即可得到相同的斜率优化问题。平坦先验在截距方向的积分有限，因为似然对截距含正系数 $n/(2\sigma^2)$ 的二次项；结合适定的斜率先验，联合后验可以正规化。高斯斜率先验下，联合后验仍是适定高斯，因此截距与斜率的联合均值、联合众数一致。若再对 $\sigma^2$ 放先验并积分，则后验一般改变，不能不经推导继续使用同一个固定权重公式。

## 相关概念

- [[04 - 统计学习/概念/Lasso回归|Lasso回归]]：双指数先验对应绝对值惩罚。
- [[04 - 统计学习/概念/岭回归|岭回归]]：高斯先验对应平方惩罚。
- [[04 - 统计学习/概念/正则化|正则化]]：正则化权重依赖损失的归一化。
- [[02 - 数理统计/概念/参数估计|参数估计]]：后验众数与后验均值是不同的估计规则。
- [[05 - 概率模型与推断/概念/概率推断|概率推断]]：以似然和先验构造后验。
- [[03 - 线性代数与优化/概念/正规方程|正规方程]]：完成平方后的岭线性方程。
- [[04 - 统计学习/概念/高维回归|高维回归]]：适定先验下，秩不足也不妨碍这里的后验正规化。

## 备注

- 已逐句对照 [[附件/books/ISLR.pdf#page=296|印刷285／PDF物理296]] 的 (a)–(b) 与 [[附件/books/ISLR.pdf#page=297|印刷286／PDF物理297]] 的 (c)–(e) 原图。6.7 无星号，页边有黄色难题图标。
- 原文 (b) 用 $p(\beta)$ 写单个双指数密度，又以 $\beta$ 指代全部系数；英文保留该记号，解答用 $\pi_L(\beta)$ 明确表示联合密度。
- 题目没有规定截距先验及是否把噪声方差当作已知；解答先在固定截距、已知方差下给出完整结论，再说明平坦截距先验的处理。$b$ 是尺度，$c$ 是方差，两者不能混用。
- `source_status: verified` 仅覆盖原题核对；推导、适定性与截距边界均为独立补充，未声称核对书中答案。学习状态保持 `not-started`。
