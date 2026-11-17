---
title: "习题 P232：Poisson个对数级数变量和的负二项律"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第4章习题4.33，印刷页161／PDF物理页192"
source_id: "DS011"
source_chapter: 4
source_exercise: "4.33"
source_stars: 0
source_refs: ["DS011 Exercise 4.33，印刷161／PDF物理192", "DS011 所引正文，印刷78／PDF物理109", "DS011 所引正文，印刷79／PDF物理110"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P232：Poisson个对数级数变量和的负二项律

## 题目

### 英文原题

> [!question] 英文原题
> **4.33** (Alternative derivation of the negative binomial distribution) Solomon (1983) details the following biological model. Suppose that each of a random number, $N$, of insects lays $X_i$ eggs, where the $X_i$s are independent, identically distributed random variables. The total number of eggs laid is $H=X_1+\cdots+X_N$. What is the distribution of $H$?
>
> It is common to assume that $N$ is Poisson$(\lambda)$. Furthermore, if we assume that each $X_i$ has the logarithmic series distribution (see Exercise 3.14) with success probability $p$ (Exercise 3.14), we have the hierarchical model
> $$
> H\mid N=X_1+\cdots+X_N,\qquad P(X_i=t)=\frac{-1}{\log(p)}\frac{(1-p)^t}{t},\qquad N\sim\operatorname{Poisson}(\lambda).
> $$
> Show that the marginal distribution of $H$ is negative binomial $(r,p)$, where $r=-\lambda/\log(p)$. (It is easiest to calculate and identify the mgf of $H$ using Theorems 4.4.3 and 4.6.7. Stuart and Ord (1987, Section 5.21) also mention this derivation of the logarithmic series distribution. They refer to $H$ as a randomly stopped sum.)

### 中文转述

> [!question] 中文转述
> **原题4.33。**
> Solomon (1983) 详细描述了如下生物模型. 假设昆虫的数量 $N$ 为随机数，每只昆虫产卵 $X_i$ 个，其中 $X_i$ 独立同分布. 总产卵数为 $H=X_1+\cdots+X_N$. $H$ 的分布是什么？
>
> 通常假定 $N\sim\operatorname{Poisson}(\lambda)$. 再假定每个 $X_i$ 服从成功概率为 $p$ 的对数级数分布（见习题3.14），得到分层模型
>
> $$
> \begin{aligned}
> H\mid N&=X_1+\cdots+X_N,\qquad P(X_i=t)=\frac{-1}{\log p}\frac{(1-p)^t}t,\\
> N&\sim\operatorname{Poisson}(\lambda).
> \end{aligned}
> $$
>
> 证明 $H$ 的边缘分布是 $\operatorname{negative\ binomial}(r,p)$，其中 $r=-\lambda/\log p$. 最容易的方法是利用定理4.4.3 和定理4.6.7 计算并识别 $H$ 的 mgf. Stuart and Ord (1987, Section 5.21) 也提及了这种对数级数分布的推导；他们将 $H$ 称为随机停止和（randomly stopped sum）.

## 提示

> [!hint]- 提示
> 先求单个产卵数的pgf，再用Poisson复合的指数公式。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 令$0<p<1$、$\lambda>0$，假定$N$与整列$X_i$独立，$N=0$时空和为0。用$-\log(1-z)=\sum_{t\ge1}z^t/t$得单项pgf
> $$
> G_X(s)=\frac{\log(1-(1-p)s)}{\log p}.
> $$
> 给定$N=n$，$G_{H\mid N}(s)=G_X(s)^n$。对Poisson分布求和，
> $$
> G_H(s)=e^{\lambda(G_X(s)-1)}=\left[\frac p{1-(1-p)s}\right]^r,\qquad r=-\lambda/\log p>0.
> $$
> 最后等式利用$p^r=e^{-\lambda}$。广义二项级数给$P(H=h)=\Gamma(r+h)p^r(1-p)^h/[\Gamma(r)h!]$，$h\ge0$。这正是失败次数版本的负二项pmf，对所有实$r>0$成立，不要求$r$为整数；若总试验次数约定则$H+r$才是相应平移变量。$P(H=0)=e^{-\lambda}=p^r$也核对了零值。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=192|印刷第161页／PDF物理第192页]]；教材信息与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。原题无星号。
- 题内引用正文已核对：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=109|印刷78／PDF109]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=110|印刷79／PDF110]]。所需条件在解答重述，原文输入与独立补充分开。
- `source_status: verified`仅指本题题干、公式及所列来源定位已核对，不表示全章正文独立复证。解答写成不等于个人已完成练习，学习状态保持`not-started`；未实测Obsidian界面渲染。
