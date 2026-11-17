"""DS011第11章固定教材数据的ANOVA、回归、两种缺失EM与闭式核对。"""
from pathlib import Path
import json,platform
import numpy as np
import scipy
from scipy.stats import f,t,norm,multivariate_normal

def anova(groups):
    ns=np.array([len(g) for g in groups]);means=np.array([np.mean(g) for g in groups]);N=int(ns.sum());k=len(groups);grand=float(np.dot(ns,means)/N)
    ssw=float(sum(np.sum((np.array(g)-m)**2) for g,m in zip(groups,means)));ssb=float(np.sum(ns*(means-grand)**2));msw=ssw/(N-k);msb=ssb/(k-1);F=msb/msw
    pairs=[]
    for i in range(k):
        for j in range(i+1,k):
            se=np.sqrt(msw*(1/ns[i]+1/ns[j]));stat=(means[i]-means[j])/se;p=2*t.sf(abs(stat),N-k)
            pairs.append({'i':i+1,'j':j+1,'difference':float(means[i]-means[j]),'standard_error':float(se),'t':float(stat),'p_two_sided':float(p),'t_squared':float(stat**2)})
    return {'n':N,'k':k,'sizes':ns.tolist(),'means':means.tolist(),'grand_mean':grand,'SSB':ssb,'SSW':ssw,'SST':ssb+ssw,'df_between':k-1,'df_within':N-k,'df_total':N-1,'MSB':msb,'MSW':msw,'F':F,'p_F':float(f.sf(F,k-1,N-k)),'pairs':pairs,'mean_ordered_pair_t_squared':float(2*sum(z['t_squared'] for z in pairs)/(k*(k-1)))}

fish=[[28,23,14,27],[33,36,34,29,31,34],[18,21,20,22,24],[11,14,11,16]]
rats=[[3.89,3.87,3.26,2.70,3.82],[8.54,9.32,8.76,9.30,10.45],[20.39,24.22,30.91,22.78,26.33]]

def regression(x,y):
    x=np.array(x,dtype=float);y=np.array(y,dtype=float);n=len(x);xc=x-x.mean();yc=y-y.mean();Sxx=float(xc@xc);Sxy=float(xc@yc);Syy=float(yc@yc);b=Sxy/Sxx;a=float(y.mean()-b*x.mean());sse=float(np.sum((y-a-b*x)**2));ssr=Sxy**2/Sxx;F=ssr/(sse/(n-2))
    return {'n':n,'xbar':float(x.mean()),'ybar':float(y.mean()),'Sxx':Sxx,'Sxy':Sxy,'Syy':Syy,'intercept':a,'slope':b,'SSE':sse,'SSR':ssr,'SST':Syy,'sigma2_MLE':sse/n,'MS_error':sse/(n-2),'df_regression':1,'df_error':n-2,'df_total':n-1,'F':F,'p_F':float(f.sf(F,1,n-2)),'r_squared':ssr/Syy}

height_x=[39,30,32,34,35,36,36,30];height_y=[71,63,63,67,68,68,70,64]
ox=np.array([20,19.6,19.6,19.4,18.4,19,19,18.3,18.2,18.6,19.2,18.2,18.7,18.5,18,17.4,16.5,17.2,17.3,17.8,17.3,18.4,16.9],dtype=float)
co=np.array([1,1.2,1.1,1.4,2.3,1.7,1.7,2.4,2.1,2.1,1.2,2.3,1.9,2.4,2.6,2.9,4,3.3,3,3.4,2.9,1.9,3.9],dtype=float)

def em_missing_y():
    xx=np.r_[ox,16.3];design=np.column_stack([np.ones(24),xx]);xtx=design.T@design
    coef=np.array([18.,-.8]);q=1.;hist=[]
    for it in range(10000):
        missing_mean=coef@design[-1];ey=np.r_[co,missing_mean];ey2=float(co@co+q+missing_mean**2)
        xty=design.T@ey;cn=np.linalg.solve(xtx,xty);qn=float((ey2-2*cn@xty+cn@xtx@cn)/24)
        err=max(np.max(abs(cn-coef)),abs(qn-q));coef,q=cn,qn
        hist.append(float(np.sum(norm.logpdf(co,coef[0]+coef[1]*ox,np.sqrt(q)))))
        if err<1e-11:break
    assert min(np.diff(hist))>=-1e-8
    closed=regression(ox,co);assert abs(coef[0]-closed['intercept'])<1e-8 and abs(q-closed['sigma2_MLE'])<1e-8
    return {'initial_parameters':{'intercept':18.,'slope':-.8,'sigma2':1.},'stopping_rule':'maximum absolute change of the three parameters < 1e-11','maximum_iterations':10000,'log_likelihood_recording':'after each complete E/M update','iterations':it+1,'intercept':float(coef[0]),'slope':float(coef[1]),'sigma2':q,'missing_y_conditional_mean':float(coef@design[-1]),'final_absolute_change':float(err),'first_log_likelihood':hist[0],'last_log_likelihood':hist[-1],'min_step':float(min(np.diff(hist)))}

