import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([-1,1,2,3,1], 2), 3),
        (([-6,2,5,-2,-7,-1,3], -2), 10),
        (([6,-1,7,4,2,3], 8), 8),
        (([-1,3,8,3], 2), 0),
        (([-10,-6,-8,-9,6,6,-6,-6,-3], -2), 25),
    ],
)
def test_solution(test_input, expected):
    assert Solution().countPairs(*test_input) == expected
