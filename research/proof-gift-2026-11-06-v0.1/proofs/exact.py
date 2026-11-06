"""Exact matrix, quaternion and Gaussian-rational helpers; no optional libraries."""
from fractions import Fraction as F
from dataclasses import dataclass

def mat(rows):return [[x if isinstance(x,C) else F(x) for x in row] for row in rows]
def zero(n,m=None):return [[F(0) for _ in range(m or n)] for _ in range(n)]
def eye(n):return mat([[int(i==j) for j in range(n)] for i in range(n)])
def tp(a):return [list(r) for r in zip(*a)]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def sc(k,a):return [[k*x for x in r] for r in a]
def sub(a,b):return add(a,sc(-1,b))
def mm(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def comm(a,b):return sub(mm(a,b),mm(b,a))
def tr(a):return sum(a[i][i] for i in range(len(a)))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def norm2(a):return sum(x*x for r in a for x in r)
def conj(g,a):return mm(mm(g,a),tp(g))
def flat(a):return [x for r in a for x in r]
def basis_skew(n):
    ans=[]
    for p in range(n):
        for q in range(p+1,n):
            k=zero(n);k[q][p]=1;k[p][q]=-1;ans.append(k)
    return ans
def axial(a):return [a[q][p] for p in range(len(a)) for q in range(p+1,len(a))]
def lin(cs,bs):
    ans=zero(len(bs[0]))
    for c,b in zip(cs,bs):ans=add(ans,sc(c,b))
    return ans
def diag(values):return mat([[v if i==j else 0 for j in range(len(values))] for i,v in enumerate(values)])
def rotation(n,p,q,c=F(3,5),s=F(4,5)):
    g=eye(n);g[p][p]=g[q][q]=c;g[p][q]=-s;g[q][p]=s;return g
def rref(rows,rhs,n):
    a=[[F(x) for x in r]+[F(b)] for r,b in zip(rows,rhs)];piv=[];k=0
    for j in range(n):
        ix=next((r for r in range(k,len(a)) if a[r][j]),None)
        if ix is None:continue
        a[k],a[ix]=a[ix],a[k];v=a[k][j];a[k]=[x/v for x in a[k]]
        for r in range(len(a)):
            if r!=k and a[r][j]:
                v=a[r][j];a[r]=[x-v*y for x,y in zip(a[r],a[k])]
        piv.append(j);k+=1
    if any(not any(r[:n]) and r[n] for r in a):raise ValueError('Inconsistent exact system')
    x=[F(0)]*n
    for i,j in enumerate(piv):x[j]=a[i][n]
    null=[]
    for j in range(n):
        if j in piv:continue
        z=[F(0)]*n;z[j]=1
        for i,p in enumerate(piv):z[p]=-a[i][j]
        null.append(z)
    assert all(dot(r,x)==b for r,b in zip(rows,rhs))
    assert all(all(dot(r,z)==0 for r in rows) for z in null)
    return x,null,len(piv)
def solve(rows,rhs):
    x,null,_=rref(rows,rhs,len(rows[0]));assert not null;return x
def inverse(a):return tp([solve(a,[F(i==j) for i in range(len(a))]) for j in range(len(a))])

@dataclass(frozen=True,eq=False)
class C:
    r:F=F(0)
    i:F=F(0)
    def __post_init__(self):object.__setattr__(self,'r',F(self.r));object.__setattr__(self,'i',F(self.i))
    @staticmethod
    def of(x):return x if isinstance(x,C) else C(F(x))
    def __add__(self,x):x=C.of(x);return C(self.r+x.r,self.i+x.i)
    __radd__=__add__
    def __neg__(self):return C(-self.r,-self.i)
    def __sub__(self,x):return self+-C.of(x)
    def __rsub__(self,x):return C.of(x)+-self
    def __mul__(self,x):x=C.of(x);return C(self.r*x.r-self.i*x.i,self.r*x.i+self.i*x.r)
    __rmul__=__mul__
    def conjugate(self):return C(self.r,-self.i)
    def __eq__(self,x):
        if not isinstance(x,(C,F,int)):return False
        x=C.of(x);return self.r==x.r and self.i==x.i

QB=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
def qm(a,b):
    w,x,y,z=a;v,p,q,r=b
    return (w*v-x*p-y*q-z*r,w*p+x*v+y*r-z*q,w*q-x*r+y*v+z*p,w*r+x*q-y*p+z*v)
def qc(a):return (a[0],-a[1],-a[2],-a[3])
def qadd(a,b):return tuple(x+y for x,y in zip(a,b))
def qscale(c,a):return tuple(c*x for x in a)
def adj(q):
    return tp([list(qm(qm(q,e),qc(q))[1:]) for e in QB[1:]])

def pack(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,C):return [str(x.r),str(x.i)]
    if isinstance(x,dict):return {str(k):pack(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [pack(v) for v in x]
    return x
