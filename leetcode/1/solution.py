# brute force

# time complexity: O(n^2)
# space complexity: O(1)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]




# using hash table

# time complexity: O(n)
# space complexity: O(n)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target - nums[i]], i]
            seen[nums[i]] = i


# another attempt

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_positions = {}
        for i, num in enumerate(nums):
            if target - num in num_positions:
                return [num_positions[target - num], i]
            num_positions[num] = i