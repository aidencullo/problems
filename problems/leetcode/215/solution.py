# time (avg) O(n), O(n^2) worst case
# space O(lgn)

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(nums, start, end):
            pivot = nums[end]
            p = start
            for i in range(start, end):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[end], nums[p] = nums[p], nums[end]
            if k < p:
                return quickSelect(nums, start, p-1)
            if k > p:
                return quickSelect(nums, p+1, end)
            return nums[p]

        k = len(nums) - k
        return quickSelect(nums, 0, len(nums) - 1)
