import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (["cbaebabacd", "abc"], [0,6]),
        (["abab", "ab"], [0,1,2]),
        (["a", "a"], [0]),
        (["a", "b"], []),
        (["", "a"], []),
        (["a", ""], []),
        (["", ""], []),
        (["aa", "aa"], [0]),
        (["aa", "aaa"], []),
        (["aaa", "aa"], [0,1]),
        (["aaa", "aaa"], [0]),
        (["aaaaaaaaa", "aaaaaaaaaaaaa"], []),
    ]
)
def testSolution(test_input, expected):
    s = Solution()
    assert s.findAnagrams(*test_input) == expected

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
