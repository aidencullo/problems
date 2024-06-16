# test_solution.py

import pytest
from solution import Solution

@pytest.mark.parametrize("input_str, expected_output", [
    ("leEeetcode", "leetcode"),
    ("abBAcC", ""),
    ("s", "s"),
    ("", ""),
    ("aA", ""),
    ("Aa", ""),
    ("abcCBA", ""),
    ("AaBbCcDd", ""),
    ("dabBAcd", "dcd"),
    ("aabAAB", "aabAAB")
])
def test_makeGood(input_str, expected_output):
    solution = Solution()
    assert solution.makeGood(input_str) == expected_output
