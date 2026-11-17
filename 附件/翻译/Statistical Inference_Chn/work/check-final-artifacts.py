from pathlib import Path
import json,re,sys,hashlib,subprocess,shutil
B=Path(__file__).resolve().parents[1]
checks=B/'work/final-checks';checks.mkdir(exist_ok=True)
log=B/'work/Statistical Inference_Chn.log'
shutil.copyfile(log,checks/log.name)
skill=Path('C:/Users/Administrator/.codex/skills/pdf-to-chinese-tex/scripts')
shutil.copytree(B/'assets',B/'work/book-static-input/assets',dirs_exist_ok=True)
check_runs=[]
for script,arg,name in [('check_math_overflow.py',checks,'math-overflow-run.txt'),('check_tex_static.py',B/'work/book-static-input/Combined_Chn.tex','static-check-run.txt')]:
 r=subprocess.run([sys.executable,'-X','utf8',str(skill/script),str(arg)],capture_output=True,text=True,encoding='utf-8',errors='replace')
 (checks/name).write_text(r.stdout+r.stderr,encoding='utf-8');print(script,'exit',r.returncode)
 check_runs.append({'script':script,'returncode':r.returncode,'output':str((checks/name).relative_to(B))})
static=json.loads((B/'work/book-static-manifest.json').read_text(encoding='utf-8'))
pdf=json.loads((B/'work/full-pdf-link-audit.json').read_text(encoding='utf-8'))
labels=json.loads((B/'work/full-pdf-label-destinations.json').read_text(encoding='utf-8'))
idx=json.loads((B/'work/index-build-audit.json').read_text(encoding='utf-8'))
source=json.loads((B/'work/source-baseline.json').read_text(encoding='utf-8'))
errors=[]
for key in ['errors','unresolved_references']:
 if static[key]:errors.append((key,static[key]))
for key in ['bad_links','number_errors','missing_index_targets']:
 if pdf[key]:errors.append((key,pdf[key]))
if [k for k,v in labels.items()if not v.get('resolved_destination')]:errors.append('missing PDF named destinations')
if idx['semantic_locations']!=1174 or idx['entries']!=1071:errors.append('index coverage')
if sum(len(v)for v in static['exercise_numbers'].values())!=625:errors.append('exercise count')
if pdf['number_checks']!=1688:errors.append('numbered object count')
text=log.read_text(encoding='utf-8',errors='replace')
for pattern in [r'LaTeX Error',r'Undefined control sequence',r'Missing character',r'Reference .*undefined',r'There were undefined references',r'multiply defined',r'Overfull \\hbox',r'Emergency stop',r'Fatal error']:
 if re.search(pattern,text):errors.append(('log',pattern))
input_hashes={p:hashlib.sha256((B/p).read_bytes()).hexdigest()for p in static['input_files']}
assets={}
for p in static['input_files']:
 t=(B/p).read_text(encoding='utf-8')
 for q in re.findall(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}',t):assets[q]=hashlib.sha256((B/q).read_bytes()).hexdigest()
notes=[]
for p in static['input_files']:
 t=(B/p).read_text(encoding='utf-8')
 for m in re.finditer(r'\\footnote(?:text)?(?:\[[^]]*\])?\{',t):
  i=m.end();d=1
  while i<len(t)and d:
   if t[i]=='{'and t[i-1]!='\\':d+=1
   elif t[i]=='}'and t[i-1]!='\\':d-=1
   i+=1
  note=t[m.end():i-1]
  notes.append({'file':p,'line':t.count('\n',0,m.start())+1,'kind':'translator'if note.startswith('译注')else'original','text':note})
(B/'work/all-footnotes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2),encoding='utf-8')
result={'source':source,'pdf':{'pages':pdf['pages'],'sha256':pdf['sha256'],'links':pdf['target_counts'],'bookmarks':len(pdf['bookmarks'])},'input_hashes':input_hashes,'asset_hashes':assets,'static_labels':static['labels'],'explicit_references':static['references'],'object_counts':static['environments'],'exercises_by_chapter':{k:len(v)for k,v in static['exercise_numbers'].items()},'number_checks':pdf['number_checks'],'index':idx,'footnotes':{'original':sum(n['kind']=='original'for n in notes),'translator':sum(n['kind']=='translator'for n in notes)},'errors':errors}
(B/'work/final-artifact-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
(checks/'check-runs.json').write_text(json.dumps(check_runs,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'pages':pdf['pages'],'assets':len(assets),'footnotes':result['footnotes'],'errors':errors},ensure_ascii=False))
raise SystemExit(bool(errors))
