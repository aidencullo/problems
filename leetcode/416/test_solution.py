import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([1, 5, 11, 5],), True),
        (([1, 2, 3, 5],), False),
        (([1, 2, 5],), False), 
        ((([1,1,2,2]),), True),
    ]
)
def testSolution(test_input, expected):
    assert Solution().canPartition(*test_input) == expected
