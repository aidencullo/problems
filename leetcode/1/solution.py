# # Solution 1
# from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:        
#         hash_map = {}
#         for index, num in enumerate(nums):
#             if target - num in hash_map:
#                 return [hash_map[target - num], index]
#             hash_map[num] = index



# Solution 2
from typing import Optional, List, Tuple
import numpy as np

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_idx = np.argsort(nums)
        nums.sort()

        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] + nums[r] == target:
                return [sorted_idx[l], sorted_idx[r]]

            if nums[l] + nums[r] > target:
                r -= 1

            if nums[l] + nums[r] < target:
                l += 1
