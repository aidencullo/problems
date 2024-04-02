import pytest

from solution import Solution
"""
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (('abcabcbb',), 3),
        (('bbbb',), 1),
        (('pwwkew',), 3),
    ]
)
def testSolution(test_input, expected):
    assert Solution().lengthOfLongestSubstring(*test_input) == expected
