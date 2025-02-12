import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (([1, 2, 1],), [1, 2, 1, 1, 2, 1]),
    (([1, 3, 2, 1],), [1, 3, 2, 1, 1, 3, 2, 1]),
])
def test_solution(test_input, expected):
    assert Solution().getConcatenation(*test_input) == expected
