from pathlib import Path
B=Path(__file__).resolve().parents[1]
for name in ['01-computer-algebra.tex','01-computer-algebra-b.tex']:
 p=B/'backmatter'/name;s=p.read_text(encoding='utf-8')
 s=s.replace(r'\needspace{5\baselineskip}\medskip',r'\medskip')
 s=s.replace(r'\medskip\noindent\textit{\hyperref[sec:',r'\needspace{5\baselineskip}\medskip\noindent\textit{\hyperref[sec:')
 # Attach the two notes to the explanatory sentence before the code block.
 startphrase='译注：代码中的反斜线' if name=='01-computer-algebra.tex' else '译注：此处Out[3]中外部'
 start=s.index(r'\footnote{'+startphrase);pos=start+len(r'\footnote');depth=0;end=None
 for i in range(pos,len(s)):
  if s[i]=='{' and (i==0 or s[i-1]!='\\'):depth+=1
  elif s[i]=='}' and s[i-1]!='\\':
   depth-=1
   if depth==0:end=i+1;break
 note=s[start:end];s=s[:start]+s[end:]
 target='输入$f(x)$，并解出变换后的变量.' if name=='01-computer-algebra.tex' else '（当然，这一步实际上并不必要.）'
 if target not in s:raise ValueError(target)
 s=s.replace(target,target+note,1)
 p.write_text(s,encoding='utf-8')
p=B/'backmatter/02-distributions.tex';s=p.read_text(encoding='utf-8')
start=s.index(r'\footnote{译注：原页的矩公式');end=s.index('\n',start);note=s[start:end];s=s[:start]+s[end:]
target=r'$$\text{矩：}\quad EX^n='
if target not in s:raise ValueError(target)
s=s.replace(target,'矩：'+note+'\n$$EX^n=',1)
s=s.replace('（Gumbel）.',r'\mbox{（Gumbel）.}').replace('（$\gamma=1$）.',r'\mbox{（$\gamma=1$）.}')
p.write_text(s,encoding='utf-8')
print('Backmatter notes and heading layout adjusted.')
