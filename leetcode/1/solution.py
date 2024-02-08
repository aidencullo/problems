from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        hash_map = {}
        for index, num in enumerate(nums):
            try:
                return [hash_map[target - num], index]
            except KeyError:
                hash_map[num] = index
                
