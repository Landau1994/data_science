from pathlib import Path
import re
B=Path(__file__).resolve().parents[1]
def edit(name,repls):
 p=B/'sections-tex'/name;s=p.read_text(encoding='utf-8')
 for a,b in repls:
  assert a in s,(name,a)
  s=s.replace(a,b)
 p.write_text(s,encoding='utf-8')
def link(n,s):return r'\hyperref[bib:source'+str(n)+']{'+s+'}'
edit('07-04.tex',[
 ('Schwarz和Samantha（1991）',link(281,'Schwarz和Samantha（1991）')),
 ('用归纳论证证明了这些事实.',r'用归纳论证证明了这些事实.\footnote{译注：此处原文写 Samantha，书末对应文献作者为 Samanta；保留原拼写，链接指向该条文献.}'),
 (r'\hyperref[exercise:7.10]{习题7.10(c)}',r'\hyperref[itm:exercise:7.10:c]{习题7.10(c)}'),
 ('\n\\item 给出下列数据', '\n\\item 给出下列数据') if False else ('\\label{exercise:7.10}', '\\label{exercise:7.10}')
])
# Add the exact target for the cross-exercise part, without changing its visible label.
p=B/'sections-tex/07-04.tex';s=p.read_text(encoding='utf-8');start=s.index(r'\label{exercise:7.10}');end=s.index(r'\end{exercise}',start);part=s[start:end]
items=list(re.finditer(r'\\item(?![A-Za-z])(?:\[[^\]]*\])?',part));assert len(items)==3
at=start+items[2].end();s=s[:at]+r'\phantomsection\label{itm:exercise:7.10:c}'+s[at:];p.write_text(s,encoding='utf-8')
edit('07-05.tex',[
 ('和Wu（1983）','和'+link(335,'Wu（1983）')),
 ('Sheaffer（1997）',link(274,'Sheaffer（1997）')+r'\footnote{译注：原文作者写 Sheaffer；书末与此处主题、年份相符的书目为 Schafer（1997）的《Analysis of Incomplete Multivariate Data》. 保留原拼写，并链接至该书目.}'),
 ('Berger（1990，1994）与Wasserman（1994）','Berger（'+link(19,'1990')+'，'+link(20,'1994')+'）与'+link(327,'Wasserman（1994）')+r'\footnote{译注：原文在此写 Wasserman（1994），书末对应稳健贝叶斯综述列为1992年；保留原年份，链接至该条文献.}'),
 ('Casella（1985，1992）','Casella（'+link(63,'1985')+'，'+link(65,'1992')+'）'),
 ('Lehmann和Casella（1999，第4.5节）',link(200,'Lehmann和Casella（1999，第4.5节）')+r'\footnote{译注：此处原文写1999年，书末该书第二版列为1998年；原年份保留.}')
])
edit('11-02.tex',[('Fisher（1935，1939）','Fisher（'+link(125,'1935')+'，'+link(126,'1939')+'）')])
edit('11-05.tex',[
 ('和Hsu（1996）','和'+link(169,'Hsu（1996）')),
 ('Naiman（1983，1984，1987）及Naiman和Wynn（1992，1997）','Naiman（'+link(227,'1983')+'，'+link(228,'1984')+'，'+link(229,'1987')+'）及Naiman和Wynn（'+link(230,'1992')+'，'+link(231,'1997')+'）'),
 ('（1972，1973，1975）','（'+link(111,'1972')+'，'+link(112,'1973')+'，'+link(113,'1975')+'）')
])
def scoped_items(name,startneedle,endneedle,key,parts,refs):
 p=B/'sections-tex'/name;s=p.read_text(encoding='utf-8');a=s.index(startneedle);z=s.index(endneedle,a)+len(endneedle);v=s[a:z]
 items=list(re.finditer(r'\\item(?![A-Za-z])(?:\[[^\]]*\])?',v));assert len(items)>=len(parts)
 for m,part in reversed(list(zip(items,parts))):v=v[:m.end()]+r'\phantomsection\label{itm:'+key+':'+part+'}'+v[m.end():]
 s=s[:a]+v+s[z:]
 for old,part in refs:
  assert s.count(old)==1,(name,old,s.count(old));s=s.replace(old,old.replace('('+part+')',r'\hyperref[itm:'+key+':'+part+']{('+part+')}'))
 p.write_text(s,encoding='utf-8')
scoped_items('04-02.tex',r'\label{thm:4.2.10}',r'\end{theorem}','thm:4.2.10',['a','b'],[('对于连续随机变量，(b)','b'),('结论. (a) 可以','a')])
scoped_items('04-05.tex','此分布有许多良好性质，包括：',r'\end{enumerate}','bivnormal',['a','b','c','d'],[])
edit('04-05.tex',[('性质 (a)、(b)、(d) 的验证','性质 '+r'\hyperref[itm:bivnormal:a]{(a)}、\hyperref[itm:bivnormal:b]{(b)}、\hyperref[itm:bivnormal:d]{(d)} 的验证'),('假设 (a)、(b) 成立，下面证明 (c).',r'假设 \hyperref[itm:bivnormal:a]{(a)}、\hyperref[itm:bivnormal:b]{(b)} 成立，下面证明 \hyperref[itm:bivnormal:c]{(c)}.')])
scoped_items('04-07.tex',r'\label{thm:4.7.9}',r'\end{theorem}','thm:4.7.9',['a','b'],[('很简单：(a)','a'),('负相关，(b)','b')])
edit('04-08.tex',[(r'\item[(iii)] 定义 $a_i=',r'\item[(iii)]\phantomsection\label{itm:exercise:4.57:b:iii} 定义 $a_i='),('Section 2.7). (iii) 的结论',r'Section 2.7). \hyperref[itm:exercise:4.57:b:iii]{(iii)} 的结论')])
edit('04-09.tex',[(r'\item[(3)] $Z_3=',r'\item[(3)]\phantomsection\label{itm:borel:3} $Z_3='),('特别是 (3) 中',r'特别是 \hyperref[itm:borel:3]{(3)} 中')])
scoped_items('07-02.tex',r'\label{ex:7.2.12}',r'\end{enumerate}','ex:7.2.12',['a','b','c'],[])
edit('07-02.tex',[('容易看出(a)和(b)成立',r'容易看出\hyperref[itm:ex:7.2.12:a]{(a)}和\hyperref[itm:ex:7.2.12:b]{(b)}成立')])
print('Completed reviewed citations, four bibliography discrepancy footnotes, and body item links.')
