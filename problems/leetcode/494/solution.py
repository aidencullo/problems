from typing import List
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for target_sum in range(1, target + 1):
            for num in nums:
                dp[target_sum - num]
