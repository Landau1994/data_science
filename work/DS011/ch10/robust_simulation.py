"""Finite, declared-location simulation shared by exercises 10.39 and 10.46."""
from pathlib import Path
import json,csv,math
import numpy as np
from scipy import stats
OUT=Path(__file__).parent
N=3000;B=199;n=15;k=1.5
def huber(x):
 lo=x.min(axis=-1)-k;hi=x.max(axis=-1)+k
 for j in range(36):
  mid=(lo+hi)/2;s=np.clip(x-mid[...,None],-k,k).sum(axis=-1);lo=np.where(s>0,mid,lo);hi=np.where(s>0,hi,mid)
 return (lo+hi)/2
allresults=[]
for idx,name in enumerate(['normal','t5','logistic','laplace']):
 seed=2026111439+idx;rng=np.random.default_rng(seed)
 if name=='normal':x=rng.standard_normal((N,n));sigma=1;f0=stats.norm.pdf(0)
 elif name=='t5':x=rng.standard_t(5,(N,n));sigma=math.sqrt(5/3);f0=stats.t.pdf(0,5)
 elif name=='logistic':x=rng.logistic(size=(N,n));sigma=math.pi/math.sqrt(3);f0=.25
 else:x=rng.laplace(size=(N,n));sigma=math.sqrt(2);f0=.5
 h=huber(x);med=np.median(x,axis=1);d=x-h[:,None];A=(abs(d)<k).mean(axis=1);BB=np.clip(d,-k,k)**2;BB=BB.mean(axis=1)
 se1=np.sqrt(BB/(n*A*A));se2=np.divide(np.sqrt(BB/n),1-A,out=np.full(N,np.inf),where=A<1);se3=np.sqrt(np.mean(d*d,axis=1)/n)
 seb=np.empty(N);sem=np.empty(N);maxres=0
 for i in range(0,N,100):
  stop=min(i+100,N);pool=x[i:stop];indices=rng.integers(n,size=(len(pool),B,n));xx=np.take_along_axis(pool[:,None,:],indices,axis=-1)
  hh=huber(xx);mm=np.median(xx,axis=-1);seb[i:stop]=hh.std(axis=1,ddof=1);sem[i:stop]=mm.std(axis=1,ddof=1)
  maxres=max(maxres,float(np.max(abs(np.clip(xx-hh[...,None],-k,k).sum(axis=-1)))))
 assert np.all(seb>0) and np.all(sem>0)
 with (OUT/f'10.39-46-{name}-samples.csv').open('w',encoding='utf-8',newline='') as f:
  w=csv.writer(f);w.writerow([*[f'x{j}' for j in range(1,n+1)],'Huber','median','SE_correct_sandwich','SE_printed_10.3.8','SE_naive','SE_boot_Huber','SE_boot_median'])
  for row in zip(x,h,med,se1,se2,se3,seb,sem):w.writerow([*row[0],*row[1:]])
 methods={'sandwich_10.3.6':(h,se1),'printed_10.3.8':(h,se2),'naive_10.3.9':(h,se3),'bootstrap_Huber':(h,seb),'bootstrap_median':(med,sem)}
 power=[]
 for shift in [0,.25,.5,.75,1,2]:
  power.append({'shift_in_population_sd':shift,**{m:float((abs((center+shift*sigma)/se)>stats.norm.ppf(.95)).mean()) for m,(center,se) in methods.items()}})
 coverage=[]
 for level in [.9,.95]:
  z=stats.norm.ppf((1+level)/2);cov={'nominal':level}
  for m,(center,se) in methods.items():cov[m]=float((abs(center)<=z*se).mean())
  cov['median_oracle_density']=float((abs(med)<=z/(2*f0*math.sqrt(n))).mean())
  # Distribution-free, conservative equal-tail order-statistic interval for this n.
  legal=[j for j in range(1,9) if 1-2*stats.binom.cdf(j-1,n,.5)>=level]
  j=max(legal);xs=np.sort(x,axis=1);cov['median_order_interval_k']=j;cov['median_order_interval_coverage']=float(((xs[:,j-1]<=0)&(0<=xs[:,n-j])).mean());cov['median_order_interval_exact_coverage']=float(1-2*stats.binom.cdf(j-1,n,.5))
  coverage.append(cov)
 allresults.append({'distribution':name,'seed':seed,'n':n,'outer_replicates':N,'bootstrap_replicates':B,'Huber_k':k,'population_sd':sigma,'power':power,'coverage':coverage,'count_printed_variance_infinite':int((A==1).sum()),'max_abs_bootstrap_score_residual':maxres,'Monte_Carlo_SE_at_probability_09':math.sqrt(.9*.1/N),'Monte_Carlo_SE_worst_case':.5/math.sqrt(N)})
 (OUT/'robust-results.json').write_text(json.dumps(allresults,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(name,'completed',flush=True)
