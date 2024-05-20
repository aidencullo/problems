class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = cost[:] + [0, 0]
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i] + min(dp[i + 1], dp[i + 2])
        return min(dp[0], dp[1])
            
