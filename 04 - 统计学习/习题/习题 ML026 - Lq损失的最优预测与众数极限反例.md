---
title: "习题 ML026：Lq损失的最优预测与众数极限反例"
topic: statistical-learning
topic_label: 统计学习
difficulty: intermediate
status: not-started
tags:
  - exercise
  - statistical-learning
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Deep Learning: Foundations and Concepts（DS003）]]"
source_id: DS003
source_chapter: 4
source_exercise: "4.12"
source_stars: 2
source_refs:
  - "DS003 Exercise 4.12，印刷130/PDF149"
  - "DS003 §4.2，式(4.40)及其后关于条件均值、中位数、众数的说明，印刷122/PDF141"
  - "DS004 Solution 4.12，式(124)–(126)及小指数解释，印刷47–48/PDF47–48"
source_status: verified
solution_status: independently-derived
created: 2026-11-02
---

# 习题 ML026：Lq损失的最优预测与众数极限反例

## 题目

### 英文原题

> [!question] 英文原题
> **Exercise 4.12（★★）** Consider the expected loss for regression problems under the $L_q$ loss function given by (4.40). Write down the condition that $y(\mathbf{x})$ must satisfy to minimize $\mathbb{E}[L_q]$. Show that, for $q=1$, this solution represents the conditional median, i.e., the function $y(\mathbf{x})$ such that the probability mass for $t<y(\mathbf{x})$ is the same as for $t\geq y(\mathbf{x})$. Also show that the minimum expected $L_q$ loss for $q\to0$ is given by the conditional mode, i.e., by the function $y(\mathbf{x})$ being equal to the value of $t$ that maximizes $p(t|\mathbf{x})$ for each $\mathbf{x}$.

### 中文转述

> [!question] 中文转述
> **原题4.12（★★）。** 考虑回归问题在式(4.40)的 $L_q$ 损失（$L_q$ loss）下的期望损失：
> $$
> \mathbb E[L_q]=\iint|f(\mathbf{x})-t|^q p(\mathbf{x},t)\,d\mathbf{x}\,dt.
> $$
> 写出预测函数 $y(\mathbf{x})$ 为最小化该期望损失所应满足的条件。证明 $q=1$ 时解是条件中位数（conditional median），也就是使 $t<y(\mathbf{x})$ 与 $t\ge y(\mathbf{x})$ 两部分概率质量相同的函数。还要证明：$q\to0$ 时最小期望损失由条件众数（conditional mode）给出，即对每个 $\mathbf{x}$，$y(\mathbf{x})$ 取使 $p(t|\mathbf{x})$ 最大的 $t$。

## 提示

> [!hint]- 提示 1
> 先固定输入 $\mathbf{x}$，最小化条件风险 $R_q(a)=\mathbb E[|a-T|^q\mid\mathbf{x}]$。对 $q>1$，求导后利用凸性；对 $q=1$，考虑左右导数。

> [!hint]- 提示 2
> 连续分布下，对固定 $a$，$|a-T|^q$ 在 $q\downarrow0$ 时几乎必然趋于1，不能只凭零点附近的形状判断最优位置。可以比较一个质量很小但密度很高的窄区间，与远处质量很大的宽区间。

## 解答

