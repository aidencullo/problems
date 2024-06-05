from functools import reduce


class Solution:
    def duplicateNumbersXOR(self, nums: list[int]) -> int:
        single = reduce(lambda x, y: x ^ y, nums)
        nums_set = set(nums)
        double = reduce(lambda x, y: x ^ y, nums_set) ^ single
        return double
