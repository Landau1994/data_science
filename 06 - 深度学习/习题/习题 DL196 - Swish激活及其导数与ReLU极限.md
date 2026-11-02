---
title: "习题 DL196：Swish激活及其导数与ReLU极限"
topic: "deep-learning"
topic_label: "深度学习"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "deep-learning"]
source: "[[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|Bishop《深度学习：基础与概念》（DS003）]]"
source_id: "DS003"
source_chapter: 6
source_exercise: "6.5"
source_stars: 2
source_refs: ["DS003 Exercise 6.5及式(6.61)，印刷205–206/PDF223–224", "DS003 §6.2.3，Sigmoid式(6.13)及ReLU式(6.17)，印刷183、185/PDF201、203"]
source_status: "verified"
solution_status: "independently-derived"
created: 2026-11-02
---

# 习题 DL196：Swish激活及其导数与ReLU极限

## 题目

### 英文原题

> [!question] 英文原题
> **6.5 (★★)** The swish activation function (Ramachandran, Zoph, and Le, 2017) is defined by
> $$
> h(x)=x\sigma(\beta x)\tag{6.61}
> $$
> where $\sigma(x)$ is the logistic-sigmoid activation function defined by (6.13). When used in a neural network, $\beta$ can be treated as a learnable parameter. Either sketch or plot using software graphs of the swish activation function as well as its first derivative for $\beta=0.1$, $\beta=1.0$, and $\beta=10$. Show that when $\beta\to\infty$, the swish function becomes the ReLU function.

### 中文转述

> [!question] 中文转述
> **Bishop 原题 6.5。** Swish 激活函数（swish activation function）由 $h(x)=x\sigma(\beta x)$ 定义，其中 $\sigma$ 是式(6.13)的逻辑 Sigmoid。网络中可把 $\beta$ 视为可学习参数。对 $\beta=0.1,1.0,10$，手绘或用软件绘制激活函数及其一阶导数的图像。证明当 $\beta\to\infty$ 时，Swish 变为 ReLU 函数。

## 提示

> [!hint]- 提示 1
> 先对乘积 $x\sigma(\beta x)$ 求导，再用 $\sigma'(a)=\sigma(a)(1-\sigma(a))$。极限分 $x<0$、$x=0$、$x>0$。

## 解答

> [!success]- 解答
> **证明范围：独立解析推导，附所要求的函数绘图。** 记 $h_\beta(x)=x\sigma(\beta x)$。由乘积法则和链式法则，
> $$
> h_\beta'(x)=\sigma(\beta x)+\beta x\sigma(\beta x)\{1-\sigma(\beta x)\}.
> $$
> 两者在每个有限 $\beta,x$ 处均光滑，且 $h_\beta(0)=0$、$h_\beta'(0)=1/2$。下图左侧为函数、右侧为上述导数，截取输入区间 $[-4,4]$；同一图内比较三种题定的正参数值。
>
> ![[附件/习题图/DS003/解答-6.5.png]]
>
> 三种曲线在原点有相同斜率，但较大的 $\beta$ 使弯曲过渡集中在更窄的邻域。Swish 不必单调：当 $\beta x=-2$ 时，$h_\beta'(x)=\sigma(-2)\{1-2\sigma(2)\}<0$。同样在 $\beta x=2$ 时，$h_\beta'(x)-1=(1-\sigma(2))(2\sigma(2)-1)>0$，所以导数也可超过1；图中可见这些行为，部分较小参数的弯曲发生在绘图区间之外。
>
> **ReLU极限。** 固定输入，令 $\beta\to+\infty$。若 $x>0$，$\sigma(\beta x)\to1$，故 $h_\beta(x)\to x$；若 $x<0$，$\sigma(\beta x)\to0$，故 $h_\beta(x)\to0$；若 $x=0$，函数恒为0。因此
> $$
> h_\beta(x)\longrightarrow\max(0,x)=\operatorname{ReLU}(x).
> $$
> 甚至对所有实数输入都有统一误差界。对 $\beta>0$，
> $$
> |h_\beta(x)-\operatorname{ReLU}(x)|
> =\frac{|x|}{1+e^{\beta|x|}}
> \le |x|e^{-\beta|x|}\le\frac1{e\beta}.
> $$
> 最后一步来自 $t e^{-\beta t}$ 在 $t=1/\beta$ 取得最大值。因此函数在整个实线上一致趋于ReLU。
>
> 导数的极限需另外区别：$x\ne0$ 时分别趋于0、1；但对每个 $\beta$，在 $x=0$ 的导数总为 $1/2$，而ReLU在0处不可导。函数趋近并不允许在该点直接交换求导和极限。

## 相关概念

- [[06 - 深度学习/概念/激活函数|激活函数]]
- [[03 - 线性代数与优化/概念/链式法则|链式法则]]
- [[06 - 深度学习/概念/神经网络|神经网络]]

## 备注

- 原题定位：[[附件/books/Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf#page=223|印刷205–206／PDF物理223–224]]；所用正文公式的实际位置见 `source_refs`。
- 原题跨印刷205–206／PDF223–224，三种参数、函数和导数作图要求及极限任务全部保留。
- 附图根据上述解析公式绘制，保留同名TikZ图源和矢量PDF，已编译、渲染并目视检查；该图是公式示意，不是训练实验。
- 题干、星号、引用公式与定位已实际对照原页；`source_status: verified` 仅限本题实际核对范围。解答为独立推导，未使用配套答案册；个人学习状态保持 `not-started`。
