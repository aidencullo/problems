import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([[1,3],[-2,2]], 1), [[-2,2]]),
        (([[3,3],[5,-1],[-2,4]], 2), [[3,3],[-2,4]]),
    ]
)
def testSolution(test_input, expected):
    assert Solution().kClosest(*test_input) == expected
