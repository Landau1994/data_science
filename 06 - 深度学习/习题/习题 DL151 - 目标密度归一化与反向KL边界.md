---
title: "习题 DL151：目标密度归一化与反向KL边界"
topic: deep-learning
topic_label: 深度学习
difficulty: advanced
status: not-started
tags:
  - exercise
  - deep-learning
source: "Understanding Deep Learning（2026-02-08 修订稿），Problem 16.11，印刷326／PDF物理340"
source_id: DS001
source_chapter: 16
source_exercise: "16.11"
source_refs: ["DS001 Problem 16.11*，印刷326/PDF340", "DS001 式(16.25)，印刷321/PDF335", "DS002 Answer to Problem16.11，印刷62/PDF62"]
source_status: verified
solution_status: independently-derived
created: 2026-10-28
---

# 习题 DL151：目标密度归一化与反向KL边界

## 题目

### 英文原题

> [!question] 英文原题
> **Problem 16.11\*** Write out the expression for the KL divergence in equation 16.25. Why does it not matter if we can only evaluate the probability $q(\mathbf x)$ up to a scaling factor $\kappa$? Does the network have to be invertible to minimize this loss function? Explain your reasoning.

### 中文转述

> [!question] 中文转述
> 展开式 (16.25) 的 KL 散度；解释只知道目标密度到常数尺度 $\kappa$ 为何无碍；讨论最小化该损失是否要求网络可逆。


## 提示

> [!hint]- 提示
> 区分答案册写的负对数目标密度与真正的反向 KL；后者还含模型自身的熵。

## 解答

> [!success]- 解答
> 独立推导，并区分原书形式写法。对具有密度的推前分布 $p_\phi$，真正的反向 KL 是
> $$
> D_{\rm KL}(p_\phi\Vert q)=E_{x\sim p_\phi}[\log p_\phi(x)-\log q(x)].
> $$
> 若 $x=f_\phi(z)$ 是可微可逆的同维映射，则可不显式求逆而在已知 $z$ 处计算
> $$
> D_{\rm KL}=E_z[\log p_Z(z)-\log|\det Df_\phi(z)|-\log q(f_\phi(z))].
> $$
> 这包含模型熵对应的雅可比项，通常依赖参数，不能删除。若 $\widetilde q=\kappa q$，其中 $\kappa>0$ 与 $\phi$ 无关，则目标仅减少常数 $\log\kappa$，梯度和极小解不变。
>
> **原书及答案册的边界。** 式 (16.25) 把经验点质量 $I^{-1}\sum_i\delta_{f_\phi(z_i)}$ 与连续目标写成 KL。严格测度意义下前者对后者不绝对连续，KL 为无穷，不能直接将其展开成有限密度积分。答案册给出的
> $$
> L_{\rm book}=-\sum_i\log q(f_\phi(z_i))
> $$
> 可以作为单独的交叉熵目标来计算，确实不要求 $f$ 可逆，只要前向及梯度存在；但它不是上面的完整反向 KL，可能把全部样本坍缩到 $q$ 的模态。例如映到任意同一模态的常值网络即可改善这项损失。
>
> 因此“不需显式逆运算”不等于“可把模型熵删去”。若使用真正的反向 KL，至少须能定义并计算或估计 $p_\phi$ 的密度/熵；非可逆生成器并不自动满足这一点。若仅使用答案册的 $L_{\rm book}$，可逆性则不是计算该有限和的必要条件。

## 相关概念

- [[06 - 深度学习/概念/归一化流|归一化流]]：可逆变换、雅可比与密度变换。
- [[01 - 概率论/概念/相对熵|相对熵]]：KL、绝对连续性与交叉熵。

## 备注

- 原题：[[附件/books/UnderstandingDeepLearning_02_09_26_C.pdf#page=340|印刷 326／PDF 340]]；教材记录见 [[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001]]。
- 题干、公式及所引原页已核对；解答为独立推导。保留并指出原书经验点质量KL与答案册省略模型熵项的区别，未将两种目标混称为同一损失。

- 答案册对照：[[附件/books/UDL_Answer_Booklet_Students.pdf#page=62|DS002，印刷62／PDF62，16.11解答]]；实际核对其交叉熵公式及无需逆映射的说明，独立解答保留上述区别。