> [!success]- 解答
> **证明范围：独立推导与反例。** 证明最优条件和中位数结论；原题关于一般连续分布的众数极限不成立，以下给出排除整个众数邻域的解析反例。已核对原书及答案册的表述，没有把错误断言当作待证明事实。
>
> **条件风险与驻点。** 设 $q>0$，固定一个条件分布有定义的输入 $\mathbf{x}$，并假定 $\mathbb E[|T|^q\mid\mathbf{x}]<\infty$。本段略去条件记号。由条件分布分解，整体风险为各输入处 $R_q(y(\mathbf{x}))$ 的加权平均，因此在不限制预测函数类别时，应在 $p(\mathbf{x})$ 几乎处处逐点选择
> $$
> y(\mathbf{x})\in\arg\min_{a\in\mathbb R}R_q(a),\qquad
> R_q(a)=\int|a-t|^q p(t|\mathbf{x})\,dt.
> $$
> 此处假定所选预测规则可测。有限 $q$ 阶矩保证 $R_q$ 连续；又取 $M$ 使 $P(|T|\le M)>0$，则 $R_q(a)\ge P(|T|\le M)(|a|-M)^q\to\infty$，其中 $|a|>M$，故每个条件风险都有最小点。
>
> 当 $q>1$ 时，有限 $q$ 阶矩允许在积分内求导，得到
> $$
> R_q'(a)=q\mathbb E[\operatorname{sgn}(a-T)|a-T|^{q-1}].
> $$
> 因为 $|a-t|^q$ 对 $a$ 严格凸，以下条件既必要又充分，并确定唯一最优值：
> $$
> \int_{t<a}(a-t)^{q-1}p(t|\mathbf{x})\,dt
> =\int_{t>a}(t-a)^{q-1}p(t|\mathbf{x})\,dt.
> $$
> 特别地，$q=2$ 时化为 $a=\mathbb E[T\mid\mathbf{x}]$。
>
> 对 $0<q<1$，在可微且允许换序时同一等式只是必要的驻点条件，仍须比较全局风险，不能由导数为零推出极小值。例如，对 $C^1$ 紧支撑密度 $p$，先写 $R_q(a)=\int|u|^q p(a-u)\,du$，对密度求导，再分开 $u<0$、$u>0$ 分部积分，即得到上式导数；零点边界项因 $|u|^q\to0$ 消失。若存在原子或不满足求导条件，应直接最小化 $R_q$，不能强套普通驻点方程。
>
> **$q=1$：条件中位数。** 记条件分布函数为 $F$。绝对值的差商绝对值不超过1，因此可把左右导数移入期望，得到
> $$
> R'_{1,-}(a)=2F(a^-)-1,\qquad R'_{1,+}(a)=2F(a)-1.
> $$
> $R_1$ 凸，所以最小点恰满足
> $$
> F(a^-)\le\frac12\le F(a).
> $$
> 这正是中位数的定义。对于题目使用的条件密度，无原子且 $F$ 连续，于是 $F(a)=1/2$，两侧概率质量相等；中位数不一定唯一。如果推广到有原子的分布，必须保留上面的两个非严格不等号，而不能要求严格一半一半。
>
> **$q\downarrow0$：原题连续众数结论的反例。** 让条件分布不依赖输入，取 $h=1/100$ 及密度
> $$
> p(t)=\frac{1}{10}\frac{\mathbf1_{[-h,h]}(t)}{2h}
> +\frac9{10}\mathbf1_{[10,11]}(t).
> $$
> 两部分质量分别为 $1/10$、$9/10$，所以归一化。第一段密度为5，第二段为 $9/10$，故所有众数都在 $[-h,h]$。这是无原子的连续分布，密度本身不要求连续。
>
> 先考虑 $V\sim\mathrm{Unif}[-h,h]$。对于 $|a|\le h$，
> $$
> \mathbb E|a-V|^q
> =\frac{(h+a)^{q+1}+(h-a)^{q+1}}{2h(q+1)}
> \ge\frac{h^q}{q+1}.
> $$
> 因为 $q+1>1$，分子在 $a=0$ 处最小；区间外该期望随 $|a|$ 增大，所以这个下界对所有 $a$ 成立。于是对整个众数邻域 $|a|\le1/50$，远处分量还满足 $|a-t|\ge499/50$，从而
> $$
> R_q(a)\ge A(q):=\frac1{10}\frac{(1/100)^q}{q+1}
> +\frac9{10}\left(\frac{499}{50}\right)^q.
> $$
> 另一方面，在 $b=21/2$ 处，窄区间内的距离不超过 $1051/100$；宽区间以 $b$ 为中心，因此
> $$
> R_q(b)\le B(q):=\frac1{10}\left(\frac{1051}{100}\right)^q
> +\frac9{10}\frac{(1/2)^q}{q+1}.
> $$
> 将这两个显式函数延拓到 $q=0$，有 $A(0)=B(0)=1$，但
> $$
> A'(0)=\frac1{10}(\ln(1/100)-1)
> +\frac9{10}\ln(499/50)>\frac65>0,
> $$
> $$
> B'(0)=\frac1{10}\ln(1051/100)
> +\frac9{10}(\ln(1/2)-1)<-\frac35<0.
> $$
> 这些严格界只用了 $\ln(1/100)>-5$、$\ln(499/50)>2$、$\ln(1051/100)<3$ 与 $\ln(1/2)<0$。由导数定义，对所有足够小的正 $q$，有 $A(q)>1>B(q)$。所以
> $$
> R_q(a)>R_q(b)\quad\text{对所有 }|a|\le1/50\text{ 同时成立}.
> $$
> 因而小 $q$ 的全局最优预测不进入整个众数邻域，尤其不可能趋于任一众数。这反驳了原题及答案册对一般连续密度的结论；证明没有依赖有限数值抽查。
>
> **可以成立的众数结论。** 对有限离散状态的零一损失，条件风险为 $1-P(T=a\mid\mathbf{x})$，最优预测确为概率最大的原子。对有限离散分布及 $0<q<1$，风险在相邻原子间是凹函数，在支持区间外单调，所以最优值可在有限个原子上比较；这些有限风险在 $q\downarrow0$ 时分别趋于 $1-P(T=a)$，因此足够小的 $q$ 只会选最大质量原子。该论证依赖有限离散支持，不适用于本题的普通连续密度。

## 相关概念

- [[04 - 统计学习/概念/决策理论|决策理论]]：按条件期望损失选择预测。
- [[04 - 统计学习/概念/损失函数与经验风险|损失函数与经验风险]]：损失形状与全局风险。
- [[01 - 概率论/概念/条件概率|条件概率]]：条件分布与中位数条件。
- [[01 - 概率论/概念/期望|期望]]：条件风险的积分。
- [[03 - 线性代数与优化/概念/凸函数|凸函数]]：驻点条件何时充分。

## 备注

- 原题见 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=149|印刷130／PDF149]]；式(4.40)及正文相同众数断言见 [[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=141|印刷122／PDF141]]。英文原题和中文转述均保留该断言，修正未混入题面。
- 已实际读取 [[00 - 首页/教材归档/DS004 - Bishop 深度学习答案册|DS004]] 的印刷47–48／PDF47–48。其式(125)的驻点式需有求导条件；印刷48关于零点附近“凹口”选众数的说明忽略了整个条件分布的风险比较，上述反例说明该推论一般不成立。
- 密度连续与分布无原子是不同条件；反例是具有分段常数密度的无原子分布。题目未要求密度连续，故反例在其范围内。
- `source_status: verified` 仅指本题原文、所用正文与答案对照的实际核对范围，不代表全书论断已验证。独立解答不表示个人完成学习，状态保持 `not-started`。
