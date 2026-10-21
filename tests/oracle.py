"""Small dense reference only for tests: expands tensors before observation.

Does not import runtime quaternion arithmetic, the compiler, or its polynomial
representation. This deliberately takes the expensive path the runtime avoids.
"""
from fractions import Fraction
from itertools import product

Q = Fraction


def multiply(x,y):
    a,b,c,d = x
    e,f,g,h = y
    return (a*e-b*f-c*g-d*h, a*f+b*e+c*h-d*g,
            a*g-b*h+c*e+d*f, a*h+b*g-c*f+d*e)


def dense(node, values):
    if node.kind == 'block':
        return dict(node.data)
    if node.kind == 'concat':
        a,b = (dense(c,values) for c in node.children)
        return {u+v:x*y for u,x in a.items() for v,y in b.items()}
    if node.kind == 'scale':
        return {w:node.data[0]*x for w,x in dense(node.children[0],values).items()}
    a,b = (dense(c,values) for c in node.children)
    factor = values[node.data[0].key] if node.kind == 'retained' else Q(1)
    return {w:a.get(w,0)+factor*b.get(w,0) for w in a.keys()|b.keys()}


def sample(tensor,gaps):
    out = [Q(0)]*4
    for word,coefficient in tensor.items():
        v = (Q(1),Q(0),Q(0),Q(0))
        for i,letter in enumerate(word):
            if i and gaps[i-1] is not None:
                v = multiply((Q(0),)+gaps[i-1],v)
            v = multiply(tuple(Q(k==letter+1) for k in range(4)),v)
        out = [a+coefficient*b for a,b in zip(out,v)]
    return tuple(out)


def circuit(node,values):
    if node.kind == 'constant':
        return node.data[0]
    if node.kind == 'read':
        tensor,obs = node.data
        expanded = dense(tensor,values)
        out = [Q(0)]*4
        for channel in obs.channels:
            v = multiply(multiply(channel.left,sample(expanded,channel.gaps)),channel.right)
            out = [a+channel.weight*b for a,b in zip(out,v)]
        return tuple(out)
    a,b = (circuit(c,values) for c in node.children)
    return multiply(a,b) if node.kind == 'mul' else tuple(x+y for x,y in zip(a,b))
