import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([-1,1,2,3,1], 2), 3),
        (([-6,2,5,-2,-7,-1,3], -2), 10),
    ],
)
def test_solution(test_input, expected):
    assert Solution().countPairs(*test_input) == expected
