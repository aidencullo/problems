import math

class Solution:
    def countBits(self, n: int) -> list[int]:
        result = []
        k = int(math.log(n, 2)) if n > 0 else 0
        for i in range(n + 1):
            result.append(sum(i >> j & 1 for j in range(k + 1)))
        return result
