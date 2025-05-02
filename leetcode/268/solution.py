class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        from functools import reduce
        import operator

        return reduce(operator.xor, nums + list(range(n)))