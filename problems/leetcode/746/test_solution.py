import pytest
from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (([10, 15, 20],), 15),
    (([1, 100, 1, 1, 1, 100, 1, 1, 100, 1],), 6),
    (([0, 0, 0, 0],), 0),
])
def test_solution(test_input, expected):
    assert Solution().minCostClimbingStairs(*test_input) == expected
