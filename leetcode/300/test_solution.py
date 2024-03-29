import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([10,9,2,5,3,7,101,18],), 4),
        (([0,1,0,3,2,3],), 4),
        (([7,7,7,7,7,7,7],), 1),
    ]
)
def testSolution(test_input, expected):
    assert Solution().lengthOfLIS(*test_input) == expected

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
