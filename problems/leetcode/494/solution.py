from typing import List
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, running):
            if i == len(nums) and target == running:
                return 1
            if i == len(nums):
                return 0

            if (i, running) in self.memo:
                return self.memo[(i, running)]
            add = dfs(i + 1, running + nums[i])
            sub = dfs(i + 1, running - nums[i])
            self.memo[(i, running)] = add + sub
            return add + sub

        self.memo = defaultdict(int)
        return dfs(0, 0)
