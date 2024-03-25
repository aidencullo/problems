from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subsets_helper(running, index) -> List[List[int]]:
            if index == len(nums):
                res.append(running)
                return
            subsets_helper(running + [nums[index]], index + 1)
            subsets_helper(running, index + 1)
        res = []
        subsets_helper([], 0)
        res.sort()
        return res
