import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (('babad',), 'bab'),
        (('babab',), 'babab'),
        (('cbbd',), 'bb'),
        (("aacabdkacaa",), 'aca'),
    ]
)
def testSolution(test_input, expected):
    actual = Solution().longestPalindrome(*test_input)
    assert actual == expected

def compare_arrays(a, b):
    assert len(a) == len(b)
    for i in range(len(a)):
        assert a[i] == b[i]
