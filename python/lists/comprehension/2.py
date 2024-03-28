"""
extend with list comprehension
"""

L1 = [1, 2, 3]
L2 = [4, 5, 6]
expected = list(range(1, 7))

# With itertools.chain
from itertools import chain

L3 = list(chain(L1, L2))

# With list comprehension
L3 = [item for sublist in [L1, L2] for item in sublist]

# test
assert L3 == expected
