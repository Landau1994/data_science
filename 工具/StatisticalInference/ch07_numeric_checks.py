"""DS011第7章的确定性数值核验；模型数据逐项核对PDF319、322、326。"""
from pathlib import Path
import json,platform,math
import scipy
import numpy as np
from scipy.special import digamma,gammaln
from scipy.optimize import brentq

egg=np.array([22.0,23.9,20.9,23.8,25.0,24.0,21.7,23.8,22.8,23.1,23.1,23.5,23.0,23.0])
gap=math.log(egg.mean())-np.log(egg).mean()
alpha=brentq(lambda a:math.log(a)-digamma(a)-gap,1,10000,xtol=1e-10)
obs=np.array([0,20,1,19]);p=.5
z=brentq(lambda z:np.prod(1-obs*z)-(1-p)**4,0,1/20,xtol=1e-15)
pop=np.array([3540,3560,3739,2784,2571,2729,3952,993,1908,948,1172,1047,3138,5485,5554,2943,4969,4828],dtype=float)
cases=np.array([3,4,1,1,3,1,2,0,2,0,1,3,5,4,6,2,5,4],dtype=float)

def em(missing):
    beta=.001;tau=pop.copy();tau[0]=1000
    history=[]
    for it in range(100000):
        x=pop.copy();y=cases.copy()
        if missing=='x':x[0]=tau[0]
        else:y[0]=beta*tau[0]
        bn=y.sum()/x.sum();tn=(x+y)/(1+bn)
        err=max(abs(bn-beta)/max(1,abs(beta)),np.max(np.abs(tn-tau))/max(1,np.max(np.abs(tau))))
        beta,tau=bn,tn
        if missing=='x':
            ll=float(np.sum(-beta*tau+cases*np.log(beta*tau)-gammaln(cases+1))+np.sum(-tau[1:]+pop[1:]*np.log(tau[1:])-gammaln(pop[1:]+1)))
        else:
            ll=float(np.sum(-tau+pop*np.log(tau)-gammaln(pop+1))+np.sum(-beta*tau[1:]+cases[1:]*np.log(beta*tau[1:])-gammaln(cases[1:]+1)))
        history.append(ll)
        if err<1e-12:break
    assert min(np.diff(history))>=-1e-8
    return {'iterations':it+1,'beta':float(beta),'tau':tau.tolist(),'final_relative_change':float(err),'log_likelihood_first':history[0],'log_likelihood_last':history[-1],'min_log_likelihood_step':float(min(np.diff(history)))}

fullbeta=float(cases.sum()/pop.sum());fulltau=(pop+cases)/(1+fullbeta)
otherbeta=float(cases[1:].sum()/pop[1:].sum())
tau=fulltau.copy();tau[0]=cases[0]/otherbeta;tau[1:]=(pop[1:]+cases[1:])/(1+otherbeta)
failure=np.array([50.1,70.1,137.0,166.9,170.5,152.8,80.5,123.5,112.6,148.5,160.0,125.4])
out={'environment':{'python':platform.python_version(),'scipy':scipy.__version__,'numpy':np.__version__,'randomness':'none'},'7.2':{'data':egg.tolist(),'n':len(egg),'sample_mean':float(egg.mean()),'mean_log':float(np.log(egg).mean()),'gamma_shape_mle':alpha,'gamma_scale_mle':float(egg.mean()/alpha),'shape_score_residual':float(math.log(alpha)-digamma(alpha)-gap)},'7.5':{'z_root':z,'one_over_z':1/z,'k_mle':math.floor(1/z),'likelihood_ratio_at26':13**4/(26*6*25*7),'likelihood_ratio_at27':13.5**4/(27*7*26*8)},'7.10':{'alpha_mle':float(len(egg)/np.log(egg.max()/egg).sum()),'beta_mle':float(egg.max())},'7.28':{'population':pop.tolist(),'cases':cases.tolist(),'population_sum':float(pop.sum()),'cases_sum':float(cases.sum()),'full_beta':fullbeta,'full_tau':fulltau.tolist(),'missing_x_beta_exact':otherbeta,'missing_x_tau_exact':tau.tolist(),'missing_x_em':em('x'),'missing_y_beta_exact':otherbeta,'missing_y_tau1_exact':float(pop[0]),'missing_y_em':em('y')},'7.29':{'m':float(pop.sum()),'beta_complete_and_missing_x':fullbeta,'tau_complete_and_missing_x':((pop+cases)/(pop.sum()+cases.sum())).tolist(),'conditional_missing_x':float(pop.sum()-pop[1:].sum())},'7.46':{'data':[1.29,.86,1.33],'method_of_moments':(1.29+.86+1.33)*2/9,'mle':1.33/2,'bias_corrected_mle':(8/7)*1.33/2},'7.49':{'data':failure.tolist(),'n_times_min':float(len(failure)*failure.min()),'sample_mean':float(failure.mean())},'scope':'只有上述固定数据、确定性根求解与EM停止阈值范围实际执行；不表示任意初值、数据或模型的收敛证明。'}
Path(__file__).with_name('ch07-numeric-results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['7.2','7.5','7.10','7.46','7.49']},ensure_ascii=False,indent=2))
print('EM iterations',out['7.28']['missing_x_em']['iterations'],out['7.28']['missing_y_em']['iterations'])
print('Poisson beta full/partial',fullbeta,otherbeta)
