class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        return reduce(operator.xor, nums, 0)
