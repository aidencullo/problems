import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
    (([3, 3], 6), [0, 1]),
])
def test_solution(test_input, expected):
    sol = Solution()
    assert sol.twoSum(*test_input) == expected
