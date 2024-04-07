# time: O(n)
# space: O(1)

from typing import List
import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_arr = math.inf
        running = 0
        lower = 0
        for i, num in enumerate(nums):
            running += num
            if running >= target:
                min_arr = min(min_arr, i-lower+1)
            while running >= target:
                running -= nums[lower]
                lower += 1
                if running >= target:
                    min_arr = min(min_arr, i-lower+1)
        if min_arr == math.inf:
            return 0
        return min_arr
