---
title: "习题 ML011：College数据的正则化与降维回归"
topic: statistical-learning
topic_label: 统计学习
difficulty: intermediate
status: not-started
tags:
  - exercise
  - statistical-learning
source: "[[00 - 首页/教材归档/DS013 - Introduction to Statistical Learning R|ISLR（DS013）]]"
source_id: DS013
source_chapter: 6
source_exercise: "6.9"
source_refs: ["DS013 §6.6，Exercise 9(a)–(g)，印刷287/PDF298"]
source_status: verified
solution_status: computationally-checked
created: 2026-10-25
---

# 习题 ML011：College数据的正则化与降维回归

## 题目

### 英文原题

> [!question] 英文原题
> **9.** In this exercise, we will predict the number of applications received using the other variables in the `College` data set.
>
> (a) Split the data set into a training set and a test set.
>
> (b) Fit a linear model using least squares on the training set, and report the test error obtained.
>
> (c) Fit a ridge regression model on the training set, with $\lambda$ chosen by cross-validation. Report the test error obtained.
>
> (d) Fit a lasso model on the training set, with $\lambda$ chosen by cross-validation. Report the test error obtained, along with the number of non-zero coefficient estimates.
>
> (e) Fit a PCR model on the training set, with $M$ chosen by cross-validation. Report the test error obtained, along with the value of $M$ selected by cross-validation.
>
> (f) Fit a PLS model on the training set, with $M$ chosen by cross-validation. Report the test error obtained, along with the value of $M$ selected by cross-validation.
>
> (g) Comment on the results obtained. How accurately can we predict the number of college applications received? Is there much difference among the test errors resulting from these five approaches?

### 中文转述

> [!question] 中文转述
> **ISLR 第 6 章第 9 题，全部 (a)–(g)。** 用 `College` 数据中的其他变量预测收到的申请数量（`Apps`）。
>
> (a) 将数据划分为训练集与测试集。
>
> (b) 在训练集上用最小二乘法（least squares）拟合线性模型，报告测试误差。
>
> (c) 在训练集上拟合岭回归（ridge regression），用交叉验证选择 $\lambda$，报告测试误差。
>
> (d) 在训练集上拟合 Lasso，用交叉验证选择 $\lambda$，报告测试误差和非零系数的数量。
>
> (e) 在训练集上拟合主成分回归（principal components regression，PCR），用交叉验证选择成分数 $M$，报告测试误差和选定的 $M$。
>
> (f) 在训练集上拟合偏最小二乘回归（partial least squares，PLS），用交叉验证选择 $M$，报告测试误差和选定的 $M$。
>
> (g) 讨论五种方法的结果：申请数量能预测得多准确，各方法测试误差之间的差异是否明显？

## 提示

> [!hint]- 提示 1
> 五种方法共用同一训练／测试划分和训练集折号，才能清楚比较。测试集只用于最终评价；标准化、PCR 方向和 PLS 方向应在每个训练折中重新学习。

> [!hint]- 提示 2
> 明确测试误差是均方误差；若报告均方根误差，应另行标记。PCR／PLS 的成分数与 Lasso 的非零原变量系数数目不是同一概念。

## 解答

