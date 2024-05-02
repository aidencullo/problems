from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            k = (l + r) // 2
            mid = nums[k]
            upper = nums[r]

            if mid < upper:
                r = k
            else:
                l = k + 1

        return nums[l]
