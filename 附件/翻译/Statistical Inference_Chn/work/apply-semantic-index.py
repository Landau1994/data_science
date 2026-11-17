"""Apply manually reviewed semantic mappings. Repeat safely after a revised map."""
from pathlib import Path
import re,json,sys
B=Path(__file__).resolve().parents[1]
entries={str(e['id']):e for e in json.loads((B/'work/index-translated.json').read_text(encoding='utf-8'))}
locations=[]
for p in sorted((B/'work').glob('index-locations-ch*.json')):locations.extend(json.loads(p.read_text(encoding='utf-8')))
if len({r['id'] for r in locations})!=len(locations):raise ValueError('Duplicate semantic mappings')
expected={r['id'] for r in json.loads((B/'work/index-semantic-candidates.json').read_text(encoding='utf-8'))}
if {r['id'] for r in locations}!=expected:raise ValueError(('Semantic index coverage',expected-{r['id'] for r in locations},{r['id'] for r in locations}-expected))
files={str(p.relative_to(B)).replace('\\','/'):p for p in (B/'sections-tex').glob('*.tex')}
texts={n:p.read_text(encoding='utf-8') for n,p in files.items()}
# Exact task-managed snippets only; retain every surrounding source character.
pat=re.compile(r'\s*%<semantic-index:[^>]+>\n.*?\n%</semantic-index>\s*',re.S)
# Entries are inserted inline so they cannot create a paragraph or break a formula.
def strip_managed(s):
 pattern=re.compile(r'\\index\{SI\d+@')
 spans=[]
 for m in pattern.finditer(s):
  depth=1;i=m.end()
  while i<len(s) and depth:
   if s[i]=='{' and s[i-1]!='\\':depth+=1
   elif s[i]=='}' and s[i-1]!='\\':depth-=1
   i+=1
  if depth:raise ValueError('Unbalanced managed index '+m[0])
  following=re.match(r'\\semanticindexanchor\{\d+:\d+\}',s[i:])
  if following:i+=following.end()
  spans.append((m.start(),i))
 for a,z in reversed(spans):s=s[:a]+s[z:]
 return s
for n,s in texts.items():texts[n]=strip_managed(s)
labels={}
for n,s in texts.items():
 for m in re.finditer(r'\\label\{([^}]+)\}',s):
  if m[1] in labels:raise ValueError('duplicate label '+m[1])
  labels[m[1]]=(n,m.end())
insertions={};resolved=[]
def esc(t):
 return t.replace('&',r'\&').replace('%',r'\%').replace('#',r'\#').replace('_',r'\_').replace('σ',r'$\sigma$').replace('²',r'${}^2$').replace('!',r'"!').replace('@',r'"@').replace('|',r'"|')
for r in locations:
 if 'label' in r:
  if r['label'] not in labels:raise ValueError(r)
  file,pos=labels[r['label']];target=r['label'];extra=''
 else:
  file=r['file'];s=texts[file];needle=r['after']
  if s.count(needle)!=1:raise ValueError(('ambiguous fragment',r,s.count(needle)))
  pos=s.index(needle)+len(needle);target='idxocc:'+r['id'];extra=r'\semanticindexanchor{'+r['id']+'}'
  # Manual fragments must end outside math and unclosed arguments.
  if needle.endswith('\\'):raise ValueError(r)
  pre=re.sub(r'(?<!\\)%[^\n]*','',s[:pos])
  depth=sum(1 if m[0]=='{'else -1 for m in re.finditer(r'(?<!\\)[{}]',pre))
  if depth or len(re.findall(r'(?<!\\)\$',pre))%2:raise ValueError(('Unsafe semantic insertion',r,depth))
 eid=r['id'].split(':')[0];e=entries[eid]
 token=r'\index{SI'+eid.zfill(4)+'@'+esc(e['zh'])+'}'+extra
 insertions.setdefault(file,[]).append((pos,token))
 resolved.append(dict(r,target=target,file=file))
if '--check' in sys.argv:
 print('Validated',len(resolved),'semantic mappings without changing TeX.')
else:
 for f,items in insertions.items():
  s=texts[f]
  for pos,token in sorted(items,reverse=True):s=s[:pos]+token+s[pos:]
  files[f].write_text(s,encoding='utf-8')
 (B/'work/index-semantic-resolved.json').write_text(json.dumps(resolved,ensure_ascii=False,indent=2),encoding='utf-8')
 print('Applied',len(resolved),'semantic index anchors to',len(insertions),'files.')
