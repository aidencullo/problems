class Solution:
    def minimumMoves(self, s: str) -> int:
        n = len(s)
        i = 0
        total = 0
        while i < n:
            if s[i] == 'X':
                total += 1
                i += 3
            else:
                i += 1
        return total