"""Three disjoint initializations of Kasner charts on a common torus slab."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import hankel2
P=np.array([-1/3,2/3,2/3])
times=[1.,1.5,2.]
mats=[np.eye(3),np.array([[1,1,0],[0,1,0],[0,0,1]]),np.array([[1,0,0],[0,1,1],[0,0,1]])]
offset=np.array([[0,0,0],[.21,-.33,.18],[-.17,.26,.35]])
velocity=np.array([[0,0,0],[.1,.08,0],[-.04,.12,.06]])
clocks=[1.,1.2,.8]
k=4
def datum(t):
    z=k*t**(1-P[0])/(1-P[0])
    c=np.sqrt(np.pi/(4*(1-P[0])))
    return c*hankel2(0,z),-c*k*t**(-P[0])*hankel2(1,z)
def chart(i,t,n):
    ti=times[i];M=mats[i];b=velocity[i];scale=clocks[i]
    f,ft=datum(ti)
    # Independent seed phase is an arbitrary unit scalar per chart.
    phase=np.exp(.23j*i)
    y=np.r_[ti**P,P/ti,phase*f,phase*ti*ft,0j]
    def rhs(s,y):
        t=ti+s*scale
        a=y[:3];H=y[3:6]
        return scale*np.r_[a*H,-sum(H)*H,y[7]/np.prod(a),-k*k*np.prod(a)*y[6]/a[0]**2,1/a[0]]
    ds=(t-ti)/scale/n
    for j in range(n):
        s=j*ds;a=rhs(s,y);b1=rhs(s+ds/2,y+ds*a/2);c=rhs(s+ds/2,y+ds*b1/2);d=rhs(s+ds,y+ds*c)
        y+=ds*(a+2*b1+2*c+d)/6
    a=y[:3].real;H=y[3:6].real
    J=np.eye(4);J[0,0]=scale;J[1:,0]=velocity[i]*scale;J[1:,1:]=M
    metric=J.T@np.diag(np.r_[1,-a*a])@J
    tidal=H*(H-sum(H))
    curvature=4*(sum(tidal**2)+sum((H[l]*H[m])**2 for l,m in [(0,1),(1,2),(2,0)]))
    return dict(J=J,metric=metric,r=curvature,l=y[-1].real,f=y[6],a=a)
def run():
    rows=[]
    for steps in [8,16,32,64]:
        vals={(i,t):chart(i,t,steps) for i in range(3) for t in [*times,1.27,1.73]}
        X=np.array([.48,-.21,.32]);Q=np.array([-.32,.14,.17])
        def ylocal(i,t,x):return np.linalg.solve(mats[i],x-offset[i]-velocity[i]*(t-times[i]))
        def mode(i,t,x):
            local=ylocal(i,t,x)
            # Spatial factor in the local basis and induced time-dependent translation.
            ang=(mats[i].T@np.array([k,0,0]))@local+k*(offset[i,0]+velocity[i,0]*(t-times[i]))
            return vals[i,t]['f']*np.exp(1j*ang)/(2*np.pi)**1.5
        def phase(i,t):
            f=vals[i,t]['f'];return f/abs(f)
        def ev(i):
            return phase(i,times[i])*mode(i,1.73,Q).conjugate()
        trans=np.array([[phase(j,times[i])/phase(j,times[j]) for j in range(3)] for i in range(3)])
        slabs=[(.85,2.03),(.91,2.12),(.96,2.22)]
        assert all(lo<min(times) and hi>max(times) for lo,hi in slabs)
        density_error=mixed_error=eval_trace=0.
        half=[]
        for i,ti in enumerate(times):
            data=vals[i,ti]
            mu=np.sqrt(np.linalg.det(-data['metric'][1:,1:]))
            half.append(np.sqrt(mu))
            density_error=max(density_error,abs(mu-ti))
        for i,ti in enumerate(times):
            for j,tj in enumerate(times):
                # Compute a mixed trace within the independently evolved j chart;
                # the two diagonal normalizers are measured by their own charts.
                zi=half[i]*vals[j,ti]['f'];zj=half[j]*vals[j,tj]['f']
                W_i=1/abs(half[i]*vals[i,ti]['f']);W_j=1/abs(zj)
                mix=W_i*(zi*zj.conjugate())*W_j
                mixed_error=max(mixed_error,abs(mix-trans[i,j]))
                eval_trace=max(eval_trace,abs(mix*ev(j)-ev(i)))
        geo=curv=kernel=ray=coord=wrong=0.
        for i in range(3):
            for j in range(3):
                u=vals[i,1.27];v=vals[j,1.27];D=np.linalg.solve(v['J'],u['J'])
                geo=max(geo,np.max(abs(u['metric']-D.T@v['metric']@D)))
                wrong=max(wrong,np.max(abs(u['metric']-v['metric'])))
                curv=max(curv,abs(u['r']-v['r']))
                kernel=max(kernel,abs(mode(i,1.27,X)*mode(i,1.73,Q).conjugate()-mode(j,1.27,X)*mode(j,1.73,Q).conjugate()))
                ray=max(ray,abs((vals[i,1.73]['l']-u['l'])-(vals[j,1.73]['l']-v['l'])))
                for l in range(3):
                    Dl=np.linalg.solve(vals[l,1.27]['J'],v['J'])
                    coord=max(coord,np.max(abs(Dl@D-np.linalg.solve(vals[l,1.27]['J'],u['J']))))
        rows.append(dict(steps=steps,metric=geo,curvature=curv,curvature_reference=abs(vals[1,1.27]['r']-64/(27*1.27**4)),
            ray=ray,kernel=kernel,coordinate_triples=coord,omitted_chart_change=float(wrong),half_density=density_error,normalized_mixed=mixed_error,trace_evaluation=eval_trace,
            normalized_triples=max(abs(trans[i,j]*trans[j,l]-trans[i,l]) for i in range(3) for j in range(3) for l in range(3)),
            adjoint=float(np.max(abs(trans-trans.conj().T))),evaluation=max(abs(trans[i,j]*ev(j)-ev(i)) for i in range(3) for j in range(3)),
            reversed=max(abs(trans[i,j].conjugate()*ev(j)-ev(i)) for i in range(3) for j in range(3))))
    return rows
