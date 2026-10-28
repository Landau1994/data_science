---
title: "习题 ML005：Lasso约束半径与误差变化"
topic: statistical-learning
topic_label: 统计学习
difficulty: intermediate
status: not-started
tags:
  - exercise
  - statistical-learning
source: "[[00 - 首页/教材归档/DS013 - Introduction to Statistical Learning R|ISLR（DS013）]]"
source_id: DS013
source_chapter: 6
source_exercise: "6.3"
source_refs: ["DS013 §6.6 Exercise 3，印刷284/PDF295"]
source_status: verified
solution_status: independently-derived
created: 2026-10-25
---

# 习题 ML005：Lasso约束半径与误差变化

## 题目

### 英文原题

> [!question] 英文原题
> **3.** Suppose we estimate the regression coefficients in a linear regression model by minimizing
> $$
> \sum_{i=1}^{n}\left(y_i-\beta_0-\sum_{j=1}^{p}\beta_jx_{ij}\right)^2
> \quad\text{subject to}\quad
> \sum_{j=1}^{p}|\beta_j|\le s
> $$
> for a particular value of $s$. For parts (a) through (e), indicate which of i. through v. is correct. Justify your answer.
>
> **(a)** As we increase $s$ from 0, the training RSS will:
>
> **i.** Increase initially, and then eventually start decreasing in an inverted U shape.
>
> **ii.** Decrease initially, and then eventually start increasing in a U shape.
>
> **iii.** Steadily increase.
>
> **iv.** Steadily decrease.
>
> **v.** Remain constant.
>
> **(b)** Repeat (a) for test RSS.
>
> **(c)** Repeat (a) for variance.
>
> **(d)** Repeat (a) for (squared) bias.
>
> **(e)** Repeat (a) for the irreducible error.

### 中文转述

> [!question] 中文转述
> **ISLR 第 6 章原题 3（记作 6.3）。** 对固定的 $s$，通过求解下列带约束的最小二乘问题估计线性回归系数：
> $$
> \min_{\beta_0,\beta}\sum_{i=1}^{n}
> \left(y_i-\beta_0-\sum_{j=1}^{p}\beta_jx_{ij}\right)^2,
> \qquad \sum_{j=1}^{p}|\beta_j|\le s.
> $$
> 对 (a)–(e)，从 i–v 中选择并说明理由。
>
> **(a)** 当 $s$ 从零逐渐增大时，训练残差平方和（training RSS）将：
>
> **i.** 先增加，最终转为减少，呈倒 U 形。
>
> **ii.** 先减少，最终转为增加，呈 U 形。
>
> **iii.** 持续增加。
>
> **iv.** 持续减少。
>
> **v.** 保持不变。
>
> **(b)** 对测试残差平方和（test RSS）回答同样的问题。
>
> **(c)** 对方差回答同样的问题。
>
> **(d)** 对平方偏差回答同样的问题。
>
> **(e)** 对不可约误差（irreducible error）回答同样的问题。

## 提示

> [!hint]- 提示 1
> 当 $s=0$ 时哪些系数必须为零？如果 $s_1<s_2$，两个可行集有怎样的包含关系？

> [!hint]- 提示 2
> 约束半径越大，正则化越弱。先严格证明最优训练 RSS 的趋势，再区分教材对测试误差、偏差和方差的典型示意与无条件定理。

## 解答

