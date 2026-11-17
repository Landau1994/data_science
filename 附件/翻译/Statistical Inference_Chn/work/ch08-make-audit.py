from pathlib import Path
import collections, hashlib, json, re, sys

root=Path.cwd()
sys.path.insert(0,str(root/'work/python-deps'))
import pymupdf as fitz

files=[]
def expand(rel):
    path=root/rel; files.append(rel)
    s=path.read_text(encoding='utf-8-sig')
    return re.sub(r'\\input\{([^}]+)\}',lambda m:expand(m[1]),s)
s=expand('chapters-tex/08.tex')
all_source='\n'.join((root/f'work/ch08-source/p{n}.txt').read_text(encoding='utf-8-sig') for n in range(333,368))
pages=[int(n) for n in re.findall(r'\\sourcepageanchor\{(\d+)\}',s)]
assert pages==list(range(333,368)), pages
labels=re.findall(r'\\label\{([^}]+)\}',s)
assert len(labels)==len(set(labels))
refs=set(re.findall(r'\\(?:auto|eq)?ref\{([^}]+)\}',s))|set(re.findall(r'\\hyperref\[([^\]]+)\]',s))
all_labels=set()
for rel in ['sections-tex','chapters-tex']:
    for path in (root/rel).glob('*.tex'):
        all_labels.update(re.findall(r'\\label\{([^}]+)\}',path.read_text(encoding='utf-8-sig')))
missing=sorted(refs-all_labels)
assert not missing, missing
events=[]
for m in re.finditer(r'\\begin\{(definition|theorem|corollary|lemma|example)\}(?:\[[^\n]*?\])?\s*\\label\{([^}]+)\}',s):
    prev=re.findall(r'\\sourcepageanchor\{(\d+)\}',s[:m.start()])
    events.append({'type':m[1],'label':m[2],'source_physical_page':int(prev[-1])})
source_types=['definition']*3+['definition','example','example','theorem','example','example','example','example','example']+['definition','example','example','example','definition','definition','example','example','definition','example','definition','theorem','corollary','example','example','definition','theorem','example','example','example','theorem','example','theorem','theorem','example','definition','theorem','example','example','example','example']
source_obj_pages=[333]*3+[334,335,335,336,337,337,338,339,340]+[341,341,342,343,343,343,344,344,345,345,345,346,347,347,348,348,348,349,349,350,351,351,351,352,352,353,353,353,354,354,356]
assert len(events)==43
assert [x['type'] for x in events]==source_types
assert [x['source_physical_page'] for x in events]==source_obj_pages
source_obj_nums=[f'8.1.{i}' for i in range(1,4)]+[f'8.2.{i}' for i in range(1,10)]+[f'8.3.{i}' for i in range(1,32)]
assert [x['label'].split(':')[1] for x in events]==source_obj_nums
proofs=re.findall(r'\\begin\{proof\}',s)
assert len(proofs)==8
source_proofs=['thm:8.2.4','thm:8.3.12','cor:8.3.13','thm:8.3.17','thm:8.3.21','thm:8.3.23','thm:8.3.24','thm:8.3.27']
source_counts=[0,0,0,0,3,3,2,2,2,2,2,2,4,0,0,2,3,2,0,0,0,3,3,0,3,2,0,3,3,2,2,2,4,2,3,2,3,2,2,2,3,4,0,0,0,3,4,0,3,3,0,2,4,4,3,0,0,0]
source_ex_pages=[357]*5+[358]*6+[359]*8+[360]*9+[361]*7+[362]*5+[363]*2+[364]*4+[365]*7+[366]*5
ex=[]
for idx,m in enumerate(re.finditer(r'\\begin\{exercise\}\\label\{exercise:8\.(\d+)\}(.*?)\\end\{exercise\}',s,re.S)):
    n=int(m[1]);assert n==idx+1
    depth=0;alpha=0;roman=0
    for token in re.finditer(r'\\begin\{enumerate\}(?:\[[^\]]*\])?|\\end\{enumerate\}|\\item\b',m[2]):
        if token[0].startswith('\\begin'):depth+=1
        elif token[0].startswith('\\end'):depth-=1
        elif depth==1:alpha+=1
        elif depth==2:roman+=1
    assert alpha==source_counts[idx],(n,alpha,source_counts[idx])
    assert roman==(2 if n==53 else 0),(n,roman)
    p=[source_ex_pages[idx]]
    if n in [5,40,42,53]:p.append(p[0]+1)
    ex.append({'label':f'exercise:8.{n}','source_physical_pages':p,'lettered_parts':[chr(97+i) for i in range(alpha)],'roman_parts':{'d':['i','ii']} if roman else {}})
assert len(ex)==58
eq_labels=re.findall(r'\\label\{(eq:8\.[^}]+)\}',s)
assert eq_labels==[f'eq:8.2.{i}' for i in range(1,7)]+[f'eq:8.3.{i}' for i in range(1,15)]
assert len(re.findall(r'\\begin\{equation\}',s))==20
def groups(s,cmd):
    for m in re.finditer(re.escape(cmd)+'{',s):
        i=m.end();start=i;depth=1
        while depth:
            if s[i]=='{' and s[i-1]!='\\':depth+=1
            elif s[i]=='}' and s[i-1]!='\\':depth-=1
            i+=1
        yield m.start(),s[start:i-1]