> [!success]- 解答
> **解答范围：独立分析方案、已实际运行的 R 分析与有限计算核验。** 配套 [[工具/ISLR/islr_ch6_applied.R|应用题脚本]] 已于 2026-10-25 在 WSL 的 Ubuntu 20.04.6 LTS、R 4.3.1 中执行题号 `6.9`；执行时的 [[工具/ISLR/运行结果/2026-10-25/analysis-script.R|代码快照]]、[[工具/ISLR/运行结果/2026-10-25/6.9/comparison.csv|比较结果]]、数据快照、划分及各方法输出均保留。以下数值仅支持这次数据版本、划分、候选参数与软件环境。
>
> **(a) 数据与评价设计。** 实际输入为 `ISLR2` 1.3.2 的 `College`，共 777 所学校，响应为 `Apps`，其他数据列作候选预测变量，学校名称只作为行标识。种子为 20261025；随机抽取 543 行作训练集，234 行作测试集；训练集使用固定五折交叉验证。[[工具/ISLR/运行结果/2026-10-25/6.9/split.csv|逐行划分]]及[[工具/ISLR/运行结果/2026-10-25/6.9/folds.csv|折号]]已保存，折 1–5 的样本数依次为 109、109、109、108、108。类别变量按固定数据模式展开为虚拟变量，本次设计含 17 个斜率；不从全数据估计中心、尺度或方向。脚本另保存了实际输入的 RDS 快照。
>
> 对测试行集合 $T$，统一采用
> $$
> \operatorname{MSE}_{\rm test}=\frac{1}{|T|}\sum_{i\in T}(\mathrm{Apps}_i-\widehat{\mathrm{Apps}}_i)^2.
> $$
> 它的单位是“申请数量的平方”；$\sqrt{\operatorname{MSE}_{\rm test}}$ 才与申请数量同单位。
>
> **(b) 最小二乘基线。** 在全部训练数据上拟合含截距的线性模型，在保留的测试行上预测，测试 MSE 为 **1,300,720.26**。其五折 CV MSE 为 **1,282,420.06**，作为训练内方法选择的比较基线；没有用训练残差代替测试误差。
>
> **(c) 岭回归。** 对预先给定的 100 点对数网格 $\lambda\in[10^{-4},10^5]$，用相同的五折划分选择折外均方误差最小的权重。各折内部标准化，截距不受惩罚；选定后用全部训练资料重拟合，最后测试。脚本中的 `glmnet(alpha=0)` 表示岭回归。本次选得 $\lambda=10^{-4}$，CV MSE 为 **1,282,480.81**，测试 MSE 为 **1,300,695.03**。所选权重位于预设网格下边界，只是该网格内最优；本次未扩展网格。
>
> **(d) Lasso。** 使用 `glmnet(alpha=1)`、相同折号与参数网格。本次也选得 $\lambda=10^{-4}$，CV MSE 为 **1,282,816.23**，测试 MSE 为 **1,300,630.41**。[[工具/ISLR/运行结果/2026-10-25/6.9/lasso-coefficients.csv|原尺度系数表]]显示全部 **17 个斜率非零**，所以这次选定的 Lasso 没有筛掉候选预测变量。非零计数不含截距，若连同非零截距一起计则为 18。其权重同样处于网格下边界，只能报告该网格内最优，本次未扩展网格。
>
> **(e) PCR。** 在每个训练折内重新中心化、缩放并学习主成分方向，评价 $M=0,1,\ldots,17$；$M=0$ 是截距基线，并列时选较小 $M$。本次选得 **$M=17$**，在全部训练资料上重学方向并拟合后的测试 MSE 为 **1,300,720.26**，CV MSE 为 **1,282,420.06**。所选成分数等于候选上限，保留全部 17 个预测方向，本次没有产生降维；其误差在数值精度内与最小二乘重合。没有先用全数据做 PCA 再交叉验证回归。
>
> **(f) PLS。** 使用与 PCR 相同的折号、候选 $M$ 及误差准则；PLS 方向只由该折训练输入与响应共同确定。本次也选得 **$M=17$**，重拟合后的测试 MSE 为 **1,300,720.26**，CV MSE 为 **1,282,420.06**。同样保留全部成分，结果在数值精度内与最小二乘重合。成分数与非零原变量系数数量不是同一个概念。
>
> **(g) 本次结果与讨论。** 下表直接汇总实际输出；MSE 四舍五入至两位小数，RMSE 的单位为申请数量。
>
> | 方法 | 选定参数 | 五折 CV MSE | 测试 MSE | 测试 RMSE | 非零斜率数 |
> | --- | --- | ---: | ---: | ---: | ---: |
> | 最小二乘 | 无惩罚 | 1,282,420.06 | 1,300,720.26 | 1,140.49 | 17 |
> | 岭回归 | $\lambda=10^{-4}$ | 1,282,480.81 | 1,300,695.03 | 1,140.48 | 17 |
> | Lasso | $\lambda=10^{-4}$ | 1,282,816.23 | 1,300,630.41 | 1,140.45 | 17 |
> | PCR | $M=17$ | 1,282,420.06 | 1,300,720.26 | 1,140.49 | 17 |
> | PLS | $M=17$ | 1,282,420.06 | 1,300,720.26 | 1,140.49 | 17 |
>
> 本次五种方法测试 MSE 的最大差为 **89.85**，约占最大测试 MSE 的 **0.00691%**；RMSE 均约为 **1,140 份申请**。在这次划分和参数集合内，五种方法没有显示明显的预测差异。RMSE 不是每所学校的误差上限；本次 234 所测试学校的实际申请数量从 152 到 21,804 不等，平均为 2,999.28，平方损失可能受申请数量较大的学校影响。未做误差差异的显著性检验，也不能据此推断所有划分或未来学校的表现相同。
>
> [[工具/ISLR/运行结果/2026-10-25/6.9/selection.txt|方法选择记录]]按训练 CV MSE 的精确最小值选择 **PLS**。原始 CV MSE 中 OLS、PCR 均为 `1282420.05683195`，PLS 为 `1282420.05683194`，差异仅约 $10^{-8}$，属于浮点数值精度，不能据此声称 PLS 实质优于最小二乘或 PCR。Lasso 的测试 MSE 虽略小，本次并未依据测试分数改选方法。
>
> 两种惩罚方法均选择网格内最弱惩罚，PCR／PLS 均选择全部成分；这些结果只说明当前候选集合中的比较，没有证明正则化或降维普遍无效，也没有确定网格以外的最优惩罚强度。若以后扩展网格，应作为新的探索性运行记录，不能反复参照这批测试误差调参再把它视为独立评价。

