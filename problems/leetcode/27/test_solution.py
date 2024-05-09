import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([3, 2, 2, 3], 3), 2),
    (([0, 1, 2, 2, 3, 0, 4, 2], 2), 5),
    (([0, 1, 2, 2, 3, 0, 4, 2], 3), 7),
    (([0, 1, 2, 2, 3, 0, 4, 2], 4), 7),
])
def test_solution(test_input, expected):
    assert Solution().removeElement(*test_input) == expected
