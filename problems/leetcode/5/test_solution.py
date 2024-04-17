import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (("babad",), "bab"),
    (("cbbd",), "bb"),
    (("a",), "a"),
    (("ac",), "a"),
    (("bb",), "bb"),
    (("ccc",), "ccc"),
    (("cccc",), "cccc"),
    (("a",), "a"),
])
def test_solution(test_input, expected):
    solution = Solution()
    assert solution.longestPalindrome(*test_input) == expected
