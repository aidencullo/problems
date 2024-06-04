import math
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        nums_counter = Counter(nums)
        return sum([math.comb(v, 2) for v in nums_counter.values() if v > 1])
