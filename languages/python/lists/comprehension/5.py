"""
remomve dups
"""

import numpy as np
n = 1000
k = 100
L = np.random.randint(k, size=(n, )).tolist()
expected = np.unique(L).tolist()

# With list comprehension
hash_map = {}
L3 = [item for i, item in enumerate(L) if item not in L[:i]]
L3.sort()


# test
assert L3 == expected
