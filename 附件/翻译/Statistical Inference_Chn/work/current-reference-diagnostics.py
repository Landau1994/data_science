from pathlib import Path
import json,re,sys,importlib.util
B=Path(__file__).resolve().parents[1]
chapters=sys.argv[1:]or['01','02','03','05','09','10'];ready={int(c)for c in chapters}
m=json.loads((B/'work/book-static-manifest.json').read_text(encoding='utf-8'))
bad=[]
for label in m['unresolved_references']:
 n=re.match(r'(?:sec|thm|def|ex|eq|lem|cor|exercise|fig|tab|item):([\d]+)',label)
 if n and int(n[1])in ready:bad.append(label)
print('Unresolved references into included chapters:',bad)
spec=importlib.util.spec_from_file_location('scan',B/'work/scan-plain-references.py');scan=importlib.util.module_from_spec(spec);spec.loader.exec_module(scan)
left=[]
for p in (B/'sections-tex').glob('*.tex'):
 if p.name[:2]not in chapters:continue
 s=p.read_text(encoding='utf-8');clean=scan.mask(s)
 for x in re.finditer(r'(?<!\d)(?:18|19|20)\d{2}(?:ab|[a-z])?(?!\d)',clean):
  context=s[max(0,x.start()-70):min(len(s),x.end()+80)].replace('\n',' ')
  if re.search(r'[A-Za-z]{3}',context):left.append({'file':p.name,'year':x[0],'line':s.count('\n',0,x.start())+1,'context':context})
(B/'work/citation-unlinked-contexts.json').write_text(json.dumps(left,ensure_ascii=False,indent=2),encoding='utf-8')
for r in left:print(r['file'],r['line'],r['context'])
