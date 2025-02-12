import operator
from functools import reduce

class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        return reduce(operator.or_, nums) * 2 ** (len(nums) - 1)
