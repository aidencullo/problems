class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(x for i, x in enumerate(nums) if i % 2 == 0)
