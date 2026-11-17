from pathlib import Path
import json,hashlib
root=Path.cwd()
render=root/'work/ch08-render'
(root/'work/ch08-pre-final-render-hashes.json').write_text(json.dumps({p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in render.glob('p*.png')}),encoding='utf-8')
def take_note(s,prefix):
 start=s.index('\\footnote{'+prefix);i=start+len('\\footnote{');depth=1
 while depth:
  if s[i]=='{' and s[i-1]!='\\':depth+=1
  elif s[i]=='}' and s[i-1]!='\\':depth-=1
  i+=1
 return s[start:i],start,i
p=root/'sections-tex/08-03-2.tex';s=p.read_text(encoding='utf-8');note,a,b=take_note(s,'译注：这里的 $\\mathscr T$')
s=s[:a]+s[b:]
pos=s.index('$$T>t_0')
s=s[:pos].rstrip()+note+'\n'+s[pos:]
p.write_text(s,encoding='utf-8')
for file,prefix in [('08-04.tex','译注：原题未明示参数空间.'),('08-04-b.tex','译注：(b) 需取似然比非减的方向')]:
 p=root/'sections-tex'/file;s=p.read_text(encoding='utf-8');note,a,b=take_note(s,prefix)
 end=s.rfind('\\end{enumerate}',0,a)
 assert not s[end+len('\\end{enumerate}'):a].strip()
 s=s[:end].rstrip()+note+'\n\\end{enumerate}'+s[b:]
 p.write_text(s,encoding='utf-8')
p=root/'sections-tex/08-04-b.tex';s=p.read_text(encoding='utf-8');note,a,b=take_note(s,'译注：原题对干扰参数 $\\sigma$')
s=s[:a]+s[b:]
target='无偏的. （假定非中心 $t$ 分布具有单调似然比.）'
assert target in s
s=s.replace(target,'无偏的.'+note+' （假定非中心 $t$ 分布具有单调似然比.）')
note,a,b=take_note(s,'译注：原文确为“例 5.4.1”')
s=s[:a]+s[b:]
target='\\hyperref[ex:5.3.5]{例~5.4.1}.）'
assert target in s
s=s.replace(target,'\\hyperref[ex:5.3.5]{例~5.4.1}'+note+'.）')
p.write_text(s,encoding='utf-8')
