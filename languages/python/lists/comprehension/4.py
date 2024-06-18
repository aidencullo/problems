"""
build a nested list
"""

import numpy as np
n = 5
expected = np.ones((n, n, n)).tolist()


# code here
L3 = [[[1 for _ in range(n)] for _ in range(n)] for _ in range(n)]


# test
assert L3 == expected
