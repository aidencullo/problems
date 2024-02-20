from typing import List

class Solution:
    # O(log n) time O(n) space?
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target, 0)

    def helper(self, nums: List[int], target: int, start: int) -> int:
        if not nums:
            return -1
        mid = len(nums) // 2
        median = nums[mid]
        if target == median:
            return start + mid
        elif target > median:
            return self.helper(nums[mid+1:], target, mid + start + 1)
        else:
            return self.helper(nums[:mid], target, start)
