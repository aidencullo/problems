# ## Solution 1
# # O(n^2) time O(n) space
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         longest_str = ""
#         longest_str_len = 0

#         for c in s:
#             if c not in longest_str:
#                 longest_str += c
#             else:
#                 while longest_str:
#                     longest_str = longest_str[1:]
#                     if c not in longest_str:
#                         longest_str += c
#                         break
#             longest_str_len = max(len(longest_str), longest_str_len)
#         return longest_str_len





## Solution 2
"""
based off answers I saw
"""

from collections import defaultdict

# O(n) time O(1) space
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        start = -1
        seen = defaultdict(lambda:-1)

        for i, c in enumerate(s):
            start = max(start, seen[c])
            result = max(result, i - start)
            seen[c] = i

        return result
