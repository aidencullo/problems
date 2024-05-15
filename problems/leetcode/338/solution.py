import math

class Solution:
    def countBits(self, n: int) -> list[int]:
        result = []
        for i in range(n + 1):
            count = 0
            while i:
                count += i % 2
                i //= 2
            result.append(count)
        return result
