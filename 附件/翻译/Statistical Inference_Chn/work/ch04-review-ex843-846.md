# 习题8.43与8.46独立数学复核

核对原PDF物理364／印刷333页，已实际查看 `work/ch08-source/p364.png`，并单独放大8.43的公式。未改第8章正文。此记录为基于源题的独立推导；没有查阅Sprott和Farewell原论文，不能把源题排印问题归因于该论文。

## 8.43

假定两组正态样本独立，n1,n2≥2，sigma²>0，r=rho²>0。若s_X²、s_Y²按通常分母n_i−1定义，则令

A=(n1−1)s_X²，B=(n2−1)s_Y²，nu=n1+n2−2。

正确的合并方差为(A+B/r)/nu，t统计量的分母平方为(1/n1+r/n2)(A+B/r)/nu。原书合并方差的A、B项多乘了n1、n2。在正态独立样本下，A/sigma²与B/(r sigma²)为独立卡方量，且独立于均值差，故该修正式具有t_nu分布。

正确的方差比是s_Y²/(r s_X²)，自由度次序为(n2−1,n1−1)。原式n2 s_Y²/(r n1 s_X²)多乘n2/n1，且声称的自由度顺序反了。如果原文小写s_i²本意是样本均值的方差估计，即通常样本方差除以n_i，那么两个n_i可以获得解释；但F自由度的倒置仍然存在。译注应给出该符号解释的边界，而不是无条件声称所有n_i都是多余的。

固定观察样本和均值差假设，展开分母平方（忽略正因子1/nu）为

A/n1+B/n2+(A/n2)r+(B/n1)/r。

导数为A/n2−B/(n1 r²)，故唯一最小点

r*=sqrt[n2(n2−1)s_Y²/(n1(n1−1)s_X²)]。

原文r=n1 sqrt(n1−1)s_X²/[n2 sqrt(n2−1)s_Y²]不等于此式。即使使用“s_i²为均值方差估计”的解释，原式分母的最小点也应为(n2/n1)sqrt[(n2−1)s_Y²/((n1−1)s_X²)]，仍与书中给出的最大化式不同。

还应区分有符号t与|t|：最小分母最大化|t|；只有分子为正时才最大化t本身。分子为负时，该点使t最小，t的上确界0在r趋0或无穷时逼近；分子为0时所有r均给出0。样本方差为0是正态连续模型下的零概率边界，可单独处理。

原页合并方差分母中还字面印有拉丁字符串rho²，而非希腊rho字形，应照录并说明。

## 8.46

假定n≥2、theta1<theta2、0<alpha<1，完整参数空间为(theta,sigma²)，sigma>0。令nu=n−1，c=t_(nu,alpha/2)>0，Z=(Xbar−theta)/(sigma/sqrt(n))，W=S/sigma；Z为标准正态，与W=sqrt(chi²_nu/nu)独立，且W>0几乎必然。

(a) 零假设下令a=sqrt(n)(theta2−theta)/sigma≥0、b=sqrt(n)(theta−theta1)/sigma≥0，则拒绝概率为

P(Z>a+cW)+P(Z<−b−cW)。

每项不超过alpha/2，而a+b=sqrt(n)(theta2−theta1)/sigma>0保证至少一项严格小于alpha/2。因此每一个有限sigma的零假设拒绝概率都严格小于alpha。但固定theta∈[theta1,theta2]，sigma趋无穷时a,b都趋0，拒绝概率趋于alpha。因此以全参数空间上确界定义的size恰为alpha，而不是“非size alpha”。

(b) 对任何有限k>0，在theta=theta2处令sigma趋0，|Xbar−theta_bar|依概率趋于(theta2−theta1)/2>0，而k S/sqrt(n)依概率趋0，故拒绝概率趋1。因此其size为1，不可能是0<alpha<1的size alpha检验。k≤0本身几乎总拒绝，亦不能给出所需alpha。

(c) 在上述完整参数空间下，两项“按自身size无偏”的结论也不能成立。(a)的实际size为alpha，而在任一固定有限sigma及theta=theta2处功效<alpha；功效关于theta连续，因此存在theta>theta2仍功效<alpha。(b)实际size为1，但有限k>0、有限sigma时接受域有正概率，功效严格小于1。

若sigma被事先固定，只把theta看作参数，则结论的解释不同：两种对称外侧拒绝域的功效关于|theta−theta_bar|递增，零假设最大值在端点取得；(a)此时的size严格小于alpha，(b)可以选择依赖于固定sigma、区间宽度和alpha的k。因此原题可有“固定sigma”的条件性解释，但不能直接据此得到对未知sigma统一成立的结论。

所有结果已发送总编；本记录不包含原论文核验，也不修改作者正文。
