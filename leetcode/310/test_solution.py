import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((4, [[1,0],[1,2],[1,3]], ), [1]),
        ((6, [[0,3],[1,3],[2,3],[4,3],[5,4]], ), [3,4]),
        ((1, [], ), [0]),
        ((2, [[0,1]], ), [0,1]),
    ]
)
def testSolution(test_input, expected):
    s = Solution()
    assert s.findMinHeightTrees(*test_input) == expected
    
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
