---
title: "习题 ST222：正态均值左侧UMP及双侧UMP不存在证明"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第8章习题8.32，印刷页330／PDF物理页361"
source_id: "DS011"
source_chapter: 8
source_exercise: "8.32"
source_stars: 0
source_refs: ["DS011 Exercise 8.32，印刷页330／PDF物理页361"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST222：正态均值左侧UMP及双侧UMP不存在证明

## 题目

### 英文原题

> [!question] 英文原题
> **8.32** Let $X_1,\ldots,X_n$ be iid n$(\theta,1)$, and let $\theta_0$ be a specified value of $\theta$.
> (a) Find the UMP, size $\alpha$, test of $H_0:\theta\ge\theta_0$ versus $H_1:\theta<\theta_0$.
> (b) Show that there does not exist a UMP, size $\alpha$, test of $H_0:\theta=\theta_0$ versus $H_1:\theta\ne\theta_0$.

### 中文转述

> [!question] 中文转述
> **原题8.32。**
> 设 $X_1,\ldots,X_n$ 独立同分布于 $\mathrm n(\theta,1)$，$\theta_0$ 为 $\theta$ 的指定值.
>
> (a)  求 $H_0:\theta\ge\theta_0$ 对 $H_1:\theta<\theta_0$ 的大小 $\alpha$ 一致最强检验.
>
> (b)  证明不存在 $H_0:\theta=\theta_0$ 对 $H_1:\theta\ne\theta_0$ 的大小 $\alpha$ 一致最强检验.

## 提示

> [!hint]- 提示
> 固定一个左备择和一个右备择，唯一最强拒绝域方向相反。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 设$0<\alpha<1$。
> (a) 拒绝$\sqrt n(\bar X-\theta_0)<-z_\alpha$，其中$P(Z>z_\alpha)=\alpha$。在边界$\theta_0$大小恰为$\alpha$；任意$\theta>\theta_0$向右平移使拒绝概率减小。对任意$\theta_1<\theta_0$，相对边界的似然比随$\bar X$严格递减，NP引理说明同一左尾检验最强；故为复合问题UMP。功效为$\Phi(-z_\alpha-\sqrt n(\theta-\theta_0))$。
> (b) 若存在双侧UMP，它对任一固定$\theta_-<\theta_0$必须等于(a)的唯一最强左尾检验（似然比严格且连续使无边界自由度）。但对任一$\theta_+>\theta_0$，唯一最强检验是相反的右尾$\sqrt n(\bar X-\theta_0)>z_\alpha$。当$0<\alpha<1$时两域在正原假设概率集合上不同，矛盾。$\alpha=0,1$的平凡端点另论，不能把不存在结论无条件含入端点。

## 相关概念

- [[02 - 数理统计/概念/假设检验|假设检验（hypothesis testing）]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 完整原题已逐页对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=361|印刷330／PDF物理361]]；原题无星号。教材信息及归档进度见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 来源已核对与独立解答写成不等于个人已完成练习；学习状态保留`not-started`。未实测Obsidian界面渲染。
