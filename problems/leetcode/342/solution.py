import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        if not 2 ** 32 % n == 0:
            return False
        return math.log(n, 2) % 2 == 0
