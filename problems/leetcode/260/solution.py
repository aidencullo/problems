import operator
from functools import reduce
import math


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor_sum = reduce(operator.xor, nums)
        k = int(math.log(xor_sum, 2)) if xor_sum > 0 else int(math.log(-xor_sum, 2))
        mask = 1 << k
        bit_set, bit_unset = 0, 0
        for num in nums:
            if mask & num:
                bit_set ^= num
            else:
                bit_unset ^= num
        return [bit_set, bit_unset]
