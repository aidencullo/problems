# sliding window

# time: O(n)
# space: O(1)

from typing import List
import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        running_sum = 0
        min_len = float('inf')
        left = 0
        for index, num in enumerate(nums):
            running_sum += num
            while running_sum >= target:
                min_len = min(min_len, index-left+1)
                running_sum -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0

# brute force

# time: O(n^3)
# space: O(n)

from typing import List
import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = math.inf
        for left, __ in enumerate(nums):
            for right, __ in enumerate(nums):
                if sum(nums[left: right+1]) >= target:
                    min_len = min(min_len, right-left+1)
        return min_len if min_len <= len(nums) else 0
