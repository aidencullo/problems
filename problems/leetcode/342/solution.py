class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        while n > 3:
            n /= 4
        return n == 1
