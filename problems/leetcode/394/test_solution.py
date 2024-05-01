import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (('3[a]2[bc]',), 'aaabcbc'),
        (('3[a2[c]]',), 'accaccacc'),
        (("2[abc]3[cd]ef",), 'abcabccdcdcdef'),
    ]
)
def testSolution(test_input, expected):
    assert Solution().decodeString(*test_input) == expected
