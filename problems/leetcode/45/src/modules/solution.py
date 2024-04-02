import sys

class Solution:
    def jump(self, nums: list[int]) -> int:
        nlen = len(nums)
        end = nums[0]
        max_reach = nums[0]
        jump = 1
        if nlen == 1:
            return 0
        for i in range(1, nlen-1):
            max_reach = max(max_reach, i+nums[i])
            if i == end:
                jump = jump + 1
                end = max_reach
        return jump
