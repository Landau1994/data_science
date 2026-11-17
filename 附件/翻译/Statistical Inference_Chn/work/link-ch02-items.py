from pathlib import Path
import re
B=Path(__file__).resolve().parents[1]
def additemlabel(s,env,label,part):
 key='itm:'+label+':'+part
 if r'\label{'+key+'}'in s:return s
 pat=r'(\\begin\{'+env+r'\}[^\n]*\\label\{'+re.escape(label)+r'\}.*?)(\\item\[\('+part+r'\)\])'
 m=re.search(pat,s,re.S);assert m,(label,part)
 assert r'\end{'+env+'}'not in m[1],(label,part)
 return s[:m.end()]+r'\phantomsection\label{'+key+'}'+s[m.end():]
p=B/'sections-tex/02-02.tex';s=p.read_text(encoding='utf-8')
s=additemlabel(s,'theorem','thm:2.2.5','a')
s=s.replace('这就证明了 (a).',r'这就证明了 \hyperref[itm:thm:2.2.5:a]{(a)}.')
p.write_text(s,encoding='utf-8')
p=B/'sections-tex/02-04.tex';s=p.read_text(encoding='utf-8')
for part in ['i','ii']:s=additemlabel(s,'theorem','thm:2.4.3',part)
# These eight references have all been checked in their theorem's prose context.
for part in ['i','ii']:
 s=s.replace('条件 ('+part+')','条件 '+r'\hyperref[itm:thm:2.4.3:'+part+']{('+part+')}')
s=s.replace(r'\hyperref[itm:thm:2.4.3:i]{(i)}、(ii)',r'\hyperref[itm:thm:2.4.3:i]{(i)}、\hyperref[itm:thm:2.4.3:ii]{(ii)}')
p.write_text(s,encoding='utf-8')
p=B/'sections-tex/02-05.tex';s=p.read_text(encoding='utf-8')
for n,part,phrase in [('2.7','a','这一推广解答 (a)'),('2.8','c','注意，(c) 中'),('2.14','a','将此与 (a) 比较'),('2.26','d','证明，对 (d) 中的密度'),('2.29','a','用 (a) 的结果计算')]:
 label='exercise:'+n;s=additemlabel(s,'exercise',label,part)
 s=s.replace(phrase,phrase.replace('('+part+')',r'\hyperref[itm:'+label+':'+part+']{('+part+')}'))
p.write_text(s,encoding='utf-8')
print('Linked theorem conditions and exercise subparts in chapter 2.')
