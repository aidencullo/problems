from math import comb

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        n = m + n - 2
        r = m - 1
        return comb(n, r)
