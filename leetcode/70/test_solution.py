import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((2,), 2),
        ((3,), 3),
        ((1,), 1),
        ((0,), 0),
        ((4,), 5),
    ]
)
def testSolution(test_input, expected):
    assert Solution().climbStairs(*test_input) == expected
