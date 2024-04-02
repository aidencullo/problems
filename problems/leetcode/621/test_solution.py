import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((["A","A","A","B","B","B"], 2), 8),
    ]
)
def testSolution(test_input, expected):
    assert Solution().leastInterval(*test_input) == expected
    
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
