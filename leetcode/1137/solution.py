class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1

        a = 0
        b = 1
        c = 1

        i = 2
        while i < n:
            c, a, b =  a + b + c, b, c
            i += 1
        return c
