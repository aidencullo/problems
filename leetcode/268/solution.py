class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums = set(nums)
        for el in range(n + 1):
            if el not in nums:
                return el