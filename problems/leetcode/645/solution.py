import math
import itertools
import operator
from functools import reduce

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        normal_and_nums = itertools.chain(range(1, n + 1), nums)
        duplicate_xor_missing = reduce(operator.xor, normal_and_nums)
        k = math.floor(math.log(duplicate_xor_missing, 2))
        msb = 1 << k
        bit_set, bit_unset = 0, 0
        normal_and_nums = itertools.chain(range(1, n + 1), nums)
        for num in normal_and_nums:
            if num & msb:
                bit_set ^= num
            else:
                bit_unset ^= num
        if bit_set in nums:
            return [bit_set, bit_unset]
        return [bit_unset, bit_set]
