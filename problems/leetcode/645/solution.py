class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        normal_sum = n * (n + 1) // 2
        missing = normal_sum - sum(set(nums))
        doubled = sum(nums) - sum(set(nums))
        return [doubled, missing]
