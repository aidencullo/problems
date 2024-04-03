"""
insert using list comprehension
"""

import numpy as np
k = 10
n = 20
L = np.random.randint(k, size=(n, )).tolist()
m = len(L)//2
expected = L[:m] + [0] + L[m:]

# With list comprehension
L3 = [L[i] if i < m else 0 if i == m else L[i-1] for i in range(n + 1)]
# or
L3 = [el for sublist in [L[:m], [0], L[m:]] for el in sublist]

# test
assert L3 == expected
