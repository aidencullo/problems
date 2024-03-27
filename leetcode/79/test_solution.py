import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"), True),
        (([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"), True),
        (([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"), False),
        (([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "A"), True),
        (([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCE"), True),
        (([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ECBA"), True),
        (([["a"]], "a"), True),
        (([["a","b"],["c","d"]], "cdba"), True),
        (([["a","b"],["c","d"]], "abcd"), False),
        (([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"), True),
    ]
)
def testSolution(test_input, expected):
    s = Solution()
    assert s.exist(*test_input) == expected

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
