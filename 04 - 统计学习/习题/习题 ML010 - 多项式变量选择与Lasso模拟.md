---
title: "习题 ML010：多项式变量选择与Lasso模拟"
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
source_exercise: "6.8"
source_refs: ["DS013 §6.6，Exercise 8(a)–(f)，印刷286/PDF297"]
source_status: verified
solution_status: computationally-checked
created: 2026-10-25
---

# 习题 ML010：多项式变量选择与Lasso模拟

## 题目

### 英文原题

> [!question] 英文原题
> **8.** In this exercise, we will generate simulated data, and will then use this data to perform best subset selection.
>
> (a) Use the `rnorm()` function to generate a predictor $X$ of length $n=100$, as well as a noise vector $\epsilon$ of length $n=100$.
>
> (b) Generate a response vector $Y$ of length $n=100$ according to the model
> $$
> Y=\beta_0+\beta_1X+\beta_2X^2+\beta_3X^3+\epsilon,
> $$
> where $\beta_0$, $\beta_1$, $\beta_2$, and $\beta_3$ are constants of your choice.
>
> (c) Use the `regsubsets()` function to perform best subset selection in order to choose the best model containing the predictors $X,X^2,\ldots,X^{10}$. What is the best model obtained according to $C_p$, BIC, and adjusted $R^2$? Show some plots to provide evidence for your answer, and report the coefficients of the best model obtained. Note you will need to use the `data.frame()` function to create a single data set containing both $X$ and $Y$.
>
> (d) Repeat (c), using forward stepwise selection and also using backwards stepwise selection. How does your answer compare to the results in (c)?
>
> (e) Now fit a lasso model to the simulated data, again using $X,X^2,\ldots,X^{10}$ as predictors. Use cross-validation to select the optimal value of $\lambda$. Create plots of the cross-validation error as a function of $\lambda$. Report the resulting coefficient estimates, and discuss the results obtained.
>
> (f) Now generate a response vector $Y$ according to the model
> $$
> Y=\beta_0+\beta_7X^7+\epsilon,
> $$
> and perform best subset selection and the lasso. Discuss the results obtained.

### 中文转述

> [!question] 中文转述
> **ISLR 第 6 章第 8 题，全部 (a)–(f)。** 生成模拟资料，比较最优子集选择（best subset selection）、逐步选择与 Lasso 回归。
>
> (a) 用 `rnorm()` 分别生成长度为 $n=100$ 的预测变量 $X$ 和噪声向量 $\epsilon$。
>
> (b) 自选常数 $\beta_0,\beta_1,\beta_2,\beta_3$，生成
> $$
> Y=\beta_0+\beta_1X+\beta_2X^2+\beta_3X^3+\epsilon.
> $$
>
> (c) 用 `data.frame()` 将 $X$ 与 $Y$ 组成同一数据集；以 $X,X^2,\ldots,X^{10}$ 为候选预测变量，用 `regsubsets()` 做最优子集选择。分别根据 $C_p$、贝叶斯信息准则（BIC）和调整后的 $R^2$ 选出最佳模型，画图说明，并报告最佳模型的系数。
>
> (d) 用前向逐步选择（forward stepwise selection）和后向逐步选择（backwards stepwise selection）重复 (c)，与最优子集结果比较。
>
> (e) 对相同的十个候选变量拟合 Lasso，用交叉验证（cross-validation）选择 $\lambda$，画交叉验证误差随 $\lambda$ 变化的图，报告系数并讨论结果。
>
> (f) 将响应改成 $Y=\beta_0+\beta_7X^7+\epsilon$，再做最优子集选择和 Lasso，讨论结果。

## 提示

> [!hint]- 提示 1
> 原始多项式列往往高度相关。某个模型预测较好，不表示它一定精确恢复真实非零幂次。将不同准则的模型与系数分别报告。

> [!hint]- 提示 2
> $C_p$ 与 BIC 取最小值，调整后的 $R^2$ 取最大值。Lasso 的尺度处理与 $\lambda$ 选择属于拟合过程；各方法比较应使用同一份生成资料。

## 解答

