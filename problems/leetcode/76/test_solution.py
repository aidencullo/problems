import pytest
from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (("ADOBECODEBANC", "ABC"), "BANC"),
    (("a", "a"), "a"),
    (("a", "aa"), ""),
    (("a", "b"), ""),
    (("aa", "aa"), "aa"),
    (("aaaaaaaaaaaabbbbbcdd", "abcdd"), "abbbbbcdd"),
])
def test_solution(test_input, expected):
    sol = Solution()
    assert sol.minWindow(*test_input) == expected
