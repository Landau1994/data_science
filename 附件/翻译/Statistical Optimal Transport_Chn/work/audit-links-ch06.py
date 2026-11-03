import sys,json,re,collections,difflib
sys.path.insert(0,r'E:/project/math/ant/tmp/pypackages')
import pymupdf as f
from pathlib import Path
b=Path(__file__).resolve().parent.parent
for key,path,first,last in [('source',b.parent.parent/'books'/'Statistical Optimal Transport.pdf',163,198),('target',b/'work/full-build/Statistical Optimal Transport_Chn.pdf',135,160)]:
    d=f.open(path)
    print(str(path),d.page_count)
    ls=[]
    for pn in range(first,last+1):
        for l in d[pn-1].get_links():
            txt=d[pn-1].get_textbox(l['from'])
            ls.append(dict(page=pn,text=txt,link=l,obj=d.xref_object(l['xref'])))
    (b/f'work/ch06-links-{key}.json').write_text(json.dumps(ls,ensure_ascii=False,default=str,indent=2),encoding='utf8')
    print('total',len(ls),'internal',sum(x['link']['kind']!=2 for x in ls))

s=json.loads((b/'work/ch06-links-source.json').read_text(encoding='utf8'))
t=json.loads((b/'work/ch06-links-target.json').read_text(encoding='utf8'))
theorem_map={'5.11':'example.5.11','5.12':'example.5.12','5.13':'example.5.13','5.14':'definition.5.14','5.20':'corollary.5.20','5.21':'theorem.5.21','5.22':'theorem.5.22','6.1':'theorem.6.1','6.2':'lemma.6.2','6.3':'theorem.6.3','6.4':'corollary.6.4','6.6':'corollary.6.6','6.9':'lemma.6.9','6.11':'theorem.6.11','6.13':'corollary.6.13','6.14':'corollary.6.14','6.16':'proposition.6.16','1.14':'theorem.1.14','1.18':'proposition.1.18','4.2':'proposition.4.2'}
item_map={'Item.5.47':'exercise.5.2','Item.5.49':'exercise.5.4','Item.5.50':'exercise.5.5','Item.5.57':'exercise.5.11','Item.6.70':'exercise.6.2','Item.6.72':'exercise.6.4','Item.6.74':'exercise.6.6'}
def norm(x,source=False):
    name=x['link'].get('nameddest','')
    if not source:return name
    if name.startswith('cite.'):
        nums=re.findall(r'\d+',x['text'])
        assert len(nums)==1,(name,x['text'])
        return 'cite.ref'+nums[0]
    if name.startswith('equation.'):
        a=name.split('.');return 'equation.'+a[1]+'.'+a[-1]
    if name.startswith('chapter.'):
        return 'section.'+name.split('.')[-1]
    if name.startswith('section.'):
        a=name.split('.');return 'subsection.'+a[-2]+'.'+a[-1]
    if name.startswith('subsection.'):
        a=name.split('.');return 'subsubsection.'+'.'.join(a[-3:])
    if name=='theorem.BM.1.2.11':return 'lemma.A.11'
    if name.startswith('theorem.'):
        a=name.split('.');return theorem_map[a[1]+'.'+a[-1]]
    if name.startswith('AMS6.'):
        return 'AMS.'+str(17+(int(name.split('.')[-1])-1)//2)
    if name.startswith('Hfootnote.6.'):
        return 'Hfootnote.'+str(int(name.split('.')[-1])+1)
    if name in item_map:return item_map[name]
    raise ValueError(name)
def key(x):
    nums=[float(v) for v in re.findall(r'-?\d+\.\d+',x['link']['from'])]
    return x['page'],round(nums[1],1),nums[0]
s=[x for x in s if x['link']['kind']!=2];t=[x for x in t if x['link']['kind']!=2]
s.sort(key=key);t.sort(key=key)
ss=[norm(x,True) for x in s];tt=[norm(x) for x in t]
sc=collections.Counter(ss);tc=collections.Counter(tt)
print('DEST DIFFERENCES')
for n in sorted(sc.keys()|tc.keys()):
    if sc[n]!=tc[n]: print(n,sc[n],tc[n])
print('SEQUENCE DIFFERENCES')
for tag,i,j,k,l in difflib.SequenceMatcher(None,ss,tt,autojunk=False).get_opcodes():
    if tag!='equal':
        print(tag,[(s[z]['page'],s[z]['link']['xref'],ss[z],s[z]['text'])for z in range(i,j)],[(t[z]['page'],t[z]['link']['xref'],tt[z],t[z]['text'])for z in range(k,l)])
rows=[]
for n in sorted(sc.keys()|tc.keys()):
    sx=[x for x in s if norm(x,True)==n];tx=[x for x in t if norm(x)==n]
    rows.append(dict(destination=n,source=[dict(page=x['page'],xref=x['link']['xref'],text=x['text'],dest=x['link']['nameddest'],rect=x['link']['from'])for x in sx],target=[dict(page=x['page'],xref=x['link']['xref'],text=x['text'],dest=x['link']['nameddest'],rect=x['link']['from'])for x in tx]))
(b/'work/ch06-link-mapping.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
