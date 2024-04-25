from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(numbers)):
            if target - numbers[i] in hash_map:
                return [hash_map[target - numbers[i]] + 1, i + 1]
            hash_map[numbers[i]] = i
