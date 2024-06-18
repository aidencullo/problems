import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (([0, 2, 1, 5, 3, 4],), [0, 1, 2, 4, 5, 3]),
    (([5, 0, 1, 2, 3, 4],), [4, 5, 0, 1, 2, 3]),
])
def test_solution(test_input, expected):
    assert Solution().buildArray(*test_input) == expected
