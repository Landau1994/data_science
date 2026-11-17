from pathlib import Path
import re,hashlib,json
b=Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn')
images={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (b/'work/ch09-output').glob('page-*.png')};(b/'work/ch09-visual-before.json').write_text(json.dumps(images))
p=b/'sections-tex/09-02.tex';t=p.read_text(encoding='utf-8').replace('首先假设$T$是连续\n','首先假设$T$是连续随机变量.\n').replace('随机变量. $T$离散时','当$T$离散时');p.write_text(t,encoding='utf-8')
for p in (b/'sections-tex').glob('09-*.tex'):
 t=p.read_text(encoding='utf-8')
 while True:
  m=re.search(r'\$\$\n\\footnote\{',t)
  if not m:break
  start=m.start()+3;end=start+len('\\footnote{');depth=1
  while depth:
   if t[end]=='{':depth+=1
   elif t[end]=='}':depth-=1
   end+=1
  note=t[start:end];op=t.rfind('$$',0,m.start());t=t[:op].rstrip()+note+'\n'+t[op:start]+t[end:]
 # note following enumerate: put on final item ending
 pattern='\\end{enumerate}\n\\footnote{'
 if pattern in t:
  start=t.index(pattern)+len('\\end{enumerate}\n');end=start+len('\\footnote{');depth=1
  while depth:
   if t[end]=='{':depth+=1
   elif t[end]=='}':depth-=1
   end+=1
  note=t[start:end];e=t.rfind('\\end{enumerate}',0,start);t=t[:e].rstrip()+note+'\n'+t[e:start]+t[end:]
 p.write_text(t,encoding='utf-8')
