from pathlib import Path
import json,re,sys,yaml

ROOT=Path.cwd()
rows=json.loads((ROOT/'工具/StatisticalInference/source-manifest.json').read_text(encoding='utf-8'))['chapters']['10']['exercises']
old=json.loads((ROOT/'附件/翻译/Statistical Inference_Chn/work/ch10-manifest.json').read_text(encoding='utf-8'))
expected={x['number']:x['parts'] for x in old['exercise_letter_parts']}
romans={k.rsplit('.',1)[0]:v for k,v in old['exercise_nested_roman_parts'].items()}
errors=[];checks=[];links=0;letter_count=roman_count=0
if [r['source_exercise'] for r in rows]!=[f'10.{n}' for n in range(1,49)]:errors.append('ordered source question set')
if [r['local_id'] for r in rows]!=[f'ST{n:03d}' for n in range(307,355)]:errors.append('ordered local ID set')
if len({r['note'] for r in rows})!=48:errors.append('unique note paths')

def text_macro_math(s):
    issues=[]
    for m in re.finditer(r'\\(?:text|mbox)\{',s):
        depth=1;i=m.end();begin=i
        while i<len(s) and depth:
            if s[i]=='{' and (i==0 or s[i-1]!='\\'):depth+=1
            if s[i]=='}' and (i==0 or s[i-1]!='\\'):depth-=1
            i+=1
        if '$' in s[begin:i-1]:issues.append('nested dollar in text macro')
    return issues

for row in rows:
    p=ROOT/row['note'];s=p.read_text(encoding='utf-8');meta=yaml.safe_load(s.split('---',2)[1]);q=row['source_exercise'];e=[]
    needed=['title','topic','topic_label','difficulty','status','tags','source','source_id','source_chapter','source_exercise','source_stars','source_refs','source_status','solution_status','created']
    e.extend('metadata missing '+k for k in needed if k not in meta)
    for k,v in {'topic':'mathematical-statistics','topic_label':'数理统计','status':'not-started','source_id':'DS011','source_chapter':10,'source_exercise':q,'source_stars':0,'source_status':'verified','solution_status':'independently-derived','created':'2026-11-13'}.items():
        if str(meta.get(k))!=str(v):e.append('metadata value '+k)
    if meta.get('difficulty') not in ['beginner','intermediate','advanced']:e.append('difficulty enum')
    if 'exercise' not in meta.get('tags',[]):e.append('exercise tag')
    if '[[' in meta.get('source','') or '](' in meta.get('source',''):e.append('linked source property')
    if row['subparts']!=expected[q]:e.append('mapped letter parts')
    if row['nested_roman_subparts']!=romans.get(q,[]):e.append('mapped roman parts')
    eng=s.split('### 英文原题',1)[1].split('### 中文转述',1)[0]
    cn=s.split('### 中文转述',1)[1].split('## 提示',1)[0]
    for label,part in [('english',eng),('chinese',cn)]:
        parts=re.findall(r'^> (?:\*\*[^*]+\*\* )?\(([a-h])\)',part,re.M)
        if parts!=expected[q]:e.append(label+' letter parts '+str(parts))
        rs=re.findall(r'^> \((i|ii|iii|iv)\)',part,re.M)
        if rs!=romans.get(q,[]):e.append(label+' roman parts '+str(rs))
    if s.count('> [!success]- 解答')!=1:e.append('unique exact solution callout')
    if s.count('> [!question]')!=2:e.append('two bilingual question callouts')
    if '> [!hint]- 提示' not in s:e.append('folded hint')
    if len(re.findall(r'(?<!\\)\$',s))%2:e.append('dollar parity')
    if re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',s):e.append('control characters')
    if re.search(r'\\(?:begin\{enumerate\}|item|autoref|hyperref|sourcepageanchor|CJKfontspec|needspace|semanticindexanchor)',s):e.append('unconverted TeX source markup')
    if re.search(r'TABLE\d+|NUMERIC\d+|原图见英文原题|将按.*实读|TODO|TBD',s):e.append('unfilled placeholder')
    e.extend(text_macro_math(s))
    in_math=False
    for line in s.splitlines():
        if '$$' in line:
            if line.strip() not in ['> $$','$$']:e.append('standalone display delimiter');break
            in_math=not in_math
    if in_math:e.append('unclosed display math')
    # Count nonescaped braces after omitting escaped literal braces.
    mathtext=re.sub(r'\\[{}]','',s)
    if mathtext.count('{')!=mathtext.count('}'):e.append('brace balance')
    begins=re.findall(r'\\begin\{([^}]+)\}',s);ends=re.findall(r'\\end\{([^}]+)\}',s)
    if sorted(begins)!=sorted(ends):e.append('environment balance')
    for link in re.findall(r'!?\[\[([^\]]+)\]\]',s):
        links+=1;target=link.split('|')[0].split('#')[0]
        if not (ROOT/target).exists() and not (ROOT/(target+'.md')).exists():e.append('unresolved link '+target)
    for section in ['## 题目','## 提示','## 解答','## 相关概念','## 备注']:
        if s.count(section)!=1:e.append('section '+section)
    if not all(a==b-31 for a,b in zip(row['printed_pages'],row['pdf_pages'])):e.append('printed/PDF offset')
    if not (439<=min(row['pdf_pages'])<=max(row['pdf_pages'])<=447):e.append('source exercise pages')
    letter_count+=len(row['subparts']);roman_count+=len(row['nested_roman_subparts'])
    checks.append({'exercise':q,'id':row['local_id'],'passed':not e,'issues':e})
    errors.extend(q+': '+z for z in e)

