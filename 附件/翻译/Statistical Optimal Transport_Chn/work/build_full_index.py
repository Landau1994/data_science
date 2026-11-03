from pathlib import Path
import json, re, runpy, shutil
BASE=Path(__file__).resolve().parents[1]
TEMP=BASE/'work/full-temp'
TEMP.mkdir(exist_ok=True)
# Original index order and hierarchy; page lists are provenance only. All
# delivered page numbers are produced by makeindex at actual TeX occurrences.
# Columns: original term | Chinese display | source printed pages | file |
#          exact target label, or a literal semantic phrase to locate.
DATA=r'''
Alexandrov curvature|Alexandrov曲率|193|07-02|label:sec:7.2.1
Alexandrov space|Alexandrov空间|196|07-02|Alexandrov空间
Atjai–Komlós–Tusnády theorem|Atjai–Komlós–Tusnády定理|47|02-04|label:sec:2.4
attention|注意力|180|06-06|注意力
barycenter|重心|212|08-01|label:def:8.1
Benamou–Brenier formula|Benamou–Brenier公式|129|05-03|label:thm:5.7
Birkhoff polytope|Birkhoff多面体|6|01-01|Birkhoff
birth-death sampling|生灭抽样|172|06-03|label:sec:6.3.2
Brenier’s theorem|Brenier定理|15|01-04|label:thm:1.8
Brenier’s theorem!improved|Brenier定理!改进形式|27|01-05|label:thm:1.16
Burer–Monteiro|Burer–Monteiro|149|05-10|Burer
Bures–Wasserstein|Bures–Wasserstein|133|05-05|label:sec:5.5
Bures–Wasserstein!gradient|Bures–Wasserstein!梯度|134|05-05|label:thm:5.21
CAT(0)|CAT(0)|||see:NPC
chaining|链式法|44|02-03|链式法
change of variables|变量代换|153|06-01|label:lem:6.2
continuity equation|连续性方程|122|05-01|label:eq:5.2
convex duality|凸对偶|230|A-01|label:def:A.4
cyclical monotonicity|循环单调性|17|01-04|label:def:1.9
dyadic partitioning|二进划分|39|02-02|label:thm:2.2
earth mover’s distance|推土机距离|52|02-05|推土机
empirical process|经验过程|44|02-03|经验过程
empirical risk minimization (ERM)|经验风险最小化（ERM）|215|08-02|经验风险
entropic optimal transport|熵正则最优传输|95|04-01|file-start
Fenchel–Young inequality|Fenchel–Young不等式|231|A-01|label:thm:A.6
first variation|一阶变分|130|05-04|label:def:5.9
Fisher–Rao|Fisher–Rao|139|05-07|label:eq:5.17
Fokker–Planck equation|Fokker–Planck方程|164|06-02|label:thm:6.11
fundamental theorem of optimal transport|最优传输基本定理|25|01-05|label:thm:1.14
geodesic|测地线|190|07-01|label:def:7.3
geodesic!extendable|测地线!可延拓|218|08-02|label:def:8.6
geodesic!generalized|测地线!广义形式|209|07-04|广义
Geodesic convexity|测地凸性|127|05-02|测地凸
geodesic space|测地空间|188|07-01|label:sec:7.1.1
Gibbs variational principle|Gibbs变分原理|98|04-01|Gibbs
gluing lemma|粘合引理|238|B-01|label:lem:B.5
goodness-of-fit testing|拟合优度检验|53|02-05|拟合优度
Grönwall’s inequality|Grönwall不等式|132|05-04|Grönwall
Hadamard|Hadamard|||see:NPC
Hellinger–Kantorovich|Hellinger–Kantorovich|||see:Wasserstein–Fisher–Rao (WFR)
Hoeffding’s decomposition|Hoeffding分解|106|04-03|Hoeffding
hugging|贴合函数|215|08-02|label:def:8.2
integral probability metric (IPM)|积分概率度量（IPM）|64|02-08|label:def:2.19
interaction energy|相互作用能|131|05-04|label:ex:5.13
internal energy|内能|131|05-04|label:ex:5.12
Kantorovich potentials|Kantorovich势|27|01-05|label:def:1.15
Kantorovich problem|Kantorovich问题|3|01-01|label:eq:KOT
Kantorovich–Rubinstein distance|Kantorovich–Rubinstein距离|||see:Wasserstein distance
Langevin diffusion|Langevin扩散|161|06-02|Langevin扩散
Langevin diffusion!mean-field|Langevin扩散!平均场|171|06-03|平均场或相互作用 Langevin 动力学
Langevin diffusion!mirror Langevin|Langevin扩散!镜像Langevin|168|06-02|所谓镜像 Langevin 扩散
Langevin diffusion!Newton–Langevin|Langevin扩散!Newton–Langevin|169|06-02|得到作为 Newton 法抽样类比的 Newton--Langevin 扩散
Langevin diffusion!underdamped Langevin|Langevin扩散!欠阻尼Langevin|169|06-02|欠阻尼
length|长度|188|07-01|label:eq:7.1
logarithmic map|对数映射|203|07-03|label:def:7.20
logistic function|逻辑斯蒂函数|178|06-05|广义线性模型使用的 logistic 函数
maximum mean discrepancy (MMD)|最大均值差异（MMD）|65|02-08|label:def:2.20
McKean–Vlasov|McKean–Vlasov|171|06-03|label:sec:6.3.1
mean-field neural networks|平均场神经网络|177|06-05|label:sec:6.5
metric derivative|度量导数|124|05-01|label:def:5.2
midpoint|中点|190|07-01|label:sec:7.1.2
Monge problem|Monge问题|2|01-01|Monge表述
neural network|神经网络|177|06-05|label:sec:6.5
neural tangent kernel (NTK)|神经切线核（NTK）|184|06-07|NTK
NNC|非负曲率（NNC）|196|07-02|NNC
non-parametric maximum likelihood (NPMLE)|非参数最大似然（NPMLE）|174|06-04|label:sec:6.4
NPC|非正曲率（NPC）|196|07-02|NPC
path|路径|188|07-01|路径
perceptron|感知机|180|06-06|感知机
plug-in estimator|代入估计量|52|02-05|代入
Poincaré inequality|Poincaré不等式|88|03-06|label:def:3.12
Polyak–Łojasiewicz (PŁ) inequality|Polyak–Łojasiewicz（PŁ）不等式|132,233|05-04|Polyak
portmanteau theorem|Portmanteau定理|238|B-01|label:thm:B.4
potential energy|势能|131|05-04|label:ex:5.11
Prokhorov’s theorem|Prokhorov定理|237|B-01|label:thm:B.3
proximal sampler|近端抽样器|168|06-02|引入的近端抽样器
rectifiable path|可求长路径|188|07-01|可求长
Rockafellar’s theorem|Rockafellar定理|17|01-04|label:thm:1.10
semi-discrete optimal transport|半离散最优传输|72,115|02-09|半离散
semidual|半对偶|23|01-05|label:sec:1.5.2
semidual!stability|半对偶!稳定性|79|03-02|label:sec:3.2
Sinkhorn divergence|Sinkhorn散度|115|04-05|Sinkhorn散度
Sinkhorn’s algorithm|Sinkhorn算法|102|04-02|Sinkhorn
Sobolev space|Sobolev空间|60|02-07|Sobolev
Stein variational gradient descent (SVGD)|Stein变分梯度下降（SVGD）|159|06-01|label:sec:6.1.4
subdifferential|次微分|230|A-01|label:def:A.2
tangent cone|切锥|199,202|07-03|label:sec:7.3
transformers|Transformer|180|06-06|label:sec:6.6
unbalanced optimal transport|非平衡最优传输|138|05-07|非平衡
variance equality|方差等式|215|08-02|label:thm:8.3
variational inference (VI)|变分推断（VI）|151|06-01|label:sec:6.1
variational inference (VI)!Gaussian|变分推断（VI）!高斯|154|06-01|label:sec:6.1.2
variational inference (VI)!mean-field|变分推断（VI）!平均场|156|06-01|label:sec:6.1.3
Wasserstein distance|Wasserstein距离|7|01-02|label:def:1.2
Wasserstein distance!sliced|Wasserstein距离!切片|69|02-08|label:sec:2.8.4
Wasserstein distance!smoothed|Wasserstein距离!平滑|68|02-08|label:sec:2.8.3
Wasserstein–Fisher–Rao (WFR)|Wasserstein–Fisher–Rao（WFR）|140,172|05-07|label:eq:5.20
Wasserstein gradient|Wasserstein梯度|130|05-04|label:prop:5.10
Wasserstein gradient flow|Wasserstein梯度流|131|05-04|label:def:5.14
weak convergence|弱收敛|237|B-01|label:def:B.1
'''
rows=[]
for line in DATA.strip().splitlines():
    en,zh,pages,file,selector=line.split('|')
    rows.append(dict(original=en,translated=zh,source_printed=pages,file=file,selector=selector))
