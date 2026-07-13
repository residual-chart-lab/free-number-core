#!/usr/bin/env python3
from __future__ import annotations
from itertools import combinations, product
from typing import Iterable, Sequence
import sympy as sp
IMAGINARY=(1,2,3)
def qmul_basis(a:int,b:int)->tuple[int,int]:
    if a==0:return 1,b
    if b==0:return 1,a
    if a==b:return -1,0
    cyclic={(1,2):3,(2,3):1,(3,1):2}
    if (a,b) in cyclic:return 1,cyclic[(a,b)]
    return -1,cyclic[(b,a)]
def multiply_word(word:Iterable[int])->tuple[int,int]:
    sign=1; value=0
    for letter in word:
        s,value=qmul_basis(value,letter); sign*=s
    return sign,value
def partial_response(word:Sequence[int], selected_gaps:Sequence[int], probes:Sequence[int])->tuple[int,int]:
    probe_at=dict(zip(selected_gaps,probes,strict=True)); expanded=[]
    for position,letter in enumerate(word,start=1):
        expanded.append(letter)
        if position<len(word) and position in probe_at: expanded.append(probe_at[position])
    return multiply_word(reversed(expanded))
def response_matrix(n:int,maximum_depth:int)->sp.Matrix:
    words=list(product(IMAGINARY,repeat=n)); rows=[]
    for depth in range(maximum_depth+1):
        for selected_gaps in combinations(range(1,n),depth):
            for probes in product(IMAGINARY,repeat=depth):
                vals=[partial_response(w,selected_gaps,probes) for w in words]
                for out in range(4): rows.append([sgn if idx==out else 0 for sgn,idx in vals])
    return sp.Matrix(rows)
def pair_basis_vector(a:int,b:int)->sp.Matrix:
    v=sp.zeros(9,1); v[3*a+b]=1; return v
def grade_two_sectors():
    metric=sum((pair_basis_vector(a,a) for a in range(3)),start=sp.zeros(9,1))
    visible=[metric]
    for a,b in ((0,1),(1,2),(2,0)): visible.append(pair_basis_vector(a,b)-pair_basis_vector(b,a))
    residual=[pair_basis_vector(0,0)-pair_basis_vector(1,1),pair_basis_vector(1,1)-pair_basis_vector(2,2),pair_basis_vector(0,1)+pair_basis_vector(1,0),pair_basis_vector(1,2)+pair_basis_vector(2,1),pair_basis_vector(2,0)+pair_basis_vector(0,2)]
    return visible,residual
def tensor_sector(left,right): return sp.Matrix.hstack(*[sp.kronecker_product(x,y) for x in left for y in right])
if __name__=='__main__':
    P,R=grade_two_sectors(); sectors={'PP':tensor_sector(P,P),'PR':tensor_sector(P,R),'RP':tensor_sector(R,P),'RR':tensor_sector(R,R)}
    totals={0:(4,77),1:(32,49),2:(72,9),3:(81,0)}
    kernels={0:{'PP':12,'PR':20,'RP':20,'RR':25},1:{'PP':0,'PR':12,'RP':12,'RR':25},2:{'PP':0,'PR':0,'RP':0,'RR':9},3:{'PP':0,'PR':0,'RP':0,'RR':0}}
    for d in range(4):
        M=response_matrix(4,d); got=(M.rank(),81-M.rank()); assert got==totals[d]
        sk={k:B.cols-(M*B).rank() for k,B in sectors.items()}; assert sk==kernels[d]
        print(d,got,sk)
    print('depth4 certificate passed')
