# 前置与第1章引用内部化

核对日期：2026-11-04。范围：`frontmatter/*.tex` 与 `sections-tex/01-*.tex`。共把153处 `\orig{原PDF物理页}{可见文字}` 转为 `\hyperref[真实标签]{原可见文字}`，其中原书目录109处、前置其他正文31处、第1章13处。原可见文字逐字保留，不改任何数学表达、证明或数值。

## 核对依据与边界

- 原目录物理22–24三页重新渲染并实际逐页查看；109行保持原层级、编号、标题与右栏原印刷页码。102个编号条目的原物理页分别用页面标题/章节号核实，再匹配已译节标签，并非按物理页偏移猜目标。
- 前置4项对应前言、最优运输导论、致谢、记号；后置3项对应习题、参考文献、索引。原书目录没有独立提示行，未新增目录内容。
- 原目录说明由“尚未译完的部分仍指向原书”更新为“标题链接到本译稿的对应内容”，右栏仍明确为原书页码。
- 前置与第1章其他44处按其可见编号、章名或上下文逐处核实。习题1、2核对原物理348页；习题58、59核对原物理356页及已译题号；定义3.13核对原物理122页的可数Lipschitz定义；(3.1)核对原物理114页及eq:3.1。
- 第1章§1.2原文误引(3.1)，仍显示(3.1)，并链接真实eq:3.1；没有改成其他公式。§1.7“下一章”对应第2章，仍显示原词。
- 没有新增正文锚点，没有改主文件或索引映射。sec:2–8在当前整合稿work/progress-preview.tex中存在，待root写入最终主稿。sec:references由root补入，sec:index已通知索引agent保留。

## 实际静态检查

全部153处替换后逐项检查新链接仍含完全相同的可见文字；范围内剩余orig为0。所有相关文件的环境栈、花括号与数学美元定界符闭合。图/公式/证明正文未改变。没有编译主稿或声称已在PDF阅读器中逐个点击。

当前目标集合中尚待整合定义的标签：`sec:index`, `sec:references`。这些是明确协调的最终章节锚点，不是无法定位的原文引用。

## 改动清单

下表文件位置是改动前位置；原物理页是旧orig中的真实目标页。可见文字中的所有编号与原文错引均保留。

