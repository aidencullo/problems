import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (('42',), 42),
        (('     -42',), -42),
        (('4193 with words',), 4193),
        (('words and 987',), 0),
        (('-91283472332',), -2147483648),
        (('3.14159',), 3),
    ]
)
def testSolution(test_input, expected):
    assert Solution().myAtoi(*test_input) == expected