assert len(rows)==100,len(rows)
(BASE/'work/full-index-plan.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')

# Execute the installed helper using its exposed functions on task-scoped
# staging copies. Its __main__ hardcodes an unrelated old book path, so it
# cannot safely be invoked verbatim. It finds English candidates; the final
# Chinese anchors below use the source-evidenced semantic map.
helper=runpy.run_path(r'C:/Users/Administrator/.codex/skills/pdf-to-chinese-tex/scripts/generate_index_anchors.py',run_name='skill_helper')
normalized=TEMP/'index-for-skill.md'
normalized.write_text('## INDEX\n'+'\n'.join(r['original'].replace('!',' ') +', '+r['source_printed'] for r in rows if r['source_printed']),encoding='utf-8')
stage=TEMP/'index-helper-stage'; stage.mkdir(exist_ok=True)
for p in (BASE/'sections-tex').glob('*.tex'): shutil.copy2(p,stage/p.name)
terms=helper['parse_original_terms_cleaned'](str(normalized))
helper['insert_index_anchors'](str(stage),terms)
print('Original index:',len(rows),'entries; helper parsed',len(terms),'English candidates.')

def display(row):
    # ASCII sort keys preserve the original English alphabetical order while
    # labels and the visible index stay Chinese with original English terms.
    ens=row['original'].split('!'); zhs=row['translated'].split('!')
    return '!'.join(e+'@'+(z if z==e or z.endswith('（'+e+'）') else z+'（'+e+'）') for e,z in zip(ens,zhs))

