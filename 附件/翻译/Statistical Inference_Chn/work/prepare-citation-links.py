from pathlib import Path
import re,json
B=Path(__file__).resolve().parents[1]
refs=json.loads((B/'work/references-all.json').read_text(encoding='utf-8'))
aliases=[];bad=[]
for r in refs:
 m=re.match(r'(.+?)\(((?:18|19|20)\d{2}[^)]*)\)',r['text'])
 if not m:bad.append(r);continue
 author=m[1]
 # Remove given-name initials and editor annotation; no bibliographic values are inferred.
 author=re.sub(r'\(eds?\.\)','',author)
 author=re.sub(r'\b[A-Z](?:\s*-\s*[A-Z])?\s*\.\s*','',author)
 author=re.sub(r'\bN(?=\s*(?:,|and))','',author)
 names=[n.strip(' ,.;') for n in re.split(r'\s+and\s+|,',author) if n.strip(' ,.;')]
 names=[n for n in names if len(n)>1 and not n.startswith('(ed')]
 years=re.findall(r'(?:18|19|20)\d{2}[a-z]?',m[2])
 aliases.append({'number':r['number'],'names':names,'years':years,'author_raw':m[1]})
(B/'work/bibliography-author-keys.json').write_text(json.dumps(aliases,ensure_ascii=False,indent=2),encoding='utf-8')
(B/'work/bibliography-unparsed.json').write_text(json.dumps(bad,ensure_ascii=False,indent=2),encoding='utf-8')
print('parsed',len(aliases),'unparsed',[(r['number'],r['text'][:40])for r in bad])
print('\n'.join(str(a) for a in aliases if any(len(n)>30 or '.'in n for n in a['names'])))