> [!success]- 解答
> **解答范围：独立分析方案与实际有限计算。** 已在 WSL 的 Ubuntu-20.04 环境执行 [[工具/ISLR/islr_ch6_applied.R|第6章应用题脚本]] 的 `6.8` 入口并成功生成结果。下面的数值来自本次输出 CSV，不是教材官方答案。完整 [[工具/ISLR/运行结果/2026-10-25/6.8/run-info.txt|运行说明]]、[[工具/ISLR/运行结果/2026-10-25/6.8/session-info.txt|R 环境记录]]、[[工具/ISLR/运行结果/2026-10-25/6.8/package-versions.csv|包版本]] 与 [[工具/ISLR/运行结果/2026-10-25/6.8/output-hashes.csv|输出 MD5 摘要]] 一并保留；下表为便于阅读而舍入，链接 CSV 保留原输出精度。
>
> **(a)–(b) 生成数据与参数。** 本次取 $n=100$，种子为 20261025；R 随机数约定为 `Mersenne-Twister / Inversion / Rejection`。依次独立生成 $X_i,\epsilon_i\sim N(0,1)$，取真实系数 $(\beta_0,\beta_1,\beta_2,\beta_3)=(1,2,-1,0.5)$，所以
> $$
> Y=1+2X-X^2+0.5X^3+\epsilon.
> $$
> 这是本方案自选的生成机制，教材没有指定这些常数。实际生成的 $X$、噪声、十列候选原始幂及两组真实系数保存在 [[工具/ISLR/运行结果/2026-10-25/6.8/data-and-parameters.rds|输入与参数快照]]；实际五折划分保存在 [[工具/ISLR/运行结果/2026-10-25/6.8/folds.csv|折号表]]。候选矩阵第 $j$ 列为原始幂 $X^j$，不是正交多项式。
>
> **(c) 最优子集选择。** 对每个大小 $k=1,\ldots,10$，以 `regsubsets(method="exhaustive")` 搜索最小训练残差平方和子集，再分别最小化 $C_p$、最小化 BIC、最大化调整后的 $R^2$；并列时选较小模型。候选集允许遗漏中间幂次，不强制多项式层级。真实信号是三次多项式，但本次三个准则分别选出 6、3、8 个斜率，具体如下。
>
> | 搜索方法 | 选择准则 | 斜率数 | 入选幂次 $j$（列为 $X^j$） | 对应准则值 | 全部系数 |
> | --- | --- | ---: | --- | ---: | --- |
> | 最优子集 | $C_p$ | 6 | 1, 3, 5, 6, 8, 9 | 6.23716856 | [[工具/ISLR/运行结果/2026-10-25/6.8/cubic-exhaustive-Cp-coefficients.csv\|CSV]] |
> | 最优子集 | BIC | 3 | 1, 2, 3 | -222.87432 | [[工具/ISLR/运行结果/2026-10-25/6.8/cubic-exhaustive-BIC-coefficients.csv\|CSV]] |
> | 最优子集 | 调整 $R^2$ | 8 | 1, 2, 3, 4, 6, 7, 8, 9 | 0.912237277 | [[工具/ISLR/运行结果/2026-10-25/6.8/cubic-exhaustive-adjusted_R2-coefficients.csv\|CSV]] |
> | 前向逐步 | $C_p$ | 3 | 1, 2, 3 | 6.80691658 | [[工具/ISLR/运行结果/2026-10-25/6.8/cubic-forward-Cp-coefficients.csv\|CSV]] |
> | 前向逐步 | BIC | 3 | 1, 2, 3 | -222.87432 | [[工具/ISLR/运行结果/2026-10-25/6.8/cubic-forward-BIC-coefficients.csv\|CSV]] |
> | 前向逐步 | 调整 $R^2$ | 10 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 | 0.910274275 | [[工具/ISLR/运行结果/2026-10-25/6.8/cubic-forward-adjusted_R2-coefficients.csv\|CSV]] |
> | 后向逐步 | $C_p$ | 6 | 1, 3, 6, 7, 8, 9 | 6.54140004 | [[工具/ISLR/运行结果/2026-10-25/6.8/cubic-backward-Cp-coefficients.csv\|CSV]] |
> | 后向逐步 | BIC | 6 | 1, 3, 6, 7, 8, 9 | -215.609959 | [[工具/ISLR/运行结果/2026-10-25/6.8/cubic-backward-BIC-coefficients.csv\|CSV]] |
> | 后向逐步 | 调整 $R^2$ | 8 | 1, 2, 3, 4, 6, 7, 8, 9 | 0.912237277 | [[工具/ISLR/运行结果/2026-10-25/6.8/cubic-backward-adjusted_R2-coefficients.csv\|CSV]] |
>
> 表中也列出 (d) 的两条逐步路径以便直接比较。最优子集的完整 [[工具/ISLR/运行结果/2026-10-25/6.8/cubic-exhaustive-scores.csv|各大小准则值]] 与下图相符。BIC 选出的模型恰好使用真实的三种幂次，但系数有有限样本误差：
> $$
> \hat Y_{\mathrm{BIC}}\approx1.423303538+2.242461124X-1.360808221X^2+0.274809722X^3.
> $$
> $C_p$ 选出的六项模型没有 $X^2$，而使用若干高次幂替代；调整 $R^2$ 偏向更大的八项模型。不能把“准则最优”等同于精确恢复真实支持集。各行链接包含截距和全部入选斜率，不只列模型大小。
>
> ![[附件/习题图/ISLR-6.8-cubic-exhaustive-criteria.png]]
>
> **(d) 前向与后向逐步选择。** 同一数据分别用 `method="forward"`、`method="backward"`。前向路径按 $C_p$、BIC、调整 $R^2$ 选出 3、3、10 项；后向路径选出 6、6、8 项。前向的 $C_p$ 与 BIC 模型均与穷举 BIC 模型一致；后向调整 $R^2$ 模型与穷举对应模型一致。后向六项模型的幂次为 $1,3,6,7,8,9$，与穷举 $C_p$ 的 $1,3,5,6,8,9$ 不同，且其 $C_p$ 为 6.54140004，高于穷举的 6.23716856。逐步搜索只走部分路径，因此最终模型不保证等同于穷举最优解。完整 [[工具/ISLR/运行结果/2026-10-25/6.8/cubic-forward-scores.csv|前向分数]]、[[工具/ISLR/运行结果/2026-10-25/6.8/cubic-backward-scores.csv|后向分数]]，以及 [[工具/ISLR/运行结果/2026-10-25/6.8/cubic-forward-criteria.png|前向准则图]]、[[工具/ISLR/运行结果/2026-10-25/6.8/cubic-backward-criteria.png|后向准则图]] 可逐项复查。
>
> **(e) 三次信号的 Lasso。** 使用相同十列候选变量和固定五折划分，`cv.glmnet(alpha=1, standardize=TRUE)` 在从 $10^5$ 到 $10^{-4}$ 的 100 点对数网格上选择参数；各训练折内部估计标准化，截距不惩罚。本次真实结果是
> $$
> \lambda_{\min}=0.0351119173422,\qquad
> \lambda_{1\mathrm{se}}=0.351119173422.
> $$
> 选定网格点的交叉验证均方误差为 1.16262431296，所报告标准误为 0.191180443533；`lambda.min` 下有 4 个非零斜率，分别为 $X,X^2,X^3,X^4$。对应原尺度预测模型为
> $$
> \hat Y_L\approx1.340763046+2.310829273X-1.107606703X^2
> +0.182597280X^3-0.097901024X^4.
> $$
> 因此本次 Lasso 找到了三个真实幂次，也保留了额外的四次项；收缩系数没有精确等于生成系数。完整 [[工具/ISLR/运行结果/2026-10-25/6.8/cubic-lasso-selected.csv|参数与非零数]]、[[工具/ISLR/运行结果/2026-10-25/6.8/cubic-lasso-coefficients.csv|原尺度系数]]、[[工具/ISLR/运行结果/2026-10-25/6.8/cubic-lasso-cv.csv|100点交叉验证结果]] 已保存。图中竖虚线对应 `lambda.min` 和 `lambda.1se`，顶端数字表示非零斜率数量。
>
> ![[附件/习题图/ISLR-6.8-cubic-lasso-cv.png]]
>
> **(f) 七次信号。** 保留同一 $X$、噪声与折号，改用真实模型 $Y=1+X^7+\epsilon$；这样比较明确只改变响应信号。对最优子集和 Lasso 重复分析，另保留两条逐步路径作为补充对照。三种搜索与三种准则的实际结果如下。
>
> | 搜索方法 | 选择准则 | 斜率数 | 入选幂次 $j$（列为 $X^j$） | 对应准则值 | 全部系数 |
> | --- | --- | ---: | --- | ---: | --- |
> | 最优子集 | $C_p$ | 5 | 4, 5, 6, 8, 9 | 3.46161423 | [[工具/ISLR/运行结果/2026-10-25/6.8/seventh-exhaustive-Cp-coefficients.csv\|CSV]] |
> | 最优子集 | BIC | 2 | 6, 7 | -626.989314 | [[工具/ISLR/运行结果/2026-10-25/6.8/seventh-exhaustive-BIC-coefficients.csv\|CSV]] |
> | 最优子集 | 调整 $R^2$ | 7 | 1, 2, 3, 4, 6, 8, 9 | 0.998376017 | [[工具/ISLR/运行结果/2026-10-25/6.8/seventh-exhaustive-adjusted_R2-coefficients.csv\|CSV]] |
> | 前向逐步 | $C_p$ | 2 | 6, 7 | 3.63484846 | [[工具/ISLR/运行结果/2026-10-25/6.8/seventh-forward-Cp-coefficients.csv\|CSV]] |
> | 前向逐步 | BIC | 2 | 6, 7 | -626.989314 | [[工具/ISLR/运行结果/2026-10-25/6.8/seventh-forward-BIC-coefficients.csv\|CSV]] |
> | 前向逐步 | 调整 $R^2$ | 9 | 1, 2, 3, 4, 6, 7, 8, 9, 10 | 0.998347129 | [[工具/ISLR/运行结果/2026-10-25/6.8/seventh-forward-adjusted_R2-coefficients.csv\|CSV]] |
> | 后向逐步 | $C_p$ | 6 | 1, 3, 4, 6, 8, 9 | 4.94550695 | [[工具/ISLR/运行结果/2026-10-25/6.8/seventh-backward-Cp-coefficients.csv\|CSV]] |
> | 后向逐步 | BIC | 5 | 3, 4, 6, 8, 9 | -617.655043 | [[工具/ISLR/运行结果/2026-10-25/6.8/seventh-backward-BIC-coefficients.csv\|CSV]] |
> | 后向逐步 | 调整 $R^2$ | 7 | 1, 2, 3, 4, 6, 8, 9 | 0.998376017 | [[工具/ISLR/运行结果/2026-10-25/6.8/seventh-backward-adjusted_R2-coefficients.csv\|CSV]] |
>
> 穷举 BIC 选中 $X^6,X^7$，模型为
> $$
> \hat Y_{\mathrm{BIC}}\approx1.316914042-0.0803015434X^6+0.960543107X^7.
> $$
> 它保留了真实的七次项，也引入额外六次项。穷举 $C_p$ 的五项模型和调整 $R^2$ 的七项模型反而均未包含 $X^7$，而以其他相关高次幂组合拟合。这是本次实际搜索结果；不能因为已知真实模型就改写为“必然选中七次项”。完整 [[工具/ISLR/运行结果/2026-10-25/6.8/seventh-exhaustive-scores.csv|穷举分数]]、[[工具/ISLR/运行结果/2026-10-25/6.8/seventh-forward-scores.csv|前向分数]]、[[工具/ISLR/运行结果/2026-10-25/6.8/seventh-backward-scores.csv|后向分数]]，以及 [[工具/ISLR/运行结果/2026-10-25/6.8/seventh-forward-criteria.png|前向准则图]]、[[工具/ISLR/运行结果/2026-10-25/6.8/seventh-backward-criteria.png|后向准则图]] 均可查阅。
>
> ![[附件/习题图/ISLR-6.8-seventh-exhaustive-criteria.png]]
>
> 七次信号的 Lasso 选定
> $$
> \lambda_{\min}=0.0432876128108,\qquad
> \lambda_{1\mathrm{se}}=0.351119173422,
> $$
> 交叉验证均方误差为 1.19341608959，所报告标准误为 0.213730246336，共有 8 个非零斜率。$X^7$ 系数为 0.953023544，$X^2,X^5$ 系数恰为零；其余非零项中，$X^9$ 系数虽仅约 $6.94427\times10^{-6}$，仍不能按数学上的精确零删除。两种信号下全部 Lasso 原尺度系数为：
>
> | 项 | 三次信号 Lasso | 七次信号 Lasso |
> | --- | ---: | ---: |
> | 截距 | 1.34076305 | 1.30423673 |
> | $X^{1}$ | 2.31082927 | 0.0506591197 |
> | $X^{2}$ | -1.1076067 | 0 |
> | $X^{3}$ | 0.18259728 | 0.0220396077 |
> | $X^{4}$ | -0.0979010241 | -0.0258428533 |
> | $X^{5}$ | 0 | 0 |
> | $X^{6}$ | 0 | -0.051956654 |
> | $X^{7}$ | 0 | 0.953023544 |
> | $X^{8}$ | 0 | -0.00521307295 |
> | $X^{9}$ | 0 | 6.9442685e-06 |
> | $X^{10}$ | 0 | -0.000536495424 |
>
> 七次信号的完整 [[工具/ISLR/运行结果/2026-10-25/6.8/seventh-lasso-selected.csv|参数与非零数]]、[[工具/ISLR/运行结果/2026-10-25/6.8/seventh-lasso-coefficients.csv|全部系数]]、[[工具/ISLR/运行结果/2026-10-25/6.8/seventh-lasso-cv.csv|100点交叉验证结果]] 与下图均来自本次运行。大惩罚下的误差较高，使总览图中最低点附近的差异较难分辨，应配合 CSV 读取数值。
>
> ![[附件/习题图/ISLR-6.8-seventh-lasso-cv.png]]
>
> **有限核验与数值边界。** 两个 `lambda.min` 都位于预设网格内部，均未选到上下边界；本次没有因此扩展网格或重新选择随机种子。高次原始幂可能造成列相关和数值病态，较大的子集及若干相互抵消的系数不等于真实多项式结构被恢复。本次没有测定设计矩阵条件数，也没有做多种种子或交叉平台稳定性检查。这里 $n=100$、候选列数为 10，是稀疏变量选择的入门模拟，并非 $p>n$ 实验；一组种子、一次五折划分和100个参数点只能支持上述有限结果。最小交叉验证误差用于调参，不能冒充独立测试误差；本次未另设测试数据，不能据此断言三次或七次信号的总体预测表现更好。

