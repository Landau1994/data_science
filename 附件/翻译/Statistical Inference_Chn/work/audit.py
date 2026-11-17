from pathlib import Path
import re,json,hashlib,subprocess,shutil,sys
from collections import Counter
B=Path(__file__).resolve().parents[1]
MAIN=B/'Statistical Inference_Chn.tex'
files=[MAIN]
for rel in re.findall(r'\\input\{([^}]+)\}',MAIN.read_text(encoding='utf-8')):files.append(B/rel)
text='\n'.join(p.read_text(encoding='utf-8') for p in files)
clean=re.sub(r'(?<!\\)%[^\n]*','',text)
labels=re.findall(r'\\label\{([^}]+)\}',clean)
refs=re.findall(r'\\(?:ref|eqref|autoref)\{([^}]+)\}',clean)+re.findall(r'\\hyperref\[([^]]+)\]',clean)
errors=[]
errors += ['duplicate label '+x for x,n in Counter(labels).items() if n>1]
errors += ['missing label '+x for x in set(refs)-set(labels)]
envs=Counter(re.findall(r'\\begin\{([^}]+)\}',clean));ends=Counter(re.findall(r'\\end\{([^}]+)\}',clean))
if envs!=ends:errors.append('environment mismatch '+str(envs-ends)+str(ends-envs))
for img in re.findall(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}',clean):
    if not (B/img).exists():errors.append('missing asset '+img)
ex=re.findall(r'\\label\{exercise:(1\.\d+)\}',clean)
if ex!=[f'1.{i}' for i in range(1,56)]:errors.append('exercise sequence mismatch')
baseline=json.loads((B/'work/source-baseline.json').read_text(encoding='utf-8'))
if hashlib.sha256(Path(baseline['path']).read_bytes()).hexdigest()!=baseline['sha256']:errors.append('source changed')
manifest={'input_files':[str(p.relative_to(B)) for p in files],'scope':'前置PDF1–31、第1章PDF32–68/印刷1–37','labels':len(labels),'references':len(refs),'objects':dict(envs),'exercise_numbers':ex,'errors':errors,'source_sha256':baseline['sha256']}
(B/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
stage=B/'work/static-input';stage.mkdir(exist_ok=True)
(stage/'Combined_Chn.tex').write_text(text,encoding='utf-8')
(stage/'bib').mkdir(exist_ok=True);shutil.copyfile(B/'bib/references.bib',stage/'bib/references.bib')
print(json.dumps({'files':len(files),'labels':len(labels),'refs':len(refs),'envs':dict(envs),'errors':errors},ensure_ascii=False))
sys.exit(bool(errors))
