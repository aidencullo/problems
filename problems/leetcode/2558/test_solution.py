import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (([25, 64, 9, 4, 100], 4), 29),
    (([1, 1, 1, 1], 4), 4),
])
def test_solution(test_input, expected):
    assert Solution().pickGifts(*test_input) == expected