| 文件及行 | 原物理页 | 原可见文字 | 新目标 |
| --- | ---: | --- | --- |
| `frontmatter/00-acknowledgments.tex:9` | 187 | `第4.4.2节` | `sec:4.4.2` |
| `frontmatter/00-introduction.tex:30` | 348 | `习题(1)` | `ex:1` |
| `frontmatter/00-introduction.tex:32` | 113 | `第3章` | `sec:3` |
| `frontmatter/00-introduction.tex:46` | 146 | `第4章` | `sec:4` |
| `frontmatter/00-introduction.tex:51` | 110 | `第2.5.3节` | `sec:2.5.3` |
| `frontmatter/00-introduction.tex:51` | 303 | `第7.4.2节` | `sec:7.4.2` |
| `frontmatter/00-introduction.tex:53` | 201 | `第5章` | `sec:5` |
| `frontmatter/00-introduction.tex:53` | 309 | `第8章` | `sec:8` |
| `frontmatter/00-introduction.tex:53` | 222 | `第5.3.5节` | `sec:5.3.5` |
| `frontmatter/00-introduction.tex:53` | 337 | `第8.4.4节` | `sec:8.4.4` |
| `frontmatter/00-introduction.tex:57` | 146 | `第4章` | `sec:4` |
| `frontmatter/00-introduction.tex:57` | 176 | `第4.4节` | `sec:4.4` |
| `frontmatter/00-introduction.tex:59` | 106 | `第2.5.1节` | `sec:2.5.1` |
| `frontmatter/00-introduction.tex:59` | 239 | `第5.5.5节` | `sec:5.5.5` |
| `frontmatter/00-introduction.tex:59` | 243 | `第6章` | `sec:6` |
| `frontmatter/00-preface.tex:10` | 146 | `第4章` | `sec:4` |
| `frontmatter/00-preface.tex:25` | 201 | `第5章` | `sec:5` |
| `frontmatter/00-preface.tex:29` | 243 | `第6章` | `sec:6` |
| `frontmatter/00-preface.tex:40` | 243 | `第6章` | `sec:6` |
| `frontmatter/00-preface.tex:45` | 201 | `第5章` | `sec:5` |
| `frontmatter/00-preface.tex:45` | 201 | `第5章` | `sec:5` |
| `frontmatter/00-preface.tex:45` | 273 | `第7章` | `sec:7` |
| `frontmatter/00-preface.tex:45` | 309 | `第8章` | `sec:8` |
| `frontmatter/00-preface.tex:45` | 243 | `第6章` | `sec:6` |
| `frontmatter/00-preface.tex:49` | 86 | `第2章` | `sec:2` |
| `frontmatter/00-preface.tex:51` | 113 | `第3章` | `sec:3` |
| `frontmatter/00-preface.tex:53` | 146 | `第4章` | `sec:4` |
| `frontmatter/00-preface.tex:55` | 201 | `第5章` | `sec:5` |
| `frontmatter/00-preface.tex:57` | 243 | `第6章` | `sec:6` |
| `frontmatter/00-preface.tex:59` | 273 | `第7章` | `sec:7` |
| `frontmatter/00-preface.tex:61` | 309 | `第8章` | `sec:8` |
| `frontmatter/00-source-contents.tex:14` | 8 | `\textbf{前言}` | `sec:preface` |
| `frontmatter/00-source-contents.tex:15` | 15 | `\hspace{1em}最优运输导论` | `sec:introduction` |
| `frontmatter/00-source-contents.tex:16` | 20 | `\textbf{致谢}` | `sec:acknowledgments` |
| `frontmatter/00-source-contents.tex:17` | 26 | `\textbf{记号}` | `sec:notation` |
| `frontmatter/00-source-contents.tex:18` | 29 | `\textbf{原问题与对偶问题}` | `sec:1` |
| `frontmatter/00-source-contents.tex:19` | 29 | `Kantorovich 问题与 Monge 问题` | `sec:1.1` |
| `frontmatter/00-source-contents.tex:20` | 37 | `对偶性` | `sec:1.2` |
| `frontmatter/00-source-contents.tex:21` | 41 | `$h$ 严格凸时 $c(x,y)=h(x-y)$ 的情形及最优 $\mathrm T$ 的存在性` | `sec:1.3` |
| `frontmatter/00-source-contents.tex:22` | 44 | `\hspace{1em}$\mathbb R^d$ 中的二次情形` | `sec:1.3.1` |
| `frontmatter/00-source-contents.tex:23` | 46 | `\hspace{1em}平坦环面上的二次情形` | `sec:1.3.2` |
| `frontmatter/00-source-contents.tex:24` | 48 | `存在性的反例` | `sec:1.4` |
| `frontmatter/00-source-contents.tex:25` | 49 | `Kantorovich 问题作为 Monge 问题的松弛` | `sec:1.5` |
| `frontmatter/00-source-contents.tex:26` | 53 | `$c$-凹性、对偶性与最优性` | `sec:1.6` |
| `frontmatter/00-source-contents.tex:27` | 53 | `\hspace{1em}凸函数与 $c$-凹函数` | `sec:1.6.1` |
| `frontmatter/00-source-contents.tex:28` | 56 | `\hspace{1em}$c$-循环单调性与对偶性` | `sec:1.6.2` |
| `frontmatter/00-source-contents.tex:29` | 63 | `\hspace{1em}对偶性的一个直接证明` | `sec:1.6.3` |
| `frontmatter/00-source-contents.tex:30` | 65 | `\hspace{1em}最优性的充分条件与稳定性` | `sec:1.6.4` |
| `frontmatter/00-source-contents.tex:31` | 69 | `讨论` | `sec:1.7` |
| `frontmatter/00-source-contents.tex:32` | 69 | `\hspace{1em}概率解释` | `sec:1.7.1` |
| `frontmatter/00-source-contents.tex:33` | 70 | `\hspace{1em}极分解` | `sec:1.7.2` |
| `frontmatter/00-source-contents.tex:34` | 72 | `\hspace{1em}匹配问题与经济学解释` | `sec:1.7.3` |
| `frontmatter/00-source-contents.tex:35` | 76 | `\hspace{1em}多边缘运输问题` | `sec:1.7.4` |
| `frontmatter/00-source-contents.tex:36` | 79 | `\hspace{1em}鞅最优运输与金融应用` | `sec:1.7.5` |
| `frontmatter/00-source-contents.tex:37` | 82 | `\hspace{1em}Monge--Amp\`ere 方程与正则性` | `sec:1.7.6` |
| `frontmatter/00-source-contents.tex:38` | 86 | `\textbf{一维问题}` | `sec:2` |
| `frontmatter/00-source-contents.tex:39` | 86 | `一维中的单调运输映射与方案` | `sec:2.1` |
| `frontmatter/00-source-contents.tex:40` | 90 | `单调映射的最优性` | `sec:2.2` |
| `frontmatter/00-source-contents.tex:41` | 94 | `Knothe 运输` | `sec:2.3` |
| `frontmatter/00-source-contents.tex:42` | 99 | `作为 Brenier 映射极限的 Knothe 映射` | `sec:2.4` |
| `frontmatter/00-source-contents.tex:43` | 106 | `讨论` | `sec:2.5` |
| `frontmatter/00-source-contents.tex:44` | 106 | `\hspace{1em}直方图均衡化` | `sec:2.5.1` |
| `frontmatter/00-source-contents.tex:45` | 108 | `\hspace{1em}由一维构造得到的单调映射` | `sec:2.5.2` |
| `frontmatter/00-source-contents.tex:46` | 110 | `\hspace{1em}通过 Knothe 或 Brenier 映射证明等周不等式` | `sec:2.5.3` |
| `frontmatter/00-source-contents.tex:47` | 113 | `\textbf{$L^1$ 与 $L^\infty$ 理论}` | `sec:3` |
| `frontmatter/00-source-contents.tex:48` | 113 | `成本为 $\|x-y\|$ 的 Monge 情形` | `sec:3.1` |
| `frontmatter/00-source-contents.tex:49` | 114 | `\hspace{1em}距离成本的对偶性` | `sec:3.1.1` |
| `frontmatter/00-source-contents.tex:50` | 115 | `\hspace{1em}次级变分问题` | `sec:3.1.2` |
| `frontmatter/00-source-contents.tex:51` | 117 | `\hspace{1em}运输射线的几何性质` | `sec:3.1.3` |
| `frontmatter/00-source-contents.tex:52` | 125 | `\hspace{1em}最优运输映射的存在与不存在` | `sec:3.1.4` |
| `frontmatter/00-source-contents.tex:53` | 127 | `\hspace{1em}单调运输的逼近` | `sec:3.1.5` |
| `frontmatter/00-source-contents.tex:54` | 130 | `上确界情形：$L^\infty$` | `sec:3.2` |
| `frontmatter/00-source-contents.tex:55` | 135 | `讨论` | `sec:3.3` |
| `frontmatter/00-source-contents.tex:56` | 135 | `\hspace{1em}不同范数与更一般的凸成本` | `sec:3.3.1` |
| `frontmatter/00-source-contents.tex:57` | 139 | `\hspace{1em}凹成本（$L^p$，$0<p<1$）` | `sec:3.3.2` |
| `frontmatter/00-source-contents.tex:58` | 146 | `\textbf{最小流}` | `sec:4` |
| `frontmatter/00-source-contents.tex:59` | 146 | `Euler 观点与 Lagrange 观点` | `sec:4.1` |
| `frontmatter/00-source-contents.tex:60` | 146 | `\hspace{1em}静态与动态模型` | `sec:4.1.1` |
| `frontmatter/00-source-contents.tex:61` | 148 | `\hspace{1em}连续性方程` | `sec:4.1.2` |
| `frontmatter/00-source-contents.tex:62` | 152 | `Beckmann 问题` | `sec:4.2` |
| `frontmatter/00-source-contents.tex:63` | 152 | `\hspace{1em}引言、形式等价与变体` | `sec:4.2.1` |
| `frontmatter/00-source-contents.tex:64` | 154 | `\hspace{1em}构造 Beckmann 问题的极小解` | `sec:4.2.2` |
| `frontmatter/00-source-contents.tex:65` | 159 | `\hspace{1em}曲线上的测度的交通强度与交通流` | `sec:4.2.3` |
| `frontmatter/00-source-contents.tex:66` | 165 | `\hspace{1em}一维中的 Beckman 问题` | `sec:4.2.4` |
| `frontmatter/00-source-contents.tex:67` | 167 | `\hspace{1em}最优 $\mathbf w$ 的刻画与唯一性` | `sec:4.2.5` |
| `frontmatter/00-source-contents.tex:68` | 169 | `运输密度的可积性` | `sec:4.3` |
| `frontmatter/00-source-contents.tex:69` | 176 | `讨论` | `sec:4.4` |
| `frontmatter/00-source-contents.tex:70` | 176 | `\hspace{1em}拥挤运输` | `sec:4.4.1` |
| `frontmatter/00-source-contents.tex:71` | 187 | `\hspace{1em}分支运输` | `sec:4.4.2` |
| `frontmatter/00-source-contents.tex:72` | 201 | `\textbf{Wasserstein 空间}` | `sec:5` |
| `frontmatter/00-source-contents.tex:73` | 203 | `定义与三角不等式` | `sec:5.1` |
| `frontmatter/00-source-contents.tex:74` | 207 | `$W_p$ 诱导的拓扑` | `sec:5.2` |
| `frontmatter/00-source-contents.tex:75` | 211 | `$\mathbb W_p$ 中的曲线与连续性方程` | `sec:5.3` |
| `frontmatter/00-source-contents.tex:76` | 213 | `\hspace{1em}Benamou--Brenier 泛函 $\mathscr B_p$` | `sec:5.3.1` |
| `frontmatter/00-source-contents.tex:77` | 216 | `\hspace{1em}绝对连续曲线具有速度场` | `sec:5.3.2` |
| `frontmatter/00-source-contents.tex:78` | 218 | `\hspace{1em}连续性方程的正则化` | `sec:5.3.3` |
| `frontmatter/00-source-contents.tex:79` | 221 | `\hspace{1em}速度场给出 Lipschitz 性质` | `sec:5.3.4` |
| `frontmatter/00-source-contents.tex:80` | 222 | `\hspace{1em}$W_p^p$ 沿测度曲线的导数` | `sec:5.3.5` |
| `frontmatter/00-source-contents.tex:81` | 226 | `$\mathbb W_p$ 中的恒速测地线` | `sec:5.4` |
| `frontmatter/00-source-contents.tex:82` | 231 | `讨论` | `sec:5.5` |
| `frontmatter/00-source-contents.tex:83` | 231 | `\hspace{1em}$W_\infty$ 距离` | `sec:5.5.1` |
| `frontmatter/00-source-contents.tex:84` | 233 | `\hspace{1em}Wasserstein 距离与负阶 Sobolev 距离` | `sec:5.5.2` |
| `frontmatter/00-source-contents.tex:85` | 235 | `\hspace{1em}Wasserstein 距离与分支运输距离` | `sec:5.5.3` |
| `frontmatter/00-source-contents.tex:86` | 238 | `\hspace{1em}切片 Wasserstein 距离` | `sec:5.5.4` |
| `frontmatter/00-source-contents.tex:87` | 239 | `\hspace{1em}$\mathbb W_2$ 中的重心` | `sec:5.5.5` |
| `frontmatter/00-source-contents.tex:88` | 243 | `\textbf{数值方法}` | `sec:6` |
| `frontmatter/00-source-contents.tex:89` | 244 | `Benamou--Brenier` | `sec:6.1` |
| `frontmatter/00-source-contents.tex:90` | 249 | `Angenent--Hacker--Tannenbaum` | `sec:6.2` |
| `frontmatter/00-source-contents.tex:91` | 256 | `Monge--Amp\`ere 方程的数值解` | `sec:6.3` |
| `frontmatter/00-source-contents.tex:92` | 259 | `讨论` | `sec:6.4` |
| `frontmatter/00-source-contents.tex:93` | 259 | `\hspace{1em}离散数值方法` | `sec:6.4.1` |
| `frontmatter/00-source-contents.tex:94` | 266 | `\hspace{1em}半离散数值方法` | `sec:6.4.2` |
| `frontmatter/00-source-contents.tex:95` | 273 | `\textbf{概率测度上的泛函}` | `sec:7` |
| `frontmatter/00-source-contents.tex:96` | 274 | `半连续性` | `sec:7.1` |
| `frontmatter/00-source-contents.tex:97` | 274 | `\hspace{1em}势能、相互作用、运输成本与对偶范数` | `sec:7.1.1` |
| `frontmatter/00-source-contents.tex:98` | 278 | `\hspace{1em}局部泛函` | `sec:7.1.2` |
| `frontmatter/00-source-contents.tex:99` | 284 | `凸性、第一变分与次微分` | `sec:7.2` |
| `frontmatter/00-source-contents.tex:100` | 287 | `\hspace{1em}对偶范数` | `sec:7.2.1` |
| `frontmatter/00-source-contents.tex:101` | 288 | `\hspace{1em}运输成本` | `sec:7.2.2` |
| `frontmatter/00-source-contents.tex:102` | 291 | `\hspace{1em}最优性条件` | `sec:7.2.3` |
| `frontmatter/00-source-contents.tex:103` | 293 | `位移凸性` | `sec:7.3` |
| `frontmatter/00-source-contents.tex:104` | 294 | `\hspace{1em}$\mathscr V$ 与 $\mathscr W$ 的位移凸性` | `sec:7.3.1` |
| `frontmatter/00-source-contents.tex:105` | 295 | `\hspace{1em}$\mathscr F$ 的位移凸性` | `sec:7.3.2` |
| `frontmatter/00-source-contents.tex:106` | 299 | `\hspace{1em}广义测地线上的凸性` | `sec:7.3.3` |
| `frontmatter/00-source-contents.tex:107` | 300 | `讨论` | `sec:7.4` |
| `frontmatter/00-source-contents.tex:108` | 300 | `\hspace{1em}一个案例研究：$\min F(\varrho)+W_2^2(\varrho,\nu)$` | `sec:7.4.1` |
| `frontmatter/00-source-contents.tex:109` | 303 | `\hspace{1em}Brunn--Minkowski 不等式` | `sec:7.4.2` |
| `frontmatter/00-source-contents.tex:110` | 304 | `\hspace{1em}城市均衡` | `sec:7.4.3` |
| `frontmatter/00-source-contents.tex:111` | 309 | `\textbf{梯度流}` | `sec:8` |
| `frontmatter/00-source-contents.tex:112` | 309 | `$\mathbb R^d$ 及度量空间中的梯度流` | `sec:8.1` |
| `frontmatter/00-source-contents.tex:113` | 314 | `$\mathbb W_2$ 中的梯度流与偏微分方程的推导` | `sec:8.2` |
| `frontmatter/00-source-contents.tex:114` | 317 | `Fokker--Planck 情形的分析` | `sec:8.3` |
| `frontmatter/00-source-contents.tex:115` | 325 | `讨论` | `sec:8.4` |
| `frontmatter/00-source-contents.tex:116` | 325 | `\hspace{1em}EVI、唯一性与测地凸性` | `sec:8.4.1` |
| `frontmatter/00-source-contents.tex:117` | 328 | `\hspace{1em}其他梯度流偏微分方程` | `sec:8.4.2` |
| `frontmatter/00-source-contents.tex:118` | 335 | `\hspace{1em}Dirichlet 边界条件` | `sec:8.4.3` |
| `frontmatter/00-source-contents.tex:119` | 337 | `\hspace{1em}演化偏微分方程：不止梯度流` | `sec:8.4.4` |
| `frontmatter/00-source-contents.tex:120` | 348 | `\textbf{习题}` | `sec:exercises` |
| `frontmatter/00-source-contents.tex:121` | 362 | `\textbf{参考文献}` | `sec:references` |
| `frontmatter/00-source-contents.tex:122` | 374 | `\textbf{索引}` | `sec:index` |
| `sections-tex/01-01.tex:19` | 348 | `习题(1)` | `ex:1` |
| `sections-tex/01-01.tex:80` | 146 | `第4章` | `sec:4` |
| `sections-tex/01-02.tex:153` | 114 | `(3.1)` | `eq:3.1` |
| `sections-tex/01-03.tex:167` | 201 | `第5章` | `sec:5` |
| `sections-tex/01-03.tex:167` | 243 | `第6章` | `sec:6` |
| `sections-tex/01-04.tex:4` | 356 | `习题58` | `ex:58` |
| `sections-tex/01-04.tex:4` | 356 | `习题59` | `ex:59` |
| `sections-tex/01-05.tex:34` | 86 | `第2章` | `sec:2` |
| `sections-tex/01-07.tex:35` | 86 | `下一章` | `sec:2` |
| `sections-tex/01-07.tex:225` | 348 | `习题2` | `ex:2` |
| `sections-tex/01-07.tex:225` | 239 | `第5.5.5节` | `sec:5.5.5` |
| `sections-tex/01-07.tex:346` | 122 | `定义3.13` | `obj:3.13` |
| `sections-tex/01-07.tex:346` | 139 | `第3.3.2节` | `sec:3.3.2` |

## 未解决项

没有无法识别的引用。最终仅需root完成已协调的章节/书目/索引锚点整合，并在最终PDF核对内部跳转。完整机器可读清单为 `work/reference-internalization-records.json`。
