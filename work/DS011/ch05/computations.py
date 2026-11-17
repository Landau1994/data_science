"""Independent finite computations for DS011 chapter 5. Run from vault root."""
from pathlib import Path
import json,math,platform,csv
import numpy as np
import scipy
from scipy import stats,special,integrate
import mpmath as mp
OUT=Path(__file__).parent
OUT.mkdir(parents=True,exist_ok=True)
results={'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'mpmath':mp.__version__},'rng':'numpy.default_rng / PCG64','seed_policy':'separate fixed seed for each exercise; not a cross-platform bitwise guarantee'}
def table(name,header,rows):
    with (OUT/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.writer(f);w.writerow(header);w.writerows(rows)
def summary(x):return {'n':len(x),'mean':float(np.mean(x)),'sample_variance':float(np.var(x,ddof=1)),'quantiles_025_50_975':np.quantile(x,[.025,.5,.975]).tolist()}
mu=60/7;sd=math.sqrt(600/49)
rows=[]
for v in range(11):
    rows.append([v,stats.nbinom.pmf(v,20,.7),stats.norm.cdf((v-mu)/sd)-stats.norm.cdf((v-1-mu)/sd),stats.norm.pdf((v-mu)/sd)/sd,stats.norm.cdf((v+.5-mu)/sd)-stats.norm.cdf((v-.5-mu)/sd)])
table('5.37-probabilities.csv',['v','exact','normal_cdf_difference','normal_local_density','continuity_corrected'],rows)
results['5.37']=rows
mp.mp.dps=70
life=[]
for c,a in [(300,mp.mpf(4)),(100,mp.mpf(20)),(100,mp.mpf('20.7'))]:
    p=mp.gammainc(a,30,mp.inf)/mp.gamma(a);t=math.ceil(.75*c)
    tail=sum(mp.binomial(c,k)*p**k*(1-p)**(c-k) for k in range(t,c+1))
    z0=(t-c*p)/mp.sqrt(c*p*(1-p));zc=(t-mp.mpf('.5')-c*p)/mp.sqrt(c*p*(1-p))
    norm0=mp.erfc(z0/mp.sqrt(2))/2;normc=mp.erfc(zc/mp.sqrt(2))/2
    life.append({'c':c,'a':str(a),'b':5,'p_survive':mp.nstr(p,18),'at_least':t,'exact_probability':mp.nstr(tail,18),'exact_log10':mp.nstr(mp.log10(tail),18),'normal':mp.nstr(norm0,18),'normal_log10':mp.nstr(mp.log10(norm0),18),'normal_cc':mp.nstr(normc,18),'normal_cc_log10':mp.nstr(mp.log10(normc),18)})
results['5.45-46']=life
# 5.53: implement the uniform algorithms of 5.52, rather than use ready-made samplers.
rng=np.random.default_rng(2026111353)
b=(rng.random((1000,8))<2/3).sum(axis=1)
h=np.empty(1000,dtype=int)
for k in range(1000):
    good=8;total=10;score=0
    for j in range(4):
        success=rng.random()<good/total;score+=success;good-=success;total-=1
    h[k]=score
nb=np.empty(1000,dtype=int)
for k in range(1000):
    success=fail=0
    while success<5:
        if rng.random()<1/3:success+=1
        else:fail+=1
    nb[k]=fail
table('5.53-samples.csv',['binomial','hypergeometric','negative_binomial'],zip(b,h,nb))
vals={}
for name,x,dist in [('binomial',b,stats.binom(8,2/3)),('hypergeometric',h,stats.hypergeom(10,8,4)),('negative_binomial',nb,stats.nbinom(5,1/3))]:
    ks=np.arange(0,max(x.max(),int(dist.ppf(.9999)))+1)
    table('5.53-'+name+'-frequency.csv',['x','empirical','theoretical'],zip(ks,[(x==k).mean() for k in ks],dist.pmf(ks)))
    vals[name]={**summary(x),'theoretical_mean':dist.mean(),'theoretical_variance':dist.var()}
results['5.53']={'seed':2026111353,'samples':vals}
# 5.54: plug-in model comparison; declared consistency rule is central 95% of S^2.
fish=np.array([158,143,106,57,97,80,109,109,350,224,109,214,84])
fishmean=float(fish.mean());fishvar=float(fish.var(ddof=1));B=50000;rng=np.random.default_rng(2026111354)
grid=[.5,1,2,3,4,5,6,8,10,15,20,30,50,100]
rv=rng.poisson(fishmean,size=(B,13)).var(axis=1,ddof=1)
pois={'n_simulations':B,'mean_sample_variance':float(rv.mean()),'interval_025_975':np.quantile(rv,[.025,.975]).tolist(),'exceedance_count':int((rv>=fishvar).sum()),'plus_one_tail':float((1+(rv>=fishvar).sum())/(B+1))}
table('5.54-poisson-variance.csv',['variance'],zip(rv))
scan=[]
for r in grid:
    p=r/(r+fishmean);v=rng.negative_binomial(r,p,size=(B,13)).var(axis=1,ddof=1)
    lo,hi=np.quantile(v,[.025,.975]);consistent=bool(lo<=fishvar<=hi)
    scan.append({'r':r,'p':p,'interval_025_975':[float(lo),float(hi)],'upper_tail':float((v>=fishvar).mean()),'consistent':consistent})
    table(f'5.54-nb-r{r}-variance.csv',['variance'],zip(v))
results['5.54']={'seed':2026111354,'data':fish.tolist(),'mean':fishmean,'sample_variance':fishvar,'moment_r':fishmean**2/(fishvar-fishmean),'replicates_per_model':B,'rule':'observed variance inside central 95% of fitted-model variance simulation','poisson':pois,'nb_grid':scan}
# 5.58: iid renewal waiting times, using independent uniforms until sum exceeds 1.
rng=np.random.default_rng(2026111358);B=1000000
s=np.zeros(B);N=np.zeros(B,dtype=int);active=np.arange(B)
while len(active):
    s[active]+=rng.random(len(active));N[active]+=1;active=active[s[active]<=1]
table('5.58-waiting-times.csv',['N'],zip(N))
v=3*math.e-math.e**2
results['5.58']={'seed':2026111358,**summary(N),'exact_variance':v,'se':math.sqrt(v/B),'normal_95_interval':[float(N.mean()-stats.norm.ppf(.975)*math.sqrt(v/B)),float(N.mean()+stats.norm.ppf(.975)*math.sqrt(v/B))],'n_clt_error_00005':math.ceil(stats.norm.ppf(.975)**2*v/(.00005**2)),'n_chebyshev_error_00005':math.ceil(v/(.05*.00005**2)),'n_clt_error_0005':math.ceil(stats.norm.ppf(.975)**2*v/(.0005**2))}
# 5.61: all legal positive-integer beta candidates, exact finite supremum.
def beta_M(a,b,m,n):
    p=a-m;q=b-n
    logterm=(p*math.log(p) if p else 0)+(q*math.log(q) if q else 0)-((p+q)*math.log(p+q) if p+q else 0)
    return math.exp(special.betaln(m,n)-special.betaln(a,b)+logterm)
ab=(1.9,10.1);candidates=[(m,n,beta_M(*ab,m,n)) for m in range(1,math.floor(ab[0])+1) for n in range(1,math.floor(ab[1])+1)]
results['5.61']={'example_ab':ab,'candidates':candidates,'best':min(candidates,key=lambda z:z[2]),'double_floor':candidates[-1]}
# 5.66: retain every generated median; exact density/quantiles for independent comparison.
rng=np.random.default_rng(2026111366);B=200000;n=15
med=np.median(rng.standard_normal((B,n)),axis=1)
table('5.66-medians.csv',['median'],zip(med))
def medpdf(x):
    c=math.factorial(15)/(math.factorial(7)**2);F=stats.norm.cdf(x)
    return c*F**7*(1-F)**7*stats.norm.pdf(x)
exactvar=integrate.quad(lambda x:x*x*medpdf(x),-9,9,epsabs=1e-12)[0]
exactq=stats.norm.ppf(stats.beta.ppf([.025,.5,.975],8,8));asympsd=math.sqrt(math.pi/30)
cut=stats.norm.ppf(.975)*asympsd
edges=np.linspace(-1.4,1.4,71);counts,_=np.histogram(med,edges)
centers=(edges[:-1]+edges[1:])/2
table('5.66-density.csv',['x','empirical_density','exact_density','asymptotic_density'],zip(centers,counts/(B*np.diff(edges)),[medpdf(x) for x in centers],stats.norm.pdf(centers,scale=asympsd)))
results['5.66']={'seed':2026111366,'n_per_sample':15,'replicates':B,**summary(med),'exact_variance':exactvar,'exact_quantiles':exactq.tolist(),'asymptotic_variance':asympsd**2,'asymptotic_quantiles':stats.norm.ppf([.025,.5,.975],scale=asympsd).tolist(),'simulated_coverage_of_asymptotic_95':float((abs(med)<=cut).mean()),'exact_coverage_of_asymptotic_95':float(stats.beta.cdf(stats.norm.cdf(cut),8,8)-stats.beta.cdf(stats.norm.cdf(-cut),8,8))}
# 5.68: three explicitly separated streams per nu; all retained values saved.
methods=[]
for nu in [2,10,25]:
    rng=np.random.default_rng(2026111368+nu);burn=5000;Nkeep=100
    z=float(rng.standard_normal());mh=[];acc=0;keptacc=0
    for i in range(burn+Nkeep):
        proposal=float(rng.standard_normal())
        logratio=stats.t.logpdf(proposal,nu)-stats.norm.logpdf(proposal)-stats.t.logpdf(z,nu)+stats.norm.logpdf(z)
        accepted=math.log(rng.random())<min(0,logratio)
        if accepted:z=proposal;acc+=1;keptacc+=i>=burn
        if i>=burn:mh.append(z)
    rng=np.random.default_rng(2026111468+nu);ar=[];attempts=0
    M=math.pi*2*math.exp(special.gammaln((nu+1)/2)-special.gammaln(nu/2))/math.sqrt(nu*math.pi)*(1+1/nu)**(-(nu+1)/2)
    while len(ar)<Nkeep:
        proposal=math.tan(math.pi*(rng.random()-.5));attempts+=1
        ratio=stats.t.pdf(proposal,nu)/(M*stats.cauchy.pdf(proposal))
        assert ratio<=1+1e-12
        if rng.random()<=ratio:ar.append(proposal)
    rng=np.random.default_rng(2026111568+nu);direct=rng.standard_normal(Nkeep)/np.sqrt(rng.chisquare(nu,Nkeep)/nu)
    table(f'5.68-nu{nu}-samples.csv',['index','metropolis','accept_reject','direct'],zip(range(1,101),mh,ar,direct))
    models=[]
    for label,x in [('metropolis',np.array(mh)),('accept_reject',np.array(ar)),('direct',direct)]:
        models.append({'method':label,**summary(x),'tail_abs_gt2':float((abs(x)>2).mean()),'lag1_correlation':float(np.corrcoef(x[:-1],x[1:])[0,1]),'empirical_cdf_sup_distance':float(stats.kstest(x,stats.t(nu).cdf).statistic)})
    methods.append({'nu':nu,'seeds':[2026111368+nu,2026111468+nu,2026111568+nu],'burn_in':burn,'retained':100,'mh_total_acceptance':acc/(burn+Nkeep),'mh_retained_acceptance':keptacc/100,'ar_M':M,'ar_attempts':attempts,'ar_theoretical_acceptance':1/M,'theoretical_tail_abs_gt2':float(2*stats.t.sf(2,nu)),'samples':models})
results['5.68']=methods
(OUT/'results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:results[k] for k in ['environment','5.45-46','5.53','5.54','5.58','5.61','5.66','5.68']},ensure_ascii=False,indent=2))
