from pathlib import Path
import re,json
B=Path(__file__).resolve().parents[1]
files={p.name:p for p in (B/'sections-tex').glob('01-*.tex')}
data={k:p.read_text(encoding='utf-8') for k,p in files.items()}
items=[
(32,'01-00.tex','text',r'\begin{quote}'),
(33,'01-01.tex','text','可数与不可数样本空间的区别'),
(34,'01-01.tex','text','基本集合运算可以组合起来'),
(35,'01-01.tex','text','例如，令$S=(0,1]$'),
(36,'01-02.tex','text',r'\subsubsection{公理化基础}'),
(37,'01-02.tex','label','def:1.2.4'),
(38,'01-02.tex','label','fig:1.2.1'),
(39,'01-02.tex','label','thm:1.2.8'),
(40,'01-02.tex','label','ex:1.2.10'),
(41,'01-02.tex','text','最后一个等号来自分配律'),
(42,'01-02.tex','text','移项后变为'),
(43,'01-02.tex','text','开始计数之前'),
(44,'01-02.tex','text','对此计数时，最简单的想法'),
(45,'01-02.tex','label','ex:1.2.19'),
(46,'01-02.tex','label','ex:1.2.20'),
(47,'01-02.tex','label','fig:1.2.2'),
(48,'01-03.tex','label','def:1.3.2'),
(49,'01-03.tex','label','ex:1.3.4'),
(50,'01-03.tex','label','thm:1.3.5'),
(51,'01-03.tex','label','def:1.3.7'),
(52,'01-03.tex','label','ex:1.3.10'),
(53,'01-03.tex','label','def:1.3.12'),
(54,'01-04.tex','label','def:1.4.1'),
(55,'01-04.tex','label','ex:1.4.4'),
(56,'01-05.tex','label','fig:1.5.1'),
(57,'01-05.tex','label','ex:1.5.5'),
(58,'01-05.tex','label','fig:1.5.2'),
(59,'01-05.tex','label','def:1.5.8'),
(60,'01-06.tex','label','def:1.6.3'),
(61,'01-06.tex','label','fig:1.6.1'),
(62,'01-06.tex','text','从纯数学的观点看'),
(63,'01-07.tex','label','exercise:1.6'),
(64,'01-07.tex','label','exercise:1.17'),
(65,'01-07.tex','label','exercise:1.29'),
(66,'01-07.tex','label','exercise:1.37'),
(67,'01-07.tex','label','exercise:1.43'),
(68,'01-07.tex','label','exercise:1.53'),
]
for n,f,kind,target in items:
    s=data[f]
    if r'\sourcepageanchor{'+str(n)+'}' in s:continue
    if kind=='text':
        if s.count(target)!=1:raise ValueError((n,f,target,s.count(target)))
        pos=s.index(target)
    else:
        needle=r'\label{'+target+'}'
        if s.count(needle)!=1:raise ValueError((n,f,target))
        pos=s.rfind(r'\begin{',0,s.index(needle))
        # Captions are within their enclosing figure; all other labels follow begin.
        if pos<0:raise ValueError((n,'no begin',target))
    data[f]=s[:pos]+'\n\\sourcepageanchor{'+str(n)+'}\n\n'+s[pos:]
for f,s in data.items():files[f].write_text(s,encoding='utf-8')
(B/'work/ch01-anchor-map.json').write_text(json.dumps({'scope':'原物理页32–68；在最近完整段落或新对象处设置导航点，跨页公式与证明不中断。页40、49、52、65、67导航至该页首个新对象。','anchors':items},ensure_ascii=False,indent=2),encoding='utf-8')
print('chapter 1 anchors:',len(items))
