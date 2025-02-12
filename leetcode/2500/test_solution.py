import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (([[1, 2, 4], [3, 3, 1]],), 8),
    (([[10]],), 10),
])
def test_solution(test_input, expected):
    assert Solution().deleteGreatestValue(*test_input) == expected
