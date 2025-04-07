class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        first = 1
        second = 2
        ways = 0
        for _ in range(2, n):
            ways = first + second
            first = second
            second = ways
        return ways
