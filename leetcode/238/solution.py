from operator import mul
from functools import reduce
from typing import Optional, List, Tuple

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        result = [1] * len(nums)
        for i, num in enumerate(nums):
            result[i] *= product
            product *= nums[i]
        product = 1
        for i, num in enumerate(nums):
            result[-(i+1)] *= product
            product *= nums[-(i+1)]
        return result
