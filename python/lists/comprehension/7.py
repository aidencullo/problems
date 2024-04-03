"""
remove using list comprehension
"""

n = 20
L = list(range(n))
expected = L[:]
expected.remove(11)

# With list comprehension
L3 = [el for el in L if el != 11]

# test
assert L3 == expected
