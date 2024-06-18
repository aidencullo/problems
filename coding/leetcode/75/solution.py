from collections import defaultdict
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        i = 0
        for num in range(3):
            for _ in range(d[num]):
                nums[i] = num
                i += 1
