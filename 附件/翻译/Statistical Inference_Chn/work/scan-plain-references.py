from pathlib import Path
import re,json,sys
B=Path(__file__).resolve().parents[1]
def endbrace(s,i):
 d=0
 for j in range(i,len(s)):
  if s[j]=='{' and (j==0 or s[j-1]!='\\'):d+=1
  elif s[j]=='}' and (j==0 or s[j-1]!='\\'):
   d-=1
   if d==0:return j+1
 return len(s)
def blank(s,a,z):return s[:a]+''.join('\n'if c=='\n'else' 'for c in s[a:z])+s[z:]
def mask(s):
 for pat in [r'(?<!\\)%[^\n]*',r'\\begin\{sourcecode\}.*?\\end\{sourcecode\}',r'\\begin\{(equation\*?|align\*?|gather\*?)\}.*?\\end\{\1\}',r'(?<!\\)\$\$.*?(?<!\\)\$\$',r'(?<!\\)\$.*?(?<!\\)\$']:
  for m in list(re.finditer(pat,s,re.S))[::-1]:s=blank(s,m.start(),m.end())
 for m in list(re.finditer(r'\\(?:hyperref\[[^]]+\]|(?:label|index|semanticindexanchor|sourcepageanchor|url|href))\{',s))[::-1]:s=blank(s,m.start(),endbrace(s,m.end()-1))
 for m in list(re.finditer(r'\\item\[[^]]*\]',s))[::-1]:s=blank(s,m.start(),m.end())
 return s
if __name__=='__main__':
 chapters=sys.argv[1:]or['01','02','05','09'];out=[]
 for p in (B/'sections-tex').glob('*.tex'):
  if p.name[:2]not in chapters:continue
  s=p.read_text(encoding='utf-8');clean=mask(s)
  for m in re.finditer(r'(?:定义|定理|引理|推论|例|习题|公式|表|图|第)\s*\d+(?:\.\d+)*(?:章|节)?|[（(](?:[a-z]|[ivx]+|\d+(?:\.\d+)*)[)）]',clean):
   # Bibliography years, labels, and titles are classified later, never silently assumed to be references.
   out.append({'file':p.name,'line':s.count('\n',0,m.start())+1,'text':m[0],'context':s[max(0,m.start()-60):min(len(s),m.end()+80)].replace('\n',' '),'offset':m.start()})
 (B/'work/plain-reference-candidates.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
 for r in out:print(f"{r['file']}:{r['line']} | {r['text']} | {r['context']}")
 print('Total candidates:',len(out))
