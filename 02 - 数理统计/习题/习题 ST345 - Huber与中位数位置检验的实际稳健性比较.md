---
title: 习题 ST345：Huber与中位数位置检验的实际稳健性比较
topic: mathematical-statistics
topic_label: 数理统计
difficulty: advanced
status: not-started
tags:
- exercise
- mathematical-statistics
source: George Casella、Roger L. Berger《Statistical Inference》（2001年第2版的2024年CRC重印），第10章习题10.39，印刷页415／PDF物理页446
source_id: DS011
source_chapter: 10
source_exercise: '10.39'
source_stars: 0
source_refs:
- DS011 Exercise 10.39，印刷415／PDF物理446
- DS011题内依赖核对：印刷400／PDF物理431；印刷401／PDF物理432
source_status: verified
solution_status: independently-derived
created: '2026-11-13'
---

# 习题 ST345：Huber与中位数位置检验的实际稳健性比较

## 题目

### 英文原题

> [!question] 英文原题
> **10.39** Expand the comparisons made in Example 10.3.7.
>
> (a) Another test based on Huber's M-estimator would be one that used a variance estimate, based on (10.3.6). Examine the performance of such a test statistic, and comment on its desirability (or lack thereof) as an alternative to either (10.3.8) or (10.3.9).
>
> (b) Another test based on Huber's M-estimator would be one that used a variance from a bootstrap calculation. Examine the performance of such a test statistic.
>
> (c) A robust competitor to $\hat\theta_M$ is the median. Examine the performance of tests of a location parameter based on the median.

### 中文转述

> [!question] 中文转述
> **原题10.39。** 扩展例10.3.7中的比较.
>
> (a)  另一种基于Huber $M$估计量的检验，可以使用式(10.3.6)的方差估计. 考察这种检验统计量的表现，评价它作为式(10.3.8)或式(10.3.9)替代量的优点（或不足）.
>
> (b)  另一种基于Huber $M$估计量的检验，可以使用自助法计算的方差. 考察这种检验统计量的表现.
>
> (c)  $\hat\theta_M$的一个稳健竞争者是中位数. 考察基于中位数的位置参数检验的表现.

## 提示

> [!hint]- 提示
> 先核对(10.3.8)分母印刷式，再明确总体、样本量、预定临界值和Monte Carlo误差。

## 解答

