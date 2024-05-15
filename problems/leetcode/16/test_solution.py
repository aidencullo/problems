import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([-1,2,1,-4], 1), 2),
        (([0,0,0], 1), 0),
        (([4,0,5,-5,3,3,0,-4,-5], -2), -2),
    ],
)
def test_solution(test_input, expected):
    assert Solution().threeSumClosest(*test_input) == expected
