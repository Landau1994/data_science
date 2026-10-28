---
title: "Lasso回归"
aliases: ["Lasso", "Lasso Regression", "Least Absolute Shrinkage and Selection Operator", "L1-regularized Linear Regression"]
topic: statistical-learning
topic_label: 统计学习
tags:
  - concept
status: not-started
source: "An Introduction to Statistical Learning: with Applications in R（R 版第二版，2023-06-21 更正印刷），§6.2.2，式 (6.7)–(6.8)，印刷页 241–243 / PDF 物理页 252–254"
source_refs: ["DS013 §6.2.2，印刷241–243/PDF252–254"]
source_status: partially-verified
created: 2026-10-25
---

# Lasso回归

## 定义

> [!info] 定义
> Lasso 回归（least absolute shrinkage and selection operator）以系数的 $\ell_1$ 范数作惩罚：给定 $\lambda\ge0$，求
> $$
> (\hat\beta_0,\hat\beta)\in\arg\min_{\beta_0\in\mathbb R,\,\beta\in\mathbb R^p}
> \left\{\sum_{i=1}^n(y_i-\beta_0-x_i^{\mathsf T}\beta)^2+\lambda\sum_{j=1}^p|\beta_j|\right\}.
> $$
> 此处不惩罚截距，采用 RSS 约定。调整目标前的常数会改变同一数值 $\lambda$ 对应的解。

原书还给出约束形式：最小化 RSS，约束 $\sum_j|\beta_j|\le s$。给定惩罚问题的一个最优解，取 $s=\|\hat\beta\|_1$，该解也是相应约束问题的最优解：否则存在惩罚不更大而 RSS 更小的可行解，与原最优性矛盾。这里不宣称 $s$ 与 $\lambda$ 必有一一对应关系。

## 直觉与解释

绝对值在零点有尖角。足够弱的信号可能落在一个区间内，使最优系数恰好为零；Lasso 因而同时具有收缩（shrinkage）与变量选择（variable selection）的作用。有限样本选出的变量仍可能是噪声或其它变量的替代信号，不能据此认定因果作用或真实模型已恢复。

与 [[04 - 统计学习/概念/岭回归|岭回归]] 一样，特征尺度、截距处理和调参方法均属于模型定义的一部分。预处理和变量筛选应放在交叉验证的训练折内部。

## 主要性质

**软阈值——独立推导。** 先对数据中心化、单独处理截距。对单个非零特征向量 $x$，记 $a=x^{\mathsf T}x>0$、$c=x^{\mathsf T}y$，则目标中与 $\beta$ 有关的部分是 $a\beta^2-2c\beta+\lambda|\beta|$。在 $\beta>0$ 和 $\beta<0$ 分别求导，再检查零点两侧导数，得到
$$
\hat\beta=\frac{S(c,\lambda/2)}{a},\qquad
S(c,t)=\operatorname{sign}(c)\max\{|c|-t,0\}.
$$
若 $|c|\le\lambda/2$，左导数不大于零、右导数不小于零，故 $\hat\beta=0$。若 $X^{\mathsf T}X=I_p$，目标按坐标分离，同样得到 $\hat\beta_j=S((X^{\mathsf T}y)_j,\lambda/2)$。一般相关设计不能直接逐坐标使用这个闭式解。

**凸性与唯一性的区别。** RSS 与 $\ell_1$ 惩罚都凸，所以目标凸；当中心化后的 $X$ 满列秩时，RSS 严格凸，斜率解唯一。$p>n$ 时这一充分条件不成立，解可能不唯一。尽管如此，所有最优解的训练拟合值相同：若两个拟合向量不同，取两组系数的中点会由平方损失的严格凸性降低 RSS，而凸惩罚不增加，产生矛盾。

## 例子与边界

> [!example] 同一个零点阈值区间
> 对 $(2-\beta)^2+\lambda|\beta|$，解为 $\max\{2-\lambda/2,0\}$；当 $\lambda\ge4$ 时系数恰好为零。这与岭回归的一维连续收缩形成比较。

若两个特征列完全相同，Lasso 未必唯一分配系数。沿用中心化后的设计与响应记号，并取 $\lambda>0$；例如 $x_1=x_2=x$、$\|x\|_2=1$、$x^{\mathsf T}y>\lambda/2$，令 $t=x^{\mathsf T}y-\lambda/2>0$。任意 $\beta_1,\beta_2\ge0$ 且 $\beta_1+\beta_2=t$ 都最优：拟合只依赖两者之和，且 $|\beta_1|+|\beta_2|=t$。因此“选择了哪一列”可能缺乏稳定性，即使预测向量已经确定。

## 相关概念

- [[04 - 统计学习/概念/正则化|正则化]]；[[03 - 线性代数与优化/概念/凸函数|凸函数]]。
- [[04 - 统计学习/概念/岭回归|岭回归]]：平方和惩罚与唯一性。
- [[04 - 统计学习/概念/弹性网络|弹性网络]]：在稀疏惩罚之外增加平方和惩罚。
- [[04 - 统计学习/概念/高维回归|高维回归]]：高维下的结构约束和解释边界。
- [[04 - 统计学习/概念/模型选择|模型选择]]；[[04 - 统计学习/概念/模型评价|模型评价]]。

## 相关习题

```dataview
TABLE WITHOUT ID file.link AS "习题", difficulty AS "难度", status AS "学习状态"
FROM #exercise
WHERE contains(file.outlinks, this.file.link)
SORT file.name ASC
```

## 来源与证明状态

已逐页查看 James 等，*An Introduction to Statistical Learning: with Applications in R*，R 版第二版、2023-06-21 更正印刷，[[附件/books/ISLR.pdf#page=252|§6.2.2，印刷241–243／PDF252–254]] 原图，核对式 (6.7)–(6.8)、稀疏性、截距继承约定和图 6.6 的调参语境，见 [[00 - 首页/教材归档/DS013 - Introduction to Statistical Learning R|DS013 统一台账]]。惩罚解到约束解的论证、软阈值、唯一性边界、拟合值唯一性和重复特征例子为独立推导。没有核验变量选择一致性、误差界或运行教材数据实验；`partially-verified` 对应上述局部核对，学习状态保持 `not-started`。
