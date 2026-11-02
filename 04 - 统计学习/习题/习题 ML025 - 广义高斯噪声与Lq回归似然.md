---
title: "习题 ML025：广义高斯噪声与Lq回归似然"
topic: statistical-learning
topic_label: 统计学习
difficulty: intermediate
status: not-started
tags: [exercise, statistical-learning]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]"
source_id: DS003
source_chapter: 4
source_exercise: "4.11"
source_stars: 2
source_refs:
  - "DS003 Exercise 4.11及式(4.66)–(4.69)，印刷130/PDF149"
  - "DS003 §4.2，式(4.40)，印刷122/PDF141"
  - "DS004 解答4.11，印刷47/PDF47"
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 ML025：广义高斯噪声与Lq回归似然

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 4.11（★★）** The following distribution
> $$
> p(x\mid\sigma^2,q)=\frac{q}{2(2\sigma^2)^{1/q}\Gamma(1/q)}\exp\left(-\frac{|x|^q}{2\sigma^2}\right)\tag{4.66}
> $$
> is a generalization of the univariate Gaussian distribution. Here $\Gamma(x)$ is the gamma function defined by
> $$
> \Gamma(x)=\int_{-\infty}^{\infty}u^{x-1}e^{-u}\,\mathrm du.\tag{4.67}
> $$
> Show that this distribution is normalized so that
> $$
> \int_{-\infty}^{\infty}p(x\mid\sigma^2,q)\,\mathrm dx=1\tag{4.68}
> $$
> and that it reduces to the Gaussian when $q=2$. Consider a regression model in which the target variable is given by $t=y(\mathbf x,\mathbf w)+\epsilon$ and $\epsilon$ is a random noise variable drawn from the distribution (4.66). Show that the log likelihood function over $\mathbf w$ and $\sigma^2$, for an observed data set of input vectors $\mathbf X=\{\mathbf x_1,\ldots,\mathbf x_N\}$ and corresponding target variables $\mathbf t=(t_1,\ldots,t_N)^{\mathsf T}$, is given by
> $$
> \ln p(\mathbf t\mid\mathbf X,\mathbf w,\sigma^2)
> =-\frac1{2\sigma^2}\sum_{n=1}^N|y(\mathbf x_n,\mathbf w)-t_n|^q-\frac Nq\ln(2\sigma^2)+\mathrm{const}\tag{4.69}
> $$
> where ‘const’ denotes terms independent of both $\mathbf w$ and $\sigma^2$. Note that, as a function of $\mathbf w$, this is the $L_q$ error function considered in Section 4.2.

### 中文转述

> [!question] 中文转述
> **原题4.11（★★）。** 式 (4.66) 是一元高斯分布的推广：
> $$
> p(x\mid\sigma^2,q)=\frac{q}{2(2\sigma^2)^{1/q}\Gamma(1/q)}\exp\left(-\frac{|x|^q}{2\sigma^2}\right).
> $$
> 题中用式 (4.67) 定义 Gamma 函数（gamma function）：$\Gamma(x)=\int_{-\infty}^{\infty}u^{x-1}e^{-u}\,\mathrm du$。证明该密度在全实轴上积分为1，并证明 $q=2$ 时退化为高斯分布。
>
> 再考虑回归模型 $t=y(\mathbf x,\mathbf w)+\epsilon$，噪声 $\epsilon$ 来自式 (4.66)。对于输入集 $\mathbf X=\{\mathbf x_1,\ldots,\mathbf x_N\}$ 和目标向量 $\mathbf t=(t_1,\ldots,t_N)^{\mathsf T}$，证明关于 $\mathbf w,\sigma^2$ 的对数似然是式 (4.69)：
> $$
> \ln p(\mathbf t\mid\mathbf X,\mathbf w,\sigma^2)
> =-\frac1{2\sigma^2}\sum_{n=1}^N|y(\mathbf x_n,\mathbf w)-t_n|^q-\frac Nq\ln(2\sigma^2)+\mathrm{const},
> $$
> 其中常数项不依赖 $\mathbf w$ 或 $\sigma^2$。注意其关于 $\mathbf w$ 的误差项对应§4.2的 $L_q$ 误差函数。

## 提示

> [!hint]- 提示 1
> 被积函数是偶函数。先把全轴积分化为正半轴积分，再令 $u=x^q/(2\sigma^2)$。检查原题 Gamma 积分的下限能否成立。

> [!hint]- 提示 2
> 给定输入后，每个目标的密度由噪声密度平移得到。独立样本的似然取乘积，再对归一化因子和残差指数分别取对数。

## 解答

