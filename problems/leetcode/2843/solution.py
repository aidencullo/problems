import math


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def isSymmetric(n):
            digits = int(math.log10(n)) + 1
            if digits % 2 == 1:
                return False
            l = str(n)[:digits // 2]
            r = str(n)[digits // 2:]
            l_sum = sum(map(int, l))
            r_sum = sum(map(int, r))
            return l_sum == r_sum

        return sum(
            1
            for i in range(low, high + 1)
            if isSymmetric(i)
            )
