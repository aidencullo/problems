import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([3,2,3],), 3),
        (([2,2,1,1,2,2],), 2),
        (([2,2,1,1,2,2,2,2,2,2,1],), 2),
    ]
)
def testSolution(test_input, expected):
    assert Solution().majorityElement(*test_input) == expected
