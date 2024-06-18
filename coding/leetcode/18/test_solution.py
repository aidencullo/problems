import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([1, 0, -1, 0, -2, 2], 0), [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
    (([2, 2, 2, 2, 2], 8), [[2, 2, 2, 2]]),
])
def test_solution(test_input, expected):
    sol = Solution()
    assert sol.fourSum(*test_input) == expected
