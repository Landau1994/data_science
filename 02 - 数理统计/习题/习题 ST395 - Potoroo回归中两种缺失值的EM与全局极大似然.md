---
title: "习题 ST395：Potoroo回归中两种缺失值的EM与全局极大似然"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第11章习题11.41，印刷页462／PDF物理页493"
source_id: "DS011"
source_chapter: 11
source_exercise: "11.41"
source_stars: 0
source_refs: ["DS011 Exercise 11.41，印刷462／PDF物理493", "DS011 Example 12.4.2及Table 12.4.2，印刷484–485／PDF物理515–516"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST395：Potoroo回归中两种缺失值的EM与全局极大似然

## 题目

### 英文原题

> [!question] 英文原题
> **11.41** In the discussion in Example 12.4.2, note that there was one observation from the Potoroo data that had a missing value. Suppose that on the 24th animal it was observed that O$_2=16.3$.
> (a) Write down the observed-data and expected complete-data log likelihood functions.
> (b) Describe the E-step and the M-step of an EM Algorithm to find the MLEs.
> (c) Find the MLEs using all 24 observations.
> (d) Actually, the O$_2$ reading on the 24th animal was not observed, but rather the CO$_2$ was observed to be 4.2 (and the O$_2$ was missing). Set up the EM Algorithm in this case and find the MLEs. (This is a much harder problem, as you now have to take expectations over the $x$s. This means you have to formulate the regression problem using the bivariate normal distribution.)

### 中文转述

> [!question] 中文转述
> **原题11.41。** 注意例12.4.2的讨论中，Potoroo数据有一个观测含缺失值. 假设第24只动物观测到$\mathrm O_2=16.3$.
>
> (a)  写出观测数据的对数似然函数，以及完整数据对数似然函数的期望.
>
> (b)  描述求MLE的EM算法的E步和M步.
>
> (c)  用全部24个观测求MLE.
>
> (d)  实际上，第24只动物未观测到$\mathrm O_2$，而是观测到$\mathrm{CO}_2=4.2$，$\mathrm O_2$缺失. 对此情形建立EM算法并求MLE. （这个问题困难得多，因为现在必须对$x$取期望，这意味着必须用二元正态分布表述回归问题.）

### 题内引用与条件

原表12.4.2的23对完整观测已逐项对照印刷485／PDF物理516；第15只氧气为18，未使用正文另设的误录10案例。

| 动物 | O₂（x，百分比） | CO₂（y，百分比） |
| --- | ---: | ---: |
| 1 | 20 | 1 |
| 2 | 19.6 | 1.2 |
| 3 | 19.6 | 1.1 |
| 4 | 19.4 | 1.4 |
| 5 | 18.4 | 2.3 |
| 6 | 19 | 1.7 |
| 7 | 19 | 1.7 |
| 8 | 18.3 | 2.4 |
| 9 | 18.2 | 2.1 |
| 10 | 18.6 | 2.1 |
| 11 | 19.2 | 1.2 |
| 12 | 18.2 | 2.3 |
| 13 | 18.7 | 1.9 |
| 14 | 18.5 | 2.4 |
| 15 | 18 | 2.6 |
| 16 | 17.4 | 2.9 |
| 17 | 16.5 | 4 |
| 18 | 17.2 | 3.3 |
| 19 | 17.3 | 3 |
| 20 | 17.8 | 3.4 |
| 21 | 17.3 | 2.9 |
| 22 | 18.4 | 1.9 |
| 23 | 16.9 | 3.9 |

## 提示

> [!hint]- 提示
> 缺失响应对条件似然的贡献积分为1；缺失预测变量时先写联合二元正态模型，并计算缺失变量的一阶、二阶条件矩。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> 约定缺失机制可忽略，先按固定$x$的条件模型$Y_i\mid x_i\sim N(\alpha+\beta x_i,v)$，$v=\sigma^2>0$。23对实际数据在题内引用表完整保留。
> (a) 设$m=23,N=24,x_0=16.3$，缺失响应为$Y_0$。其条件密度积分为1，观测对数似然为
> $$
> \ell_o(\alpha,\beta,v)=-\frac m2\log(2\pi v)-\frac1{2v}\sum_{i=1}^{m}(y_i-\alpha-\beta x_i)^2.
> $$
> 完整对数似然将$m$换为$N$并加入$(Y_0-\alpha-\beta x_0)^2$。在旧参数下令$h=\alpha^{old}+\beta^{old}x_0$、$u=v^{old}$，则
> $$
> Q=-\frac N2\log(2\pi v)-\frac1{2v}\left[\sum_{i=1}^{m}(y_i-\alpha-\beta x_i)^2+(h-\alpha-\beta x_0)^2+u\right].
> $$
> (b) E步为$E(Y_0\mid\mathrm{obs})=h,E(Y_0^2\mid\mathrm{obs})=h^2+u$。M步先把缺失响应替换为$h$、对全部24个固定$x$作普通最小二乘得$(\alpha^{new},\beta^{new})$，再取
> $$
> v^{new}=\frac1{24}\left[\sum_{i=1}^{23}(y_i-\alpha^{new}-\beta^{new}x_i)^2+(h-\alpha^{new}-\beta^{new}x_0)^2+u\right].
> $$
> 不能只作均值填补而丢失条件方差$u$。
> (c) 观测似然恰是23对完整数据的似然，所以全局MLE与这23对的回归相同：$\widehat\alpha=18.6745730378$、$\widehat\beta=-.893986191860$、$\widehat v=.0503426756825$；缺失$Y_0$条件均值$4.10259811047$。实际EM初值为$(\alpha,\beta,v)=(18,-.8,1)$，停止规则为三参数绝对改变量最大值小于$10^{-11}$，最多10000步；第19步实际改变量为$2.21334\times10^{-12}$，与直接解一致。首个更新后记录的观测对数似然为$-1.78020812$，最终为$1.73678833$，最小计算增量$-3.9\times10^{-14}$属浮点舍入。这里“全部24观测”只有23个响应，第24个已知$x$不能凭空提供条件回归参数信息。
> (d) 此时必须为$X$建模。令$Z=(X,Y)^T\sim N_2(\mu,\Sigma)$。观测似然为23个二元正态密度之积，乘第24个$Y$的边缘正态密度；$y_0=4.2$。E步在旧参数下
> $$
> h_x=\mu_X+\frac{\Sigma_{XY}}{\Sigma_{YY}}(y_0-\mu_Y),\qquad
> u_x=\Sigma_{XX}-\frac{\Sigma_{XY}^2}{\Sigma_{YY}}.
> $$
> 故$E(Z_0)=(h_x,y_0)^T$，$E(Z_0Z_0^T)=\begin{pmatrix}h_x^2+u_x&h_xy_0\\h_xy_0&y_0^2\end{pmatrix}$。完整$Q$为$-N\log|\Sigma|/2-\frac12\operatorname{tr}[\Sigma^{-1}\sum E\{(Z_i-\mu)(Z_i-\mu)^T\mid\mathrm{obs}\}]+\mathrm{const}$。M步
> $$
> \mu^{new}=\frac1N\sum E(Z_i\mid\mathrm{obs}),\quad
> \Sigma^{new}=\frac1N\sum E(Z_iZ_i^T\mid\mathrm{obs})-\mu^{new}(\mu^{new})^T.
> $$
> 再转换为$Y\mid X$参数：$\beta=\Sigma_{XY}/\Sigma_{XX}$、$\alpha=\mu_Y-\beta\mu_X$、$v=\Sigma_{YY}-\Sigma_{XY}^2/\Sigma_{XX}$。
> 实际EM及直接解给
> $$
> \widehat\mu=\binom{18.2433855515}{2.37083333333},\quad
> \widehat\Sigma=\begin{pmatrix}.957430128702&-.864390595372\\-.864390595372&.831232638889\end{pmatrix},
> $$
> 因此$\widehat\alpha=18.8413938742$、$\widehat\beta=-.902823683378$、$\widehat v=.0508403376973$。缺失$x$条件均值$16.3412532361$、条件方差$.0585589025112$。
> 为确认是全局MLE而非仅EM固定点，改参数化成$X\mid Y\sim N(a+bY,u)$与$Y\sim N(\mu_Y,v_Y)$。观测似然分为23对反向回归的似然和24个$Y$边缘的似然，分别有直接唯一解：$a=20.7087916733,b=-1.03989010408,u=.0585589025110$；$\mu_Y=2.37083333333,v_Y=.831232638889$。再用$\mu_X=a+b\mu_Y,\Sigma_{XY}=bv_Y,\Sigma_{XX}=u+b^2v_Y$得到上述同一结果。程序初值为23对完整观测的联合正态MLE（协方差分母23），以均值和协方差全部元素的最大绝对改变量小于$10^{-11}$停止，最多10000步；实际两步确认固定点，末次改变量为0。第一步后观测对数似然为$-31.8381594533$，第二步不变。这两步只描述该初值的实际运行，不作为一般全局收敛证明。
> 完整输入、运行环境、实现、收敛及交叉核算见[[工具/StatisticalInference/ch11_numeric_checks.py|计算实现]]与[[工具/StatisticalInference/ch11-numeric-results.json|实际结果]]；无随机抽样。

## 相关概念

- [[03 - 线性代数与优化/概念/正规方程|正规方程]]
- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=493|印刷462／PDF物理493]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