> [!success]- 解答
> **证明范围：独立推导。** **共同实施。** 独立考察标准正态、标准$t_5$、标准Logistic、尺度1双指数四个对称位置模型；每模型实际模拟3000个$n=15$样本，$k=1.5$固定，$H_0:\theta=0$，双侧名义水平.1。真实总体标准差依次$1,\sqrt{5/3},\pi/\sqrt3,\sqrt2$，替代位置为$0,.25\sigma,.5\sigma,.75\sigma,\sigma,2\sigma$。同一未平移样本按位置等变性用于各替代，既省计算又严格保持该模型实验；没有假装各列相互独立实验。
>
> **(a)** 令残差$r_i=X_i-\hat\theta_H$、$A_n=n^{-1}\sum I(|r_i|<k)$、$B_n=n^{-1}\sum\min(r_i^2,k^2)$。正确夹心估计(10.3.6)为$\hat V_1=B_n/A_n^2$，标准误$\sqrt{\hat V_1/n}$。原(10.3.8)打印分母为$(1-A_n)^2$，而非$A_n^2$，所以打印值$\hat V_2=B_n/(1-A_n)^2$不一致；若补正分母，它与$\hat V_1$在连续样本中逐点相同，不是另一个竞争者。naive(10.3.9)为$\hat V_3=n^{-1}\sum r_i^2$。本次分别保留打印式与正确式以展示差别。$A_n=1$时打印式为$\infty$，相应检验不拒绝；四模型此类样本数分别453、162、5、89，明确计入，没有丢掉。
>
> **(b)** 每个原样本再独立有放回重抽199次，逐次求Huber根。bootstrap标准误为这些根的样本标准差，检验统计量$(\hat\theta_H-0)/s_H^*$；这里$s_H^*$已是估计量的标准误，不应再乘或除$\sqrt n$。每个模型使用固定独立种子2026111439至2026111442；二分求根最大绝对得分残差实际小于$2.1\times10^{-9}$。
>
> **(c)** 用同一199次成对索引重抽样分别计算中位数，以其bootstrap标准差$s_M^*$构造$M_n/s_M^*$。这是数据内估计标准误的中位数检验，未使用未知真密度。所有方法统一与$z_{.95}=1.6448536$比较，实际完整功效表如下：
>
> **正态：**
>
> |位置偏移/σ|正确夹心|打印10.3.8|naive|Huber bootstrap|中位数bootstrap|
> |---:|---:|---:|---:|---:|---:|
> |0|0.1313|0.0000|0.1373|0.1313|0.1193|
> |0.25|0.2720|0.0000|0.2823|0.2733|0.2033|
> |0.5|0.6203|0.0000|0.6377|0.6220|0.4470|
> |0.75|0.8800|0.0003|0.8907|0.8780|0.7180|
> |1|0.9797|0.0040|0.9837|0.9807|0.8880|
> |2|1.0000|0.1897|1.0000|1.0000|0.9997|
>
> **t5：**
>
> |位置偏移/σ|正确夹心|打印10.3.8|naive|Huber bootstrap|中位数bootstrap|
> |---:|---:|---:|---:|---:|---:|
> |0|0.1320|0.0003|0.1237|0.1283|0.1093|
> |0.25|0.3150|0.0013|0.2863|0.3120|0.2460|
> |0.5|0.6967|0.0070|0.6687|0.6847|0.5670|
> |0.75|0.9323|0.0313|0.9117|0.9310|0.8333|
> |1|0.9897|0.0963|0.9873|0.9890|0.9530|
> |2|1.0000|0.5847|1.0000|1.0000|0.9997|
>
> **Logistic：**
>
> |位置偏移/σ|正确夹心|打印10.3.8|naive|Huber bootstrap|中位数bootstrap|
> |---:|---:|---:|---:|---:|---:|
> |0|0.1257|0.0077|0.1243|0.1163|0.0967|
> |0.25|0.3023|0.0460|0.2967|0.2913|0.2300|
> |0.5|0.6527|0.1827|0.6653|0.6470|0.5117|
> |0.75|0.8883|0.4373|0.9023|0.8857|0.7790|
> |1|0.9797|0.7090|0.9830|0.9777|0.9253|
> |2|1.0000|0.9767|1.0000|1.0000|0.9997|
>
> **双指数：**
>
> |位置偏移/σ|正确夹心|打印10.3.8|naive|Huber bootstrap|中位数bootstrap|
> |---:|---:|---:|---:|---:|---:|
> |0|0.1207|0.0010|0.0910|0.1153|0.0823|
> |0.25|0.3540|0.0010|0.2983|0.3440|0.2847|
> |0.5|0.7383|0.0133|0.6833|0.7240|0.6690|
> |0.75|0.9413|0.0697|0.9207|0.9387|0.8967|
> |1|0.9917|0.1967|0.9850|0.9883|0.9737|
> |2|0.9997|0.7483|0.9997|0.9997|0.9993|
>
>
> 在零假设行，正确夹心与Huber bootstrap拒绝率约.116–.132，仍高于名义.1；中位数bootstrap约.082–.119，四模型中较接近但并非精确控制。打印(10.3.8)拒绝率极低，不能把其低拒绝率误认为优良校准，代价是功效下降；修正后的(10.3.8)与(10.3.6)本来相同。不同总体、位置和方法的实际结果均有抽样误差，每个概率在.9或.1附近Monte Carlo标准误约.00548，最坏约.00913，不能对千分位差异作显著优劣声称。bootstrap也未自动纠正小样本正态临界值的乐观性。
>
> 全部12000个原始15维样本、估计量、五种标准误及每个概率记录在[[work/DS011/ch10/robust-results.json|模拟结果]]与对应samples.csv。

## 相关概念

- [[01 - 概率论/概念/随机变量|随机变量]]
- [[01 - 概率论/概念/期望|期望]]
- [[02 - 数理统计/概念/统计推断|统计推断]]
- [[02 - 数理统计/概念/参数估计|参数估计]]
- [[02 - 数理统计/概念/重采样|重采样]]
- [[02 - 数理统计/概念/假设检验|假设检验]]

## 备注

- 来源：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=446|印刷第415页／PDF物理第446页]]；版本与归档见[[00 - 首页/教材归档/DS011 - Statistical Inference|DS011统一台账]]。
- 实读例10.3.7、式(10.3.6)–(10.3.9)及表10.3.6：印刷400–401／PDF431–432。打印分母与正确公式分开计算；原表10000次仅作模型背景，本次实际为每模型3000、每样本199重抽，不冒称原规模。
- 已实读本题所用正文：[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=431|印刷400／PDF物理431]]；[[附件/books/George Casella, Roger Berger - Statistical Inference (Chapman & Hall_CRC Texts in Statistical Science) (2024, Chapman and Hall_CRC) - libgen.li.pdf#page=432|印刷401／PDF物理432]]；其余题内外部文献仅保留原引用，未声称查阅。
- 英文原题逐题对照PDF原始页面，保留原分题、提示、引用及可见疑误；原题无星号。题内引用补充与独立解答不混入原文；未查阅答案册或题内外部文献。
- 来源核对不表示个人学习完成，学习状态保持not-started。公式、链接与元数据检查不等于Obsidian实际渲染检查。
