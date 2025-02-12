class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        n = len(s)
        low, high = 0, n
        res = [0] * (n + 1)
        for i, char in enumerate(s):
            if char == 'D':
                res[i] = high
                high -= 1
            if char == 'I':
                res[i] = low
                low += 1
        res[-1] = low
        return res
