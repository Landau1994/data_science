# 全书动态索引交叉审阅

审阅日期：2026-11-03. 审阅范围：原书索引印刷257–258页／PDF物理266–267页；`work/full-index-plan.json`、`work/full-index-anchor-report.json`、`work/build_full_index.py`；全部100个目标锚点所处TeX语义位置. 不编辑正文TeX. 根据root后续授权，仅修订生成器DATA中的selector及中文显示，未执行`--apply`，避免与正文排版修改并发覆盖.

## 原词条集合与层级

已实际查看两页索引原图，并逐项对照原词、原页码和层级. 原书共有100个逻辑词条：87个顶层、13个子条目；其中4个“see”词条，96个有页码词条. 4个双页码词条各多一个位置，因此总计100个实际页码锚点，另4个see. 当前计划集合完整，没有漏词、多词或误合并.

13个子条目的父子关系均正确：Brenier定理→改进形式；Bures–Wasserstein→梯度；测地线→可延拓、广义形式；Langevin扩散→平均场、镜像、Newton、欠阻尼；半对偶→稳定性；变分推断→高斯、平均场；Wasserstein距离→切片、平滑. 四个多位置词条为PŁ不等式(132,233)、半离散传输(72,115)、切锥(199,202)、WFR(140,172)，额外目标分别为A.10、04-05半离散段、定义7.19、6.3.2生灭抽样，语义对应.

除索引两页外，针对确定错位和高风险符号另看了原图物理135、137、147、180、181、183、200：分别核实连续性PDE、度量导数定义、BW梯度定理、近端/镜像、Newton/欠阻尼、平均场Langevin与路径长度. 本轮没有宣称把所有正文源页重新逐页看过；其余定位依据实际TeX定义、标题、段落及之前章节源页核对记录.

## 确定问题与处理

1. 连续性方程原锚点(5.1)是粒子ODE，已在DATA改为实际PDE (5.2). 度量导数原锚点定义5.4是绝对连续测度类，已改为定义5.2. BW梯度原命题5.19是测地凸性；root已改为定理5.21. Wasserstein梯度原公式(5.9)是一阶变分；root已改为命题5.10.
2. 镜像Langevin和Newton–Langevin原先命中一般优化算法列表，已改为真正扩散的精确全名. 近端抽样器原先命中一般近端格式，已移到算法引入句. 平均场Langevin从McKean标题移到实际命名段. 长度从章引言移到长度定义(7.1).
3. IPM、MMD、二进划分由较宽节标题改为原索引所指页的定义2.19、定义2.20、定理2.2. Benamou–Brenier从定理可选标题内的文字命中改为定理5.7标签. logistic从算子附近改为公式后的正文命名处.
4. 中文名统一：本轮将chaining设为正文“链式法”，change of variables设为正文“变量代换”. root此前已将NTK、NPMLE、smoothed分别统一为“神经切线核”“非参数最大似然”“平滑”.
5. 旧快照的logistic锚曾落在`operatorname`参数内、NTK曾割开英文kernel；root已改locator和NTK selector. 本轮再次纯读取解析生成器并在去除现有index后的文本上定位，100行中96个主位置全部可找到，均不在任何未闭合花括号参数内. 未更动root已有的无换行插入及清理逻辑.

上述14项DATA修订已保存于生成器；两个梯度与三个中文修订为root在审阅过程中已落实的修订. 计划JSON及锚点report由root统一apply再生成，本轮未提前覆盖它们.

## 仍需root统一处理与成品复核

- 四个see的概念映射正确. 但旧report中的NPC目标被无条件拼成“非正曲率（NPC）（NPC）”，而正常display函数的可见名为“非正曲率（NPC）”. 建议see目标直接复用目标条目的可见显示名，避免重复及与实际索引名不一致. WFR目标同样应复用显示逻辑，而非另拼一套名字. 本轮依授权只改DATA，未改see生成逻辑，已即时通知root.
- 当前方案通过正文`index`、`makeindex`、`printindex`生成译稿页码；`source_printed`仅是对照来源，不作为索引输出页码. 生成器中未发现把原书页码写入index输出的代码. 最终页码、点击落点、see显示、两栏分页仍待root apply后成品PDF视觉/链接复核，不能用当前旧report代替最终验证.
- 原索引把Ajtai拼成Atjai；原图确为Atjai，当前original及可见原名保留这一源错误，正文定理拼写Ajtai. 此为原书索引疑误，不算新引入的译文错误，勿为表面一致而无说明修改来源词条.

