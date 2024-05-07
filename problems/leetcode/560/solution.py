from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0] * (n + 1) for __ in range(k + 1)]
        dp[0] = [1] * (n + 1)
        for i in range(1, k + 1):
            for j in range(1, n + 1):
                if nums[j-1] <= i:
                    dp[i][j] = dp[i - nums[j-1]][j-1]
        return sum(dp[-1])
