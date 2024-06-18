import math

class Solution:
    def countBits(self, n: int) -> list[int]:
        result = [0] * (n + 1)
        for i in range(n + 1):
            k = int(math.log(i, 2)) if i > 0 else 0
            mask = 1 << k
            result[i] = result[(mask-1) & i] + ((mask & i) >> k)
        return result
