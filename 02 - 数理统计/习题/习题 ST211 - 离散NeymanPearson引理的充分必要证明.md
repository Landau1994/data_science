---
title: "习题 ST211：离散NeymanPearson引理的充分必要证明"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "advanced"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.21，印刷页329／PDF物理页360"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.21"
source_stars: 0
source_refs: ["DS011 Exercise 8.21，印刷页329／PDF物理页360", "DS011 所引正文，印刷315／PDF物理346"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST211：离散NeymanPearson引理的充分必要证明

## 题目

### 英文原题

> [!question] 英文原题
> **8.21** In the proof of Theorem 8.3.12 (Neyman–Pearson Lemma), it was stated that the proof, which was given for continuous random variables, can easily be adapted to cover discrete random variables. Provide the details, that is, prove the Neyman–Pearson Lemma for discrete random variables. Assume that the $\alpha$ level is attainable.

### 中文转述

> [!question] 中文转述
> **原题8.21。**
> 定理8.3.12（Neyman–Pearson 引理）的证明指出，对连续随机变量给出的证明很容易适配到离散情形. 补出细节，即证明离散随机变量的 Neyman–Pearson 引理. 假定给定的 $\alpha$ 水平可达到.

## 提示

> [!hint]- 提示
> 把非负积分改成可数求和，并完整处理等号条件。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 在可数共同样本空间上记pmf为$f_0,f_1$，取$k\ge0$及检验$\phi$：$f_1>kf_0$处为1，$f_1<kf_0$处为0，等号处可选择以使$\sum\phi f_0=\alpha$。对任意水平$\alpha$的竞争检验$0\le\psi\le1$，逐点有$(\phi-\psi)(f_1-kf_0)\ge0$，且其绝对值被$f_1+kf_0$控制，可求和。于是
> $$E_1\phi-E_1\psi\ge k(E_0\phi-E_0\psi)=k(\alpha-E_0\psi)\ge0.$$
> 证明充分性；简单备择下最强即UMP。
> 必要性按原定理要求$k>0$：若$\psi$也最强，则左端为0，上述不等式强迫$E_0\psi=\alpha$且非负级数之和为0，故每个$(\phi-\psi)(f_1-kf_0)=0$。在$f_1>kf_0$处必须$\psi=1$，在$f_1<kf_0$处必须$\psi=0$，除去$f_0=f_1=0$的不可观察点；等号处仍可任意选择满足大小。这正是定理的必要条件。题设“可达到”确保所需选择存在；非随机化不总能达到任意给定$\alpha$，允许边界随机化则可达到。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=360|印刷329／PDF物理360]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 引用输入实际核对页：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=346|印刷315／PDF物理346]]；解答已重述所需假设及结果。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
