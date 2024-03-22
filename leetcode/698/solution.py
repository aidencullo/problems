from functools import reduce
from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def canPartitionKSubsetsHelper(num_index: int, partitions) -> bool:
            if any(partition > sum(nums) // k for partition in partitions):
                return False
            if num_index == len(nums):
                return all(partition == partitions[0] for partition in partitions)
            num = nums[num_index]
            for bin in range(k):
                partitions[bin] += num
                if canPartitionKSubsetsHelper(num_index + 1, partitions):
                    return True
                partitions[bin] -= num
                if not partitions[bin]:
                    break
            return False
        nums.sort(reverse=True)
        return canPartitionKSubsetsHelper(0, [0] * k)
