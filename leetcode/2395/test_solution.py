import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([4,2,4],), True),
        (([4,4],), False),
        (([4,2],), False),
        (([1,2,3],), False),
        (([0,0,0,0],), True),
        (([0,0,0],), True),
        (([0,0],), False),
        (([1,2,3,4],), False),
        (([1,2,3,4,5],), False),
    ]
)
def testSolution(test_input, expected):
    assert Solution().findSubarrays(*test_input) == expected
