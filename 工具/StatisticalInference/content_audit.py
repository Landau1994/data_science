"""只读补充校验：数学定界符、花括号、环境与新习题占位文字。"""
from pathlib import Path
import json,re,sys
from collections import Counter

ROOT=Path(__file__).resolve().parents[2]
MANIFEST=Path(__file__).with_name('source-manifest.json')

def audit():
 m=json.loads(MANIFEST.read_text(encoding='utf-8'));errors=[];warnings=[];checked=0;ids=[]
 for ch,data in m['chapters'].items():
  for row in data['exercises']:
   p=ROOT/row['note'];ids.append(row['local_id'])
   if not p.exists(): errors.append([row['note'],'文件缺失']);continue
   raw=p.read_text(encoding='utf-8-sig');body=raw.split('---',2)[-1];checked+=1
   if any(ord(c)<32 and c not in '\n\r\t' for c in body):errors.append([row['note'],'含意外控制字符'])
   if body.count('> [!success]- 解答')!=1:errors.append([row['note'],'解答callout数量不是1'])
   if re.search(r'<%|TODO|待补充解答|此处填写',body):errors.append([row['note'],'疑似模板占位'])
   for residual in re.finditer(r'\\(?:item(?![A-Za-z])|(?:begin|end)\{enumerate\}|(?:label|autoref|eqref)\{|hyperref\[|sourcepageanchor)',body):
    errors.append([row['note'],'残余正文TeX命令',residual.group()])
   dollars=list(re.finditer(r'(?<!\\)(?:\$\$|\$)',body));current=None;start=0
   for token in dollars:
    if current is None:current=token.group();start=token.end();continue
    if current!=token.group():errors.append([row['note'],'行内与展示公式定界符交叉']);break
    formula=body[start:token.start()]
    if '\t' in formula:errors.append([row['note'],'数学公式中含制表控制字符'])
    if current=='$' and '\n' in formula:warnings.append([row['note'],'跨行的单美元公式',formula[:100]])
    braces=0
    for brace in re.finditer(r'(?<!\\)[{}]',formula):
     braces+=1 if brace.group()=='{' else -1
     if braces<0:break
    if braces:errors.append([row['note'],'数学花括号不平衡',formula[:90]])
    stack=[]
    for env in re.finditer(r'\\(begin|end)\{([^}]+)\}',formula):
     if env[1]=='begin':stack.append(env[2])
     elif not stack or stack.pop()!=env[2]:errors.append([row['note'],'数学环境嵌套不匹配',env[2]])
    if stack:errors.append([row['note'],'数学环境未闭合',stack])
    current=None
   if current is not None:errors.append([row['note'],'数学定界符未闭合'])
 duplicate_ids=[k for k,v in Counter(ids).items() if v>1]
 if duplicate_ids:errors.append(['全书','重复本库编号',duplicate_ids])
 return {'source_id':m['source_id'],'checked_notes':checked,'errors':errors,'warnings':warnings,
  'scope':'只检语法结构，不代替原页逐字核对或数学证明审查；未运行Obsidian'}

if __name__=='__main__':
 result=audit();print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(bool(result['errors']))