## 相关概念

- [[04 - 统计学习/概念/岭回归|岭回归]]；[[04 - 统计学习/概念/Lasso回归|Lasso回归]]。
- [[04 - 统计学习/概念/模型选择|模型选择]]；[[04 - 统计学习/概念/模型评价|模型评价]]。
- [[02 - 数理统计/概念/重采样|重采样]]；[[04 - 统计学习/概念/损失函数与经验风险|损失函数与经验风险]]。
- [[09 - 数据计算与可复现性/概念/可复现分析|可复现分析]]。

## 备注

- 原题已逐项对照 [[附件/books/ISLR.pdf#page=298|ISLR 印刷 287／PDF 物理 298]] 原图，保留 (a)–(g)，无原题星号。原书题号 9 在本库记为 6.9。
- 数据来源为实际读取的教材配套 `ISLR2::College`；[[工具/ISLR/运行结果/2026-10-25/6.9/package-versions.csv|运行包版本]]为 ISLR2 1.3.2、glmnet 4.1.8、pls 2.8.4，完整 R 环境记录见 [[工具/ISLR/运行结果/2026-10-25/6.9/session-info.txt|sessionInfo]]。实际输入保留为同目录 `source-data.rds`；没有以其他来源的同名数据替代。种子、划分与折号已保存，固定种子不保证不同平台逐位一致。
- 运行代码快照的 SHA256 为 `3c83ac9238f038b693932012c084feedd9fb6b2661e121127c658c91520f7e02`，见 [[工具/ISLR/运行结果/2026-10-25/verification.json|代码版本与输出摘要核验记录]]。`comparison.csv` 保留未四舍五入数值；各方法的 `*-coefficients.csv`、`*-test-predictions.csv` 与调参表均在本次运行目录中。表中数值由这些真实结果整理，未补造测试结论。
- `source_status: verified` 仅覆盖原题及定位；`solution_status: computationally-checked` 表示独立脚本已运行并获得上述有限结果，不表示官方答案、普遍性能保证或个人学习完成。
- 该数据题用于比较正则化与降维方法，原题没有要求构造 $p>n$ 的场景。学习状态保持 `not-started`。
