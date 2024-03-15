import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([1,2,3,4],), [24,12,8,6]),
    ]
)
def testSolution(test_input, expected):
    assert Solution().productExceptSelf(*test_input) == expected