## 相关概念

- [[04 - 统计学习/概念/Lasso回归|Lasso回归]]：稀疏惩罚、尺度与相关列。
- [[04 - 统计学习/概念/正则化|正则化]]；[[04 - 统计学习/概念/模型选择|模型选择]]。
- [[02 - 数理统计/概念/重采样|重采样]]：交叉验证和固定折划分。
- [[04 - 统计学习/概念/泛化、欠拟合与过拟合|泛化、欠拟合与过拟合]]。
- [[09 - 数据计算与可复现性/概念/可复现分析|可复现分析]]：环境、数据、参数与输出记录。

## 备注

- 原题逐项对照 [[附件/books/ISLR.pdf#page=297|ISLR 印刷 286／PDF 物理 297]] 原图，包含 (a)–(f)，无原题星号。题号在本库记作 6.8，原页显示为 8。
- `source_status: verified` 只表示本题文字、公式与定位已核对；`solution_status: computationally-checked` 表示配套方案已按上述输入实际执行，数值来自保留的 CSV，不表示一般数学结论或官方答案。
- 实际执行环境：WSL 的 Ubuntu 20.04.6 LTS，R 4.3.1（x86_64-pc-linux-gnu），`leaps` 3.2、`glmnet` 4.1.8；详细环境含 BLAS/LAPACK 见运行目录。以 `Rscript "工具/ISLR/islr_ch6_applied.R" 6.8 "工具/ISLR/运行结果/2026-10-25/6.8"` 为本库根目录下的运行入口，具体输入、折号及结果均已保存；重跑时应另换空输出目录，保留本次结果。固定种子不保证跨平台逐位一致。
- 四张嵌入图逐字节复制自本次运行目录的原始 PNG，并已查看图像；没有重绘或修改图中结果。完成计算与归档不代表用户完成学习，个人状态保持 `not-started`。
- 实际执行的 [[工具/ISLR/运行结果/2026-10-25/analysis-script.R|代码快照]] 及 [[工具/ISLR/运行结果/2026-10-25/verification.json|SHA-256 与输出摘要核对]] 标识本次代码版本；51 个原始输出文件的 MD5 核对通过。
