from functools import reduce
import operator

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return reduce(operator.xor, nums)
