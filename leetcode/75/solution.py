# time: O(nlogn)
# space: O(logn)

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def qs(nums, low, high):
            if low < high:
                p = partition(nums, low, high)
                qs(nums, low, p - 1)
                qs(nums, p + 1, high)
        
        def partition(nums, low, high):
            pivot = nums[high]
            i = low - 1
            for j in range(low, high):
                if nums[j] < pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1], nums[high] = nums[high], nums[i + 1]
            return i + 1
        
        qs(nums, 0, len(nums) - 1)
