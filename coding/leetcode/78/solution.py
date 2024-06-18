from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subsets_helper(index, running) -> None:
            if index == len(nums):
                self.res.append(running)
                return
            subsets_helper(index + 1, running)
            subsets_helper(index + 1, [nums[index]] + running)
        self.res = []
        subsets_helper(0, [])
        return self.res
