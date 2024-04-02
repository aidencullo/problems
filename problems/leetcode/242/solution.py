# 242. Valid Anagram
# Easy
# Topics
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.











# from collections import defaultdict

# # O(n log n) time O(n) space
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

# # O(n) time O(n) space
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s_dict = defaultdict(int)
#         for letter in s:
#             s_dict[letter] += 1
            
#         t_dict = defaultdict(int)
#         for letter in t:
#             t_dict[letter] += 1

#         return s_dict == t_dict

from collections import Counter

# O(n) time O(n) space
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
