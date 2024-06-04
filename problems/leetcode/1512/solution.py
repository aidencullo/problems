import math
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        nums_counter = Counter(nums)
        return sum(
            math.comb(count, 2)
            for count in nums_counter.values()
        )
