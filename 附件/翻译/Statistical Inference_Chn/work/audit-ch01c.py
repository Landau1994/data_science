from pathlib import Path
import re, json
base = Path(__file__).resolve().parent.parent
paths = [base/'sections-tex/01-07.tex', base/'sections-tex/01-08.tex', base/'frontmatter/00-example-list.tex']
for p in paths:
    t = p.read_text(encoding='utf-8').replace('。','.')
    p.write_text(t, encoding='utf-8')
t = paths[0].read_text(encoding='utf-8')
ids = re.findall(r'\\label\{exercise:(1\.\d+)\}', t)
assert ids == ['1.'+str(i) for i in range(1,56)]
report = {}
for p in paths:
    s=p.read_text(encoding='utf-8')
    envs = re.findall(r'\\(begin|end)\{([^}]+)\}',s)
    stack=[]
    for kind,env in envs:
        if kind=='begin':stack.append(env)
        else: assert stack.pop()==env,(p,env)
    assert not stack
    assert s.count('$$')%2==0
    assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',s)
    report[p.name] = {
      'exercises':len(re.findall(r'\\begin\{exercise\}',s)),
      'lettered_parts':len(re.findall(r'\\item\[\([a-z]\)\]',s)),
      'roman_rules':len(re.findall(r'\\item\[i+\.\]',s)),
      'numbered_equations':len(re.findall(r'\\begin\{(?:equation|align)\}',s)),
      'unnumbered_displays':s.count('$$')//2,
      'tables':s.count(r'\begin{tabular}'),
      'figures':s.count(r'\includegraphics'),
      'external_page_references':len(re.findall(r'\\sourcepageref\{',s)),
      'labels':re.findall(r'\\label\{([^}]+)\}',s),
    }
report['exercise_ids']=ids
(base/'work/ch01c-static.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({name:{k:v for k,v in values.items() if k!='labels'} for name,values in report.items() if name!='exercise_ids'},ensure_ascii=False))
