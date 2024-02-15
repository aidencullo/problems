from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        table = Counter(s)
        total = 0
        for freq in table.values():
            total += freq - (freq % 2)
        total += any(freq for freq in table.values() if freq % 2 == 1)
        return total
