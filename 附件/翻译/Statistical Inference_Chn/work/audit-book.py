from pathlib import Path
from collections import Counter
import re,json,hashlib,sys,shutil,subprocess
B=Path(__file__).resolve().parents[1]
target=Path(sys.argv[1]) if len(sys.argv)>1 else B/'Statistical Inference_Chn.tex'
if not target.is_absolute():target=B/target
preview='--preview' in sys.argv
files=[]
def expand(p,stack=()):
 p=p.resolve()
 if p in stack:raise ValueError('Recursive input '+str(p))
 files.append(p);s=p.read_text(encoding='utf-8')
 def sub(m):
  q=B/m[1]
  if not q.suffix:q=q.with_suffix('.tex')
  return '\n'+expand(q,stack+(p,))+'\n'
 return re.sub(r'\\input\{([^}]+)\}',sub,s)
text=expand(target)
clean=re.sub(r'\\begin\{sourcecode\}.*?\\end\{sourcecode\}','',text,flags=re.S)
clean=re.sub(r'(?<!\\)%[^\n]*','',clean)
labels=[v for v in re.findall(r'\\label\{([^}]+)\}',clean) if '#' not in v]
labels+=['src:'+n for n in re.findall(r'\\sourcepageanchor\{(\d+)\}',clean)]
labels+=['idxocc:'+n for n in re.findall(r'\\semanticindexanchor\{([\d:]+)\}',clean)]
refs=re.findall(r'\\(?:ref|eqref|autoref|pageref)\*?\{([^}]+)\}',clean)+re.findall(r'\\hyperref\[([^]]+)\]',clean)
refs=[r for r in refs if '#'not in r]
errors=[];unresolved=sorted(set(refs)-set(labels))
errors+=['duplicate label '+x for x,n in Counter(labels).items() if n>1]
if not preview:errors+=['missing label '+x for x in unresolved]
envs=Counter(re.findall(r'\\begin\{([^}]+)\}',clean));ends=Counter(re.findall(r'\\end\{([^}]+)\}',clean))
if envs!=ends:errors.append('environment counts differ '+str(envs-ends)+str(ends-envs))
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
 if m[1]=='begin':stack.append(m[2])
 elif not stack or stack.pop()!=m[2]:errors.append('environment order '+m[0]);break
for img in re.findall(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}',clean):
 if not (B/img).exists():errors.append('missing asset '+img)
exercises={}
for v in re.findall(r'\\label\{exercise:(\d+\.\d+)\}',clean):exercises.setdefault(v.split('.')[0],[]).append(v)
for ch,nums in exercises.items():
 if nums!=[f'{ch}.{i}' for i in range(1,len(nums)+1)]:errors.append('exercise order '+ch)
baseline=json.loads((B/'work/source-baseline.json').read_text(encoding='utf-8'))
if hashlib.sha256(Path(baseline['path']).read_bytes()).hexdigest()!=baseline['sha256']:errors.append('source PDF changed')
stage=B/'work/book-static-input';stage.mkdir(exist_ok=True);(stage/'bib').mkdir(exist_ok=True)
(stage/'Combined_Chn.tex').write_text(text,encoding='utf-8');shutil.copyfile(B/'bib/references.bib',stage/'bib/references.bib')
checker=Path('C:/Users/Administrator/.codex/skills/pdf-to-chinese-tex/scripts/check_fidelity.py')
r=subprocess.run([sys.executable,'-X','utf8',str(checker),str(stage)],capture_output=True,text=True,encoding='utf-8')
(B/'work/book-fidelity-script.txt').write_text(r.stdout+r.stderr,encoding='utf-8')
if r.returncode:errors.append('bundled fidelity script: '+r.stdout+r.stderr)
manifest={'target':str(target.relative_to(B)),'preview':preview,'input_files':[str(p.relative_to(B)) for p in files],'labels':len(labels),'references':len(refs),'environments':dict(envs),'exercise_numbers':exercises,'source_page_anchors':[int(n) for n in re.findall(r'\\sourcepageanchor\{(\d+)\}',clean)],'unresolved_references':unresolved,'errors':errors,'source_sha256':baseline['sha256']}
(B/'work/book-static-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'files':len(files),'labels':len(labels),'refs':len(refs),'exercise_counts':{k:len(v)for k,v in exercises.items()},'unresolved_preview_refs':len(unresolved),'errors':errors},ensure_ascii=False))
sys.exit(bool(errors))
