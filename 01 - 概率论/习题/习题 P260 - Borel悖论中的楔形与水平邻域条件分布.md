---
title: "习题 P260：Borel悖论中的楔形与水平邻域条件分布"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第4章习题4.61，印刷页166／PDF物理页197"
source_id: "DS011"
source_chapter: 4
source_exercise: "4.61"
source_stars: 0
source_refs: ["DS011 Exercise 4.61，印刷166／PDF物理197", "DS011 所引正文，印刷167／PDF物理198", "DS011 所引正文，印刷168／PDF物理199"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P260：Borel悖论中的楔形与水平邻域条件分布

## 题目

### 英文原题

> [!question] 英文原题
> **4.61** DeGroot (1986) gives the following example of the Borel Paradox (Miscellanea 4.9.3): Suppose that $X_1$ and $X_2$ are iid exponential$(1)$ random variables, and define $Z=(X_2-1)/X_1$. The probability-zero sets $\{Z=0\}$ and $\{X_2=1\}$ seem to be giving us the same information, but lead to different conditional distributions.
> (a) Find the distribution of $X_1\mid Z=0$, and compare it to the distribution of $X_1\mid X_2=1$.
> (b) For small $\varepsilon>0$ and $x_1>0,x_2>0$, consider the sets
> $$B_1=\{(x_1,x_2):-\varepsilon<(x_2-1)/x_1<\varepsilon\}\quad\text{and}\quad B_2=\{(x_1,x_2):1-\varepsilon<x_2<1+\varepsilon\}.$$
> Draw these sets and support the argument that $B_1$ is informative about $X_1$, but $B_2$ is not.
> (c) Calculate $P(X_1\le x\mid B_1)$ and $P(X_1\le x\mid B_2)$, and show that their limits (as $\varepsilon\to0$) agrees with part (a).
>
> (Communicated by L. Mark Berliner, Ohio State University.)

### 中文转述

> [!question] 中文转述
> **原题4.61。**
> DeGroot (1986) 给出如下 Borel 悖论（杂录 4.9.3）的例子. 设 $X_1,X_2$ 为独立同分布的 $\operatorname{exponential}(1)$ 随机变量，定义 $Z=(X_2-1)/X_1$. 零概率集合 $\{Z=0\}$ 与 $\{X_2=1\}$ 看似提供了相同信息，却导出不同条件分布.
>
> (a)  求 $X_1\mid Z=0$ 的分布，并与 $X_1\mid X_2=1$ 比较.
>
> (b)  对小的 $\varepsilon>0$ 及 $x_1>0,x_2>0$，考虑
>
> $$
> B_1=\left\{(x_1,x_2):-\varepsilon<\frac{x_2-1}{x_1}<\varepsilon\right\},\qquad
> B_2=\{(x_1,x_2):1-\varepsilon<x_2<1+\varepsilon\}.
> $$
>
> 画出这两个集合，并说明为何 $B_1$ 提供了关于 $X_1$ 的信息，而 $B_2$ 没有.
>
> (c)  计算 $P(X_1\le x\mid B_1)$ 与 $P(X_1\le x\mid B_2)$，说明它们在 $\varepsilon\to0$ 时的极限与 (a) 一致.
>
> （由俄亥俄州立大学 L. Mark Berliner 提供.）

## 提示

> [!hint]- 提示
> 楔形带的竖直宽度依赖$x_1$，而水平带不依赖；必须保留第一象限裁切。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** (a) 变换$x_2=1+zx_1$的Jacobian为$x_1$，因此$f_{X_1,Z}(t,z)=t e^{-t-(1+zt)}$，支持$t>0,1+zt>0$。在$z=0$归一化得到$t e^{-t}$，即Gamma$(2,1)$。而$X_1,X_2$独立，按其连续条件密度版本$X_1\mid X_2=1\sim\operatorname{Exp}(1)$。
> (b) 第一象限内$B_1$为$\max(0,1-\varepsilon x_1)<x_2<1+\varepsilon x_1$，竖直截段宽度随$x_1$变化；$B_2$为水平带$1-\varepsilon<x_2<1+\varepsilon$（取$0<\varepsilon<1$），不限制$x_1$。因此前者改变$x_1$权重，后者由独立性不改变。
>
> ![[附件/习题图/DS011/习题4.61-Borel条件邻域.png]]
>
> 图为本库独立示意，取$\varepsilon=0.2$；虚线表示严格不等式边界，不是原书图。
> (c) 令$h=1/\varepsilon$，$H_a(t)=(1-e^{-at})/a$（$a>0,t\ge0$），$u=\min(x,h)$。对$x\ge0$，直接积分得
> $$
> \begin{aligned}J_\varepsilon(x)&=e^{-1}[H_{1-\varepsilon}(u)-H_{1+\varepsilon}(u)]\\&\quad+\mathbf1_{\{x>h\}}\left[e^{-h}-e^{-x}-\frac{e^{-1}}{1+\varepsilon}(e^{-(1+\varepsilon)h}-e^{-(1+\varepsilon)x})\right].\end{aligned}
> $$
> 这是$\int_0^x e^{-t}[e^{-\max(0,1-\varepsilon t)}-e^{-(1+\varepsilon t)}]dt$的分段原函数。分母为
> $$
> J_\varepsilon(\infty)=\frac{2\varepsilon e^{-1}}{1-\varepsilon^2}-\frac{\varepsilon e^{-1/\varepsilon}}{1-\varepsilon}>0.
> $$
> 所以$P(X_1\le x\mid B_1)=J_\varepsilon(x)/J_\varepsilon(\infty)$（$x\ge0$，否则0）。$B_2$与$X_1$独立，故条件CDF对每个$\varepsilon$均为$1-e^{-x}$，$x\ge0$。
> 当$\varepsilon\downarrow0$，竖直截段概率除以$2\varepsilon e^{-1}$逐点趋$t$；对$0<\varepsilon\le1/2$可由常数倍$t e^{t/2}$控制，乘$e^{-t}$后可积，故支配收敛给$B_1$条件CDF极限$\int_0^xte^{-t}dt=1-e^{-x}(1+x)$。$B_2$极限仍$1-e^{-x}$，与(a)一致。这些答案对应明确邻域序列，不声称零概率事件本身有唯一条件律。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=197|印刷第166页／PDF物理第197页]]；教材信息与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。原题无星号。
- 题内引用正文已核对：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=198|印刷167／PDF198]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=199|印刷168／PDF199]]。所需条件在解答重述，原文输入与独立补充分开。
- `source_status: verified`仅指本题题干、公式及所列来源定位已核对，不表示全章正文独立复证。解答写成不等于个人已完成练习，学习状态保持`not-started`；未实测Obsidian界面渲染。
