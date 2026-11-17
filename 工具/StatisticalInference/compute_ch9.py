"""第9章确定性数值求解。根与离散边界均单独报告，不作模拟。"""
from pathlib import Path
import json, math, platform
import scipy
import numpy as np
import mpmath as mp
from scipy.stats import chi2, norm, t, poisson
from scipy.optimize import brentq
from scipy.special import gammaln
OUT=Path(__file__).with_name('ch9-computations');OUT.mkdir(exist_ok=True)
eggs=[22.,23.9,20.9,23.8,25.,24.,21.7,23.8,22.8,23.1,23.1,23.5,23.,23.]
a=len(eggs)/sum(math.log(max(eggs)/v) for v in eggs)
aphids=[155,104,66,50,36,40,30,35,42]
y=sum(aphids); n=len(aphids)
def lr_pvalue(mu):
 k=np.arange(0,int(poisson.ppf(1-1e-14,mu))+2,dtype=float)
 dev=2*(np.where(k>0,k*np.log(np.maximum(k,1)/mu),0)-k+mu)
 obs=2*(y*math.log(y/mu)-y+mu)
 return float(np.sum(poisson.pmf(k,mu)[dev>=obs-1e-10]))
def boundary(lo,hi,increasing):
 for _ in range(70):
  m=(lo+hi)/2
  if (lr_pvalue(m)>.1)==increasing: hi=m
  else: lo=m
 return (lo+hi)/2
low=boundary(y*.8,y,True);high=boundary(y,y*1.2,False)
# 检查所有可能接受的排序区间，防止离散p值在边界附近形成未发现的小分量。
# Chernoff两尾界 p_LR <= 2 exp[-D(y;mu)/2] 将接受集限制在有限区间。
D=lambda mu:2*(y*math.log(y/mu)-y+mu)
limit=2*math.log(2/.1)
bound_lo=brentq(lambda z:D(z)-limit,y*.1,y)
bound_hi=brentq(lambda z:D(z)-limit,y,y*3)
switches=[]
for k in range(0,4*y):
 if k==y:continue
 z=math.exp(((k*math.log(k) if k else 0)-y*math.log(y))/(k-y)-1)
 if bound_lo<z<bound_hi:switches.append(z)
breaks=sorted([bound_lo,y,bound_hi]+switches)
accepted=[]
for l,r in zip(breaks,breaks[1:]):
 mid=(l+r)/2
 ks=np.arange(0,int(poisson.ppf(1-1e-14,mid))+2,dtype=float)
 devs=2*(np.where(ks>0,ks*np.log(np.maximum(ks,1)/mid),0)-ks+mid)
 selected=ks[devs>=D(mid)-1e-10].astype(int)
 lo_tail=int(max((v for v in selected if v<mid),default=-1))
 hi_tail=int(min((v for v in selected if v>=mid),default=len(ks)))
 pv=lambda z:float(poisson.cdf(lo_tail,z)+poisson.sf(hi_tail-1,z))
 der=lambda z:float(-poisson.pmf(lo_tail,z)+poisson.pmf(hi_tail-1,z))
 points=[l,r]
 if der(l)*der(r)<0:points.insert(1,brentq(der,l,r))
 sub=[]
 for a1,b1 in zip(points,points[1:]):
  roots=[a1,b1]
  if (pv(a1)-.1)*(pv(b1)-.1)<0:roots.insert(1,brentq(lambda z:pv(z)-.1,a1,b1))
  for aa,bb in zip(roots,roots[1:]):
   if pv((aa+bb)/2)>.1:sub.append([aa,bb])
 accepted.extend(sub)
merged=[]
for interval in accepted:
 if merged and abs(merged[-1][1]-interval[0])<1e-7:merged[-1][1]=interval[1]
 else:merged.append(interval)
