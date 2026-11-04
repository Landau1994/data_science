"""核对整合预览的真实输入、静态结构、已译章编号与原件哈希；不是全书完成判据。"""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re
from pypdf import PdfReader

root = Path(__file__).resolve().parent.parent
work = root / 'work'
seen, order, failures = set(), [], []

def clean(text):
    return re.sub(r'(?m)(?<!\\)%.*$', '', text)

def walk(path):
    if path in seen:
        failures.append('重复输入：' + str(path.relative_to(root)))
        return
    seen.add(path)
    content = clean(path.read_text(encoding='utf-8'))
    cursor = 0
    for match in re.finditer(r'\\input\{([^}]+)\}', content):
        order.append(content[cursor:match.start()])
        child = root / (match.group(1) + ('' if match.group(1).endswith('.tex') else '.tex'))
        if not child.exists():
            failures.append('缺少输入：' + str(child))
        else:
            walk(child)
        cursor = match.end()
    order.append(content[cursor:])
    stack = []
    for token in re.finditer(r'\\(begin|end)\{([^}]+)\}', content):
        kind, name = token.groups()
        if kind == 'begin':
            stack.append(name)
        elif not stack or stack.pop() != name:
            failures.append('环境不匹配：' + str(path.relative_to(root)))
    if stack:
        failures.append('环境未闭合：' + str(path.relative_to(root)))
    if len(re.findall(r'(?<!\\)\$', content)) % 2:
        failures.append('美元定界符奇数：' + str(path.relative_to(root)))
    if len(re.findall(r'(?<!\\)\\\[', content)) != len(re.findall(r'(?<!\\)\\\]', content)):
        failures.append('展示定界符不匹配：' + str(path.relative_to(root)))

walk(work / 'progress-preview.tex')
joined = '\n'.join(order)
labels = [key for key in re.findall(r'\\label\{([^}]+)\}', joined) if '#' not in key]
hint_ids = re.findall(r'\\begin\{sourcehint\}\{(\d+)\}', joined)
labels += ['hint:' + value for value in hint_ids]
duplicates = [key for key, value in Counter(labels).items() if value > 1]
failures += ['重复标签：' + key for key in duplicates]
bibkeys = set(re.findall(r'@\w+\{([^,]+),', (root / 'bib/references.bib').read_text(encoding='utf-8')))
cites = {key.strip() for match in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}', joined) for key in match.split(',')}
failures += ['缺少文献：' + key for key in cites - bibkeys]
refs = set(re.findall(r'\\(?:auto|eq|page)?ref\{([^}]+)\}|\\hyperref\[([^]]+)\]', joined))
refkeys = {left or right for left, right in refs if '#' not in (left or right)}
unresolved = sorted(refkeys - set(labels))
unexpected_unresolved = unresolved
failures += ['非预期的缺失引用：' + key for key in unexpected_unresolved]
aux = (work / 'progress-preview.aux').read_text(encoding='utf-8')
numbers = dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}', aux))
expected = {1: (54,8,14,0), 2: (26,8,4,5), 3: (28,8,3,5), 4: (46,35,6,7),
            5: (36,7,2,4), 6: (5,4,8,5), 7: (32,4,3,1), 8: (11,28,3,0)}
for chapter, counts in expected.items():
    for prefix, total in zip(['obj', 'eq', 'box', 'fig'], counts):
        for number in range(1, total + 1):
            key = f'{prefix}:{chapter}.{number}'
            if numbers.get(key) != f'{chapter}.{number}':
                failures.append('编号不符：' + key + '=' + str(numbers.get(key)))
source = root.parent.parent / 'books/Santambrogio 2015 Optiomal Transport For Applied Mathematicians.pdf'
digest = hashlib.sha256(source.read_bytes()).hexdigest()
if digest != '7820e876d4312d7355f0a1549b2af2186594eebef8d411d651c6235b8c119b68':
    failures.append('原件哈希不符')
pdf = PdfReader(work / 'progress-preview.pdf')
for number in range(1, 70):
    if numbers.get(f'ex:{number}') != str(number):
        failures.append('习题编号不符：' + str(number))
    if f'hint:{number}' not in numbers:
        failures.append('缺少提示：' + str(number))
report = {'scope': '已译1–8章、69题及69条提示整合预览；前置及索引未包含',
          'input_files': len(seen), 'labels': len(labels), 'unique_cites': len(cites),
          'bib_keys': len(bibkeys), 'pdf_pages': len(pdf.pages), 'source_sha256': digest,
          'expected_pending_refs': unresolved, 'failures': failures,
          'limitations': '不是来源忠实性、全页视觉、最终PDF链接或全书完成证明。'}
(work / 'progress-audit.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({key: value for key, value in report.items() if key != 'expected_pending_refs'}, ensure_ascii=False, indent=2))
raise SystemExit(bool(failures))
