from typing import List
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        n = len(nums)
        dp = {0: 1}
        for i in range(1, n + 1):
            new_dp = defaultdict(int)
            for key in dp:
                new_dp[key + nums[i-1]] += dp[key]
                new_dp[key - nums[i-1]] += dp[key]
            dp = new_dp
        return dp[target]
                
