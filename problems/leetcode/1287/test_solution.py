import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (([1, 2, 2, 6, 6, 6, 6, 7, 10],), 6),
    (([1, 1],), 1),
])
def test_solution(test_input, expected):
    assert Solution().findSpecialInteger(*test_input) == expected
