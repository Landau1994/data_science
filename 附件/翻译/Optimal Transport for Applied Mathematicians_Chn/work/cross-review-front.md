# 前言、导论及致谢独立交叉复核

## 范围与方法

- 原书：Filippo Santambrogio，Optimal Transport for Applied Mathematicians，Springer 2015，本地原PDF.
- 审阅文件：`frontmatter/00-preface.tex`、`00-introduction.tex`、`00-acknowledgments.tex`.
- 实际读取原PDF物理8–21页全部逐页文本，并逐一目视`work/front-source-008.png`至`front-source-021.png`全部14张原页图. 未将提取文本当作公式与字体的最终依据.
- 逐段核对了正文、各个小标题、作者地点／日期／署名、两条编号公式、其余行间式、5条脚注，以及所有可见参考文献和编号交叉引用. 这些原文没有证明，译文未添加证明或独立数学讲解.

## 已直接修复

1. 导论物理19页熵记号原为普通斜体`E(\varrho)`，原稿误写成`\mathcal E(\varrho)`；现已恢复`E`. 通过pypdf的`visitor_text`核实原字体为Times-Italic，不是rsfs字体. 同页概率测度空间`\mathbb W_p`原字母W来自MSBM10，保留黑板体；密度`\varrho`与无微分符号的原积分按原页保留.
2. 致谢恢复“former advisor”为“我过去的导师”，将“close collaborator”精确表达为“与我密切合作的”，不把紧密合作替换为原文没有声明的“长期”.
3. 致谢末段“a sort of sabbatical semester”补足“学期”的原有信息，现为“一种类似学术休假学期的安排”.

## 数学与字体核对

- 导论公式(1)：两积分区域为`A`与`T^{-1}(A)`，`g(y)dy`及`f(x)dx`，Borel集合限定完整；保留原编号，并有`eq:intro1`标签.
- 导论公式(2)：原页确写`g(T(x))\det(DT(x))=f(x)`，未带绝对值. 译文保留，不擅自修正原公式；光滑性与单射条件在其前保留. 有`eq:intro2`标签及后续真实引用.
- 原弱-*紧性为`L^\infty`，原页图确认，不采信OCR将无穷读为1.
- Monge–Ampère式保留`\det(D^2u(x))=f(x)/g(\nabla u(x))`；极分解的复合说明完整.
- 物理17页Lebesgue测度字母L经pypdf核实来自rsfs10，译文已有`\mathscr L^d`，无需修改. 概率测度空间的`\mathbb W_p`与距离的普通`W_p`未混同.
- 原前言第3章概览中的第二个极限为`p=\infty`，原页12确认，译文正确.
- 导论的散度约束为`\nabla\cdot w=\mu-\nu`，符号与方向正确.

## 章外原页定位逐项检查

以下目标均以实际`work/page-NNN.txt`中的章／节标题或习题题目定位，再与本次原页图中的可见引用对照；不通过单一页码偏移推算.

| 引用 | 原PDF物理页 | 结果 |
| --- | --- | --- |
| 第2章 | 86 | 章标题存在 |
| 第3章 | 113 | 章标题存在 |
| 第4章 | 146 | 章标题存在 |
| 第5章 | 201 | 章标题存在 |
| 第6章 | 243 | 章标题存在 |
| 第7章 | 273 | 章标题存在 |
| 第8章 | 309 | 章标题存在 |
| §2.5.1 | 106 | Histogram equalization标题存在 |
| §2.5.3 | 110 | Isoperimetric inequality标题存在 |
| §4.4 | 176 | 实际Discussion标题存在，不只是页眉 |
| §4.4.2 | 187 | Branched transport标题存在 |
| §5.3.5 | 222 | Derivative of Wp along curves of measures标题存在 |
| §5.5.5 | 239 | Barycenters in W2标题存在 |
| §7.4.2 | 303 | Brunn–Minkowski inequality标题存在 |
| §8.4.4 | 337 | Evolution PDEs: not only gradient flows标题存在 |
| 习题(1) | 348 | Exercise 1完整题目存在 |

第1章、§1.7.2与§1.7.6采用译稿内部标签，待主任务构建与统一PDF目的地审计. 来源文献键均保留原编号，没有增造文献. 前言提及69道全书习题是作者原有介绍，不代表本次选译已翻译全书习题.

## 结论和边界

本范围未发现段落、公式、脚注或人名清单的缺失；仅作上述三处确定修订. 前言中的人名`L Ruschednorf`依原页保留原有写法，没有按外部知识静默改名. 此次是来源内容交叉复核，未编译主文件、未检查最终译稿页面布局、未声称最终PDF跳转已经验证；由主任务统一执行.
