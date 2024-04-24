import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([1, 1, 1, 1, 1], 3), 5),
    (([1], 1), 1),
    (([10,32,4,24,7,35,42,13,45,4,0,47,40,48,23,45,31,9,11,20], 30), 6116),
])
def test_solution(test_input, expected):
    sol = Solution()
    assert sol.findTargetSumWays(*test_input) == expected
