from typing import List
from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i, remaining_sum):
            if remaining_sum == target and i == len(nums):
                return 1
            if i != len(nums):
                return dfs(i + 1, remaining_sum - nums[i]) + dfs(i + 1, remaining_sum + nums[i])
            return 0
        return dfs(0, 0)
