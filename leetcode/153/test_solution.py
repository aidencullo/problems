import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([3, 4, 5, 1, 2], ), 1),
    (([4, 5, 6, 7, 0, 1, 2], ), 0),
    (([11, 13, 15, 17], ), 11),
])
def test_solution(test_input, expected):
    sol = Solution()
    assert sol.findMin(*test_input) == expected
