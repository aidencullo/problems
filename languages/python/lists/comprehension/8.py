"""
map using list comprehension
"""


n = 20
L = list(range(n))
expected = list(map(lambda x: x * 2, L))


# With list comprehension
L3 = [el * 2 for el in L]


# test
assert L3 == expected
