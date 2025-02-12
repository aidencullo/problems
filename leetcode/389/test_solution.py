import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (("abcd", "abcde"), "e"),
    (("", "y"), "y"),
    (("a", "aa"), "a"),
])
def test_solution(test_input, expected):
    assert Solution().findTheDifference(*test_input) == expected
