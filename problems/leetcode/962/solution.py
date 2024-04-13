# brute force

# time O(n^2)
# space O(1)

from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ramp = 0
        for i in range(len(nums)):
            for j in range(len(nums)-1, -1, -1):
                if nums[i] <= nums[j]:
                    ramp = max(ramp, j-i)
        return ramp