figs=['习题10.11-Gamma效率比较','习题10.14-自助分布比较','习题10.17-相关自助分布','习题10.34-伯努利LRT分布','习题10.44-二项区间比较']
for f in figs:
    for suffix in ['.tex','.pdf','.png']:
        p=ROOT/'附件/习题图/DS011'/(f+suffix)
        if not p.exists() or p.stat().st_size==0:errors.append('missing figure '+str(p))
    log=(ROOT/'附件/习题图/DS011'/(f+'.log')).read_text(encoding='utf-8',errors='replace')
    if re.search('^!|Warning|Missing character',log,re.M):errors.append('figure compilation warning '+f)

report={'chapter':10,'questions':len(rows),'lettered_subparts':letter_count,'nested_roman_subparts':roman_count,'ordered_sets_match':not any('set' in e for e in errors),'resolved_wikilink_occurrences':links,'source_pages_visually_checked':list(range(439,449)),'referenced_body_pages_visually_checked':[114,229,230,234,235,374,399,406,*range(410,439),449,450],'figures':{'PGFPlots_sources':5,'compiled':5,'rendered_and_visually_checked':5,'obsidian_rendering_checked':False},'computations':{'10.13':'all 256 ordered samples and 35 count vectors; 31 distinct means','10.14':'20,000 each model and bootstrap method; original samples and raw resamples retained','10.16':'1,000,000 binomial samples plus exact 25-term variance','10.17':'two explicitly distinguished data interpretations; each 1,000 nonparametric and 1,000 parametric correlations','10.30':'quadrature for 3 score functions x 2 populations x 5 tuning constants','10.34':'4 models x 10,000 LRT statistics','10.39/10.46':'4 populations x 3,000 samples of size15; 199 bootstrap resamples each; actual errors/powers/coverage retained','10.44':'exact finite binomial sums for n12/25/100, levels.9/.95, p=.001:.001:.999','10.45':'n1 exact counterexample, plus endpoint search n1..150 at alpha.1/.05/.01; finite search not a theorem'},'deterministic_record_checks':'work/DS011/ch10/verification.json; Gamma known-mean MLE score, all35 weighted multisets, Bernoulli variance formula over25 finite models, exact n1 coverage counterexample, reaggregation of all12000 robust-simulation records','independent_parent_review':{'10.30/ST336':'Parent independently read complete note and original PDF444/447; zero-tail 0/0, arbitrarily distant roots and conditional remote-cluster threshold scope confirmed','10.45/ST351':'Parent independently read complete note, original447 and body436; corrected Wilson lower endpoint0.05462075552885 and coverage0.9454 at p0.0546 confirmed'},'material_source_issues':['10.5 reciprocal normal moments','10.7 differentiability missing for efficient transforms','10.8 theorem reference and information sign','10.11 ARE direction and known-mean MOM/MLE distinction','10.13/10.15 exhaustive n^n-1 denominator discrepancy','10.16 printed variance .00529 not reproduced','10.17 original 5.58 and 580.3.07 entries','10.19 negative AR sign and stationary initialization','10.24/10.26 location derivative sign','10.25 symmetry insufficient for normality','10.27 missing contamination-atom median branch','10.29 Logistic score needs x/2','10.30 zero tail limits give 0/0 and require a root-selection rule','10.33 wrong observed-information scaling','10.39/10.46 printed10.3.8 denominator','10.45 corrected score does not universally guarantee nominal coverage'],'errors':errors,'checks':checks}
(ROOT/'工具/StatisticalInference/核验记录/ch10-current-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='checks'},ensure_ascii=False,indent=2))
sys.exit(bool(errors))
