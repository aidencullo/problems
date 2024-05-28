from collections import Counter

class Solution:
    def isSubsequence(self, word1: str, word2: str) -> bool:
        l, r = 0, 0
        n, m = len(word1), len(word2)
        while l < n and r < m:
            if word1[l] == word2[r]:
                l += 1
            r += 1
        return l == n
