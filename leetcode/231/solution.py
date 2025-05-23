class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        while n > 1:
            n /= 2
        return n == 1
