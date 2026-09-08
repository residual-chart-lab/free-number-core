#!/usr/bin/env python3
"""Targeted exact check; this does not reconstruct the n=6 chart atlas."""
from pathlib import Path
import sys
import numpy as np
# This path works in the extracted snapshot layout.
p=Path(__file__).resolve().parents[1]/'certificates'
if not p.exists(): p=Path(__file__).resolve().parents[3]/'certificates'
sys.path.insert(0,str(p))
from n6_spectator_chart_transition_certificate import theta_operator
T=theta_operator(); I=np.eye(12,dtype=np.int64)
assert not np.count_nonzero((T-I)@(T-I)@(T+I))
assert np.count_nonzero((T-I)@(T-I))
assert np.count_nonzero((T-I)@(T+I))
assert np.count_nonzero(T-I) and np.count_nonzero(T+I)
print('theta dimension: 12')
print('exact minimal polynomial: (t-1)^2(t+1)')
print('No floating-point rank calculation used.')
print('ALL CHECKS PASSED')
