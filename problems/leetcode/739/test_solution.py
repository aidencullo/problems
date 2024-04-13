import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([73, 74, 75, 71, 69, 72, 76, 73],), [1, 1, 4, 2, 1, 1, 0, 0]),
    (([30, 40, 50, 60],), [1, 1, 1, 0]),
    (([30, 60, 90],), [1, 1, 0]),
])
def test_solution(test_input, expected):
    sol = Solution()
    actual = sol.dailyTemperatures(*test_input)
    assert actual == expected
