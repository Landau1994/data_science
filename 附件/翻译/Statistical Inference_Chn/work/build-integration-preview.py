from pathlib import Path
import subprocess,sys
B=Path(__file__).resolve().parents[1]
s=(B/'Statistical Inference_Chn.tex').read_text(encoding='utf-8').split(r'\end{document}')[0]
chapters=[int(a)for a in sys.argv[1:]]or[2,3,5,9]
scope='第1、'+'、'.join(str(ch)for ch in chapters)+'章及书后材料合编预览'
s=s.replace('统计推断：书前材料及第1章中文译稿','统计推断：'+scope).replace('中文译稿：书前材料及第1章.','中文译稿：'+scope+'.').replace('按章校对，持续汇总全书；','中间核验版本；')
for ch in chapters:s+='\n'+r'\setcounter{section}{'+str(ch-1)+'}\n'+r'\input{chapters-tex/'+f'{ch:02}.tex'+'}\n'
s+='\n'+r'\appendix'+'\n'
for name in ['01-computer-algebra.tex','02-distributions.tex','03-references.tex','04-index.tex']:s+=r'\input{backmatter/'+name+'}\n'
s+=r'\end{document}'+'\n';(B/'work/integration-preview.tex').write_text(s,encoding='utf-8')
r=subprocess.run([sys.executable,'-X','utf8',str(B/'work/audit-book.py'),'work/integration-preview.tex','--preview'],cwd=B)
if r.returncode:raise SystemExit(r.returncode)
for n in range(1,4):
 r=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error','-output-directory=work','work/integration-preview.tex'],cwd=B,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 (B/f'work/integration-build-{n}.txt').write_bytes(r.stdout)
 print('pass',n,'exit',r.returncode)
 if r.returncode:print(r.stdout.decode('utf-8','replace')[-2000:]);raise SystemExit(r.returncode)
