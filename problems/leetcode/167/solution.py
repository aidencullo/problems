# time: O(nlogn)
# space: O(1)

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            l, r = i+1, len(numbers)-1
            complement = target - num
            while l <= r:
                k = (l + r) // 2
                middle = numbers[k]
                if middle < complement:
                    l = k + 1
                elif middle > complement:
                    r = k - 1
                else:
                    return [i+1, k+1]
                
