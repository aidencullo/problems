# time: O(n^2)
# space: O(n^2

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(target, nums):
            seen = set()
            for i, num in enumerate(nums):
                if i < len(nums) - 1 and nums[i] == nums[i+1]:
                    seen.add(num)
                    continue
                if target - num in seen:
                    res.append([-target, target-num, num])
                seen.add(num)
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            twoSum(-num, nums[i+1:])
        return res
