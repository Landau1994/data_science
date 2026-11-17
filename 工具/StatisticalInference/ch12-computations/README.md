# DS011 第12章实际计算

`calc_ch12.py` 包含原PDF实核后的动物、Challenger、雀鹰、心率与23只袋鼠数据，以及实际执行的拟合和Bootstrap。原始教材仍以DS011统一台账登记，此目录不是新的学习台账。

运行：在本目录执行 `python -X utf8 calc_ch12.py`。本次环境为Python 3.10、NumPy 1.26.2、SciPy 1.11.4；准确版本、系数、信息矩阵、对数似然、迭代与随机参数见 `ch12-computations.json`。

- Probit与Logistic使用中心化预测变量和带回溯的Newton迭代；雀鹰二次与线性模型使用同一完整9组数据。
- LAD用HiGHS线性规划求解；非唯一解沿用求解器确定选择。Huber损失阈值为该样本OLS残差标准差的1.5倍，每次Bootstrap重拟合时重新计算阈值。
- Bootstrap固定23个原设计值。随机发生器为NumPy `default_rng` 的PCG64，种子20261113。每方法／实际误差族运行2000次，标准差分母为1999。运行顺序与完整实现一致。
- 正态与双指数误差使用相同目标方差；Double Exponential和Laplace同义，后一个名称复用双指数实际抽样结果。原残差与均值中心化残差两种重抽方式均实际执行，使用相同抽样索引作比较。
- `ch12-bootstrap-replicates.csv` 保存16,000行实际系数重复；不只保存最终标准误。`run-manifest.json` 保存本次实现、结果和CSV的SHA256。

这些是指定数据、模型、算法及有限重复次数的数值结果，不能替代一般证明或宣称Monte Carlo误差为零。未验证Obsidian界面渲染。