notes=[]
for i,(pos,txt) in enumerate(groups(s,r'\footnote'),1):
    prevobj=[x for x in re.finditer(r'\\label\{((?:def|thm|ex|exercise|sec):[^}]+)\}',s[:pos])]
    pp=re.findall(r'\\sourcepageanchor\{(\d+)\}',s[:pos])
    notes.append({'ordinal':i,'type':'translator' if txt.startswith('译注：') else 'source','nearest_preceding_label':prevobj[-1][1] if prevobj else None,'source_physical_page_nearby':int(pp[-1]),'text_tex':txt})
assert len(notes)==23 and all(x['type']=='translator' for x in notes)
baseline=json.loads((root/'work/source-baseline.json').read_text(encoding='utf-8-sig'))
src=fitz.open(baseline['path'])
numbered_source=[]
for n in range(333,368):
    for line in src[n-1].get_text('dict')['blocks']:
        if 'lines' not in line:continue
        for ln in line['lines']:
            tx=''.join(sp['text'] for sp in ln['spans']).strip()
            if re.fullmatch(r'\(8\.[23]\.\d+\)',tx) and ln['bbox'][0]>400:
                numbered_source.append({'label':'eq:'+tx[1:-1],'source_physical_page':n})
assert [x['label'] for x in numbered_source]==eq_labels,numbered_source
pdf=fitz.open(root/'work/ch08-preview.pdf')
render=root/'work/ch08-render';render.mkdir(exist_ok=True)
punct=[]
for i,p in enumerate(pdf,1):
    p.get_pixmap(matrix=fitz.Matrix(1.45,1.45),alpha=False).save(render/f'p{i:03}.png')
    for block in p.get_text('dict')['blocks']:
        for line in block.get('lines',[]):
            tx=''.join(x['text'] for x in line['spans']).strip()
            if tx.startswith(('.',',',';',':','，','。','；','：')):punct.append({'page':i,'text':tx,'bbox':list(line['bbox'])})
log=(root/'work/ch08-preview.log').read_text(encoding='utf-8',errors='replace')
manifest={
 'chapter':8,'title_zh':'假设检验','source_sha256':baseline['sha256'],
 'source_physical_pages':list(range(333,368)),'source_printed_pages':[302,336],
 'authorship_and_review':{'translation':'root supplied full draft 08-00 through 08-05 before handoff','source_first_hand_review':'root: source333-367','independent_review':'source_inventory: source333-367 all 35 images and full text/formula comparison; additional cross-reference source213-216'},
 'files_in_input_order':files,'source_page_anchors':pages,
 'shared_objects':events,'shared_object_counts':dict(collections.Counter(x['type'] for x in events)),
 'proofs':source_proofs,'numbered_equations':numbered_source,
 'figures':json.loads((root/'work/ch08-figure-crops.json').read_text(encoding='utf-8-sig')),
 'numbered_tables':['tab:8.3.1'],'unnumbered_exercise_tables':['exercise:8.20','exercise:8.41'],
 'exercises':ex,'lettered_subpart_count':sum(source_counts),'roman_subpart_count':2,
 'footnotes':notes,'source_footnote_count':0,'translator_footnote_count':23,
 'label_count':len(labels),'duplicate_labels':[],'missing_reference_targets':missing,
 'local_preview':{'path':'work/ch08-preview.pdf','page_count':len(pdf),'sha256':hashlib.sha256((root/'work/ch08-preview.pdf').read_bytes()).hexdigest(),'overfull_hbox_count':log.count('Overfull \\hbox'),'overfull_vbox_count':log.count('Overfull \\vbox'),'missing_glyph_count':log.count('Missing character:'),'foreign_reference_warning_targets':sorted(set(re.findall(r'Reference `([^\']+)\'[^\n]*undefined',log))),'line_initial_punctuation_candidates':punct,'visual_reviewed_pages':[]},
 'independent_review_fixes':['ex8.2.9 literal quad fixed to \\quad','exercise8.35(b): restored source instruction Show that as 证明','exercise8.9(b): long statistic displayed to remove overfull box','exercise8.46 translator note: explicit k>0 for nontrivial claim; k<=0 separated','exercise8.42(d): source erroneous Example5.4.1 retained visually, link to actual variance-ratio example5.3.5 and translator explanation'],
 'deferred_to_root':['bibliography linking','semantic index anchors','complete-book compilation and cross-chapter navigation','final public PDF validation'],
 'unresolved_content_findings':[]
}
(root/'work/ch08-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'objects':len(events),'types':manifest['shared_object_counts'],'equations':len(eq_labels),'proofs':len(proofs),'exercises':len(ex),'letters':sum(source_counts),'roman':2,'notes':len(notes),'anchors':len(pages),'preview_pages':len(pdf),'overfull_hbox':manifest['local_preview']['overfull_hbox_count'],'line_initial_punctuation':punct,'foreign_ref_warnings':manifest['local_preview']['foreign_reference_warning_targets']},ensure_ascii=False))
