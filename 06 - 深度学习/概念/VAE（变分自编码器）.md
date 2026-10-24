---
title: 变分自编码器
aliases:
  - Variational Autoencoder
  - VAE
  - Amortized Variational Inference
topic: deep-learning
topic_label: 深度学习
tags:
  - concept
  - deep-learning
status: not-started
source: "理解深度学习（Understanding Deep Learning，2026-02-08修订稿），第17.4.1节（印刷页334／PDF物理页348）、第17.5–17.6节（印刷页336／PDF物理页350）与第17.7节（印刷页339／PDF物理页353）"
source_status: partially-verified
created: 2026-10-24
---

# 变分自编码器

## 定义

> [!info] 变分自编码器（variational autoencoder，VAE）
> 将潜变量生成模型 $p_\theta(x,z)=p(z)p_\theta(x\mid z)$ 与可学习的近似后验 $q_\phi(z\mid x)$ 结合，通常通过最大化数据的证据下界训练。编码器输出近似后验的参数，解码器给出条件分布的参数；两者并非一般意义上的可逆函数。

本页 $\log$ 采用自然对数，相对熵的单位为 nat；[[01 - 概率论/概念/相对熵|相对熵]]页采用以2为底的 bit，二者满足 $D_{\mathrm{nat}}=(\ln 2)D_{\mathrm{bit}}$。改变底数时，正则化系数或目标中的相应权重也须一致换算。

## 直觉与解释

编码器与解码器常用[[06 - 深度学习/概念/神经网络|神经网络]]参数化：前者把观测映射到近似后验的分布参数，后者把潜变量映射到观测条件分布的参数。网络输出的参数与这些概率分布应加以区分，不能把两个网络直接理解为互逆的确定性映射。

普通重构网络把输入压缩后再还原；VAE 额外指定潜变量先验和观测概率模型，希望既解释训练数据，又能从先验采样生成新数据。编码器不是输出唯一“真实编码”，而是近似输入对应的潜变量后验。

同一个编码网络处理许多输入，称为摊销推断（amortized inference）：不必为每个样本从头优化一套后验参数，但共享网络可能引入额外近似误差。重构项好看不等于后验准确，也不代表从先验抽样就一定生成高质量对象。

## 主要性质

固定 $x$，在 $0<p_\theta(x)<\infty$、$q_\phi$ 对真实后验绝对连续且相关积分有限时，[[05 - 概率模型与推断/概念/变分推断|变分推断]]页的独立分解给出
$$
\mathcal L(\theta,\phi;x)=E_{q_\phi(z\mid x)}\log p_\theta(x\mid z)-\operatorname{KL}(q_\phi(z\mid x)\|p(z))\le\log p_\theta(x).
$$
因此训练通常最大化 $\mathcal L$，或最小化其负值，不能颠倒不等号。上式的“重构项”由观测分布决定；只有在特定固定方差高斯观测模型下，负对数似然才与平方误差相差固定比例和常数。

若编码分布为对角高斯，可写
$$
z=\mu_\phi(x)+\sigma_\phi(x)\odot\varepsilon,\qquad \varepsilon\sim N(0,I),\quad\sigma_\phi(x)>0.
$$
这是重参数化（reparameterization）：随机源不依赖 $\phi$，可在可微和允许交换微分与期望的条件下，用链式法则构造路径导数估计。它不是任意离散潜变量的通用可微公式；随机估计仍有方差，梯度存在也不保证优化收敛。

## 例子与边界

> [!example] 一维线性高斯解码器
> 设 $Z\sim N(0,1)$，$X=aZ+\eta$，其中 $\eta\sim N(0,\tau^2)$ 与 $Z$ 独立且 $\tau>0$。条件对数密度等于 $-(x-az)^2/(2\tau^2)-\tfrac12\log(2\pi\tau^2)$，所以重构项是该平方误差在 $q_\phi$ 下的负期望，加上明确常数。若近似后验恰为真实后验，ELBO 与对数证据相等；任意编码器通常没有这个保证。

例中若改变或学习 $\tau$，归一化项也随参数变化，不能只保留平方误差而声称目标完全相同。KL 项的缩放改为任意系数时，也须重新说明目标与原始 ELBO 的关系。

## 相关概念

- [[06 - 深度学习/概念/神经网络|神经网络]]：编码器与解码器可使用网络参数化，概率模型与训练目标还须另行指定。
- [[05 - 概率模型与推断/概念/潜变量|潜变量]]；[[05 - 概率模型与推断/概念/生成模型|生成模型]]；[[05 - 概率模型与推断/概念/变分推断|变分推断]]。
- [[01 - 概率论/概念/相对熵|相对熵]]；[[06 - 深度学习/概念/深度学习|深度学习]]；[[06 - 深度学习/概念/反向传播|反向传播]]。

## 相关习题

```dataview
TABLE WITHOUT ID file.link AS "习题", difficulty AS "难度", status AS "学习状态"
FROM #exercise
WHERE contains(file.outlinks, this.file.link)
SORT file.name ASC
```

## 来源与证明状态

Simon J. D. Prince，*Understanding Deep Learning*，本地 2026-02-08 修订稿，见 [[00 - 首页/教材归档/DS001 - Understanding Deep Learning|DS001 统一教材台账]]。本轮实读第 17.4.1 节印刷页 334／PDF 物理页 348 的 ELBO–KL 分解式 (17.17)；第 17.5–17.6 节印刷页 336／PDF 物理页 350 的编码分布及目标式 (17.20)–(17.21)；第 17.7 节印刷页 339／PDF 物理页 353 的重参数化式 (17.25)，后两页已核对原图。本页统一记号，并独立推导高斯观测项；梯度期望关系另需交换条件。局部核对不包含全章证明审计、训练收敛或实际生成质量。
