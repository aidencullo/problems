from typing import Optional, List, Tuple

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:

            k = (l + r) // 2

            if target == nums[k]:
                return k

            if nums[l] <= nums[k]:
                if nums[l] <= target and target <= nums[k]:
                    r = k - 1
                else:
                    l = k + 1
            else:
                if nums[l] <= target or target <= nums[k]:
                    r = k - 1
                else:
                    l = k + 1
        return -1
