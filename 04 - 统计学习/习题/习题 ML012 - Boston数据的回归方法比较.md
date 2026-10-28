---
title: "习题 ML012：Boston数据的回归方法比较"
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
source_exercise: "6.11"
source_refs: ["DS013 §6.6，Exercise 11(a)–(c)，印刷288/PDF299"]
source_status: verified
solution_status: computationally-checked
created: 2026-10-25
---

# 习题 ML012：Boston数据的回归方法比较

## 题目

### 英文原题

> [!question] 英文原题
> **11.** We will now try to predict per capita crime rate in the `Boston` data set.
>
> (a) Try out some of the regression methods explored in this chapter, such as best subset selection, the lasso, ridge regression, and PCR. Present and discuss results for the approaches that you consider.
>
> (b) Propose a model (or set of models) that seem to perform well on this data set, and justify your answer. Make sure that you are evaluating model performance using validation set error, cross-validation, or some other reasonable alternative, as opposed to using training error.
>
> (c) Does your chosen model involve all of the features in the data set? Why or why not?

### 中文转述

> [!question] 中文转述
> **ISLR 第 6 章第 11 题，全部 (a)–(c)。** 尝试预测 `Boston` 数据集中的人均犯罪率（per capita crime rate，`crim`）。
>
> (a) 尝试本章的一些回归方法，例如最优子集选择（best subset selection）、Lasso、岭回归（ridge regression）和主成分回归（PCR）；展示并讨论所采用方法的结果。
>
> (b) 提出在此数据上表现良好的一个模型或一组模型，并说明依据。用验证集误差、交叉验证（cross-validation）或其他合理替代方法评价性能，不用训练误差作评价依据。
>
> (c) 你选择的模型是否包含数据集中的全部特征？为什么？

## 提示

> [!hint]- 提示 1
> 目标变量是 `crim`，不要沿用其他 Boston 例子把房价变量 `medv` 当作响应。方法与调参都应使用训练资料内的验证规则。

> [!hint]- 提示 2
> Lasso 可以令某些原变量系数恰为零；岭回归通常只是收缩；PCR 即使只用少量成分，也可能组合了全部原始变量。

## 解答

