class Solution:
    def climbStairs(self, n: int) -> int:
        dp = []
        dp.append(1)
        dp.append(1)
        for i in range(1, n):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]
