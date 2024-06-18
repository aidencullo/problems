from typing import Optional, List, Tuple

# O(n) time O(1) space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = float('-inf')
        runningMaxSub = float('-inf')
        for num in nums:
            if  num > runningMaxSub and runningMaxSub < 0:
                runningMaxSub = 0
            runningMaxSub += num
            maxSub = max(maxSub, runningMaxSub)
        return maxSub
