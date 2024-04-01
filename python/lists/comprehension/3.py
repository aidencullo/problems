"""
append with list comprehension
"""

L1 = [1, 2, 3]
L2 = [4]
expected = L1 + L2

# With itertools.chain
from itertools import chain

L3 = list(chain(L1, L2))

# With list comprehension
L3 = [item for sublist in [L1, L2] for item in sublist]

# With extend
L3 = L1[:]
L3.extend(L2)


# test
assert L3 == expected
