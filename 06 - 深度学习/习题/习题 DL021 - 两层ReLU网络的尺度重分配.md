---
title: "习题 DL021：两层ReLU网络的尺度重分配"
topic: deep-learning
topic_label: 深度学习
difficulty: intermediate
status: not-started
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08 修订稿），Problem 4.3及式(4.18)，印刷54／PDF物理68"
source_id: DS001
source_chapter: 4
source_exercise: "4.3"
source_refs: ["DS001 Problem 4.3 与式(4.18)，印刷54/PDF68","DS001 Problem 3.5，印刷39/PDF53"]
source_status: verified
solution_status: independently-derived
created: 2026-10-28
---

# 习题 DL021：两层ReLU网络的尺度重分配

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 4.3** Using the non-negative homogeneity property of the ReLU function (see problem 3.5), show that:
> $$
> \begin{aligned}
> &\operatorname{ReLU}\!\left[\boldsymbol\beta_1+\lambda_1\cdot\boldsymbol\Omega_1
> \operatorname{ReLU}[\boldsymbol\beta_0+\lambda_0\cdot\boldsymbol\Omega_0\mathbf x]\right]\\
> &\quad=\lambda_0\lambda_1\cdot
> \operatorname{ReLU}\!\left[
> \frac{1}{\lambda_0\lambda_1}\boldsymbol\beta_1+
> \boldsymbol\Omega_1\operatorname{ReLU}\!\left[
> \frac{1}{\lambda_0}\boldsymbol\beta_0+\boldsymbol\Omega_0\mathbf x
> \right]\right].
> \end{aligned}
> \tag{4.18}
> $$
> where $\lambda_0$ and $\lambda_1$ are non-negative scalars. From this, we see that the weight matrices can be rescaled by any magnitude as long as the biases are also adjusted, and the scale factors can be re-applied at the end of the network.

### 中文转述

> [!question] 中文转述
> **UDL 原题 4.3。** 使用 ReLU 的非负齐次性（non-negative homogeneity，见原题 3.5），证明上面的式 (4.18)。原题称 $\lambda_0,\lambda_1$ 是非负标量，并由此说明：只要同时调整偏置，就可以重缩放权重矩阵，并将尺度因子移到网络末端。原题中“非负”包含的零值问题在解答中另行说明。

## 提示

> [!hint]- 提示 1
> 先假设两个尺度因子严格为正。在最内层提取 $\lambda_0$，再在外层提取 $\lambda_0\lambda_1$。

> [!hint]- 提示 2
> 对向量逐坐标使用 $\operatorname{ReLU}(cz)=c\operatorname{ReLU}(z)$（$c\ge0$）。提取尺度时，偏置必须除以同一个尺度；先检查分母是否为零。

## 解答

> [!success]- 解答
> **独立证明，并补足原式的非零分母条件。** 各矩阵与向量维数相容，ReLU 逐坐标作用。式 (4.18) 按通常实数运算有意义，需要
> $$
> \lambda_0>0,\qquad \lambda_1>0.
> $$
> 对这些尺度，先写
> $$
> \boldsymbol\beta_0+\lambda_0\boldsymbol\Omega_0\mathbf x
> =\lambda_0\left(\frac{\boldsymbol\beta_0}{\lambda_0}
> +\boldsymbol\Omega_0\mathbf x\right).
> $$
> 非负齐次性给出
> $$
> \operatorname{ReLU}(\boldsymbol\beta_0+\lambda_0\boldsymbol\Omega_0\mathbf x)
> =\lambda_0\operatorname{ReLU}\!\left(
> \frac{\boldsymbol\beta_0}{\lambda_0}+\boldsymbol\Omega_0\mathbf x\right).
> $$
> 代入外层，把其输入整理为
> $$
> \begin{aligned}
> &\boldsymbol\beta_1+\lambda_0\lambda_1\boldsymbol\Omega_1
> \operatorname{ReLU}\!\left(
> \frac{\boldsymbol\beta_0}{\lambda_0}+\boldsymbol\Omega_0\mathbf x\right)\\
> &\quad=\lambda_0\lambda_1\left[
> \frac{\boldsymbol\beta_1}{\lambda_0\lambda_1}
> +\boldsymbol\Omega_1\operatorname{ReLU}\!\left(
> \frac{\boldsymbol\beta_0}{\lambda_0}+\boldsymbol\Omega_0\mathbf x\right)
> \right].
> \end{aligned}
> $$
> 再对外层 ReLU 使用齐次性，便得到原式右边。这也明确说明，提取尺度时必须相应调整两层偏置，不能只更改矩阵而保持偏置不动。
>
> **零尺度的边界。** 原式左边在零值处仍有定义，但右边含除零项：
>
> - 若 $\lambda_1=0$，左边为 $\operatorname{ReLU}(\boldsymbol\beta_1)$，与 $\lambda_0$ 无关。
> - 若 $\lambda_0=0$、$\lambda_1>0$，左边为
> $$
> \operatorname{ReLU}\!\left(
> \boldsymbol\beta_1+\lambda_1\boldsymbol\Omega_1
> \operatorname{ReLU}(\boldsymbol\beta_0)\right),
> $$
> 与输入 $\mathbf x$ 无关。
>
> 两者同时为零已经包含在第一种情况中。不能把右边未定义的分式与外面的零因子相乘来当作证明。因此，“非负”条件下原式存在表述缺口；所写重参数化等式的有效条件是严格为正，零值须以上述原始计算单独处理。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]：矩阵、偏置和逐坐标激活。
- [[06 - 深度学习/习题/习题 DL005 - ReLU的非负齐次性|ReLU 的非负齐次性]]：两次提取正尺度的依据。
- [[06 - 深度学习/概念/激活函数|激活函数]]

## 备注

- 原题、式 (4.18) 及“non-negative scalars”用语均核对 [[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=68|印刷 54／PDF 68]]；英文保持原来的非负条件，没有静默改成 strictly positive。
- 原题 3.5 位于 [[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=53|印刷 39／PDF 53]]。本题证明采用其正数情形；零尺度分析为本页明确补充。

