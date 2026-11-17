"""Independent computations; source errata are never silently repaired here."""
from pathlib import Path
import numpy as np,json,csv,math,platform,itertools
import scipy
from scipy import stats,special,optimize,integrate
OUT=Path(__file__).parent;OUT.mkdir(parents=True,exist_ok=True)
R={'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},'rng':'PCG64 via numpy.default_rng','fixed_seed_caveat':'Not a cross-version bitwise guarantee'}
def save(name,header,rows):
 with (OUT/name).open('w',encoding='utf-8',newline='') as f:
  w=csv.writer(f);w.writerow(header);w.writerows(rows)
def done(name,value):
 R[name]=value;(OUT/'results.json').write_text(json.dumps(R,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8');print(name,'done',flush=True)
def summ(x):return {'mean':float(np.mean(x)),'variance_ddof1':float(np.var(x,ddof=1)),'q025_50_975':np.quantile(x,[.025,.5,.975]).tolist()}
T=104;n=15;done('10.9',{'sum':T,'n':n,'lambda_mle':T/n,'UMVU_zero':(1-1/n)**T,'MLE_zero':math.exp(-T/n),'UMVU_one':T/n*(1-1/n)**(T-1),'MLE_one':T/n*math.exp(-T/n)})
a=np.linspace(.1,10,200);rows=[]
for mu in a:
 rows.append([mu,*[1/((mu/b)*special.polygamma(1,mu/b)) for b in [1,3,5,10]]])
save('10.11-mean-ARE.csv',['mu','beta1','beta3','beta5','beta10'],rows)
rows=[]
for b in np.linspace(.1,10,200):
 vals=[]
 for mu in [1,3,5,10]:
  a=mu/b;tri=special.polygamma(1,a);vals.append(tri/((a*tri-1)*(2+3/a)))
 rows.append([b,*vals])
save('10.11-scale-ARE.csv',['beta','mu1','mu3','mu5','mu10'],rows)
c=-np.log([.5,1.5]).mean();a=optimize.brentq(lambda a:np.log(a)-special.digamma(a)-c,.01,1000)
done('10.11',{'known_mu_counterexample':{'mu':1,'data':[.5,1.5],'MOM_beta':.25,'MLE_beta':1/a,'MLE_shape':a},'known_beta_mean_ARE_example_a1':float(1/special.polygamma(1,1))})
x=np.array([2,4,9,12]);means=np.array([np.mean(v) for v in itertools.product(x,repeat=4)])
save('10.13-all-ordered-resamples.csv',['index','mean'],enumerate(means,1));counts=[]
for c0 in range(5):
 for c1 in range(5-c0):
  for c2 in range(5-c0-c1):
   c3=4-c0-c1-c2;cs=[c0,c1,c2,c3];w=math.factorial(4)/math.prod(math.factorial(v) for v in cs)/256
   counts.append([*cs,float(x@cs/4),w])
save('10.13-multisets.csv',['c2','c4','c9','c12','mean','probability'],counts)
done('10.13',{'n_ordered':len(means),'n_multisets':len(counts),'distinct_means':len(np.unique(means)),'mean':float(means.mean()),'conditional_variance_denominator256':float(means.var()),'exhaustive_sample_variance_denominator255':float(means.var(ddof=1))})
def gamma_fit(x):
 m=x.mean(axis=-1);c=np.log(m)-np.log(x).mean(axis=-1);constant=c<1e-14
 safe=np.where(constant,1e-12,c);a=(3-safe+np.sqrt((safe-3)**2+24*safe))/(12*safe)
 for it in range(30):
  step=(np.log(a)-special.digamma(a)-safe)/(1/a-special.polygamma(1,a));new=a-step;a=np.where(new>0,new,a/2)
 var=m*m/a;var=np.where(constant,0,var)
 return m,var,a,constant
def empirical_varS2(x):
 n=len(x);d=x-x.mean();m2=np.mean(d*d);m4=np.mean(d**4);return float((m4-(n-3)/(n-1)*m2*m2)/n)
normal=np.array([-1.81,.63,2.22,2.41,2.95,4.16,4.24,4.53,5.09]);fish=np.array([19,32,29,13,8,12,16,20,14,17,22,18,23]);gam=np.array([.28,.98,1.36,1.38,2.4,7.42]);B=20000;rng=np.random.default_rng(2026111414)
va_np=rng.choice(normal,(B,len(normal))).var(axis=1,ddof=1);va_par=rng.normal(normal.mean(),normal.std(ddof=0),(B,len(normal))).var(axis=1,ddof=1)
vb_np=rng.choice(fish,(B,len(fish))).var(axis=1,ddof=1);vb_par=rng.poisson(fish.mean(),(B,len(fish))).var(axis=1,ddof=1)
save('10.14-normal-variances.csv',['nonparametric','parametric'],zip(va_np,va_par));save('10.14-fish-variances.csv',['nonparametric','parametric'],zip(vb_np,vb_par))
gm,gv,ga,_=gamma_fit(gam);gb=gm/ga
gp=rng.gamma(ga,gb,(B,len(gam)));gn=rng.choice(gam,(B,len(gam)));mp,vp,ap,cp=gamma_fit(gp);mn,vn,an,cn=gamma_fit(gn)
save('10.14-gamma-estimates.csv',['param_mean','param_variance','nonparam_mean','nonparam_variance'],zip(mp,vp,mn,vn))
done('10.14',{'seed':2026111414,'B':B,'normal':{'data':normal.tolist(),'mean':normal.mean(),'S2':normal.var(ddof=1),'MLE_variance':normal.var(),'nonparametric_var_S2':va_np.var(ddof=1),'nonparametric_exact_conditional_var_S2':empirical_varS2(normal),'parametric_var_S2':va_par.var(ddof=1),'parametric_exact_conditional_var_S2':2*normal.var()**2/(len(normal)-1)},'fish':{'data':fish.tolist(),'mean':fish.mean(),'S2':fish.var(ddof=1),'nonparametric_var_S2':vb_np.var(ddof=1),'parametric_var_S2':vb_par.var(ddof=1),'nonparametric_quantiles':np.quantile(vb_np,[.025,.5,.975]).tolist(),'parametric_quantiles':np.quantile(vb_par,[.025,.5,.975]).tolist()},'gamma':{'data':gam.tolist(),'MLE_mean':float(gm),'MLE_variance':float(gv),'MLE_shape':float(ga),'MLE_scale':float(gb),'parametric_mean_estimates':summ(mp),'parametric_variance_estimates':summ(vp),'nonparametric_mean_estimates':summ(mn),'nonparametric_variance_estimates':summ(vn),'constant_nonparametric_resamples_with_boundary_MLE':int(cn.sum())}})
p=11/24;n=24;q=p*(1-p);rng=np.random.default_rng(2026111416);ph=rng.binomial(n,p,1000000)/n;h=ph*(1-ph);k=np.arange(n+1);hh=k/n*(1-k/n);pmf=stats.binom.pmf(k,n,p);exact=float(np.sum(pmf*(hh-np.sum(pmf*hh))**2))
save('10.16-million-binomial-variance.csv',['H'],zip(h));done('10.16',{'seed':2026111416,'B':len(h),'p':p,'first_order':(1-2*p)**2*q/n,'second_order_term':2*(q/n)**2,'sum_first_and_second':(1-2*p)**2*q/n+2*(q/n)**2,'exact_variance':exact,'simulation_variance':h.var(ddof=1),'bootstrap_conditional_exact':exact})
base=np.array([[576,3.39],[635,3.30],[5.58,2.81],[578,3.03],[666,3.44],[580,3.07],[555,3.00],[661,3.43],[651,3.36],[605,3.13],[653,3.12],[575,2.74],[545,2.76],[572,2.88],[594,2.96]])
def corr(a):
 d=a-a.mean(axis=-2,keepdims=True);v=(d*d).sum(axis=-2);return (d[...,0]*d[...,1]).sum(axis=-1)/np.sqrt(v[...,0]*v[...,1])
out=[]
for j,label in enumerate(['literal_5.58_with_comma_repaired','proposed_558_with_comma_repaired']):
 x=base.copy()
 if j:x[2,0]=558
 rng=np.random.default_rng(2026111417+j);rho=float(corr(x));mu=x.mean(axis=0);cov=np.cov(x,rowvar=False,ddof=0);boot=rng.choice(len(x),(1000,len(x)));rnp=corr(x[boot]);par=rng.multivariate_normal(mu,cov,(1000,len(x)));rp=corr(par)
 assert np.isfinite(rnp).all() and np.isfinite(rp).all()
 save(f'10.17-{j}-bootstrap.csv',['nonparametric_r','parametric_r'],zip(rnp,rp))
 out.append({'data_assumption':label,'data':x.tolist(),'seed':2026111417+j,'r':rho,'mean_LSAT_GPA':mu.tolist(),'MLE_covariance':cov.tolist(),'MLE_variances':np.diag(cov).tolist(),'nonparametric_sd':float(rnp.std(ddof=1)),'parametric_sd':float(rp.std(ddof=1)),'delta_sd':(1-rho*rho)/math.sqrt(15),'z_asymptotic_variance':1/15})
done('10.17',out)
rows=[]
for nu in [3,5,10,25,50]:rows.append([nu,4*stats.t.pdf(0,nu)**2*nu/(nu-2)])
rows.append(['infinity',2/math.pi]);mix=[]
for delta in [0,.01,.05,.1,.2]:
 for sigma in [1,2,5,10]:mix.append([delta,sigma,2/math.pi*((1-delta)+delta/sigma)**2*((1-delta)+delta*sigma*sigma)])
done('10.23',{'student_t':rows,'Tukey_grid':mix})
# ARE of locally consistent estimating-equation roots, not an invented global breakdown rule.
out=[]
for family,dist,I in [('normal',stats.norm(),1),('laplace',stats.laplace(),1)]:
 for c in [.5,1,1.5,2,3]:
  vals={}
  for name in ['Huber','Tukey_printed','Andrews']:
   bound=c*math.pi if name=='Andrews' else c
   if name=='Huber':
    A=dist.cdf(c)-dist.cdf(-c);BB=integrate.quad(lambda x:x*x*dist.pdf(x),-c,c,epsabs=1e-11)[0]+c*c*(1-A)
   elif name=='Tukey_printed':
    A=integrate.quad(lambda x:(c*c-3*x*x)*dist.pdf(x),-c,c,epsabs=1e-11)[0];BB=integrate.quad(lambda x:x*x*(c*c-x*x)**2*dist.pdf(x),-c,c,epsabs=1e-11)[0]
   else:
    A=integrate.quad(lambda x:math.cos(x/c)*dist.pdf(x),-bound,bound,epsabs=1e-11)[0];BB=integrate.quad(lambda x:c*c*math.sin(x/c)**2*dist.pdf(x),-bound,bound,epsabs=1e-11)[0]
   vals[name]={'A':A,'B':BB,'ARE':A*A/(BB*I)}
  out.append({'distribution':family,'c':c,'values':vals})
done('10.30',out)
table=np.array([[34,19],[6,16]]);chi,pval,dof,expected=stats.chi2_contingency(table,correction=False);p1=34/40;p2=19/35;wald=(p1-p2)/math.sqrt(p1*(1-p1)/40+p2*(1-p2)/35)
done('10.31',{'table':table.tolist(),'Pearson_chi2':chi,'p_two_sided':pval,'expected':expected.tolist(),'unpooled_Wald':wald,'unpooled_p_two_sided':float(2*stats.norm.sf(abs(wald))),'Fisher_exact_two_sided':float(stats.fisher_exact(table).pvalue)})
out=[]
for n,p in [(25,.5),(25,.1),(100,.1),(100,.5)]:
 rng=np.random.default_rng(2026111434+n+int(100*p));Y=rng.binomial(n,p,10000);z=2*(special.xlogy(Y,Y/(n*p))+special.xlogy(n-Y,(n-Y)/(n*(1-p))))
 save(f'10.34-n{n}-p{p}-lrt.csv',['LRT'],zip(z));out.append({'n':n,'p0':p,'seed':2026111434+n+int(100*p),'B':10000,'mean':float(z.mean()),'quantiles_80_90_95_99':np.quantile(z,[.8,.9,.95,.99]).tolist(),'rejection_05':float((z>stats.chi2.ppf(.95,1)).mean())})
done('10.34',{'models':out,'chi2_quantiles':stats.chi2.ppf([.8,.9,.95,.99],1).tolist()})
aph=np.array([155,104,66,50,36,40,30,35,42]);n=len(aph);mean=aph.mean();v=aph.var(ddof=1);r=mean*mean/(v-mean);z=stats.norm.ppf(.95);A=n-z*z/r;coef=n*mean+z*z/2;disc=coef*coef-A*n*mean*mean;nb=[(coef-math.sqrt(disc))/A,(coef+math.sqrt(disc))/A]
def dev(mu):return 2*n*(mu-mean+mean*math.log(mean/mu))-z*z
poisLR=[optimize.brentq(dev,.01,mean),optimize.brentq(dev,mean,mean*3)]
done('10.41',{'data':aph.tolist(),'n':n,'mean':mean,'S2':v,'r_moment_estimate':r,'NB_score_plugin_r_90':nb,'NB_Wald_using_S_90':[mean-z*math.sqrt(v/n),mean+z*math.sqrt(v/n)],'Poisson_LR_asymptotic90':poisLR,'Poisson_Garwood90':[float(stats.chi2.ppf(.05,2*aph.sum())/(2*n)),float(stats.chi2.ppf(.95,2*(aph.sum()+1))/(2*n))]})
def wilson(n,z,cc=False):
 y=np.arange(n+1);p=y/n
 def root(q,sign):return (2*n*q+z*z+sign*z*np.sqrt(z*z+4*n*q*(1-q)))/(2*(n+z*z))
 if cc:
  lo=root(np.maximum(p-.5/n,0),-1);hi=root(np.minimum(p+.5/n,1),1);lo[0]=0;hi[-1]=1
 else:lo=root(p,-1);hi=root(p,1)
 return lo,hi
def ac(n,z):
 y=np.arange(n+1);p=(y+2)/(n+4);se=np.sqrt(p*(1-p)/(n+4));return np.maximum(p-z*se,0),np.minimum(p+z*se,1)
def coverage(n,p,lo,hi):
 y=np.arange(n+1);prob=stats.binom.pmf(y,n,p);return float(prob@((lo<=p)&(p<=hi)))
comparisons=[]
for n in [12,25,100]:
 for alpha in [.1,.05]:
  z=stats.norm.ppf(1-alpha/2);methods={'Wilson':wilson(n,z),'Wilson_CC':wilson(n,z,True),'Agresti_Coull_plus4':ac(n,z)}
  rows=[]
  for p in np.linspace(.001,.999,999):
   vals=[]
   for name,(lo,hi) in methods.items():
    prob=stats.binom.pmf(np.arange(n+1),n,p);vals.extend([coverage(n,p,lo,hi),float(prob@(hi-lo))])
   rows.append([p,*vals])
  save(f'10.44-n{n}-alpha{alpha}.csv',['p','Wilson_coverage','Wilson_length','CC_coverage','CC_length','AC_coverage','AC_length'],rows)
  comparisons.append({'n':n,'alpha':alpha,'selected':[{'p':p,**{name:{'coverage':coverage(n,p,lo,hi),'expected_length':float(stats.binom.pmf(np.arange(n+1),n,p)@(hi-lo))} for name,(lo,hi) in methods.items()}} for p in [.01,.1,.5]]})
done('10.44',comparisons)
counter=[]
for alpha in [.1,.05,.01]:
 for n in range(1,151):
  z=stats.norm.ppf(1-alpha/2);lo,hi=wilson(n,z,True);points=np.unique(np.r_[lo,hi]);points=points[(points>0)&(points<1)]
  points=np.clip(np.r_[points-1e-10,points+1e-10],1e-12,1-1e-12)
  for p in points:
   cov=coverage(n,p,lo,hi)
   if cov<1-alpha-1e-7:
    counter.append({'n':n,'alpha':alpha,'p':float(p),'coverage':cov});break
  if counter and counter[-1]['alpha']==alpha:break
done('10.45',{'counterexamples_to_universal_nominal_lower_bound':counter,'scope':'finite check n1..150, alpha .1,.05,.01, both sides of all interval endpoints; not a proof outside scope'})
