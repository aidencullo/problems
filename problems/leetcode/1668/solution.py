class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        l, r = 0, n
        while l <= r:
            k = (l + r) // 2
            if word * k in sequence:
                l = k + 1
            else:
                r = k - 1
        return r
