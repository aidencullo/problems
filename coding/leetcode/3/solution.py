class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        longest = 0
        left = 0
        for right, char in enumerate(s):
            if char in hash_set:
                while char not in hash_set:
                    hash_set.add(char)
        return longest
        
