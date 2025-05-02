class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums = set(nums)
        counting = set(range(n + 1))
        missing = counting - nums
        return missing.pop()