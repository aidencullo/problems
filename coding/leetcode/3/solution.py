class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        longest = 0
        left = 0
        for right, char in enumerate(s):
            if char in hash_set:
                while s[left] != char:
                    hash_set.remove(s[left])
                    left += 1
                left += 1
            hash_set.add(char)
            longest = max(longest, len(hash_set))
        return longest
        
