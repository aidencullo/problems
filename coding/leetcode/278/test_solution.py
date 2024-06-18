import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (5, 4)
    ]
)
def testSolution(test_input, expected):
    assert Solution().firstBadVersion(test_input) == expected
