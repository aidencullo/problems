from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            seen = set()
            target = -nums[i]
            for j in range(len(nums)-1, i, -1):
                if target - nums[j] in seen:
                    res.append([nums[i], nums[j], target-nums[j]])
                seen.add(nums[j])
        return res
