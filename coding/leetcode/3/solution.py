class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = 0
        hash_set = {}
        longest = 0
        for right, char in enumerate(s):
            if char in hash_set:
                last = max(last, hash_set[char] + 1)
            hash_set[char] = right
            longest = max(longest, right - last + 1)
        return longest        
