from pathlib import Path
import subprocess
B=Path(__file__).resolve().parents[1]
main=(B/'Statistical Inference_Chn.tex').read_text(encoding='utf-8').split(r'\begin{document}',1)[0]
body='\n'.join(r'\input{backmatter/'+f+'}' for f in ['01-computer-algebra.tex','02-distributions.tex','03-references.tex','04-index.tex'])
(B/'work/back-preview.tex').write_text(main+'\n'+r'\begin{document}\appendix'+'\n'+body+'\n'+r'\end{document}',encoding='utf-8')
for n in range(1,3):
    r=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error','-output-directory=work','work/back-preview.tex'],cwd=B,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (B/f'work/back-build-{n}.txt').write_bytes(r.stdout)
    print('pass',n,'exit',r.returncode)
    if r.returncode: print(r.stdout.decode('utf-8','replace')[-1600:]);raise SystemExit(r.returncode)
