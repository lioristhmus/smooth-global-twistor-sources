"""Propagate the two shifted peaks on a nonflat Kasner axis by a Cauchy solve."""
import numpy as np
from scipy.special import hankel2
from waves import bump
def run():
    t=1.23;shift=1.2;x=np.linspace(-np.pi,np.pi,8192,endpoint=False)
    wrap=lambda z:(z+np.pi)%(2*np.pi)-np.pi
    total=[]
    for p in [-1/3,2/3]:
        eta=(t**(1-p)-1)/(1-p);k=np.arange(1,769)
        def f(t):return hankel2(0,k*t**(1-p)/(1-p))
        u=f(t)/f(1)
        v0=-k*hankel2(1,k/(1-p))/f(1)
        tests=[bump(wrap(x-eta-center),.36) for center in [0,shift,-shift]]
        four=np.array([np.mean(w)*np.ones(1) for w in tests])[:,0]
        hat=np.array([np.conj(np.fft.fft(np.fft.ifftshift(w))/len(x))[k] for w in tests])
        def pairs(v):
            j=len(v)
            return 2*four+4*np.real(hat[:,:j]@(v*np.cos(k[:j]*shift)))
        ref=pairs(u)
        for N in [16,32,64,128,256]:
            modes=k[:N];fval=np.ones(N,complex);v=v0[:N].copy()
            nstep=4*N;dt=(t-1)/nstep
            def rhs(s,f,v):return v/s,-modes**2*s**(1-2*p)*f
            for i in range(nstep):
                s=1+i*dt
                a,b=rhs(s,fval,v);c,d=rhs(s+dt/2,fval+dt*a/2,v+dt*b/2)
                e,f1=rhs(s+dt/2,fval+dt*c/2,v+dt*d/2);h,j=rhs(s+dt,fval+dt*e,v+dt*f1)
                fval+=dt*(a+2*c+2*e+h)/6;v+=dt*(b+2*d+2*f1+j)/6
            around=np.linspace(eta+shift-.18,eta+shift+.18,1501)
            envelope=np.real(np.exp(1j*around[:,None]*modes)@(fval*np.cos(modes*shift)))
            total.append(dict(p=p,N=N,eta=eta,ode_error=float(np.max(abs(fval-u[:N]))),
                pair=pairs(fval).tolist(),reference768=ref.tolist(),pair_error=float(np.max(abs(pairs(fval)-ref))),
                peak_shift=float(around[np.argmax(envelope)]-eta-shift),wrong_branch_error=float(np.max(abs(pairs(fval.conj())-ref)))))
    return total