## 逐项登记

下表覆盖原书全部100个逻辑词条. 页码均为原书印刷页，仅作来源登记. 目标列为修订后的DATA；“对应”表示原词、层级、中文语义与目标位置核对通过，并不代表成品PDF点击验收完成.

|序号|原词条（!为子层级）|原页|中文显示|目标|本轮结论|
|---:|---|---|---|---|---|
|1|Alexandrov curvature|193|Alexandrov曲率|`07-02 / label:sec:7.2.1`|对应|
|2|Alexandrov space|196|Alexandrov空间|`07-02 / Alexandrov空间`|对应|
|3|Atjai–Komlós–Tusnády theorem|47|Atjai–Komlós–Tusnády定理|`02-04 / label:sec:2.4`|对应|
|4|attention|180|注意力|`06-06 / 注意力`|对应|
|5|barycenter|212|重心|`08-01 / label:def:8.1`|对应|
|6|Benamou–Brenier formula|129|Benamou–Brenier公式|`05-03 / label:thm:5.7`|安全位置：由可选定理标题内的词命中改为定理5.7标签|
|7|Birkhoff polytope|6|Birkhoff多面体|`01-01 / Birkhoff`|对应|
|8|birth-death sampling|172|生灭抽样|`06-03 / label:sec:6.3.2`|对应|
|9|Brenier’s theorem|15|Brenier定理|`01-04 / label:thm:1.8`|对应|
|10|Brenier’s theorem!improved|27|Brenier定理!改进形式|`01-05 / label:thm:1.16`|对应|
|11|Burer–Monteiro|149|Burer–Monteiro|`05-10 / Burer`|对应|
|12|Bures–Wasserstein|133|Bures–Wasserstein|`05-05 / label:sec:5.5`|对应|
|13|Bures–Wasserstein!gradient|134|Bures–Wasserstein!梯度|`05-05 / label:thm:5.21`|审阅时已通知root修正：命题5.19改为BW梯度定理5.21|
|14|CAT(0)|see|CAT(0)|`see:NPC`|see概念对应；显示目标待统一|
|15|chaining|44|链式法|`02-03 / 链式法`|用正文定义术语“链式法”统一中文与定位|
|16|change of variables|153|变量代换|`06-01 / label:lem:6.2`|中文由“变量替换”统一为正文“变量代换”|
|17|continuity equation|122|连续性方程|`05-01 / label:eq:5.2`|确定语义错位：ODE (5.1)改为连续性PDE (5.2)|
|18|convex duality|230|凸对偶|`A-01 / label:def:A.4`|对应|
|19|cyclical monotonicity|17|循环单调性|`01-04 / label:def:1.9`|对应|
|20|dyadic partitioning|39|二进划分|`02-02 / label:thm:2.2`|原页39对应定理2.2，改为其标签以精确定位|
|21|earth mover’s distance|52|推土机距离|`02-05 / 推土机`|对应|
|22|empirical process|44|经验过程|`02-03 / 经验过程`|对应|
|23|empirical risk minimization (ERM)|215|经验风险最小化（ERM）|`08-02 / 经验风险`|对应|
|24|entropic optimal transport|95|熵正则最优传输|`04-01 / file-start`|对应|
|25|Fenchel–Young inequality|231|Fenchel–Young不等式|`A-01 / label:thm:A.6`|对应|
|26|first variation|130|一阶变分|`05-04 / label:def:5.9`|对应|
|27|Fisher–Rao|139|Fisher–Rao|`05-07 / label:eq:5.17`|对应|
|28|Fokker–Planck equation|164|Fokker–Planck方程|`06-02 / label:thm:6.11`|对应|
|29|fundamental theorem of optimal transport|25|最优传输基本定理|`01-05 / label:thm:1.14`|对应|
|30|geodesic|190|测地线|`07-01 / label:def:7.3`|对应|
|31|geodesic!extendable|218|测地线!可延拓|`08-02 / label:def:8.6`|对应|
|32|geodesic!generalized|209|测地线!广义形式|`07-04 / 广义`|对应|
|33|Geodesic convexity|127|测地凸性|`05-02 / 测地凸`|对应|
|34|geodesic space|188|测地空间|`07-01 / label:sec:7.1.1`|对应|
|35|Gibbs variational principle|98|Gibbs变分原理|`04-01 / Gibbs`|对应|
|36|gluing lemma|238|粘合引理|`B-01 / label:lem:B.5`|对应|
|37|goodness-of-fit testing|53|拟合优度检验|`02-05 / 拟合优度`|对应|
|38|Grönwall’s inequality|132|Grönwall不等式|`05-04 / Grönwall`|对应|
|39|Hadamard|see|Hadamard|`see:NPC`|see概念对应；显示目标待统一|
|40|Hellinger–Kantorovich|see|Hellinger–Kantorovich|`see:Wasserstein–Fisher–Rao (WFR)`|see概念对应；显示目标待统一|
|41|Hoeffding’s decomposition|106|Hoeffding分解|`04-03 / Hoeffding`|对应|
|42|hugging|215|贴合函数|`08-02 / label:def:8.2`|对应|
|43|integral probability metric (IPM)|64|积分概率度量（IPM）|`02-08 / label:def:2.19`|从节标题提前定位改为定义2.19|
|44|interaction energy|131|相互作用能|`05-04 / label:ex:5.13`|对应|
|45|internal energy|131|内能|`05-04 / label:ex:5.12`|对应|
|46|Kantorovich potentials|27|Kantorovich势|`01-05 / label:def:1.15`|对应|
|47|Kantorovich problem|3|Kantorovich问题|`01-01 / label:eq:KOT`|对应|
|48|Kantorovich–Rubinstein distance|see|Kantorovich–Rubinstein距离|`see:Wasserstein distance`|see概念对应；显示目标待统一|
|49|Langevin diffusion|161|Langevin扩散|`06-02 / Langevin扩散`|对应|
|50|Langevin diffusion!mean-field|171|Langevin扩散!平均场|`06-03 / 平均场或相互作用 Langevin 动力学`|从McKean标题改为实际命名平均场Langevin的段落|
|51|Langevin diffusion!mirror Langevin|168|Langevin扩散!镜像Langevin|`06-02 / 所谓镜像 Langevin 扩散`|从优化列表“镜像下降”改为实际扩散全名|
|52|Langevin diffusion!Newton–Langevin|169|Langevin扩散!Newton–Langevin|`06-02 / 得到作为 Newton 法抽样类比的 Newton--Langevin 扩散`|从优化列表“Newton法”改为实际扩散全名|
|53|Langevin diffusion!underdamped Langevin|169|Langevin扩散!欠阻尼Langevin|`06-02 / 欠阻尼`|对应|
|54|length|188|长度|`07-01 / label:eq:7.1`|从章引言“长度空间”改为长度定义(7.1)|
|55|logarithmic map|203|对数映射|`07-03 / label:def:7.20`|对应|
|56|logistic function|178|逻辑斯蒂函数|`06-05 / 广义线性模型使用的 logistic 函数`|由算子名内/相邻位置改为公式后正文命名处|
|57|maximum mean discrepancy (MMD)|65|最大均值差异（MMD）|`02-08 / label:def:2.20`|从节标题提前定位改为定义2.20|
|58|McKean–Vlasov|171|McKean–Vlasov|`06-03 / label:sec:6.3.1`|对应|
|59|mean-field neural networks|177|平均场神经网络|`06-05 / label:sec:6.5`|对应|
|60|metric derivative|124|度量导数|`05-01 / label:def:5.2`|确定语义错位：测度类定义5.4改为度量导数定义5.2|
|61|midpoint|190|中点|`07-01 / label:sec:7.1.2`|对应|
|62|Monge problem|2|Monge问题|`01-01 / Monge表述`|对应|
|63|neural network|177|神经网络|`06-05 / label:sec:6.5`|对应|
|64|neural tangent kernel (NTK)|184|神经切线核（NTK）|`06-07 / NTK`|root已统一为“神经切线核”并改为完整NTK匹配|
|65|NNC|196|非负曲率（NNC）|`07-02 / NNC`|对应|
|66|non-parametric maximum likelihood (NPMLE)|174|非参数最大似然（NPMLE）|`06-04 / label:sec:6.4`|root已统一为正文“非参数最大似然”|
|67|NPC|196|非正曲率（NPC）|`07-02 / NPC`|对应|
|68|path|188|路径|`07-01 / 路径`|对应|
|69|perceptron|180|感知机|`06-06 / 感知机`|对应|
|70|plug-in estimator|52|代入估计量|`02-05 / 代入`|对应|
|71|Poincaré inequality|88|Poincaré不等式|`03-06 / label:def:3.12`|对应|
|72|Polyak–Łojasiewicz (PŁ) inequality|132,233|Polyak–Łojasiewicz（PŁ）不等式|`05-04 / Polyak`|对应|
|73|portmanteau theorem|238|Portmanteau定理|`B-01 / label:thm:B.4`|对应|
|74|potential energy|131|势能|`05-04 / label:ex:5.11`|对应|
|75|Prokhorov’s theorem|237|Prokhorov定理|`B-01 / label:thm:B.3`|对应|
|76|proximal sampler|168|近端抽样器|`06-02 / 引入的近端抽样器`|从一般“近端格式”改为实际近端抽样器的引入句|
|77|rectifiable path|188|可求长路径|`07-01 / 可求长`|对应|
|78|Rockafellar’s theorem|17|Rockafellar定理|`01-04 / label:thm:1.10`|对应|
|79|semi-discrete optimal transport|72,115|半离散最优传输|`02-09 / 半离散`|对应|
|80|semidual|23|半对偶|`01-05 / label:sec:1.5.2`|对应|
|81|semidual!stability|79|半对偶!稳定性|`03-02 / label:sec:3.2`|对应|
|82|Sinkhorn divergence|115|Sinkhorn散度|`04-05 / Sinkhorn散度`|对应|
|83|Sinkhorn’s algorithm|102|Sinkhorn算法|`04-02 / Sinkhorn`|对应|
|84|Sobolev space|60|Sobolev空间|`02-07 / Sobolev`|对应|
|85|Stein variational gradient descent (SVGD)|159|Stein变分梯度下降（SVGD）|`06-01 / label:sec:6.1.4`|对应|
|86|subdifferential|230|次微分|`A-01 / label:def:A.2`|对应|
|87|tangent cone|199,202|切锥|`07-03 / label:sec:7.3`|对应|
|88|transformers|180|Transformer|`06-06 / label:sec:6.6`|对应|
|89|unbalanced optimal transport|138|非平衡最优传输|`05-07 / 非平衡`|对应|
|90|variance equality|215|方差等式|`08-02 / label:thm:8.3`|对应|
|91|variational inference (VI)|151|变分推断（VI）|`06-01 / label:sec:6.1`|对应|
|92|variational inference (VI)!Gaussian|154|变分推断（VI）!高斯|`06-01 / label:sec:6.1.2`|对应|
|93|variational inference (VI)!mean-field|156|变分推断（VI）!平均场|`06-01 / label:sec:6.1.3`|对应|
|94|Wasserstein distance|7|Wasserstein距离|`01-02 / label:def:1.2`|对应|
|95|Wasserstein distance!sliced|69|Wasserstein距离!切片|`02-08 / label:sec:2.8.4`|对应|
|96|Wasserstein distance!smoothed|68|Wasserstein距离!平滑|`02-08 / label:sec:2.8.3`|root已统一为正文“平滑”|
|97|Wasserstein–Fisher–Rao (WFR)|140,172|Wasserstein–Fisher–Rao（WFR）|`05-07 / label:eq:5.20`|对应|
|98|Wasserstein gradient|130|Wasserstein梯度|`05-04 / label:prop:5.10`|审阅时已通知root修正：一阶变分公式(5.9)改为命题5.10|
|99|Wasserstein gradient flow|131|Wasserstein梯度流|`05-04 / label:def:5.14`|对应|
|100|weak convergence|237|弱收敛|`B-01 / label:def:B.1`|对应|

## 四个额外位置

|词条|第二个原页|目标|结论|
|---|---:|---|---|
|Polyak–Łojasiewicz不等式|233|A-02 / def:A.10|对应欧氏空间PŁ定义|
|半离散最优传输|115|04-05 / 半离散|对应半离散熵传输讨论|
|切锥|202|07-03 / def:7.19|对应正式切锥定义；首位置保留7.3节引入|
|Wasserstein–Fisher–Rao|172|06-03 / sec:6.3.2|对应WFR生灭抽样应用|

纯读取验证结果：Python语法解析通过；DATA恰100行，96个页码主条目、4个see；96个主selector无缺失、无锚点处于未闭合花括号参数内. 本报告写入时未运行生成器、未编译、未改正文与主文件.
