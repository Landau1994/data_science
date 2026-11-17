from pathlib import Path
B=Path(__file__).resolve().parents[1]
def l(n,s):return r'\hyperref[bib:source'+str(n)+']{'+s+'}'
changes={
'12-06.tex':[
 ('Carroll和Ruppert，1985，1988','Carroll和Ruppert，'+l(60,'1985')+'，'+l(61,'1988')),
 ('Hawkins（1993，1994，1995）','Hawkins（'+l(161,'1993')+'，'+l(162,'1994')+'，'+l(163,'1995')+'）'),
 ('Hettmansberger和McKean（1998）',l(165,'Hettmansberger和McKean（1998）'))],
'12-03.tex':[('Dalal等，1989',l(91,'Dalal等，1989'))],
'12-05.tex':[
 ('Ellis（1998）',l(115,'Ellis（1998）')),
 ('Portnoy和Misera（1998）',l(245,'Portnoy和Misera（1998）')+r'\footnote{译注：原正文写 Misera，书末对应文献写 Mizera；本段 Ellis 文献的书末条目没有列出年份. 保留原正文和书目各自的写法.}'),
 ('第(iii)项原称','第'+r'\hyperref[item:12.3.b.iii]{(iii)}'+'项原称'),
 ('(a)的$\\hat\\beta$',r'\hyperref[item:12.27.a]{(a)}的$\hat\beta$'),
 ('(b)导数右端',r'\hyperref[item:12.27.b]{(b)}导数右端')],
'12-04.tex':[
 ('第(1)至(3)项','第'+r'\hyperref[item:10.2.huber.1]{(1)}至\hyperref[item:10.2.huber.3]{(3)}项'),
 ('的第(1)项','的第'+r'\hyperref[item:10.2.huber.1]{(1)}项')]
}
for name,repls in changes.items():
 p=B/'sections-tex'/name;s=p.read_text(encoding='utf-8')
 for a,b in repls:assert a in s,(name,a);s=s.replace(a,b)
 p.write_text(s,encoding='utf-8')
p=B/'sections-tex/12-05.tex';s=p.read_text(encoding='utf-8')
assert r'\label{item:12.3.b.iii}' not in s
a=s.index(r'\label{exercise:12.3}');z=s.index(r'\end{exercise}',a);v=s[a:z]
needle=r'\item $D(A,B)=D(B,A)$';assert needle in v
v=v.replace(needle,r'\item\phantomsection\label{item:12.3.b.iii} $D(A,B)=D(B,A)$')
s=s[:a]+v+s[z:];p.write_text(s,encoding='utf-8')
print('Chapter 12 bibliography and body part links completed; one added bibliographic discrepancy note.')
