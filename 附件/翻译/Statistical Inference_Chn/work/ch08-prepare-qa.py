from pathlib import Path
import re,json,sys,hashlib
root=Path.cwd();sys.path.insert(0,str(root/'work/python-deps'));import pymupdf as fitz
tex='\n'.join(p.read_text(encoding='utf-8-sig') for p in (root/'sections-tex').glob('08-*.tex'))
refs=set(re.findall(r'\\(?:auto|eq)?ref\{([^}]+)\}',tex))|set(re.findall(r'\\hyperref\[([^\]]+)\]',tex))
refs={r for r in refs if not re.search(r'(^|:)8(?:\.|$)',r)}
labels={}
for p in [root/'work/Statistical Inference_Chn.aux',*sorted((root/'work').glob('ch0[1-7]*.aux')),root/'work/integration-preview.aux']:
 if p.exists():
  for ln in p.read_text(encoding='utf-8-sig').splitlines():
   m=re.match(r'\\newlabel\{([^}]+)\}',ln)
   if m and m.group(1) in refs:labels[m.group(1)]=ln
(root/'work/ch08-external-labels.tex').write_text('% Local preview only: real labels imported from existing builds; foreign destinations are not validated here.\n'+'\n'.join(labels.values())+'\n',encoding='utf-8')
p=root/'work/ch08-preview.tex';s=p.read_text(encoding='utf-8-sig')
s=s.replace('\\input{work/ch08-external-labels.tex}\n','')
s=s.replace('\\begin{document}','\\input{work/ch08-external-labels.tex}\n\\begin{document}')
p.write_text(s,encoding='utf-8')
print('external refs',len(refs),'loaded',len(labels),'not loaded',sorted(refs-labels.keys()))
