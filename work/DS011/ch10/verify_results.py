"""Deterministic checks of formulas and already generated records; no new simulation."""
from pathlib import Path
import json,math
import numpy as np
from scipy import stats,special

HERE=Path(__file__).parent
R=json.loads((HERE/'results.json').read_text(encoding='utf-8'))
RR=json.loads((HERE/'robust-results.json').read_text(encoding='utf-8'))
checks={}
z=R['10.11']['known_mu_counterexample'];a=z['MLE_shape'];x=np.array(z['data'])
residual=math.log(a)+1-special.digamma(a)+np.log(x).mean()-x.mean()
assert abs(residual)<1e-11
checks['10.11_known_mean_MLE_shape_score_residual']=float(residual)
cs=np.genfromtxt(HERE/'10.13-multisets.csv',delimiter=',',names=True)
assert len(cs)==35 and abs(cs['probability'].sum()-1)<1e-14
m=float(cs['mean']@cs['probability']);v=float(((cs['mean']-m)**2)@cs['probability'])
assert abs(m-6.75)<1e-14 and abs(v-3.921875)<1e-14
checks['10.13_multiset_weight_sum_mean_variance']=[float(cs['probability'].sum()),m,v]
diff=0
for n in [1,2,5,24,100]:
    k=np.arange(n+1);h=k/n*(1-k/n)
    for p in [.01,.1,.5,.8,.99]:
        q=p*(1-p);pr=stats.binom.pmf(k,n,p)
        exact=float(pr@((h-float(pr@h))**2))
        formula=(n-1)**2/n**3*q*(1-4*q)+2*(n-1)/n**3*q*q
        diff=max(diff,abs(exact-formula));assert abs(exact-formula)<1e-14
checks['10.10_formula_max_error_25_finite_models']=diff
z=stats.norm.ppf(.975);p=.0546
lo=(1+z*z-z*math.sqrt(z*z+1))/(2*(1+z*z))
assert p<lo and 1-p<.95
checks['10.45_exact_counterexample']={'n':1,'p':p,'Y1_lower_endpoint':lo,'coverage':1-p}
recomputed={}
for r in RR:
    name=r['distribution'];raw=np.genfromtxt(HERE/f'10.39-46-{name}-samples.csv',delimiter=',',names=True,deletechars='')
    assert len(raw)==3000
    methods={'sandwich_10.3.6':('Huber','SE_correct_sandwich'),'printed_10.3.8':('Huber','SE_printed_10.3.8'),'naive_10.3.9':('Huber','SE_naive'),'bootstrap_Huber':('Huber','SE_boot_Huber'),'bootstrap_median':('median','SE_boot_median')}
    max_difference=0
    for row in r['power']:
        shift=row['shift_in_population_sd']*r['population_sd']
        for method,(center,se) in methods.items():
            actual=float((abs((raw[center]+shift)/raw[se])>stats.norm.ppf(.95)).mean())
            max_difference=max(max_difference,abs(actual-row[method]))
    for row in r['coverage']:
        for method,(center,se) in methods.items():
            actual=float((abs(raw[center])<=stats.norm.ppf((1+row['nominal'])/2)*raw[se]).mean())
            max_difference=max(max_difference,abs(actual-row[method]))
    assert max_difference==0
    inf=int(np.isinf(raw['SE_printed_10.3.8']).sum())
    assert inf==r['count_printed_variance_infinite']
    recomputed[name]={'rows':len(raw),'maximum_probability_difference':max_difference,'printed_SE_infinite':inf}
checks['10.39_46_reaggregate_existing_records']=recomputed
(HERE/'verification.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(checks,ensure_ascii=False,indent=2))
