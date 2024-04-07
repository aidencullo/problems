# time: O(n)
# space: O(1)

from typing import List
import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        running = 0
        min_len = math.inf
        lower = 0
        for index, num in enumerate(nums):
            running += num

            if running >= target:
                min_len = min(min_len, index-lower+1)
            while running >= target:
                running -= nums[lower]
                lower += 1
                if running >= target:
                    min_len = min(min_len, index-lower+1)
        return min_len
