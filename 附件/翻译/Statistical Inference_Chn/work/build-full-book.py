from pathlib import Path
import subprocess,sys
B=Path(__file__).resolve().parents[1]
r=subprocess.run([sys.executable,'-X','utf8','work/audit-book.py'],cwd=B)
if r.returncode:raise SystemExit(r.returncode)
for n in range(1,4):
 r=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error','-output-directory=work','Statistical Inference_Chn.tex'],cwd=B,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 (B/f'work/full-build-{n}.txt').write_bytes(r.stdout)
 print('pass',n,'exit',r.returncode,flush=True)
 if r.returncode:print(r.stdout.decode('utf-8','replace')[-4000:]);raise SystemExit(r.returncode)
