from typing import Optional, List, Tuple

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search_min(l, r):
            while l <= r:
                k = (l + r) // 2
                if nums[l] <= nums[k] and nums[k] <= nums[r]:
                    break
                if nums[k] > nums[k + 1]:
                    return k + 1
                if nums[l] > nums[k]:
                    r = k
                else:
                    l = k
            return 0

        def convert_index(index, start_index):
            return (start_index + index) % len(nums)
                    
        start_index = search_min(0, len(nums) - 1)
        
        l, r = 0, len(nums) - 1
        while l <= r:
            k = (l + r) // 2
            middle = nums[convert_index(k, start_index)]

            if target < middle:
                r = k - 1
            elif target > middle:
                l = k + 1
            else:
                return convert_index(k, start_index)
        return -1
