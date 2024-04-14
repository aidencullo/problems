from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(nums: List[int], target: int, ):
            if not nums:
                if target == 0:
                    
            helper(nums[1:], target - nums[0], nums[0])
            helper(nums[1:], target)
        self.res = []
        helper(nums, target)
        return res
        
