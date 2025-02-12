import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (([2, 7, 4, 1, 8, 1],), 1),
    (([1],), 1),
])
def test_solution(test_input, expected):
    assert Solution().lastStoneWeight(*test_input) == expected
