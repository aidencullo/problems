# O(n) time complexity, O(n) space complexity

from typing import List

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = set()
        for i, x in enumerate(nums[:-1]):
            y = nums[i+1]
            two_sum = x + y
            if two_sum in sums:
                return True
            sums.add(two_sum)
        return False