> [!success]- 解答
> **证明范围：独立推导，修正原题的 Gamma 积分下限。** 取 $q>0$、$\sigma^2>0$。原式 (4.67) 的下限写为 $-\infty$；以下采用正确的实参数 Gamma 定义
> $$
> \Gamma(a)=\int_0^{\infty}u^{a-1}e^{-u}\,\mathrm du,\qquad a>0.
> $$
> 原积分在负半轴通常没有实数幂的定义，且即使有定义也受到 $e^{-u}$ 的指数增长影响，不能作为这里的归一化常数。英文原题和中文转述保留了原页的下限。
>
> **归一化。** 令 $c=2\sigma^2>0$。利用偶性和换元 $u=x^q/c$，有 $x=c^{1/q}u^{1/q}$、$\mathrm dx=c^{1/q}u^{1/q-1}\mathrm du/q$，所以
> $$
> \begin{aligned}
> I&=\int_{-\infty}^{\infty}\exp(-|x|^q/c)\,\mathrm dx\\
> &=2\int_0^{\infty}\exp(-x^q/c)\,\mathrm dx\\
> &=\frac{2c^{1/q}}q\int_0^{\infty}u^{1/q-1}e^{-u}\,\mathrm du\\
> &=\frac{2c^{1/q}}q\Gamma(1/q).
> \end{aligned}
> $$
> 它与式 (4.66) 的前因子互为倒数，故总积分为1。$q>0$ 同时保证正半轴换元合法和 Gamma 参数 $1/q>0$。
>
> **高斯特例。** 取 $q=2$，由 $\Gamma(1/2)=\sqrt\pi$，
> $$
> p(x\mid\sigma^2,2)=\frac1{\sqrt{2\pi\sigma^2}}\exp\left(-\frac{x^2}{2\sigma^2}\right)
> =\mathcal N(x\mid0,\sigma^2).
> $$
> 这里的 Gamma 半整数值也可由换元 $u=v^2$ 化为高斯积分：$\Gamma(1/2)=2\int_0^{\infty}e^{-v^2}\,\mathrm dv=\sqrt\pi$；最后一步所用的高斯积分已在[[01 - 概率论/习题/习题 P012 - 极坐标计算高斯归一化积分|原题2.12]]通过极坐标独立证明，取其中 $\sigma^2=1/2$ 即得。
>
> **回归对数似然。** 固定 $q$，假定给定输入后的噪声样本独立，且共享该分布的尺度参数。记 $r_n=t_n-y(\mathbf x_n,\mathbf w)$。平移的雅可比为1，因此
> $$
> p(t_n\mid\mathbf x_n,\mathbf w,\sigma^2,q)
> =\frac q{2(2\sigma^2)^{1/q}\Gamma(1/q)}\exp\left(-\frac{|r_n|^q}{2\sigma^2}\right).
> $$
> 取 $N$ 项乘积并取对数，得到
> $$
> \begin{aligned}
> \ln p(\mathbf t\mid\mathbf X,\mathbf w,\sigma^2,q)
> &=-\frac1{2\sigma^2}\sum_{n=1}^N|r_n|^q-\frac Nq\ln(2\sigma^2)\\
> &\quad+N\ln q-N\ln2-N\ln\Gamma(1/q).
> \end{aligned}
> $$
> 最后一行与 $\mathbf w,\sigma^2$ 无关，正是式 (4.69) 的常数项。固定 $\sigma^2,q$ 后，最大化似然等价于最小化 $\sum_n|r_n|^q$。若还要估计 $q$，则最后一行依赖 $q$，不能省略；若估计 $\sigma^2$，也不能省略 $-(N/q)\ln(2\sigma^2)$。
>
> **尺度和实际方差。** 对 $r>-1$，相同换元给出
> $$
> \mathrm E[|X|^r]=c^{r/q}\frac{\Gamma((r+1)/q)}{\Gamma(1/q)}.
> $$
> 密度对称且所有非负阶矩有限，因此均值为零，实际方差为
> $$
> \operatorname{var}(X)=(2\sigma^2)^{2/q}\frac{\Gamma(3/q)}{\Gamma(1/q)}.
> $$
> $q=2$ 时利用 $\Gamma(3/2)=\tfrac12\Gamma(1/2)$ 得到方差 $\sigma^2$，其中递推式 $\Gamma(a+1)=a\Gamma(a)$ 可对定义积分分部积分直接得到；但一般 $q$ 下，符号 $\sigma^2$ 只是尺度参数。例如 $q=1$ 对应尺度为 $2\sigma^2$ 的 Laplace 分布，方差为 $8\sigma^4$。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]：样本似然与参数相关的归一化项。
- [[04 - 统计学习/概念/损失函数与经验风险|损失函数与经验风险]]：负对数似然产生的 $L_q$ 损失。
- [[01 - 概率论/概念/期望|期望]]：广义高斯的绝对矩与实际方差。
- [[01 - 概率论/概念/概率模型|概率模型]]：条件噪声分布与独立样本假设。

## 备注

- 原题、星号及式 (4.66)–(4.69)：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=149|印刷130／PDF物理149]]；$L_q$ 风险式 (4.40)：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=141|印刷122／PDF物理141]]，均已查看原页。
- 原页式 (4.67) 的 Gamma 积分下限确实印作 $-\infty$。本笔记在原题中照录，在解答中明确修正为0，不改原PDF。密度还需 $q>0,\sigma^2>0$；一般形状参数下不能直接把 $\sigma^2$ 解释为方差。
- 已查看[[00 - 首页/教材归档/DS004 - Bishop 深度学习答案册|DS004]]印刷47／PDF47的4.11，其归一化换元使用正半轴，Gamma 定义的引用号仍显示“(??)”。本解答独立写全换元、固定参数范围、对数似然的常数及绝对矩；未据此声称核验整本答案册。
- `source_status: verified` 仅指本题及引用位置核对；独立解答不等于完成个人学习，状态保持 `not-started`。