> [!success]- 解答
> **证明范围：独立推导；严格最优化结论与典型统计趋势分开。** 教材意图对应 **(a) iv，(b) ii，(c) iii，(d) iv，(e) v**。其中训练 RSS 应理解为**单调不增，允许平台**；测试 RSS 的 U 形及方差、平方偏差的方向是典型图景，原题给出的条件不足以使这些趋势成为普遍定理。
>
> **(a) 训练 RSS：iv，精确说为单调不增。** 设
> $$
> \begin{aligned}
> \mathcal C_s&=\{(\beta_0,\beta):\|\beta\|_1\le s\},\\
> R(s)&=\min_{(\beta_0,\beta)\in\mathcal C_s}
> \|y-\beta_0\mathbf1-X\beta\|_2^2.
> \end{aligned}
> $$
> 对 $0\le s_1\le s_2$，有 $\mathcal C_{s_1}\subseteq\mathcal C_{s_2}$；扩大最小化范围不能提高最小值，所以 $R(s_2)\le R(s_1)$。当 $s=0$ 时所有斜率为零，最优截距是 $\bar y$，此时拟合为常数。若某个无约束最小二乘解的斜率满足 $\|\hat\beta_{\mathrm{LS}}\|_1\le s_*$，则对所有 $s\ge s_*$，该解可行，$R(s)$ 恒等于无约束最小 RSS。故原题的“steadily decrease”不能理解为永远严格下降。
>
> **(b) 测试 RSS：典型选择 ii。** 从只含截距的模型逐步放松约束，常可降低欠拟合偏差；继续放松则可能增大估计方差，使测试误差反升。平方损失下的期望预测误差为平方偏差、方差与不可约误差之和，因此常见曲线呈 U 形。
>
> 这不保证某个固定测试集的 RSS 先降后升。它可以单调下降、单调上升、保持不变或出现多个局部转折；即使取期望，最优点也可能在端点。例如如果无约束模型没有明显过拟合，放松约束后测试误差未必反升。原题没有指定数据生成模型或测试集，不能由可行集包含关系推导测试误差的 U 形。
>
> **(c) 方差：典型选择 iii。** $s=0$ 时只估计截距，逐步放松约束允许更复杂的样本依赖拟合，通常带来更高方差。这里的方差指在指定预测位置或指定输入分布下，对重复抽取的训练资料计算的预测方差，而不是一次训练集上不同拟合值的样本方差。对于一般设计的 Lasso，原题未给足以保证这种方差严格单调的分布和设计条件；不能把“通常增加”升级为所有问题的结论。
>
> **(d) 平方偏差：典型选择 iv。** 更大的可行集通常允许逼近更复杂的回归函数，故平方偏差往往减少；如果原模型已经正确而且估计偏差为零，则可保持零。一般相关设计和任意预测位置下，约束半径增大并不直接推出平方偏差单调减少。可行集包含只控制最优训练损失，不能控制对随机训练资料取期望后的非线性函数。
>
> **(e) 不可约误差：v。** 固定数据生成机制，例如 $Y=f(X)+\epsilon$、$E[\epsilon\mid X]=0$，则不可约误差为 $\operatorname{Var}(\epsilon\mid X)$ 或其关于目标输入分布的平均；调整拟合超参数 $s$ 不会改变响应噪声机制，所以它保持不变。它在期望风险分解中出现，不是某次有限测试 RSS 可以单独识别出的一个已知数。
>
> **非唯一性边界。** 即使系数不唯一，最优训练 RSS 仍有明确的最小值。对同一可行凸集，若两组最优系数产生不同的训练拟合向量，它们的中点仍然可行，而平方损失对拟合向量严格凸，会产生更低损失，矛盾；故训练拟合向量唯一。但新输入上的预测可能依赖所选系数解。要讨论预测偏差与方差，还须规定算法如何在多解间选择。

## 相关概念

- [[04 - 统计学习/概念/Lasso回归|Lasso回归]]：$\ell_1$ 球半径与稀疏拟合。
- [[04 - 统计学习/概念/正则化|正则化]]：约束越松，惩罚作用越弱。
- [[04 - 统计学习/概念/泛化、欠拟合与过拟合|泛化、欠拟合与过拟合]]：训练损失趋势与测试误差趋势的区别。
- [[04 - 统计学习/概念/模型评价|模型评价]]：预测误差需要独立评价。
- [[03 - 线性代数与优化/概念/凸集|凸集]]：可行集包含和中点可行性。
- [[03 - 线性代数与优化/概念/凸函数|凸函数]]：拟合向量的唯一性。

## 备注

- 原题逐项对照 [[附件/books/ISLR.pdf#page=295|ISLR 印刷第 284 页／PDF 物理第 295 页]]，完整保留 (a)–(e) 和五个选项；原题没有星号。
- 本题中的 $s$ 是约束半径，增大它会**减弱**正则化；它与增大惩罚权重 $\lambda$ 的方向相反。二者之间也没有对所有资料通用的固定数值换算。
- 典型选项对应教材的偏差方差权衡；平台、测试误差不必 U 形及多解选择条件为独立补充。未核对官方答案，未运行模拟。
- `source_status: verified` 只表示本题原文和定位已核对；个人学习状态保持 `not-started`。
