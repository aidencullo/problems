# time O(n)
# space O(n)

from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        ramp = 0
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                ramp = max(ramp, i - stack.pop())
        return ramp
