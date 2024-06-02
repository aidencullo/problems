import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    ([5,4,2,3], [3,2,5,4]),
    ([2,5], [5,2]),
])
def test_solution(test_input, expected):
    assert Solution().numberGame(test_input) == expected
