class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        from functools import reduce
        import operator

        range_xor = reduce(operator.xor, range(n + 1))
        nums_xor = reduce(operator.xor, nums)
        return nums_xor ^ range_xor