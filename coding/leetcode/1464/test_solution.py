import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (([3, 4, 5, 2],), 12),
    (([1, 5, 4, 5],), 16),
    (([3, 7],), 12),
])
def test_solution(test_input, expected):
    assert Solution().maxProduct(*test_input) == expected