def em_missing_x():
    z=np.column_stack([ox,co]);mu=z.mean(0);cov=np.cov(z.T,bias=True);hist=[]
    for it in range(10000):
        ex=mu[0]+cov[0,1]/cov[1,1]*(4.2-mu[1]);vx=cov[0,0]-cov[0,1]**2/cov[1,1]
        exz=np.array([ex,4.2]);outer=np.array([[vx+ex**2,ex*4.2],[ex*4.2,4.2**2]])
        mn=(z.sum(0)+exz)/24;cn=(z.T@z+outer)/24-np.outer(mn,mn)
        err=max(np.max(abs(mn-mu)),np.max(abs(cn-cov)));mu,cov=mn,cn
        ll=float(np.sum(multivariate_normal.logpdf(z,mean=mu,cov=cov))+norm.logpdf(4.2,mu[1],np.sqrt(cov[1,1])));hist.append(ll)
        if err<1e-11:break
    assert min(np.diff(hist))>=-1e-8
    beta=cov[0,1]/cov[0,0];alpha=mu[1]-beta*mu[0];q=cov[1,1]-cov[0,1]**2/cov[0,0]
    reverse=regression(co,ox);all_y=np.r_[co,4.2];my=float(all_y.mean());vy=float(np.var(all_y));bx=reverse['slope'];ax=reverse['intercept'];qx=reverse['sigma2_MLE'];mx=ax+bx*my;vxy=bx*vy;vxx=qx+bx**2*vy
    assert np.max(np.abs(mu-np.array([mx,my])))<1e-8 and np.max(np.abs(cov-np.array([[vxx,vxy],[vxy,vy]])))<1e-8
    return {'initial_parameters':'joint bivariate-normal MLE from the 23 complete pairs; covariance denominator 23','stopping_rule':'maximum absolute change over mean and covariance entries < 1e-11','maximum_iterations':10000,'log_likelihood_recording':'after each complete E/M update','iterations':it+1,'joint_mean':mu.tolist(),'joint_covariance_MLE':cov.tolist(),'intercept_y_on_x':float(alpha),'slope_y_on_x':float(beta),'sigma2_y_given_x':float(q),'missing_x_conditional_mean':float(mu[0]+cov[0,1]/cov[1,1]*(4.2-mu[1])),'missing_x_conditional_variance':float(cov[0,0]-cov[0,1]**2/cov[1,1]),'final_absolute_change':float(err),'first_log_likelihood':hist[0],'last_log_likelihood':hist[-1],'min_step':float(min(np.diff(hist))),'reverse_regression_closed_form':{'x_given_y':reverse,'marginal_y_mean_all24':my,'marginal_y_variance_all24':vy,'joint_mean':[mx,my],'joint_covariance':[[vxx,vxy],[vxy,vy]]}}

out={'environment':{'python':platform.python_version(),'scipy':scipy.__version__,'numpy':np.__version__,'randomness':'none'},'11.17':{'data':fish,'ANOVA':anova(fish),'alpha_for_report':.05,'t_critical':float(t.isf(.025,15))},'11.21':{'data':rats,'ANOVA':anova(rats)},'11.34':{'x':height_x,'y':height_y,'fit':regression(height_x,height_y)},'11.41':{'O2':ox.tolist(),'CO2':co.tolist(),'complete23_regression':regression(ox,co),'case_c_O2_16_3_y_missing':em_missing_y(),'case_d_CO2_4_2_x_missing':em_missing_x()},'scope':'原书固定数据、确定性解析拟合与指定初值EM的实际核验；没有随机模拟。表11.2.1式数据位于PDF453；Potoroo表12.4.2位于PDF516，均逐项目视核对。'}
Path(__file__).with_name('ch11-numeric-results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for key in ['11.17','11.21','11.34','11.41']:print(key,json.dumps(out[key],ensure_ascii=False))
