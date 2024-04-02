import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (("23",), ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        (("",), []),
        (("2",), ["a","b","c"]),
    ]
)
def testSolution(test_input, expected):
    actual = Solution().letterCombinations(*test_input)
    compare_arrays(actual, expected)

def compare_arrays(a, b):
    assert len(a) == len(b)
    for i in range(len(a)):
        assert a[i] == b[i]

def compare_trees(a, b):
    assert (a is None) == (b is None)
    if a is None:
        return
    assert a.val == b.val
    compare_trees(a.left, b.left)
    compare_trees(a.right, b.right)
