---
title: "Wasserstein 距离"
aliases: ["Wasserstein distance","Wasserstein metric"]
topic: linear-algebra-optimization
topic_label: 线性代数与优化
tags:
  - concept
status: not-started
source: "Statistical Optimal Transport（Springer 2025），§1.2 定义 1.2 及前文，印刷页 7 / PDF 物理页 21"
source_status: partially-verified
created: 2026-10-24
---

# Wasserstein 距离

## 定义

> [!info] 定义
> 在度量空间 $(\mathcal X,d)$ 上，给定 $p\ge1$，记 $\mathcal P_p(\mathcal X)$ 为满足 $\int d(x,o)^p\,d\mu(x)<\infty$ 的概率测度集合，其中 $o$ 是任一固定基点。Wasserstein 距离（Wasserstein distance）定义为
> $$
> W_p(\mu,\nu)=\left(\inf_{\pi\in\Pi(\mu,\nu)}\int d(x,y)^p\,d\pi(x,y)\right)^{1/p}.
> $$

$\Pi(\mu,\nu)$ 是具有这两个边缘分布的耦合集。改变基点不改变有限矩条件，因为三角不等式可将不同基点的矩互相控制。

## 直觉与解释

$W_p$ 测量重新排列概率质量所需的距离：较大的 $p$ 对远距离搬运更敏感。它需要底层空间的距离；把同一数据坐标从米换成厘米，距离值也会随之缩放。它和只比较概率密度比的散度反映不同信息，不能把二者数值直接当作同一尺度。

## 主要性质

对 $\mathcal P_p(\mathcal X)$ 中的分布，独立耦合与 $d(x,y)^p\le2^{p-1}(d(x,o)^p+d(y,o)^p)$ 给出有限性。交换耦合的两个坐标保持成本，故 $W_p(\mu,\nu)=W_p(\nu,\mu)$。对角耦合直接给出 $W_p(\mu,\mu)=0$。

在 Polish 空间上，$W_p$ 是 $\mathcal P_p$ 上的度量。这一完整结论中的“距离为零推出测度相同”和三角不等式在此作为未展开的理论输入；三角不等式通常借助耦合的拼接及 Minkowski 不等式，不能仅从定义中的下确界直接略去证明。

## 例子与边界

> [!example] 点质量与异常值
> 两个点质量只有一种耦合，故 $W_p(\delta_x,\delta_y)=d(x,y)$。在实线上令 $\nu_\varepsilon=(1-\varepsilon)\delta_0+\varepsilon\delta_R$，则 $W_p(\delta_0,\nu_\varepsilon)=\varepsilon^{1/p}|R|$。很小的远端质量仍可能产生明显距离。

若 $\mu$ 没有有限 $p$ 阶矩，与 $\delta_o$ 的上述公式为无穷大；此时不能直接使用 $\mathcal P_p$ 上的有限度量结论。经验分布间距离较小也不自动给出总体分布估计的误差保证。

弱收敛也不单独保证此距离收敛：令 $\mu_n=(1-1/n)\delta_0+(1/n)\delta_n$，任意有界连续函数的积分差至多为其上确界范数的 $2/n$，故 $\mu_n$ 弱收敛于 $\delta_0$；但 $W_1(\mu_n,\delta_0)=1$。逃向远端的少量质量说明矩条件不能被省略。

## 相关概念

[[03 - 线性代数与优化/概念/最优传输|最优传输]]给出成本最小化基础；[[03 - 线性代数与优化/概念/梯度流|梯度流]]可使用此距离作为几何；[[01 - 概率论/概念/相对熵|相对熵]]是另一种分布比较方式。

## 相关习题

```dataview
TABLE WITHOUT ID file.link AS "习题", difficulty AS "难度", status AS "学习状态"
FROM #exercise
WHERE contains(file.outlinks, this.file.link)
SORT file.name ASC
```

## 来源与证明状态

已实读附件 Chewi、Niles-Weed、Rigollet，*Statistical Optimal Transport*（Springer 2025），§1.2 定义 1.2 及前文，印刷页 7 / PDF 物理页 21，核对有限 p 阶矩与欧氏空间中的 Wasserstein 定义，见 [[00 - 首页/教材归档/DS006 - Statistical Optimal Transport|DS006 统一台账]]。source_status 为 partially-verified，仅指这些定义及适用范围。本页的度量空间写法、矩界、对称性和点质量公式为独立整理；完整 Polish 空间度量定理未在此证明，不把该推广说成已核对的原书原句。

原书本页达到下确界的证明中，有将 $I(\bar\gamma)$ 与 $W_p$ 直接比较、末尾写 $I(\bar\gamma)=W_p$ 的幂次混写；按该页 $I$ 的定义，相应量应为 $W_p^p$。这里保留可见说明，不照用这些中间式；定义 1.2 的外部 $1/p$ 次方没有该问题。
