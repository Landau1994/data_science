from pathlib import Path
import subprocess, re, json, hashlib
BASE=Path(__file__).resolve().parents[1]
NAME='Statistical Optimal Transport_Chn'
OUT=BASE/'work/full-build'; OUT.mkdir(parents=True,exist_ok=True)
events=[]
def run(args,tag):
    p=subprocess.run(args,cwd=BASE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    s=p.stdout.decode('utf-8',errors='replace')
    (OUT/(tag+'.txt')).write_text(s,encoding='utf-8')
    events.append({'tag':tag,'command':args,'exit':p.returncode})
    print(tag,'exit',p.returncode,flush=True)
    if p.returncode:
        print(s[-7000:],flush=True)
        (BASE/'work/full-build-events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2),encoding='utf-8')
        raise SystemExit(p.returncode)
xe=['xelatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory=work/full-build',NAME+'.tex']
run(xe,'xelatex-1')
run(['bibtex','-terse','work/full-build/'+NAME],'bibtex')
bbl=OUT/(NAME+'.bbl')
t=bbl.read_text('utf-8')
t=re.sub(r'\\bibitem\{ref(\d+)\}',lambda m:'\\bibitem['+m[1]+']{ref'+m[1]+'}',t)
bbl.write_text(t,encoding='utf-8')
def makeidx(tag):
    rel='work/full-build/'+NAME
    run(['makeindex','-o',rel+'.ind','-t',rel+'.ilg',rel+'.idx'],tag)
    return (OUT/(NAME+'.idx')).read_bytes()
last=makeidx('makeindex-1')
run(xe,'xelatex-2')
last=makeidx('makeindex-2')
run(xe,'xelatex-3')
passno=3
while (OUT/(NAME+'.idx')).read_bytes()!=last and passno<6:
    last=makeidx(f'makeindex-{passno}')
    passno+=1; run(xe,f'xelatex-{passno}')
(BASE/'work/full-build-events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2),encoding='utf-8')
log=(OUT/(NAME+'.log')).read_text('utf-8',errors='replace')
for line in log.splitlines():
    if any(w in line for w in ['Overfull','undefined','Missing character','multiply defined','LaTeX Error','Warning']): print(line)
print('PDF built in work/full-build; delivery copy waits for final checks.',flush=True)