> [!success]- 解答
> **解答范围：独立分析方案及一次实际 R 运行。** 已在 WSL 的 Ubuntu 20.04.6、R 4.3.1 中执行 [[工具/ISLR/islr_ch6_applied.R|应用题脚本]] 的 `6.11` 入口。输入、划分、折号、软件版本、拟合对象和全部结果保存在 [[工具/ISLR/运行结果/2026-10-25/6.11/comparison.csv|本次比较结果]] 所在目录；下述结论仅支持该数据版本和本次划分。
>
> **(a) 比较设计。** 取教材配套 `ISLR2::Boston`，以 `crim` 为响应，其他实际数据列为候选预测变量；保存输入快照与字段名，不混用其他包的同名版本。本次为 506 行、12 个候选预测变量，训练 354 行、测试 152 行。种子 20261025；训练集做固定五折交叉验证。
>
> 原题要求尝试“some”方法，所列方法是示例。本方案比较最小二乘基线、岭回归、Lasso 与 PCR，没有宣称运行最优子集选择。岭与 Lasso 在预设对数网格上选择最小交叉验证误差的 $\lambda$；PCR 在各训练折内重新学习标准化与方向，选择成分数 $M$，包含 $M=0$ 截距基线。全部方法使用相同折号；最后都在训练资料上拟合，再到相同测试行上评价。
>
> 统一损失是原始响应尺度的均方误差：
> $$
> \operatorname{MSE}=\frac1m\sum_{i=1}^{m}(\mathrm{crim}_i-\widehat{\mathrm{crim}}_i)^2.
> $$
> 若对响应取对数，就改变了目标量和误差尺度；不能把对数尺度误差混入本方案的方法比较表。
>
> **实际结果。** 下表按保存的完整数值四舍五入；非零斜率数不包括截距。
>
> | 方法 | 训练内选定参数 | 五折 MSE | 测试 MSE | 非零斜率数 |
> | --- | --- | --- | --- | --- |
> | 最小二乘 | 无 | 41.698490 | 48.578757 | 12 |
> | 岭回归 | $\lambda=0.0657933$ | 41.680318 | 48.433138 | 12 |
> | Lasso | $\lambda=0.00231013$ | 41.693874 | 48.542682 | 12 |
> | PCR | $M=12$ | 41.698490 | 48.578757 | 12 |
>
> **(b) 选择与结论。** 预先按各方法训练内交叉验证均方误差选取最小者，保留测试集仅作最后一次评价。脚本按这条规则选择了岭回归；其测试均方根误差约为 $6.959$。该次运行中岭回归的测试 MSE 也最低，但这不是用来反选方法的依据。
>
> 四种方法的差异很小，岭与最小二乘的测试 MSE 只差约 $0.146$。因此可以报告“按既定准则选岭回归”，不能据此断言岭回归在总体上显著更好。PCR 选满 12 个成分，其线性预测与这里的最小二乘相同。两个惩罚方法的最优 $\lambda$ 均在预设网格内部，PCR 的 $M$ 位于可行上端。
>
> 测试误差低只支持这次划分中的预测表现；没有自动给出因果解释、跨时期适用性或模型优劣的显著性结论。若之后根据测试结果调整候选方法，就应将该比较标作探索性，并重新设计独立评价。
>
> **(c) 是否使用全部特征。** 应读取选定模型的实际原尺度系数。Lasso 的非零斜率个数可能小于候选特征数，零系数表示该次拟合未直接使用相应线性项；并非证明该变量与响应无关。岭回归通常对全部候选项收缩，不自动做精确变量删除，特殊数据可能出现恰好为零的系数。PCR 的 $M$ 表示成分数而不是保留原始变量的数量：一个成分本身可含所有原变量。若 $M=0$，模型只有截距。
>
> 本次选中的岭模型确实使用了全部 12 个候选预测变量：`zn`、`indus`、`chas`、`nox`、`rm`、`age`、`dis`、`rad`、`tax`、`ptratio`、`lstat`、`medv`。这来自 [[工具/ISLR/运行结果/2026-10-25/6.11/ridge-coefficients.csv|实际系数表]]，符合岭惩罚主要做收缩的机制。该次 Lasso 也没有删除任何候选项，不能把“用 Lasso”直接等同于“已经选出更少变量”。
>
> 脚本为各方法输出原变量系数与测试预测，并以 $10^{-10}$ 的数值阈值汇报 `nonzero_slopes`；解释精确稀疏性仍应查看原始系数输出，不能把数值阈值当成数学上的零。

## 相关概念

- [[04 - 统计学习/概念/Lasso回归|Lasso回归]]；[[04 - 统计学习/概念/岭回归|岭回归]]。
- [[04 - 统计学习/概念/模型选择|模型选择]]；[[04 - 统计学习/概念/模型评价|模型评价]]。
- [[02 - 数理统计/概念/重采样|重采样]]；[[04 - 统计学习/概念/预测、推断与决策|预测、推断与决策]]。
- [[09 - 数据计算与可复现性/概念/可复现分析|可复现分析]]。

## 备注

- 原题逐项对照 [[附件/books/ISLR.pdf#page=299|ISLR 印刷 288／PDF 物理 299]] 原图，保留 (a)–(c)，无原题星号；原页题号 11 在本库记为 6.11。
- 本次实际使用 `ISLR2 1.3.2`、`glmnet 4.1.8`、`pls 2.8.4`；R 为 4.3.1，系统为 WSL Ubuntu 20.04.6。缺少的 ISLR2 从 CRAN 安装到本次任务临时目录，未修改 WSL 的系统或个人 R 库。数据快照为结果目录中的 `source-data.rds`，确切划分与折号见 `split.csv`、`folds.csv`。
- 运行方式为 WSL 中设置临时数据包的 `R_LIBS` 后调用 `Rscript .../islr_ch6_applied.R 6.11 .../6.11`；种子、目标、100 点网格和五折规则与正文一致。可复查的 [[工具/ISLR/运行结果/2026-10-25/analysis-script.R|运行时代码快照]] 与 [[工具/ISLR/运行结果/2026-10-25/verification.json|SHA-256 及输出摘要核对]] 标识代码版本；24 个结果文件的 MD5 核对通过。固定种子不保证跨平台逐位一致。
- 数据是地区层面的历史资料，不作个人层面解释；预测关联不推出因果关系。未扩展候选方法或重试种子，不将本次划分结果外推为总体优劣结论。
- `source_status: verified` 只覆盖原题；`solution_status: computationally-checked` 表示已完成上述有限范围的实际计算，不是统计结论的普遍证明。学习状态保持 `not-started`。
