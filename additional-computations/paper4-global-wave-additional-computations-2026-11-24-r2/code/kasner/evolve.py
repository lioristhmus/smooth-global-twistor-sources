"""Classical RK4 for f and the canonical momentum t f'. No Bessel evaluations."""
def march(t,u,v,T,p,k,n):
    h=(T-t)/n
    def rhs(s,a,b):return b/s,-k*k*s**(1-2*p)*a
    for j in range(n):
        s=t+j*h
        a,b=rhs(s,u,v);c,d=rhs(s+h/2,u+h*a/2,v+h*b/2)
        e,f=rhs(s+h/2,u+h*c/2,v+h*d/2);g,l=rhs(s+h,u+h*e,v+h*f)
        u+=h*(a+2*c+2*e+g)/6;v+=h*(b+2*d+2*f+l)/6
    return u,v
