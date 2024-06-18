import pytest
from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (("leet**cod*e",), "lecoe"),
])
def test_solution(test_input, expected):
    assert Solution().removeStars(*test_input) == expected