def locate(t,sel):
    if sel=='file-start': return 0
    if sel.startswith('label:'):
        k=sel[6:]; needle='\\label{'+k+'}'
        i=t.find(needle)
        return (i+len(needle)) if i>=0 else None
    # Spacing varies in Chinese/English mixed prose. Match the semantic term,
    # then avoid leaving the anchor inside section arguments or environments'
    # optional titles. Anchoring immediately after that argument's closing
    # brace/bracket preserves the same occurrence without fragile contents.
    pat=r'\s*'.join(re.escape(c) for c in sel)
    m=re.search(pat,t,re.I)
    if not m: return None
    pos=m.end()
    before=t[:m.start()]
    opened=[]
    for z,c in enumerate(before):
        if c=='{' and (z==0 or before[z-1]!='\\'): opened.append(z)
        elif c=='}' and (z==0 or before[z-1]!='\\') and opened: opened.pop()
    if opened:
        start=opened[-1]
        cmd=re.search(r'\\([A-Za-z]+)\*?\{$',t[max(0,start-30):start+1])
        if cmd and cmd[1] in ['section','subsection','subsubsection','emph','textbf','textit','operatorname','mathrm','mathsf','text']:
            depth=1; j=start+1
            while j<len(t) and depth:
                if t[j]=='{' and t[j-1]!='\\': depth+=1
                if t[j]=='}' and t[j-1]!='\\': depth-=1
                j+=1
            pos=j
            # The label should remain attached to the heading before index.
            lm=re.match(r'\s*\\label\{[^}]+\}',t[pos:])
            if lm: pos+=lm.end()
    return pos

if '--apply' in __import__('sys').argv:
    missing=[]; inserted=[]
    # Remove only anchors created by this pipeline, enabling repeatable update.
    for f in (BASE/'sections-tex').glob('*.tex'):
        t=f.read_text('utf-8')
        t=re.sub(r'\\index\{[^{}]*\}(?:\s*% FULLINDEX[^\n]*\n?)?', '', t)
        f.write_text(t,encoding='utf-8')
    for row in rows:
        if row['selector'].startswith('see:'): continue
        f=BASE/'sections-tex'/f'{row["file"]}.tex'
        if not f.exists(): missing.append(row); continue
        t=f.read_text('utf-8'); pos=locate(t,row['selector'])
        if pos is None: missing.append(row); continue
        anchor='\\index{'+display(row)+'|hyperpage}'
        f.write_text(t[:pos]+anchor+t[pos:],encoding='utf-8')
        inserted.append(dict(row,anchor_context=t[max(0,pos-70):pos+70]))
    # Extra original page locations for multi-location entries.
    extra=[('Polyak–Łojasiewicz (PŁ) inequality','A-02','label:def:A.10'),('semi-discrete optimal transport','04-05','半离散'),('tangent cone','07-03','label:def:7.19'),('Wasserstein–Fisher–Rao (WFR)','06-03','label:sec:6.3.2')]
    for en,file,sel in extra:
        row=next(r for r in rows if r['original']==en); f=BASE/'sections-tex'/f'{file}.tex'
        if not f.exists(): missing.append(dict(row,file=file,selector=sel)); continue
        t=f.read_text('utf-8'); pos=locate(t,sel)
        if pos is None: missing.append(dict(row,file=file,selector=sel)); continue
        f.write_text(t[:pos]+'\\index{'+display(row)+'|hyperpage}'+t[pos:],encoding='utf-8')
        inserted.append(dict(row,file=file,selector=sel))
    see=[]
    for row in rows:
        if not row['selector'].startswith('see:'): continue
        target=next(r for r in rows if r['original']==row['selector'][4:])
        see.append('\\index{'+display(row)+'|see{'+display(target).split('@',1)[1]+'}}')
    (BASE/'backmatter/index-crossrefs.tex').write_text('\n'.join(see)+'\n',encoding='utf-8')
    (BASE/'work/full-index-anchor-report.json').write_text(json.dumps({'inserted':inserted,'missing':missing,'crossrefs':see},ensure_ascii=False,indent=2),encoding='utf-8')
    print('Inserted',len(inserted),'anchors; missing',[(r['original'],r['file'],r['selector']) for r in missing])
