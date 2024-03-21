# time: O(2^n)

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def canPartitionHelper(l, r, i):
            if i == len(nums):
                return l == r
            return (canPartitionHelper(l + nums[i], r, i + 1)
                    or canPartitionHelper(l, r + nums[i], i + 1))
        return canPartitionHelper(0, 0, 0)
