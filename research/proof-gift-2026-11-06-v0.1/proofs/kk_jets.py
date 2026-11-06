"""Independent exact Euler-Lagrange evaluation via second-order rational jets."""
from exact import F,zero,eye,mat,mm,inverse,dot,solve

class Jet:
    def __init__(self,value,gradient,hessian):self.v=F(value);self.g=gradient;self.h=hessian
    @classmethod
    def const(cls,value,n):return cls(value,[F(0)]*n,zero(n))
    @classmethod
    def variable(cls,value,index,n):
        j=cls.const(value,n);j.g[index]=F(1);return j
    def of(self,x):return x if isinstance(x,Jet) else Jet.const(x,len(self.g))
    def __add__(self,x):
        x=self.of(x);n=len(self.g)
        return Jet(self.v+x.v,[a+b for a,b in zip(self.g,x.g)],[[self.h[i][j]+x.h[i][j] for j in range(n)] for i in range(n)])
    __radd__=__add__
    def __neg__(self):return self*F(-1)
    def __sub__(self,x):return self+-self.of(x)
    def __rsub__(self,x):return self.of(x)+-self
    def __mul__(self,x):
        x=self.of(x);n=len(self.g)
        return Jet(self.v*x.v,[self.v*x.g[i]+x.v*self.g[i] for i in range(n)],
                   [[self.v*x.h[i][j]+x.v*self.h[i][j]+self.g[i]*x.g[j]+x.g[i]*self.g[j] for j in range(n)] for i in range(n)])
    __rmul__=__mul__
    def inverse(self):
        n=len(self.g);v=self.v
        return Jet(1/v,[-x/v**2 for x in self.g],[[2*self.g[i]*self.g[j]/v**3-self.h[i][j]/v**2 for j in range(n)] for i in range(n)])
    def __truediv__(self,x):return self*self.of(x).inverse()
    def __rtruediv__(self,x):return self.of(x)*self.inverse()
    def __pow__(self,k):
        if k<0:return self.inverse()**(-k)
        ans=self.of(1)
        for _ in range(k):ans=ans*self
        return ans

def el_acceleration(lagrangian,nq,vel,count=None):
    count=count or nq
    rows=[[lagrangian.h[nq+i][nq+j] for j in range(count)] for i in range(count)]
    rhs=[lagrangian.g[i]-sum(lagrangian.h[nq+i][j]*vel[j] for j in range(nq)) for i in range(count)]
    return solve(rows,rhs)

def background(d,trial,gauged=False):
    nq=d+1;nvar=2*nq;kappa=F(2+trial,5);p=F(1+trial,7)
    vel=[F(i+2,2*i+5) for i in range(d)]
    # At q=0: phi=2 and A_mu=(mu+1)/7.
    chig=[F(2*i-1,13) for i in range(d)]
    chih=[[F((i+j+2)%5-2,17) for j in range(d)] for i in range(d)]
    av=[F(i+1,7)+(chig[i] if gauged else 0) for i in range(d)]
    w=p/4-kappa*dot(av,vel);vel5=vel+[w]
    q=[Jet.variable(0,i,nvar) for i in range(nq)]
    u=[Jet.variable(v,nq+i,nvar) for i,v in enumerate(vel5)]
    metric=[]
    for i in range(d):
        row=[]
        for j in range(d):
            value=F(-1 if i==j==0 else int(i==j))
            x=Jet.const(value,nvar)
            for k in range(d):x=x+q[k]*F((i+j+k+trial)%7-3,19)+q[k]*q[k]*F((i+j+k)%3+1,23)
            row.append(x)
        metric.append(row)
    phi=2+sum(q[i]*F(i+1,11)+q[i]*q[i]*F(1,i+5) for i in range(d))
    avec=[]
    for i in range(d):
        a=F(i+1,7)+sum(q[j]*F(((i+1)*(j+2)+trial)%7-3,11)+q[j]*q[j]*F(i+j+1,29) for j in range(d))
        if gauged:a=a+chig[i]+sum(chih[i][j]*q[j] for j in range(d))
        avec.append(a)
    kinetic=sum(metric[i][j]*u[i]*u[j]/2 for i in range(d) for j in range(d))
    au=sum(avec[i]*u[i] for i in range(d));fiber=u[d]+kappa*au
    l5=kinetic+phi**2*fiber**2/2
    routh=kinetic+kappa*p*au-p*p/(2*phi**2)
    return locals()

def check_kk():
    records=[];projection=True;gauge=True
    for d in [2,3,4]:
        for trial in [0,1]:
            b=background(d,trial);nq=b['nq'];v=b['vel'];v5=b['vel5'];g=b['metric'];a=b['avec'];phi=b['phi'];p=b['p'];k=b['kappa']
            full=el_acceleration(b['l5'],nq,v5);reduced=el_acceleration(b['routh'],nq,v5,d)
            inv=inverse([[g[i][j].v for j in range(d)] for i in range(d)])
            expected=[]
            for mu in range(d):
                connection=sum(F(1,2)*inv[mu][sig]*(g[sig][rho].g[nu]+g[sig][nu].g[rho]-g[nu][rho].g[sig])*v[nu]*v[rho]
                               for sig in range(d) for nu in range(d) for rho in range(d))
                lorentz=k*p*sum(inv[mu][sig]*(a[nu].g[sig]-a[sig].g[nu])*v[nu] for sig in range(d) for nu in range(d))
                scalar=p*p/phi.v**3*sum(inv[mu][sig]*phi.g[sig] for sig in range(d))
                expected.append(-connection+lorentz+scalar)
            lift=-2*p/phi.v**3*sum(phi.g[i]*v[i] for i in range(d))-k*(sum(a[i].g[j]*v[i]*v[j] for i in range(d) for j in range(d))+sum(a[i].v*full[i] for i in range(d)))
            projection &= full[:d]==reduced==expected and full[d]==lift and b['l5'].g[nq+d]==p
            bg=background(d,trial,True);fullg=el_acceleration(bg['l5'],nq,bg['vel5'])
            expected_y=full[d]-k*(dot(b['chig'],full[:d])+sum(b['chih'][i][j]*v[i]*v[j] for i in range(d) for j in range(d)))
            gauge &= fullg[:d]==full[:d] and fullg[d]==expected_y and bg['l5'].v==b['l5'].v
            records.append({'base_dimension':d,'trial':trial,'p':p,'phi':phi.v,'full_projected_acceleration':full[:d],
                            'Routh_acceleration':reduced,'independent_field_formula':expected,'lift_acceleration':lift,
                            'gauge_extra_coordinate_acceleration':fullg[d],'exact':full[:d]==reduced==expected})
    return {'projection_and_lift':projection,'gauge':gauge,'cases':records,
            'method':'Exact second-order multivariate automatic differentiation of the full and Routh Lagrangians, separately solved Euler-Lagrange systems; polynomial x-dependent metric/A/phi and quadratic gauge functions.'}
