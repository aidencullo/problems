import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
    ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),
])
def test_solution(test_input, expected):
    s = Solution()
    s.setZeroes(test_input)
    assert test_input == expected
