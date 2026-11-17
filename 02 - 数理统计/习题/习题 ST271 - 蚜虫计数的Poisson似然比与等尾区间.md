---
title: "习题 ST271：蚜虫计数的Poisson似然比与等尾区间"
topic: "mathematical-statistics"
topic_label: "数理统计"
difficulty: "intermediate"
status: "not-started"
tags: ["exercise", "mathematical-statistics"]
source: "George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第9章习题9.23，印刷页368／PDF物理页399"
source_id: "DS011"
source_chapter: 9
source_exercise: "9.23"
source_stars: 0
source_refs: ["DS011 Exercise 9.23，印刷368／PDF物理399", "DS011 Example 9.2.15及(9.2.17)，印刷351／PDF物理382"]
source_status: "verified"
solution_status: "independently-derived"
created: "2026-11-13"
---

# 习题 ST271：蚜虫计数的Poisson似然比与等尾区间

## 题目

### 英文原题

> [!question] 英文原题
> **9.23** (a) Let $X_1,\ldots,X_n$ be a random sample from a Poisson population with parameter $\lambda$ and define $Y=\sum X_i$. In Example 9.2.15 a confidence interval for $\lambda$ was found using the method of Section 9.2.3. Construct another interval for $\lambda$, by inverting an LRT, and compare the intervals.
> (b) The following data, the number of aphids per row in nine rows of a potato field, can be assumed to follow a Poisson distribution:
> $$
> 155,\quad104,\quad66,\quad50,\quad36,\quad40,\quad30,\quad35,\quad42.
> $$
> Use these data to construct a 90% LRT confidence interval for the mean number of aphids per row. Also, construct an interval using the method of Example 9.2.15.

### 中文转述

> [!question] 中文转述
> **原题9.23。**
> (a)  设$X_1,\ldots,X_n$为来自参数为$\lambda$的泊松总体的随机样本，定义$Y=\sum X_i$. 例9.2.15用节9.2.3的方法求得了$\lambda$的置信区间. 通过反演LRT构造$\lambda$的另一个区间，并比较这些区间.
>
> (b)  以下数据是某块马铃薯田中九行作物每行的蚜虫数，可以假定它们服从泊松分布：
>
> $$
> 155,\quad104,\quad66,\quad50,\quad36,\quad40,\quad30,\quad35,\quad42.
> $$
>
> 用这些数据为每行的平均蚜虫数构造$90\%$ LRT置信区间. 再用例9.2.15的方法构造一个区间.

## 提示

> [!hint]- 提示
> Poisson样本先约简为总数$Y$；对每个候选均值逐点按似然比标定检验，再与卡方等尾反演区间比较，别以Wilks截值冒充精确标定。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** 教材输入与补充假设另行标明。
>
> (a) $Y\sim\mathrm{Pois}(n\lambda)$，写$\mu=n\lambda$、$y=Y$，似然比$\Lambda_\mu(y)=e^{y-\mu}(\mu/y)^y$，$y=0$时为$e^{-\mu}$。精确非随机LRT可按似然比从小到大拒绝：定义$p_{\rm LR}(y;\mu)=\sum_{k:\Lambda_\mu(k)\le\Lambda_\mu(y)}e^{-\mu}\mu^k/k!$，拒绝$p_{\rm LR}\le\alpha$。它逐参数控制大小，反演$C(y)=\{\lambda:p_{\rm LR}(y;n\lambda)>\alpha\}$；边界随机化可取恰好大小。与此不同，共同卡方截值给近似区间$2[y\log(y/\mu)-y+\mu]\le\chi^2_{1,\alpha}$，不是有限样本精确校准。
> 例9.2.15等尾Garwood区间为$[q_{2y,\alpha/2}/(2n),q_{2(y+1),1-\alpha/2}/(2n)]$，$q$为下侧分位数，$y=0$下端取0。精确LRT按似然比排序，Garwood分别分配两尾；两者因离散性一般不同，均不应无证明宣称处处最短。
> (b) 实际总数$y=558,n=9,\bar x=62$。按上述有限Poisson求和与离散边界二分，精确非随机LRT端点约为$[57.77847723,66.44919766]$；上端因排序变化有跳跃，应以定义的$p_{\rm LR}>.1$决定端点是否包含，不把它当连续方程零点。相邻上端尾概率约$.101916$与$.0979123$。卡方近似LRT为$[57.78242163,66.41797820]$；Garwood为$[57.74688817,66.49441480]$。这些是同一单行均值的区间，未检验各行相同均值假设是否合理。
> 实际数据、算法、求和误差与结果见[[工具/StatisticalInference/ch9-computations/results.json|第9章数值结果]]；另以Chernoff双尾界限定可能接受范围，逐一检查该范围内全部232个排序区间及其内部驻点，数值只得到一个连通分量，避免仅靠二分遗漏小分量。Poisson求和省略上尾质量至多$10^{-14}$。

## 相关概念

- [[02 - 数理统计/概念/区间估计|区间估计]]
- [[02 - 数理统计/概念/假设检验|假设检验]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[01 - 概率论/概念/概率模型|概率模型]]

## 备注

- 统一来源见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011教材台账]]；原题位于[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=399|印刷368／PDF物理399]]。已对照原始页面核对完整英文、分题与定位，原题无星号。
- 解答为独立推导；引用的教材结论按source_refs核对，不使用答案册代替证明。
- 来源核对、归档与个人学习分别记录；verified只指所列来源核对范围，学习状态保持not-started。未实测Obsidian渲染。