dev=lambda mu: 2*(y*math.log(y/mu)-y+mu)-chi2.isf(.1,1)
asym=[brentq(dev,y*.5,y)/n,brentq(dev,y,y*1.5)/n]
garwood=[chi2.ppf(.05,2*y)/(2*n),chi2.ppf(.95,2*(y+1))/(2*n)]
known=math.ceil((8*norm.isf(.025))**2)
unknown=next(N for N in range(2,10000) if chi2.ppf(.9,N-1)<=(N-1)*N/(64*t.isf(.025,N-1)**2))
alpha=.1;nu=2
cutoffs={}
for name,power in [('likelihood',1.5),('shortest_length',2),('unbiased_ratio',1)]:
 # nu=2时CDF为1-exp(-x/2)。用60位数直接解，避免极窄尾区间
 # 中双精度CDF相减及默认根容差影响较大端点的末位。
 mp.mp.dps=60
 def eq_high(aa):
  bb=-2*mp.log(mp.exp(-aa/2)-mp.mpf('.9'))
  return mp.mpf(str(power))*mp.log(aa)-aa/2-mp.mpf(str(power))*mp.log(bb)+bb/2
 ll=mp.mpf('1e-50');rr=-2*mp.log(mp.mpf('.9'))-mp.mpf('1e-50')
 for _ in range(250):
  mm=(ll+rr)/2
  if eq_high(mm)>0:rr=mm
  else:ll=mm
 aa_mp=(ll+rr)/2;bb_mp=-2*mp.log(mp.exp(-aa_mp/2)-mp.mpf('.9'))
 aa,bb=float(aa_mp),float(bb_mp)
 cutoffs[name]={'a':aa,'b':bb,'mass':float(chi2.cdf(bb,nu)-chi2.cdf(aa,nu)),
                 'high_precision_a':str(aa_mp),'high_precision_b':str(bb_mp),
                 'length_coefficient_of_s_squared':nu*(1/aa-1/bb),'endpoint_ratio':bb/aa}
aa=chi2.ppf(.05,nu);bb=chi2.ppf(.95,nu)
cutoffs['equal_tail']={'a':aa,'b':bb,'mass':.9,'length_coefficient_of_s_squared':nu*(1/aa-1/bb),'endpoint_ratio':bb/aa}
p=.04;al=.05;delta=.01;beta=(al-p)/(1-p)
cox_old=p*norm.sf(norm.isf(al)-delta/10)+(1-p)*norm.sf(norm.isf(al)-delta)
cox_new=p+(1-p)*norm.sf(norm.isf(beta)-delta)
c=.442;u=1-c**(1/3)
aa=brentq(lambda z:3*z*(1-z)**2-c,.25,1/3)
bb=brentq(lambda z:3*z*(1-z)**2-c,1/3,.45)
result={'environment':{'python':platform.python_version(),'scipy':scipy.__version__,'numpy':np.__version__,'mpmath':mp.__version__,'method':'确定性分位数与一维求根；9.52用60位数二分，无随机抽样'},
 '9.3':{'data':eggs,'alpha_mle':a,'beta_mle':max(eggs),'upper':max(eggs)*.05**(-1/(len(eggs)*a))},
 '9.18':{'target':c,'correct_boundaries':[u,aa,bb,1-bb,1-aa,1-u],'original_counterexample_p':.634,'original_acceptance_probability':3*.634**2*.366},
 '9.23':{'data':aphids,'sum':y,'exact_nonrandomized_LR_interval':[low/n,high/n],
  'all_ordering_cells_checked':len(breaks)-1,'Chernoff_outer_bounds':[bound_lo/n,bound_hi/n],
  'connected_components_from_all_cells':[[a/n,b/n] for a,b in merged],
  'endpoint_pvalues_one_sided_limits':[[lr_pvalue(v-1e-6),lr_pvalue(v+1e-6)] for v in [low,high]],
  'asymptotic_chisquare_LR_interval':asym,'Garwood_equal_tail':garwood,
  'truncation':'Poisson upper omitted mass <=1e-14; deterministic LR ordering and bisection; discrete p-value may jump'},
 '9.34':{'known_sigma_min_n':known,'unknown_sigma_min_n':unknown,
  'probability_at_n':float(chi2.cdf((unknown-1)*unknown/(64*t.isf(.025,unknown-1)**2),unknown-1)),
  'probability_at_previous_n':float(chi2.cdf((unknown-2)*(unknown-1)/(64*t.isf(.025,unknown-2)**2),unknown-2))},
 '9.45':{'original_Madansky_coverage':.99**120,'exact_corrected_minimum_denominator':-math.log(.3)/120,
  'correct_quantile_upper_.3':float(chi2.isf(.3,240)), 'UMA_expected_length_factor':240/chi2.isf(.3,240),
  'original_Madansky_length_factor':-1/(120*math.log(.99)),'corrected_Madansky_length_factor':-1/math.log(.3)},
 '9.49':{'p':p,'alpha':al,'delta':delta,'conditional_test_power':float(cox_old),'always_reject_large_variance_power':float(cox_new)},
 '9.52':cutoffs}
(OUT/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
