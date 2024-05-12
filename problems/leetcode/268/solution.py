class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total_nums = set([i for i in range(n + 1)])
        for num in nums:
            total_nums.remove(num)
        return list(total_nums)[0]
