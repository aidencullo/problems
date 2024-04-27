from typing import List
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        n = len(nums)
        dp = [defaultdict(int) for __ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for k in range(-total, total + 1):
                dp[i][k] += dp[i-1][k + nums[i-1]]
                dp[i][k] += dp[i-1][k - nums[i-1]]
        return dp[-1][target]
                
