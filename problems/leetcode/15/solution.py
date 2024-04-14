# time O(n^2)
# space O(n^3)

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.twoSum(nums[i+1:], -num)
        return self.res

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] > target:
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                self.res.append([-target, nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                l += 1
                r -= 1
