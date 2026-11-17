from pathlib import Path
import re,importlib.util,json
B=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('scan',B/'work/scan-plain-references.py');scan=importlib.util.module_from_spec(spec);spec.loader.exec_module(scan)
cache={};log=[]
def read(n):
 if n not in cache:cache[n]=(B/'sections-tex'/n).read_text(encoding='utf-8')
 return cache[n]
def replace(n,a,b):
 s=read(n)
 if b in s:return
 assert s.count(a)==1,(n,a)
 cache[n]=s.replace(a,b);log.append({'file':n,'old':a,'new':b})
def item(n,label,part):
 s=read(n);key='itm:'+label+':'+part
 if r'\label{'+key+'}'in s:return key
 pos=s.index(r'\label{'+label+'}')
 end=re.search(r'\\end\{(?:theorem|definition|example|exercise)\}',s[pos:]);assert end,label
 section=s[pos:pos+end.start()];depth=0;count=0
 for m in re.finditer(r'\\(begin|end)\{enumerate\}|\\item(?:\[([^]]+)\])?',section):
  if m[1]=='begin':depth+=1
  elif m[1]=='end':depth-=1
  elif depth==1:
   count+=1;k=m[2].strip('()（） .')if m[2]else chr(96+count)
   if k==part:
    after=section[m.end():];old=re.match(r'\s*(?:\\phantomsection)?\\label\{([^}]+)\}',after)
    if old:return old[1]
    point=pos+m.end();cache[n]=s[:point]+r'\phantomsection\label{'+key+'}'+s[point:];return key
 raise ValueError((n,label,part))
def scope(n,start,end,keys):
 s=read(n);a=s.index(start);z=s.index(end,a+len(start))if end else len(s);seg=s[a:z];mask=scan.mask(seg)
 changes=[]
 for m in re.finditer(r'[（(]([a-z]|[ivx]+)[)）]',mask):
  if m[1]in keys:changes.append((m.start(),m.end(),r'\hyperref['+keys[m[1]]+']{'+m[0]+'}'))
 for x,y,t in reversed(changes):seg=seg[:x]+t+seg[y:]
 cache[n]=s[:a]+seg+s[z:];log.append({'file':n,'scope':start,'end':end,'links':len(changes)})
for label,parts,end in [('def:1.2.1','ab',r'\begin{example}'),('thm:1.2.8','abc',r'\begin{theorem}'),('thm:1.2.9','abc',r'\begin{example}'),('thm:1.2.11','ab',r'\subsubsection')]:
 keys={p:item('01-02.tex',label,p)for p in parts};scope('01-02.tex',r'\label{'+label+'}',end,keys)
replace('01-03.tex',r'定理\ref{thm:1.2.9}(a)',r'定理\ref{thm:1.2.9}\hyperref[itm:thm:1.2.9:a]{(a)}')
replace('01-03.tex','要证明(a)',r'要证明\hyperref[item:1.3.9a]{(a)}')
replace('01-06.tex',r'定理\ref{thm:1.2.9}(c)',r'定理\ref{thm:1.2.9}\hyperref[itm:thm:1.2.9:c]{(c)}')
replace('01-07.tex',r'定理\ref{thm:1.3.9}的(b)和(c)',r'定理\ref{thm:1.3.9}的\hyperref[item:1.3.9b]{(b)}和\hyperref[item:1.3.9c]{(c)}')
key=item('01-07.tex','exercise:1.32','ii');replace('01-07.tex','规则(ii)','规则'+r'\hyperref['+key+']{(ii)}')
keys={p:item('03-06.tex','thm:3.6.8',p)for p in 'ab'};scope('03-06.tex',r'\label{thm:3.6.8}',None,keys)
keys={p:item('03-08.tex','thm:3.8.1',p)for p in ['i','v']};scope('03-08.tex',r'\label{thm:3.8.1}',r'\end{theorem}',keys)
replace('03-01.tex','Johnson, Kotz, and Balakrishnan (1994, 1995)',r'Johnson, Kotz, and Balakrishnan (\hyperref[bib:source178]{1994}, \hyperref[bib:source179]{1995})')
replace('03-01.tex',r'\hyperref[bib:source177]{Johnson and Kotz (1969}–1972)',r'\hyperref[bib:source177]{Johnson and Kotz (1969–1972)}')
replace('03-05.tex','原文此处指向第3.2节',r'原文此处指向\hyperref[sec:3.2]{第3.2节}')
replace('03-05.tex','原交叉引用疑应为第3.3节',r'原交叉引用疑应为\hyperref[sec:3.3]{第3.3节}')
replace('05-01.tex',r'\autoref{thm:1.2.11}(a)',r'\autoref{thm:1.2.11}\hyperref[itm:thm:1.2.11:a]{(a)}')
replace('05-03.tex',r'\begin{proof}[\autoref{thm:5.3.1}(c)的证明]',r'\begin{proof}[{\autoref{thm:5.3.1}\hyperref[item:5.3.1c]{(c)}的证明}]')
key=item('05-06.tex','ex:5.6.7','b');scope('05-06.tex',r'\label{ex:5.6.7}',r'\subsubsection{接受／拒绝算法}',{'b':key})
key=item('05-07.tex','exercise:5.38','d');replace('05-08.tex',r'\autoref{exercise:5.38}(d)',r'\autoref{exercise:5.38}\hyperref['+key+']{(d)}')
for n,s in cache.items():(B/'sections-tex'/n).write_text(s,encoding='utf-8')
(B/'work/body-item-link-edits-first.json').write_text(json.dumps(log,ensure_ascii=False,indent=2),encoding='utf-8')
print('Linked verified body condition and cross-exercise subpart references;',len(cache),'files.')
