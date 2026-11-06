"""Specify B2 driver paths. The runtime receives tensors, not edge rotations."""
from pathlib import Path
import json
import sys
from fractions import Fraction as F
sys.path.insert(0, str(Path(__file__).resolve().parent))
from b2 import outer, scale, packed

root = Path(__file__).resolve().parent
x, y, z = (F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(0), F(0), F(1))
forward = [x, (F(3,5), F(4,5), F(0)), y, (F(0), F(3,5), F(4,5)),
           z, (F(4,5), F(0), F(3,5)), x]
alternative = [x, (F(5,13), F(12,13), F(0)), y,
               (F(0), F(5,13), F(12,13)), z, (F(12,13), F(0), F(5,13)), x]
upper = [x, (F(3,5), F(4,5), F(0)), y]
lower = [x, (F(3,5), F(-4,5), F(0)), tuple(-v for v in y)]
cases = {}

def put(name, points, amplitudes=None):
    aa = amplitudes or [F(1)] * len(points)
    cases[name] = [scale(a, outer(n, n)) for a, n in zip(aa, points)]

put("forward_triangle", forward)
put("reverse_triangle", list(reversed(forward)))
put("other_subdivision", alternative)
put("backtrack", forward + list(reversed(forward))[1:])
put("varying_amplitude", forward, [F(1), F(2), F(1,2), F(3,2), F(1), F(4), F(1)])
put("negative_amplitude", forward, [F(-1,2)] * len(forward))
put("constant_axis", [x] * len(forward), [F(1), F(2), F(1,2), F(3,2), F(1), F(4), F(1)])
put("arc_upper", upper)
put("arc_lower", lower)
put("sign_flipped_directions", [tuple(-v for v in n) for n in forward])
put("repeated_sample", forward[:2] + [forward[1]] + forward[2:])
payload = {"cases": packed(cases), "data": "Only B2 tensors; no rotation links, eigenvectors or signed direction metadata used by the generator."}
out = root / "INPUT.json"
with out.open("xb") as stream:
    stream.write((json.dumps(payload, indent=2) + "\n").encode("utf-8"))
print(str(out))
