# sliding window

# time: O(n)
# space: O(1)

from typing import List
import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length_of_nums = len(nums)
        running_sum = 0
        min_len = length_of_nums + 1
        left = 0
        for index, num in enumerate(nums):
            running_sum += num
            while running_sum >= target:
                min_len = min(min_len, index-left+1)
                running_sum -= nums[left]
                left += 1
        return min_len if min_len <= length_of_nums else 0

# brute force

# time: O(n^2)
# space: O(1)

from typing import List
import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = math.inf
        for left in range(len(nums)):
            running_sum = 0
            for right in range(left, len(nums)):
                running_sum += nums[right]
                if running_sum >= target:
                    min_len = min(min_len, right-left+1)
        return min_len if min_len <= len(nums) else 0


# presum + bin search

# time: O(nlogn)
# space: O(n)

from typing import List
import numpy as np
import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sums = np.cumsum(nums)
        prefix_sum = 0
        min_len = math.inf
        for index, num in enumerate(nums):
            min_next_index = binary_search(prefix_sum + target, prefix_sums)
            if min_next_index != -1:
                min_len = min(min_len, min_next_index - index + 1)
            prefix_sum += num
        return min_len if min_len != math.inf else 0

def binary_search(target, prefix_sums):
    return binary_search_helper(target, prefix_sums, 0, len(prefix_sums) - 1)

def binary_search_helper(target, prefix_sums, lower, upper):
    if upper < lower:
        if lower == len(prefix_sums):
            return -1
        else:
            return lower
    middle_index = upper+lower // 2
    middle = prefix_sums[middle_index]
    if target < middle:
        return binary_search_helper(target, prefix_sums, lower, middle_index - 1)
    if target > middle:
        return binary_search_helper(target, prefix_sums, middle_index + 1, upper)
    return middle_index

