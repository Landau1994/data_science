---
title: "习题 P223：独立Gamma总和与比例的Beta分解"
topic: "probability-theory"
topic_label: "概率论"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "probability-theory"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第4章习题4.24，印刷页160／PDF物理页191"
source_id: "DS011"
source_chapter: 4
source_exercise: "4.24"
source_stars: 0
source_refs: ["DS011 Exercise 4.24，印刷160／PDF物理191"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 P223：独立Gamma总和与比例的Beta分解

## 题目

### 英文原题

> [!question] 英文原题
> **4.24** Let $X$ and $Y$ be independent random variables with $X\sim\operatorname{gamma}(r,1)$ and $Y\sim\operatorname{gamma}(s,1)$. Show that $Z_1=X+Y$ and $Z_2=X/(X+Y)$ are independent, and find the distribution of each. ($Z_1$ is gamma and $Z_2$ is beta.)

### 中文转述

> [!question] 中文转述
> **原题4.24。**
> 设 $X,Y$ 独立，$X\sim\operatorname{gamma}(r,1)$，$Y\sim\operatorname{gamma}(s,1)$. 证明 $Z_1=X+Y$ 与 $Z_2=X/(X+Y)$ 独立，并求各自分布. $Z_1$ 为 Gamma 分布，$Z_2$ 为 Beta 分布.

## 提示

> [!hint]- 提示
> 采用$(x,y)=(tu,t(1-u))$，Jacobian为$t$。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 参数$r,s>0$。逆变换$x=z_1z_2,y=z_1(1-z_2)$，支持$z_1>0,0<z_2<1$，绝对Jacobian$z_1$。于是
> $$
> f_{Z_1,Z_2}(t,u)=\frac{t^{r+s-1}e^{-t}}{\Gamma(r+s)}\frac{\Gamma(r+s)}{\Gamma(r)\Gamma(s)}u^{r-1}(1-u)^{s-1}.
> $$
> 右边是Gamma$(r+s,1)$和Beta$(r,s)$两个归一化密度的乘积，支持又为直积，故二者独立，边缘分别为题述两个分布。参数1在本题为尺度1。

## 相关概念

- [[01 - 概率论/概念/概率模型|概率模型]]
- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/条件概率|条件概率]]
- [[01 - 概率论/概念/期望|期望]]

## 备注

- 原题已对照[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=191|印刷第160页／PDF物理第191页]]；教材信息与进展见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。原题无星号。
- `source_status: verified`仅指本题题干、公式及所列来源定位已核对，不表示全章正文独立复证。解答写成不等于个人已完成练习，学习状态保持`not-started`；未实测Obsidian界面渲染。
