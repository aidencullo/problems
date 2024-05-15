import math

class Solution:
    def countBits(self, n: int) -> list[int]:
        result = [0] * (n + 1)
        for i in range(n + 1):
            result[i] = result[i >> 1] + (i & 1)
        return result
