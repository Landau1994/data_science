"""只回传经root原页对照的第5章索引定位，不改维护者的总台账。"""
from pathlib import Path
import json

work = Path(__file__).resolve().parent
resolved = {
    (48,177): ('idx:root5-p177-emd', '原201页脚注1的Earth Mover Distance译名与名称讨论'),
    (159,179): ('sec:5.1', '原203页5.1节给出Wp费用最小值的正式定义'),
    (160,181): ('obj:5.3', '原205页引理5.3，映射与逼近的三角不等式证明'),
    (41,182): ('obj:5.4', '原206页引理5.4，明确以测度分解证明三角不等式'),
    (70,182): ('obj:5.5', '原206页gluing lemma的原陈述5.5'),
    (160,182): ('obj:5.4', '原206页引理5.4的三角不等式第二证明'),
    (114,183): ('obj:5.6', '原207页注5.6明确推广到一般Polish空间'),
    (159,183): ('sec:5.2', '原207页5.2节开头比较Wp距离诱导拓扑与弱收敛'),
    (161,183): ('obj:5.7', '原207页定义5.7，Wasserstein空间的原定义'),
    (162,183): ('sec:5.2', '原207页5.2节开头重述弱/窄收敛与Cb对偶'),
    (44,184): ('obj:5.9', '原208页定理5.9及证明以距离费用W1的Lip1对偶公式刻画弱收敛'),
    (92,184): ('idx:root5-p184-localcompact', '原208页第三条bullet讨论紧邻域、局部紧性和C0的对偶'),
    (99,187): ('idx:root5-p187-metricderivative', '原211页框5.1第一无编号定义，度量导数首次定义'),
    (99,188): ('idx:root5-p188-metricformula', '原212页框5.1延续的度量导数极限公式'),
    (8,188): ('idx:root5-p188-ac', '原212页框5.1绝对连续曲线的g积分控制定义及AC记号'),
    (15,189): ('sec:5.3.1', '原213页5.3.1标题引入Benamou–Brenier泛函B_p'),
    (148,196): ('obj:5.22', '原220页注5.22完整定义环面周期卷积及同等构造'),
    (148,199): ('idx:root5-p199-torus', '原223页定理5.24证明第二部分为保紧性选用环面构造'),
    (137,200): ('idx:root5-p200-semiconcavity', '原224页定理5.24证明用一致半凹性推出梯度几乎处处收敛'),
    (43,202): ('sec:5.4', '原226页5.4节引入Wasserstein空间常速测地线/位移插值'),
    (68,202): ('box:5.2', '原226页框5.2的一般度量空间测地线与长度空间定义'),
    (15,203): ('idx:root5-p203-bb', '原227页定理5.27后段引入Benamou–Brenier公式名称及动态解释'),
    (66,203): ('obj:5.27', '原227页定理5.27显式构造Wp常速测地线'),
    (85,205): ('idx:root5-p205-kinetic', '原229页末定义曲线p-动能K_p，随后用于表示定理'),
    (98,205): ('idx:root5-p205-kinetic', '原229页末引出曲线表示定理并定义AC/C上的动能，随后5.31给曲线测度Q'),
    (3,207): ('sec:5.5.1', '原231页5.5.1标题及首显示式定义W_infinity运输费用距离'),
    (45,209): ('sec:5.5.2', '原233页5.5.2节首段将W1写为Lipschitz半范数的对偶范数'),
    (1,210): ('idx:root5-p210-hminusone', '原234页引理5.33后明确定义dot H^{-1}范数与Neumann表示'),
    (2,211): ('idx:root5-p211-crowd', '原235页首段讨论拥挤约束rho<=1的L-infinity密度限制'),
    (32,211): ('idx:root5-p211-crowd', '原235页同段以人群运动解释密度接近1的演化模型'),
    (15,211): ('idx:root5-p211-bb', '原235页定理5.34证明应用Benamou–Brenier公式求反向估计'),
    (18,211): ('sec:5.5.3', '原235页5.5.3首段回顾d_alpha分支运输距离的定义'),
    (140,214): ('sec:5.5.4', '原238页5.5.4给出切片Wasserstein距离的积分定义'),
    (77,215): ('idx:root5-p215-images', '原239页段落将图像空间位置和RGB分量联系于R5上的测度'),
    (104,215): ('sec:5.5.5', '原239页开始5.5.5重心问题；其多边缘等价描述延续至原240页，保留原索引指向节首的范围'),
    (140,217): ('fig:5.3', '原241页图5.3图注第二排明确解释SW2重心插值'),
}
items = json.loads((work / 'index-map-root-scope.json').read_text(encoding='utf-8'))
result = []
for item in items:
    refs = [ref for ref in item['references'] if 177 <= int(ref['source_printed_page']) <= 218]
    if not refs:
        continue
    item['references'] = refs
    for ref in refs:
        pair = item['id'], int(ref['source_printed_page'])
        if pair in resolved:
            ref['target'], ref['basis'] = resolved[pair]
    result.append(item)
(work / 'index-map-root5-resolved.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
done = sum(ref['target'] is not None for item in result for ref in item['references'])
total = sum(len(item['references']) for item in result)
print(f'第5章索引逐页定位：{done}/{total}')
