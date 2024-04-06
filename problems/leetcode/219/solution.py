# time: O(n)
# space: O(n)

from typing import List
import math

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = {}
        for i, num in enumerate(nums):
            if num in hash_table:
                if math.fabs(hash_table[num] - i) <= k:
                    return True
            hash_table.update({num: i})
        return False
