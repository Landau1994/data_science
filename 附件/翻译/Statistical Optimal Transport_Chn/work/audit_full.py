from pathlib import Path
from collections import Counter
import re, json, hashlib, sys
BASE=Path(__file__).resolve().parents[1]
NAME='Statistical Optimal Transport_Chn'
main=BASE/(NAME+'.tex')
counts={1:8,2:10,3:8,4:6,5:10,6:8,7:5,8:5}
files=[BASE/f'sections-tex/{c:02}-{n:02}.tex' for c,count in counts.items() for n in range(1,count+1)]+[BASE/f'sections-tex/A-{n:02}.tex' for n in range(1,4)]+[BASE/'sections-tex/B-01.tex']
source=BASE.parents[1]/'books/Statistical Optimal Transport.pdf'
assert hashlib.sha256(source.read_bytes()).hexdigest().upper()=='91E9CB41212ABC18B294283C19CA4B91F51920A532E5CC24B710A1481EEED272'
outside={'原书第 5.6 节':'sec:5.6','原书定理 B.3':'thm:B.3','原书定理 B.4':'thm:B.4','原书引理 B.5':'lem:B.5','原书附录 B':'sec:B','附录 A':'sec:A','原书第 3 章':'sec:3','原书附录 A':'sec:A','原书定理 A.6':'thm:A.6','原书第 7 章':'sec:7','原书第2.8.1节':'sec:2.8.1','原书附录A':'sec:A'}
for f in files:
    if not f.exists(): continue
    t=f.read_text('utf-8').replace('。','.')
    if f.name.startswith('01-'):
        def external(m):
            k=outside.get(m[2]); return '\\autoref{'+k+'}' if k else m[0]
        t=re.sub(r'\\externalref\{([^}]+)\}\{([^}]+)\}',external,t)
        t=re.sub(r'\\label\{exer:(\d+)\}(?!\\label\{exer:1\.)',lambda m:m[0]+'\\label{exer:1.'+m[1]+'}',t)
    f.write_text(t,encoding='utf-8')
tex=main.read_text('utf-8')
def expand(t,visited):
    def sub(m):
        rel=m[1]; f=BASE/rel
        if f in visited: raise ValueError('Duplicate or circular include: '+rel)
        if not f.exists(): raise FileNotFoundError(rel)
        visited.append(f)
        return '\n% INCLUDED '+rel+'\n'+expand(f.read_text('utf-8'),visited)+'\n'
    return re.sub(r'\\input\{([^}]+)\}',sub,t)
visited=[]
joined=expand(tex,visited)
nc=re.sub(r'(?m)(?<!\\)%.*$','',joined)
labels=re.findall(r'\\label\{([^}]+)\}',nc)
refs=[]
for pat in [r'\\(?:autoref|eqref|ref)\{([^}]+)\}',r'\\hyperref\[([^]]+)\]']: refs+=re.findall(pat,nc)
cites={k.strip() for group in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}',nc) for k in group.split(',')}
bib=(BASE/'bib/references-full.bib').read_text('utf-8')
bibkeys=set(re.findall(r'@\w+\{([^,]+),',bib))
env=Counter(re.findall(r'\\begin\{([^}]+)\}',nc)); end=Counter(re.findall(r'\\end\{([^}]+)\}',nc))
errors=[]
dups=[k for k,v in Counter(labels).items() if v>1]
if dups: errors.append(('duplicate labels',dups))
missing=set(refs)-set(labels)
if missing: errors.append(('missing labels',sorted(missing)))
if cites-bibkeys: errors.append(('missing citations',sorted(cites-bibkeys)))
if env!=end: errors.append(('environment mismatch',dict(env-end),dict(end-env)))
body=nc[nc.index(r'\begin{document}'):]
if body.count(r'\appendix')!=1: errors.append(('appendix count',body.count(r'\appendix')))
for f in files:
    if f not in visited: errors.append(('not included',str(f.relative_to(BASE))))
    if f.exists() and f.read_text('utf-8').count(chr(36)*2)%2: errors.append(('unbalanced display delimiters',f.name))
for g in re.findall(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}',nc):
    if not (BASE/g).exists(): errors.append(('missing graphic',g))
if re.search(r'\\externalref\{',nc[nc.index(r'\begin{document}'):]): errors.append(('remaining external original-book references',True))
objects=json.loads((BASE/'work/full-source-objects.json').read_text('utf-8'))
prefix={'Proposition':'prop','Theorem':'thm','Definition':'def','Example':'ex','Lemma':'lem','Assumption':'assump','Corollary':'cor','Remark':'rem'}
for o in objects:
    k=prefix[o['type']]+':'+o['number']
    if k not in labels: errors.append(('missing source object',k))
equations={'1':25,'2':22,'3':9,'4':27,'5':32,'6':29,'7':17,'8':13,'A':3}
exercises={1:10,2:9,3:5,4:8,5:17,6:12,7:4,8:6}
for c,n in equations.items():
    for k in range(1,n+1):
        if f'eq:{c}.{k}' not in labels: errors.append(('missing numeric equation',f'{c}.{k}'))
for c,n in exercises.items():
    for k in range(1,n+1):
        if f'exer:{c}.{k}' not in labels: errors.append(('missing exercise',f'{c}.{k}'))
if env['exercise']!=71: errors.append(('exercise count',env['exercise']))
structured=sum(env[x] for x in ['theorem','lemma','proposition','corollary','definition','example','remark','assumption'])
if structured!=166: errors.append(('numbered statement count',structured))
manifest={'source':'../../books/Statistical Optimal Transport.pdf','scope':'All 269 physical pages','output':main.name,'input_files':[str(f.relative_to(BASE)).replace('\\','/') for f in visited],'bibliography':{'file':'bib/references-full.bib','entries':len(bibkeys),'source_numbers':list(range(1,331))},'objects':{},'totals':dict(env),'source_numbered_statements':166,'source_numeric_equations':177,'source_exercises':71,'labels':labels,'reference_occurrences':len(refs),'citation_keys':sorted(cites)}
for f in files:
    if f.exists():
        t=f.read_text('utf-8'); o=dict(Counter(re.findall(r'\\begin\{([^}]+)\}',t))); o['display_eqs']=t.count(chr(36)*2)//2
        manifest['objects'][f.stem]=o
(BASE/'work/manifest-full.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
(BASE/'work/full-static-check.json').write_text(json.dumps({'errors':errors,'labels':len(labels),'references':len(refs),'citation_keys':len(cites),'environments':dict(env)},ensure_ascii=False,indent=2),encoding='utf-8')
# Explicit expansion adapts the bundled checker's older directory convention.
scope=BASE/'work/full-static-scope'; (scope/'bib').mkdir(parents=True,exist_ok=True)
check=re.sub(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}',lambda m:''.join('\\cite{'+k.strip()+'}' for k in m[1].split(',')),joined)
(scope/'Statistical Optimal Transport_Chn.tex').write_text(check,encoding='utf-8')
(scope/'bib/references.bib').write_text(bib,encoding='utf-8')
(BASE/'work/full-combined-for-static.tex').write_text(joined.replace('{assets/','{../assets/'),encoding='utf-8')
print(json.dumps({'errors':errors,'labels':len(labels),'references':len(refs),'numbered_statements':structured,'exercises':env['exercise'],'bib':len(bibkeys)},ensure_ascii=False))
if errors: raise SystemExit(1)
