import math

class Solution:
    def isUgly(self, n: int) -> bool:
        prime_factors = [2, 3, 5]
        if n <= 0:
            return False
        for factor in prime_factors:
            while n % factor == 0:
                n //= factor
        return n == 1
