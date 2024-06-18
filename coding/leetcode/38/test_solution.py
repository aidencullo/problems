import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (1, '1'),
        (2, '11'),
        (3, '21'),
        (4, '1211'),
        (5, '111221'),
        (6, '312211'),
        (7, '13112221'),
        (8, '1113213211'),
        (9, '31131211131221'),
        (10, '13211311123113112211'),
        (11, '11131221133112132113212221'),
        (12, '3113112221232112111312211312113211'),
   ]
)
def testSolution(test_input, expected):
    s = Solution()
    assert s.countAndSay(test_input) == expected
    
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
