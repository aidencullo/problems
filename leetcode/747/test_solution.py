import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (([3, 6, 1, 0],), 1),
    (([1, 2, 3, 4],), -1),
])
def test_solution(test_input, expected):
    assert Solution().dominantIndex(*test_input) == expected
