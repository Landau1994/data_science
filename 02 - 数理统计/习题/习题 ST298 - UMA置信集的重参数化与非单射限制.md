---
title: "习题 ST298：UMA置信集的重参数化与非单射限制"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第9章习题9.50，印刷页372／PDF物理页403"
source_id: "DS011"
source_chapter: 9
source_exercise: "9.50"
source_stars: 0
source_refs: ["DS011 Exercise 9.50，印刷372／PDF物理403"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST298：UMA置信集的重参数化与非单射限制

## 题目

### 英文原题

> [!question] 英文原题
> **9.50** Let $X\sim f(x|\theta)$, and suppose that the interval $\{\theta:a(X)\le\theta\le b(X)\}$ is a UMA confidence set for $\theta$.
> (a) Find a UMA confidence set for $1/\theta$. Note that if $a(x)<0<b(x)$, this set is $\{1/\theta:1/b(x)\le1/\theta\}\cup\{1/\theta:1/\theta\le1/a(x)\}$. Hence it is possible for the UMA confidence set to be neither an interval nor bounded.
> (b) Show that, if $h$ is a strictly increasing function, the set $\{h(\theta):h(a(X))\le h(\theta)\le h(b(X))\}$ is a UMA confidence set for $h(\theta)$. Can the condition on $h$ be relaxed?

### 中文转述

> [!question] 中文转述
> **原题9.50。**
> 设$X\sim f(x\mid\theta)$，假设区间$\{\theta:a(X)\le\theta\le b(X)\}$为$\theta$的UMA置信集.
>
> (a)  求$1/\theta$的UMA置信集. 注意，若$a(x)<0<b(x)$，则此集合为$\{1/\theta:1/b(x)\le1/\theta\}\cup\{1/\theta:1/\theta\le1/a(x)\}$. 因而UMA置信集可能既非区间，也无界.
>
> (b)  证明：若$h$严格递增，则集合$\{h(\theta):h(a(X))\le h(\theta)\le h(b(X))\}$为$h(\theta)$的UMA置信集. 对$h$的条件能否放宽？

## 提示

> [!hint]- 提示
> 先求原置信集在映射$h$下的完整像；倒数跨0时必须拆成两个分支，再用一一重参数化比较错误覆盖事件。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> 先将参数空间限制为倒数有定义的$\theta\ne0$。
> (a) 取$D(X)=\{1/\theta:\theta\in[a(X),b(X)]\cap\Theta\}$。若区间在零的一侧，则$D=[1/b,1/a]$；若$a<0<b$，则$D=(-\infty,1/a]\cup[1/b,\infty)$，等于原题两个半线并集；端点恰为0时取相应极限，零本身不取倒数。真值覆盖事件与原集合完全相同。
> (b) 令$\eta=h(\theta)$、$h$为一一可测变换且有可测逆。在对应参数空间中，对任意候选置信程序$D'$可拉回$C'=h^{-1}(D')$，保持真值覆盖率及任意一对真、假参数的覆盖概率。若原$C$在这些比较中一致最准确，$h(C)$也一致最准确，否则反向拉回会反驳原最优性。严格递增时像集写成$[h(a),h(b)]\cap h(\Theta)$，严格递减时交换端点；更一般一一变换也保留集合意义的两侧UMA，但未必保留区间或单侧错误方向。非单射变换把多个参数合成同一目标值，错误覆盖对应原参数集合而非单一点，原UMA性质通常不能直接推出，需重新处理干扰参数与复合检验。若讨论单侧UMA，则须保持或相应反转次序，不能对任意非单调映射照搬单侧结论。

## 相关概念

- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=403|印刷372／PDF物理403]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
