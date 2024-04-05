import pytest
from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (["abcde", "ace"], 3),
    (["abc", "abc"], 3),
    (["abc", "def"], 0),
    (["abc", ""], 0),
    (["", "abc"], 0),
    (["", ""], 0),
    ((["bsbininm", "jmjkbkjkv"], 1)),
])
def test_solution(test_input, expected):
    assert Solution().longestCommonSubsequence(*test_input) == expected
