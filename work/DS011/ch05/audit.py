from pathlib import Path
import json,re,yaml,sys
ROOT=Path.cwd();MAP=ROOT/'工具/StatisticalInference/source-manifest.json'
rows=json.loads(MAP.read_text(encoding='utf-8'))['chapters']['5']['exercises']
old=json.loads((ROOT/'附件/翻译/Statistical Inference_Chn/work/ch05-manifest.json').read_text(encoding='utf-8'))
expected={x['id']:list(x['source_letter_parts']) for x in old['exercises']}
errors=[];checks=[];allparts=0
if [x['source_exercise'] for x in rows]!=[f'5.{n}' for n in range(1,70)]:errors.append('ordered question set')
if [x['local_id'] for x in rows]!=[f'ST{n:03d}' for n in range(12,81)]:errors.append('local ID set')
for row in rows:
    p=ROOT/row['note'];s=p.read_text(encoding='utf-8');meta=yaml.safe_load(s.split('---',2)[1]);n=int(row['source_exercise'].split('.')[1]);e=[]
    for key in ['title','topic','topic_label','difficulty','status','tags','source','source_id','source_chapter','source_exercise','source_stars','source_refs','source_status','solution_status','created']:
        if key not in meta:e.append('metadata missing '+key)
    if meta['topic']!='mathematical-statistics' or meta['source_chapter']!=5 or meta['source_exercise']!=row['source_exercise'] or meta['status']!='not-started' or meta['source_status']!='verified':e.append('metadata values')
    if row['subparts']!=expected[row['source_exercise']]:e.append('map parts')
    eng=s.split('### 英文原题',1)[1].split('### 中文转述',1)[0]
    cn=s.split('### 中文转述',1)[1].split('## 提示',1)[0]
    for label,part in [('english',eng),('chinese',cn)]:
        parts=re.findall(r'^> (?:\*\*[^*]+\*\* )?\(([a-z])\)',part,re.M)
        if parts!=expected[row['source_exercise']]:e.append(label+' parts '+str(parts))
    if s.count('> [!success]- 解答')!=1:e.append('unique solution')
    if s.count('> [!question]')!=2:e.append('bilingual question')
    if '> [!hint]-' not in s:e.append('folded hint')
    if len(re.findall(r'(?<!\\)\$',s))%2:e.append('dollars')
    for ch in s:
        if ord(ch)<32 and ch not in '\n\t\r':e.append('control character '+str(ord(ch)));break
    if re.search(r'\\(?:begin\{enumerate\}|item|autoref|hyperref|sourcepageanchor|CJKfontspec|needspace)',s):e.append('unconverted source markup')
    if re.search('TABLE(?:37|54|68)',s):e.append('unfilled table')
    for link in re.findall(r'!?\[\[([^\]]+)\]\]',s):
        target=link.split('|')[0].split('#')[0]
        if not (ROOT/target).exists() and not (ROOT/(target+'.md')).exists():e.append('unresolved '+target)
    # Every standalone display delimiter is itself on a separate callout line.
    in_math=False
    for line in s.splitlines():
        if '$$' in line:
            if line.strip() not in ['> $$','$$']:e.append('display delimiter inline');break
            in_math=not in_math
    if in_math:e.append('unclosed display')
    allparts+=len(row['subparts']);checks.append({'exercise':row['source_exercise'],'id':row['local_id'],'passed':not e,'issues':e})
    errors.extend(row['source_exercise']+': '+z for z in e)
report={'chapter':5,'questions':len(rows),'lettered_subparts':allparts,'ordered_sets_match':not any('set' in e for e in errors),'source_pages_visually_checked':list(range(239,250)),'referenced_body_pages_visually_checked':[114,207,211,218,219,221,222,223,225,226,228,231,233,234,235,236,237,238],'figures':{'PGFPlots_sources':4,'compiled':4,'rendered_and_visually_checked':4,'obsidian_rendering_checked':False},'simulations':{'5.53':'3 x 1000','5.54':'15 models x 50000','5.58':'1000000','5.66':'200000','5.68':'3 degrees x 3 methods x 100 retained; MH burnin5000'},'errors':errors,'checks':checks}
(ROOT/'工具/StatisticalInference/核验记录/ch05-current-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='checks'},ensure_ascii=False,indent=2))
sys.exit(bool(errors))
