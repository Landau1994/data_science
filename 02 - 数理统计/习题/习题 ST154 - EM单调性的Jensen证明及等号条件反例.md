---
title: "习题 ST154：EM单调性的Jensen证明及等号条件反例"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第7章习题7.31，印刷页292／PDF物理页323"
source_id: "DS011"
source_chapter: 7
source_exercise: "7.31"
source_stars: 0
source_refs: ["DS011 Exercise 7.31，印刷292／PDF物理323", "DS011 式(7.2.17)–(7.2.20)的条件密度与Q函数，印刷265／PDF物理296", "DS011 定理7.2.20及原等号表述，印刷266／PDF物理297"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST154：EM单调性的Jensen证明及等号条件反例

## 题目

### 英文原题

> [!question] 英文原题
> **7.31** Prove Theorem 7.2.20.
>
> (a) Show that, using (7.2.19), we can write
> $$
> \log L(\widehat\theta^{(r)}\mid\mathbf y)=E[\log L(\widehat\theta^{(r)}\mid\mathbf y,\mathbf X)\mid\widehat\theta^{(r)},\mathbf y]-E[\log k(\mathbf X\mid\widehat\theta^{(r)},\mathbf y)\mid\widehat\theta^{(r)},\mathbf y],
> $$
> and, since $\widehat\theta^{(r+1)}$ is a maximum, $[\log L(\widehat\theta^{(r+1)}\mid\mathbf y,\mathbf X)\mid\widehat\theta^{(r)},\mathbf y]\ge E[\log L(\widehat\theta^{(r)}\mid\mathbf y,\mathbf X)\mid\widehat\theta^{(r)},\mathbf y]$. When is the inequality an equality?
>
> (b) Now use Jensen’s inequality to show that $E[\log k(\mathbf X\mid\widehat\theta^{(r+1)},\mathbf y)\mid\widehat\theta^{(r)},\mathbf y]\le E[\log k(\mathbf X\mid\widehat\theta^{(r)},\mathbf y)\mid\widehat\theta^{(r)},\mathbf y]$, which together with part (a) proves the theorem.
>
> Hint: If $f$ and $g$ are densities, since $\log$ is a concave function, Jensen’s inequality (4.7.7) implies
> $$
> \int\log\left(\frac{f(x)}{g(x)}\right)g(x)dx\le\log\left(\int\frac{f(x)}{g(x)}g(x)dx\right)=\log\left(\int f(x)dx\right)=0.
> $$
> By the property of logs, this in turn implies that $\int\log[f(x)]g(x)dx\le\int\log[g(x)]g(x)dx$.

### 中文转述

> [!question] 中文转述
> **原题7.31。** 证明定理7.2.20.
>
> (a)  说明，利用式7.2.19，可以写成
>
> $$
> \begin{aligned}
> \log L(\widehat\theta^{(r)}\mid\boldsymbol y)
> &=E[\log L(\widehat\theta^{(r)}\mid\boldsymbol y,\boldsymbol X)\mid\widehat\theta^{(r)},\boldsymbol y]\\
> &\quad-E[\log k(\boldsymbol X\mid\widehat\theta^{(r)},\boldsymbol y)\mid\widehat\theta^{(r)},\boldsymbol y],
> \end{aligned}
> $$
>
> 而由于$\widehat\theta^{(r+1)}$是极大值点，有
>
> $$
> \begin{aligned}
> &[\log L(\widehat\theta^{(r+1)}\mid\boldsymbol y,\boldsymbol X)\mid\widehat\theta^{(r)},\boldsymbol y]\\
> &\qquad\ge E[\log L(\widehat\theta^{(r)}\mid\boldsymbol y,\boldsymbol X)\mid\widehat\theta^{(r)},\boldsymbol y].
> \end{aligned}
> $$
>
> 何时不等式取等号？
>
> (b)  用Jensen不等式说明
>
> $$
> \begin{aligned}
> &E[\log k(\boldsymbol X\mid\widehat\theta^{(r+1)},\boldsymbol y)\mid\widehat\theta^{(r)},\boldsymbol y]\\
> &\qquad\le E[\log k(\boldsymbol X\mid\widehat\theta^{(r)},\boldsymbol y)\mid\widehat\theta^{(r)},\boldsymbol y],
> \end{aligned}
> $$
>
> 将其与(a)结合即可证明定理.
>
> 提示：若$f$和$g$是密度，因$\log$是凹函数，Jensen不等式式4.7.7意味着
>
> $$
> \begin{aligned}
> \int\log\left(\frac{f(x)}{g(x)}\right)g(x)\,dx
> &\le\log\left(\int\frac{f(x)}{g(x)}g(x)\,dx\right)\\
> &=\log\int f(x)\,dx=0.
> \end{aligned}
> $$
>
> 再由对数的性质，得到$\int\log[f(x)]g(x)\,dx\le\int\log[g(x)]g(x)\,dx$.

## 提示

> [!hint]- 提示
> 把观察对数似然增量写成Q增量加KL散度，分别追踪两处等号。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 记$\ell(\theta)=\log L(\theta\mid y)$，$k_r(x)=k(x\mid\theta_r,y)$，$Q_r(\theta)=\int k_r\log L(\theta\mid y,x)dx$，$H_r(\theta)=\int k_r\log k(x\mid\theta,y)dx$。假设所用期望有限且条件密度支持相容；无穷情形可用KL扩展值，但不可任意作$\infty-\infty$。
>
> **(a)** 从完全密度$L(\theta\mid y,x)=L(\theta\mid y)k(x\mid\theta,y)$取对数并对$k_r$积分，得$\ell(\theta)=Q_r(\theta)-H_r(\theta)$，代入$\theta_r$即原式。原(a)第二个比较式左边漏写$E$，正确形式为$Q_r(\theta_{r+1})\ge Q_r(\theta_r)$。因为M步选择$Q_r$的全局最大点，所以不等式成立；等号当且仅当旧点$\theta_r$也是该步$Q_r$的最大点。若最大点唯一，则等价于两次参数相同；一般允许并列，不能直接下此结论。
>
> **(b)** 对$k_r$应用Jensen，
> $$
> H_r(\theta)-H_r(\theta_r)=\int k_r\log\frac{k_\theta}{k_r}\le
> \log\int_{\{k_r>0\}} k_\theta\le0.
> $$
> 若两密度共同支持，则末积分为1，得到原提示；支持不全时把原提示的等号改为不等号仍能证明。严格凹性表明等号要求$k_\theta=k_r$几乎处处（并且无额外支持质量）。因此
> $$
> \ell(\theta_{r+1})-\ell(\theta_r)
> =Q_r(\theta_{r+1})-Q_r(\theta_r)+D_{KL}(k_r\Vert k_{r+1})\ge0.
> $$
> 这证明EM的似然单调性。一般正确等号条件是**$Q$增量为零且两次缺失数据条件分布相同**；单调性本身既不证明参数收敛，也不证明全局MLE的唯一性。
>
> **原定理等号措辞的边界与反例。** PDF297将似然等号写成“当且仅当两次$Q$值相同”，在任意并列M步选择下过强。取参数空间仅$\{0,1\}$，观测$Y=1$，规定$P_0(Y=1)=1/4$、$P_1(Y=1)=1/2$；给定该观测，缺失二元$X$的分布为$k_0=(1/2,1/2)$、$k_1=(a,1-a)$，其中$a=(2-\sqrt3)/4$，所以$a(1-a)=1/16$。其余$Y=0$条件分布任选归一化分布，即得到合法联合实验。
>
> 从参数0开始，$Q_0(0)=\log(1/4)+\log(1/2)=\log(1/8)$，$Q_0(1)=\log(1/2)+\tfrac12\log[a(1-a)]=\log(1/8)$，两点都为M步全局最大。若选参数1，$Q$不变但$\ell$增加$\log2$。所以书中等号的反向命题需要额外的唯一M步最大点、或并列时保留旧点等条件；这里不把错误断言硬证明。

## 相关概念

- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/充分统计量|充分统计量]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已逐项对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=323|印刷第292页／PDF物理第323页]]；版本与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。无星号。
- 原(a)比较式左侧漏E照录；原定理的等号反向命题保留引用并给合法有限实验反例。
- 英文原文、中文转述与本库独立解答分别保留；实际核对正文位置列于`source_refs`。题内文献引用不表示已查阅其原文。`source_status: verified`只指本题及所列位置的核对范围，不表示整章理论独立复证。学习状态保持`not-started`，未实测Obsidian界面渲染。
