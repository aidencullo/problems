import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([5, 2, 3, 10, 6, 8], 6, 10), 3),
    (([2, 5, 1, 3, 4], 5, 10), 3),
    (([9, 0, 9], 3, 9), 4),
    (([9, 7, 0, 3, 9, 8, 6, 5, 7, 6], 10, 31), 40),
])
def test_solution(test_input, expected):
    sol = Solution()
    assert sol.perfectSum(*test_input) == expected
