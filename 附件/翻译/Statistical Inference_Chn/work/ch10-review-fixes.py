import pathlib
b=pathlib.Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn')
p=b/'sections-tex/10-01.tex';t=p.read_text(encoding='utf-8')
t=t.replace(r'\autoref{exercise:5.5.22}',r'\hyperref[ex:5.5.22]{习题5.5.22}\footnote{译注：原文称“习题5.5.22”，实际对应\autoref{ex:5.5.22}. 原称呼保留，链接指向对应例.}')
t=t.replace('（这不应令人意外，因为\\eqref{eq:10.1.7}表明Delta方法方差估计基于一个下界.）','（这不应令人意外，因为\\eqref{eq:10.1.7}表明Delta方法方差估计基于一个下界.）'+r'\footnote{译注：表中“真实值”与所述$n=24$二项模型不符. 按该模型对$Y=0,\ldots,24$逐项求和，$\operatorname{Var}[(Y/24)(1-Y/24)]$在$p=1/4,1/2,2/3$时约为$.001911,.000208,.001109$，并非表中的$.00484,.00531,.00519$. 原表及其比较结论保留；此核算仅针对表述的这三个参数值.}')
p.write_text(t,encoding='utf-8')
p=b/'sections-tex/10-04.tex';t=p.read_text(encoding='utf-8').replace(r'由\eqref{eq:7.4.1}',r'由\hyperref[eq:10.1.7]{(7.4.1)}');p.write_text(t,encoding='utf-8')
p=b/'sections-tex/10-05.tex';t=p.read_text(encoding='utf-8');t=t.replace('证明这个方差估计等于$2[\\operatorname{Var}(\\hat p)]^2$.','证明这个方差估计等于$2[\\operatorname{Var}(\\hat p)]^2$.'+r'\footnote{译注：(a)的$.00007$对应一阶Delta近似，而非题干所列二阶形式；(b)的$.00529$也与$n=24,p=11/24$下对二项概率逐项求和所得方差（约$.000271$）不符. 原题数值保留，须核查原书的数值计算或统计量表述.}')
p.write_text(t,encoding='utf-8')
