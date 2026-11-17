from pathlib import Path
import sys,json,re,hashlib
from collections import Counter
from urllib.parse import unquote
B=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(B/'work/python-deps'))
import pymupdf as fitz
pdf=B/'work/Statistical Inference_Chn.pdf';d=fitz.open(pdf)
render=B/'work/render-output';render.mkdir(exist_ok=True)
result={'pages':len(d),'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'internal_links':0,'remote_links':0,'web_links':0,'bad_links':[],'rendered':[],'source_page_targets':[],'suspicious_line_starts':[]}
for i,p in enumerate(d):
    pix=p.get_pixmap(dpi=110);pix.save(render/f'page-{i+1:03}.png')
    result['rendered'].append({'page':i+1,'sha256':hashlib.sha256(pix.samples).hexdigest()})
    for l in p.get_links():
        if l['kind']==fitz.LINK_GOTO or (l['kind']==fitz.LINK_NAMED and 'page' in l):
            result['internal_links']+=1
            if not 0<=l.get('page',-1)<len(d):result['bad_links'].append({'page':i+1,'link':str(l)})
        elif l['kind']==fitz.LINK_GOTOR:
            result['remote_links']+=1;result['source_page_targets'].append(l.get('page',-1)+1)
            if not 0<=l.get('page',-1)<566:result['bad_links'].append({'page':i+1,'link':str(l)})
            if Path(unquote(l.get('file',''))).name != Path(json.loads((B/'work/source-baseline.json').read_text(encoding='utf-8'))['path']).name:
                result['bad_links'].append({'page':i+1,'file':l.get('file')})
        else:result['web_links']+=1
    for b in p.get_text('dict')['blocks']:
        for line in b.get('lines',[]):
            s=''.join(x['text'] for x in line['spans']).strip()
            if s.startswith(('.',',','，','；',')')):result['suspicious_line_starts'].append({'page':i+1,'text':s[:100],'bbox':line['bbox']})
aux=(B/'work/Statistical Inference_Chn.aux').read_text(encoding='utf-8')
result['numbering_errors']=[]
for typ,num,printed in re.findall(r'\\newlabel\{(def|thm|ex|eq|fig|tab|exercise):(\d+(?:\.\d+)+)\}\{\{([^}]+)\}',aux):
    if num!=printed:result['numbering_errors'].append([typ,num,printed])
result['label_number_checks']=len(re.findall(r'\\newlabel\{(?:def|thm|ex|eq|fig|tab|exercise):',aux))
result['bookmarks']=d.get_toc()
baseline=json.loads((B/'work/source-baseline.json').read_text(encoding='utf-8'))
src=fitz.open(baseline['path'])
result['source_links_scope']={'front':sum(len(src[i].get_links()) for i in range(31)),'chapter1':sum(len(src[i].get_links()) for i in range(31,68))}
(B/'work/pdf-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['rendered','source_page_targets','suspicious_line_starts','bookmarks']},ensure_ascii=False))
