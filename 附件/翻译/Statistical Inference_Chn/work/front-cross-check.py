from pathlib import Path
import re, json, subprocess
base=Path(__file__).resolve().parent.parent
pdf=next((base.parents[1]/'books').glob('George Casella*.pdf'))
report={}
for name,start,end in [('contents',8,11),('tables',20,20),('figures',22,23)]:
    src=subprocess.check_output(['pdftotext','-f',str(start),'-l',str(end),'-layout',str(pdf),'-']).decode('utf-8')
    expected=re.findall(r'^\s*(\d+(?:\.\d+)*)\s+\S.*?\s+(\d+)\s*$',src,re.M)
    tex=(base/f'frontmatter/00-{name}.tex').read_text(encoding='utf-8')
    actual=[]
    bad=[]
    for line in tex.splitlines():
        m=re.match(r'\\sourcepageref\{(\d+)\}\{(\d+(?:\.\d+)*)\s+',line)
        if m:
            z=re.search(r'& \\sourcepageref\{(\d+)\}\{(\d+)\}',line)
            assert z,line
            actual.append((m[2],z[2]))
            if int(m[1])!=int(z[2])+31 or int(z[1])!=int(z[2])+31:bad.append(line)
    report[name]={'expected_numbered_entries':len(expected),'actual_numbered_entries':len(actual),
                  'number_order_page_match':expected==actual,'bad_page_mappings':bad}
    assert expected==actual,(name,expected,actual)
    assert not bad
(base/'work/front-cross-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
