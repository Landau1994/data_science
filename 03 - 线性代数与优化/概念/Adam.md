---
title: "Adam"
aliases: ["Adaptive Moment Estimation"]
topic: "linear-algebra-optimization"
topic_label: "线性代数与优化"
tags: ["concept","linear-algebra-optimization"]
status: "not-started"
source: "Understanding Deep Learning（Simon J. D. Prince，2026-02-08修订稿），§6.4式6.15–6.18，印刷90／PDF物理104"
source_refs: ["DS001 §6.4式6.15–6.18，印刷90/PDF104"]
source_status: "partially-verified"
created: "2026-10-28"
---

# Adam

## 定义

> [!info] 定义
> Adam是自适应矩估计（adaptive moment estimation）优化算法。给定梯度或小批量梯度 $g_t$，取 $m_0=v_0=0$、$0\le\beta_1,\beta_2<1$，在 $t\ge1$ 时计算
> $$
> m_t=\beta_1m_{t-1}+(1-\beta_1)g_t,\qquad
> v_t=\beta_2v_{t-1}+(1-\beta_2)(g_t\odot g_t),
> $$
> $$
> \widehat m_t=\frac{m_t}{1-\beta_1^t},\quad
> \widehat v_t=\frac{v_t}{1-\beta_2^t},\quad
> \theta_{t+1}=\theta_t-\eta_t
> \frac{\widehat m_t}{\sqrt{\widehat v_t}+\epsilon}.
> $$
> 运算逐坐标进行，$\eta_t>0$、$\epsilon>0$；本页将初始参数记作 $\theta_1$。

## 直觉与解释

一阶统计量平滑梯度方向，二阶统计量记录梯度平方的尺度，分母据此调节各坐标步幅。$v_t$对应原始二阶矩的平滑估计，不是减去均值后的梯度方差。它同时依赖历史状态，因而相同当前梯度也可能产生不同更新；不能只看本次梯度大小来解释一步移动。

分母中的小正数避免零除，也改变非常小梯度下的尺度。算法仍需要选择学习率，不能由“自适应”推出任何步长都稳定。

小批量时应先求本批梯度，再逐坐标平方。这一般不同于逐样本梯度平方的平均；替换二者会改变二阶状态及后续步幅，并非同一公式的简单实现差异。

## 主要性质

独立说明零初始化的修正动机：递推展开得
$$
m_t=(1-\beta_1)\sum_{j=1}^t\beta_1^{t-j}g_j.
$$
若各时刻梯度均值同为 $\mu$，则 $E[m_t]=(1-\beta_1^t)\mu$，除以 $1-\beta_1^t$ 后期望为 $\mu$。若梯度平方的期望也恒定，$v_t$同理。训练中的分布一般随参数变化；这个推导不意味着对任意非平稳过程都得到了当前梯度矩的无偏估计。

公式给出确定的更新规则，但本页未证明收敛。历史动量、随机采样及非凸目标都使“每步下降”“达到全局最小”需要额外条件。Adam中加入L2梯度与直接对参数作衰减，还会经过不同的自适应缩放，不能直接沿用普通梯度下降的等价说法。

## 例子与边界

一维恒定梯度 $g_t=c\ne0$ 时，几何和给出 $\widehat m_t=c$、$\widehat v_t=c^2$，每步移动量为 $-\eta_tc/(|c|+\epsilon)$。例如 $c=2$ 时为 $-2\eta_t/(2+\epsilon)$，可直接检查实现的首步是否遗漏偏差修正。若所有历史梯度为零，则两个状态均为零，更新为零；这不排除零梯度所在位置是鞍点或极大值。

## 相关概念

- [[03 - 线性代数与优化/概念/随机梯度下降|随机梯度下降]]
- [[03 - 线性代数与优化/概念/梯度下降|梯度下降]]
- [[04 - 统计学习/概念/正则化|正则化]]
- [[06 - 深度学习/概念/反向传播|反向传播]]

## 相关习题

```dataview
TABLE WITHOUT ID file.link AS "习题", difficulty AS "难度", status AS "学习状态"
FROM #exercise
WHERE contains(file.outlinks, this.file.link)
SORT file.name ASC
```

## 来源与证明状态

Simon J. D. Prince，*Understanding Deep Learning*，2026-02-08修订稿，统一来源见[[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001教材台账]]。实际查看印刷90／PDF104的式(6.15)–(6.18)、偏差修正及批次梯度平方；本页用常见的两个衰减系数记号重写，$\epsilon$与原页一致放在平方根外。几何和推导及恒定梯度例子为独立补充；没有把正文的定性优化描述当成无条件收敛定理，也未运行Adam训练比较。 来源状态为部分核对，个人学习状态保持尚未开始。

