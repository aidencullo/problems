class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 1
        while k*word in sequence:
            k += 1
        return k - 1
