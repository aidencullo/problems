# dp

# time complexity: O(2^n)
# space complexity: O(2^n)

from typing import List
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            new_dp = defaultdict(int)
            for running in dp:
                new_dp[running + num] += dp[running]
                new_dp[running - num] += dp[running]
            dp = new_dp
        return dp[target]
